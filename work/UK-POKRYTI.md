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

## Další dávky

Pokračovat od ID 451. Fyzika čeká na plnou knihu. Chemie pokračuje kap. 4.11 od str. 166, biologie od otázky 591 a zbytek 542–588. Úplné pokrytí zatím nebylo dosaženo.
