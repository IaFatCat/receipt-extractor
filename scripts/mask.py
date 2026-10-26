"""Маскування персональних даних в OCR-текстах однаковими плейсхолдерами.

Використання:
    uv run python scripts/mask.py data/private/ocr data/texts

НЕ маскуються (публічні реквізити бізнесу і поля, що витягуються):
    назва продавця, ІД (ЄДРПОУ/РНОКПП ФОП), ПН, ФН, номер чека, суми, позиції, дати.
Маскуються: касир/оператор, платіжна картка, телефони, картка лояльності, RRN, код авторизації.

Після запуску ОБОВ'ЯЗКОВО переглянь кожен текст очима: regex не бачить ПІБ у довільному місці.
Скрипт друкує всі зміни, щоб перегляд був швидким.
"""

import re
import shutil
import sys
from pathlib import Path

# (назва, патерн, заміна). Порядок важливий: спершу рядкові правила, потім загальні.
LINE_RULES = [
    # "Касир: Іваненко І.І." / "КАССИР ..." / "Оператор ..." -> залишаємо мітку, маскуємо решту рядка
    ("cashier", re.compile(r"(?im)^(.*?\b(?:касир|кассир|оператор|продавець-консультант)\b\s*[:№]?\s*)(.+)$"),
     r"\1[CASHIER]"),
    ("rrn", re.compile(r"(?im)^(.*?\b(?:RRN|РРН)\b\s*[:№]?\s*)([0-9A-Z]{6,})"), r"\1[RRN]"),
    ("auth", re.compile(r"(?im)^(.*?\b(?:код\s*авт\w*\.?|авт\.?\s*код|auth\w*(?:\s*code)?)\s*[:№]?\s*)([0-9A-Z]{4,8})\b"),
     r"\1[AUTH_CODE]"),
    ("loyalty", re.compile(r"(?im)^(.*?\b(?:ДК|ЛК|картк\w*\s+лояльн\w*|бонусн\w*\s+картк\w*|клієнт)\b\s*[:№]?\s*)(\d{6,})"),
     r"\1[LOYALTY_ID]"),
]
GLOBAL_RULES = [
    # 4441 **** **** 1234 / 444111******1234 / ****1234 / XXXX XXXX XXXX 1234
    ("card", re.compile(r"\b\d{4,6}[\s*xXх•]{4,}\d{4}\b|(?<![\w*])[*xXх•]{4,}[\s*xXх•]*\d{4}\b"), "[CARD]"),
    # телефони: лише з префіксом 38 або з роздільниками, щоб не зачепити 10-значні ФН / РНОКПП
    ("phone", re.compile(r"\+?38\s?\(?0\d{2}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}\b"
                         r"|\(0\d{2}\)\s?\d{3}[\s-]?\d{2}[\s-]?\d{2}\b"
                         r"|\b0\d{2}[\s-]\d{3}[\s-]\d{2}[\s-]\d{2}\b"), "[PHONE]"),
]


def mask(text: str) -> tuple[str, list[str]]:
    log: list[str] = []
    for name, pat, repl in LINE_RULES + GLOBAL_RULES:
        def _sub(m: re.Match, name=name, repl=repl) -> str:
            new = m.expand(repl)
            log.append(f"  {name}: {m.group(0).strip()!r} -> {new.strip()!r}")
            return new
        text = pat.sub(_sub, text)
    return text, log


def main(src: Path, dst: Path) -> None:
    dst.mkdir(parents=True, exist_ok=True)
    for p in sorted(src.glob("*.txt")):
        masked, log = mask(p.read_text(encoding="utf-8"))
        (dst / p.name).write_text(masked, encoding="utf-8")
        print(f"{p.name}: {len(log)} замін")
        print("\n".join(log) if log else "  (нічого) — перевір очима, чи справді немає ПІБ")
    cfg = src / "ocr_config.json"
    if cfg.exists():  # налаштування OCR — у репозиторій, поруч з текстами
        shutil.copy(cfg, dst.parent / "ocr_config.json")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
