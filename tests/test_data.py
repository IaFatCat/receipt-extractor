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
    "card": re.compile(r"\b\d{4,9}(?:[ ]?[*xXхХ•]){4,}[ ]?\d{1,4}\b|\b\d{16}\b"),
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


def _mask_module():
    spec = importlib.util.spec_from_file_location("mask", ROOT / "scripts" / "mask.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


@pytest.mark.parametrize("path", GOLDEN_FILES, ids=lambda p: p.stem)
def test_golden_valid(path: Path):
    Receipt.model_validate_json(path.read_text(encoding="utf-8"))


@pytest.mark.skipif(not TEXT_FILES, reason="тексти ще не згенеровано (make ocr && make mask)")
@pytest.mark.parametrize("path", GOLDEN_FILES, ids=lambda p: p.stem)
def test_golden_has_text(path: Path):
    assert (TEXTS / f"{path.stem}.txt").exists(), "golden без тексту"


@pytest.mark.parametrize("path", GOLDEN_FILES, ids=lambda p: p.stem)
def test_masking_does_not_touch_golden_values(path: Path):
    """Маскування не зачіпає поля, які витягуються.
    Перевіряємо правила маскування на самих значеннях golden, а не наявність значень у тексті:
    golden розмічено з фото, і помилки OCR — частина задачі, а не помилка маскування."""
    m = _mask_module()
    gold = json.loads(path.read_text(encoding="utf-8"))
    values = [_get(gold, f) for f in VERBATIM] + [it["name"] for it in gold["items"]]
    for v in filter(None, values):
        assert m.mask(str(v))[0] == str(v), f"маскування змінює {v!r}"


@pytest.mark.parametrize("path", TEXT_FILES, ids=lambda p: p.stem)
def test_no_residual_pii(path: Path):
    s = path.read_text(encoding="utf-8")
    for name, p in PII.items():
        assert not p.search(s), f"схоже на {name}: {p.search(s).group(0)!r}"


def test_mask_script():
    m = _mask_module()
    src = ("ІД 12345678  ПН 123456789012\nФН 4000123456\nКасир: Петренко О.В.\n"
           "Картка 444111******1234\nRRN: 123456789012\nКод авт.: A1B2C3\nтел. +38 (067) 123-45-67\n"
           "ЕПЗ 449135666XXXXXX9\n#PE=788443\n# КОД ТРАНЗ.: 614420143972\nФоменко Н Каса 01\n"
           "ЧЕК № 000205557 00451\n             25.05.2026 21:51:01\n1000 X 3,00\n")
    out, _ = m.mask(src)
    for kept in ("12345678", "123456789012", "4000123456"):
        assert kept in out
    for kept in ("25.05.2026", "1000 X 3,00", "00451", "Каса 01"):
        assert kept in out
    for gone in ("Петренко", "444111", "A1B2C3", "067", "449135666", "788443", "614420143972", "Фоменко"):
        assert gone not in out
    for ph in ("[CASHIER]", "[CARD]", "[RRN]", "[AUTH_CODE]", "[PHONE]"):
        assert ph in out
