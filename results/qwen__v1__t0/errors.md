# Помилки на golden: qwen__v1__t0

| doc | r | поле | тип | golden | модель |
|---|---|---|---|---|---|
| azk_01 | 0 | seller.name | wrong | ПП "УКРПАЛЕТСИСТЕМ" | ЗН, ДЛЕ га АГЗП 196 |
| azk_01 | 0 | seller.tax_id | missed | 32285225 | None |
| azk_01 | 0 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_01 | 0 | receipt_number | missed | 448678 | None |
| azk_01 | 0 | fiscal_number | missed | 3001071005 | None |
| azk_01 | 0 | issued_at | missed | 2026-08-28 21:33:14 | None |
| azk_01 | 0 | total | wrong | 2065.60 | 205.6 |
| azk_01 | 0 | payment_method | wrong | card | cash |
| azk_01 | 0 | items | lines | 1 рядків | 1 рядків, зіставлено 0 |
| azk_01 | 0 | category | class | fuel | transport |
| azk_04 | 0 | seller.vat_payer_number | missed | 383053623016 | None |
| azk_04 | 0 | receipt_number | missed | 3240140 | None |
| azk_04 | 0 | fiscal_number | missed | 3001212342 | None |
| azk_04 | 0 | issued_at | missed | 2026-06-21 19:06:56 | None |
| azk_04 | 0 | items[0].name | item | Бензин А-95 | Бензин Aa 1983 .25 В |
| azk_04 | 0 | items[0].qty | item | 25.79 | 1 |
| azk_04 | 0 | items[0].unit_price | item | 76.90 | None |
| azk_04 | 0 | items[0].vat_group | item | А | None |
| azk_11 | 0 | seller.tax_id | missed | 32285225 | None |
| azk_11 | 0 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_11 | 0 | receipt_number | missed | 495195 | None |
| azk_11 | 0 | fiscal_number | missed | 3001071004 | None |
| azk_11 | 0 | issued_at | missed | 2026-06-25 18:19:00 | None |
| azk_11 | 0 | total | wrong | 731.00 | 751 |
| azk_11 | 0 | items[0].name | item | Сигарети JTI Camel Blue | Сигарети УП Сане} Blue |
| azk_11 | 0 | items[0].qty | item | 2 | 1 |
| azk_11 | 0 | items[0].unit_price | item | 175.00 | None |
| azk_11 | 0 | items[0].vat_group | item | Б | None |
| azk_11 | 0 | items | lines | 4 рядків | 1 рядків, зіставлено 1 |
| azk_11 | 0 | category | class | other | transport |
| food_01 | 0 | seller.name | wrong | ПІІ "МакДональдз Юкрейн Лтд" | МакДональйз Юкрейн Мга |
| food_01 | 0 | seller.vat_payer_number | missed | 237444526652 | None |
| food_01 | 0 | receipt_number | missed | 000205557 | None |
| food_01 | 0 | fiscal_number | missed | 3000932994 | None |
| food_01 | 0 | issued_at | missed | 2026-05-25 21:51:01 | None |
| food_01 | 0 | items[2].vat_group | item | А | None |
| food_01 | 0 | items[0].vat_group | item | А | None |
| food_01 | 0 | items | lines | 3 рядків | 2 рядків, зіставлено 2 |
| food_01 | 0 | category | class | meals | fuel |
| food_03 | 0 | seller.name | wrong | GoH Craft Pub | Poster |
| food_03 | 0 | issued_at | missed | 2026-04-24 19:43:00 | None |
| food_03 | 0 | payment_method | wrong | card | cash |
| food_03 | 0 | items[2].unit_price | item | 108.00 | None |
| food_03 | 0 | items[10].name | item | Пиво Rebrew світле нефільтроване непастеризоване < POPELKA L | Пиво Rebrew світле нефільтроване непастеризоване ПЕТ-кег (ке |
| food_03 | 0 | items[10].unit_price | item | 103.00 | None |
| food_03 | 0 | items[3].name | item | Пиво MUZA IPA (5,4%) ПЕТ КЕГ 30л. Superdelic (келих 0.3) | Пиво MUZA IPA ПЕТ КЕГ (келих 0,3) |
| food_03 | 0 | items[3].unit_price | item | 123.00 | None |
| food_03 | 0 | items[7].name | item | Пиво Цитадель Хоппі Келлербір, кега 28л Хмільний Нуль (келих | Пиво Цитадель Хмільний Нуль ПЕТ КЕГ (келих 0,5) |
| food_03 | 0 | items[7].unit_price | item | 168.00 | None |
| food_03 | 0 | items[4].name | item | Донер з куркою та грибами | Донер з куркою грибами Пиво MUZA IPA ПЕТ КЕГ (келих 0,5) |
| food_03 | 0 | items[0].name | item | Пиво Rebrew світле нефільтроване непастеризоване < POPELKA L | Пастеризоване пиво S POPELKA LAGER (ЛОПЕЛКА ЛАГЕР) ПЕТ-кег ( |
| food_03 | 0 | items[0].qty | item | 2 | 1 |
| food_03 | 0 | items[0].unit_price | item | 148.00 | None |
| food_03 | 0 | items[0].amount | item | 296.00 | 188 |
| food_03 | 0 | items | lines | 11 рядків | 9 рядків, зіставлено 9 |
| food_03 | 0 | category | class | meals | groceries |
| fop_01 | 0 | seller.name | wrong | ФО-П Федик О.Б. | Наркетопт |
| fop_01 | 0 | seller.vat_payer_number | missed | 305740855920 | None |
| fop_01 | 0 | receipt_number | missed | 11650133 | None |
| fop_01 | 0 | fiscal_number | missed | 3001247585 | None |
| fop_01 | 0 | issued_at | missed | 2026-06-20 15:52:37 | None |
| fop_01 | 0 | items[1].discount | item | 0.94 | None |
| fop_01 | 0 | items[1].vat_group | item | А | None |
| fop_01 | 0 | items[2].discount | item | 0.76 | None |
| fop_01 | 0 | items[2].vat_group | item | А | None |
| fop_01 | 0 | items[0].discount | item | 1.86 | None |
| fop_01 | 0 | items[0].vat_group | item | А | None |
| fop_01 | 0 | items[6].name | item | 154745-ВВ Круасан Шоколад 350г | Круасан зі смаком маракуйї 385 г |
| fop_01 | 0 | items[6].discount | item | 3.64 | None |
| fop_01 | 0 | items[6].vat_group | item | А | None |
| fop_01 | 0 | items[3].unit_price | item | 23.60 | None |
| fop_01 | 0 | items[3].amount | item | 23.60 | 75.7 |
| fop_01 | 0 | items[3].discount | item | 0.94 | None |
| fop_01 | 0 | items[3].vat_group | item | А | None |
| fop_01 | 0 | items[4].name | item | 154733-ВВ Круасан Малина 385г | Круасан Малина 368г |
| fop_01 | 0 | items[4].unit_price | item | 75.70 | None |
| fop_01 | 0 | items[4].amount | item | 75.70 | 75 |
| fop_01 | 0 | items[4].discount | item | 3.03 | None |
| fop_01 | 0 | items[4].vat_group | item | А | None |
| fop_01 | 0 | items[7].name | item | 110936-Пакет п/е майка 340*550 МАРКЕТОПТ | Круасан Шоколад 350 г |
| fop_01 | 0 | items[7].discount | item | 0.28 | None |
| fop_01 | 0 | items[7].vat_group | item | А | None |
| fop_01 | 0 | items | lines | 8 рядків | 7 рядків, зіставлено 7 |
| fop_02 | 0 | seller.name | wrong | ЗОРІНА КРІСТІНА ПАВЛІВНА | МАГАЗИН Ш |
| fop_02 | 0 | seller.tax_id | missed | 2981206608 | None |
| fop_02 | 0 | receipt_number | missed | 9988 | None |
| fop_02 | 0 | fiscal_number | missed | 3001258680 | None |
| fop_02 | 0 | issued_at | missed | 2026-09-05 17:35:20 | None |
| fop_02 | 0 | items[1].qty | item | 0.450 | 419 |
| fop_02 | 0 | items[1].unit_price | item | 254.50 | None |
| fop_02 | 0 | items[1].amount | item | 114.53 | 123.95 |
| fop_02 | 0 | items[1].vat_group | item | Н | None |
| fop_02 | 0 | items[2].qty | item | 1 | 369.5 |
| fop_02 | 0 | items[2].unit_price | item | 0.40 | None |
| fop_02 | 0 | items[2].amount | item | 0.40 | 116.76 |
| fop_02 | 0 | items[2].vat_group | item | Н | None |
| fop_02 | 0 | items | lines | 4 рядків | 2 рядків, зіставлено 2 |
| shop_01 | 0 | seller.name | wrong | ТОВ "Приватінвест" | IIpuBarinBect |
| shop_01 | 0 | seller.tax_id | missed | 21550555 | None |
| shop_01 | 0 | seller.vat_payer_number | missed | 215505526546 | None |
| shop_01 | 0 | receipt_number | missed | q64Dxa1JXX0 | None |
| shop_01 | 0 | issued_at | missed | 2026-09-08 14:59:34 | None |
| shop_01 | 0 | items[0].vat_group | item | А | None |
| shop_01 | 0 | category | class | office | transport |
| shop_02 | 0 | seller.name | wrong | ТОВ "НОВА ЛІНІЯ 1" | ЛЬНИЙ КОМПЛЕКС |
| shop_02 | 0 | seller.tax_id | missed | 30728887 | None |
| shop_02 | 0 | seller.vat_payer_number | missed | 307288826516 | None |
| shop_02 | 0 | receipt_number | missed | 14556 | None |
| shop_02 | 0 | fiscal_number | missed | 3000786185 | None |
| shop_02 | 0 | issued_at | missed | 2026-05-24 20:48:08 | None |
| shop_02 | 0 | items[4].vat_group | item | А | None |
| shop_02 | 0 | items[1].vat_group | item | А | None |
| shop_02 | 0 | items[3].vat_group | item | А | None |
| shop_02 | 0 | items[8].vat_group | item | Б | None |
| shop_02 | 0 | items[2].vat_group | item | А | None |
| shop_02 | 0 | items[7].vat_group | item | Б | None |
| shop_02 | 0 | items[5].unit_price | item | 267.00 | None |
| shop_02 | 0 | items[5].vat_group | item | А | None |
| shop_02 | 0 | items[6].vat_group | item | А | None |
| shop_02 | 0 | items[9].name | item | Стіки TEREA Amber | Crikw TEREA Amber 175 |
| shop_02 | 0 | items[9].vat_group | item | Б | None |
| shop_02 | 0 | items[0].name | item | Карниз для душ. шторки B | Карниз ANA AYU. ШТОРКИ В fe 8% |
| shop_02 | 0 | items[0].vat_group | item | А | None |
| super_01 | 0 | * |  |  | FAILED |
