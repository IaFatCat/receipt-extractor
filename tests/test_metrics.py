from decimal import Decimal
from pathlib import Path

from extractor.metrics import arithmetic_checks, compare, not_in_text
from extractor.schema import Receipt

FX = Path(__file__).parent / "fixtures"
GOLD = Receipt.model_validate_json((FX / "sample_golden.json").read_text(encoding="utf-8"))
TEXT = (FX / "sample.txt").read_text(encoding="utf-8")


def test_golden_fixture_is_consistent():
    assert arithmetic_checks(GOLD) == {"sum_eq_total": True, "qty_x_price": True, "vat_consistent": True}


def test_perfect_prediction():
    c = compare(GOLD, GOLD)
    assert set(c["fields"].values()) <= {"correct", "both_null"}
    assert c["items"]["matched"] == 2
    assert not_in_text(GOLD, TEXT) == []


def test_hallucination_and_swap_detected():
    pred = GOLD.model_copy(deep=True)
    pred.discount_total = Decimal("5.00")          # у чеку знижки немає
    pred.items[0].qty, pred.items[0].unit_price = Decimal("414.00"), Decimal("0.334")  # переплутані
    pred.fiscal_number = "4000999999"
    c = compare(GOLD, pred)
    assert c["fields"]["discount_total"] == "hallucinated"
    assert c["fields"]["fiscal_number"] == "wrong"
    assert c["items"]["field_correct"]["qty"] == 1
    assert "fiscal_number" in not_in_text(pred, TEXT)
    # Обмеження арифметики: переставлені qty/ціна дають ту саму суму — ловить лише порівняння з golden
    assert arithmetic_checks(pred)["qty_x_price"] is True


def test_masking_placeholder_in_field_is_not_in_text_safe():
    pred = GOLD.model_copy(deep=True)
    pred.seller.name = "ТОВ ВИГАДАНИЙ"
    assert "seller.name" in not_in_text(pred, TEXT)
