"""Метрики прогону.

На всіх документах: валідність, latency, токени, вартість, «немає в тексті», арифметика.
На golden: точність по полях, вигадані значення, позиції, ПДВ, category (окремо — це класифікація).
"""

from __future__ import annotations

import json
import re
import statistics
from collections import Counter, defaultdict
from datetime import datetime
from decimal import Decimal
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from .schema import CLASSIFICATION_FIELDS, EXTRACTIVE_FIELDS, SCALAR_FIELDS, Receipt

TOL, VAT_TOL = Decimal("0.01"), Decimal("0.02")
ITEM_FIELDS = ("name", "qty", "unit_price", "amount", "discount", "vat_group")
TEXT_CHECK_FIELDS = ["seller.name", "seller.tax_id", "seller.vat_payer_number", "receipt_number", "fiscal_number"]


# --- нормалізація ------------------------------------------------------------

def get(obj: Any, path: str) -> Any:
    for k in path.split("."):
        if obj is None:
            return None
        obj = getattr(obj, k, None)
    return obj


# Латинські двійники кириличних літер: «А95» з латинською A == «А95» з кириличною
_HOMOGLYPHS = str.maketrans("ABCEHIKMOPTXY", "АВСЕНІКМОРТХУ")


def norm_str(s: str) -> str:
    """Регістр, лапки, пробіли (переноси рядків у назвах) і латинські двійники не мають значення."""
    s = re.sub(r"[«»\"'“”„`]", "", s.upper()).translate(_HOMOGLYPHS)
    return re.sub(r"\s+", "", s).strip(".,;:")


def norm_compact(s: str) -> str:
    return re.sub(r"\s+", "", s).upper()


def norm_value(v: Any) -> Any:
    if v is None:
        return None
    if isinstance(v, Decimal):
        return v.normalize()
    if isinstance(v, datetime):  # до хвилини: секунди на фото бувають обрізані
        return v.replace(tzinfo=None, second=0, microsecond=0)
    if hasattr(v, "value"):  # StrEnum
        return v.value
    if isinstance(v, str):
        return norm_str(v)
    return v


def same(a: Any, b: Any) -> bool:
    return norm_value(a) == norm_value(b)


def same_field(field: str, g: Any, p: Any) -> bool:
    if field == "receipt_number" and isinstance(g, str) and isinstance(p, str):
        # «ЧЕК № 000205557 00451»: другий номер — службовий, обидва варіанти вважаємо правильними
        return norm_str(g) == norm_str(p) or norm_str(g) in [norm_str(t) for t in p.split()]
    return same(g, p)


def same_item_field(field: str, g: Any, p: Any) -> bool:
    gv, pv = getattr(g, field), getattr(p, field)
    if field == "discount":
        return same(gv or Decimal(0), pv or Decimal(0))
    if field == "unit_price" and (gv is None or pv is None) and g.qty == 1:
        # ціну окремо не надруковано: при qty=1 «null» і «= сума рядка» еквівалентні
        return same(gv if gv is not None else g.amount, pv if pv is not None else p.amount)
    return same(gv, pv)


# --- арифметика кодом ------------------------------------------------------

def arithmetic_checks(r: Receipt) -> dict[str, bool | None]:
    items_sum = sum((i.amount - (i.discount or 0) for i in r.items), Decimal(0))
    out: dict[str, bool | None] = {
        "sum_eq_total": abs(items_sum - (r.discount_total or 0) - r.total) <= TOL
        or abs(items_sum - r.total) <= TOL,  # мережі по-різному друкують суму позиції: до/після знижки
    }
    lines = [abs(i.qty * i.unit_price - i.amount) <= TOL for i in r.items if i.unit_price is not None]
    out["qty_x_price"] = all(lines) if lines else None
    vat = []
    for v in r.vat:
        if v.rate is None or v.amount is None:
            continue  # «звільнені», акциз тощо
        base = sum((i.amount - (i.discount or 0) for i in r.items if i.vat_group == v.group), Decimal(0))
        if base == 0:
            continue
        expected = (base * v.rate / (100 + v.rate)).quantize(Decimal("0.01"))  # ПДВ у ціні
        vat.append(abs(expected - v.amount) <= VAT_TOL)
    out["vat_consistent"] = all(vat) if vat else None
    return out


# --- «немає в тексті» — дешевий детектор галюцинацій без golden ------------

def _num_variants(d: Decimal) -> list[str]:
    s = f"{d:.2f}"
    return [s, s.replace(".", ",")]


def not_in_text(r: Receipt, text: str) -> list[str]:
    t = norm_compact(text)
    bad = []
    for f in TEXT_CHECK_FIELDS:
        v = get(r, f)
        if isinstance(v, str) and v and norm_compact(v) not in t:
            bad.append(f)
    if not any(x in t for x in _num_variants(r.total)):
        bad.append("total")
    for i, it in enumerate(r.items):
        if norm_compact(it.name) not in t:
            bad.append(f"items[{i}].name")
    return bad


# --- вирівнювання позицій ----------------------------------------------------

def align_items(gold: list, pred: list) -> list[tuple[int, int]]:
    cands = []
    for gi, g in enumerate(gold):
        for pi, p in enumerate(pred):
            score = SequenceMatcher(None, norm_str(g.name), norm_str(p.name)).ratio()
            if g.amount == p.amount:
                score += 0.5
            if score >= 0.6:
                cands.append((score, gi, pi))
    used_g, used_p, pairs = set(), set(), []
    for _, gi, pi in sorted(cands, reverse=True):
        if gi not in used_g and pi not in used_p:
            used_g.add(gi)
            used_p.add(pi)
            pairs.append((gi, pi))
    return pairs


# --- порівняння одного документа з golden ----------------------------------

def compare(gold: Receipt, pred: Receipt) -> dict[str, Any]:
    fields: dict[str, str] = {}
    for f in SCALAR_FIELDS:
        g, p = get(gold, f), get(pred, f)
        if g is None and p is None:
            fields[f] = "both_null"
        elif g is None:
            fields[f] = "hallucinated"
        elif p is None:
            fields[f] = "missed"
        else:
            fields[f] = "correct" if same_field(f, g, p) else "wrong"

    pairs = align_items(gold.items, pred.items)
    item_fields, item_errors = Counter(), []
    for gi, pi in pairs:
        g, p = gold.items[gi], pred.items[pi]
        for f in ITEM_FIELDS:
            ok = same_item_field(f, g, p)
            item_fields[f] += ok
            if not ok:
                item_errors.append((f"items[{gi}].{f}", getattr(g, f), getattr(p, f)))

    gv, pv = {v.group: v for v in gold.vat}, {v.group: v for v in pred.vat}
    vat_match = [(gv[k], pv[k]) for k in gv.keys() & pv.keys()]

    return {
        "fields": fields,
        "items": {"gold": len(gold.items), "pred": len(pred.items), "matched": len(pairs),
                  "field_correct": dict(item_fields), "errors": item_errors},
        "vat": {"gold": len(gv), "pred": len(pv), "matched": len(vat_match),
                "rate_correct": sum(same(a.rate, b.rate) for a, b in vat_match),
                "amount_correct": sum(same(a.amount, b.amount) for a, b in vat_match)},
        "category": {"gold": gold.category.value, "pred": pred.category.value},
    }


# --- агрегати прогону ----------------------------------------------------------

def _pct(values: list[float], q: float) -> float | None:
    if not values:
        return None
    if len(values) == 1:
        return values[0]
    return statistics.quantiles(values, n=100, method="inclusive")[int(q) - 1]


def _frac(k: int, n: int) -> dict[str, Any]:
    return {"k": k, "n": n, "rate": round(k / n, 4) if n else None}


def compute_run(run_dir: Path, texts: dict[str, str], golden: dict[str, Receipt],
                segments: dict[str, str] | None = None) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    meta = json.loads((run_dir / "meta.json").read_text(encoding="utf-8"))
    calls = [json.loads(line) for line in (run_dir / "calls.jsonl").read_text(encoding="utf-8").splitlines() if line]
    preds: dict[tuple[str, int], Receipt] = {}
    for f in (run_dir / "outputs").glob("*.json"):
        o = json.loads(f.read_text(encoding="utf-8"))
        if o.get("status") == "ok" and o.get("data"):
            preds[(o["doc_id"], o["repeat"])] = Receipt.model_validate(o["data"])

    n = len(calls)
    lat = [c["latency_s"] for c in calls]  # для кешованих — latency оригінального виклику
    ok = [c for c in calls if c["status"] == "ok"]
    costs = [c["cost_usd"] for c in calls]
    m: dict[str, Any] = {
        "run_id": meta["run_id"], "model_key": meta["model_key"], "model": meta["model"],
        "provider": meta["provider"], "prompt_version": meta["prompt_version"],
        "sampling_key": meta["sampling_key"], "repeats": meta["repeats"],
        "calls": n,
        "valid_first_try": _frac(sum(c["first_try_valid"] for c in calls), n),
        "valid_after_reask": _frac(sum(c["status"] == "ok" and not c["first_try_valid"] for c in calls), n),
        "failed": _frac(n - len(ok), n),
        "latency_p50_s": _pct(lat, 50), "latency_p95_s": _pct(lat, 95),
        "avg_in_tokens": statistics.fmean(c["in_tokens"] + c["cache_read_tokens"] + c["cache_write_tokens"]
                                          for c in calls) if calls else None,
        "avg_out_tokens": statistics.fmean(c["out_tokens"] for c in calls) if calls else None,
        "cost_per_1000_usd": round(statistics.fmean(costs) * 1000, 4) if costs else None,
        "hours_per_1000_sequential": round(statistics.fmean(lat) * 1000 / 3600, 2) if lat else None,
        "thinking_chars_total": sum(c.get("thinking_chars", 0) for c in calls),
        "ctx_truncated": sum(c.get("ctx_truncated", False) for c in calls),
    }

    # --- без golden: «немає в тексті» і арифметика на всіх валідних
    nit_slots = nit_bad = 0
    arith = defaultdict(lambda: [0, 0])
    for (doc, _), r in preds.items():
        bad = not_in_text(r, texts.get(doc, ""))
        nit_slots += sum(get(r, f) is not None for f in TEXT_CHECK_FIELDS) + 1 + len(r.items)
        nit_bad += len(bad)
        for k, v in arithmetic_checks(r).items():
            if v is not None:
                arith[k][0] += v
                arith[k][1] += 1
    m["not_in_text"] = _frac(nit_bad, nit_slots)
    m["arithmetic_pred"] = {k: _frac(*v) for k, v in arith.items()}

    # --- golden
    errors: list[dict[str, Any]] = []
    fstat = defaultdict(Counter)
    items, vat, cat_conf = Counter(), Counter(), Counter()
    item_fields = Counter()
    seg_correct = defaultdict(lambda: [0, 0])
    stability = []
    gold_docs = [d for d in golden if any(k[0] == d for k in preds) or any(c["doc_id"] == d for c in calls)]
    for doc in gold_docs:
        g = golden[doc]
        reps = [preds.get((doc, r)) for r in range(meta["repeats"])]
        valid = [p for p in reps if p is not None]
        if meta["repeats"] > 1 and len(valid) == meta["repeats"]:
            dumps = {p.model_dump_json() for p in valid}
            stability.append(len(dumps) == 1)
        for rep, p in enumerate(reps):
            if p is None:
                for f in SCALAR_FIELDS:
                    fstat[f]["failed"] += 1
                errors.append({"doc": doc, "repeat": rep, "field": "*", "gold": "", "pred": "FAILED"})
                continue
            c = compare(g, p)
            for f, st in c["fields"].items():
                fstat[f][st] += 1
                if st in ("wrong", "missed", "hallucinated"):
                    errors.append({"doc": doc, "repeat": rep, "field": f, "kind": st,
                                   "gold": str(get(g, f)), "pred": str(get(p, f))})
                if f in SCALAR_FIELDS:
                    seg = (segments or {}).get(doc, "all")
                    seg_correct[seg][0] += st in ("correct", "both_null")
                    seg_correct[seg][1] += 1
            for k in ("gold", "pred", "matched"):
                items[k] += c["items"][k]
            item_fields.update(c["items"]["field_correct"])
            errors += [{"doc": doc, "repeat": rep, "field": f, "kind": "item", "gold": str(gv_), "pred": str(pv_)}
                       for f, gv_, pv_ in c["items"]["errors"]]
            if c["items"]["matched"] < max(c["items"]["gold"], c["items"]["pred"]):
                errors.append({"doc": doc, "repeat": rep, "field": "items", "kind": "lines",
                               "gold": f"{c['items']['gold']} рядків", "pred": f"{c['items']['pred']} рядків, "
                                                                                f"зіставлено {c['items']['matched']}"})
            vat.update({k: v for k, v in c["vat"].items()})
            cat_conf[(c["category"]["gold"], c["category"]["pred"])] += 1
            if c["category"]["gold"] != c["category"]["pred"]:
                errors.append({"doc": doc, "repeat": rep, "field": "category", "kind": "class",
                               "gold": c["category"]["gold"], "pred": c["category"]["pred"]})

    m["golden_docs"] = len(gold_docs)
    m["fields"] = {f: _frac(s["correct"] + s["both_null"], sum(s.values())) for f, s in fstat.items()}
    scalar_tot = [fstat[f] for f in SCALAR_FIELDS if f in fstat]
    m["field_accuracy_micro"] = _frac(sum(s["correct"] + s["both_null"] for s in scalar_tot),
                                      sum(sum(s.values()) for s in scalar_tot))
    null_slots = sum(fstat[f]["both_null"] + fstat[f]["hallucinated"] for f in EXTRACTIVE_FIELDS if f in fstat)
    m["hallucinated"] = _frac(sum(fstat[f]["hallucinated"] for f in EXTRACTIVE_FIELDS if f in fstat), null_slots)
    m["missed"] = _frac(sum(fstat[f]["missed"] for f in EXTRACTIVE_FIELDS if f in fstat),
                        sum(fstat[f]["correct"] + fstat[f]["wrong"] + fstat[f]["missed"]
                            for f in EXTRACTIVE_FIELDS if f in fstat))
    prec = items["matched"] / items["pred"] if items["pred"] else None
    rec = items["matched"] / items["gold"] if items["gold"] else None
    m["items"] = {
        "precision": round(prec, 4) if prec is not None else None,
        "recall": round(rec, 4) if rec is not None else None,
        "f1": round(2 * prec * rec / (prec + rec), 4) if prec and rec else None,
        "matched_field_accuracy": {f: _frac(item_fields[f], items["matched"])
                                   for f in ITEM_FIELDS},
    }
    m["vat"] = {"group_recall": _frac(vat["matched"], vat["gold"]),
                "rate_correct": _frac(vat["rate_correct"], vat["matched"]),
                "amount_correct": _frac(vat["amount_correct"], vat["matched"])}
    assert CLASSIFICATION_FIELDS == ["category"]
    m["category"] = {"accuracy": _frac(sum(v for (g, p), v in cat_conf.items() if g == p), sum(cat_conf.values())),
                     "confusion": {f"{g}->{p}": v for (g, p), v in sorted(cat_conf.items())}}
    m["by_segment_field_accuracy"] = {s: _frac(*v) for s, v in sorted(seg_correct.items())}
    m["stability_all_repeats_identical"] = _frac(sum(stability), len(stability)) if stability else None
    return m, errors


def golden_arithmetic(golden: dict[str, Receipt]) -> dict[str, Any]:
    """Базова лінія: скільки golden-чеків самі по собі сходяться. Розбіжність тут — проблема каси, не моделі."""
    acc = defaultdict(lambda: [0, 0])
    for r in golden.values():
        for k, v in arithmetic_checks(r).items():
            if v is not None:
                acc[k][0] += v
                acc[k][1] += 1
    return {k: _frac(*v) for k, v in acc.items()}
