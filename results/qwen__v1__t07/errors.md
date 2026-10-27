# Помилки на golden: qwen__v1__t07

| doc | r | поле | тип | golden | модель |
|---|---|---|---|---|---|
| azk_01 | 0 | seller.name | wrong | ПП "УКРПАЛЕТСИСТЕМ" | ЗН, ДЛЕ га АГЗП 196 |
| azk_01 | 0 | seller.tax_id | missed | 32285225 | None |
| azk_01 | 0 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_01 | 0 | receipt_number | missed | 448678 | None |
| azk_01 | 0 | fiscal_number | missed | 3001071005 | None |
| azk_01 | 0 | issued_at | missed | 2026-08-28 21:33:14 | None |
| azk_01 | 0 | total | wrong | 2065.60 | 2068 |
| azk_01 | 0 | payment_method | wrong | card | cash |
| azk_01 | 0 | items | lines | 1 рядків | 1 рядків, зіставлено 0 |
| azk_01 | 0 | category | class | fuel | other |
| azk_01 | 1 | seller.name | wrong | ПП "УКРПАЛЕТСИСТЕМ" | ЗН, ДЛЕ га АГЗП |
| azk_01 | 1 | seller.tax_id | missed | 32285225 | None |
| azk_01 | 1 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_01 | 1 | receipt_number | missed | 448678 | None |
| azk_01 | 1 | fiscal_number | missed | 3001071005 | None |
| azk_01 | 1 | issued_at | missed | 2026-08-28 21:33:14 | None |
| azk_01 | 1 | total | wrong | 2065.60 | 205.6 |
| azk_01 | 1 | items | lines | 1 рядків | 1 рядків, зіставлено 0 |
| azk_01 | 1 | category | class | fuel | transport |
| azk_01 | 2 | seller.name | wrong | ПП "УКРПАЛЕТСИСТЕМ" | ЗН, ДЛЕ га АГЗП |
| azk_01 | 2 | seller.tax_id | missed | 32285225 | None |
| azk_01 | 2 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_01 | 2 | receipt_number | wrong | 448678 | 494024028 |
| azk_01 | 2 | fiscal_number | missed | 3001071005 | None |
| azk_01 | 2 | issued_at | wrong | 2026-08-28 21:33:14 | 2808-01-28 21:23:14+00:00 |
| azk_01 | 2 | total | wrong | 2065.60 | 20.56 |
| azk_01 | 2 | items | lines | 1 рядків | 1 рядків, зіставлено 0 |
| azk_01 | 2 | category | class | fuel | transport |
| azk_04 | 0 | seller.vat_payer_number | missed | 383053623016 | None |
| azk_04 | 0 | receipt_number | missed | 3240140 | None |
| azk_04 | 0 | fiscal_number | missed | 3001212342 | None |
| azk_04 | 0 | issued_at | missed | 2026-06-21 19:06:56 | None |
| azk_04 | 0 | items[0].qty | item | 25.79 | 1 |
| azk_04 | 0 | items[0].unit_price | item | 76.90 | None |
| azk_04 | 0 | items[0].vat_group | item | А | None |
| azk_04 | 1 | seller.vat_payer_number | missed | 383053623016 | None |
| azk_04 | 1 | receipt_number | missed | 3240140 | None |
| azk_04 | 1 | fiscal_number | missed | 3001212342 | None |
| azk_04 | 1 | issued_at | missed | 2026-06-21 19:06:56 | None |
| azk_04 | 1 | items[0].name | item | Бензин А-95 | Бензин Aa 1983 .25 В |
| azk_04 | 1 | items[0].qty | item | 25.79 | 1 |
| azk_04 | 1 | items[0].unit_price | item | 76.90 | None |
| azk_04 | 1 | items[0].vat_group | item | А | None |
| azk_04 | 2 | seller.vat_payer_number | missed | 383053623016 | None |
| azk_04 | 2 | receipt_number | missed | 3240140 | None |
| azk_04 | 2 | fiscal_number | missed | 3001212342 | None |
| azk_04 | 2 | issued_at | missed | 2026-06-21 19:06:56 | None |
| azk_04 | 2 | items[0].name | item | Бензин А-95 | Бензин Аа 1983 .25 В |
| azk_04 | 2 | items[0].qty | item | 25.79 | 1 |
| azk_04 | 2 | items[0].unit_price | item | 76.90 | None |
| azk_04 | 2 | items[0].vat_group | item | А | None |
| azk_11 | 0 | seller.tax_id | missed | 32285225 | None |
| azk_11 | 0 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_11 | 0 | receipt_number | missed | 495195 | None |
| azk_11 | 0 | fiscal_number | missed | 3001071004 | None |
| azk_11 | 0 | issued_at | missed | 2026-06-25 18:19:00 | None |
| azk_11 | 0 | total | wrong | 731.00 | 751 |
| azk_11 | 0 | items[0].name | item | Сигарети JTI Camel Blue | Сигарети УП Sanе} Blue |
| azk_11 | 0 | items[0].qty | item | 2 | 1 |
| azk_11 | 0 | items[0].unit_price | item | 175.00 | None |
| azk_11 | 0 | items[0].amount | item | 350.00 | 350.006 |
| azk_11 | 0 | items[0].vat_group | item | Б | None |
| azk_11 | 0 | items | lines | 4 рядків | 1 рядків, зіставлено 1 |
| azk_11 | 0 | category | class | other | transport |
| azk_11 | 1 | seller.tax_id | missed | 32285225 | None |
| azk_11 | 1 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_11 | 1 | receipt_number | missed | 495195 | None |
| azk_11 | 1 | fiscal_number | missed | 3001071004 | None |
| azk_11 | 1 | issued_at | missed | 2026-06-25 18:19:00 | None |
| azk_11 | 1 | total | wrong | 731.00 | 751.00 |
| azk_11 | 1 | items[0].name | item | Сигарети JTI Camel Blue | Сигарети УП Сане} Blue |
| azk_11 | 1 | items[0].qty | item | 2 | 1 |
| azk_11 | 1 | items[0].unit_price | item | 175.00 | None |
| azk_11 | 1 | items[0].vat_group | item | Б | None |
| azk_11 | 1 | items | lines | 4 рядків | 1 рядків, зіставлено 1 |
| azk_11 | 1 | category | class | other | transport |
| azk_11 | 2 | seller.tax_id | missed | 32285225 | None |
| azk_11 | 2 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_11 | 2 | receipt_number | missed | 495195 | None |
| azk_11 | 2 | fiscal_number | missed | 3001071004 | None |
| azk_11 | 2 | issued_at | missed | 2026-06-25 18:19:00 | None |
| azk_11 | 2 | total | wrong | 731.00 | 751 |
| azk_11 | 2 | items[0].name | item | Сигарети JTI Camel Blue | Сигарети УП Сане} Blue |
| azk_11 | 2 | items[0].qty | item | 2 | 1 |
| azk_11 | 2 | items[0].unit_price | item | 175.00 | None |
| azk_11 | 2 | items[0].vat_group | item | Б | None |
| azk_11 | 2 | items | lines | 4 рядків | 1 рядків, зіставлено 1 |
| azk_11 | 2 | category | class | other | transport |
| food_01 | 0 | seller.name | wrong | ПІІ "МакДональдз Юкрейн Лтд" | МакДональйз Юкрейн Мга |
| food_01 | 0 | seller.vat_payer_number | missed | 237444526652 | None |
| food_01 | 0 | receipt_number | wrong | 000205557 | 75 |
| food_01 | 0 | fiscal_number | missed | 3000932994 | None |
| food_01 | 0 | issued_at | wrong | 2026-05-25 21:51:01 | 2025-05-02 21:51:01+00:00 |
| food_01 | 0 | items[0].vat_group | item | А | None |
| food_01 | 0 | items[2].name | item | АПЕЛЬС СІК ВЕЛ МЕНЮ додатково | APЕЛЬС СТК ВЕЛ МЕНЮ |
| food_01 | 0 | items[2].vat_group | item | А | None |
| food_01 | 0 | items | lines | 3 рядків | 2 рядків, зіставлено 2 |
| food_01 | 0 | category | class | meals | groceries |
| food_01 | 1 | seller.name | wrong | ПІІ "МакДональдз Юкрейн Лтд" | МакДональйз Юкрейн Мга |
| food_01 | 1 | seller.vat_payer_number | missed | 237444526652 | None |
| food_01 | 1 | receipt_number | missed | 000205557 | None |
| food_01 | 1 | fiscal_number | missed | 3000932994 | None |
| food_01 | 1 | issued_at | missed | 2026-05-25 21:51:01 | None |
| food_01 | 1 | items[2].vat_group | item | А | None |
| food_01 | 1 | items[0].vat_group | item | А | None |
| food_01 | 1 | items[1].vat_group | item | А | None |
| food_01 | 1 | category | class | meals | fuel |
| food_01 | 2 | seller.name | wrong | ПІІ "МакДональдз Юкрейн Лтд" | МакДональйз Юкрейн Мга |
| food_01 | 2 | seller.vat_payer_number | missed | 237444526652 | None |
| food_01 | 2 | receipt_number | missed | 000205557 | None |
| food_01 | 2 | fiscal_number | missed | 3000932994 | None |
| food_01 | 2 | issued_at | missed | 2026-05-25 21:51:01 | None |
| food_01 | 2 | items[2].vat_group | item | А | None |
| food_01 | 2 | items[0].vat_group | item | А | None |
| food_01 | 2 | items[1].vat_group | item | А | None |
| food_01 | 2 | category | class | meals | fuel |
| food_03 | 0 | seller.name | missed | GoH Craft Pub | None |
| food_03 | 0 | issued_at | missed | 2026-04-24 19:43:00 | None |
| food_03 | 0 | payment_method | wrong | card | cash |
| food_03 | 0 | items[2].unit_price | item | 108.00 | None |
| food_03 | 0 | items[5].unit_price | item | 188.00 | None |
| food_03 | 0 | items[3].unit_price | item | 123.00 | None |
| food_03 | 0 | items[10].name | item | Пиво Rebrew світле нефільтроване непастеризоване < POPELKA L | Пиво Rebrew світле нефільтроване непастеризоване ПЕТ-кег (ке |
| food_03 | 0 | items[10].unit_price | item | 103.00 | None |
| food_03 | 0 | items[7].name | item | Пиво Цитадель Хоппі Келлербір, кега 28л Хмільний Нуль (келих | Пиво Цитадель Хмільний Нуль ПЕТ КЕГ (келих 0,5) |
| food_03 | 0 | items[7].unit_price | item | 168.00 | None |
| food_03 | 0 | items[0].name | item | Пиво Rebrew світле нефільтроване непастеризоване < POPELKA L | пастеризоване Пиво світле (ПОПЕЛКА ЛАГЕР) ПЕТ-кег (келих 0,5 |
| food_03 | 0 | items[0].qty | item | 2 | 1 |
| food_03 | 0 | items[0].unit_price | item | 148.00 | None |
| food_03 | 0 | items[0].amount | item | 296.00 | 188 |
| food_03 | 0 | items | lines | 11 рядків | 10 рядків, зіставлено 10 |
| food_03 | 0 | category | class | meals | groceries |
| food_03 | 1 | seller.name | wrong | GoH Craft Pub | poster |
| food_03 | 1 | issued_at | missed | 2026-04-24 19:43:00 | None |
| food_03 | 1 | payment_method | wrong | card | cash |
| food_03 | 1 | items[8].qty | item | 1 | 50 |
| food_03 | 1 | items[10].name | item | Пиво Rebrew світле нефільтроване непастеризоване < POPELKA L | пиво rebrew світле нефільтроване непастеризоване ПЕТ-кег (ке |
| food_03 | 1 | items[10].unit_price | item | 103.00 | None |
| food_03 | 1 | items[5].name | item | Пиво MUZA IPA (5,4%) ПЕТ КЕГ 30л. Superdelic (келих 0.5) | пиво muza ipa ПЕТ КЕГ (келих 0.5) |
| food_03 | 1 | items[5].unit_price | item | 188.00 | None |
| food_03 | 1 | items[7].name | item | Пиво Цитадель Хоппі Келлербір, кега 28л Хмільний Нуль (келих | пиво цитадель ПЕТ КЕГ (келих 0.5) |
| food_03 | 1 | items[7].unit_price | item | 168.00 | None |
| food_03 | 1 | items[2].unit_price | item | 108.00 | None |
| food_03 | 1 | items[2].amount | item | 324.00 | 246 |
| food_03 | 1 | items[1].name | item | Пиво світле "Бургомістр Rein Пілснер", л (келих 0.5) | xonni kennepip kera 28h хмільний нуль (келих 0.5) |
| food_03 | 1 | items[1].qty | item | 1 | 2 |
| food_03 | 1 | items[3].name | item | Пиво MUZA IPA (5,4%) ПЕТ КЕГ 30л. Superdelic (келих 0.3) | пиво muza ipa ПЕТ КЕГ (келих 0.3) |
| food_03 | 1 | items[3].unit_price | item | 123.00 | None |
| food_03 | 1 | items[3].amount | item | 246.00 | 376 |
| food_03 | 1 | items[0].name | item | Пиво Rebrew світле нефільтроване непастеризоване < POPELKA L | пастеризоване | S POPELKA LAGER (ЛОПЕЛКА ЛАГЕР) ПЕТ-кег (кел |
| food_03 | 1 | items[0].qty | item | 2 | 1 |
| food_03 | 1 | items[0].unit_price | item | 148.00 | None |
| food_03 | 1 | items[0].amount | item | 296.00 | 188 |
| food_03 | 1 | items | lines | 11 рядків | 12 рядків, зіставлено 11 |
| food_03 | 1 | category | class | meals | groceries |
| food_03 | 2 | seller.name | wrong | GoH Craft Pub | bypromictp |
| food_03 | 2 | issued_at | missed | 2026-04-24 19:43:00 | None |
| food_03 | 2 | payment_method | wrong | card | cash |
| food_03 | 2 | items[1].name | item | Пиво світле "Бургомістр Rein Пілснер", л (келих 0.5) | Фісташки 50r Пиво світле India Pale Ale Westward (келих 0.5) |
| food_03 | 2 | items[5].unit_price | item | 188.00 | None |
| food_03 | 2 | items[5].amount | item | 376.00 | 188 |
| food_03 | 2 | items[3].unit_price | item | 123.00 | None |
| food_03 | 2 | items[3].amount | item | 246.00 | 123 |
| food_03 | 2 | items[10].unit_price | item | 103.00 | None |
| food_03 | 2 | items[10].amount | item | 309.00 | 103 |
| food_03 | 2 | items[7].unit_price | item | 168.00 | None |
| food_03 | 2 | items[7].amount | item | 336.00 | 168 |
| food_03 | 2 | items[0].name | item | Пиво Rebrew світле нефільтроване непастеризоване < POPELKA L | пастеризоване |S POPELKA LAGER ' (ЛОПЕЛКА | ‹ ЛАГЕР)», 5%, П |
| food_03 | 2 | items[0].qty | item | 2 | 1 |
| food_03 | 2 | items[0].unit_price | item | 148.00 | None |
| food_03 | 2 | items[0].amount | item | 296.00 | 188 |
| food_03 | 2 | items | lines | 11 рядків | 9 рядків, зіставлено 8 |
| food_03 | 2 | category | class | meals | groceries |
| fop_01 | 0 | seller.name | wrong | ФО-П Федик О.Б. | магазин "Наркетопт" |
| fop_01 | 0 | seller.vat_payer_number | missed | 305740855920 | None |
| fop_01 | 0 | receipt_number | missed | 11650133 | None |
| fop_01 | 0 | fiscal_number | missed | 3001247585 | None |
| fop_01 | 0 | issued_at | missed | 2026-06-20 15:52:37 | None |
| fop_01 | 0 | total | wrong | 347.42 | 278.50 |
| fop_01 | 0 | items[1].discount | item | 0.94 | None |
| fop_01 | 0 | items[1].vat_group | item | А | None |
| fop_01 | 0 | items[2].discount | item | 0.76 | None |
| fop_01 | 0 | items[2].vat_group | item | А | None |
| fop_01 | 0 | items[0].discount | item | 1.86 | None |
| fop_01 | 0 | items[0].vat_group | item | А | None |
| fop_01 | 0 | items[7].name | item | 110936-Пакет п/е майка 340*550 МАРКЕТОПТ | Пакет п/е майка 34 - MAPKETONT |
| fop_01 | 0 | items[7].discount | item | 0.28 | None |
| fop_01 | 0 | items[7].vat_group | item | А | None |
| fop_01 | 0 | items[6].name | item | 154745-ВВ Круасан Шоколад 350г | Круасан Малина 3685г |
| fop_01 | 0 | items[6].discount | item | 3.64 | None |
| fop_01 | 0 | items[6].vat_group | item | А | None |
| fop_01 | 0 | items[3].unit_price | item | 23.60 | None |
| fop_01 | 0 | items[3].amount | item | 23.60 | 75.70 |
| fop_01 | 0 | items[3].discount | item | 0.94 | None |
| fop_01 | 0 | items[3].vat_group | item | А | None |
| fop_01 | 0 | items[5].unit_price | item | 75.70 | None |
| fop_01 | 0 | items[5].amount | item | 75.70 | 6.90 |
| fop_01 | 0 | items[5].discount | item | 3.03 | None |
| fop_01 | 0 | items[5].vat_group | item | А | None |
| fop_01 | 0 | items | lines | 8 рядків | 7 рядків, зіставлено 7 |
| fop_01 | 1 | seller.name | wrong | ФО-П Федик О.Б. | магазин "Наркетопт" |
| fop_01 | 1 | seller.vat_payer_number | missed | 305740855920 | None |
| fop_01 | 1 | receipt_number | missed | 11650133 | None |
| fop_01 | 1 | fiscal_number | missed | 3001247585 | None |
| fop_01 | 1 | issued_at | missed | 2026-06-20 15:52:37 | None |
| fop_01 | 1 | items[6].name | item | 154745-ВВ Круасан Шоколад 350г | BB Круасан Малина '3685г |
| fop_01 | 1 | items[6].discount | item | 3.64 | None |
| fop_01 | 1 | items[6].vat_group | item | А | None |
| fop_01 | 1 | items[1].qty | item | 1 | 5 |
| fop_01 | 1 | items[1].unit_price | item | 23.60 | None |
| fop_01 | 1 | items[1].amount | item | 23.60 | 118.00 |
| fop_01 | 1 | items[1].discount | item | 0.94 | None |
| fop_01 | 1 | items[1].vat_group | item | А | None |
| fop_01 | 1 | items[3].qty | item | 1 | 2 |
| fop_01 | 1 | items[3].unit_price | item | 23.60 | None |
| fop_01 | 1 | items[3].amount | item | 23.60 | 75.70 |
| fop_01 | 1 | items[3].discount | item | 0.94 | None |
| fop_01 | 1 | items[3].vat_group | item | А | None |
| fop_01 | 1 | items[5].unit_price | item | 75.70 | None |
| fop_01 | 1 | items[5].amount | item | 75.70 | 6.90 |
| fop_01 | 1 | items[5].discount | item | 3.03 | None |
| fop_01 | 1 | items[5].vat_group | item | А | None |
| fop_01 | 1 | items[2].qty | item | 1 | 5 |
| fop_01 | 1 | items[2].unit_price | item | 18.90 | None |
| fop_01 | 1 | items[2].amount | item | 18.90 | 94.50 |
| fop_01 | 1 | items[2].discount | item | 0.76 | None |
| fop_01 | 1 | items[2].vat_group | item | А | None |
| fop_01 | 1 | items[7].qty | item | 1 | 2 |
| fop_01 | 1 | items[7].unit_price | item | 6.90 | None |
| fop_01 | 1 | items[7].amount | item | 6.90 | 13.80 |
| fop_01 | 1 | items[7].discount | item | 0.28 | None |
| fop_01 | 1 | items[7].vat_group | item | А | None |
| fop_01 | 1 | items[0].qty | item | 1 | 4 |
| fop_01 | 1 | items[0].unit_price | item | 46.60 | None |
| fop_01 | 1 | items[0].amount | item | 46.60 | 186.40 |
| fop_01 | 1 | items[0].discount | item | 1.86 | None |
| fop_01 | 1 | items[0].vat_group | item | А | None |
| fop_01 | 1 | items | lines | 8 рядків | 7 рядків, зіставлено 7 |
| fop_01 | 2 | seller.name | wrong | ФО-П Федик О.Б. | Наркетопт |
| fop_01 | 2 | seller.vat_payer_number | missed | 305740855920 | None |
| fop_01 | 2 | receipt_number | missed | 11650133 | None |
| fop_01 | 2 | fiscal_number | missed | 3001247585 | None |
| fop_01 | 2 | issued_at | missed | 2026-06-20 15:52:37 | None |
| fop_01 | 2 | items[1].discount | item | 0.94 | None |
| fop_01 | 2 | items[1].vat_group | item | А | None |
| fop_01 | 2 | items[2].discount | item | 0.76 | None |
| fop_01 | 2 | items[2].vat_group | item | А | None |
| fop_01 | 2 | items[0].discount | item | 1.86 | None |
| fop_01 | 2 | items[0].vat_group | item | А | None |
| fop_01 | 2 | items[6].name | item | 154745-ВВ Круасан Шоколад 350г | Круасан зі смаком маракуйї 385 г |
| fop_01 | 2 | items[6].discount | item | 3.64 | None |
| fop_01 | 2 | items[6].vat_group | item | А | None |
| fop_01 | 2 | items[3].unit_price | item | 23.60 | None |
| fop_01 | 2 | items[3].amount | item | 23.60 | 75.7 |
| fop_01 | 2 | items[3].discount | item | 0.94 | None |
| fop_01 | 2 | items[3].vat_group | item | А | None |
| fop_01 | 2 | items[4].name | item | 154733-ВВ Круасан Малина 385г | Круасан Малина 385 г |
| fop_01 | 2 | items[4].unit_price | item | 75.70 | None |
| fop_01 | 2 | items[4].amount | item | 75.70 | 75 |
| fop_01 | 2 | items[4].discount | item | 3.03 | None |
| fop_01 | 2 | items[4].vat_group | item | А | None |
| fop_01 | 2 | items[7].name | item | 110936-Пакет п/е майка 340*550 МАРКЕТОПТ | Круасан Шоколад 350 г |
| fop_01 | 2 | items[7].discount | item | 0.28 | None |
| fop_01 | 2 | items[7].vat_group | item | А | None |
| fop_01 | 2 | items | lines | 8 рядків | 7 рядків, зіставлено 7 |
| fop_02 | 0 | * |  |  | FAILED |
| fop_02 | 1 | seller.name | wrong | ЗОРІНА КРІСТІНА ПАВЛІВНА | МАГАЗИН Ш |
| fop_02 | 1 | seller.tax_id | missed | 2981206608 | None |
| fop_02 | 1 | receipt_number | missed | 9988 | None |
| fop_02 | 1 | fiscal_number | missed | 3001258680 | None |
| fop_02 | 1 | issued_at | missed | 2026-09-05 17:35:20 | None |
| fop_02 | 1 | items[1].name | item | СОСИСКИ ДИТЯЧІ В/С (ЧЕРЕВА) (Б) | СОСИСКИ ДИТЯЧІ |
| fop_02 | 1 | items[1].qty | item | 0.450 | 0.29 |
| fop_02 | 1 | items[1].unit_price | item | 254.50 | None |
| fop_02 | 1 | items[1].amount | item | 114.53 | 116.76 |
| fop_02 | 1 | items[1].vat_group | item | Н | None |
| fop_02 | 1 | items[2].name | item | ПАКЕТИ ФАСУВАЛЬНІ №9 10 МКР 1000 ШТ/УП | ПАКЕТИ @ACYBAADHI №9 |
| fop_02 | 1 | items[2].qty | item | 1 | 10 |
| fop_02 | 1 | items[2].unit_price | item | 0.40 | None |
| fop_02 | 1 | items[2].amount | item | 0.40 | 114.53 |
| fop_02 | 1 | items[2].vat_group | item | Н | None |
| fop_02 | 1 | items | lines | 4 рядків | 3 рядків, зіставлено 2 |
| fop_02 | 2 | seller.name | wrong | ЗОРІНА КРІСТІНА ПАВЛІВНА | МАГАЗИН |
| fop_02 | 2 | seller.tax_id | missed | 2981206608 | None |
| fop_02 | 2 | receipt_number | missed | 9988 | None |
| fop_02 | 2 | fiscal_number | missed | 3001258680 | None |
| fop_02 | 2 | issued_at | missed | 2026-09-05 17:35:20 | None |
| fop_02 | 2 | items[1].name | item | СОСИСКИ ДИТЯЧІ В/С (ЧЕРЕВА) (Б) | СОСИСКИ ДИТЯЧІ 500 GR (в) |
| fop_02 | 2 | items[1].unit_price | item | 254.50 | None |
| fop_02 | 2 | items[1].vat_group | item | Н | None |
| fop_02 | 2 | items[2].qty | item | 1 | 0.4 |
| fop_02 | 2 | items[2].unit_price | item | 0.40 | None |
| fop_02 | 2 | items[2].amount | item | 0.40 | 116.76 |
| fop_02 | 2 | items[2].vat_group | item | Н | None |
| fop_02 | 2 | items | lines | 4 рядків | 3 рядків, зіставлено 2 |
| shop_01 | 0 | seller.name | wrong | ТОВ "Приватінвест" | IIpuBarinBect |
| shop_01 | 0 | seller.tax_id | missed | 21550555 | None |
| shop_01 | 0 | seller.vat_payer_number | missed | 215505526546 | None |
| shop_01 | 0 | receipt_number | missed | q64Dxa1JXX0 | None |
| shop_01 | 0 | issued_at | missed | 2026-09-08 14:59:34 | None |
| shop_01 | 0 | items[0].qty | item | 1.000 | 4 |
| shop_01 | 0 | items[0].vat_group | item | А | К |
| shop_01 | 0 | category | class | office | groceries |
| shop_01 | 1 | seller.name | wrong | ТОВ "Приватінвест" | IIpuBarinBect |
| shop_01 | 1 | seller.tax_id | missed | 21550555 | None |
| shop_01 | 1 | seller.vat_payer_number | missed | 215505526546 | None |
| shop_01 | 1 | receipt_number | missed | q64Dxa1JXX0 | None |
| shop_01 | 1 | issued_at | missed | 2026-09-08 14:59:34 | None |
| shop_01 | 1 | items[0].vat_group | item | А | None |
| shop_01 | 1 | category | class | office | other |
| shop_01 | 2 | seller.name | wrong | ТОВ "Приватінвест" | Brain |
| shop_01 | 2 | seller.tax_id | missed | 21550555 | None |
| shop_01 | 2 | seller.vat_payer_number | missed | 215505526546 | None |
| shop_01 | 2 | receipt_number | missed | q64Dxa1JXX0 | None |
| shop_01 | 2 | issued_at | missed | 2026-09-08 14:59:34 | None |
| shop_01 | 2 | items[0].qty | item | 1.000 | 4 |
| shop_01 | 2 | items[0].vat_group | item | А | None |
| shop_02 | 0 | seller.name | wrong | ТОВ "НОВА ЛІНІЯ 1" | ЛЬНИЙ КОМПЛЕКС |
| shop_02 | 0 | seller.tax_id | missed | 30728887 | None |
| shop_02 | 0 | seller.vat_payer_number | missed | 307288826516 | None |
| shop_02 | 0 | receipt_number | missed | 14556 | None |
| shop_02 | 0 | fiscal_number | missed | 3000786185 | None |
| shop_02 | 0 | issued_at | missed | 2026-05-24 20:48:08 | None |
| shop_02 | 0 | items[8].vat_group | item | Б | None |
| shop_02 | 0 | items[4].vat_group | item | А | None |
| shop_02 | 0 | items[3].vat_group | item | А | None |
| shop_02 | 0 | items[1].vat_group | item | А | None |
| shop_02 | 0 | items[7].vat_group | item | Б | None |
| shop_02 | 0 | items[9].vat_group | item | Б | None |
| shop_02 | 0 | items[2].vat_group | item | А | None |
| shop_02 | 0 | items[5].unit_price | item | 267.00 | None |
| shop_02 | 0 | items[5].vat_group | item | А | None |
| shop_02 | 0 | items[6].vat_group | item | А | None |
| shop_02 | 0 | items[0].name | item | Карниз для душ. шторки B | Карниз ANA AYU. ШТОРКИ |
| shop_02 | 0 | items[0].vat_group | item | А | None |
| shop_02 | 1 | seller.name | wrong | ТОВ "НОВА ЛІНІЯ 1" | ЛЬНИЙ КОМПЛЕКС |
| shop_02 | 1 | seller.tax_id | missed | 30728887 | None |
| shop_02 | 1 | seller.vat_payer_number | missed | 307288826516 | None |
| shop_02 | 1 | receipt_number | missed | 14556 | None |
| shop_02 | 1 | fiscal_number | missed | 3000786185 | None |
| shop_02 | 1 | issued_at | missed | 2026-05-24 20:48:08 | None |
| shop_02 | 1 | items[1].qty | item | 1 | 4 |
| shop_02 | 1 | items[1].vat_group | item | А | None |
| shop_02 | 1 | items[2].vat_group | item | А | None |
| shop_02 | 1 | items[7].vat_group | item | Б | None |
| shop_02 | 1 | items[5].qty | item | 2 | 3 |
| shop_02 | 1 | items[5].unit_price | item | 267.00 | None |
| shop_02 | 1 | items[5].vat_group | item | А | None |
| shop_02 | 1 | items[9].name | item | Стіки TEREA Amber | Crikw TEREA Amber 175 |
| shop_02 | 1 | items[9].vat_group | item | Б | None |
| shop_02 | 1 | items[0].name | item | Карниз для душ. шторки B | Карниз ANA AYU. ШТОРКИ В fe 8% |
| shop_02 | 1 | items[0].qty | item | 1 | 4 |
| shop_02 | 1 | items[0].vat_group | item | А | None |
| shop_02 | 1 | items[4].qty | item | 1 | 2 |
| shop_02 | 1 | items[4].unit_price | item | 20.10 | None |
| shop_02 | 1 | items[4].amount | item | 20.10 | 40.2 |
| shop_02 | 1 | items[4].vat_group | item | А | None |
| shop_02 | 1 | items[3].qty | item | 1 | 3 |
| shop_02 | 1 | items[3].unit_price | item | 97.00 | None |
| shop_02 | 1 | items[3].amount | item | 97.00 | 285 |
| shop_02 | 1 | items[3].vat_group | item | А | None |
| shop_02 | 1 | items[8].qty | item | 1 | 4 |
| shop_02 | 1 | items[8].unit_price | item | 175.00 | None |
| shop_02 | 1 | items[8].amount | item | 175.00 | 700 |
| shop_02 | 1 | items[8].vat_group | item | Б | None |
| shop_02 | 1 | items[6].qty | item | 1 | 6 |
| shop_02 | 1 | items[6].unit_price | item | 410.00 | None |
| shop_02 | 1 | items[6].amount | item | 410.00 | 2460 |
| shop_02 | 1 | items[6].vat_group | item | А | None |
| shop_02 | 2 | seller.name | wrong | ТОВ "НОВА ЛІНІЯ 1" | ЛЬНИЙ КОМПЛЕКС |
| shop_02 | 2 | seller.tax_id | missed | 30728887 | None |
| shop_02 | 2 | seller.vat_payer_number | missed | 307288826516 | None |
| shop_02 | 2 | receipt_number | missed | 14556 | None |
| shop_02 | 2 | fiscal_number | missed | 3000786185 | None |
| shop_02 | 2 | issued_at | missed | 2026-05-24 20:48:08 | None |
| shop_02 | 2 | items[4].vat_group | item | А | 63 |
| shop_02 | 2 | items[1].vat_group | item | А | 73 |
| shop_02 | 2 | items[3].vat_group | item | А | 39 |
| shop_02 | 2 | items[8].vat_group | item | Б | 24 |
| shop_02 | 2 | items[2].vat_group | item | А | 63 |
| shop_02 | 2 | items[7].vat_group | item | Б | 24 |
| shop_02 | 2 | items[5].unit_price | item | 267.00 | None |
| shop_02 | 2 | items[5].vat_group | item | А | 63 |
| shop_02 | 2 | items[6].vat_group | item | А | 24 |
| shop_02 | 2 | items[9].name | item | Стіки TEREA Amber | Crikw TEREA Amber 175 |
| shop_02 | 2 | items[9].vat_group | item | Б | 24 |
| shop_02 | 2 | items[0].name | item | Карниз для душ. шторки B | Карниз ANA AYU. ШТОРКИ В fe 8% |
| shop_02 | 2 | items[0].vat_group | item | А | 63 |
| super_01 | 0 | seller.vat_payer_number | missed | 360036026593 | None |
| super_01 | 0 | receipt_number | missed | 106038 | None |
| super_01 | 0 | fiscal_number | missed | 3000780445 | None |
| super_01 | 0 | issued_at | missed | 2026-07-23 18:29:20 | None |
| super_01 | 0 | items[1].qty | item | 0.144 | 143.86 |
| super_01 | 0 | items[1].unit_price | item | 999.00 | None |
| super_01 | 0 | items[1].vat_group | item | А | None |
| super_01 | 0 | items[13].qty | item | 1 | 1.49 |
| super_01 | 0 | items[13].vat_group | item | А | None |
| super_01 | 0 | items[11].qty | item | 1 | 2.28 |
| super_01 | 0 | items[11].amount | item | 119.00 | 2.28 |
| super_01 | 0 | items[11].vat_group | item | А | None |
| super_01 | 0 | items[8].qty | item | 0.548 | 3.49 |
| super_01 | 0 | items[8].unit_price | item | 35.89 | None |
| super_01 | 0 | items[8].amount | item | 19.67 | 3.49 |
| super_01 | 0 | items[8].vat_group | item | А | None |
| super_01 | 0 | items[5].qty | item | 1 | 38.49 |
| super_01 | 0 | items[5].amount | item | 38.49 | 115.47 |
| super_01 | 0 | items[5].vat_group | item | А | None |
| super_01 | 0 | items[6].qty | item | 1 | 69.99 |
| super_01 | 0 | items[6].amount | item | 38.49 | 21.19 |
| super_01 | 0 | items[6].vat_group | item | А | None |
| super_01 | 0 | items[10].qty | item | 1 | 19.67 |
| super_01 | 0 | items[10].amount | item | 69.99 | 19.67 |
| super_01 | 0 | items[10].vat_group | item | А | None |
| super_01 | 0 | items[2].name | item | Корейка по кіровоград.Ятрань к/в в/г ваг | ога по к! ово град. Ятрань к/в в |
| super_01 | 0 | items[2].qty | item | 0.226 | 17.97 |
| super_01 | 0 | items[2].unit_price | item | 699.00 | None |
| super_01 | 0 | items[2].amount | item | 157.97 | 17.97 |
| super_01 | 0 | items[2].vat_group | item | А | None |
| super_01 | 0 | items[9].name | item | Яйце куряче С0 Молодильне Ясенсвіт 10шт | куряче CO Молодильне AcexHcBiT cn. |
| super_01 | 0 | items[9].qty | item | 1 | 19.67 |
| super_01 | 0 | items[9].amount | item | 72.99 | 19.67 |
| super_01 | 0 | items[9].vat_group | item | А | None |
| super_01 | 0 | items[7].name | item | Йогурт 2,2% Ліс. ягода Галичина ПЕТ300г | Ліс. ягода Галичина Пе 3 |
| super_01 | 0 | items[7].qty | item | 1 | 10.27 |
| super_01 | 0 | items[7].amount | item | 38.49 | 10.27 |
| super_01 | 0 | items[7].vat_group | item | А | None |
| super_01 | 0 | items[3].name | item | Шинка ювілейна Ятрань к/в в/г т/у ваг | ювілейна Ятрань к/в В/Г ШИ ый |
| super_01 | 0 | items[3].qty | item | 0.216 | 23.07 |
| super_01 | 0 | items[3].unit_price | item | 461.40 | None |
| super_01 | 0 | items[3].amount | item | 99.66 | 23.07 |
| super_01 | 0 | items[3].vat_group | item | А | None |
| super_01 | 0 | items | lines | 14 рядків | 11 рядків, зіставлено 11 |
| super_01 | 1 | seller.vat_payer_number | missed | 360036026593 | None |
| super_01 | 1 | receipt_number | wrong | 106038 |  |
| super_01 | 1 | fiscal_number | missed | 3000780445 | None |
| super_01 | 1 | total | wrong | 946.87 | 30007.8 |
| super_01 | 1 | items[8].qty | item | 0.548 | 1 |
| super_01 | 1 | items[8].unit_price | item | 35.89 | None |
| super_01 | 1 | items[8].vat_group | item | А | None |
| super_01 | 1 | items[1].qty | item | 0.144 | 1 |
| super_01 | 1 | items[1].unit_price | item | 999.00 | None |
| super_01 | 1 | items[1].vat_group | item | А | None |
| super_01 | 1 | items[5].vat_group | item | А | None |
| super_01 | 1 | items[0].vat_group | item | А | None |
| super_01 | 1 | items[10].vat_group | item | А | None |
| super_01 | 1 | items[9].name | item | Яйце куряче С0 Молодильне Ясенсвіт 10шт | куряче CO Молодильне AcexHcBiT |
| super_01 | 1 | items[9].vat_group | item | А | None |
| super_01 | 1 | items[11].amount | item | 119.00 | 9 |
| super_01 | 1 | items[11].vat_group | item | А | None |
| super_01 | 1 | items[6].amount | item | 38.49 | 8.49 |
| super_01 | 1 | items[6].vat_group | item | А | None |
| super_01 | 1 | items[13].amount | item | 1.49 | 14.9 |
| super_01 | 1 | items[13].vat_group | item | А | None |
| super_01 | 1 | items[12].qty | item | 1 | 4.194 |
| super_01 | 1 | items[12].amount | item | 40.79 | 100 |
| super_01 | 1 | items[12].vat_group | item | А | None |
| super_01 | 1 | items[4].name | item | Козинаки хомка насіння+льон АСК 450г | ювілейна Ятрань к/в В/Г ШИ ый |
| super_01 | 1 | items[4].vat_group | item | А | None |
| super_01 | 1 | items[7].name | item | Йогурт 2,2% Ліс. ягода Галичина ПЕТ300г | Ліс. ягода Галичина Пе 3.49 A |
| super_01 | 1 | items[7].qty | item | 1 | 2.28 |
| super_01 | 1 | items[7].amount | item | 38.49 | 54.8 |
| super_01 | 1 | items[7].vat_group | item | А | None |
| super_01 | 1 | items | lines | 14 рядків | 13 рядків, зіставлено 12 |
| super_01 | 2 | seller.vat_payer_number | missed | 360036026593 | None |
| super_01 | 2 | receipt_number | wrong | 106038 | 3000780445 |
| super_01 | 2 | fiscal_number | missed | 3000780445 | None |
| super_01 | 2 | issued_at | wrong | 2026-07-23 18:29:20 | 2307-07-20 18:29:20+00:00 |
| super_01 | 2 | total | wrong | 946.87 | 3000.78 |
| super_01 | 2 | payment_method | wrong | card | cash |
| super_01 | 2 | items[5].vat_group | item | А | None |
| super_01 | 2 | items[13].qty | item | 1 | 45 |
| super_01 | 2 | items[13].vat_group | item | А | None |
| super_01 | 2 | items[11].qty | item | 1 | 9.00 |
| super_01 | 2 | items[11].amount | item | 119.00 | 548.00 |
| super_01 | 2 | items[11].vat_group | item | А | None |
| super_01 | 2 | items[10].qty | item | 1 | 69.99 |
| super_01 | 2 | items[10].amount | item | 69.99 | 458.00 |
| super_01 | 2 | items[10].vat_group | item | А | None |
| super_01 | 2 | items[6].amount | item | 38.49 | 8.49 |
| super_01 | 2 | items[6].vat_group | item | А | None |
| super_01 | 2 | items[1].qty | item | 0.144 | 17.97 |
| super_01 | 2 | items[1].unit_price | item | 999.00 | None |
| super_01 | 2 | items[1].amount | item | 143.86 | 461.40 |
| super_01 | 2 | items[1].vat_group | item | А | None |
| super_01 | 2 | items[8].qty | item | 0.548 | 19.67 |
| super_01 | 2 | items[8].unit_price | item | 35.89 | None |
| super_01 | 2 | items[8].amount | item | 19.67 | 548.00 |
| super_01 | 2 | items[8].vat_group | item | А | None |
| super_01 | 2 | items[12].qty | item | 1 | 19.4 |
| super_01 | 2 | items[12].amount | item | 40.79 | 548.00 |
| super_01 | 2 | items[12].vat_group | item | А | None |
| super_01 | 2 | items[9].name | item | Яйце куряче С0 Молодильне Ясенсвіт 10шт | Куряче CO Молодильне AcexHcBiT |
| super_01 | 2 | items[9].amount | item | 72.99 | 32.99 |
| super_01 | 2 | items[9].vat_group | item | А | None |
| super_01 | 2 | items[7].name | item | Йогурт 2,2% Ліс. ягода Галичина ПЕТ300г | Ліс. ягода Галичина Пе 3 |
| super_01 | 2 | items[7].qty | item | 1 | 2.28 |
| super_01 | 2 | items[7].amount | item | 38.49 | 34.99 |
| super_01 | 2 | items[7].vat_group | item | А | None |
| super_01 | 2 | items[2].name | item | Корейка по кіровоград.Ятрань к/в в/г ваг | Овочі град. Ятрань к/в В/Г ШИ ый |
| super_01 | 2 | items[2].qty | item | 0.226 | 99.99 |
| super_01 | 2 | items[2].unit_price | item | 699.00 | None |
| super_01 | 2 | items[2].amount | item | 157.97 | 548.00 |
| super_01 | 2 | items[2].vat_group | item | А | None |
| super_01 | 2 | items[0].name | item | Пакет середній 34*55 Novus 7кг | Мясні колбаски середня 34455 Novus КГ |
| super_01 | 2 | items[0].qty | item | 1 | 5.99 |
| super_01 | 2 | items[0].amount | item | 5.99 | 143.86 |
| super_01 | 2 | items[0].vat_group | item | А | None |
| super_01 | 2 | items | lines | 14 рядків | 12 рядків, зіставлено 12 |
