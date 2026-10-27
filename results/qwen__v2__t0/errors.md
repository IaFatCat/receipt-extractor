# Помилки на golden: qwen__v2__t0

| doc | r | поле | тип | golden | модель |
|---|---|---|---|---|---|
| azk_01 | 0 | seller.name | wrong | ПП "УКРПАЛЕТСИСТЕМ" | АГЗП |
| azk_01 | 0 | seller.tax_id | missed | 32285225 | None |
| azk_01 | 0 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_01 | 0 | receipt_number | missed | 448678 | None |
| azk_01 | 0 | fiscal_number | missed | 3001071005 | None |
| azk_01 | 0 | issued_at | wrong | 2026-08-28 21:33:14 | 2808-10-23 21:23:14+00:00 |
| azk_01 | 0 | total | wrong | 2065.60 | 205.6 |
| azk_01 | 0 | payment_method | wrong | card | cash |
| azk_01 | 0 | items | lines | 1 рядків | 1 рядків, зіставлено 0 |
| azk_01 | 0 | category | class | fuel | groceries |
| azk_04 | 0 | seller.vat_payer_number | missed | 383053623016 | None |
| azk_04 | 0 | receipt_number | missed | 3240140 | None |
| azk_04 | 0 | fiscal_number | missed | 3001212342 | None |
| azk_04 | 0 | issued_at | wrong | 2026-06-21 19:06:56 | 2021-06-21 19:06:56+00:00 |
| azk_04 | 0 | items[0].name | item | Бензин А-95 | Бензин A-95-Epp05-E0 |
| azk_04 | 0 | items[0].qty | item | 25.79 | 19.8325 |
| azk_04 | 0 | items[0].unit_price | item | 76.90 | None |
| azk_04 | 0 | items[0].vat_group | item | А | В |
| azk_11 | 0 | seller.tax_id | wrong | 32285225 | 2402209020 |
| azk_11 | 0 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_11 | 0 | receipt_number | missed | 495195 | None |
| azk_11 | 0 | fiscal_number | missed | 3001071004 | None |
| azk_11 | 0 | issued_at | wrong | 2026-06-25 18:19:00 | 2026-06-25 18:35:20+00:00 |
| azk_11 | 0 | total | wrong | 731.00 | 751 |
| azk_11 | 0 | items[0].name | item | Сигарети JTI Camel Blue | Сигарети УП Сане} Blue |
| azk_11 | 0 | items[0].unit_price | item | 175.00 | None |
| azk_11 | 0 | items[0].vat_group | item | Б | None |
| azk_11 | 0 | items | lines | 4 рядків | 1 рядків, зіставлено 1 |
| azk_11 | 0 | category | class | other | groceries |
| food_01 | 0 | seller.name | wrong | ПІІ "МакДональдз Юкрейн Лтд" | МакДональйз Юкрейн Мга |
| food_01 | 0 | seller.vat_payer_number | missed | 237444526652 | None |
| food_01 | 0 | receipt_number | missed | 000205557 | None |
| food_01 | 0 | fiscal_number | missed | 3000932994 | None |
| food_01 | 0 | issued_at | wrong | 2026-05-25 21:51:01 | 2025-05-04 21:51:01+00:00 |
| food_01 | 0 | items[2].name | item | АПЕЛЬС СІК ВЕЛ МЕНЮ додатково | АПЕЛЬС СТК ВЕЛ МЕНЮ |
| food_01 | 0 | items[2].vat_group | item | А | 8 |
| food_01 | 0 | items | lines | 3 рядків | 2 рядків, зіставлено 2 |
| food_01 | 0 | category | class | meals | groceries |
| food_03 | 0 | seller.name | wrong | GoH Craft Pub | bypromictp |
| food_03 | 0 | issued_at | missed | 2026-04-24 19:43:00 | None |
| food_03 | 0 | payment_method | wrong | card | cash |
| food_03 | 0 | items[10].name | item | Пиво Rebrew світле нефільтроване непастеризоване < POPELKA L | Пиво Rebrew світле нефільтроване непастеризоване (келих 0.3) |
| food_03 | 0 | items[7].name | item | Пиво Цитадель Хоппі Келлербір, кега 28л Хмільний Нуль (келих | Пиво Цитадель (келих 0.5) |
| food_03 | 0 | items[4].name | item | Донер з куркою та грибами | Донер 3 куркою (келих 0.5) |
| food_03 | 0 | items[5].name | item | Пиво MUZA IPA (5,4%) ПЕТ КЕГ 30л. Superdelic (келих 0.5) | Пиво MUZA IPA |
| food_03 | 0 | items[3].name | item | Пиво MUZA IPA (5,4%) ПЕТ КЕГ 30л. Superdelic (келих 0.3) | Пиво MUZA IPA |
| food_03 | 0 | items[1].name | item | Пиво світле "Бургомістр Rein Пілснер", л (келих 0.5) | Пиво світле 1 (келих 0.5) |
| food_03 | 0 | items[1].unit_price | item | 158.00 | 188 |
| food_03 | 0 | items[1].amount | item | 158.00 | 188 |
| food_03 | 0 | items | lines | 11 рядків | 10 рядків, зіставлено 10 |
| food_03 | 0 | category | class | meals | groceries |
| fop_01 | 0 | seller.name | wrong | ФО-П Федик О.Б. | ТОВ "Наркетопт" |
| fop_01 | 0 | seller.vat_payer_number | missed | 305740855920 | None |
| fop_01 | 0 | receipt_number | missed | 11650133 | None |
| fop_01 | 0 | fiscal_number | missed | 3001247585 | None |
| fop_01 | 0 | issued_at | wrong | 2026-06-20 15:52:37 | 2020-06-26 15:52:37+00:00 |
| fop_01 | 0 | items[1].discount | item | 0.94 | None |
| fop_01 | 0 | items[2].discount | item | 0.76 | None |
| fop_01 | 0 | items[0].discount | item | 1.86 | None |
| fop_01 | 0 | items[6].name | item | 154745-ВВ Круасан Шоколад 350г | 154737-BB Круасан зі смак ом маракуйї 385 г |
| fop_01 | 0 | items[6].discount | item | 3.64 | None |
| fop_01 | 0 | items[4].unit_price | item | 75.70 | None |
| fop_01 | 0 | items[4].amount | item | 75.70 | 75 |
| fop_01 | 0 | items[4].discount | item | 3.03 | None |
| fop_01 | 0 | items[3].unit_price | item | 23.60 | None |
| fop_01 | 0 | items[3].amount | item | 23.60 | 75.7 |
| fop_01 | 0 | items[3].discount | item | 0.94 | None |
| fop_01 | 0 | items[7].name | item | 110936-Пакет п/е майка 340*550 МАРКЕТОПТ | 1406-BB Круасан Шоколад я 350 0.08 |
| fop_01 | 0 | items[7].discount | item | 0.28 | None |
| fop_01 | 0 | items | lines | 8 рядків | 7 рядків, зіставлено 7 |
| fop_02 | 0 | seller.name | wrong | ЗОРІНА КРІСТІНА ПАВЛІВНА | МАГАЗИН Ш |
| fop_02 | 0 | seller.tax_id | wrong | 2981206608 | 2081200608 |
| fop_02 | 0 | receipt_number | missed | 9988 | None |
| fop_02 | 0 | fiscal_number | missed | 3001258680 | None |
| fop_02 | 0 | issued_at | wrong | 2026-09-05 17:35:20 | 2026-05-16 17:35:20+00:00 |
| fop_02 | 0 | items[1].qty | item | 0.450 | 0.144 |
| fop_02 | 0 | items[1].unit_price | item | 254.50 | None |
| fop_02 | 0 | items[1].amount | item | 114.53 | 350 |
| fop_02 | 0 | items[1].vat_group | item | Н | Б |
| fop_02 | 0 | items[2].qty | item | 1 | 25.79 |
| fop_02 | 0 | items[2].unit_price | item | 0.40 | None |
| fop_02 | 0 | items[2].amount | item | 0.40 | 424 |
| fop_02 | 0 | items | lines | 4 рядків | 2 рядків, зіставлено 2 |
| shop_01 | 0 | seller.name | wrong | ТОВ "Приватінвест" | TOB "IIpuBarinBect" |
| shop_01 | 0 | seller.vat_payer_number | missed | 215505526546 | None |
| shop_01 | 0 | receipt_number | missed | q64Dxa1JXX0 | None |
| shop_01 | 0 | issued_at | wrong | 2026-09-08 14:59:34 | 2026-09-08 14:35:27+00:00 |
| shop_02 | 0 | seller.name | wrong | ТОВ "НОВА ЛІНІЯ 1" | ЛЬНИЙ КОМПЛЕКС |
| shop_02 | 0 | seller.tax_id | missed | 30728887 | None |
| shop_02 | 0 | seller.vat_payer_number | missed | 307288826516 | None |
| shop_02 | 0 | receipt_number | missed | 14556 | None |
| shop_02 | 0 | fiscal_number | missed | 3000786185 | None |
| shop_02 | 0 | issued_at | wrong | 2026-05-24 20:48:08 | 2405-06-20 20:48:08+00:00 |
| shop_02 | 0 | items[5].unit_price | item | 267.00 | None |
| shop_02 | 0 | items[4].name | item | Прокладка силіконова 1/2 | ПРокладка силіконова 1/2 20,10х 1= 20,10-A,%% |
| shop_02 | 0 | items[0].name | item | Карниз для душ. шторки B | Карниз ANA AYU. ШТОРКИ В fe 8% |
| shop_02 | 0 | items[8].name | item | Сигарети Camel Blue | Сигарети Camel Blue 175,00х 1= — 175,00-Б |
| shop_02 | 0 | items[7].name | item | Стіки TEREA Arbor Pearl | Crikw TEREA Arbor Pearl 175,00x 1= 175,00-Б |
| shop_02 | 0 | items[9].name | item | Стіки TEREA Amber | Crikw TEREA Amber 175,00x 1= 175 ,00-b ee |
| shop_02 | 0 | items[3].name | item | Кільця для шторки Bacche | Кільця для шторки Bacche 97,00x 1= o7,00-A |
| shop_02 | 0 | items[3].unit_price | item | 97.00 | None |
| shop_02 | 0 | items[3].amount | item | 97.00 | 7 |
| super_01 | 0 | seller.vat_payer_number | missed | 360036026593 | None |
| super_01 | 0 | receipt_number | missed | 106038 | None |
| super_01 | 0 | fiscal_number | missed | 3000780445 | None |
| super_01 | 0 | payment_method | wrong | card | cash |
| super_01 | 0 | items[13].vat_group | item | А | None |
| super_01 | 0 | items[9].name | item | Яйце куряче С0 Молодильне Ясенсвіт 10шт | куряче CO Молодильне AcexHcBiT |
| super_01 | 0 | items[11].amount | item | 119.00 | 9 |
| super_01 | 0 | items[8].unit_price | item | 35.89 | None |
| super_01 | 0 | items[8].amount | item | 19.67 | 35.89 |
| super_01 | 0 | items[8].vat_group | item | А | None |
| super_01 | 0 | items[1].qty | item | 0.144 | 16 |
| super_01 | 0 | items[1].unit_price | item | 999.00 | None |
| super_01 | 0 | items[1].amount | item | 143.86 | 461.4 |
| super_01 | 0 | items[1].vat_group | item | А | None |
| super_01 | 0 | items[6].amount | item | 38.49 | 8.49 |
| super_01 | 0 | items[4].name | item | Козинаки хомка насіння+льон АСК 450г | ювілейна Ятрань к/в В/Г ШИ |
| super_01 | 0 | items[7].name | item | Йогурт 2,2% Ліс. ягода Галичина ПЕТ300г | Ліс. ягода Галичина Пе 3.49 А |
| super_01 | 0 | items[7].amount | item | 38.49 | 2.28 |
| super_01 | 0 | items[0].name | item | Пакет середній 34*55 Novus 7кг | МАГАЗИН NG нори. КИЇВСЬКА бБЛАЄ bh sit |
| super_01 | 0 | items[0].vat_group | item | А | None |
| super_01 | 0 | items | lines | 14 рядків | 11 рядків, зіставлено 11 |
