"""Перераховує метрики всіх прогонів у results/ і оновлює авто-блок REPORT.md.

Ручні розділи REPORT.md (розбір помилок, вибір) поза маркерами AUTO не чіпаються.
Метрики перераховуються з outputs/ при кожному запуску, тож правка golden не вимагає нового прогону моделей.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .config import DATA, GOLDEN, RESULTS, ROOT, TEXTS
from .metrics import compute_run, golden_arithmetic
from .schema import SCALAR_FIELDS, Receipt

START, END = "<!-- AUTO:START -->", "<!-- AUTO:END -->"


def _f(x: dict | None) -> str:
    if not x or not x.get("n"):
        return "—"
    return f"{x['k']}/{x['n']}"


def _p(x: dict | None) -> str:
    if not x or x.get("rate") is None:
        return "—"
    return f"{x['rate'] * 100:.0f}%"


def _num(v: Any, fmt: str = "{:.2f}") -> str:
    return "—" if v is None else fmt.format(v)


def load_golden() -> dict[str, Receipt]:
    return {p.stem: Receipt.model_validate_json(p.read_text(encoding="utf-8")) for p in sorted(GOLDEN.glob("*.json"))}


def build() -> list[dict[str, Any]]:
    texts = {p.stem: p.read_text(encoding="utf-8") for p in TEXTS.glob("*.txt")}
    golden = load_golden()
    seg_path = DATA / "segments.json"
    segments = json.loads(seg_path.read_text(encoding="utf-8")) if seg_path.exists() else None
    runs = []
    for d in sorted(p for p in RESULTS.iterdir() if (p / "meta.json").exists()) if RESULTS.exists() else []:
        m, errors = compute_run(d, texts, golden, segments)
        (d / "metrics.json").write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding="utf-8")
        lines = [f"# Помилки на golden: {m['run_id']}\n", "| doc | r | поле | тип | golden | модель |",
                 "|---|---|---|---|---|---|"]
        lines += [f"| {e['doc']} | {e['repeat']} | {e['field']} | {e.get('kind', '')} | "
                  f"{str(e['gold'])[:60]} | {str(e['pred'])[:60]} |" for e in errors]
        (d / "errors.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        runs.append(m)
    return runs


def render(runs: list[dict[str, Any]], golden: dict[str, Receipt]) -> str:
    if not runs:
        return "_Ще немає прогонів у results/. Запусти `make run`._"
    out = [
        "## Зведена таблиця",
        "",
        f"Golden: {len(golden)} чеків. Точність — на golden, у форматі «правильно/всього» "
        "(при temperature>0 рахується по всіх повторах). Валідність, latency і вартість — на всіх текстах.",
        "",
        "| Модель | Промпт | Семплінг | Валідні з 1-ї | Після re-ask | Failed | Поля (micro) | Вигадані | "
        "Пропущені | Позиції F1 | category | Немає в тексті | p50, с | p95, с | $ / 1000 | год / 1000 |",
        "|" + "---|" * 16,
    ]
    for m in runs:
        out.append(
            f"| {m['model']} | {m['prompt_version']} | {m['sampling_key']} | {_f(m['valid_first_try'])} | "
            f"{_f(m['valid_after_reask'])} | {_f(m['failed'])} | {_f(m['field_accuracy_micro'])} | "
            f"{_f(m['hallucinated'])} | {_f(m['missed'])} | {_num(m['items']['f1'])} | "
            f"{_f(m['category']['accuracy'])} | {_f(m['not_in_text'])} | {_num(m['latency_p50_s'], '{:.1f}')} | "
            f"{_num(m['latency_p95_s'], '{:.1f}')} | {_num(m['cost_per_1000_usd'], '{:.3f}')} | "
            f"{_num(m['hours_per_1000_sequential'], '{:.2f}')} |")

    out += ["", "## Точність по полях", "", "| Поле | " + " | ".join(m["run_id"] for m in runs) + " |",
            "|---|" + "---|" * len(runs)]
    for f in SCALAR_FIELDS + ["seller.address"]:
        out.append(f"| {f} | " + " | ".join(_f(m["fields"].get(f)) for m in runs) + " |")
    for f in ("name", "qty", "unit_price", "amount", "vat_group"):
        out.append(f"| items.{f} (зіставлені) | "
                   + " | ".join(_f(m["items"]["matched_field_accuracy"].get(f)) for m in runs) + " |")
    out.append("| vat.rate | " + " | ".join(_f(m["vat"]["rate_correct"]) for m in runs) + " |")
    out.append("| vat.amount | " + " | ".join(_f(m["vat"]["amount_correct"]) for m in runs) + " |")

    out += ["", "## Арифметика (перевіряє код, не модель)", "",
            "Базова лінія — golden: якщо сам чек не сходиться, це проблема каси, а не моделі.", "",
            "| Перевірка | golden | " + " | ".join(m["run_id"] for m in runs) + " |",
            "|---|---|" + "---|" * len(runs)]
    ga = golden_arithmetic(golden)
    for k in ("sum_eq_total", "qty_x_price", "vat_consistent"):
        out.append(f"| {k} | {_f(ga.get(k))} | " + " | ".join(_f(m["arithmetic_pred"].get(k)) for m in runs) + " |")

    out += ["", "## category (класифікація, окремо від витягування)", ""]
    for m in runs:
        conf = ", ".join(f"{k}: {v}" for k, v in m["category"]["confusion"].items() if k.split("->")[0] != k.split("->")[1])
        out.append(f"- **{m['run_id']}**: {_f(m['category']['accuracy'])}" + (f"; помилки — {conf}" if conf else ""))

    seg_runs = [m for m in runs if len(m.get("by_segment_field_accuracy", {})) > 1]
    if seg_runs:
        segs = sorted({s for m in seg_runs for s in m["by_segment_field_accuracy"]})
        out += ["", "## Точність по сегментах", "", "| Прогін | " + " | ".join(segs) + " |",
                "|---|" + "---|" * len(segs)]
        for m in seg_runs:
            out.append(f"| {m['run_id']} | " + " | ".join(_f(m["by_segment_field_accuracy"].get(s)) for s in segs) + " |")

    stab = [m for m in runs if m.get("stability_all_repeats_identical")]
    if stab:
        out += ["", "## Стабільність при temperature > 0", ""]
        out += [f"- **{m['run_id']}**: усі {m['repeats']} повтори ідентичні у "
                f"{_f(m['stability_all_repeats_identical'])} golden-чеків" for m in stab]

    sanity = [m for m in runs if m["thinking_chars_total"] or m["ctx_truncated"]]
    if sanity:
        out += ["", "## ⚠ Перевірки коректності прогону", ""]
        out += [f"- {m['run_id']}: thinking_chars={m['thinking_chars_total']}, ctx_truncated={m['ctx_truncated']}"
                for m in sanity]
    out += ["", "Деталі кожного прогону: `results/<run_id>/metrics.json`, помилки по полях: `results/<run_id>/errors.md`."]
    return "\n".join(out)


def update_report() -> None:
    runs = build()
    block = f"{START}\n{render(runs, load_golden())}\n{END}"
    path = ROOT / "REPORT.md"
    text = path.read_text(encoding="utf-8") if path.exists() else f"# Звіт\n\n{START}\n{END}\n"
    if START in text and END in text:
        text = text[: text.index(START)] + block + text[text.index(END) + len(END):]
    else:
        text += "\n" + block + "\n"
    path.write_text(text, encoding="utf-8")
    print(f"REPORT.md оновлено: {len(runs)} прогонів")
