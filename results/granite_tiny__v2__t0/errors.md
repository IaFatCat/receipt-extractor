# Помилки на golden: granite_tiny__v2__t0

| doc | r | поле | тип | golden | модель |
|---|---|---|---|---|---|
| azk_01 | 0 | seller.name | wrong | ПП "УКРПАЛЕТСИСТЕМ" | ЗАО ‚вул, Харкзвське woce, 13 |
| azk_01 | 0 | seller.tax_id | missed | 32285225 | None |
| azk_01 | 0 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_01 | 0 | receipt_number | missed | 448678 | None |
| azk_01 | 0 | fiscal_number | missed | 3001071005 | None |
| azk_01 | 0 | issued_at | missed | 2026-08-28 21:33:14 | None |
| azk_01 | 0 | total | wrong | 2065.60 | 27120.6 |
| azk_01 | 0 | items | lines | 1 рядків | 4 рядків, зіставлено 0 |
| azk_01 | 0 | category | class | fuel | other |
| azk_04 | 0 | seller.vat_payer_number | wrong | 383053623016 | 363052623016 |
| azk_04 | 0 | receipt_number | missed | 3240140 | None |
| azk_04 | 0 | fiscal_number | missed | 3001212342 | None |
| azk_04 | 0 | issued_at | missed | 2026-06-21 19:06:56 | None |
| azk_04 | 0 | items[0].name | item | Бензин А-95 | Бензин Автонобтльний |
| azk_04 | 0 | items[0].qty | item | 25.79 | 0.25 |
| azk_04 | 0 | items[0].unit_price | item | 76.90 | None |
| azk_04 | 0 | items[0].vat_group | item | А | 21 |
| azk_04 | 0 | items | lines | 1 рядків | 3 рядків, зіставлено 1 |
| azk_11 | 0 | seller.tax_id | wrong | 32285225 | 2404110010 |
| azk_11 | 0 | seller.vat_payer_number | wrong | 322852206095 | X 175,00 |
| azk_11 | 0 | receipt_number | missed | 495195 | None |
| azk_11 | 0 | fiscal_number | missed | 3001071004 | None |
| azk_11 | 0 | issued_at | wrong | 2026-06-25 18:19:00 | 1806-02-24 18:35:20+00:00 |
| azk_11 | 0 | total | wrong | 731.00 | 751 |
| azk_11 | 0 | items[0].name | item | Сигарети JTI Camel Blue | Сигарети УП Сане} Blue |
| azk_11 | 0 | items[0].vat_group | item | Б | 3 |
| azk_11 | 0 | items | lines | 4 рядків | 2 рядків, зіставлено 1 |
| azk_11 | 0 | category | class | other | transport |
| food_01 | 0 | seller.name | wrong | ПІІ "МакДональдз Юкрейн Лтд" | МакДональйз Юкрейн Мга |
| food_01 | 0 | receipt_number | missed | 000205557 | None |
| food_01 | 0 | fiscal_number | missed | 3000932994 | None |
| food_01 | 0 | issued_at | wrong | 2026-05-25 21:51:01 | 7505-05-25 21:51:01+03:00 |
| food_01 | 0 | total | wrong | 325.00 | 580 |
| food_01 | 0 | items | lines | 3 рядків | 4 рядків, зіставлено 0 |
| food_01 | 0 | category | class | meals | other |
| food_03 | 0 | seller.name | wrong | GoH Craft Pub | Пастеризоване ПОПЕЛКА ЛАГЕР |
| food_03 | 0 | issued_at | missed | 2026-04-24 19:43:00 | None |
| food_03 | 0 | payment_method | wrong | card | cash |
| food_03 | 0 | items[4].name | item | Донер з куркою та грибами | Донер 3 куркою 1 318,00 |
| food_03 | 0 | items[6].name | item | Пиво світле Ne IPA Outback (келих 0.5) | Пиво світле Ne 1 218,00 |
| food_03 | 0 | items[5].name | item | Пиво MUZA IPA (5,4%) ПЕТ КЕГ 30л. Superdelic (келих 0.5) | Пиво MUZA IPA 2 188,00 |
| food_03 | 0 | items[5].qty | item | 2 | 1 |
| food_03 | 0 | items[5].unit_price | item | 188.00 | None |
| food_03 | 0 | items[3].name | item | Пиво MUZA IPA (5,4%) ПЕТ КЕГ 30л. Superdelic (келих 0.3) | Пиво MUZA IPA 2 123,00 |
| food_03 | 0 | items[3].qty | item | 2 | 1 |
| food_03 | 0 | items[3].unit_price | item | 123.00 | None |
| food_03 | 0 | items[1].name | item | Пиво світле "Бургомістр Rein Пілснер", л (келих 0.5) | Пиво світле 1 188,00 |
| food_03 | 0 | items[9].unit_price | item | 208.00 | None |
| food_03 | 0 | items[9].amount | item | 208.00 | 336 |
| food_03 | 0 | items[10].name | item | Пиво Rebrew світле нефільтроване непастеризоване < POPELKA L | Пиво Rebrew З 103,00 |
| food_03 | 0 | items[10].qty | item | 3 | 1 |
| food_03 | 0 | items[10].unit_price | item | 103.00 | None |
| food_03 | 0 | items[8].name | item | Фісташки 50г | Пиво світле 1 188,00 |
| food_03 | 0 | items | lines | 11 рядків | 10 рядків, зіставлено 8 |
| food_03 | 0 | category | class | meals | pharmacy |
| fop_01 | 0 | seller.name | wrong | ФО-П Федик О.Б. | Магазин "Наркетопт" |
| fop_01 | 0 | receipt_number | missed | 11650133 | None |
| fop_01 | 0 | fiscal_number | missed | 3001247585 | None |
| fop_01 | 0 | issued_at | missed | 2026-06-20 15:52:37 | None |
| fop_01 | 0 | items[2].discount | item | 0.76 | None |
| fop_01 | 0 | items[7].name | item | 110936-Пакет п/е майка 340*550 МАРКЕТОПТ | 110936- Пакет п/е майка 34 |
| fop_01 | 0 | items[7].discount | item | 0.28 | None |
| fop_01 | 0 | items[0].name | item | 106043-Хліб ІЛОНА Староукраїнський 500 г | 106043-Хліб ІЛОНА тарілка |
| fop_01 | 0 | items[0].discount | item | 1.86 | None |
| fop_01 | 0 | items[6].name | item | 154745-ВВ Круасан Шоколад 350г | 154737- BB Круасан зі смаком маракуйї 385 г OAs |
| fop_01 | 0 | items[6].discount | item | 3.64 | None |
| fop_01 | 0 | items[4].name | item | 154733-ВВ Круасан Малина 385г | 21406 BB Круасан Шоколад я |
| fop_01 | 0 | items[4].discount | item | 3.03 | None |
| fop_01 | 0 | items[5].name | item | 154737-ВВ Круасан зі смаком маракуйї 385 г | 3685г 75.008 :+. Знинка дпявласн. Карти ЗА 7 |
| fop_01 | 0 | items[5].discount | item | 3.03 | None |
| fop_01 | 0 | items | lines | 8 рядків | 7 рядків, зіставлено 6 |
| fop_02 | 0 | seller.name | wrong | ЗОРІНА КРІСТІНА ПАВЛІВНА | МАГАЗИН Ш |
| fop_02 | 0 | seller.tax_id | missed | 2981206608 | None |
| fop_02 | 0 | seller.vat_payer_number | hallucinated | None | 2081200608 |
| fop_02 | 0 | receipt_number | missed | 9988 | None |
| fop_02 | 0 | fiscal_number | missed | 3001258680 | None |
| fop_02 | 0 | issued_at | missed | 2026-09-05 17:35:20 | None |
| fop_02 | 0 | items[3].qty | item | 0.316 | 369.5 |
| fop_02 | 0 | items[3].unit_price | item | 369.50 | None |
| fop_02 | 0 | items[1].name | item | СОСИСКИ ДИТЯЧІ В/С (ЧЕРЕВА) (Б) | ДИТЯЧІ СОСИСКИ |
| fop_02 | 0 | items[1].qty | item | 0.450 | 54.5 |
| fop_02 | 0 | items[1].unit_price | item | 254.50 | None |
| fop_02 | 0 | items[2].qty | item | 1 | 25.79 |
| fop_02 | 0 | items[2].unit_price | item | 0.40 | None |
| fop_02 | 0 | items[2].amount | item | 0.40 | 350 |
| fop_02 | 0 | items[0].name | item | СИР РАДОМЕР СЕРЕНАДА 45% КГ | СЕРЕНАДА 455 КГ |
| fop_02 | 0 | items[0].qty | item | 0.294 | 419 |
| fop_02 | 0 | items[0].unit_price | item | 419.90 | 0.29 |
| fop_02 | 0 | items[0].amount | item | 123.45 | 123.95 |
| fop_02 | 0 | items | lines | 4 рядків | 7 рядків, зіставлено 4 |
| shop_01 | 0 | seller.name | wrong | ТОВ "Приватінвест" | TOB "IIpuBarinBect" |
| shop_01 | 0 | seller.vat_payer_number | wrong | 215505526546 | 21550555 |
| shop_01 | 0 | receipt_number | missed | q64Dxa1JXX0 | None |
| shop_01 | 0 | issued_at | missed | 2026-09-08 14:59:34 | None |
| shop_01 | 0 | items | lines | 1 рядків | 3 рядків, зіставлено 1 |
| shop_01 | 0 | category | class | office | other |
| shop_02 | 0 | * |  |  | FAILED |
| super_01 | 0 | seller.name | wrong | ТОВ "НОВУС УКРАЇНА" | ТОВ  |
| super_01 | 0 | seller.vat_payer_number | missed | 360036026593 | None |
| super_01 | 0 | receipt_number | missed | 106038 | None |
| super_01 | 0 | fiscal_number | missed | 3000780445 | None |
| super_01 | 0 | items[5].qty | item | 1 | 3 |
| super_01 | 0 | items[1].qty | item | 0.144 | 1 |
| super_01 | 0 | items[1].unit_price | item | 999.00 | None |
| super_01 | 0 | items[1].vat_group | item | А | None |
| super_01 | 0 | items[0].qty | item | 1 | 5 |
| super_01 | 0 | items[0].vat_group | item | А | None |
| super_01 | 0 | items[13].name | item | Пакет майка зелений біо | пакет майка зелений 610 1.49 A |
| super_01 | 0 | items[13].vat_group | item | А | None |
| super_01 | 0 | items[6].amount | item | 38.49 | 8.49 |
| super_01 | 0 | items[4].amount | item | 99.99 | 45 |
| super_01 | 0 | items[4].vat_group | item | А | None |
| super_01 | 0 | items[12].name | item | Хліб Бородинський Кулиничі н/ск. 400г | alk Hni6 Бородинський Кулиничі н/ск. 4 19 4 |
| super_01 | 0 | items[12].amount | item | 40.79 | 4 |
| super_01 | 0 | items[12].vat_group | item | А | None |
| super_01 | 0 | items[2].name | item | Корейка по кіровоград.Ятрань к/в в/г ваг | 0 вка по к! ово град. Ятрань к/в в |
| super_01 | 0 | items[2].qty | item | 0.226 | 1 |
| super_01 | 0 | items[2].unit_price | item | 699.00 | None |
| super_01 | 0 | items[2].amount | item | 157.97 | 17.97 |
| super_01 | 0 | items[2].vat_group | item | А | None |
| super_01 | 0 | items[9].name | item | Яйце куряче С0 Молодильне Ясенсвіт 10шт | ai Anne куряче CO Молодильне AcexHcBiT |
| super_01 | 0 | items[9].amount | item | 72.99 | 17.97 |
| super_01 | 0 | items[9].vat_group | item | А | None |
| super_01 | 0 | items[3].name | item | Шинка ювілейна Ятрань к/в в/г т/у ваг | ти ювілейна Ятрань к/в В/Г ШИ ый |
| super_01 | 0 | items[3].qty | item | 0.216 | 1 |
| super_01 | 0 | items[3].unit_price | item | 461.40 | None |
| super_01 | 0 | items[3].amount | item | 99.66 | 99.99 |
| super_01 | 0 | items[10].name | item | Сметана 20% Галичина 300г стакан | ФН 3000780445 | |
| super_01 | 0 | items[10].vat_group | item | А | None |
| super_01 | 0 | items[7].name | item | Йогурт 2,2% Ліс. ягода Галичина ПЕТ300г | Штрих код 4820222762816 |
| super_01 | 0 | items | lines | 14 рядків | 34 рядків, зіставлено 12 |
