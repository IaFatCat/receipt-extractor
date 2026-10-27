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
    # "Касир: Іваненко І.І." / "КАССИР ..." / "ОПЕРАТОР 06 Тарасенко Т. Г." / "Офіціант Макс" / "Роздрукував: Юра"
    ("cashier", re.compile(r"(?im)^(.*?\b(?:касир|кассир|оператор|продавець-консультант|офіціант|роздрукував)"
                           r"\b[ \t]*[:№]?[ \t]*)([^\s:№].*)$"), r"\1[CASHIER]"),  # [ \t]: «КАСИР:» з порожнім рядком не з'їдає наступний
    # McDonald's: "Фоменко Н Каса 01" — ПІБ без мітки перед номером каси
    ("cashier", re.compile(r"(?im)^(\s*)([А-ЯІЇЄҐ][А-ЯІЇЄҐа-яіїєґ'’-]+\s+[А-ЯІЇЄҐ]\.?)(\s+Каса\s+\d+)"),
     r"\1[CASHIER]\3"),
    # "RRN: …", "#RRN=…", "#Код RRN: …", "КОД ТРАНЗ. …", "# КОД ТРАНЗ.: …" (код транзакції = RRN)
    ("rrn", re.compile(r"(?im)^(.*?(?:\bRRN\b|\bРРН\b|код\s*транз\w*\.?)\s*[:№=]?\s*)([0-9A-Z]{6,})"),
     r"\1[RRN]"),
    # "КОД АВТ. 318035", "#Код Авторізації: 345255", "#PE=345255" (PE у термінальному блоці = код авторизації)
    ("auth", re.compile(r"(?im)^(.*?(?:\bкод\s*авт\w*\.?|\bавт\.?\s*код|\bauth\w*(?:\s*code)?|#?\bPE)"
                        r"\s*[:№=]?\s*)([0-9A-Z]{4,8})\b"), r"\1[AUTH_CODE]"),
    ("loyalty", re.compile(r"(?im)^(.*?\b(?:ДК|ЛК|картк\w*\s+лояльн\w*|бонусн\w*\s+картк\w*|клієнт)\b\s*[:№]?\s*)"
                           r"(\d{6,})"), r"\1[LOYALTY_ID]"),
    # SOCAR: "#Гість:" і номер картки лояльності на наступному рядку
    ("loyalty", re.compile(r"(?im)^(.*?\bГість\b\s*:?\s*\n?\s*#?\s*)(\d{8,})"), r"\1[LOYALTY_ID]"),
]
GLOBAL_RULES = [
    # 449135XXXXXX6459 / 4491XXXXXXXX6459 / 449135666******9 / 449135666XXXXXX9 / ************6459
    # Щонайменше 4 символи маски (* / X) поспіль, без переносу рядка: «00451\n   25.05» і «1000 X 3,00» не чіпаємо
    ("card", re.compile(r"\b\d{4,9}(?:[ ]?[*xXхХ•]){4,}[ ]?\d{1,4}\b|(?<![\w*])(?:[*xXхХ•][ ]?){4,}\d{1,4}\b"),
     "[CARD]"),
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
