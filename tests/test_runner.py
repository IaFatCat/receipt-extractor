"""Runner на фейковому провайдері: re-ask, failed, облік токенів усіх спроб. Без мережі і без LLM."""

import asyncio
import json
from pathlib import Path

from extractor.providers import RawResponse, Sampling
from extractor.runner import extract

FX = Path(__file__).parent / "fixtures"
GOOD = json.dumps(json.loads((FX / "sample_golden.json").read_text(encoding="utf-8")), ensure_ascii=False)
S = Sampling(temperature=0)


class Fake:
    name, model = "fake", "fake"

    def __init__(self, replies):
        self.replies, self.calls = list(replies), []

    async def complete(self, system, messages, schema, sampling, timeout_s):
        self.calls.append(messages)
        r = self.replies.pop(0)
        if isinstance(r, Exception):
            raise r
        return RawResponse(text=r, in_tokens=100, out_tokens=50)


def _run(p):
    return asyncio.run(extract(p, "d1", 0, "text", "sys", S, timeout_s=5, max_reask=1))


def test_first_try_valid():
    r = _run(Fake([GOOD]))
    assert r.status == "ok" and r.first_try_valid and r.attempts == 1 and r.in_tokens == 100


def test_reask_then_valid_counts_all_tokens():
    p = Fake(['{"total": "x"}', GOOD])
    r = _run(p)
    assert r.status == "ok" and not r.first_try_valid and r.attempts == 2
    assert r.in_tokens == 200 and r.out_tokens == 100
    assert "валідацію" in p.calls[1][-1]["content"]  # модель отримала текст помилки


def test_exhausted_reask_is_failed():
    r = _run(Fake(["not json", "still not json"]))
    assert r.status == "failed" and r.error.startswith("validation") and r.last_raw == "still not json"


def test_transport_error_is_failed():
    r = _run(Fake([TimeoutError("boom")]))
    assert r.status == "failed" and r.error.startswith("transport")
