# Univerzita Karlova (2. LF UK) — modelové otázky

Kvíz v páté záložce. Úložiště `uk-learning-v2`, volba sekce `uk-section`, sekce `physics`, `chemistry`, `biology` a „Všechny otázky“. Generátor dávky `create_uk_001_050.py`, banka `uk-001-050.json`, začlenění do aplikace `uk_integration.py`.

## Zdroje (složka vlastníka „Univerzita Karlova“, mimo GitHub)

| Předmět | Soubor | Publikace | Rozsah | Klíč |
|---|---|---|---|---|
| Fyzika | `806318126-nahled-EK51316.pdf` | Amler a kol., *Modelové otázky z fyziky pro přijímací zkoušky*, Karolinum pro 2. LF UK, 8. vyd. 2023, ISBN 978-80-246-5740-0 | **jen ukázka**: 15 stran, úlohy 1.01–1.64 (Základní pojmy) a 2.01–2.05 (Mechanika I), str. 5–15 | v ukázce chybí, odpovědi ověřeny výpočtem |
| Chemie | `876103174-Modelove-Otazky-z-Chemie-Pro-Prijimaci-Zkousky.pdf` | Blanický, Pelouch, *Modelové otázky z chemie pro přijímací zkoušky*, Karolinum pro 2. LF UK, 7. vyd. 2019, ISBN 978-80-246-4441-7 | 220 stran, kap. 1–5, asi 1 180 otázek | správná písmena tučně přímo u otázek; otázky nejsou číslované, evidence je „str. X, otázka N“ (pořadí na tištěné stránce) |
| Biologie | `776944895-Modelove-Otazky-z-Biologie-Pro-Prijimaci-Zkousky.pdf` | Kočárek a kol., *Modelové otázky z biologie pro přijímací zkoušky*, Karolinum pro 2. LF UK, 7. vyd. 2019, ISBN 978-80-246-4443-1 | 206 stran, 11 kapitol, 920 otázek | str. 198–204 |

Všechna tři PDF vydala Univerzita Karlova (Nakladatelství Karolinum) pro 2. lékařskou fakultu UK. Tištěná strana odpovídá straně PDF. V originále může být správných 1–4 odpovědí; každá otázka kvízu je přeformulovaná tak, aby měla právě jednu obhajitelnou správnou odpověď.

## Dávka ID 1–50 (v2.44.0)

| Předmět | Kapitola | Použité úlohy | ID |
|---|---|---|---|
| Fyzika | 1. Základní pojmy (str. 5–10) | 1.01, 1.04, 1.06, 1.07, 1.08, 1.09, 1.10, 1.11, 1.13, 1.14, 1.31, 1.38, 1.41 | 1–13 |
| Fyzika | 2. Mechanika I (str. 15) | 2.01, 2.02, 2.03, 2.05 | 14–17 |
| Chemie | 1.1 Složení a struktura atomu | str. 8/2, 11/1, 11/5, 14/3, 14/6 | 18–22 |
| Chemie | 1.2 Periodická soustava | str. 18/6, 19/2, 21/2, 30/1 | 23–26 |
| Chemie | 1.3–1.5 Biogenní prvky, vazba, kinetika | str. 31/1, 32/5, 33/4, 34/1, 34/5 | 27–31 |
| Chemie | 1.7–1.8 Iontový součin vody, Brönstedova teorie | str. 37/4, 40/3, 40/5 | 32–34 |
| Biologie | Úvod do biologie (str. 10–13) | 10, 12, 15, 17, 18, 21, 22, 26 | 35–42 |
| Biologie | Buněčná biologie (str. 17–26) | 33, 36, 40, 41, 48, 54, 66, 88 | 43–50 |

Převod na jednu správnou odpověď: fyzika 1.06 a 1.11 (v originále více správných), 2.01 a 2.05 (formulace vztahu); chemie str. 40/5 (amfolyt, distraktor amoniak nahrazen, protože i NH₃ je amfoterní); biologie 17 (zúženo na místo glykolýzy), 21 (otázka na děj, který katabolický není), 15 (upřesněno na vnitřní membránu mitochondrií).

Porovnání se stávajícími sadami podle ověřovaného poznatku (somatologie, biologie, České Budějovice, LF MU):
- Nepřidáno jako duplicita: chemie str. 30/6 (hlavní kationt plazmy Na⁺, BIO 73), biologie 125 (karyotyp, BIO 702 a ČB 576), biologie 28 (kobalt ve vitaminu B12, blízké BIO 892).
- Příbuzné, ale přidané jako jiná znalost: chemie str. 8/2 (význam l) vs. LF MU 71 (hodnoty l); biologie 15 (umístění oxidativní fosforylace) vs. LF MU 96 (úloha dýchacího řetězce); biologie 41 (syntéza mitochondriálních bílkovin) vs. LF MU 42 (vlastní ribozomy organel); biologie 54 (izotonické prostředí) vs. LF MU 97 (hypertonický roztok); biologie 40 (kolagen v mezibuněčné hmotě) vs. BIO 11 (kolagenní vlákna a pevnost); chemie str. 31/1 (Mg v chlorofylu) vs. biologie 26 (porfyrinové jádro).
- Vynecháno jako stejný poznatek v rámci dávky: fyzika 1.15 (výpočet kapání jako 1.14), 2.04 (stejná situace jako 2.03).
- Odloženo jako sporné: biologie 115 (inkrustace × impregnace se v učebnicích definují různě), fyzika 1.53 (rok jako vedlejší jednotka) a 1.54 (význam slova „vteřina“).

## Další dávky

Pokračovat od ID 51. Nedotčeno: fyzika úlohy 1.02–1.03, 1.05, 1.12, 1.15–1.30, 1.32–1.37, 1.39–1.40, 1.42–1.64, 2.04 (zbytek fyziky po str. 15 v ukázce chybí, plná kniha není k dispozici); chemie zbytek kap. 1 a kap. 2–5 (str. 42–219); biologie zbytek kapitol Úvod a Buněčná biologie a kapitoly Molekulární biologie až Historie (str. 40–197). Úplné pokrytí zatím nebylo dosaženo.
