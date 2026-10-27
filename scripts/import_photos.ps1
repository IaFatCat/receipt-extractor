# Копіює оригінали фото в data\private\photos під іменами датасету. Оригінали не змінюються.
# Запуск з кореня проєкту:  .\scripts\import_photos.ps1 -Source "C:\шлях\до\ЧекиДляРозпізнавання"
param([Parameter(Mandatory=$true)][string]$Source)
$ErrorActionPreference = "Stop"
$dst = Join-Path $PSScriptRoot "..\data\private\photos"
New-Item -ItemType Directory -Force $dst | Out-Null
$map = [ordered]@{
    "20260528_195018.jpg" = "super_05.jpg"
    "20260625_210020.jpg" = "azk_11.jpg"
    "20260625_210105.jpg" = "super_06.jpg"
    "20260713_195415.jpg" = "azk_05.jpg"
    "20260727_221928.jpg" = "food_05.jpg"
    "20260817_213648.jpg" = "azk_06.jpg"
    "20260822_193927.jpg" = "azk_07.jpg"
    "20260822_193949.jpg" = "azk_08.jpg"
    "20260905_180355.jpg" = "fop_04.jpg"
    "20260909_080953.jpg" = "azk_09.jpg"
    "20260909_081003.jpg" = "azk_10.jpg"
    "apteka_20260809_183251.jpg" = "super_02.jpg"
    "azk_20260621_201931.jpg" = "azk_04.jpg"
    "azk_20260625_210046.jpg" = "azk_12.jpg"
    "azk_20260809_180533.jpg" = "azk_13.jpg"
    "azk_20260828_220956.jpg" = "azk_01.jpg"
    "azk_20260909_081010.jpg" = "azk_02.jpg"
    "clothes_20260628_213530.jpg" = "shop_04.jpg"
    "epik_20260524_210729.jpg" = "shop_02.jpg"
    "epik_20260822_195142.jpg" = "shop_03.jpg"
    "fastfood_20260525_220132.jpg" = "food_01.jpg"
    "fastfood_20260822_200121.jpg" = "food_02.jpg"
    "meel_20260620_161231.jpg" = "fop_01.jpg"
    "meel_20260713_195428.jpg" = "super_03.jpg"
    "meel_20260723_184547.jpg" = "super_01.jpg"
    "meel_20260905_180401.jpg" = "fop_02.jpg"
    "monitor_20260909_081141.jpg" = "shop_01.jpg"
    "other_20260722_194449.jpg" = "fop_03.jpg"
    "pivo_20260424_194724.jpg" = "food_03.jpg"
    "pivo_20260501_204829.jpg" = "food_04.jpg"
    "tabaco_20260828_220938.jpg" = "azk_03.jpg"
    "tabaco_20260909_081114.jpg" = "super_04.jpg"
}
$ok = 0
foreach ($k in $map.Keys) {
    $src = Join-Path $Source $k
    if (-not (Test-Path -LiteralPath $src)) { Write-Warning "Немає файлу: $k"; continue }
    Copy-Item -LiteralPath $src -Destination (Join-Path $dst $map[$k]) -Force
    $ok++
}
Write-Host "Скопійовано $ok з $($map.Count) фото в $dst"
