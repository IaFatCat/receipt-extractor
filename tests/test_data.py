"""Тести даних: golden валідний, маскування не зачепило витягувані поля, ПД не лишилося."""

import importlib.util
import json
import re
from pathlib import Path

import pytest

from extractor.config import GOLDEN, ROOT, TEXTS
from extractor.schema import Receipt, receipt_json_schema

GOLDEN_FILES = sorted(GOLDEN.glob("*.json"))
TEXT_FILES = sorted(TEXTS.glob("*.txt"))
VERBATIM = ["seller.name", "seller.tax_id", "seller.vat_payer_number", "receipt_number", "fiscal_number"]
PII = {
    "card": re.compile(r"\b\d{4,6}[\s*xXх•]{4,}\d{4}\b|\b\d{16}\b"),
    "phone": re.compile(r"\+?38\s?\(?0\d{2}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}\b"),
}


def _norm(s: str) -> str:
    return re.sub(r"\s+", "", s).upper()


def _get(d: dict, path: str):
    for k in path.split("."):
        d = (d or {}).get(k)
    return d


def test_schema_has_no_refs():
    assert "$ref" not in json.dumps(receipt_json_schema())


@pytest.mark.parametrize("path", GOLDEN_FILES, ids=lambda p: p.stem)
def test_golden_valid_and_has_text(path: Path):
    Receipt.model_validate_json(path.read_text(encoding="utf-8"))
    assert (TEXTS / f"{path.stem}.txt").exists(), "golden без тексту"


@pytest.mark.parametrize("path", GOLDEN_FILES, ids=lambda p: p.stem)
def test_masking_kept_extracted_fields(path: Path):
    gold = json.loads(path.read_text(encoding="utf-8"))
    text = _norm((TEXTS / f"{path.stem}.txt").read_text(encoding="utf-8"))
    for f in VERBATIM:
        v = _get(gold, f)
        assert v is None or _norm(str(v)) in text, f"{f}={v!r} немає в тексті"
    for it in gold["items"]:
        assert _norm(it["name"]) in text, f"позиція {it['name']!r} немає в тексті"


@pytest.mark.parametrize("path", TEXT_FILES, ids=lambda p: p.stem)
def test_no_residual_pii(path: Path):
    s = path.read_text(encoding="utf-8")
    for name, p in PII.items():
        assert not p.search(s), f"схоже на {name}: {p.search(s).group(0)!r}"


def test_mask_script():
    spec = importlib.util.spec_from_file_location("mask", ROOT / "scripts" / "mask.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    src = ("ІД 12345678  ПН 123456789012\nФН 4000123456\nКасир: Петренко О.В.\n"
           "Картка 444111******1234\nRRN: 123456789012\nКод авт.: A1B2C3\nтел. +38 (067) 123-45-67\n")
    out, _ = m.mask(src)
    for kept in ("12345678", "123456789012", "4000123456"):
        assert kept in out
    for gone in ("Петренко", "444111", "A1B2C3", "067"):
        assert gone not in out
    for ph in ("[CASHIER]", "[CARD]", "[RRN]", "[AUTH_CODE]", "[PHONE]"):
        assert ph in out
