from __future__ import annotations

import os
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, Field, SecretStr

from .providers import Sampling

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
TEXTS = DATA / "texts"
GOLDEN = DATA / "golden"
PROMPTS = ROOT / "prompts"
RESULTS = ROOT / "results"
CACHE = ROOT / ".cache" / "calls"


class ModelCfg(BaseModel):
    provider: Literal["ollama", "anthropic", "openai"]
    model: str
    # $ за 1M токенів; для локальної моделі 0 — її ціна рахується часом
    price_in: float = 0.0
    price_out: float = 0.0
    price_cache_read: float = 0.0
    price_cache_write: float = 0.0
    num_ctx: int = 8192
    think: bool | None = False   # None — не передавати зовсім (моделі без режиму міркування)
    num_thread: int | None = None  # Ollama: скільки ядер CPU брати; None — рішення Ollama
    num_predict: int | None = None  # Ollama: стеля вихідних токенів; зупиняє модель, що зациклилась у JSON
    timeout_s: float | None = None  # перекриває загальний timeout_s (повільна модель на CPU)
    send_top_p: bool = False
    base_url: str | None = None
    api_key_env: str | None = None   # з якої змінної .env брати ключ (для openai-сумісних: OpenRouter тощо)
    schema_in_prompt: bool = False   # дублювати JSON Schema в system-промпті (коли response_format не підтримано)
    extra_body: dict = Field(default_factory=dict)  # додаткові поля запиту, напр. налаштування маршрутизації OpenRouter
    hardware: str | None = None  # де фізично крутиться модель: для чесного «год / 1000»
    concurrency: int = 1


class SamplingCfg(Sampling):
    repeats: int = Field(1, ge=1)


class Experiments(BaseModel):
    models: dict[str, ModelCfg]
    prompts: list[str]
    sampling: dict[str, SamplingCfg]
    timeout_s: float = 90
    max_reask: int = 1


class Secrets(BaseModel):
    anthropic_api_key: SecretStr | None = None
    anthropic_workspace_id: str | None = None
    openai_api_key: SecretStr | None = None
    openrouter_api_key: SecretStr | None = None
    ollama_base_url: str = "http://localhost:11434"


def _load_dotenv(path: Path) -> None:
    """Мінімальний .env-парсер: зайвої залежності для трьох змінних не треба."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def load_secrets() -> Secrets:
    _load_dotenv(ROOT / ".env")
    return Secrets(
        anthropic_api_key=os.getenv("ANTHROPIC_API_KEY") or None,
        anthropic_workspace_id=os.getenv("ANTHROPIC_WORKSPACE_ID") or None,
        openai_api_key=os.getenv("OPENAI_API_KEY") or None,
        openrouter_api_key=os.getenv("OPENROUTER_API_KEY") or None,
        ollama_base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
    )


def load_experiments(path: Path | None = None) -> Experiments:
    path = path or ROOT / "configs" / "experiments.yaml"
    return Experiments.model_validate(yaml.safe_load(path.read_text(encoding="utf-8")))
