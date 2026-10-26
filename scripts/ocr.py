"""OCR фото чеків -> сирі тексти + фіскальний QR + ocr_config.json.

Використання:
    uv add opencv-python-headless pytesseract
    uv run python scripts/ocr.py data/private/photos data/private/ocr

Потрібен встановлений tesseract з мовами ukr, eng, rus
(Windows: інсталятор UB Mannheim, при встановленні відмітити Ukrainian і Russian).
Текст зберігається РІВНО так, як віддав OCR — без ручних правок.
"""

import json
import os
import shutil
import sys
from pathlib import Path

import cv2
import pytesseract

LANG = "ukr+eng+rus"
OEM, PSM = 1, 6  # LSTM; один блок тексту (чек — одна колонка)
TAX_DOMAIN = "tax.gov.ua"  # фіскальний QR веде на перевірку в податковій
MIN_WIDTH = 1500
EXTS = {".jpg", ".jpeg", ".png", ".webp", ".heic"}
WIN_DEFAULT = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")


def _setup_tesseract() -> None:
    """Windows: інсталятор UB Mannheim не додає tesseract у PATH — шукаємо самі."""
    cmd = os.getenv("TESSERACT_CMD") or shutil.which("tesseract")
    if not cmd and WIN_DEFAULT.exists():
        cmd = str(WIN_DEFAULT)
    if not cmd:
        sys.exit("tesseract не знайдено. Встанови його або задай TESSERACT_CMD=шлях\\до\\tesseract.exe")
    pytesseract.pytesseract.tesseract_cmd = cmd
    langs = set(pytesseract.get_languages(config=""))
    missing = set(LANG.split("+")) - langs
    if missing:
        sys.exit(f"У tesseract немає мов {sorted(missing)}. Перевстанови, відмітивши Ukrainian і Russian "
                 f"в Additional language data.")


def preprocess(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape
    if w < MIN_WIDTH:
        k = MIN_WIDTH / w
        gray = cv2.resize(gray, None, fx=k, fy=k, interpolation=cv2.INTER_CUBIC)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    # адаптивний поріг краще за Otsu на фото з тінню і відблиском
    return cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY, 31, 15)


def fiscal_qr(img) -> str | None:
    ok, decoded, _, _ = cv2.QRCodeDetector().detectAndDecodeMulti(img)
    if not ok:
        return None
    for s in decoded:  # кілька QR на чеку: беремо лише податковий
        if s and TAX_DOMAIN in s:
            return s
    return None


def main(src: Path, dst: Path) -> None:
    _setup_tesseract()
    dst.mkdir(parents=True, exist_ok=True)
    photos = sorted(p for p in src.iterdir() if p.suffix.lower() in EXTS)
    qr_index: dict[str, str | None] = {}
    for i, p in enumerate(photos, 1):
        img = cv2.imread(str(p))
        if img is None:
            print(f"[skip] не читається: {p.name} (HEIC з iPhone конвертуй у JPG)")
            continue
        text = pytesseract.image_to_string(preprocess(img), lang=LANG,
                                           config=f"--oem {OEM} --psm {PSM}")
        (dst / f"{p.stem}.txt").write_text(text, encoding="utf-8")
        qr_index[p.stem] = fiscal_qr(img)
        print(f"[{i}/{len(photos)}] {p.name}: {len(text)} симв., QR={'так' if qr_index[p.stem] else 'ні'}")

    (dst / "qr.json").write_text(json.dumps(qr_index, ensure_ascii=False, indent=2), encoding="utf-8")
    config = {
        "engine": "tesseract",
        "version": str(pytesseract.get_tesseract_version()),
        "lang": LANG, "oem": OEM, "psm": PSM,
        "preprocess": ["grayscale", f"upscale_to_width_{MIN_WIDTH}", "gaussian_blur_3",
                       "adaptive_threshold_gaussian_31_15"],
        "qr": f"cv2.QRCodeDetector.detectAndDecodeMulti, фільтр за доменом {TAX_DOMAIN}",
        "manual_edits": "немає; змінено лише маскування персональних даних",
    }
    (dst / "ocr_config.json").write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nГотово: {len(photos)} фото -> {dst}")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
