"""Провайдери за одним інтерфейсом.

Два види повторів розділені:
  * транспортні (timeout, 429, 5xx, 529) — tenacity з exponential backoff + Retry-After, тут;
  * валідаційні (JSON не пройшов схему) — один re-ask з текстом помилки, у runner.extract.
"""

from __future__ import annotations

import json
from typing import Any, Protocol

import httpx
from pydantic import BaseModel
from tenacity import (
    AsyncRetrying,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential_jitter,
)

TRANSIENT_STATUS = {408, 409, 425, 429, 500, 502, 503, 504, 529}


class Sampling(BaseModel):
    temperature: float
    top_p: float = 1.0


class RawResponse(BaseModel):
    text: str
    in_tokens: int = 0
    out_tokens: int = 0
    cache_read_tokens: int = 0
    cache_write_tokens: int = 0
    thinking_chars: int = 0        # має бути 0: міркування вимкнено
    ctx_truncated: bool = False    # Ollama тихо обрізає вхід понад num_ctx


class ProviderUnavailable(RuntimeError):
    """Провайдер не налаштований або недоступний — runner пропускає його з попередженням."""


class Provider(Protocol):
    name: str
    model: str

    async def check(self) -> None: ...
    async def complete(self, system: str, messages: list[dict[str, str]], schema: dict[str, Any],
                       sampling: Sampling, timeout_s: float) -> RawResponse: ...
    async def aclose(self) -> None: ...


def _transient(e: BaseException) -> bool:
    if isinstance(e, (httpx.TimeoutException, httpx.ConnectError, httpx.RemoteProtocolError)):
        return True
    return isinstance(e, httpx.HTTPStatusError) and e.response.status_code in TRANSIENT_STATUS


def _transient_local(e: BaseException) -> bool:
    """Локальна модель: ReadTimeout — не збій мережі, а надто довга генерація.
    Повтор того самого запиту при temperature 0 дасть те саме, тож не повторюємо."""
    return not isinstance(e, httpx.ReadTimeout) and _transient(e)


class _RetryAfterWait:
    """Exponential backoff з джитером, але не менше за Retry-After сервера."""

    def __init__(self) -> None:
        self._exp = wait_exponential_jitter(initial=1, max=30)

    def __call__(self, rs) -> float:  # noqa: ANN001
        base = self._exp(rs)
        exc = rs.outcome.exception() if rs.outcome else None
        if isinstance(exc, httpx.HTTPStatusError):
            ra = exc.response.headers.get("retry-after")
            if ra and ra.replace(".", "", 1).isdigit():
                return max(base, min(float(ra), 60.0))
        return base


async def _post_with_retry(client: httpx.AsyncClient, url: str, *, json_body: dict, headers: dict | None,
                           timeout_s: float, attempts: int, is_transient=_transient) -> dict:
    async for attempt in AsyncRetrying(retry=retry_if_exception(is_transient), stop=stop_after_attempt(attempts),
                                       wait=_RetryAfterWait(), reraise=True):
        with attempt:
            r = await client.post(url, json=json_body, headers=headers, timeout=timeout_s)
            if r.status_code >= 400:  # тіло відповіді — головна підказка (OpenRouter пише причину 404 саме там)
                raise httpx.HTTPStatusError(f"{r.status_code} {url}: {r.text[:600]}", request=r.request, response=r)
            return r.json()
    raise AssertionError("unreachable")


# --- Ollama -----------------------------------------------------------------

class OllamaProvider:
    name = "ollama"

    def __init__(self, model: str, base_url: str, num_ctx: int = 8192, think: bool | None = False, num_thread: int | None = None,
                 num_predict: int | None = None, transport_attempts: int = 4) -> None:
        self.model, self.num_ctx, self.think, self.attempts = model, num_ctx, think, transport_attempts
        self.num_thread, self.num_predict = num_thread, num_predict
        self.client = httpx.AsyncClient(base_url=base_url)

    async def check(self) -> None:
        try:
            r = await self.client.get("/api/tags", timeout=5)
            r.raise_for_status()
        except httpx.HTTPError as e:
            raise ProviderUnavailable(f"Ollama недоступна ({e!r}). Запусти `ollama serve`.") from e
        names = {m["name"] for m in r.json().get("models", [])}
        if self.model not in names and f"{self.model}:latest" not in names:
            raise ProviderUnavailable(f"Модель {self.model} не завантажена: `ollama pull {self.model}`")

    async def complete(self, system, messages, schema, sampling, timeout_s) -> RawResponse:
        d = await _post_with_retry(self.client, "/api/chat", headers=None, timeout_s=timeout_s,
                                   attempts=self.attempts, is_transient=_transient_local, json_body={
            "model": self.model,
            "stream": False,
            "format": schema,                 # constrained decoding за JSON Schema
            # qwen3.x / gemma: міркування вимикаємо явно; моделі без цього режиму відхиляють сам параметр
            **({"think": self.think} if self.think is not None else {}),
            "messages": [{"role": "system", "content": system}, *messages],
            "options": {"temperature": sampling.temperature, "top_p": sampling.top_p,
                        "num_ctx": self.num_ctx,
                        **({"num_thread": self.num_thread} if self.num_thread else {}),
                        **({"num_predict": self.num_predict} if self.num_predict else {})},
        })
        msg = d.get("message", {})
        in_tok = d.get("prompt_eval_count", 0) or 0
        return RawResponse(
            text=msg.get("content", ""),
            in_tokens=in_tok,
            out_tokens=d.get("eval_count", 0) or 0,
            thinking_chars=len(msg.get("thinking") or ""),
            # обрізаний вхід або вихід уперся в num_predict (done_reason == "length")
            ctx_truncated=in_tok >= self.num_ctx - 16 or d.get("done_reason") == "length",
        )

    async def aclose(self) -> None:
        await self.client.aclose()


# --- Anthropic (Messages API, forced tool use = гарантовано JSON за схемою) ---

class AnthropicProvider:
    name = "anthropic"
    TOOL = "save_receipt"

    def __init__(self, model: str, api_key: str | None, max_tokens: int = 4096,
                 send_top_p: bool = False, transport_attempts: int = 5, workspace_id: str | None = None) -> None:
        if not api_key:
            raise ProviderUnavailable("ANTHROPIC_API_KEY не задано в .env — платна модель пропускається.")
        self.model, self.max_tokens, self.send_top_p, self.attempts = model, max_tokens, send_top_p, transport_attempts
        headers = {"Authorization": f"Bearer {api_key}", "anthropic-version": "2023-06-01",
                   "content-type": "application/json"}
        if workspace_id:  # потрібен, лише якщо ключ не прив'язаний до workspace
            headers["anthropic-workspace-id"] = workspace_id
        self.client = httpx.AsyncClient(base_url="https://api.anthropic.com", headers=headers)

    async def check(self) -> None:
        return None

    async def complete(self, system, messages, schema, sampling, timeout_s) -> RawResponse:
        body: dict[str, Any] = {
            "model": self.model,
            "max_tokens": self.max_tokens,
            # Однаковий для всіх документів префікс (system + tool schema) -> prompt caching.
            # Кешується лише префікс понад мінімальну довжину моделі; коротший просто не кешується.
            "system": [{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
            "tools": [{"name": self.TOOL, "description": "Зберегти дані чека за схемою.",
                       "input_schema": schema}],
            "tool_choice": {"type": "tool", "name": self.TOOL},
            "messages": messages,
            "temperature": sampling.temperature,
        }
        # Частина моделей відхиляє temperature разом із top_p -> вмикається явно в конфігу.
        if self.send_top_p and sampling.top_p < 1.0:
            body["top_p"] = sampling.top_p
        d = await _post_with_retry(self.client, "/v1/messages", headers=None, timeout_s=timeout_s,
                                   attempts=self.attempts, json_body=body)
        tool = next((b for b in d.get("content", []) if b.get("type") == "tool_use"), None)
        text = json.dumps(tool["input"], ensure_ascii=False) if tool else \
            "".join(b.get("text", "") for b in d.get("content", []))
        u = d.get("usage", {})
        return RawResponse(text=text, in_tokens=u.get("input_tokens", 0), out_tokens=u.get("output_tokens", 0),
                           cache_read_tokens=u.get("cache_read_input_tokens", 0) or 0,
                           cache_write_tokens=u.get("cache_creation_input_tokens", 0) or 0,
                           ctx_truncated=d.get("stop_reason") == "max_tokens")

    async def aclose(self) -> None:
        await self.client.aclose()


# --- OpenAI-сумісний (OpenAI, OpenRouter, vLLM) --------------------------------

class OpenAICompatProvider:
    name = "openai"

    def __init__(self, model: str, api_key: str | None, base_url: str = "https://api.openai.com/v1",
                 transport_attempts: int = 5, key_name: str = "OPENAI_API_KEY",
                 extra_body: dict | None = None, schema_in_prompt: bool = False, max_tokens: int = 4096) -> None:
        if not api_key:
            raise ProviderUnavailable(f"{key_name} не задано в .env — платна модель пропускається.")
        self.model, self.attempts, self.extra_body = model, transport_attempts, extra_body or {}
        self.schema_in_prompt = schema_in_prompt
        # Без max_tokens OpenRouter резервує кредити під максимум моделі (65536) і повертає 402 на малому балансі
        self.max_tokens = max_tokens
        self.client = httpx.AsyncClient(base_url=base_url, headers={"Authorization": f"Bearer {api_key}"})

    def _schema_hint(self, schema: dict[str, Any]) -> str:
        # Якщо провайдер не підтримує response_format, схема в промпті — єдине, що задає формат
        if not self.schema_in_prompt:
            return ""
        return "\n\nJSON Schema відповіді:\n" + json.dumps(schema, ensure_ascii=False)

    async def check(self) -> None:
        return None

    async def complete(self, system, messages, schema, sampling, timeout_s) -> RawResponse:
        d = await _post_with_retry(self.client, "/chat/completions", headers=None, timeout_s=timeout_s,
                                   attempts=self.attempts, json_body={
            "model": self.model,
            "messages": [{"role": "system", "content": system + self._schema_hint(schema)}, *messages],
            # strict=false: схема має необов'язкові поля з default, strict їх не допускає
            "response_format": {"type": "json_schema",
                                "json_schema": {"name": "receipt", "schema": schema, "strict": False}},
            "temperature": sampling.temperature, "top_p": sampling.top_p,
            "max_tokens": self.max_tokens,
            **self.extra_body,
        })
        if "choices" not in d:  # OpenRouter повертає помилку провайдера з кодом 200
            raise RuntimeError(f"Немає choices у відповіді: {str(d.get('error', d))[:300]}")
        u = d.get("usage", {})
        cached = (u.get("prompt_tokens_details") or {}).get("cached_tokens", 0) or 0
        choice = d["choices"][0]
        return RawResponse(text=choice["message"].get("content") or "",
                           in_tokens=u.get("prompt_tokens", 0) - cached, out_tokens=u.get("completion_tokens", 0),
                           cache_read_tokens=cached, ctx_truncated=choice.get("finish_reason") == "length")

    async def aclose(self) -> None:
        await self.client.aclose()
