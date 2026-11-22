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

## Další dávky

Pokračovat od ID 251. Fyzika čeká na plnou knihu. Chemie pokračuje kap. 3.2 od str. 97, biologie od otázky 421. Úplné pokrytí zatím nebylo dosaženo.
