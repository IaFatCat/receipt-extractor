"""CLI:
    python -m extractor run [--models haiku qwen] [--prompts v1]
    python -m extractor report
    python -m extractor golden-draft --run haiku__v1__t0 --docs r01 r05 …
"""

from __future__ import annotations

import argparse
import asyncio
import json

from .config import GOLDEN, RESULTS, ROOT, load_experiments
from .report import update_report
from .runner import run_all


def golden_draft(run_id: str, docs: list[str] | None) -> None:
    """Чернетка golden з виходу моделі — ЛИШЕ як заготовка для ручної перевірки кожного поля.
    Упередження на користь моделі-джерела треба згадати у звіті."""
    src = RESULTS / run_id / "outputs"
    dst = ROOT / "data" / "golden_draft"
    dst.mkdir(parents=True, exist_ok=True)
    n = 0
    for f in sorted(src.glob("*__r0.json")):
        doc = f.name.removesuffix("__r0.json")
        if (docs and doc not in docs) or (GOLDEN / f"{doc}.json").exists():
            continue
        o = json.loads(f.read_text(encoding="utf-8"))
        if o.get("data"):
            (dst / f"{doc}.json").write_text(json.dumps(o["data"], ensure_ascii=False, indent=2), encoding="utf-8")
            n += 1
    print(f"{n} чернеток у data/golden_draft/. Перевір КОЖНЕ поле проти тексту і перенеси в data/golden/.")


def main() -> None:
    ap = argparse.ArgumentParser(prog="extractor")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--models", nargs="*")
    r.add_argument("--prompts", nargs="*")
    r.add_argument("--sampling", nargs="*", help="лише ці конфігурації семплінгу, напр. t0")
    r.add_argument("--golden-only", action="store_true", help="лише чеки з golden set")
    sub.add_parser("report")
    g = sub.add_parser("golden-draft")
    g.add_argument("--run", required=True)
    g.add_argument("--docs", nargs="*")
    a = ap.parse_args()
    if a.cmd == "run":
        asyncio.run(run_all(load_experiments(), only_models=a.models, only_prompts=a.prompts,
                            only_sampling=a.sampling, golden_only=a.golden_only))
        update_report()
    elif a.cmd == "report":
        update_report()
    else:
        golden_draft(a.run, a.docs)


if __name__ == "__main__":
    main()
