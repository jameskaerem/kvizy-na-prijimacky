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

## Dávka ID 51–100 (v2.46.0)

Soubor `uk-051-100.json`, generátor `create_uk_051_100.py`. Odpovědi fyziky ověřeny výpočtem, chemie a biologie porovnány s klíčem.

| Předmět | Kapitola | Použité úlohy | ID |
|---|---|---|---|
| Fyzika | 1. Základní pojmy (str. 5–13) | 1.05, 1.12, 1.15, 1.27, 1.28, 1.30, 1.32, 1.34, 1.36, 1.37, 1.39, 1.40, 1.47, 1.49, 1.52, 1.56 | 51–66 |
| Chemie | 1.1–1.8 | str. 15/1, 15/2, 24/2, 32/3, 34/3, 36/3, 36/4, 38/6, 41/1 | 67–75 |
| Chemie | 2.1 Anorganické sloučeniny | str. 44/4, 47/2, 48/2, 53/3, 53/5, 57/1, 59/5 | 76–82 |
| Chemie | 2.2.1 Kyseliny a zásady | str. 66/1, 68/1 | 83–84 |
| Biologie | Buněčná biologie (str. 35–36) | 135, 141 | 85–86 |
| Biologie | Molekulární biologie (str. 41–67) | 159, 162, 163, 197, 201, 202, 216, 217, 225, 251, 255, 284, 287, 291 | 87–100 |

Převod na jednu správnou odpověď: fyzika 1.27, 1.28, 1.30, 1.34, 1.36 (v originále více správných vyjádření, ptáme se na jedno), 1.39 (zúženo na roční období), 1.05 (nejmenší dostatečné balení); biologie 217 (doplněno „téměř“ univerzální kvůli výjimkám v mitochondriích).

Porovnání se stávajícími sadami:
- Nepřidáno jako duplicita: fyzika 1.48, 1.60–1.62 (skalár a vektor, ČB 534), 1.16–1.25 a 1.63–1.64 (základní a odvozené jednotky SI, LF MU 1 a ČB 543), 1.45–1.46 (převod km/h, UK 4), 1.02–1.03 (hmotnost vody, UK 1); chemie str. 19/3 (helium ve vesmíru, ve vysvětlení UK 24); biologie 123 (meióza ze dvou dělení, SOM 31), 148 (erytrocyt bez jádra, BIO 86), 153 (základní typy tkání, biologická sada), 189 a 272 (rRNA v jadérku, SOM 27), 176 (tRNA v translaci, SOM 23), 139 (osmotická lýza, LF MU 97 a UK 48).
- Příbuzné, ale přidané jako jiná znalost: chemie str. 15/1 (beta plus) vs. UK 22 (beta minus); fyzika 1.15 (objem láhve) vs. UK 10 (kapky za minutu); fyzika 1.12 (tera) vs. 1.56 (sada předpon); biologie 197 (aminoacyl-tRNA-syntetáza) vs. SOM 23 (tRNA přenáší aminokyseliny).
- Vynecháno v rámci dávky: chemie str. 35/1 (definice kinetiky), 36/1 (součin rozpustnosti, UK 33), 59/4 (sublimát, ve vysvětlení UK 82).
- Odloženo jako sporné: fyzika 1.50 (km jako odvozená jednotka) a 1.53–1.54 jako v první dávce.

## Dávka ID 101–150 (v2.47.0)

Soubor `uk-101-150.json`, generátor `create_uk_101_150.py`. Textová kopie chemie, kterou vlastník dodal 22. 11. 2026, nemá tučně vyznačená správná písmena, proto jsou odpovědi chemie ověřené výkladem a do kvízu šly jen otázky s jednoznačnou odpovědí. Biologie porovnána s klíčem (str. 198–204). PDF ukázky fyziky je bajtově shodné se soupisem zdrojů (SHA-256 `cfee5765…`).

| Předmět | Kapitola | Použité úlohy | ID |
|---|---|---|---|
| Fyzika | 1. Základní pojmy (str. 12) | 1.55 | 101 |
| Chemie | 2.1 Anorganické sloučeniny (str. 42–61) | str. 42/4, 43/1, 44/2, 46/1, 47/5, 48/4, 49/5, 50/1, 50/2, 59/3, 51/2, 51/6, 52/1, 53/6, 54/3, 54/4, 54/6, 55/1, 55/4, 56/5, 57/2, 57/4, 57/6, 58/1, 58/6, 59/2, 59/6, 60/2, 60/3, 60/4, 61/2, 61/4, 61/6 | 102–134 |
| Chemie | 2.2.1 Kyseliny a zásady (str. 62–64) | str. 62/3, 63/3, 64/6 | 135–137 |
| Biologie | Molekulární biologie (str. 67–69) | 292, 294, 295, 296, 301, 302 | 138–143 |
| Biologie | Genetika (str. 71–73) | 305, 306, 307, 308, 309, 310, 312 | 144–150 |

Převod na jednu správnou odpověď: biologie 292 (ptáme se na renaturaci, hybridizace je ve vysvětlení), 305 (spojeno „a“ a „d“ klíče), 306 (otázka obrácena na vyloučenou skupinu 0), 312 (spojeno „b“ a „d“).

**Fyzika: ukázka je tímto vyčerpaná.** Zbylé úlohy 1.02–1.03, 1.16–1.26, 1.29, 1.33, 1.35, 1.41–1.46, 1.48, 1.51, 1.57–1.64 a 2.04 testují stejný poznatek jako už zařazené otázky (UK 1, 4, 13, 14–17, 56–58, 66 a ČB 534, LF MU 1); 1.50, 1.53 a 1.54 zůstávají odložené jako sporné. Další fyzika UK vyžaduje plnou knihu Amler a kol.

Chemie kap. 2.1 (str. 42–62) je tím celá posouzená. Nepřidané položky:
- Stejný poznatek jako existující otázka: 44/4 a 45/1 (amfoterní oxid, UK 76), 45/6, 47/1, 47/3 (vodík v hydridech, UK 77), 48/3 a 48/5 (karbid vápenatý, UK 78), 50/6, 56/6, 57/1, 57/3 (přechodná tvrdost, UK 81), 51/3, 59/4, 59/5 (rtuťné a rtuťnaté soli, UK 82), 51/4 (hydrogensiřičitan, ČB 525), 52/2 (hydrogenfosforečnan, LF MU 31), 52/3 (dichroman, LF MU 28), 53/3, 53/4, 54/2 (pálené a hašené vápno, UK 79), 53/5 (sádra, UK 80), 54/5 (modrá skalice, vysvětlení UK 73), 59/1 (lučavka, UK 84).
- Varianta otázky téže dávky: 42/1–42/2, 43/2–43/6, 44/1, 44/3 (zásadotvorné a kyselinotvorné oxidy, UK 102–103), 45/4–45/5 (oxidy fosforu, UK 102), 49/1 (karbidy, UK 107), 49/6 (hydrogen-soli síry, UK 109), 50/5 (kamenec, UK 111), 57/5, 58/3, 58/4 (CS₂ a H₂S, UK 123–124), 60/1 (souhrn triviálních názvů UK 116, 131), 61/3, 62/2 (fosgen, UK 132), 61/5 (kyanid, UK 133).
- Prosté přiřazení vzorce a názvu, poznatek pokrývají otázky na pravidla názvosloví v sadách LF MU a UK: 47/4, 48/6, 49/2–49/4, 50/3, 51/1, 51/5, 52/4–52/6, 53/1–53/2, 54/1, 55/5, 58/2.
- Odloženo jako sporné bez tučného klíče: 42/3, 43/4, 44/5, 44/6, 45/2, 45/3 (klasifikace oxidů podle mezních oxidačních čísel je specifická pro učebnici), 46/3–46/6 (polarita vazby v PH₃ je hraniční), 47/6 a 48/1 (CuCl₂ jako iontový halogenid), 55/2–55/3 (neexistující komplexy), 58/5 (koncentrace jodové tinktury).
- Ponecháno pro další dávku: 46/2 (skupenství iontových hydridů), 55/6, 56/1–56/4 (rozpustnost uhličitanů a síranů), 60/5–60/6, 61/1, 62/1 (jedovaté plyny a sloučeniny rtuti).

Biologie 291–312: 291 (UK 100), 293 (cukr v nukleotidech, ČB 301), 297–298 (párování bází, LF MU 94), 299–300 (kodon a antikodon, UK 91 a 93), 303 (nukleotid jako stavební jednotka), 304 (promotor, UK 87) nebyly přidány jako stejný poznatek; 311 je varianta 309.

## Dávka ID 151–200 (v2.49.0)

Soubor `uk-151-200.json`, generátor `create_uk_151_200.py` (společná pomocná funkce `batch_tools.py`). Chemie ověřena výkladem, biologie porovnána s klíčem.

| Předmět | Kapitola | Použité úlohy | ID |
|---|---|---|---|
| Chemie | 2.1 Anorganické sloučeniny (odložené) | str. 46/2, 56/2, 56/3 | 151–153 |
| Chemie | 2.2.1 Kyseliny a zásady (str. 63–69) | str. 63/2, 64/1, 64/2, 66/2, 66/3, 66/5, 66/6, 67/3, 67/4, 67/5, 67/6, 68/2, 68/3, 68/4, 68/6, 69/1 | 154–169 |
| Chemie | 2.2.2 Hydrolýza solí (str. 69–70) | str. 69/3, 70/1, 70/2 | 170–172 |
| Chemie | 2.3 Oxidační číslo, oxidace a redukce (str. 70–76) | str. 70/4, 71/3, 72/1, 73/3, 73/6, 74/1, 74/5, 75/2, 75/3, 76/5 | 173–182 |
| Biologie | Genetika (str. 73–83) | 313, 319, 323, 325, 327, 328, 337, 338, 339, 341, 342, 343, 344, 345, 353, 357, 361, 363 | 183–200 |

Nepřidané položky:
- Kap. 2.1, zbytek odložených: 55/6, 56/1, 56/4 (varianty 152–153 a vysvětlení UK 133), 60/5–60/6, 61/1 (jedovaté plyny a kyanidy: CO je v ČB 269 a BIO 249, fosgen v UK 132, kyanid v UK 133), 62/1 (sublimát, vysvětlení UK 82).
- Kap. 2.2.1 (str. 62–69): 62/4–62/6, 63/1, 63/4–63/6 (názvosloví kyselin, varianty UK 135, 136, 154), 64/3–64/5 (elektrolyty, varianty 155–156), 65/1–65/6 a 66/1 (síla kyselin, UK 83 a 137), 66/4 (neutralizace jako protolýza, varianta 158), 67/1 (vysvětlení UK 137), 67/2 (varianta 159), 68/1 (UK 84), 68/5 (varianta 162).
- Kap. 2.2.2: 69/2, 69/4, 69/5, 70/3 (hydrolýza, varianty 170–172).
- Kap. 2.3 do str. 76: 70/5, 71/1, 71/2, 71/4–71/6, 72/2, 72/4, 72/5, 73/2, 73/4, 73/5, 74/2–74/4, 74/6, 75/1 (určení oxidačního čísla, varianty 173–180 a ČB 528, 530), 72/6 a 73/1 (fluor, ČB 528), 75/4–75/6, 76/1–76/4, 76/6 (oxidační a redukční činidla, varianty 181–182). Odloženo jako sporné: 72/3 (fosfor může mít oxidační číslo IV, např. v H₄P₂O₆).
- Biologie 313–365: 314 (žádná možnost není správná, klíč d), 315–316 (polygenní systém, varianta 197), 317 (zdroje proměnlivosti, souhrnně pokryté UK 86 a ČB 206), 318 (varianta 200), 320, 332–334, 355, 356, 358, 359, 365 (základní pojmy alela, homozygot a dominance, LF MU 144–145 a UK 148), 321, 331, 349 (štěpné poměry, ČB 118 a LF MU 145, 148), 322 (definice populace), 324 (výpočty z q², LF MU 150), 326 a 330 (hemofilie, SOM 41 a ČB 203), 329 a 360 (daltonismus a X-recesivní dědičnost, SOM 42 a UK 191), 335 a 347 (vazba genů, LF MU 148), 336 (varianta 184), 340 a 348 (varianty 187 a 192), 346 (rodokmen hemofilie, varianta 183 a 194), 350–352 (varianty 191, 195, 200), 354 (genom, ČB 291), 362 (gamety dihybrida, ČB 206), 364 (monogenní znaky, varianta 199).

## Dávka ID 201–250 (v2.51.0)

Soubor `uk-201-250.json`, generátor `create_uk_201_250.py` (sdílený `batch_tools.py`). Chemie ověřena výpočtem a výkladem (textová kopie nemá vyznačený klíč), biologie porovnána s klíčem. Otázky s více správnými možnostmi přeformulovány na jednu správnou.

| Předmět | Kapitola | Použité úlohy | ID |
|---|---|---|---|
| Chemie | 2.3 Oxidace a redukce (str. 77–79) | str. 77/3, 77/5, 77/6, 78/2, 78/6, 79/1, 79/2, 79/3, 79/4, 79/5 | 201–210 |
| Chemie | 2.4 Elektrolýza (str. 79–81) | str. 79/6, 80/4, 81/3 | 211–213 |
| Chemie | 2.5 Úprava chemických rovnic (str. 81–83) | str. 81/4, 82/1, 82/2, 82/3, 83/1, 83/3 | 214–219 |
| Chemie | 3.1 Výpočty z chemických vzorců (str. 84–86) | str. 84/1, 85/3, 85/5, 86/3 | 220–223 |
| Chemie | 3.2 Látkové množství a koncentrace (str. 87–96) | str. 87/2, 88/1, 88/2, 89/4, 92/2, 92/5, 95/3, 96/3, 96/4 | 224–232 |
| Biologie | Genetika (str. 84–94) | 367, 369, 370, 371, 375, 376, 383, 391, 392, 399, 402, 403, 405, 406, 410, 411, 413, 418 | 233–250 |

Nepřidané položky:
- Kap. 2.3 str. 77–79: 77/1, 77/2, 78/1, 78/3–78/5 (definice oxidace a redukce, varianty 203, 210 a UK 181–182), 77/4 (CuSO₄ + Fe, UK 73).
- Kap. 2.4: 80/1–80/3, 80/5, 81/1, 81/2 (produkty elektrolýzy NaCl a KCl, varianty 211–212).
- Kap. 2.5: 82/4 (nabídka v textové kopii neúplná), 83/2 a 83/4 (stejný postup jako 214 a 219).
- Kap. 3.1: 84/2, 84/3, 85/1, 85/2 (hmotnost prvku ve sloučenině, varianta 220), 85/4 (varianta 221), 86/1 (Glauberova sůl, varianta 222), 86/2 (varianta 223).
- Kap. 3.2 str. 86–96: 86/4, 86/5, 87/1, 87/3–87/6 (jednotky veličin, varianta 224 a ČB 543, LF MU 14), 88/3 (hodnota N_A, ve vysvětlení 226), 88/4–88/6, 89/1 (počet atomů ve vzorci, triviální), 89/2, 89/3, 89/5, 90/1–90/5, 91/1–91/5, 92/3, 92/4 (n = m/M a počet částic, varianty 227 a 231), 92/1 (varianta 228), 93/1–93/5, 94/1–94/5 (c = m/(M·V), varianta 229; 94/4 a 94/5 mají v zadání chybné Ar), 95/1, 95/2, 95/4, 95/5, 96/1, 96/2 (m = c·V·M, varianta 230), 96/5 (varianta 232).
- Biologie 366–420: 366, 372 (alela a genotyp, ČB 407 a LF MU 140), 368 a 374 (dominantní a X-vázaná dědičnost, UK 189 a 191), 373, 377, 378, 419, 420 (Mendelovy štěpné poměry, ČB 118, UK 148, 196), 379 (vazba genů, LF MU 147), 380 (centimorgan, ve vysvětlení 250), 381 a 382 (polygenní a multifaktoriální znaky, LF MU 200 a varianta 234), 384 (konkordance dvojčat, sporné zadání), 385, 386, 390, 414, 415 (panmixie, faktory frekvence alel a drift, UK 184, 185, 192), 387–389, 401 (výpočty H–W, varianta 240 a LF MU 150), 393 a 407–409 (X-recesivní dědičnost a hemofilie, UK 191, SOM 38–41), 394 a 396 (autozomově recesivní dědičnost, UK 190), 395 (vlastnosti mutací, obecné), 397 (trizomie, BIO 837 a LF MU 149), 398 a 400 (zpětné křížení a 1/16, varianty 235 a ČB 118), 404 (pojmy křížení, triviální), 412 (alogamická populace, opak 249), 416 (proband, ČB 568), 417 (organizace prenatální diagnostiky v ČR, časově citlivé).

## Dávka ID 251–300 (v2.53.0)

Soubor `uk-251-300.json`, generátor `create_uk_251_300.py`. Chemie ověřena výpočtem a výkladem, biologie porovnána s klíčem. Otázky s více správnými možnostmi přeformulovány na jednu správnou.

| Předmět | Kapitola | Použité úlohy | ID |
|---|---|---|---|
| Chemie | 3.2 Látkové množství (str. 97) | str. 97/1, 97/3 | 251–252 |
| Chemie | 3.3 Hmotnostní a objemový zlomek (str. 98–105) | str. 98/1, 101/1, 101/4, 103/5, 104/2, 105/4 | 253–258 |
| Chemie | 3.4 Molární objem plynu (str. 106–108) | str. 106/1, 107/5 | 259–260 |
| Chemie | 3.5 pH kyselin a zásad (str. 108–117) | str. 111/5, 112/3, 115/3, 117/1 | 261–264 |
| Chemie | 4.1 Reakce organických sloučenin a činidla (str. 118–121) | str. 118/1, 118/2, 118/3, 119/1, 119/3, 119/4, 119/5, 120/1, 120/3, 121/3 | 265–274 |
| Chemie | 4.2 Izomerie, konformace, konfigurace (str. 122–125) | str. 122/1, 122/4, 123/2, 123/5, 124/1, 124/5, 125/2, 125/3 | 275–282 |
| Biologie | Genetika (str. 95–103) | 422, 433, 434, 436, 437, 448, 451, 452, 453, 455, 458, 459, 460, 461 | 283–296 |
| Biologie | Bakteriologie a virologie (str. 105–106) | 463, 465, 470, 472 | 297–300 |

Nepřidané položky:
- Chemie str. 97–105: 97/2, 97/4 (varianty 251–252), 98/2, 98/3 (varianta 253), 98/4, 98/5, 99/1–99/5, 100/1–100/5, 101/3, 103/3, 103/4 (m = w · m(roztoku), LF MU 126 a ČB 584), 101/2 (varianta 254), 101/5, 102/1–102/5 (ředění vodou, varianta 255 a LF MU 127), 103/1, 103/2 (hmotnostní zlomek prvku, UK 220–221), 104/1 (varianta 256), 104/3–104/5, 105/1–105/3 (varianty 257), 105/5 (varianta 258).
- Kap. 3.4: 106/2–106/5, 107/1–107/4, 108/1 (varianty 259–260).
- Kap. 3.5: 108/2–108/5, 109/1–109/5, 110/1–110/5, 111/1–111/4, 112/1, 112/2, 112/4–112/6, 113/1–113/6, 114/1–114/5, 115/1, 115/2, 115/4, 115/5, 116/1–116/5, 117/2–117/4 (převody pH, [H₃O⁺] a [OH⁻] a ředění, varianty 261–264, LF MU 186–188, 227–234 a ČB 532). 109/2–109/5 mají v zadání „roztok silné báze“ s pH pod 7, vynecháno jako zavádějící.
- Kap. 4.1: 119/2 (reakce jen jako obrázek), 120/2, 120/4–120/6, 121/1, 121/2, 121/4, 121/5 (zařazení činidel, varianty 271–274).
- Kap. 4.2: 122/2, 122/3, 122/5, 123/1 (keto- a enolforma, varianty 275–276), 123/3, 123/4, 123/6 (chiralita, varianty 277–278), 124/2–124/4, 124/6 (konformace a cis-trans, varianty 279–281), 125/1 a 125/5 (vzorce jen jako obrázek), 125/4 (konstituční izomerie, varianta 282).
- Biologie 421–472: 421, 423, 430–432, 454 (H–W a drift, UK 184–185, 240 a 249), 424, 443 (daltonismus, SOM 42 a UK 199), 425 (AR rodiče Aa × Aa, UK 190), 426 (otcovství, žádného z mužů nelze vyloučit, zadání nejednoznačné), 427 a 428 (A × B, LF MU 193), 429 (9 : 3 : 3 : 1, ČB 118), 435 (heritabilita 1, varianta 249 z dávky 233–250), 438, 462 (rodokmen a proband, ČB 568), 439, 440 (Morganovo číslo, UK 250), 441 a 447 (XD a AD dědičnost, UK 189 a 200), 442, 444, 446 (AR dědičnost, UK 190 a 194), 445 a 450 (hemofilie, ČB 203 a SOM 41), 449 (minorgeny, UK 197), 456 (Klinefelter, UK 245), 457 (organizace prenatální péče, časově citlivé), 464 (archea, nejednoznačné), 466, 467 (chromozom a stavba prokaryot, LF MU 139 a SOM 15), 468 (viry, SOM 12), 469 (bakteriofág, UK 88), 471 (prion, BIO 535).

## Dávka ID 301–350 (v2.55.0)

Soubor `uk-301-350.json`, generátor `create_uk_301_350.py`. Chemie ověřena výkladem a počítáním vazeb (textová kopie nemá vyznačený klíč), biologie porovnána s klíčem. Otázky s více správnými možnostmi přeformulovány na jednu správnou.

| Předmět | Kapitola | Použité úlohy | ID |
|---|---|---|---|
| Chemie | 4.2 Izomerie (str. 126) | str. 126/3 | 301 |
| Chemie | 4.3 Alifatické a alicyklické uhlovodíky (str. 127–135) | str. 127/1, 127/2, 127/4, 127/6, 128/1, 128/4, 129/2, 130/2, 130/3, 130/5, 131/4, 131/5, 131/6, 132/1, 132/3, 132/4, 132/6, 133/6, 134/2, 134/4, 134/5, 135/1, 135/4 | 302–324 |
| Chemie | 4.4 Aromatické uhlovodíky (str. 136–139) | str. 136/3, 136/4, 137/1, 137/2, 137/5, 138/1, 138/3, 138/4, 138/6, 139/3 | 325–334 |
| Biologie | Bakteriologie a virologie (str. 108–109) | 481, 482, 484, 486, 487, 488 | 335–340 |
| Biologie | Biologie rostlin a hub (str. 112–116) | 491, 495, 497, 501, 505, 507, 508, 511, 512, 515 | 341–350 |

Nepřidané položky:
- Chemie str. 126–139: 126/1, 126/2, 128/6, 129/1, 129/3, 129/4, 134/3, 135/6, 136/1, 136/2 (vzorce jen jako obrázek), 126/4 (homologická řada, triviální), 126/5 a 131/3 (dva názvy CCl₄), 127/3 (formulace „téměř vždy“), 127/5 (varianta 304), 128/2 (vinyl, varianta 306), 128/3 (alkyly butanu, varianta 307), 128/5, 133/2, 133/4, 133/5 (adice bromu, UK 267 a 321), 130/1 (varianta 267), 130/4 (cyklohexan zařazen mezi alkany, sporné), 130/6 (freony, varianta 311), 131/1, 131/2 (nasycené vzorce, varianta 309; 131/2 má dvě stejné možnosti), 132/2 (nejjednodušší alken, triviální), 132/5 (CₙH₂ₙ, ve vysvětlení 309), 133/1, 133/3, 135/2 (hydrogenace na alkan, triviální), 134/1 (varianta 319), 135/3 („kolik vazeb“ nejednoznačné), 135/5 (klíč „vinylalkohol“ je jen nestálý meziprodukt, tautomerie v UK 276), 137/3 (acetofenon, žádná možnost nesedí), 137/4 (toluen aromatický, triviální), 138/2 (homologická řada benzenu, triviální), 138/5 (mononitrací toluenu nevzniká TNT, zadání nejednoznačné), 139/1 (o-xylen, varianta 333), 139/2 (výroba styrenu, ve vysvětlení 328 jen vzorec), 139/4–139/6 (kondenzované areny, varianty 334; 139/4 a 139/5 mají dvě správné možnosti).
- Biologie 473–515: 473 (HIV a pomocné T lymfocyty, BIO 828), 474 (reverzní transkriptáza, LF MU 88), 475, 477, 490 (složení virionu, UK 300 a SOM 12), 476 (bakteriofág, UK 88), 478, 479 (viry a virová onemocnění, UK 299), 480 (prokaryota, UK 298), 483 (výživa bakterií, triviální), 485 (bakteriofág, UK 88), 489 (stafylokoky, ve vysvětlení 340), 492 (produkty fotosyntézy, voda jen v rozepsané rovnici, nejednoznačné), 493 (plazmolýza, LF MU 91), 494 (námel, dvě správné možnosti), 496, 498–500 (pigmenty a fáze fotosyntézy, více správných možností, pro další dávku), 502 (plastidy, UK 44), 503, 504, 506, 509, 510, 513, 514 (více správných možností, pro další dávku).

## Dávka ID 351–400 (v2.57.0)

Soubor `uk-351-400.json`, generátor `create_uk_351_400.py`. Chemie ověřena výkladem, biologie porovnána s klíčem. Otázky s více správnými možnostmi přeformulovány na jednu správnou.

| Předmět | Kapitola | Použité úlohy | ID |
|---|---|---|---|
| Chemie | 4.5 Terpeny (str. 144–145) | str. 144/4, 145/2, 145/3, 145/4, 145/5 | 351–355 |
| Chemie | 4.6 Alkoholy a thioly (str. 145–150) | str. 145/6, 146/3, 146/4, 146/6, 148/1–148/6, 149/1, 149/2, 149/3, 149/5, 150/2 | 356–370 |
| Chemie | 4.7 Fenoly (str. 150–152) | str. 150/3, 150/6, 151/3, 151/4, 152/2, 151/5, 151/6 | 371–377 |
| Chemie | 4.8 Aldehydy (str. 152) | str. 152/3, 152/6 | 378–379 |
| Biologie | Biologie rostlin a hub (str. 113–116) | 496, 498, 500, 503, 504, 506, 509, 510, 513 | 380–388 |
| Biologie | Biologie živočichů a protistů (str. 118–122) | 517, 519, 521, 523, 524, 525, 526, 527, 529, 532, 537, 539 | 389–400 |

Nepřidané položky:
- Chemie str. 139–152: 139/6, 140/1, 140/2 (kondenzované areny, varianta 334), 140/3, 140/4, 141/1–141/3, 142/1–142/3, 143/1–143/3, 144/1, 144/2, 147/1 (vzorce jen jako obrázek), 144/3 a 145/1 (počty isoprenů, varianty 351–352), 146/1 (varianta 356), 146/2 a 146/5 (glycerol trojsytný, ve vysvětlení 357), 149/4 (vinylalkohol a acetaldehyd, UK 276), 149/6 a 150/1 (thioly a disulfidy, varianta 370), 150/4 (varianta 371), 150/5 (dvě správné možnosti, naftoly ve 372), 151/1 (α-naftol, ve vysvětlení 372), 151/2 (dvě správné možnosti, varianta 373), 152/1 (fenoláty jako soli, ve vysvětlení 377), 152/4 a 152/5 (formaldehyd z methanolu, varianta 360).
- Biologie 496–539: 497, 501, 505, 507, 508, 511, 512, 515 (už v dávce 301–350), 499 (fáze fotosyntézy, ve vysvětlení 381–382), 502 (plastidy semiautonomní, UK 44 a LF MU 42), 514 (dvouděložné, opak 388), 516 (okolík, ve vysvětlení 350), 518 (močovina v játrech, BIO 299), 520 (nervová trubice z ektodermu, BIO 453), 522 (toxoplazma, dvě správné možnosti, pro další dávku), 528 (původ struny hřbetní, varianta 397), 530 (okysličení krve v aortě ryb, sporný klíč), 531, 533–536, 538 (více správných možností, pro další dávku).

## Dávka ID 401–450 (v2.59.0)

Soubor `uk-401-450.json`, generátor `create_uk_401_450.py`. Chemie ověřena výkladem, biologie porovnána s klíčem. Otázky s více správnými možnostmi přeformulovány na jednu správnou.

| Předmět | Kapitola | Použité úlohy | ID |
|---|---|---|---|
| Chemie | 4.8 Aldehydy (str. 153) | str. 153/1, 153/2, 153/5 | 401–403 |
| Chemie | 4.9 Ketony a ethery (str. 155–156) | str. 155/4, 155/5, 156/3, 156/6 | 404–407 |
| Chemie | 4.10 Karboxylové kyseliny a deriváty (str. 157–164) | str. 159/1, 157/2, 157/3, 157/6, 158/3, 158/4, 158/5, 158/6, 159/3, 159/4, 161/3, 160/2, 160/4, 160/5, 161/4, 161/6, 162/1, 162/3, 162/6, 163/1, 163/4, 163/5, 164/1, 164/2 | 408–431 |
| Chemie | 4.11 Aminy, amidy, alkaloidy (str. 166) | str. 166/3 | 432 |
| Biologie | Biologie živočichů a protistů (str. 122–130) | 540, 541, 543, 545, 546, 548, 549, 556, 557, 558, 562, 568, 572, 574, 576, 578, 580, 589 | 433–450 |

Nepřidané položky:
- Chemie str. 153–164: 153/3 (butanal, varianta 401), 153/4, 155/2, 157/1 (vzorce aldehydu, ketonu a etheru, varianta 408), 153/6, 154/1–155/1 (vzorce jen jako obrázek), 155/3 (dvě správné možnosti, aceton ve 404), 156/1, 156/2 (redukce ketonu, varianta 404), 156/4 (benzochinon z hydrochinonu, UK 373), 156/5 (acetofenon, ve 405), 157/4 (chiralita hydroxykyselin, UK 278), 157/5 (varianta 410), 158/1, 158/2 (varianty 412), 159/2 (název esteru, varianta 415), 159/5 (vzorec vinyl-acetátu, OCR nečitelné), 159/6 (dvě správné možnosti, malonová = propandiová, varianta 418), 160/1 (keton z 2-hydroxymáselné kyseliny, sporné, acetoctová vzniká z 3-hydroxymáselné), 160/3 (varianta 419), 160/6, 161/1 (laktát na pyruvát, varianta 421 a LF MU 345), 161/2 (varianta 418), 161/5 (hydrogenace fumarátu, varianta 423), 162/2 (varianta 424), 162/4, 162/5 (kyselina benzoová z toluenu, UK 332), 163/2, 163/3 (varianty 427–428), 163/6 (kyselina ftalová z o-xylenu, pro další dávku), 164/3 (vzorce v OCR neúplné).
- Biologie 540–590: 542, 544, 550, 551, 553, 569, 570, 581–584, 587 (více správných možností, část přeformulována, zbytek pro další dávku), 547 (trichomonáda, BIO 826), 552, 559, 563, 571 (zařazení ploštěnců a hlístic, LF MU 396 a UK 443), 554 (ježura, UK 391), 555 (amnion plazů a savců, varianta 448), 560, 561, 564, 585 (spavá nemoc a malárie, LF MU 399–400), 565 (lamblie, LF MU 299), 577, 590 (oddělené oběhy ptáků a savců, LF MU 395), 566, 567, 573, 579, 586, 588 (pro další dávku).

## Dávka ID 451–500 (v2.61.0)

Soubor `uk-451-500.json`, generátor `create_uk_451_500.py`. Chemie ověřena výkladem, biologie porovnána s klíčem. Otázky s více správnými možnostmi přeformulovány na jednu správnou.

| Předmět | Kapitola | Použité úlohy | ID |
|---|---|---|---|
| Chemie | 4.11 Aminy, amidy, alkaloidy (str. 166–170) | str. 166/5, 167/1, 168/1, 168/4, 168/5, 169/2, 169/3, 169/5, 169/6, 170/2 | 451–460 |
| Chemie | 5.1 Heterocyklické sloučeniny (str. 171–177) | str. 171/1, 172/1, 172/4, 172/5, 172/6, 173/6, 174/1, 174/2, 174/3, 174/5, 174/6, 175/2, 175/3, 175/4, 175/6, 176/1, 176/2, 176/3, 176/4, 176/6, 177/1 | 461–481 |
| Chemie | 5.2 Monosacharidy (str. 179) | str. 179/3 | 482 |
| Biologie | Biologie živočichů a protistů (str. 122–133) | 542, 544, 566, 567, 569, 573, 581, 583, 584, 586, 587, 588, 593, 596, 598, 605 | 483–498 |
| Biologie | Biologie člověka (str. 137–138) | 620, 623 | 499–500 |

Nepřidané položky:
- Chemie str. 166–179: 166/2–166/4 (zápis aminů, UK 432), 167/2 (varianta 452), 168/2, 168/3, 177/2–179/2 (vzorce jen jako obrázek), 169/1, 169/4 (varianty 454 a 457), 170/1 (varianta 460), 172/2, 172/3, 173/1, 175/1 (dvě správné možnosti), 173/2–173/5 (pyrrol a porfyrin v hemu a chlorofylu, UK 42), 174/4 (varianta 469), 175/5 (varianta 474), 176/5 (varianta 479).
- Biologie 542–625: 550, 553, 570 (více správných možností, trypanozoma a toxoplazma v LF MU 399 a UK 522), 591 (žebříčková nervová soustava, SOM 66), 592 (struna hřbetní, UK 397), 594, 595, 602–604 (plíce, oběh, teplokrevnost a komorové oko, UK 449, 491 a 390), 597 (vzdušnice, SOM 239), 599, 600 (komorové a složené oko, UK 390), 601 (kostra žraloka, UK 446), 606–619, 621, 622, 624, 625 (biologie člověka pokrytá bankami SOM, BIO a ČB, například obratle BIO 31–32, nefron BIO 336–339, oko BIO 651–678, Langerhansovy ostrůvky BIO 588, vestibulární ústrojí BIO 616–630).

## Dávka ID 501–550 (v2.63.0)

Soubor `uk-501-550.json`, generátor `create_uk_501_550.py`. Chemie ověřena výkladem, biologie porovnána s klíčem. Otázky s více správnými možnostmi přeformulovány na jednu správnou.

| Předmět | Kapitola | Použité úlohy | ID |
|---|---|---|---|
| Chemie | 5.2 Monosacharidy, disacharidy, polysacharidy (str. 179–185) | str. 179/4, 180/2, 180/3, 180/5, 180/6, 181/1, 181/4, 181/5, 182/1, 182/3, 183/1, 183/6, 183/2, 184/1, 184/2, 184/5, 185/2 | 501–517 |
| Chemie | 5.3 Lipidy (str. 185–190) | str. 185/3, 185/6, 186/3, 186/4, 187/1, 187/3, 187/5, 188/1, 188/2, 188/4, 188/6, 189/2, 189/3, 189/5, 190/1 | 518–532 |
| Biologie | Biologie člověka (str. 138–145) | 626, 631, 632, 633, 634, 635, 638, 640, 641, 643, 646, 651, 654, 656, 658, 661, 662, 665 | 533–550 |

Nepřidané položky:
- Chemie str. 180–190: 180/1 (varianta 501), 180/4 (varianta 503), 181/2, 181/3, 181/6 (složení laktózy a sacharózy, BIO 286–287), 182/2 (maltóza, v 507), 182/4–182/6 (varianty 510), 183/3–183/5 (varianty 511), 184/3 (glykogen u živočichů, BIO 298, ČB 16), 184/4, 184/6 (celulóza, BIO 265 a 516), 185/1 (Fehlingova reakce, BIO 869), 185/4, 185/5, 186/1 (varianty 518–519), 186/2, 186/5, 186/6 (varianty 520–521), 187/2, 187/4, 187/6, 188/3, 188/5 (varianty 523–527), 189/1 (esenciální kyselina linolová, BIO 322), 189/4, 189/6, 190/2, 190/3 (varianty 530–532), 190/4 (cholesterol jako sterol, ČB 280).
- Biologie 626–665: 627 (kortikoidy kůry nadledvin, BIO 578), 628, 636 (imunoglobuliny a plazmatické buňky, BIO 107), 629 (menopauza, BIO 798), 630 (vitamin D, ČB 15), 637 (myofibrily, SOM 110), 639, 642 (triceps a biceps, BIO 61–62), 644, 645 (testosteron, ČB 329, SOM 543), 647, 649 (čípky a tyčinky, BIO 664, ČB 638), 648 (sluch, BIO 637), 650 (aldosteron, ČB 355), 652 (neuron, ČB 408), 653 (synapse, BIO 411–414), 655 (ADH, BIO 349), 657 (TSH, BIO 550), 659, 660 (dendrit a axon, SOM 68, BIO 394), 663 (inzulin, BIO 589), 664 (hladká svalovina střeva, BIO 70).

## Dávka ID 551–600 (v2.65.0)

Soubor `uk-551-600.json`, generátor `create_uk_551_600.py`. Chemie ověřena výkladem, biologie porovnána s klíčem. Otázky s více správnými možnostmi přeformulovány na jednu správnou.

| Předmět | Kapitola | Použité úlohy | ID |
|---|---|---|---|
| Chemie | 5.4 Vitaminy (str. 191–193) | str. 191/2, 191/3, 191/4, 191/6, 192/1, 192/2, 192/4, 193/1 | 551–558 |
| Chemie | 5.5 Hormony (str. 193) | str. 193/2 | 559 |
| Chemie | 5.6 Aminokyseliny (str. 195–205) | str. 195/1, 195/3, 195/5, 195/6, 196/1, 197/3, 197/4, 197/5, 198/1, 198/3, 198/4, 198/6, 199/1, 202/1–202/5, 203/1–203/5, 204/3, 205/2 | 560–584 |
| Chemie | 5.7 Bílkoviny, peptidy (str. 206) | str. 206/3 | 585 |
| Biologie | Biologie člověka (str. 146–153) | 670, 671, 672, 674, 676, 677, 679, 680, 684, 688, 696, 703, 705, 710, 712 | 586–600 |

Nepřidané položky:
- Chemie str. 190–206: 190/5, 190/6, 191/1 (rozpustnost vitaminů, BIO 324), 191/5 (tokoferol, BIO 896), 192/3 (UK 471), 192/5 (varianta 557), 192/6 (fylochinony, varianta 554), 193/3, 193/4, 194/5 (steroidní hormony, UK 532), 193/5, 193/6 (hormony štítné žlázy, BIO 562), 194/1, 194/6 (inzulin a glukagon, BIO 589–592), 194/2 (glukagon, ČB 611), 194/3 (dřeň nadledvin, UK 546), 194/4 (parathormon, BIO 570–571), 195/2, 195/4 (varianty 561), 197/1 (esenciální aminokyseliny, BIO 304), 197/2, 197/6, 202/6, 204/2 (serin, varianta 565), 198/2, 199/3, 204/5 (aromatické aminokyseliny a tyrosin, varianty 569 a 582), 198/5 (varianta 570), 199/2 (varianta 571), 199/4–201/4, 205/1, 205/3, 206/1 (vzorce jen jako obrázek), 203/6, 204/1, 204/4 (varianty 573, 574 a 581), 206/2, 206/4 (varianty 585).
- Biologie 666–712: 666 (křivice, BIO 895), 667 (vitamin C, BIO 894), 668 (obecná úloha vitaminů, BIO 325), 669 (poplicnice, BIO 202), 673, 675, 682, 685, 687, 693 (všechny možnosti správné, obecné výčty), 678 (vrátník, ČB 520), 681 (močová trubice, BIO 732), 683 (receptory synapse, BIO 413), 686 (obrana leukocytů, BIO 105), 689 (levá síň, ČB 25), 690 (dvě nesprávné možnosti), 691 (klíč chybí), 692 (komplement, BIO 103), 694 (B-lymfocyty, BIO 111), 695 (plazmatické buňky, BIO 107), 697 (pepsin, BIO 274), 698 (vrátnicová žíla, BIO 128), 699 (tlusté střevo, BIO 293), 700 (dýchací centrum, SOM 266), 701 (ADH, BIO 349), 702 (limbický systém, BIO 499), 704 (deltový sval, SOM 133), 706 (homeostáza, BIO 3), 707 (erytrocyty, BIO 84–86), 708 (BIO 87), 709 (hemolýza, BIO 89, SOM 152), 711 (srdeční automacie, odloženo do další dávky).

## Dávka ID 601–650 (v2.67.0)

Soubor `uk-601-650.json`, generátor `create_uk_601_650.py`. Chemie ověřena výkladem, biologie porovnána s klíčem. Otázky s více správnými možnostmi přeformulovány na jednu správnou.

| Předmět | Kapitola | Použité úlohy | ID |
|---|---|---|---|
| Chemie | 5.7 Bílkoviny, peptidy (str. 207–211) | str. 207/3, 207/5, 208/3, 208/4, 208/5, 209/1, 209/3, 209/4, 209/5, 209/6, 210/6, 211/3, 211/4 | 601–613 |
| Chemie | 5.8 Enzymy a metabolismus (str. 211–217) | str. 211/5, 211/6, 212/1, 212/2, 212/5, 212/6, 213/2, 213/5, 214/2, 214/3, 215/4, 216/3, 216/5, 217/2 | 614–627 |
| Chemie | 5.9 Nukleové kyseliny (str. 218) | str. 218/2, 218/3, 218/5 | 628–630 |
| Biologie | Biologie člověka (str. 153–168) | 713, 733, 739, 740, 742, 757, 762, 767, 772, 777, 779, 785, 786, 787, 789, 798, 801, 802 | 631–648 |
| Biologie | Evoluční biologie (str. 170) | 804, 805 | 649–650 |

Nepřidané položky:
- Chemie str. 206–219: 206/5, 206/6, 207/1, 207/2 (vzorce jen jako obrázek), 207/4 (varianta 601), 208/1 (varianta 602), 208/2 (L-aminokyseliny, UK 564), 208/6 (více správných možností, vazby v terciární struktuře uvedeny v 605), 209/2 (pyrrol v hemu a chlorofylu, UK 42), 210/1 (varianta 610), 210/2 (albumin, BIO 300), 210/3, 210/4, 211/1, 211/2 (fibrilární bílkoviny, varianty 608–609), 210/5 (kolagen, BIO 362), 212/3, 212/4 (varianty 617), 213/1, 213/3, 213/4, 213/6, 214/1, 217/1 (varianty 619–621), 214/4, 214/5 (varianty 623), 214/6, 215/1 (fotosyntéza, UK 343, 382), 215/2 (laktát, LF MU 243), 215/3 (BIO 308), 215/5, 215/6, 216/1, 216/2, 216/4 (varianty 624), 216/6 (monoacylglycerol, UK 523), 217/3, 217/4 (močovina, BIO 299), 217/5 (ATP, BIO 53), 217/6, 218/1 (proteosyntéza a tRNA, SOM 23, ČB 201), 218/4 (varianta 630), 219/1, 219/2 (báze, UK 475–476), 219/3 (varianta 629), 219/4 (dvojšroubovice, LF MU 36).
- Biologie 711–810: 711 (srdeční automacie, BIO 67), 714 (SOM 266), 715 (SOM 244), 716 (BIO 264), 717 (SOM 303), 718 (SOM 332), 719 (vitamin K, UK 555), 720, 721 (ČB 520, BIO 272), 722 (BIO 340), 723 (nefron), 724 (inzulin, BIO 589), 725, 729, 755, 756 (hypofýza, BIO 546–549, UK 545), 726, 727 (glukokortikoidy a stres, BIO 578, UK 541), 728, 743, 771 (štítná žláza, BIO 562, ČB 257), 730 (proprioreceptory, UK 537), 731 (BIO 446), 732 (BIO 398), 734, 748 (vady oka, BIO 681–684), 735 (UK 543), 736 (BIO 616), 737 (SOM 543), 738 (UK 539), 741 (BIO 644), 744, 747, 750–752 (sítnice, BIO 662–667), 745 (SOM 474), 746 (BIO 690), 749 (BIO 110), 753 (BIO 654), 754 (BIO 58), 758 (glykogen, SOM 311), 759, 765, 766 (rozpustnost vitaminů, BIO 324), 760 (BIO 112), 761 (BIO 627), 763 (hematokrit, ČB 274), 764 (BIO 375), 768 (BIO 536), 769 (kosterní sval, BIO 51), 770 (mapa chuti na jazyku je zastaralá), 773 (počet menstruačních cyklů, obecné), 774 (dendritická buňka, neúplný výklad), 775, 788 (řízení srdce, BIO 68), 776 (BIO 453), 778 (BIO 394), 780 (BIO 224), 781 (ČB 106), 782 (BIO 168), 783, 784 (sluch a světlo, BIO 637, UK 544), 790, 792, 796 (všechny nebo více správných), 791, 793 (varianty 640), 794 (ČB 622), 795, 799 (závislosti, obecné), 797 (očkování, BIO 108), 800 (krevní obraz, obecné), 803 (více správných), 806 (SOM 3), 807 (sporný klíč, první savci se objevují až v pozdním triasu), 808 (ČB 400), 809 (ČB 553), 810 (více správných, trilobiti UK 442).

## Dávka ID 651–700 (v2.69.0)

Soubor `uk-651-700.json`, generátor `create_uk_651_700.py`. Biologie porovnána s klíčem a se současnými poznatky. Otázky s více správnými možnostmi přeformulovány na jednu správnou. Chemie je tímto uzavřená: všech 1 137 úloh str. 7–219 je použito nebo vyřazeno s důvodem v předchozích dávkách.

| Předmět | Kapitola | Použité úlohy | ID |
|---|---|---|---|
| Biologie | Evoluční biologie (str. 172–180) | 813, 815, 817, 818, 819, 820, 821, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 836, 837, 838, 839, 840, 841, 842, 843, 845, 846, 848, 850, 852, 854, 855, 856 | 651–685 |
| Biologie | Ekologie (str. 182–185) | 857, 858, 859, 860, 861, 862, 863, 864, 865, 867, 870, 871, 872, 873, 874 | 686–700 |

Úpravy klíče: 817 (kniha uvádí střední juru, nejstarší nesporné krytosemenné jsou ze spodní křídy, proto otázka zní na druhohory), 852 (klíč v knize chybí, odpověď o křížení podle sekvenování neandrtálského genomu), 832 (místo chůze po dvou, ČB 553, zjišťuje objem mozkovny), 829 (Moravský kras vynechán, aby byla jedna správná možnost).

Nepřidané položky:
- Biologie 811–874: 811 (všechny možnosti správné, hominizace LF MU 486), 812 (Darwinův přírodní výběr, ČB 131), 814, 853 (pořadí druhů Homo, LF MU 484), 816 (sporné, nejstarší jisté fosilie křídlatého hmyzu jsou až z karbonu), 822 (vznik mitochondrií, LF MU 487), 835, 844 (progenoti, UK 650), 847 (varianta 679), 849 (varianta 677), 851 (africký původ, varianta 655), 866 (varianta 694), 868 (ekosystém, LF MU 492), 869 (populace, LF MU 498).

## Dávka ID 701–737 (v2.71.0)

Soubor `uk-701-737.json`, generátor `create_uk_701_737.py` (`batch_tools.build` nově přijímá kratší závěrečnou dávku). Biologie porovnána s klíčem. Otázky s více správnými možnostmi přeformulovány na jednu správnou.

| Předmět | Kapitola | Použité úlohy | ID |
|---|---|---|---|
| Biologie | Ekologie (str. 185–187) | 876, 877, 878, 879, 880, 881, 883, 884, 885 | 701–709 |
| Biologie | Historie biologie a medicíny (str. 189–196) | 886, 887, 888, 890, 891, 892, 893, 894, 898, 899, 900, 901, 902, 904, 905, 906, 908, 909, 910, 912, 913, 914, 915, 916, 917, 918, 919, 920 | 710–737 |

Úpravy: 877 (všechny čtyři možnosti jsou národní parky, otázka se ptá na CHKO Český ráj), 900 (správný je i Watson, proto jsou distraktory jen badatelé před rokem 1901), 905, 906, 915, 916, 917 a 920 zúženy na jeden poznatek z výčtu správných možností.

Nepřidané položky:
- Biologie 875–920: 875 (skleníkový efekt, LF MU 494), 882 (parazité, varianta 689), 889 (Darwin a přírodní výběr, ČB 131), 895 (dvoušroubovice DNA, LF MU 36), 896 (buněčná teorie, ČB 377), 897 (klíč chybí a obhajitelných je více možností), 903 (Purkyně a buněčná teorie, LF MU 37), 907 (Jesenius, ČB 411), 911 (Nightingalová, ČB 467).

## Formát zkoušky a dávka ID 738–787 (v2.75.0)

Od verze 2.74.0 kvíz Univerzity Karlovy používá formát přijímací zkoušky 2. LF UK: možnosti se zaškrtávají a správných může být více, jedna, nebo žádná. Nové otázky proto přebírají úlohy knihy v původním znění a pořadí možností a–d i s úplným klíčem (pole `answers`). Starší otázky 1–737 zůstávají beze změny, kvůli uloženému pokroku.

Kontrola pokrytí 22. 11. 2026 ukázala, že u biologie 1–290 mapa neuvádí, proč nebyla použita asi stovka úloh. Šlo hlavně o úlohy s více správnými odpověďmi. Doplňují se postupně v tomto formátu.

Soubor `uk-738-787.json`, generátor `create_uk_738_787.py` (`batch_tools.build_multi`). Klíč podle knihy (str. 198–199). Úloha 31 nemá v textové kopii klíč, odpověď b, c, d je ověřená výkladem (prokaryota = archea a bakterie včetně sinic).

| Předmět | Kapitola | Úlohy | ID |
|---|---|---|---|
| Biologie | Úvod do biologie (str. 9–14) | 1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 16, 19, 20, 23, 25, 27, 29 | 738–754 |
| Biologie | Buněčná biologie (str. 16–26) | 31, 32, 34, 35, 37, 38, 39, 44, 45, 49, 50, 51, 52, 55, 56, 57, 58, 59, 60, 61, 62, 63, 68, 69, 72, 74, 76, 77, 78, 79, 80, 83, 84 | 755–787 |

Úpravy znění: 51 „intermediární filamenta“ místo tiskové chyby „intermediální mikrofilamenta“, 39 oprava překlepu „steně“. Otázky mají úplnou větu, aby se nezaměňovaly se staršími otázkami se stejným začátkem.

Nepřidáno v rozsahu 1–84:
- Stejný poznatek jako starší otázka: 4 (gameta, BIO 697), 28 (kobalt v B12, BIO 892), 30 (katabolismus, UK 40), 42 (bílkoviny a ribozomy mitochondrií, UK 46), 46 (jadérko a ribozomy, SOM 27), 47 (meióza, ČB 115), 64, 65 a 70 (haploidní gameta a výsledek meiózy, ČB 577 a LF MU 766), 67 (cytokineze a telofáze, nová 774), 71 (barvení v metafázi, nová 772), 73 (mitochondrie, nová 758), 75 (semiautonomní organely, UK 44 a LF MU 42).
- Pro další dávku: 14, 24 (ATP), 43 (funkce ER), 81, 82 (typy určení pohlaví).
- Sporný klíč: 53 (pinocytóza, klíč zahrnuje vstřebávání tukových kapének v tenkém střevě pinocytózou, což současný výklad trávení tuků nepodporuje).
- Úlohy 85 a výš se doplní v další dávce.

## Dávka ID 788–837 (v2.76.0)

Soubor `uk-788-837.json`, generátor `create_uk_788_837.py`. Formát zkoušky s více správnými odpověďmi, znění a klíč podle knihy (str. 198–199).

| Předmět | Kapitola | Úlohy | ID |
|---|---|---|---|
| Biologie | Úvod do biologie (str. 11) | 14 | 788 |
| Biologie | Buněčná biologie (str. 18–38) | 43, 81, 82, 85, 86, 87, 90, 91, 93, 95, 96, 97, 98, 99, 101, 102, 104, 112, 113, 114, 116, 118, 119, 121, 122, 124, 126, 128, 129, 130, 131, 132, 134, 138, 140, 143, 144, 145, 146, 147, 149, 151, 152, 154 | 789–832 |
| Biologie | Molekulární biologie (str. 40–41) | 155, 156, 157, 158, 160 | 833–837 |

Nepřidáno v rozsahu 85–160:
- Stejný poznatek jako starší nebo nová otázka: 24 (ATP z oxidativní fosforylace, nová 788), 89 (zygota 46 chromozomů, nová 787), 92 a 110 (složení biomembrán, nové 757 a 767), 94, 105, 106 a 120 (replikace v S fázi, nové 776 a 799), 100 (trizomie, BIO a ČB), 103 (mitochondrie jako energetické centrum, nová 758), 108 a 136 (Golgiho komplex, nová 781), 109 (lysozomy, nová 760), 111 (aktivní transport proteiny, nová 759), 117 (generační doba, nová 806), 127 (kontrolní bod v G1, UK 49), 133 (metafáze, nová 772), 142 (crossing-over v profázi I, UK 86), 107 (heterotrofie, ČB 260 a UK 41), 137 (pohlavní chromozom spermie, ČB 202), 150 (akrozom, BIO 709).
- Už dříve vyřazeno (viz dávky 1–150): 115 (sporné), 123, 125, 139, 148, 153.
- Úlohy 159 a výš se doplní v dalších dávkách.

## Dávka ID 838–887 (v2.77.0)

Soubor `uk-838-887.json`, generátor `create_uk_838_887.py`. Formát zkoušky s více správnými odpověďmi, znění a klíč podle knihy (str. 199), klíč všech 50 úloh strojově porovnán s knihou.

| Předmět | Kapitola | Úlohy | ID |
|---|---|---|---|
| Biologie | Molekulární biologie (str. 41–57) | 161, 164, 166, 167, 168, 169, 170, 173, 175, 177, 178, 179, 180, 182, 184, 186, 190, 191, 194, 196, 199, 200, 203, 204, 205, 208, 210, 211, 212, 213, 214, 218, 219, 220, 221, 222, 223, 224, 226, 227, 228, 229, 231, 232, 233, 234, 235, 236, 237, 238 | 838–887 |

Nepřidáno v rozsahu 159–240 (stejný poznatek jako starší nebo nová otázka):
- 165 (reverzní transkriptáza, LF MU 88), 171 (mimojaderná DNA, UK 305), 172 (ústřední dogma, nová 834), 174, 183 a 185 (páry bází, nové 843 a 855, LF MU 94), 176 (tRNA v translaci, SOM 23), 181 (Amesův test, LF MU 497), 187 (definice translace, nové 838 a 868), 188 a 215 (kodon, nová 851), 189 (rRNA v jadérku, SOM 27), 192 a 193 (tRNA a antikodon, nové 848 a 858), 195 a 209 (nukleotidy jako stavební jednotka, nové 859 a 864), 198 a 239 (semikonzervativní replikace, nová 846), 206 a 207 (Chargaffovo pravidlo, nové 862 a 863), 230 (introny, LF MU 47 a nová 842), 240 (definice transkripce, nové 853 a 868).
- Úlohy 159, 160, 162, 163, 197, 201, 202, 216, 217 a 225 už byly použity dříve.
- Úlohy 241 a výš se doplní v dalších dávkách.

## Dávka ID 888–937 (v2.78.0)

Soubor `uk-888-937.json`, generátor `create_uk_888_937.py`. Formát zkoušky s více správnými odpověďmi, klíč všech 50 úloh strojově porovnán s knihou (str. 199).

| Předmět | Kapitola | Úlohy | ID |
|---|---|---|---|
| Biologie | Molekulární biologie (str. 58–69) | 244, 245, 246, 247, 252, 256, 258, 259, 260, 263, 265, 268, 271, 275, 276, 278, 279, 282, 283, 285, 286, 289, 290, 304 | 888–911 |
| Biologie | Genetika (str. 73–89) | 311, 314, 315, 317, 320, 321, 322, 324, 329, 332, 333, 335, 336, 340, 347, 351, 355, 359, 362, 368, 373, 382, 384, 386, 393, 395 | 912–937 |

Nepřidáno v rozsahu 241–400 (stejný poznatek jako starší nebo nová otázka):
- Molekulární biologie: 241 a 274 (translace, nové 838 a 840), 242, 243 a 281 (tichá a záměnová mutace, nová 845), 248, 293 a 303 (stavba nukleotidu, nová 859), 249 (hnRNA, UK 140 a nová 847), 250 (sekvence genu určuje protein, nová 856), 253 (proteiny jádra z cytoplazmy, nová 867), 254, 297 a 298 (komplementarita bází, nová 843), 257 (RNA-polymeráza, nová 853), 261, 262 a 300 (předloha translace, nová 858), 264, 288 a 299 (kodon, nové 851 a 870), 266 (plazmidy, UK 143), 267 (mimojaderná DNA, UK 144), 269 (telomery, UK 47), 270 (nukleozom, UK 85), 272 (rRNA v jadérku, SOM 27), 273 (tRNA, nová 848), 277 (degenerace kódu, nové 869 a 870), 280 (delece a posun rámce, UK 141).
- Genetika: 316 a 381 (geny malého účinku, UK 197), 318 a 352 (X-vázaná dominance, UK 200), 326 (hemofilik a zdravá žena, ČB 117), 330 (přenašečka hemofilie, UK 183), 331, 378 a 400 (štěpné poměry dihybrida, ČB 118 a LF MU 148), 334 a 366 (alely, nová 922), 346 (rodina s hemofilií, UK 286), 348 (brachydaktylie, UK 186), 349, 356 a 377 (uniformita a 1:2:1, nová 932), 350 (AD choroba Aa × Aa, UK 193 a nová 932), 354 (genom, nová 908), 358 (neúplná dominance, nová 912), 360 a 374 (X-vázaná recesivita, nové 920 a 927), 364 (krevní skupiny jako monogenní znak, UK 146 a 199), 365 (AA × aa, nová 929), 372 (genotyp, BIO 705), 379 (vazba genů, nové 926 a 930), 380 (centimorgan, UK 250), 387–389 (výpočty Hardyho–Weinbergova zákona, UK 240 a nová 919), 390 (drift, UK 184), 394 a 396 (albinismus, UK 190 a nová 925), 397 (trizomie, BIO a ČB), 398 (zpětné křížení, UK 235).
- Úlohy 401 a výš se doplní v dalších dávkách.

## Dávka ID 938–987 (v2.79.0)

Soubor `uk-938-987.json`, generátor `create_uk_938_987.py`. Formát zkoušky s více správnými odpověďmi, klíč všech 50 úloh strojově porovnán s knihou (str. 199–200).

| Předmět | Kapitola | Úlohy | ID |
|---|---|---|---|
| Biologie | Genetika (str. 91–102) | 404, 415, 417, 420, 426, 428, 431, 439, 440, 457 | 938–947 |
| Biologie | Bakteriologie a virologie (str. 105–110) | 464, 469, 475, 477, 478, 480, 483, 485, 489 | 948–956 |
| Biologie | Biologie rostlin a hub (str. 112–116) | 492, 494, 499, 502, 514, 516 | 957–962 |
| Biologie | Biologie živočichů a protistů (str. 119–133) | 522, 528, 530, 531, 534, 538, 550, 551, 552, 553, 561, 570, 577, 579, 582, 591, 592, 594, 600, 601, 603 | 963–983 |
| Biologie | Biologie člověka (str. 135–139) | 609, 615, 628, 630 | 984–987 |

Nepřidáno v rozsahu 401–604 (stejný poznatek jako starší nebo nová otázka):
- Genetika: 401, 430, 432 a 454 (výpočty Hardyho–Weinbergova zákona, UK 149, 240 a 292, nové 919 a 944), 407 (hemofilie na X, BIO 836), 408 (holandrická dědičnost, UK 244), 409, 424 a 443 (daltonismus a X-vázaná dědičnost, nová 920), 412 (alogamická populace, UK 147), 414 a 423 (drift, UK 184 a nová 924), 416 a 462 (proband, ČB 568), 419 a 429 (9:3:3:1, ČB 118 a nová 941), 421 (podmínky genetické rovnováhy, UK 185), 425, 442 a 444 (rodiče u AR choroby, nová 913), 427 (krevní skupiny A × B, LF MU 194), 435 (heritabilita, UK 248), 438 (genealogické vyšetření, ČB 13), 441 (X-vázaná dominance, UK 200), 445 (riziko u přenašečky hemofilie, UK 183), 446 (aa × Aa, UK 194), 447 (AD choroba u heterozygotů, UK 189), 449 (geny malého účinku, UK 197), 450 (hemofilik a zdravá žena, ČB 117), 456 (Klinefelterův syndrom, UK 245).
- Bakteriologie a virologie: 466 (kruhový chromozom prokaryot, UK 337), 467 (co prokaryota nemají, UK 298), 468 a 490 (stavba a množení virů, nové 950 a 952), 471 (prion, BIO 535), 473 (HIV a pomocné T lymfocyty, BIO 828), 474 (retroviry, nová 894), 476 (bakteriofág, nová 949), 479 (virová onemocnění, UK 299).
- Rostliny a živočichové: 493 (plazmolýza, LF MU 91), 518 (močovina v játrech, BIO 299), 520 (nervová trubice, BIO 453), 533, 559, 563 a 571 (hlísti a ploštěnci, LF MU 396, nové 970 a 971), 535 (nehty z pokožky, SOM), 536 a 555 (zárodečné obaly, UK 399 a 448), 547 (trichomoniáza, BIO 826), 554 (ježura, UK 438), 560 a 585 (přenašeči spavé nemoci a malárie, LF MU 399 a 400), 564 (původce malárie, nová 973), 565 (lamblie, LF MU 299), 575 (gonochorismus, LF MU 391 a 476), 590 a 595 (oddělený krevní oběh, nové 975 a 983), 597 (vzdušnice, nová 966), 599 a 604 (komorové oko, UK 390), 602 (teplokrevní živočichové, UK 491).
- Úlohy 605 a výš (kromě již použitých 609, 615, 628 a 630) se doplní v dalších dávkách.

## Stav pokrytí

Chemie (Blanický, Pelouch, 1 137 úloh str. 7–219) je posouzená celá. Biologie (Kočárek, 920 otázek) má ověřené úlohy 85–290 jen částečně: nepoužité úlohy s více správnými odpověďmi se doplňují od ID 788 (viz oddíly výše). Fyzika (Amler) je pokrytá jen v rozsahu dodané ukázky (úlohy 1.01–1.64 a 2.01–2.05). Pro další fyziku je potřeba plná kniha. Další dávka začne od ID 988.
