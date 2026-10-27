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

# OCR плутає кирилицю й латиницю (КОД -> KOA, АВТ -> ABT, ЕПЗ -> EN3/HENS) і псує мітки,
# тому мітки описано класами символів-двійників, а не точним словом.
A, B, T, E, P, H, O, K = "[AА]", "[BВ]", "[TТ]", "[EЕ]", "[PР]", "[HН]", "[OО0]", "[KК]"
MASKCH = r"[*xXхХkKкКnNжЖ#%¥+&•]"  # як OCR бачить символи маски номера картки

# (назва, патерн, заміна). Порядок важливий: спершу рядкові правила, потім загальні.
LINE_RULES = [
    # "Касир: Іваненко І.І." / "КАССИР ..." / "ОПЕРАТОР 06 Тарасенко Т. Г." / "Офіціант Макс" / "Роздрукував: Юра"
    ("cashier", re.compile(r"(?im)^(.*?\b(?:касир|кассир|оператор|продавець-консультант|офіціант|роздрукував)"
                           r"\b[ \t]*[:№]?[ \t]*)([^\s:№].*)$"), r"\1[CASHIER]"),  # [ \t]: «КАСИР:» з порожнім рядком не з'їдає наступний
    # McDonald's: "Фоменко Н Каса 01" — ПІБ без мітки перед номером каси
    ("cashier", re.compile(r"(?im)^(.*?)([А-ЯІЇЄҐ][А-ЯІЇЄҐа-яіїєґ'’-]+\s+[А-ЯІЇЄҐ]\.?)(\s+Каса\s+\d+)"),
     r"\1[CASHIER]\3"),
    # Прізвище з ініціалами без мітки (мітку «ОПЕРАТОР» OCR зіпсував): "Тарасенко Т.Г", "Тарасенко T. Г."
    # ФОП як продавець ("ФО-П Федик О.Б.") — публічний реквізит, не маскуємо.
    ("cashier", re.compile(r"(?m)(?<!ФО-П )(?<!ФОП )\b[А-ЯІЇЄҐ][а-яіїєґ'’]{2,}[ \t]+[А-ЯІЇЄҐA-Z][.,][ \t]?"
                           r"[А-ЯІЇЄҐA-Z][.,]?"), "[CASHIER]"),
    # "RRN: …", "#RRN=…", "WRRN=…", "КОД ТРАНЗ. …", "KOA ТРАНЗ.: …" (код транзакції = RRN); цифри можуть бути з пробілом
    ("rrn", re.compile(rf"(?im)^(.*?(?:RRN|РРН|{T}{P}{A}{H}[3З]\w*\.?)[ \t:№=.\-]*)(\d[\d ]{{7,14}}\d)"),
     r"\1[RRN]"),
    # "КОД АВТ. 318035", "KOA ABT. …", "КИ АВТОРИЗАЦІЇ: 164789", "#Код Авторізації: …", "#PE=345255"
    ("auth", re.compile(rf"(?im)^(.*?(?:{A}{B}{T}\w*\.?|\bauth\w*(?:\s*code)?|#?\bPE)[ \t:№=,.|]*)"
                        r"([0-9A-Z]{4,8})\b"), r"\1[AUTH_CODE]"),
    ("loyalty", re.compile(r"(?im)^(.*?\b(?:ДК|ЛК|картк\w*\s+лояльн\w*|бонусн\w*\s+картк\w*|клієнт)\b\s*[:№]?\s*)"
                           r"(\d{6,})"), r"\1[LOYALTY_ID]"),
    # SOCAR: "#Гість:" і номер картки лояльності на наступному рядку
    ("loyalty", re.compile(r"(?im)^(.*?\bГість\b\s*:?\s*\n?\s*#?\s*)(\d{8,})"), r"\1[LOYALTY_ID]"),
    # Рядок з міткою ЕПЗ (номер картки) у будь-якому написанні OCR: ЕПЗ, EN3, ENB, HENS, Ens.
    # «Карта/Карти» не мітка: «ПЛАТ. КАРТА 2065,60» і «Знижка…Карти -1.86» — це суми, їх витягуємо.
    ("card", re.compile(rf"(?im)^(.*?(?<![А-ЯA-Zа-яa-z])(?:{E}[ПNН][3ЗBВSs]|HENS)\b[ \t:#.]*)(\S.{{3,}})$"),
     r"\1[CARD]"),
]
GLOBAL_RULES = [
    # Номер картки без мітки: 4-9 цифр, далі щонайменше 3 символи маски (X, *, як їх бачить OCR), далі цифри.
    # Пробіл усередині маски допускаємо, перенос рядка — ні: «1000 X 3,00» і «1000 ШТ/» не чіпаємо.
    ("card", re.compile(rf"\b\d{{4,9}}(?:[ ]?\d{{2,5}})?(?:[ ]?{MASKCH}){{3,}}[ ]?[\dA-Za-zА-Яа-я]{{0,4}}\b"
                        rf"|(?<![\w*])(?:{MASKCH}[ ]?){{4,}}\d{{1,4}}\b"
                        rf"|\b\d{{6}}[ ]?{MASKCH}{{2,}}[ ]?\d{{4}}\b"), "[CARD]"),  # «449135 xx 6459»
    # телефони: лише з префіксом 38 або з роздільниками, щоб не зачепити 10-значні ФН / РНОКПП
    ("phone", re.compile(r"\+?38\s?\(?0\d{2}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}\b"
                         r"|\(0\d{2}\)\s?\d{3}[\s-]?\d{2}[\s-]?\d{2}\b"
                         r"|\b0\d{2}[\s-]\d{3}[\s-]\d{2}[\s-]\d{2}\b"), "[PHONE]"),
]

# Ручний список після перегляду очима (data/private/pii_denylist.txt, не в git):
# рядки «ПЛЕЙСХОЛДЕР<TAB>фрагмент». Фрагмент і решта рядка після нього замінюються плейсхолдером.
DENYLIST = Path(__file__).resolve().parents[1] / "data" / "private" / "pii_denylist.txt"


def _denylist_rules() -> list:
    if not DENYLIST.exists():
        return []
    rules = []
    for line in DENYLIST.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#") or "\t" not in line:
            continue
        ph, frag = line.split("\t", 1)
        rules.append((f"denylist:{ph}", re.compile(rf"(?im){re.escape(frag.strip())}.*$"), f"[{ph.strip()}]"))
    return rules


def mask(text: str) -> tuple[str, list[str]]:
    log: list[str] = []
    for name, pat, repl in LINE_RULES + GLOBAL_RULES + _denylist_rules():
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
