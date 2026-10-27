# Помилки на golden: haiku__v1__t0

| doc | r | поле | тип | golden | модель |
|---|---|---|---|---|---|
| azk_01 | 0 | seller.name | missed | ПП "УКРПАЛЕТСИСТЕМ" | None |
| azk_01 | 0 | seller.tax_id | missed | 32285225 | None |
| azk_01 | 0 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_01 | 0 | receipt_number | missed | 448678 | None |
| azk_01 | 0 | fiscal_number | missed | 3001071005 | None |
| azk_01 | 0 | issued_at | wrong | 2026-08-28 21:33:14 | 2028-08-28 21:23:14+03:00 |
| azk_01 | 0 | total | wrong | 2065.60 | 688 |
| azk_01 | 0 | items | lines | 1 рядків | 1 рядків, зіставлено 0 |
| azk_01 | 0 | category | class | fuel | other |
| azk_04 | 0 | seller.vat_payer_number | wrong | 383053623016 | 363052623016 |
| azk_04 | 0 | items[0].name | item | Бензин А-95 | Бензин A-95-Epp05-E0 |
| azk_04 | 0 | items[0].qty | item | 25.79 | 1 |
| azk_04 | 0 | items[0].unit_price | item | 76.90 | None |
| azk_04 | 0 | items[0].vat_group | item | А | В |
| azk_11 | 0 | seller.name | wrong | ПП "УКРПАЛЕТСИСТЕМ" | ТОВ "УКРПАЛЕТСИСТЕМА" |
| azk_11 | 0 | seller.tax_id | missed | 32285225 | None |
| azk_11 | 0 | seller.vat_payer_number | missed | 322852206095 | None |
| azk_11 | 0 | receipt_number | missed | 495195 | None |
| azk_11 | 0 | fiscal_number | missed | 3001071004 | None |
| azk_11 | 0 | issued_at | wrong | 2026-06-25 18:19:00 | 2026-06-25 18:00:00+03:00 |
| azk_11 | 0 | discount_total | hallucinated | None | 0 |
| azk_11 | 0 | total | wrong | 731.00 | 131 |
| azk_11 | 0 | items[2].name | item | TEREAPROVENCEPEARLTBEH | DADE NCEPEARL TOE |
| azk_11 | 0 | items[2].vat_group | item | Б | None |
| azk_11 | 0 | items[1].name | item | TEREASIENNATBEH | TFAEASTEMVATBER |
| azk_11 | 0 | items[1].vat_group | item | Б | None |
| azk_11 | 0 | items[0].name | item | Сигарети JTI Camel Blue | Сигарети УП Сане} Blue |
| azk_11 | 0 | items[0].qty | item | 2 | 1 |
| azk_11 | 0 | items[0].unit_price | item | 175.00 | 350 |
| azk_11 | 0 | items[0].amount | item | 350.00 | 175 |
| azk_11 | 0 | items[0].vat_group | item | Б | None |
| azk_11 | 0 | items | lines | 4 рядків | 3 рядків, зіставлено 3 |
| food_01 | 0 | seller.name | wrong | ПІІ "МакДональдз Юкрейн Лтд" | МакДональдз Юкрейн Мга |
| food_01 | 0 | receipt_number | wrong | 000205557 | 0002053391 |
| food_01 | 0 | fiscal_number | missed | 3000932994 | None |
| food_01 | 0 | issued_at | wrong | 2026-05-25 21:51:01 | 2025-05-15 21:51:01+00:00 |
| food_01 | 0 | items[2].name | item | АПЕЛЬС СІК ВЕЛ МЕНЮ додатково | АПЕЛЬС СТК ВЕЛ МЕНЮ додатково |
| food_01 | 0 | items[2].vat_group | item | А | None |
| food_01 | 0 | items[1].name | item | ДІПИ КАРТОПЛЯНІ МЕНЮ додатково | КАРТОПЛЯНІ МЕНЮ додатково |
| food_01 | 0 | items[1].vat_group | item | А | None |
| food_03 | 0 | seller.name | missed | GoH Craft Pub | None |
| food_03 | 0 | issued_at | missed | 2026-04-24 19:43:00 | None |
| food_03 | 0 | payment_method | wrong | card | unknown |
| food_03 | 0 | items[10].name | item | Пиво Rebrew світле нефільтроване непастеризоване < POPELKA L | Пиво Rebrew світле нефільтроване непастеризоване POPELKA LAG |
| food_03 | 0 | items[5].name | item | Пиво MUZA IPA (5,4%) ПЕТ КЕГ 30л. Superdelic (келих 0.5) | Пиво MUZA IPA (5,4%) ПЕТ КЕГ 30л. Superdelic (келих 0,5) |
| food_03 | 0 | items[3].name | item | Пиво MUZA IPA (5,4%) ПЕТ КЕГ 30л. Superdelic (келих 0.3) | Пиво MUZA IPA (5,4%) ПЕТ КЕГ 30л. Superdelic (келих 0,3) |
| food_03 | 0 | items[6].name | item | Пиво світле Ne IPA Outback (келих 0.5) | Пиво світле IPA Outback (келих 0,5) |
| food_03 | 0 | items[7].name | item | Пиво Цитадель Хоппі Келлербір, кега 28л Хмільний Нуль (келих | Пиво Цитадель Xonni Kennep6ip, Kera 28h |
| food_03 | 0 | items[1].name | item | Пиво світле "Бургомістр Rein Пілснер", л (келих 0.5) | Хмільний Нуль (келих 0,5) |
| food_03 | 0 | items[0].name | item | Пиво Rebrew світле нефільтроване непастеризоване < POPELKA L | пастеризоване POPELKA LAGER (ЛОПЕЛКА ЛАГЕР), 5%, ПЕТ-кег (ке |
| food_03 | 0 | items[0].qty | item | 2 | 1 |
| food_03 | 0 | items[0].unit_price | item | 148.00 | 158 |
| food_03 | 0 | items[0].amount | item | 296.00 | 158 |
| food_03 | 0 | items | lines | 11 рядків | 12 рядків, зіставлено 11 |
| fop_01 | 0 | seller.name | wrong | ФО-П Федик О.Б. | Наркетопт |
| fop_01 | 0 | fiscal_number | missed | 3001247585 | None |
| fop_01 | 0 | items[1].name | item | 15577-Гірчиця ВЕРЕС Французька 130 г д/п | Гірчиця ВЕРЕС Франц Узька 130 г д/п |
| fop_01 | 0 | items[2].name | item | 29014-Хрін ВЕРЕС Український 130 г д/п | Хрін ВЕРЕС Український 130 г д/п |
| fop_01 | 0 | items[2].discount | item | 0.76 | 0.16 |
| fop_01 | 0 | items[3].name | item | 14458-Гірчиця ВЕРЕС Домашня 130 г д/п | Гірчиця ВЕРЕС Домашня 130 г д/п |
| fop_01 | 0 | items[5].name | item | 154737-ВВ Круасан зі смаком маракуйї 385 г | Круасан зі смаком маракуйї 385 г |
| fop_01 | 0 | items[5].discount | item | 3.03 | None |
| fop_01 | 0 | items[0].name | item | 106043-Хліб ІЛОНА Староукраїнський 500 г | Хліб ІЛОНА таро Ваїнський 500 г |
| fop_01 | 0 | items[6].name | item | 154745-ВВ Круасан Шоколад 350г | Круасан Шоколад 350 г |
| fop_01 | 0 | items[6].vat_group | item | А | B |
| fop_01 | 0 | items[7].name | item | 110936-Пакет п/е майка 340*550 МАРКЕТОПТ | Пакет п/е майка 34 х 50 см |
| fop_01 | 0 | items[4].name | item | 154733-ВВ Круасан Малина 385г | Круасан Малина 385 г |
| fop_01 | 0 | items[4].amount | item | 75.70 | 75 |
| fop_01 | 0 | items[4].discount | item | 3.03 | 0.7 |
| fop_02 | 0 | seller.name | wrong | ЗОРІНА КРІСТІНА ПАВЛІВНА | ФОП SOPIHA KPICTIHA ПАВЛІВНА |
| fop_02 | 0 | seller.tax_id | wrong | 2981206608 | 2081200608 |
| fop_02 | 0 | receipt_number | missed | 9988 | None |
| fop_02 | 0 | fiscal_number | wrong | 3001258680 | ТНа001074017 |
| fop_02 | 0 | issued_at | wrong | 2026-09-05 17:35:20 | 2026-05-05 00:00:00+03:00 |
| fop_02 | 0 | items[2].name | item | ПАКЕТИ ФАСУВАЛЬНІ №9 10 МКР 1000 ШТ/УП | ПАКЕТИ @ACYBAADHI №9 10 МКР 1000 WT |
| fop_02 | 0 | items[3].name | item | СЕРВЕЛАТ В/К В/С (НАКАТ) (Б) | CEPBEAAT B/K B/C CHAKAT |
| fop_02 | 0 | items[1].name | item | СОСИСКИ ДИТЯЧІ В/С (ЧЕРЕВА) (Б) | СОСИСКИ ДИТЯЧІ BSC CUEPEBA |
| fop_02 | 0 | items[0].name | item | СИР РАДОМЕР СЕРЕНАДА 45% КГ | СЕРЕНАДА 455 КГ |
| fop_02 | 0 | items[0].qty | item | 0.294 | 0.29 |
| fop_02 | 0 | items[0].unit_price | item | 419.90 | 419 |
| fop_02 | 0 | items[0].amount | item | 123.45 | 123.95 |
| shop_01 | 0 | seller.name | wrong | ТОВ "Приватінвест" | ТОВ "IIpuBarinBect" і магазин "BRAIN" |
| shop_01 | 0 | receipt_number | wrong | q64Dxa1JXX0 | q64DxalJXX0 |
| shop_01 | 0 | items[0].name | item | Монітор Dell S2725DC (210-BSRL) | Монітор Dell $2725DC (210-BSR) |
| shop_02 | 0 | seller.name | wrong | ТОВ "НОВА ЛІНІЯ 1" | ТОВ "ЛЬНИЙ КОМПЛЕКС TOP" |
| shop_02 | 0 | fiscal_number | wrong | 3000786185 | 3050786185 |
| shop_02 | 0 | items[2].name | item | Набір (Паста Gebatut2 80 | Hasip СПаста Gebatut2 80 |
| shop_02 | 0 | items[7].name | item | Стіки TEREA Arbor Pearl | Crikw TEREA Arbor Pearl |
| shop_02 | 0 | items[9].name | item | Стіки TEREA Amber | Crikw TEREA Amber |
| shop_02 | 0 | items[5].name | item | Гачок клейкий HSS-502S P | Гачок клейкий Н55-5025 Р |
| shop_02 | 0 | items[6].name | item | 63021 Завіска Vallen 180 | Завіска Uallen 180 |
| shop_02 | 0 | items[0].name | item | Карниз для душ. шторки B | Карниз ANA AYU. ШТОРКИ В |
| shop_02 | 0 | category | class | groceries | other |
| super_01 | 0 | seller.name | wrong | ТОВ "НОВУС УКРАЇНА" | ТОВ "HOBYC УК АННА" |
| super_01 | 0 | receipt_number | wrong | 106038 | 1060 |
| super_01 | 0 | items[5].name | item | Йогурт 2,2% Галичина ман. папая 300г пл. | Йогурт 2,2% Галичина ман. папая 30 |
| super_01 | 0 | items[5].qty | item | 1 | 3 |
| super_01 | 0 | items[8].name | item | Огірок тепличний ваг | Огірок тепличний |
| super_01 | 0 | items[8].qty | item | 0.548 | 2 |
| super_01 | 0 | items[8].unit_price | item | 35.89 | None |
| super_01 | 0 | items[1].name | item | Шинка Фітнес Яловича натуральна в/к ваг | Шинка фітнес Яловича натуральна |
| super_01 | 0 | items[1].qty | item | 0.144 | 1 |
| super_01 | 0 | items[1].unit_price | item | 999.00 | None |
| super_01 | 0 | items[10].name | item | Сметана 20% Галичина 300г стакан | Сметана 205 ралинина 300r стакан |
| super_01 | 0 | items[13].name | item | Пакет майка зелений біо | Пакет майка зелений 610 |
| super_01 | 0 | items[0].name | item | Пакет середній 34*55 Novus 7кг | пакет середня 34455 Novus |
| super_01 | 0 | items[9].name | item | Яйце куряче С0 Молодильне Ясенсвіт 10шт | Куряче Молодильне |
| super_01 | 0 | items[11].name | item | Сир к/м б/л 5% Яготин 350г пакет | Сир к/м б/л 5% Яготин 350r пакет |
| super_01 | 0 | items[11].unit_price | item | None | None |
| super_01 | 0 | items[11].amount | item | 119.00 | 9 |
| super_01 | 0 | items[6].name | item | Йогурт 2,2% Галичина ананас 300г пл. | Йогурт 2,25 Галичина ананас 300r п |
| super_01 | 0 | items[6].unit_price | item | None | None |
| super_01 | 0 | items[6].amount | item | 38.49 | 8.49 |
| super_01 | 0 | items[7].name | item | Йогурт 2,2% Ліс. ягода Галичина ПЕТ300г | Ліс. ягода Галичина Пе |
| super_01 | 0 | items[7].unit_price | item | None | None |
| super_01 | 0 | items[7].amount | item | 38.49 | 3.49 |
| super_01 | 0 | items[4].name | item | Козинаки хомка насіння+льон АСК 450г | Ятрань к/в ювілейна |
| super_01 | 0 | items | lines | 14 рядків | 12 рядків, зіставлено 11 |
