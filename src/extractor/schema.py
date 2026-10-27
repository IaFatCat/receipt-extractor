"""Схема витягування фіскального чека.

Поля, яких може не бути в чеку, допускають null: модель не повинна вигадувати.
Арифметику (сума позицій = total, ПДВ = ставка) схема НЕ перевіряє — це робить
metrics.arithmetic_checks, бо чек сам буває з розбіжностями округлення.
"""

from __future__ import annotations

import copy
from datetime import datetime
from decimal import Decimal
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class PaymentMethod(StrEnum):
    CASH = "cash"
    CARD = "card"
    MIXED = "mixed"
    UNKNOWN = "unknown"


class Currency(StrEnum):
    UAH = "UAH"
    EUR = "EUR"
    USD = "USD"
    PLN = "PLN"
    OTHER = "other"


class ExpenseCategory(StrEnum):
    GROCERIES = "groceries"
    MEALS = "meals"
    TRANSPORT = "transport"
    FUEL = "fuel"
    LODGING = "lodging"
    PHARMACY = "pharmacy"
    OFFICE = "office"
    OTHER = "other"


# Визначення per-member зі StrEnum не потрапляють у JSON Schema, тому вони тут —
# у description поля, яке модель бачить у схемі.
CATEGORY_DESC = (
    "Класифікація (не витягування): категорія витрати за продавцем і основною частиною суми. "
    "groceries — продукти й побутові товари в магазині; "
    "meals — готова їжа й напої (кафе, ресторан, фастфуд); "
    "transport — таксі, проїзд, паркування; "
    "fuel — пальне на АЗК (не товари магазину АЗК); "
    "lodging — готель, оренда житла; "
    "pharmacy — аптека; "
    "office — канцтовари, техніка, обладнання для роботи; "
    "other — усе, що не підходить під жодну категорію вище."
)


class _Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class VatLine(_Strict):
    group: str = Field(max_length=2, description="Літера групи ПДВ як надруковано: А, Б, Н …")
    rate: Decimal | None = Field(None, description="Ставка у %: 20 / 7 / 0; null — «звільнені» або не вказано")
    amount: Decimal | None = Field(None, description="Сума ПДВ за групою, як надруковано")


class Seller(_Strict):
    name: str | None = Field(None, description="Назва продавця дослівно (ТОВ/ФОП …)")
    vat_payer_number: str | None = Field(None, pattern=r"^\d{12}$", description="«ПН» — 12 цифр")
    tax_id: str | None = Field(None, pattern=r"^\d{8}$|^\d{10}$", description="«ІД»: ЄДРПОУ (8) або РНОКПП ФОП (10)")
    address: str | None = None


class ReceiptItem(_Strict):
    name: str = Field(description="Назва дослівно, зі скороченнями й помилками друку, без розшифровки")
    qty: Decimal = Field(gt=0, description="Кількість або вага; може бути дробовою (0.334, 0.294)")
    unit_price: Decimal | None = Field(None, description="Ціна за одиницю, якщо надрукована окремо")
    amount: Decimal = Field(description="Сума за рядком, як надруковано (до знижки на рядок)")
    discount: Decimal | None = Field(None, ge=0, description="Знижка на цей рядок (рядок «Знижка…» під позицією) "
                                                            "як додатне число; null, якщо рядка знижки немає")
    vat_group: str | None = Field(None, max_length=2, description="Літера групи ПДВ біля позиції")


class Receipt(_Strict):
    seller: Seller
    receipt_number: str | None = Field(None, description="«ЧЕК №», буває буквено-цифровий")
    fiscal_number: str | None = Field(None, pattern=r"^\d{10}$", description="«ФН» / «ФН ПРРО» — 10 цифр")
    issued_at: datetime | None = Field(None, description="Дата й час видачі чека")
    currency: Currency
    items: list[ReceiptItem] = Field(min_length=1)
    vat: list[VatLine] = Field(default_factory=list, description="Підсумки ПДВ за групами з підвалу чека")
    discount_total: Decimal | None = Field(None, description="Загальна знижка, якщо надрукована")
    total: Decimal = Field(description="Підсумок до сплати («СУМА»)")
    payment_method: PaymentMethod
    category: ExpenseCategory = Field(description=CATEGORY_DESC)


# --- групи полів для метрик -------------------------------------------------

# Скалярні поля, що порівнюються з golden. Шлях через крапку.
SCALAR_FIELDS = [
    "seller.name", "seller.tax_id", "seller.vat_payer_number",
    "receipt_number", "fiscal_number", "issued_at",
    "currency", "discount_total", "total", "payment_method",
]
# Поля, значення яких має бути в тексті дослівно -> на них рахуємо «вигадані значення».
# category / currency / payment_method свідомо виключені: їх модель виводить, а не копіює.
# seller.address у метриках не порівнюється: багаторядкова, межа між назвою магазину й адресою неоднозначна.
EXTRACTIVE_FIELDS = [
    "seller.name", "seller.tax_id", "seller.vat_payer_number",
    "receipt_number", "fiscal_number", "issued_at", "discount_total", "total",
]
CLASSIFICATION_FIELDS = ["category"]


def _inline_refs(node: Any, defs: dict[str, Any]) -> Any:
    if isinstance(node, dict):
        if "$ref" in node:
            return _inline_refs(copy.deepcopy(defs[node["$ref"].split("/")[-1]]), defs)
        return {k: _inline_refs(v, defs) for k, v in node.items() if k != "$defs"}
    if isinstance(node, list):
        return [_inline_refs(v, defs) for v in node]
    return node


def receipt_json_schema() -> dict[str, Any]:
    """JSON Schema без $ref: однаково добре їсть і Ollama (grammar), і tool use провайдера."""
    raw = Receipt.model_json_schema()
    return _inline_refs(raw, raw.get("$defs", {}))
