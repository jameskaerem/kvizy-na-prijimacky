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

## Další dávky

Pokračovat od ID 151. Fyzika čeká na plnou knihu. Chemie pokračuje odloženými položkami kap. 2.1 a kapitolou 2.2 (str. 62+), biologie genetikou od otázky 313 (str. 73+). Úplné pokrytí zatím nebylo dosaženo.
