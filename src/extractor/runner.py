"""Прогін матриці експериментів: моделі × версії промпту × конфігурації семплінгу × повтори.

results/<model>__<prompt>__<sampling>/
    meta.json              модель, провайдер, prompt_version, prompt_sha, семплінг, git commit …
    calls.jsonl            кожен виклик: status, спроби, latency, токени, вартість, помилка
    outputs/<doc>__r<k>.json
"""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
import subprocess

import httpx
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ValidationError

from .config import CACHE, GOLDEN, PROMPTS, RESULTS, ROOT, TEXTS, Experiments, ModelCfg, Secrets, load_secrets
from .providers import (
    AnthropicProvider,
    OllamaProvider,
    OpenAICompatProvider,
    Provider,
    ProviderUnavailable,
    Sampling,
)
from .schema import Receipt, receipt_json_schema

SCHEMA = receipt_json_schema()
SCHEMA_SHA = hashlib.sha256(json.dumps(SCHEMA, sort_keys=True).encode()).hexdigest()[:12]
MAX_TEXT_CHARS = 20_000  # чек довший за це — майже напевно сміття OCR, а не чек


class CallResult(BaseModel):
    doc_id: str
    repeat: int
    status: Literal["ok", "failed"]
    first_try_valid: bool
    attempts: int
    latency_s: float
    in_tokens: int = 0
    out_tokens: int = 0
    cache_read_tokens: int = 0
    cache_write_tokens: int = 0
    thinking_chars: int = 0
    ctx_truncated: bool = False
    cost_usd: float = 0.0
    cache_hit: bool = False
    data: Receipt | None = None
    error: str | None = None
    last_raw: str | None = None


def user_message(text: str) -> str:
    # Текст чека — дані, не інструкції. Закривальний тег у самому тексті нейтралізуємо.
    safe = text.replace("</receipt_text>", "</receipt_text_>")
    return f"<receipt_text>\n{safe}\n</receipt_text>"


def cost(m: ModelCfg, r: CallResult) -> float:
    return (r.in_tokens * m.price_in + r.out_tokens * m.price_out
            + r.cache_read_tokens * m.price_cache_read + r.cache_write_tokens * m.price_cache_write) / 1e6


async def extract(p: Provider, doc_id: str, repeat: int, text: str, system: str, sampling: Sampling,
                  timeout_s: float, max_reask: int) -> CallResult:
    messages = [{"role": "user", "content": user_message(text[:MAX_TEXT_CHARS])}]
    t0 = time.perf_counter()
    acc = dict(in_tokens=0, out_tokens=0, cache_read_tokens=0, cache_write_tokens=0, thinking_chars=0)
    truncated, raw_text = False, None

    def done(**kw) -> CallResult:
        return CallResult(doc_id=doc_id, repeat=repeat, latency_s=round(time.perf_counter() - t0, 3),
                          ctx_truncated=truncated, last_raw=raw_text, **acc, **kw)

    for attempt in range(1, max_reask + 2):
        try:
            raw = await p.complete(system, messages, SCHEMA, sampling, timeout_s)
        except (httpx.HTTPError, TimeoutError, RuntimeError) as e:  # транспорт вичерпав retry, 4xx, помилка провайдера
            return done(status="failed", first_try_valid=False, attempts=attempt, error=f"transport: {e!r}"[:500])
        for k in acc:  # вартість і токени — по ВСІХ спробах, інакше re-ask «здешевлює» модель
            acc[k] += getattr(raw, k)
        truncated |= raw.ctx_truncated
        raw_text = raw.text
        try:
            data = Receipt.model_validate_json(raw.text)
        except ValidationError as ve:
            err = str(ve)[:1500]
            messages += [{"role": "assistant", "content": raw.text[:4000]},
                         {"role": "user", "content": f"JSON не пройшов валідацію схеми:\n{err}\n"
                                                     "Виправ лише помилкові поля і поверни повний JSON."}]
            last_err = err
            continue
        raw_text = None
        return done(status="ok", first_try_valid=attempt == 1, attempts=attempt, data=data)
    return done(status="failed", first_try_valid=False, attempts=attempt,
                error=f"validation: re-ask вичерпано: {last_err[:300]}")


def build_provider(m: ModelCfg, s: Secrets) -> Provider:
    if m.provider == "ollama":
        return OllamaProvider(m.model, m.base_url or s.ollama_base_url, num_ctx=m.num_ctx, think=m.think,
                              num_thread=m.num_thread, num_predict=m.num_predict)
    if m.provider == "anthropic":
        key = s.anthropic_api_key.get_secret_value() if s.anthropic_api_key else None
        return AnthropicProvider(m.model, key, send_top_p=m.send_top_p, workspace_id=s.anthropic_workspace_id)
    key_name = m.api_key_env or "OPENAI_API_KEY"
    secret = {"OPENAI_API_KEY": s.openai_api_key, "OPENROUTER_API_KEY": s.openrouter_api_key}.get(key_name)
    key = secret.get_secret_value() if secret else (os.getenv(key_name) or None)
    return OpenAICompatProvider(m.model, key, base_url=m.base_url or "https://api.openai.com/v1",
                                key_name=key_name, extra_body=m.extra_body, schema_in_prompt=m.schema_in_prompt)


def _git_commit() -> str:
    try:
        sha = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True,
                             text=True, check=True).stdout.strip()
        dirty = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True).stdout
        return sha + ("-dirty" if dirty.strip() else "")
    except Exception:
        return "nogit"


def _cache_key(m: ModelCfg, prompt_sha: str, sampling: Sampling, text: str, repeat: int) -> str:
    payload = [m.provider, m.model, m.base_url, m.schema_in_prompt, m.extra_body, m.think, m.num_ctx, prompt_sha, SCHEMA_SHA,
               sampling.model_dump(), text, repeat]
    if m.num_predict:  # лише якщо задано: не інвалідуємо кеш уже прогнаних моделей
        payload.append({"num_predict": m.num_predict})
    return hashlib.sha256(json.dumps(payload, ensure_ascii=False).encode()).hexdigest()


def load_docs() -> dict[str, str]:
    return {p.stem: p.read_text(encoding="utf-8") for p in sorted(TEXTS.glob("*.txt"))}


def load_prompt(version: str) -> tuple[str, str]:
    text = (PROMPTS / f"extract_{version}.md").read_text(encoding="utf-8")
    return text, hashlib.sha256(text.encode()).hexdigest()[:12]


async def run_model(mkey: str, m: ModelCfg, p: Provider, exp: Experiments, docs: dict[str, str],
                    prompts: list[str]) -> None:
    sem = asyncio.Semaphore(m.concurrency)
    CACHE.mkdir(parents=True, exist_ok=True)
    for pv in prompts:
        system, prompt_sha = load_prompt(pv)
        for skey, sc in exp.sampling.items():
            sampling = Sampling(temperature=sc.temperature, top_p=sc.top_p)
            run_id = f"{mkey}__{pv}__{skey}"
            out = RESULTS / run_id
            (out / "outputs").mkdir(parents=True, exist_ok=True)
            jobs = [(d, r) for d in docs for r in range(sc.repeats)]
            done_n = 0

            async def one(doc_id: str, rep: int) -> CallResult:
                nonlocal done_n
                cpath = CACHE / f"{_cache_key(m, prompt_sha, sampling, docs[doc_id], rep)}.json"
                if cpath.exists():
                    res = CallResult.model_validate_json(cpath.read_text(encoding="utf-8"))
                    # дублікати тексту (той самий чек двічі) ділять кеш — ідентифікатори беремо поточні
                    res.doc_id, res.repeat, res.cache_hit = doc_id, rep, True
                else:
                    async with sem:
                        res = await extract(p, doc_id, rep, docs[doc_id], system, sampling,
                                            m.timeout_s or exp.timeout_s, exp.max_reask)
                    res.cost_usd = round(cost(m, res), 8)
                    if not res.error or not res.error.startswith("transport"):  # транспортні збої не кешуємо
                        cpath.write_text(res.model_dump_json(), encoding="utf-8")
                done_n += 1
                mark = "✓" if res.status == "ok" else f"✗ {(res.error or '')[:160]}"
                print(f"  [{run_id}] {done_n}/{len(jobs)} {doc_id} r{rep} {mark}"
                      f"{' (cache)' if res.cache_hit else f' {res.latency_s:.1f}s'}", flush=True)
                return res

            print(f"\n▶ {run_id}: {len(jobs)} викликів")
            results = await asyncio.gather(*(one(d, r) for d, r in jobs))
            with (out / "calls.jsonl").open("w", encoding="utf-8") as f:
                for r in results:
                    f.write(r.model_dump_json(exclude={"data", "last_raw"}) + "\n")
                    (out / "outputs" / f"{r.doc_id}__r{r.repeat}.json").write_text(
                        r.model_dump_json(indent=2, include={"doc_id", "repeat", "status", "error", "data", "last_raw"}),
                        encoding="utf-8")
            meta = {
                "run_id": run_id, "model_key": mkey, "provider": m.provider, "model": m.model, "hardware": m.hardware,
                "base_url": m.base_url,
                "prompt_version": pv, "prompt_sha": prompt_sha, "schema_sha": SCHEMA_SHA,
                "sampling_key": skey, "sampling": sampling.model_dump(), "repeats": sc.repeats,
                "top_p_sent": m.provider != "anthropic" or (m.send_top_p and sampling.top_p < 1.0),
                "think": m.think if m.provider == "ollama" else None,
                "num_ctx": m.num_ctx if m.provider == "ollama" else None,
                "num_thread": m.num_thread if m.provider == "ollama" else None,
                "num_predict": m.num_predict if m.provider == "ollama" else None,
                "prices_per_1m": {"in": m.price_in, "out": m.price_out,
                                  "cache_read": m.price_cache_read, "cache_write": m.price_cache_write},
                "timeout_s": m.timeout_s or exp.timeout_s, "max_reask": exp.max_reask, "n_docs": len(docs),
                "git_commit": _git_commit(), "finished_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "python": sys.version.split()[0],
            }
            (out / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")


async def run_all(exp: Experiments, only_models: list[str] | None = None,
                  only_sampling: list[str] | None = None, golden_only: bool = False,
                  only_prompts: list[str] | None = None) -> None:
    secrets, docs = load_secrets(), load_docs()
    if not docs:
        print(f"⚠ Немає текстів у {TEXTS.relative_to(ROOT)} — прогін пропущено, звіт збирається з results/.")
        return
    if golden_only:  # стохастичні повтори повільної локальної моделі — лише там, де їх є з чим порівняти
        docs = {k: v for k, v in docs.items() if (GOLDEN / f"{k}.json").exists()}
    if only_sampling:
        exp = exp.model_copy(update={"sampling": {k: v for k, v in exp.sampling.items() if k in only_sampling}})
    prompts = only_prompts or exp.prompts
    for mkey, m in exp.models.items():
        if only_models and mkey not in only_models:
            continue
        try:
            p = build_provider(m, secrets)
            await p.check()
        except ProviderUnavailable as e:
            print(f"⚠ {mkey}: {e} Використовую вже наявні results/.")
            continue
        try:
            await run_model(mkey, m, p, exp, docs, prompts)
        finally:
            await p.aclose()
