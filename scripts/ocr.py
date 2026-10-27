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
import numpy as np
import pytesseract

LANG = "ukr+eng+rus"
OEM, PSM = 1, 4  # LSTM; одна колонка тексту змінного розміру (чек)
TAX_DOMAIN = "tax.gov.ua"  # фіскальний QR веде на перевірку в податковій
TARGET_WIDTH = 1600        # ширина вирізаного чека після масштабування, px
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


def _paper_contour(small, v_thr: int, s_max: int = 70):
    hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
    mask = ((hsv[..., 2] >= v_thr) & (hsv[..., 1] <= s_max)).astype(np.uint8) * 255
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (31, 31)))
    cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not cnts:
        return None, 0.0
    c = max(cnts, key=cv2.contourArea)
    return c, cv2.contourArea(c) / (small.shape[0] * small.shape[1])


def find_receipt(img):
    """Вирізає чек з фото і вирівнює нахил.

    Чек — найбільша світла малонасичена пляма. Поріг яскравості піднімаємо, доки пляма не
    перестане займати весь кадр (світла скатертина) і не стане схожою на смугу чека.
    Без цього текстура фону (джинси, тканина) після бінаризації стає тисячами «літер».
    Повертає (crop, кут, частка кадру); якщо чек не знайдено — весь кадр і частку 1.0."""
    h, w = img.shape[:2]
    k = 1000 / max(h, w)
    small = cv2.resize(img, None, fx=k, fy=k, interpolation=cv2.INTER_AREA)
    v = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)[..., 2]
    found = None
    for pct in (55, 65, 75, 82, 88, 92):
        c, frac = _paper_contour(small, max(120, int(np.percentile(v, pct))))
        if c is None:
            continue
        (_, _), (rw, rh), _ = cv2.minAreaRect(c)
        if 0.06 <= frac <= 0.7 and max(rw, rh) / max(min(rw, rh), 1) >= 1.4:
            found = (c, frac)
            break
    if found is None:
        return img, 0.0, 1.0
    c, frac = found
    (cx, cy), (rw, rh), ang = cv2.minAreaRect(c)
    if rw > rh:
        rw, rh, ang = rh, rw, ang + 90
    ang = ang - 90 if ang > 45 else ang + 90 if ang < -45 else ang
    cx, cy, rw, rh = cx / k, cy / k, rw / k * 1.02, rh / k * 1.02
    rot = cv2.warpAffine(img, cv2.getRotationMatrix2D((cx, cy), ang, 1.0), (w, h),
                         flags=cv2.INTER_CUBIC, borderValue=(255, 255, 255))
    x0, y0 = int(max(cx - rw / 2, 0)), int(max(cy - rh / 2, 0))
    return rot[y0:int(min(cy + rh / 2, h)), x0:int(min(cx + rw / 2, w))], ang, frac


def preprocess(crop):
    """Сірий -> фіксована ширина -> вирівнювання освітлення (ділення на розмитий фон) -> Otsu."""
    g = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    k = TARGET_WIDTH / g.shape[1]
    g = cv2.resize(g, None, fx=k, fy=k, interpolation=cv2.INTER_CUBIC if k > 1 else cv2.INTER_AREA)
    norm = cv2.divide(g, cv2.medianBlur(g, 61), scale=255)
    return cv2.threshold(norm, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def fiscal_qr(*images) -> str | None:
    det = cv2.QRCodeDetector()
    for img in images:  # спершу вирізаний чек, потім зменшені копії: детектор чутливий до масштабу
        for scale in (1.0, 0.5, 0.35):
            im = img if scale == 1.0 else cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
            ok, decoded, _, _ = det.detectAndDecodeMulti(im)
            for s in (decoded if ok else []):  # кілька QR на чеку: беремо лише податковий
                if s and TAX_DOMAIN in s:
                    return s
    return None


def main(src: Path, dst: Path) -> None:
    _setup_tesseract()
    dst.mkdir(parents=True, exist_ok=True)
    photos = sorted(p for p in src.iterdir() if p.suffix.lower() in EXTS)
    qr_index: dict[str, str | None] = {}
    (dst / "crops").mkdir(exist_ok=True)
    for i, p in enumerate(photos, 1):
        img = cv2.imread(str(p))  # IMREAD_COLOR враховує EXIF-орієнтацію
        if img is None:
            print(f"[skip] не читається: {p.name} (HEIC з iPhone конвертуй у JPG)")
            continue
        crop, ang, frac = find_receipt(img)
        cv2.imwrite(str(dst / "crops" / f"{p.stem}.jpg"), crop, [cv2.IMWRITE_JPEG_QUALITY, 80])
        text = pytesseract.image_to_string(preprocess(crop), lang=LANG, config=f"--oem {OEM} --psm {PSM}")
        (dst / f"{p.stem}.txt").write_text(text, encoding="utf-8")
        qr_index[p.stem] = fiscal_qr(crop, img)
        warn = "  ⚠ чек не знайдено, OCR по всьому кадру" if frac >= 1.0 else ""
        print(f"[{i}/{len(photos)}] {p.name}: чек {frac:.0%} кадру, нахил {ang:+.1f}°, {len(text)} симв., "
              f"QR={'так' if qr_index[p.stem] else 'ні'}{warn}")

    (dst / "qr.json").write_text(json.dumps(qr_index, ensure_ascii=False, indent=2), encoding="utf-8")
    config = {
        "engine": "tesseract",
        "version": str(pytesseract.get_tesseract_version()),
        "lang": LANG, "oem": OEM, "psm": PSM,
        "preprocess": ["receipt_crop_hsv_paper_mask+deskew_minAreaRect", "grayscale",
                       f"resize_to_width_{TARGET_WIDTH}", "illumination_divide_median61", "otsu_threshold"],
        "qr": f"cv2.QRCodeDetector.detectAndDecodeMulti, фільтр за доменом {TAX_DOMAIN}",
        "manual_edits": "немає; змінено лише маскування персональних даних",
    }
    (dst / "ocr_config.json").write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nГотово: {len(photos)} фото -> {dst}")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
