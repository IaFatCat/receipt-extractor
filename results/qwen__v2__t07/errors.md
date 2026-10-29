# Помилки на golden: qwen__v2__t07

| doc | r | поле | тип | golden | модель |
|---|---|---|---|---|---|
| azk_01 | 0 | seller.name | wrong | ПП "УКРПАЛЕТСИСТЕМ" | га АГЗП |
| azk_01 | 0 | seller.tax_id | missed | 32285225 | None |
| azk_01 | 0 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_01 | 0 | receipt_number | missed | 448678 | None |
| azk_01 | 0 | fiscal_number | missed | 3001071005 | None |
| azk_01 | 0 | issued_at | missed | 2026-08-28 21:33:14 | None |
| azk_01 | 0 | payment_method | wrong | card | cash |
| azk_01 | 0 | items[0].name | item | Бензин авт А95-Євро5-Е10 | ТЕРВІМА: ЗІКА |
| azk_01 | 0 | items[0].qty | item | 26.18 | 1 |
| azk_01 | 0 | items[0].unit_price | item | 78.90 | None |
| azk_01 | 0 | items[0].vat_group | item | А | None |
| azk_01 | 0 | category | class | fuel | groceries |
| azk_01 | 1 | seller.name | wrong | ПП "УКРПАЛЕТСИСТЕМ" | га АГЗП |
| azk_01 | 1 | seller.tax_id | missed | 32285225 | None |
| azk_01 | 1 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_01 | 1 | receipt_number | missed | 448678 | None |
| azk_01 | 1 | fiscal_number | missed | 3001071005 | None |
| azk_01 | 1 | issued_at | wrong | 2026-08-28 21:33:14 | 2808-10-23 21:23:14+00:00 |
| azk_01 | 1 | total | wrong | 2065.60 | 20.56 |
| azk_01 | 1 | payment_method | wrong | card | cash |
| azk_01 | 1 | items | lines | 1 рядків | 1 рядків, зіставлено 0 |
| azk_01 | 1 | category | class | fuel | transport |
| azk_01 | 2 | seller.name | wrong | ПП "УКРПАЛЕТСИСТЕМ" | ЗАО 'вул, Харкзвське woce, 13 |
| azk_01 | 2 | seller.tax_id | missed | 32285225 | None |
| azk_01 | 2 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_01 | 2 | receipt_number | missed | 448678 | None |
| azk_01 | 2 | fiscal_number | missed | 3001071005 | None |
| azk_01 | 2 | issued_at | missed | 2026-08-28 21:33:14 | None |
| azk_01 | 2 | total | wrong | 2065.60 | 205.6 |
| azk_01 | 2 | payment_method | wrong | card | cash |
| azk_01 | 2 | items | lines | 1 рядків | 1 рядків, зіставлено 0 |
| azk_01 | 2 | category | class | fuel | groceries |
| azk_04 | 0 | seller.vat_payer_number | wrong | 383053623016 | 363052623016 |
| azk_04 | 0 | receipt_number | missed | 3240140 | None |
| azk_04 | 0 | fiscal_number | missed | 3001212342 | None |
| azk_04 | 0 | issued_at | missed | 2026-06-21 19:06:56 | None |
| azk_04 | 0 | items[0].name | item | Бензин А-95 | Бензин A95-Epo5-E0 |
| azk_04 | 0 | items[0].qty | item | 25.79 | 1983.25 |
| azk_04 | 0 | items[0].unit_price | item | 76.90 | None |
| azk_04 | 0 | items[0].vat_group | item | А | В |
| azk_04 | 0 | category | class | fuel | transport |
| azk_04 | 1 | seller.vat_payer_number | missed | 383053623016 | None |
| azk_04 | 1 | receipt_number | missed | 3240140 | None |
| azk_04 | 1 | fiscal_number | missed | 3001212342 | None |
| azk_04 | 1 | issued_at | missed | 2026-06-21 19:06:56 | None |
| azk_04 | 1 | total | wrong | 1983.25 | 21.06 |
| azk_04 | 1 | items[0].name | item | Бензин А-95 | Бензин A95-Epo5-E0 |
| azk_04 | 1 | items[0].qty | item | 25.79 | 3 |
| azk_04 | 1 | items[0].unit_price | item | 76.90 | None |
| azk_04 | 1 | items[0].vat_group | item | А | В |
| azk_04 | 1 | category | class | fuel | transport |
| azk_04 | 2 | seller.tax_id | hallucinated | None | 363052623016 |
| azk_04 | 2 | seller.vat_payer_number | missed | 383053623016 | None |
| azk_04 | 2 | receipt_number | missed | 3240140 | None |
| azk_04 | 2 | fiscal_number | missed | 3001212342 | None |
| azk_04 | 2 | issued_at | missed | 2026-06-21 19:06:56 | None |
| azk_04 | 2 | total | wrong | 1983.25 | 20 |
| azk_04 | 2 | items[0].name | item | Бензин А-95 | Бензин Aa 1983 .25 В |
| azk_04 | 2 | items[0].qty | item | 25.79 | 1983.25 |
| azk_04 | 2 | items[0].unit_price | item | 76.90 | None |
| azk_04 | 2 | items[0].amount | item | 1983.25 | 20 |
| azk_04 | 2 | items[0].vat_group | item | А | None |
| azk_04 | 2 | category | class | fuel | transport |
| azk_11 | 0 | seller.tax_id | missed | 32285225 | None |
| azk_11 | 0 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_11 | 0 | receipt_number | missed | 495195 | None |
| azk_11 | 0 | fiscal_number | missed | 3001071004 | None |
| azk_11 | 0 | issued_at | wrong | 2026-06-25 18:19:00 | 2506-12-18 18:35:20+00:00 |
| azk_11 | 0 | total | wrong | 731.00 | 751 |
| azk_11 | 0 | items[0].name | item | Сигарети JTI Camel Blue | Сигарети УП Sanе Blue |
| azk_11 | 0 | items[0].unit_price | item | 175.00 | None |
| azk_11 | 0 | items[0].vat_group | item | Б | None |
| azk_11 | 0 | items | lines | 4 рядків | 1 рядків, зіставлено 1 |
| azk_11 | 0 | category | class | other | transport |
| azk_11 | 1 | seller.tax_id | missed | 32285225 | None |
| azk_11 | 1 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_11 | 1 | receipt_number | missed | 495195 | None |
| azk_11 | 1 | fiscal_number | missed | 3001071004 | None |
| azk_11 | 1 | issued_at | wrong | 2026-06-25 18:19:00 | 2026-06-25 18:35:20+00:00 |
| azk_11 | 1 | total | wrong | 731.00 | 289 |
| azk_11 | 1 | items[0].name | item | Сигарети JTI Camel Blue | Сигарети УП Sanе} Blue |
| azk_11 | 1 | items[0].qty | item | 2 | 0.144 |
| azk_11 | 1 | items | lines | 4 рядків | 1 рядків, зіставлено 1 |
| azk_11 | 1 | category | class | other | transport |
| azk_11 | 2 | seller.tax_id | missed | 32285225 | None |
| azk_11 | 2 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_11 | 2 | receipt_number | missed | 495195 | None |
| azk_11 | 2 | fiscal_number | missed | 3001071004 | None |
| azk_11 | 2 | issued_at | missed | 2026-06-25 18:19:00 | None |
| azk_11 | 2 | total | wrong | 731.00 | 751 |
| azk_11 | 2 | items[0].name | item | Сигарети JTI Camel Blue | Сигарети УП Сане} Blue |
| azk_11 | 2 | items[0].qty | item | 2 | 175 |
| azk_11 | 2 | items[0].unit_price | item | 175.00 | None |
| azk_11 | 2 | items[0].vat_group | item | Б | None |
| azk_11 | 2 | items | lines | 4 рядків | 1 рядків, зіставлено 1 |
| azk_11 | 2 | category | class | other | groceries |
| food_01 | 0 | seller.name | wrong | ПІІ "МакДональдз Юкрейн Лтд" | "МакДональйз Юкрейн Мга" |
| food_01 | 0 | seller.vat_payer_number | missed | 237444526652 | None |
| food_01 | 0 | receipt_number | missed | 000205557 | None |
| food_01 | 0 | fiscal_number | missed | 3000932994 | None |
| food_01 | 0 | issued_at | wrong | 2026-05-25 21:51:01 | 2025-05-07 21:51:01+00:00 |
| food_01 | 0 | items[2].vat_group | item | А | 8 |
| food_01 | 0 | items | lines | 3 рядків | 2 рядків, зіставлено 2 |
| food_01 | 0 | category | class | meals | groceries |
| food_01 | 1 | seller.name | wrong | ПІІ "МакДональдз Юкрейн Лтд" | МакДональдс Україна Мга |
| food_01 | 1 | seller.tax_id | hallucinated | None | 237444526652 |
| food_01 | 1 | seller.vat_payer_number | missed | 237444526652 | None |
| food_01 | 1 | receipt_number | missed | 000205557 | None |
| food_01 | 1 | fiscal_number | missed | 3000932994 | None |
| food_01 | 1 | issued_at | missed | 2026-05-25 21:51:01 | None |
| food_01 | 1 | items[2].name | item | АПЕЛЬС СІК ВЕЛ МЕНЮ додатково | АПЕЛЬСИННИЙ МЕНЮ |
| food_01 | 1 | items[2].vat_group | item | А | В |
| food_01 | 1 | items | lines | 3 рядків | 2 рядків, зіставлено 2 |
| food_01 | 1 | category | class | meals | groceries |
| food_01 | 2 | seller.name | wrong | ПІІ "МакДональдз Юкрейн Лтд" | "МакДональйз Юкрейн Мга" |
| food_01 | 2 | seller.vat_payer_number | missed | 237444526652 | None |
| food_01 | 2 | receipt_number | missed | 000205557 | None |
| food_01 | 2 | fiscal_number | missed | 3000932994 | None |
| food_01 | 2 | issued_at | missed | 2026-05-25 21:51:01 | None |
| food_01 | 2 | items[2].vat_group | item | А | None |
| food_01 | 2 | items[0].vat_group | item | А | None |
| food_01 | 2 | items | lines | 3 рядків | 2 рядків, зіставлено 2 |
| food_01 | 2 | category | class | meals | fuel |
| food_03 | 0 | seller.name | wrong | GoH Craft Pub | bypromictp |
| food_03 | 0 | issued_at | missed | 2026-04-24 19:43:00 | None |
| food_03 | 0 | payment_method | wrong | card | cash |
| food_03 | 0 | items[2].name | item | Асорті горіхів. | Асорті горіхів (келих 0,3) |
| food_03 | 0 | items[2].unit_price | item | 108.00 | None |
| food_03 | 0 | items[2].vat_group | item | None | 5% |
| food_03 | 0 | items[3].name | item | Пиво MUZA IPA (5,4%) ПЕТ КЕГ 30л. Superdelic (келих 0.3) | Пиво MUZA IPA (кетель 0.5) |
| food_03 | 0 | items[3].unit_price | item | 123.00 | None |
| food_03 | 0 | items[3].vat_group | item | None | 5. |
| food_03 | 0 | items | lines | 11 рядків | 3 рядків, зіставлено 2 |
| food_03 | 0 | category | class | meals | groceries |
| food_03 | 1 | seller.name | wrong | GoH Craft Pub | bypromictp |
| food_03 | 1 | issued_at | missed | 2026-04-24 19:43:00 | None |
| food_03 | 1 | payment_method | wrong | card | cash |
| food_03 | 1 | items[1].name | item | Пиво світле "Бургомістр Rein Пілснер", л (келих 0.5) | Пастеризоване ПІлснер, л (келих 0,5) |
| food_03 | 1 | items[1].unit_price | item | 158.00 | 188.00 |
| food_03 | 1 | items[1].amount | item | 158.00 | 188.00 |
| food_03 | 1 | items[1].vat_group | item | None | 5, |
| food_03 | 1 | items | lines | 11 рядків | 1 рядків, зіставлено 1 |
| food_03 | 1 | category | class | meals | groceries |
| food_03 | 2 | seller.name | wrong | GoH Craft Pub | bypromictp |
| food_03 | 2 | issued_at | wrong | 2026-04-24 19:43:00 | 1654-11-28 13:22:25+00:00 |
| food_03 | 2 | payment_method | wrong | card | cash |
| food_03 | 2 | items[10].name | item | Пиво Rebrew світле нефільтроване непастеризоване < POPELKA L | Пиво Rebrew світле нефільтроване непастеризоване (келих 0.5) |
| food_03 | 2 | items[4].name | item | Донер з куркою та грибами | Донер 3 куркою грибами (келих 0.5) |
| food_03 | 2 | items[3].name | item | Пиво MUZA IPA (5,4%) ПЕТ КЕГ 30л. Superdelic (келих 0.3) | Пиво MUZA IPA (келих 0.3) |
| food_03 | 2 | items[0].name | item | Пиво Rebrew світле нефільтроване непастеризоване < POPELKA L | Пастеризоване ' (ЛОПЕЛКА | ‚ ЛАГЕР)», 5%, ПЕТ-кег (келих 0,5 |
| food_03 | 2 | items[0].qty | item | 2 | 1 |
| food_03 | 2 | items[0].unit_price | item | 148.00 | 158 |
| food_03 | 2 | items[0].amount | item | 296.00 | 188 |
| food_03 | 2 | items | lines | 11 рядків | 5 рядків, зіставлено 5 |
| food_03 | 2 | category | class | meals | groceries |
| fop_01 | 0 | seller.name | wrong | ФО-П Федик О.Б. | Магазин "Наркетопт" |
| fop_01 | 0 | seller.vat_payer_number | missed | 305740855920 | None |
| fop_01 | 0 | receipt_number | missed | 11650133 | None |
| fop_01 | 0 | fiscal_number | missed | 3001247585 | None |
| fop_01 | 0 | issued_at | missed | 2026-06-20 15:52:37 | None |
| fop_01 | 0 | total | wrong | 347.42 | 237.44 |
| fop_01 | 0 | items[2].discount | item | 0.76 | None |
| fop_01 | 0 | items[2].vat_group | item | А | None |
| fop_01 | 0 | items[0].qty | item | 1 | 0.5 |
| fop_01 | 0 | items[0].discount | item | 1.86 | None |
| fop_01 | 0 | items[0].vat_group | item | А | None |
| fop_01 | 0 | items[1].discount | item | 0.94 | None |
| fop_01 | 0 | items[1].vat_group | item | А | None |
| fop_01 | 0 | items[6].name | item | 154745-ВВ Круасан Шоколад 350г | 154733-BB Круасан Малина 3685г |
| fop_01 | 0 | items[6].discount | item | 3.64 | None |
| fop_01 | 0 | items[6].vat_group | item | А | None |
| fop_01 | 0 | items[5].unit_price | item | 75.70 | None |
| fop_01 | 0 | items[5].amount | item | 75.70 | 6.9 |
| fop_01 | 0 | items[5].discount | item | 3.03 | None |
| fop_01 | 0 | items[5].vat_group | item | А | None |
| fop_01 | 0 | items[3].unit_price | item | 23.60 | None |
| fop_01 | 0 | items[3].amount | item | 23.60 | 75.7 |
| fop_01 | 0 | items[3].discount | item | 0.94 | None |
| fop_01 | 0 | items[3].vat_group | item | А | None |
| fop_01 | 0 | items[7].unit_price | item | 6.90 | None |
| fop_01 | 0 | items[7].amount | item | 6.90 | 5.24 |
| fop_01 | 0 | items[7].discount | item | 0.28 | None |
| fop_01 | 0 | items[7].vat_group | item | А | None |
| fop_01 | 0 | items | lines | 8 рядків | 7 рядків, зіставлено 7 |
| fop_01 | 1 | seller.name | wrong | ФО-П Федик О.Б. | ТОВ "Наркетопт" |
| fop_01 | 1 | seller.vat_payer_number | missed | 305740855920 | None |
| fop_01 | 1 | receipt_number | missed | 11650133 | None |
| fop_01 | 1 | fiscal_number | missed | 3001247585 | None |
| fop_01 | 1 | issued_at | wrong | 2026-06-20 15:52:37 | 2026-10-20 15:52:37+00:00 |
| fop_01 | 1 | items[1].discount | item | 0.94 | None |
| fop_01 | 1 | items[1].vat_group | item | А | None |
| fop_01 | 1 | items[2].discount | item | 0.76 | None |
| fop_01 | 1 | items[2].vat_group | item | А | None |
| fop_01 | 1 | items[0].discount | item | 1.86 | None |
| fop_01 | 1 | items[0].vat_group | item | А | None |
| fop_01 | 1 | items[6].name | item | 154745-ВВ Круасан Шоколад 350г | 154737-BB Круасан зі смаком маракуйї 385 г |
| fop_01 | 1 | items[6].discount | item | 3.64 | None |
| fop_01 | 1 | items[6].vat_group | item | А | None |
| fop_01 | 1 | items[4].unit_price | item | 75.70 | None |
| fop_01 | 1 | items[4].amount | item | 75.70 | 75 |
| fop_01 | 1 | items[4].discount | item | 3.03 | None |
| fop_01 | 1 | items[4].vat_group | item | А | None |
| fop_01 | 1 | items[3].unit_price | item | 23.60 | None |
| fop_01 | 1 | items[3].amount | item | 23.60 | 75.7 |
| fop_01 | 1 | items[3].discount | item | 0.94 | None |
| fop_01 | 1 | items[3].vat_group | item | А | None |
| fop_01 | 1 | items[7].name | item | 110936-Пакет п/е майка 340*550 МАРКЕТОПТ | 1406 BB Круасан Шоколад 350 г |
| fop_01 | 1 | items[7].discount | item | 0.28 | None |
| fop_01 | 1 | items[7].vat_group | item | А | None |
| fop_01 | 1 | items | lines | 8 рядків | 7 рядків, зіставлено 7 |
| fop_01 | 2 | seller.name | wrong | ФО-П Федик О.Б. | ТОВ "Наркетопт" |
| fop_01 | 2 | seller.vat_payer_number | missed | 305740855920 | None |
| fop_01 | 2 | receipt_number | missed | 11650133 | None |
| fop_01 | 2 | fiscal_number | missed | 3001247585 | None |
| fop_01 | 2 | issued_at | wrong | 2026-06-20 15:52:37 | 2026-10-20 15:52:37+00:00 |
| fop_01 | 2 | items[1].discount | item | 0.94 | None |
| fop_01 | 2 | items[2].discount | item | 0.76 | None |
| fop_01 | 2 | items[0].discount | item | 1.86 | None |
| fop_01 | 2 | items[6].name | item | 154745-ВВ Круасан Шоколад 350г | 154733-BB Круасан Малина 3685г |
| fop_01 | 2 | items[6].discount | item | 3.64 | None |
| fop_01 | 2 | items[6].vat_group | item | А | None |
| fop_01 | 2 | items[5].unit_price | item | 75.70 | None |
| fop_01 | 2 | items[5].amount | item | 75.70 | 6.9 |
| fop_01 | 2 | items[5].discount | item | 3.03 | None |
| fop_01 | 2 | items[5].vat_group | item | А | В |
| fop_01 | 2 | items[7].unit_price | item | 6.90 | None |
| fop_01 | 2 | items[7].amount | item | 6.90 | 2.08 |
| fop_01 | 2 | items[7].discount | item | 0.28 | None |
| fop_01 | 2 | items[3].unit_price | item | 23.60 | None |
| fop_01 | 2 | items[3].amount | item | 23.60 | 75.7 |
| fop_01 | 2 | items[3].discount | item | 0.94 | None |
| fop_01 | 2 | items[3].vat_group | item | А | None |
| fop_01 | 2 | items | lines | 8 рядків | 7 рядків, зіставлено 7 |
| fop_02 | 0 | seller.name | wrong | ЗОРІНА КРІСТІНА ПАВЛІВНА | МАГАЗИН Ш |
| fop_02 | 0 | seller.tax_id | wrong | 2981206608 | 2081200608 |
| fop_02 | 0 | receipt_number | missed | 9988 | None |
| fop_02 | 0 | fiscal_number | missed | 3001258680 | None |
| fop_02 | 0 | issued_at | wrong | 2026-09-05 17:35:20 | 2026-05-05 17:35:20+00:00 |
| fop_02 | 0 | items[3].qty | item | 0.316 | 369.5 |
| fop_02 | 0 | items[3].unit_price | item | 369.50 | None |
| fop_02 | 0 | items[3].vat_group | item | Н | ~ |
| fop_02 | 0 | items[1].qty | item | 0.450 | 0.144 |
| fop_02 | 0 | items[1].unit_price | item | 254.50 | None |
| fop_02 | 0 | items[1].amount | item | 114.53 | 35 |
| fop_02 | 0 | items[1].vat_group | item | Н | Б |
| fop_02 | 0 | items[2].qty | item | 1 | 4.4 |
| fop_02 | 0 | items[2].unit_price | item | 0.40 | None |
| fop_02 | 0 | items[2].amount | item | 0.40 | 54.5 |
| fop_02 | 0 | items[2].vat_group | item | Н | -Н |
| fop_02 | 0 | items | lines | 4 рядків | 3 рядків, зіставлено 3 |
| fop_02 | 1 | seller.name | wrong | ЗОРІНА КРІСТІНА ПАВЛІВНА | МАГАЗИН ШВЕЦЬКА |
| fop_02 | 1 | seller.tax_id | wrong | 2981206608 | 2081200608 |
| fop_02 | 1 | receipt_number | missed | 9988 | None |
| fop_02 | 1 | fiscal_number | wrong | 3001258680 | ТН001074017 |
| fop_02 | 1 | issued_at | wrong | 2026-09-05 17:35:20 | 2026-09-15 17:35:20+00:00 |
| fop_02 | 1 | items[2].name | item | ПАКЕТИ ФАСУВАЛЬНІ №9 10 МКР 1000 ШТ/УП | ПАКЕТИ СЕРАДАЧІ №9 10 МКР 1000 Вт |
| fop_02 | 1 | items[2].unit_price | item | 0.40 | None |
| fop_02 | 1 | items[2].amount | item | 0.40 | 54.5 |
| fop_02 | 1 | items[1].name | item | СОСИСКИ ДИТЯЧІ В/С (ЧЕРЕВА) (Б) | СОСИСКИ ДИТЯЧІ (в) ПАПЕРОВА упаковка |
| fop_02 | 1 | items[1].qty | item | 0.450 | 1 |
| fop_02 | 1 | items[1].unit_price | item | 254.50 | None |
| fop_02 | 1 | items[1].amount | item | 114.53 | 350 |
| fop_02 | 1 | items | lines | 4 рядків | 3 рядків, зіставлено 2 |
| fop_02 | 2 | seller.name | wrong | ЗОРІНА КРІСТІНА ПАВЛІВНА | МАГАЗИН БОРСКИХ ЯГОД |
| fop_02 | 2 | seller.tax_id | missed | 2981206608 | None |
| fop_02 | 2 | seller.vat_payer_number | hallucinated | None | 2081200608 |
| fop_02 | 2 | receipt_number | missed | 9988 | None |
| fop_02 | 2 | fiscal_number | missed | 3001258680 | None |
| fop_02 | 2 | issued_at | wrong | 2026-09-05 17:35:20 | 2026-05-17 17:35:20+00:00 |
| fop_02 | 2 | items[2].name | item | ПАКЕТИ ФАСУВАЛЬНІ №9 10 МКР 1000 ШТ/УП | ПАКЕТИ ЧАСЧИКАДHI №9 10 МКР 1000 WT |
| fop_02 | 2 | items[2].qty | item | 1 | 0.4 |
| fop_02 | 2 | items[2].unit_price | item | 0.40 | None |
| fop_02 | 2 | items[2].amount | item | 0.40 | 116.76 |
| fop_02 | 2 | items[2].vat_group | item | Н | -Н |
| fop_02 | 2 | items[1].name | item | СОСИСКИ ДИТЯЧІ В/С (ЧЕРЕВА) (Б) | СОСИСКИ ДИТЯЧІ (в) (в) |
| fop_02 | 2 | items[1].qty | item | 0.450 | 0.144 |
| fop_02 | 2 | items[1].unit_price | item | 254.50 | None |
| fop_02 | 2 | items[1].amount | item | 114.53 | 123.95 |
| fop_02 | 2 | items[1].vat_group | item | Н | -Н |
| fop_02 | 2 | items | lines | 4 рядків | 2 рядків, зіставлено 2 |
| shop_01 | 0 | seller.name | wrong | ТОВ "Приватінвест" | TOB "IIpuBarinBect" |
| shop_01 | 0 | seller.vat_payer_number | missed | 215505526546 | None |
| shop_01 | 0 | receipt_number | missed | q64Dxa1JXX0 | None |
| shop_01 | 0 | issued_at | missed | 2026-09-08 14:59:34 | None |
| shop_01 | 0 | items[0].name | item | Монітор Dell S2725DC (210-BSRL) | Монітор Dell $2725DC |
| shop_01 | 0 | items[0].vat_group | item | А | None |
| shop_01 | 1 | seller.name | wrong | ТОВ "Приватінвест" | TOB "IIpuBarinBect" |
| shop_01 | 1 | seller.vat_payer_number | missed | 215505526546 | None |
| shop_01 | 1 | receipt_number | missed | q64Dxa1JXX0 | None |
| shop_01 | 1 | total | wrong | 14062.00 | 14223.71 |
| shop_01 | 1 | items[0].qty | item | 1.000 | 4 |
| shop_01 | 1 | items | lines | 1 рядків | 2 рядків, зіставлено 1 |
| shop_01 | 2 | seller.name | wrong | ТОВ "Приватінвест" | TOB "IIpuBarinBect" |
| shop_01 | 2 | seller.vat_payer_number | missed | 215505526546 | None |
| shop_01 | 2 | receipt_number | wrong | q64Dxa1JXX0 | q64DxalJXX0 |
| shop_01 | 2 | issued_at | missed | 2026-09-08 14:59:34 | None |
| shop_01 | 2 | items[0].qty | item | 1.000 | 4 |
| shop_01 | 2 | category | class | office | other |
| shop_02 | 0 | seller.name | wrong | ТОВ "НОВА ЛІНІЯ 1" | ЛЬНИЙ КОМПЛЕКС |
| shop_02 | 0 | seller.tax_id | wrong | 30728887 | 341001040983 |
| shop_02 | 0 | seller.vat_payer_number | wrong | 307288826516 | 386185 14 30728887 |
| shop_02 | 0 | receipt_number | missed | 14556 | None |
| shop_02 | 0 | fiscal_number | missed | 3000786185 | None |
| shop_02 | 0 | issued_at | wrong | 2026-05-24 20:48:08 | 2405-08-26 20:48:08+00:00 |
| shop_02 | 0 | items[1].vat_group | item | А | None |
| shop_02 | 0 | items[6].vat_group | item | А | None |
| shop_02 | 0 | items[2].vat_group | item | А | None |
| shop_02 | 0 | items[5].unit_price | item | 267.00 | None |
| shop_02 | 0 | items[5].vat_group | item | А | None |
| shop_02 | 0 | items[4].name | item | Прокладка силіконова 1/2 | ПРокладка силіконова 1/2 20,10х 1= 20,10-A,%% |
| shop_02 | 0 | items[4].vat_group | item | А | None |
| shop_02 | 0 | items[0].name | item | Карниз для душ. шторки B | Карниз ANA AYU. ШТОРКИ В fe 8% |
| shop_02 | 0 | items[0].vat_group | item | А | None |
| shop_02 | 0 | items[8].name | item | Сигарети Camel Blue | Сигарети Camel Blue 175,00х 1= — 175,00-Б |
| shop_02 | 0 | items[8].vat_group | item | Б | None |
| shop_02 | 0 | items[7].name | item | Стіки TEREA Arbor Pearl | Crikw TEREA Arbor Pearl 175,00x 1= 175,00-Б |
| shop_02 | 0 | items[7].vat_group | item | Б | None |
| shop_02 | 0 | items[9].name | item | Стіки TEREA Amber | Crikw TEREA Amber 175,00x 1= 175 ,00-b ee |
| shop_02 | 0 | items[9].vat_group | item | Б | None |
| shop_02 | 0 | items[3].name | item | Кільця для шторки Bacche | Кільця для шторки Bacche 97,00x 1= o7,00-A |
| shop_02 | 0 | items[3].unit_price | item | 97.00 | None |
| shop_02 | 0 | items[3].amount | item | 97.00 | 7 |
| shop_02 | 0 | items[3].vat_group | item | А | None |
| shop_02 | 1 | seller.name | wrong | ТОВ "НОВА ЛІНІЯ 1" | ЛЬНИЙ КОМПЛЕКС |
| shop_02 | 1 | seller.tax_id | missed | 30728887 | None |
| shop_02 | 1 | receipt_number | missed | 14556 | None |
| shop_02 | 1 | fiscal_number | missed | 3000786185 | None |
| shop_02 | 1 | issued_at | missed | 2026-05-24 20:48:08 | None |
| shop_02 | 1 | items[4].vat_group | item | А | None |
| shop_02 | 1 | items[1].vat_group | item | А | None |
| shop_02 | 1 | items[6].vat_group | item | А | None |
| shop_02 | 1 | items[8].vat_group | item | Б | None |
| shop_02 | 1 | items[2].vat_group | item | А | None |
| shop_02 | 1 | items[7].vat_group | item | Б | None |
| shop_02 | 1 | items[5].unit_price | item | 267.00 | None |
| shop_02 | 1 | items[5].vat_group | item | А | None |
| shop_02 | 1 | items[9].name | item | Стіки TEREA Amber | Crikw TEREA Amber 175 |
| shop_02 | 1 | items[9].vat_group | item | Б | None |
| shop_02 | 1 | items[0].name | item | Карниз для душ. шторки B | Карниз ANA AYU. ШТОРКИ В fe 8% |
| shop_02 | 1 | items[0].vat_group | item | А | None |
| shop_02 | 1 | items[3].unit_price | item | 97.00 | None |
| shop_02 | 1 | items[3].amount | item | 97.00 | 7 |
| shop_02 | 1 | items[3].vat_group | item | А | None |
| shop_02 | 2 | seller.name | wrong | ТОВ "НОВА ЛІНІЯ 1" | ЛЬНИЙ КОМПЛЕКС |
| shop_02 | 2 | seller.tax_id | missed | 30728887 | None |
| shop_02 | 2 | seller.vat_payer_number | missed | 307288826516 | None |
| shop_02 | 2 | receipt_number | missed | 14556 | None |
| shop_02 | 2 | fiscal_number | missed | 3000786185 | None |
| shop_02 | 2 | issued_at | missed | 2026-05-24 20:48:08 | None |
| shop_02 | 2 | payment_method | wrong | card | cash |
| shop_02 | 2 | items[2].qty | item | 1 | 15 |
| shop_02 | 2 | items[9].name | item | Стіки TEREA Amber | Crikw TEREA Amber 175 |
| shop_02 | 2 | items[0].name | item | Карниз для душ. шторки B | Карниз ANA AYU. ШТОРКИ В fe 8% |
| shop_02 | 2 | items[3].unit_price | item | 97.00 | 7 |
| shop_02 | 2 | items[3].amount | item | 97.00 | 7 |
| super_01 | 0 | seller.vat_payer_number | missed | 360036026593 | None |
| super_01 | 0 | receipt_number | missed | 106038 | None |
| super_01 | 0 | fiscal_number | missed | 3000780445 | None |
| super_01 | 0 | issued_at | missed | 2026-07-23 18:29:20 | None |
| super_01 | 0 | total | wrong | 946.87 | 735.38 |
| super_01 | 0 | payment_method | wrong | card | cash |
| super_01 | 0 | items[8].qty | item | 0.548 | 1 |
| super_01 | 0 | items[8].unit_price | item | 35.89 | None |
| super_01 | 0 | items[9].name | item | Яйце куряче С0 Молодильне Ясенсвіт 10шт | куряче CO Молодильне AcexHcBiT |
| super_01 | 0 | items[13].name | item | Пакет майка зелений біо | Пакет майка зелений 610 1.49 |
| super_01 | 0 | items[11].amount | item | 119.00 | 9 |
| super_01 | 0 | items[1].qty | item | 0.144 | 16 |
| super_01 | 0 | items[1].unit_price | item | 999.00 | None |
| super_01 | 0 | items[1].amount | item | 143.86 | 461.4 |
| super_01 | 0 | items[1].vat_group | item | А | None |
| super_01 | 0 | items[6].amount | item | 38.49 | 8.49 |
| super_01 | 0 | items[4].name | item | Козинаки хомка насіння+льон АСК 450г | ювілейна Ятрань к/в В/Г ШИ |
| super_01 | 0 | items[4].qty | item | 1 | 25 |
| super_01 | 0 | items[7].name | item | Йогурт 2,2% Ліс. ягода Галичина ПЕТ300г | Ліс. ягода Галичина Пе 3.49 |
| super_01 | 0 | items[7].amount | item | 38.49 | 2.28 |
| super_01 | 0 | items | lines | 14 рядків | 12 рядків, зіставлено 11 |
| super_01 | 1 | seller.vat_payer_number | missed | 360036026593 | None |
| super_01 | 1 | receipt_number | missed | 106038 | None |
| super_01 | 1 | fiscal_number | missed | 3000780445 | None |
| super_01 | 1 | issued_at | wrong | 2026-07-23 18:29:20 | 2307-07-20 18:29:20+00:00 |
| super_01 | 1 | total | wrong | 946.87 | 7521.8 |
| super_01 | 1 | payment_method | wrong | card | cash |
| super_01 | 1 | items[10].name | item | Сметана 20% Галичина 300г стакан | Сметана 205 ралинина 300р стакан 69.99 |
| super_01 | 1 | items[9].name | item | Яйце куряче С0 Молодильне Ясенсвіт 10шт | куряче Молодильне AcexHcBiT |
| super_01 | 1 | items[13].name | item | Пакет майка зелений біо | Пакет майка зелений 610 1.49 |
| super_01 | 1 | items[11].amount | item | 119.00 | 9 |
| super_01 | 1 | items[1].qty | item | 0.144 | 16 |
| super_01 | 1 | items[1].unit_price | item | 999.00 | 461.4 |
| super_01 | 1 | items[1].amount | item | 143.86 | 7374.4 |
| super_01 | 1 | items[1].vat_group | item | А | None |
| super_01 | 1 | items[6].amount | item | 38.49 | 8.49 |
| super_01 | 1 | items[8].qty | item | 0.548 | 0.294 |
| super_01 | 1 | items[8].unit_price | item | 35.89 | 19.67 |
| super_01 | 1 | items[8].amount | item | 19.67 | 5.83 |
| super_01 | 1 | items[8].vat_group | item | А | None |
| super_01 | 1 | items[4].name | item | Козинаки хомка насіння+льон АСК 450г | ювілейна Ятрань к/в В/Г ШИ ый |
| super_01 | 1 | items[7].name | item | Йогурт 2,2% Ліс. ягода Галичина ПЕТ300г | Ліс. ягода Галичина Пе 3.49 |
| super_01 | 1 | items[7].amount | item | 38.49 | 25.79 |
| super_01 | 1 | items | lines | 14 рядків | 12 рядків, зіставлено 11 |
| super_01 | 2 | seller.name | wrong | ТОВ "НОВУС УКРАЇНА" | ПРИВАТБАНК НОВУС УКРАЇНА |
| super_01 | 2 | seller.vat_payer_number | missed | 360036026593 | None |
| super_01 | 2 | receipt_number | missed | 106038 | None |
| super_01 | 2 | fiscal_number | missed | 3000780445 | None |
| super_01 | 2 | issued_at | missed | 2026-07-23 18:29:20 | None |
| super_01 | 2 | payment_method | wrong | card | cash |
| super_01 | 2 | items[8].qty | item | 0.548 | 0.294 |
| super_01 | 2 | items[8].unit_price | item | 35.89 | None |
| super_01 | 2 | items[8].vat_group | item | А | None |
| super_01 | 2 | items[5].qty | item | 1 | 0.144 |
| super_01 | 2 | items[5].vat_group | item | А | None |
| super_01 | 2 | items[10].vat_group | item | А | None |
| super_01 | 2 | items[13].vat_group | item | А | None |
| super_01 | 2 | items[9].name | item | Яйце куряче С0 Молодильне Ясенсвіт 10шт | куряче CO Молодильне AcexHcBiT |
| super_01 | 2 | items[9].vat_group | item | А | None |
| super_01 | 2 | items[11].amount | item | 119.00 | 9 |
| super_01 | 2 | items[11].vat_group | item | А | None |
| super_01 | 2 | items[1].qty | item | 0.144 | 16 |
| super_01 | 2 | items[1].unit_price | item | 999.00 | None |
| super_01 | 2 | items[1].amount | item | 143.86 | 461.4 |
| super_01 | 2 | items[1].vat_group | item | А | None |
| super_01 | 2 | items[6].amount | item | 38.49 | 8.49 |
| super_01 | 2 | items[6].vat_group | item | А | None |
| super_01 | 2 | items[4].name | item | Козинаки хомка насіння+льон АСК 450г | ювілейна Ятрань к/в В/Г ШИ ый |
| super_01 | 2 | items[4].vat_group | item | А | None |
| super_01 | 2 | items[7].name | item | Йогурт 2,2% Ліс. ягода Галичина ПЕТ300г | Ліс. ягода Галичина Пе 3 |
| super_01 | 2 | items[7].qty | item | 1 | 2.28 |
| super_01 | 2 | items[7].amount | item | 38.49 | 35.89 |
| super_01 | 2 | items[7].vat_group | item | А | None |
| super_01 | 2 | items[0].name | item | Пакет середній 34*55 Novus 7кг | МАГАЗИН NG нори. КИЇВСЬКА бБЛАЄ bh sit |
| super_01 | 2 | items[0].vat_group | item | А | None |
| super_01 | 2 | items | lines | 14 рядків | 11 рядків, зіставлено 11 |
