.PHONY: run report test install ocr mask lint

# Одна команда для ментора: ставить залежності, проганяє доступні моделі, будує REPORT.md.
# Немає ключа в .env -> платна модель пропускається; немає Ollama -> локальна пропускається;
# звіт у будь-якому разі будується з закомічених results/.
run: install
	uv run python -m extractor run
	@echo "Готово: REPORT.md"

report:
	uv run python -m extractor report

install:
	uv sync --quiet

test:
	uv run pytest -q

lint:
	uv run ruff check src tests scripts

# Підготовка даних (лише локально, data/private/ не в git)
ocr:
	uv run --extra ocr python scripts/ocr.py data/private/photos data/private/ocr

mask:
	uv run python scripts/mask.py data/private/ocr data/texts
