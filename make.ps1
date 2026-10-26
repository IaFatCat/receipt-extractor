# Windows-аналог Makefile, ті самі цілі:  .\make.ps1 run | report | test | ocr | mask | lint
# Якщо PowerShell блокує скрипт:  powershell -ExecutionPolicy Bypass -File .\make.ps1 run
param([ValidateSet("run", "report", "test", "install", "ocr", "mask", "lint")][string]$Task = "run")

$ErrorActionPreference = "Stop"
$env:PYTHONUTF8 = "1"   # кирилиця у виводі та файлах без сюрпризів з кодовою сторінкою консолі

function Invoke-Uv { uv @args; if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE } }

switch ($Task) {
    "install" { Invoke-Uv sync --quiet }
    "run"     { Invoke-Uv sync --quiet; Invoke-Uv run python -m extractor run; Write-Host "Готово: REPORT.md" }
    "report"  { Invoke-Uv run python -m extractor report }
    "test"    { Invoke-Uv run pytest -q }
    "lint"    { Invoke-Uv run ruff check src tests scripts }
    "ocr"     { Invoke-Uv run --extra ocr python scripts/ocr.py data/private/photos data/private/ocr }
    "mask"    { Invoke-Uv run python scripts/mask.py data/private/ocr data/texts }
}
