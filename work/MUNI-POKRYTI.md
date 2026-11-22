# LF MU — modelové testové otázky (2018)

Zdroj: `916110468-Modelove-Testove-Otazky-k-Prijimacim-Zkouskam-Na-LF-MU-fyzika-chemie-biologie-Vojtech-Mornstein-Jiri-Dostal-Iva-Slaninov.pdf`, Vojtěch Mornstein, Jiří Dostál, Iva Slaninová, ISBN 978-80-210-9045-3. Čísla stran jsou tištěná (PDF = strana + 1).

| Oddíl | Tištěné strany | Klíč | Stav |
|---|---|---|---|
| Fyzika | 7–59 | 60 | 312 otázek, všech osm kapitol posouzeno celé (stav 2.73.0) |
| Chemie | 62–119 | 120 | 318 otázek, všech šest kapitol posouzeno celé (stav 2.73.0) |
| Biologie | 122–153 | 154 | 139 otázek, všech sedm kapitol posouzeno celé (stav 2.73.0) |

První dávka ID 1–50: přesná čísla původních úloh u každé položky v `muni-001-050.json` (kapitola + číslo, protože číslování začíná v oddílech znovu). Úlohy mají vlastní formulaci a čtyři možnosti. Seskupené odkazy označují příbuzné zdrojové varianty, nikoli další samostatné otázky. V původním klíči E označuje chybějící správnou možnost; např. fyzika 24, 26 a 40 jsou převedeny na otázky s explicitní správnou odpovědí.

Při porovnání s existujícími sadami nebyly vybrány zrychlení v SI (ČB 537), prosté určení skaláru (ČB 534), ani mol jako základní jednotka (ČB 543) jako samostatné položky. Obdobné výpočty a znalosti je nutné dále porovnávat před každou další dávkou. Nezpracované položky, nečitelné případy a rozpor s klíčem zůstávají otevřené; úplné pokrytí nebylo dosaženo.

## Druhá dávka ID 51–100 (v2.41.0)

Soubor `muni-051-100.json`, generátor `create_muni_051_100.py`. Odpovědi ověřeny výpočtem nebo výkladem a porovnány s klíčem na str. 60, 120 a 154.

| Předmět | Kapitola (tištěné strany) | Použité úlohy | ID |
|---|---|---|---|
| Fyzika | Kinematika a dynamika (11–14) | 1, 2, 3, 5, 6, 8, 12, 14, 20, 27 | 51–60 |
| Fyzika | Práce, energie a výkon (15) | 36, 37, 39, 43 | 61–64 |
| Fyzika | Otáčivý pohyb (17), Gravitace (18) | 51; 58, 64 | 65–67 |
| Chemie | Stavba atomu (67–70) | 1, 2, 5, 8, 14, 18, 22, 26, 30, 31, 41 | 68–78 |
| Chemie | Chemická vazba (70–71) | 48, 50, 52, 58, 60, 62 | 79–84 |
| Biologie | Biologie buňky (123–131) | 5, 12, 13, 29, 32, 35, 40, 48, 52, 56, 62, 63, 75, 76, 78, 86 | 85–100 |

Klíč E (žádná nabídnutá možnost) převeden na explicitní správnou odpověď: fyzika kinematika 3 (a = 20 m·s⁻²), gravitace 58 (r/100), chemie 8 (l = 0, 1, 2), biologie buňky 12 (S fáze).

Porovnání s existujícími sadami podle ověřované znalosti:
- Nepřidáno jako duplicita: chemie 24 (počet valenčních elektronů draslíku, ČB 529), biologie buňky 21 (přepis DNA do mRNA s antiparalelní komplementaritou, ČB 120).
- Příbuzné, ale přidané jako jiná znalost: gravitace 58 (zákon gravitační síly) vs. ČB 542 (Coulombův zákon); biologie 78 (chromatidy v metafázi II) vs. ČB 122 (metafáze mitózy); biologie 5 (stavba bakteriální buňky) vs. ČB 302 (penicilin a buněčná stěna); houpačka 27 (rovnováha momentů) vs. ČB 581 (změna ramene síly).
- Vynecháno jako stejný poznatek v rámci dávky: kinematika 4 (stejný vztah jako 3), 17 a 18 (stejné vztahy jako 14 a 20), 23 (rovnováha sil jako 12), chemie 4 (n² jako 5), 9 a 10 (konfigurace jako 14).
- Nejasné a odložené: chemie 28 (exponent v PDF nečitelný), 66 (klíč b, ale vodíkové vazby tvoří i NH₃), biologie buňky 62 v původním znění (ATP i aminokyseliny také procházejí póry; otázka přeformulována s jednoznačnými distraktory), fyzika gravitace 62 (zdůvodnění beztíže odstředivou silou je sporné).

## Třetí dávka ID 101–150 (v2.48.0)

Soubor `muni-101-150.json`, generátor `create_muni_101_150.py`. Zdroj dodal vlastník 22. 11. 2026 jako textovou kopii (OCR) téže publikace. Odpovědi ověřeny výpočtem nebo výkladem a porovnány s klíčem na str. 60, 120 a 154.

| Předmět | Kapitola (tištěné strany) | Použité úlohy | ID |
|---|---|---|---|
| Fyzika | Hydrostatika (19–22) | 1, 3, 6, 7, 9, 11, 14, 15, 21, 24, 27, 29, 30, 32 | 101–114 |
| Fyzika | Hydrodynamika (22–24) | 33, 35, 38, 40, 41, 48, 51, 54 | 115–122 |
| Fyzika | Pružnost (24–25) | 56, 59, 62 | 123–125 |
| Chemie | Roztoky, výpočty koncentrací (73–76) | 1, 3, 4, 8, 15, 17, 18, 19, 26, 30, 33, 40, 48 | 126–138 |
| Biologie | Genetika (132–134) | 3, 6, 7, 10, 14, 18, 21, 23, 24, 26, 29, 31 | 139–150 |

Klíč E převeden na explicitní správnou odpověď: fyzika 9 (1 torr ≈ 133 Pa), 14 (těleso zůstane v klidu), chemie 1 (1,92 g), 15 (w = 0,200).

Hydrostatika, hydrodynamika a pružnost (úlohy 1–64) jsou tím posouzené celé. Nepřidané úlohy:
- Varianta téhož poznatku v této dávce: 2 (vztah pro lis, ve vysvětlení 101), 4, 5, 31 (Archimedův zákon jako princip, 102), 8, 22, 23 (hodnoty tlaku, 104–105, 111), 10 a 12 (atmosférický tlak v ČR a na horách, 106), 13 (jako 103), 16 a 19 (vztlak bublin, 108), 17, 25, 26, 28 (vztlak nezávisí na materiálu a tvaru, 102 a 110), 18 a 20 (stlačitelné těleso, princip 108), 34, 52, 53 (výtok, 122), 36, 43, 44 (Bernoulliho rovnice, 115 a 117), 37 a 39 (členy Bernoulliho rovnice, 117), 42, 45–47, 49–50, 55 (rovnice spojitosti, 116 a 120), 57, 58, 60, 61, 63, 64 (Hookův zákon, 123–125).
- Rozporný klíč: 31 (hustoměr; klíč „c“ = Bernoulliho rovnice, správně Archimedův zákon), nepoužito.
- Chemie úlohy 1–48: ostatní úlohy jsou výpočty stejného typu jako zařazené (hmotnostní zlomek, ředění, látková koncentrace, přepočet z hustoty, neutralizace). Úlohy 49–126 kapitoly Roztoky čekají na další dávku.
- Genetika úlohy 1–36: 1 a 33 (posunová mutace, UK 141), 2 a 12 (9 : 3 : 3 : 1, ČB 118), 4 a 28 (chromatidy v meióze II, LF MU 78), 5 (transdukce, UK 88), 8, 9, 11, 16, 19 (základní pojmy, UK 149 a ČB 407, 597), 13 (genové mutace, jako 21), 15 (AB0, ČB 114), 17 (plazmidy, UK 143), 20 a 34–35 (gamety a typy potomků dihybrida, ČB 206), 22 (trisomie 21, BIO 837), 25 (crossing-over, UK 86), 27 (pojmy hybridů), 30 (Hardyho–Weinbergův vztah, UK 149), 32 (antikodon, UK 93), 36 a 37 (vázaná dědičnost, SOM 38 a 42). Úlohy 37–69 čekají na další dávku.

Dosud nepokryté oddíly: zbylé úlohy prvních kapitol fyziky (jednotky, kinematika) a chemie (vzorce, stavba atomu) mimo seznam výše, fyzika od kapitoly Kmity a akustika (str. 25+), chemie Roztoky 49–126 a dále, biologie Genetika 37–69, Biologie člověka a další.

## Čtvrtá dávka ID 151–200 (v2.50.0)

Soubor `muni-151-200.json`, generátor `create_muni_151_200.py` (sdílený `batch_tools.py`). Odpovědi ověřeny výpočtem nebo výkladem a porovnány s klíčem na str. 60, 120 a 154.

| Předmět | Kapitola (tištěné strany) | Použité úlohy | ID |
|---|---|---|---|
| Fyzika | Kmity a akustika (25–29) | 1, 2, 4, 9, 10, 11, 12, 13, 14, 16, 21, 22, 23, 25, 29, 31, 32, 33, 35, 38, 41, 42, 43, 45, 47, 48 | 151–176 |
| Chemie | Roztoky, elektrolyty, pH (77–81) | 53, 54, 55, 56, 62, 65, 69, 72, 94, 96, 104, 107 | 177–188 |
| Biologie | Genetika (135–137) | 38, 43, 46, 50, 52, 53, 54, 56, 57, 61, 62, 64 | 189–200 |

Klíč E převeden na explicitní správnou odpověď: fyzika 11 (ω = 2πf), 21 (ultrazvuk má vyšší frekvenci), 43 (souhlásky jsou hluky a šumy).

Kapitola Kmity a akustika (úlohy 1–48) je posouzená celá. Nepřidané úlohy:
- Varianta téhož poznatku: 3, 5–8 (energie a rychlost v krajní a rovnovážné poloze, 151–153), 15, 17–20 (změna fáze, 155 a 160), 24, 26–28, 30 (šíření zvuku, 163, 165–166; 27 a 28 také BIO 631–632), 34 a 36 (výpočet hladiny intenzity, 167 a 169), 37 (postupné vlnění, 170), 39 (jednotka intenzity, 162), 40 a 44 (podélné vlnění v plynech, 163), 46 (30 dB = ×1000, princip 167).
- Chemie: 49–52 a 57–61, 63, 64, 66–68, 70, 71, 73, 74 jsou výpočty nebo třídění stejného typu jako zařazené úlohy (neutralizace, silné a slabé elektrolyty, koncentrace iontů ze vzorce soli; elektrolyty také UK 155–156). 78 a 80 (konjugovaný pár, amfolyt) jsou ve sbírce UK 33–34, 95 (iontový součin vody) je UK 74. 89–93 (silné a slabé kyseliny a báze, princip 94 a UK 155), 97–103, 105, 106, 108, 109 (výpočty pH a ředění, princip 96, 104, 107).
- Genetika úlohy 37–69: 37 (daltonismus, SOM 42 a 45), 39 a 40 (transkripce a replikace, UK 97–98 a ČB 120), 41 (92 chromatid, ČB 122), 42, 44, 51, 59 (základní pojmy dominance, XY, gen a alela, BIO 703 a ČB 407), 45 (pojmy transdukce a transformace, UK 88 a LF MU 146), 47 a 58 (dihybridní poměry, ČB 118 a 189 této dávky), 48, 49, 63 (Hardyho–Weinbergův zákon a panmixie, UK 149, 185, 192), 55 (64 kodonů, UK 91), 60 a 69 (heterozygot × recesivní homozygot 1 : 1, UK 186), 65 (AB0 monogenně, UK 199), 66 (rodokmen je jen obrázek, v textové kopii nečitelný), 67 (genotypy v nabídce poškozené OCR), 68 (kodominance AB, LF MU 143). Genetika je tím posouzená celá.

Dosud nepokryté oddíly: zbylé úlohy prvních kapitol fyziky (jednotky, kinematika) a chemie (vzorce, stavba atomu) mimo seznamy výše, fyzika od kapitoly Termodynamika (str. 30+), chemie Roztoky 75–88 a 110–126 a další kapitoly, biologie od oddílu Biologie člověka (str. 138+).

## Pátá dávka ID 201–250 (v2.52.0)

Soubor `muni-201-250.json`, generátor `create_muni_201_250.py`. Odpovědi ověřeny výpočtem nebo výkladem a porovnány s klíčem na str. 60, 120 a 154.

| Předmět | Kapitola (tištěné strany) | Použité úlohy | ID |
|---|---|---|---|
| Fyzika | Termodynamika, fázové změny (30–35) | 1, 3, 8, 11, 12, 14, 17, 20, 21, 22, 23, 27, 30, 31, 32, 42, 43, 45, 47, 52, 55, 58, 60, 63, 65, 66 | 201–226 |
| Chemie | Roztoky, pH a hydrolýza (79–82) | 75, 82, 84, 110, 111, 114, 118, 120, 122, 123, 124, 126 | 227–238 |
| Biologie | Biologie člověka (139–147) | 12, 20, 31, 34, 39, 48, 50, 77, 80, 85, 96, 99 | 239–250 |

Klíč E převeden na explicitní správnou odpověď: chemie 82 (konjugovaná kyselina acetátu je CH₃COOH).

Termodynamika úlohy 1–70: nepřidáno
- Varianty téže znalosti: 2, 4–7, 48 (jednotky R, nRT, kT, pV, c·m·Δt; princip 202), 9, 33, 37, 40 (adiabatický a izobarický děj, 206 a 210), 13, 15, 16, 19, 24–26, 28, 34, 36 (stavová rovnice a zákony dějů, 204–205, 211), 18 (stavové veličiny, 214), 29 (hustota plynů, princip 226), 35 a 38 (stavová rovnice, 208), 39 (tepelná rovnováha), 44, 64 (kinetická teorie, 218–219), 46 (plynový teploměr), 49–51 (obecné a technické souvislosti), 53, 54 (sublimace, 220), 56, 57 (tání pod tlakem, princip 222), 59 a 61 (rozpuštěné látky a bod tuhnutí či varu, 222–223), 62 (vzdálenost atomů), 67, 68 (počet molekul, 225), 69 a 70 (objem a tlak po reakci H₂ s O₂).
- Sporný klíč: 10 (práce úměrná tlaku, ve skutečnosti W = p·ΔV), 41 (volná expanze ideálního plynu teplotu nemění, klíč „vždy snižuje“), 49 (klíč chybí).
- Povrchové jevy (úlohy 71–81) čekají na další dávku.

Chemie Roztoky je tím posouzená celá (1–126). Nepřidáno: 76 (koncentrace Na⁺ z pH, varianta 227), 77, 79–81, 83, 85–88 (Brönstedovy páry a amfolyty, varianty 228–229 a UK 33–34), 112, 113, 115–117, 119 (hydrolýza solí, varianta 232 a UK 170–172; 115 a 117 klíč „žádná“), 121 (klíč „žádná“, princip 237), 125 (zrcadlová k 236).

Biologie člověka úlohy 1–100: většina je stejný poznatek jako otázky biologické sady (BIO) a somatologie (SOM): kostra, svaly, oběh, krev, trávení, ledviny, smysly, nervy a hormony (např. 1–11, 13–19, 22–30, 32, 33, 35–38, 40–44, 46, 49, 51, 52, 54, 55, 57, 59–68, 71, 75, 81, 86, 87, 98, 100). Sporné nebo nečitelné: 21 (klíč glukóza, přímým zdrojem je ATP), 38 (pořadí fází srdečního cyklu podle klíče sporné), 70, 79 (exponent v OCR nečitelný), 74 (klíč sporný), 89 (zadání v OCR poškozené), 95 (nabídka neúplná). Kandidáti na další dávku: 45, 47, 53, 56, 58, 69, 72, 73, 76, 78, 82–84, 88, 90–94, 97.

Dosud nepokryté oddíly: fyzika Povrchové jevy (str. 35+), Elektřina a magnetismus, Optika, Atomová a jaderná fyzika, zbylé úlohy prvních kapitol; chemie od kapitoly Periodický systém prvků (str. 83+) a zbylé úlohy prvních kapitol; biologie kandidáti výše, Životní funkce, Evoluce, Ekologie.

## Šestá dávka ID 251–300 (v2.54.0)

Soubor `muni-251-300.json`, generátor `create_muni_251_300.py`. Odpovědi ověřeny výpočtem nebo výkladem a porovnány s klíčem na str. 60, 120 a 154.

| Předmět | Kapitola (tištěné strany) | Použité úlohy | ID |
|---|---|---|---|
| Fyzika | Povrchové jevy (36–37) | 72, 73, 75, 76, 77, 78, 79, 80 | 251–258 |
| Fyzika | Elektřina a magnetismus (37–40) | 1, 3, 4, 7, 10, 14, 15, 16, 19, 22, 25, 27, 28, 29, 32, 33, 34, 35 | 259–276 |
| Chemie | Periodický systém, vlastnosti prvků, redoxní děje (83–87) | 9, 12, 17, 24, 27, 30, 32, 34, 49, 51, 54, 56 | 277–288 |
| Biologie | Biologie člověka (142–147) | 45, 52, 53, 58, 69, 73, 76, 91, 92 | 289–297 |
| Biologie | Životní funkce, medicínsky významné organismy (148–149) | 5, 9, 19 | 298–300 |

Klíč E převeden na explicitní správnou odpověď: fyzika elektřina 35 (dva paralelně a třetí sériově). Elektřina 25 převzata s µA a µF (v OCR „pA“ a „pF“); výsledek t = CU/I na předponě nezávisí.

Termodynamika je tím posouzená celá (1–81). Nepřidáno z povrchových jevů: 71 a 81 (tlak v bublinách a kapkách, princip 252–253), 74 (kapilární tlak, princip 258).

Elektřina úlohy 1–35: 2, 11, 12 (nepřímá úměrnost permitivitě, princip 260–261), 5 a 13 (klíč „žádná z uvedených“), 6 (εᵣ nemůže být 0,5, princip 261), 8 (vzorec síly jednotkových nábojů), 9 (Coulombův zákon, ČB 542), 17 (pole dvou nábojů, klíč „žádná“), 18 (klíč „žádná“, výsledek 33,3 nF), 20 (napětí po přiblížení desek), 21 (olej za vzduch, míra snížení podle oleje), 23 a 24 (kombinace kondenzátorů, klíč „žádná“ či „nelze rozhodnout“), 26 (klíč „závisí na polaritě“ je sporný, desky se vždy přitahují), 30 (předpona proudu v OCR nejistá), 31 (klíč „žádná“). Úlohy 36–89 čekají na další dávku.

Chemie úlohy 1–56: 1, 2, 4–8, 10, 11, 13–16 (zařazení prvků, varianty 277–278 a LF MU 75), 3 (cín, LF MU 75), 18 a 19 (kyselinotvorné oxidy, UK 104), 20–22 (amfoterní oxidy a hydroxidy, UK 76), 23 (oxid alkalického kovu s vodou), 25 (obsah CO₂ ve vzduchu, časově citlivá hodnota), 26, 36–39 (klíč „žádný výrok není nesprávný“; u 36 je sporný, Na⁺ je menší než K⁺), 28 (sádra, UK 80), 29 (redukce O₂ v mitochondriích, LF MU 96), 31 (výsledek bez jednotek), 33 (varianta 283), 35 (CO a hemoglobin, BIO 249), 40–47 (pojmy oxidace a redukce, UK 201–210), 48 (klíč „žádná“), 50 (vodíkový ion se redukuje, UK 201), 52, 53, 55 (výběr redoxní reakce, princip 287). Úlohy 57 a dál čekají na další dávku.

Biologie člověka je tím posouzená celá (1–100). Z kandidátů minulé dávky nepřidáno: 47 (minutový objem, LF MU 240), 56 (počet leukocytů, ve vysvětlení LF MU 239), 72 (uložení štítné žlázy, BIO 561), 78 (spála, LF MU 246), 82 (endokrinní žlázy, BIO 536), 83 (trojcípá chlopeň, BIO 140), 84 a 88 (klíč „žádná“), 90 (chrup, LF MU 242), 93 (žluté tělísko, BIO 738), 94 (kost klínová, ČB 86), 97 (lymfocyty jako agranulocyty, ČB 636). Životní funkce úlohy 1–25: zbytek čeká na další dávku.

## Sedmá dávka ID 301–350 (v2.56.0)

Soubor `muni-301-350.json`, generátor `create_muni_301_350.py`. Odpovědi ověřeny výpočtem nebo výkladem a porovnány s klíčem na str. 60 a 120.

| Předmět | Kapitola (tištěné strany) | Použité úlohy | ID |
|---|---|---|---|
| Fyzika | Elektřina a magnetismus, elektronika (40–45) | 36, 38, 39, 40, 41, 42, 44, 46, 48, 49, 50, 51, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87 | 301–340 |
| Chemie | Periodický systém, rovnováhy a disperzní soustavy (87–89) | 57, 58, 60, 61, 63, 64, 65, 66, 69, 72 | 341–350 |

Klíč E převeden na explicitní správnou odpověď: elektřina 36 (otázka obrácena na konkrétní zapojení 200 Ω, všechny čtyři hodnoty lze sestavit), 38 (13,5 MJ), 51 (5 ms), 63 (1,8 · 10⁻⁶ N), 65 (pohyb beze změny), 81 (kruhový pohyb). Chemie 61 (hledá nesprávné tvrzení) převedena na otázku, jak se mění K při zředění.

Elektřina je tím posouzená celá (1–89). Nepřidáno z úloh 36–89: 37 (I = Q/t, LF MU 273 a 305), 43 (kov při rostoucí teplotě, varianta 304), 45 (bor v křemíku, varianta 307, pro případnou další dávku), 47 (jednotka F, ve vysvětlení 309), 52 (vzorec kapacitance, LF MU 11, pro případnou další dávku), 62 (permeabilita oceli, číselný údaj se liší podle druhu), 70–74 (vzorce impedancí, OCR vzorců nečitelné), 76 (varianta 329), 88 (obrazovka, zastaralá technika), 89 (elektrické hudební nástroje, dlouhé víceúrovňové zadání).

Chemie úlohy 57–72: 59 (varianta 342), 62 (varianta 343), 67 (složení zubní pasty, specifické), 68 (suspenze fosforečnanu, varianta 349), 70 (olej a voda se rozdělí na dvě fáze, triviální), 71 (CaSO₄ je málo rozpustný, ne zcela nerozpustný; sporné). Periodický systém je tím posouzený celý (1–72).

## Osmá dávka ID 351–400 (v2.58.0)

Soubor `muni-351-400.json`, generátor `create_muni_351_400.py`. Odpovědi ověřeny výpočtem nebo výkladem a porovnány s klíčem na str. 60 a 154.

| Předmět | Kapitola (tištěné strany) | Použité úlohy | ID |
|---|---|---|---|
| Fyzika | Optika: geometrická optika, mikroskop, vlnová optika (46–51) | 2, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 23, 24, 25, 27, 28, 30, 31, 35, 36, 37, 38, 39, 40, 45, 46, 47, 49, 52, 53, 54, 55, 56, 57 | 351–390 |
| Biologie | Životní funkce, medicínsky významné organismy (147–149) | 1, 3, 6, 7, 8, 11, 12, 16, 20, 21 | 391–400 |

Klíč E převeden na explicitní správnou odpověď: optika 10 (+4 D), 15 (paprsky vystupují rovnoběžně), 18 (+0,1 D), 19 (−2 D), 31 (předmět v 1,5f). Optika 3 doplněna o podmínku, že se světlo lomí do druhého prostředí. Optika 14 doplněna o neskutečný přímý obraz (lupa), na kterém klíč 0,0875 m závisí. Optika 25 převedena na mohutnost větší než 2 D, což je přesnější než klíčové „větší než 1 D“.

Nepřidáno z optiky 1–57: 1 (klíč „žádná“, princip 351), 4 (lom do rohovky, varianta 351), 8 (vláknová optika, varianta 355), 16 (varianta 363), 22 (rozptylka ve vodě, varianta 367), 26 (klíč c odporuje 25, sporné), 29 (2f, varianta 373), 32 a 33 (záměrně chybné zadání), 34 (symbol d, ve vysvětlení 375), 41 (varianta 377–378), 42–44 (oční vady a akomodace, BIO 671–684), 48 (nejdelší vlnová délka, CB 306), 50 a 51 (varianty 384). Úlohy 58–74 (interference, polarizace, fotometrie) čekají na další dávku.

Z životních funkcí nepřidáno: 2 (žebříčková nervová soustava, SOM 66), 4 (amnion, BIO 758 a UK 399), 13 (bezjaderné erytrocyty, BIO 84), 17 (odkysličená krev v plicnici, CB 38), 22 (vzdušnice, SOM 239), 23 (klíšťová encefalitida, BIO 530). Úlohy 10, 14, 15, 18, 24, 25 čekají na další dávku.

## Devátá dávka ID 401–450 (v2.60.0)

Soubor `muni-401-450.json`, generátor `create_muni_401_450.py`. Odpovědi ověřeny výpočtem nebo výkladem a porovnány s klíčem na str. 60 a 120.

| Předmět | Kapitola (tištěné strany) | Použité úlohy | ID |
|---|---|---|---|
| Fyzika | Optika: interference, polarizace, fotometrie (51–52) | 61, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74 | 401–413 |
| Fyzika | Elementární částice, radioaktivita (53–55) | 1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 14, 15, 17, 19, 20, 21, 22, 25 | 414–431 |
| Chemie | Organická chemie: názvosloví a izomerie (90–93) | 9, 14, 16, 18, 19, 20, 21, 22, 25, 27, 28, 29, 30, 31, 33, 36, 38, 45, 46 | 432–450 |

Klíč E převeden na explicitní správnou odpověď: chemie 29 (3 izomery tetrachlorbenzenu), 30 (jediný pentachlorbenzen). Fyzika částic 6 (klíč „elektron“, ale fermion je i neutron) převedena na otázku, která částice fermion není (foton). Chemie 20 má v OCR vzorec C₄H₈ nečitelný, klíč 5 izomerů odpovídá C₄H₈. Chemie 38 doplněna o vlastní distraktory (původní možnosti jsou v OCR neúplné).

Optika je tím posouzená celá (1–74). Nepřidáno z úloh 58–74: 58 (Newtonovy kroužky, LF MU 382), 59 (barevné skvrny ropy, LF MU 390), 60 (chvění vzduchu, LF MU 381), 63 (hologram, LF MU 387).

Elementární částice 1–25: 4 (klíč „žádná“, varianta 416), 10 (varianta 420), 13 (klíč „žádná“, srovnání vlnových délek s neurčenou hybností), 16 (klíč „žádná“, varianta 427), 18 (gama a rentgen, UK 68), 23 (počet neutronů, LF MU 69), 24 (OCR rovnice reakce neúplné). Úlohy 26–71 čekají na další dávku; klíč k nim v textové kopii chybí (stránka klíče je přerušená), proto se budou ověřovat výpočtem a výkladem.

Organická chemie úlohy 1–46: 1–5, 13, 15, 17, 48, 49 (vzorce jen jako obrázek), 6 (název dvojvazného zbytku, „ethylen“ i „dimethylen“ se používají), 7, 8, 10–12 (vinyl, fenyl, benzyl, UK 306, 325–326), 23 (klíč „žádná“, všechny možnosti jsou izomery), 24 (název 3-methylbut-2-en je chybný), 26 (klíč „žádná“), 32 (ether a alkohol, UK 282), 34, 35, 37 (varianty 446–447), 39 a 42 (tautomerie vinylalkoholu a cis-trans izomerie, UK 276 a 424). Úlohy 40, 41, 43, 44, 47 a dál čekají na další dávku.

## Dávka 451–500 (verze 2.62.0)

Fyzika, Elementární částice, jaderná a kvantová fyzika (str. 55–58), ID 451–475: úlohy 26, 27, 29, 30, 31, 34, 35, 37, 38, 40, 42, 44, 45, 46, 49, 50, 51, 52, 53, 55, 57, 58, 60, 61, 68. Klíč k úlohám 26–71 v publikaci chybí, odpovědi jsou ověřené výpočtem a výkladem (alfa A − 4, β⁻ Z + 1, poločasy, vazebná energie na nukleon, rentgenové a fotoelektrické jevy). Úloha 31 je přeformulovaná na „teoreticky nikdy“.

Biologie, ID 476–500:
- Životní funkce (str. 149–150): 14, 15, 18, 24, 25 (25 s klíčem „není správné“: borelióza je bakteriální).
- Evoluční biologie (str. 150–151): 4, 7, 8, 9, 11, 12. Vynecháno: 1 (3,5 mld. let, SOM 3), 2 (sapientace, pokrývá úloha 8), 3 a 5 (Darwin, přírodní výběr a vznik druhů, ČB 131), 6 (klíč „žádná“, stejná znalost jako Ekologie 15), 10 (zařazení neandertálce je sporné, Homo sapiens neanderthalensis i samostatný druh H. neanderthalensis).
- Ekologie (str. 151–153): 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17. Vynecháno: 3 (sporný klíč c „soubor populací“, odporuje úloze 14c, podle níž je biom celek ekosystémů se společnými znaky), 6 (zoocenóza, pojem vysvětlen v úloze 2), 11 (priony jsou bílkoviny, ne RNA, BIO 535).

## Dávka 501–550 (verze 2.64.0)

Fyzika, Elementární částice, jaderná a kvantová fyzika (str. 56–58), ID 501–507: úlohy 39, 41, 47, 59, 69, 70, 71 (39, 41 a 59 s klíčem „žádná“ přeformulovány na správnou odpověď). Vyřazeny zbylé úlohy oddílu: 28 a 32 (v textu chybí), 33 (vzorec zákona, pokrývá 460), 36 (vazebná energie na nukleon, pokrývá 458), 43 (Bq, MUNI 464), 48 (rentgenové záření má rozsah 1 pm až 10 nm, dvě možnosti správné), 54, 63, 64, 67 (zadání poškozené), 56 (brzdné záření, 466 a 470), 62 a 65 (Compton a fotoefekt, 474 a 504), 66 (sporné, rozptyl měkkého RTG záření nedá UV). Oddíl je tím uzavřen.

Chemie, ID 508–550:
- Organická chemie: názvosloví a izomerie (str. 92): 40, 43.
- Organická chemie: reakce a deriváty (str. 93–98): 50, 53, 54, 55, 56, 57, 58, 61, 62, 65, 66, 69, 70, 72, 73, 74, 76, 78, 80, 81, 82, 83, 85, 88, 89, 90, 93, 94, 99, 100, 103, 105, 106, 109, 112, 113, 114, 115, 116, 117, 118. Úlohy 56, 78, 90 a 117 s klíčem „žádná“ mají doplněnou správnou odpověď (ethylbenzen, hydrogenace, butan-1-ol, akrylová kyselina).

Vynecháno z úloh 39–118: 39, 41 (tautomerie, UK 276 a 508), 42 (UK 424), 44 (varianta 509), 47 (varianta 450), 48, 49, 71 (vzorec jen jako obrázek), 51, 52 (elektrofil, UK 271), 59, 60 (naftalen a anthracen, varianty 516), 63 (klíč „žádná“, všechna činidla reagují), 64 (varianta 526), 67 (UK 332), 68 (chloroform, UK 317), 75 (naftol, UK 372), 77, 92 (benzaldehyd a benzylalkohol, UK 379 a 402), 79 (UK 367), 84 (UK 404), 86, 87 (chinony, UK 373), 91 (varianta 532), 95 (UK 361), 96 (UK 370), 97 (redukce ketonu, UK 404), 98 (acetaly, UK 365), 101 (UK 452), 102, 110, 111 (třídění aminů, 538–539), 104 (UK 272), 107 (UK 453), 108 (varianta 541).

## Dávka 551–600 (verze 2.66.0)

Chemie, ID 551–600:
- Organická chemie: reakce a deriváty (str. 98–103), ID 551–577: 123, 127, 128, 130, 132, 133, 135, 137, 140, 143, 145, 149, 154, 155, 156, 157, 166, 168, 169, 172, 174, 175, 177, 179, 183, 184, 185. Úloha 169 s klíčem „žádná“ má doplněnou správnou trojici (aldimin, disulfid, acetal). Organická chemie je tím uzavřena.
- Sacharidy, lipidy a další biomolekuly (str. 104–107), ID 578–600: 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 16, 18, 20, 23, 24, 25, 28, 32, 34, 35, 40, 43.

Vynecháno z organické chemie 119–185: 119 (benzoyl, UK 327), 120 (UK 409), 121, 122, 129, 134 (klíč „žádná“ nebo více správných možností; trikarboxylová citronová kyselina UK 410), 124–126, 139, 147, 148, 151–153, 160–163, 167, 170, 171, 173, 176, 178, 181 (vzorce nebo schémata jen jako obrázek), 131, 136 (mléčná a pyrohroznová kyselina, UK 421), 138 (močovina, UK 457), 141 (kyselina jablečná, UK 422), 142 (nitrily, UK 454), 144, 146 (pyran, UK 467), 150, 158 (počet dusíků v pyrimidinu a purinu, UK 474 a 478), 159 (thiazol, UK 462), 164 (porfin, UK 42), 165 (pyridin v nikotinu, UK 471), 180 (klíč „žádná“, chinony a difenoly UK 373), 182 (varianta 527).

Vynecháno z úloh 1–44 o sacharidech a lipidech: 8 (varianta 582), 13–15 (vzorce jen jako obrázek), 17, 19 (glykosidová vazba, UK 506), 21, 22 (laktóza a sacharóza, BIO 286–287), 26 (varianta 593–594), 27, 29, 39 (klíč „žádná“), 30, 31, 33 (palmitová, olejová a linolová kyselina, UK 518–521), 36–38, 41, 42 (mýdla a ztužování, UK 524–529), 44 (žluknutí, UK 528).

## Dávka 601–650 (verze 2.68.0)

Chemie, oddíl Sacharidy, lipidy, aminokyseliny, nukleové kyseliny, enzymy, metabolismus (str. 107–116), ID 601–650: úlohy 46, 50, 52, 53, 58, 59, 62, 63, 64, 65, 67, 68, 69, 71, 74, 76, 77, 82, 83, 86, 87, 91, 92, 98, 99, 100, 105, 106, 108, 109, 110, 111, 114, 116, 118, 119, 120, 122, 124, 125, 127, 130, 132, 136, 137, 139, 140, 142, 143, 145. Úlohy 64, 87, 105 a 106 s klíčem „žádná“ mají doplněnou správnou odpověď (transkripce DNA → RNA, guanidinová skupina argininu, amyláza jako hydroláza vazeb α(1→4), lipáza).

Vynecháno z úloh 45–145: 45 (žluknutí, UK 528), 47–49 (purinové a pyrimidinové báze, UK 475–476), 51 (UK 629), 54, 57, 61 (glykosidová vazba, varianty 603), 55 (klíč „žádná“), 56 (varianta 604), 60 (varianta 605), 66 (antikodon, UK 93), 70, 72, 73, 75 (serin, valin, leucin, asparagová kyselina, UK 565–579), 78–81, 89, 90 (vzorce jen jako obrázek nebo varianta 617), 84, 85 (UK 561, 571–572), 88 (izoelektrický bod, UK 563), 93 (varianta 623), 94 (cystein a disulfidy, UK 568), 95 (klíč „žádná“), 96 (UK 608), 97 (sporný klíč, disulfidové můstky spojují podjednotky například u inzulinu a protilátek), 101, 104 (hydrolázy, UK 620), 102, 103 (pepsin a trypsin, BIO 274), 107 (laktát, LF MU 243), 112, 113 (β-oxidace, UK 624), 115, 117, 121 (varianty 633 a 636), 123 (varianta 638), 126 (močovina, BIO 299), 128 (varianta 641), 129 (varianta 619), 131 (adrenalin, UK 546), 133 (prolaktin, SOM 414), 134 (křivice, BIO 895), 135 (hořčík v chlorofylu, UK 27), 138, 141, 144 (klíč „žádná“).

Dosud nepokryté oddíly: chemie úlohy 146–171 posledního oddílu a zbylé úlohy prvních kapitol; biologie Životní funkce 10; zbylé úlohy prvních kapitol fyziky.

## Dávka 651–700 (verze 2.70.0)

Soubor `muni-651-700.json`, generátor `create_muni_651_700.py`. Odpovědi ověřeny výpočtem nebo výkladem a porovnány s klíčem na str. 120.

- Chemie, Enzymy, metabolismus a biomolekuly (str. 116–119), ID 651–666: úlohy 146, 148, 150, 151, 153, 154, 155, 157, 158, 159, 163, 164, 165, 167, 168, 170. Úlohy 150 a 151 s klíčem „žádná“ mají doplněnou správnou odpověď (glyceraldehyd-3-fosfátdehydrogenáza; vitamin C si člověk nesyntetizuje). V 164 nahrazeny distraktory s nejednoznačnou „dehydrogenací alaninu“ a „hydroxylací glycinu“.
- Chemie, Vzorce a výpočty (str. 62–67), ID 667–694: úlohy 14, 20, 22, 23, 26, 27 (názvosloví) a 32, 34, 35, 39, 42, 43, 44, 45, 47, 48, 52, 57, 60, 61, 62, 63, 66, 67, 69, 70, 71, 75 (výpočty). Úlohy 14, 45 a 75 s klíčem „žádná“ mají doplněnou správnou odpověď.
- Chemie, Stavba atomu (str. 67–69), ID 695–700: úlohy 3, 6, 11, 13, 19, 33.

Vynecháno z biochemie 146–171: 147 (transaminace aspartátu, varianta 652), 149 (malát → oxalacetát, LF MU 557), 152 (dikation argininu, varianta LF MU 650), 156 (vitamin K, UK 555 a LF MU 644, klíč „žádná“), 160 (transaminace, varianta 652), 161 (substrátová fosforylace z fosfoenolpyruvátu, LF MU 647), 162 (glyceraldehyd-3-fosfátdehydrogenáza, varianta 653), 166 (FADH₂, LF MU 646), 169 (provitamin A, UK 551), 171 (ligáza, varianta 655). Biochemie (1–171) je tím posouzená celá.

Vynecháno ze Vzorců 1–75: 17 (chlorečnan, LF MU 22), 18 (Mn₂(PO₃)₆ je metafosforečnan, nabídnuté názvy nejsou jednoznačné), 19 a 25 (manganan, LF MU 20), 21 (fosforečnan, LF MU 24), 24 (dichroman, LF MU 28), 30, 31, 33 (hmotnostní zlomek prvku, varianty 673 a LF MU 33–34), 36–38 (hmotnost prvku ve sloučenině, varianty 676), 40, 41 (obrácený výpočet, varianty 677), 46 (Avogadrova konstanta, UK 226), 49 (varianta 682), 50, 51 (počet atomů z látkového množství, varianty 683, klíč „žádná“), 53 (atomy vodíku ve vodě, UK 228), 54, 55 (varianty 679 a 683), 56, 58, 59 (hmotnost plynu z objemu, varianty 684), 64, 74 (spalování ethynu, varianty 688), 65 (spalování propanu, UK 219), 68 (výtěžek, varianta 690), 72, 73 (elektrolýza vody, varianty 693). Kapitola Vzorce (1–75) je tím posouzená celá.

Biologie Životní funkce 10 (trypanozoma a moucha tse-tse) vyřazena jako varianta LF MU 399.

Dosud nepokryté oddíly: chemie Stavba atomu a chemická vazba, fyzika Jednotky a Kinematika a dynamika, biologie Historie a Biologie buňky (zbylé úlohy mimo použité).

## Dávka 701–750 (verze 2.72.0)

Soubor `muni-701-750.json`, generátor `create_muni_701_750.py`. Odpovědi ověřeny výpočtem nebo výkladem a porovnány s klíčem na str. 60, 120 a 154.

- Fyzika, Jednotky (str. 8–10), ID 701–710: úlohy 18, 37, 45, 46, 47, 48, 50, 52, 53, 56. Úloha 37 s klíčem „žádná“ má doplněnou jednotku N·m.
- Fyzika, Kinematika a dynamika, práce, otáčivý pohyb, gravitace (str. 11–18), ID 711–732: úlohy 7, 13, 15, 16, 25, 30; práce 31, 32, 33, 38, 42, 44, 46; otáčivý pohyb 44, 46, 47, 49; kombinované 54, 55, 56, 57; gravitace 61. Úloha 49 s klíčem „žádná“ má doplněnou hodnotu 0,500 J.
- Chemie, Stavba atomu a chemická vazba (str. 69–72), ID 733–745: úlohy 35, 37, 42, 53, 54, 55, 57, 63, 64, 65, 68, 71, 73. V 71 a 73 nahrazeny distraktory, které by mohly vodíkové vazby tvořit slabě.
- Biologie, Obecná biologie a Biologie buňky (str. 122–126), ID 746–750: úlohy 7; 15, 19, 31, 34.

Vynecháno z Jednotek 1–63: 12, 25 (zrychlení, ČB 537), 13 (povrchové napětí, LF MU 10), 21 (klíč „žádná“, varianta LF MU 7), 31–36 (vyjádření jednotek, klíč „žádná“ nebo v OCR nečitelné exponenty; koncentrace a náboj LF MU 14–15), 39 (intenzita zvuku, LF MU 162), 43 (klíč „žádná“), 49 (předpony v OCR nečitelné), 51 (varianta 707), 54, 55 (varianty 709), 57, 60, 61, 63 (vektory, varianty 710), 58, 59, 62 (skaláry, ČB 534). Jednotky (1–63) jsou tím posouzené celé.

Vynecháno z Kinematiky a dynamiky 1–64: 9–11 (impuls síly, varianty LF MU 56), 17, 19, 21, 22 (volný pád a svislý vrh, varianty LF MU 58–59), 23, 24 (pohyb stálou rychlostí, LF MU 57), 26 (varianta 715), 28, 29 (houpačka, LF MU 60), 34 (varianta 717), 35 (LF MU 62), 40 (varianta 718), 41 (klíč „žádná“, varianta 717), práce 45 (LF MU 61), otáčivý pohyb 45 (varianta 724), 48, 50, 52, 53 (dostředivá síla, varianty 725; 50 klíč „žádná“), 59 (LF MU 66), 60 (varianta 723), 62 (sporné, viz dávka 51–100), 63 (zachování energie, LF MU 61). Mechanika (1–64) je tím posouzená celá.

Vynecháno ze Stavby atomu a chemické vazby 1–74 (kromě dříve uvedených 4, 9, 10, 24, 28, 66): 7 (varianta 696), 12, 15, 16, 17 (konfigurace, varianty 697–698 a LF MU 72), 20, 21, 23, 25 (valenční elektrony, LF MU 74 a ČB 529), 27, 29 (p-prvky, LF MU 75), 32 (LF MU 77), 34, 36, 38, 39, 40 (trendy v periodické soustavě, varianty 733–734 a LF MU 76), 43–46, 49, 69 (iontové a kovalentní sloučeniny, varianty 735), 47 (vaznost, UK 70), 51 (varianta LF MU 80), 56 (varianta 738), 59 (dipólový moment, LF MU 83), 61 (polární vazba, UK 29), 67 (varianta 742), 70 (dipól má i hydrazin, nejednoznačné), 72 (varianta 744), 74 (thiol tvoří s vodou jen slabé vodíkové vazby, nejednoznačné). Kapitola (1–74) je tím posouzená celá.

Vynecháno z Obecné biologie 1–11: 1 a 9 (jádro jako rozdíl prokaryot a eukaryot, SOM 14), 4 (viry se množí jen v buňce, SOM 12), 8 (HIV, BIO 828). Kapitola je tím posouzená celá.

Dosud nepokrytá zůstává jen Biologie buňky (zbylé úlohy 1–88).

## Závěrečná dávka 751–769 (verze 2.73.0)

Soubor `muni-751-769.json`, generátor `create_muni_751_769.py`. Odpovědi porovnány s klíčem na str. 154.

- Biologie, Biologie buňky (str. 127–131), ID 751–769: úlohy 42, 43, 44, 50, 51, 53, 57, 64, 67, 68, 69, 74, 79, 81, 82, 83, 84, 85, 88. Úloha 79 s klíčem „žádná“ má doplněnou trojici jádro, mitochondrie a chloroplasty.

Vynecháno z Biologie buňky 1–88 (kromě dříve uvedených 21 a 62): 2, 41, 61 (triviální výroky), 4 (vzruch, BIO 424), 9 (DNA-polymeráza, UK 97), 16, 20, 24, 28, 33 (transkripce a translace, LF MU 609–611), 17, 18 (komplementarita bází, LF MU 89 a UK 93), 22 (bakteriofág, varianta 746), 25 (varianta 748), 36 (cytokineze, ČB 300), 37, 38, 45, 65 (semiautonomní organely, LF MU 42 a UK 41), 39 (fagocytóza, BIO 91), 46 (stavba membrány, SOM 16), 47 (varianta LF MU 44), 49 (varianta 754), 54, 77 (endocytóza, varianty 756), 55 (dýchací řetězec, LF MU 96 a UK 37), 58 (izotop kyslíku, LF MU 632), 59, 60 (cytoskelet, SOM 29 a LF MU 39), 66 (viry, LF MU 87), 70 (varianta 751), 71 (metafáze, LF MU 98 a ČB 122), 72 (lyzozomy, ČB 299), 73 (Golgiho aparát, varianta 764), 80 (rozdíl prokaryot a eukaryot, SOM 14), 87 (centromera, nepřesná formulace „sesterských chromozomů“).

## Formát zkoušky a dávka ID 770–786 (v2.81.0)

Od verze 2.74.0 nabízí kvíz LF MU stejně jako skutečná zkouška pátou možnost E „Žádná odpověď není správná“. Soubor `muni-770-786.json`, generátor `create_muni_770_786.py` (funkce `build_muni_exam`): možnosti zůstávají v pořadí knihy a klíč e se ukládá jako odpověď 4. Doplněny úlohy, které starší dávky vynechaly jen kvůli klíči „žádná“.

| Předmět | Kapitola | Úlohy | ID |
|---|---|---|---|
| Fyzika | Elektřina a magnetismus (str. 38–40) | 13, 17, 18, 31 | 770–773 |
| Fyzika | Jednotky (str. 9) | 43 | 774 |
| Chemie | Periodický systém a vlastnosti prvků (str. 84–86) | 26, 37, 39 | 775–777 |
| Chemie | Organická chemie: názvosloví a izomerie (str. 91) | 26 | 778 |
| Chemie | Organická chemie: reakce a deriváty (str. 94–99) | 63, 122, 134 | 779–781 |
| Chemie | Sacharidy, lipidy a další biomolekuly (str. 106–107) | 27, 39 | 782–783 |
| Chemie | Nukleové kyseliny, Aminokyseliny a bílkoviny, Enzymy a metabolismus (str. 108–116) | 55, 95, 141 | 784–786 |

Úlohy s klíčem „žádná“, které zůstávají vynechané:
- Sporný nebo chybný klíč: Periodický systém 36 (Na⁺ je menší než K⁺, výrok d je tedy nesprávný a klíč e neplatí), 38 (hliník je nejrozšířenějším kovem jen v zemské kůře), 48 (měď má skutečně menší elektronegativitu než stříbro, z pokusu to ale vyvodit nelze), Elektřina 23 a 24 (kombinace kondenzátorů, „nelze rozhodnout“), Elementární částice 13.
- Nečitelné nebo chybějící zadání: Elektřina 5 (exponenty jednotek v OCR), Biologie člověka 88 (text v kopii chybí).
- Stejný poznatek jako jiná otázka: Biologie člověka 84 (monocyty a makrofágy, BIO 94), Organická chemie 23 (izomery C₄H₈, LF MU 438), 121 (dikarboxylové kyseliny, UK 409 a LF MU 576), 129 (hydroxykyseliny, LF MU 554), Sacharidy 29 (polysacharidy, UK 510), 138 (ligáza, LF MU 655), 144 (vitamin D, UK 636 a 987) a úlohy, u nichž mapa výše uvádí variantu (například Roztoky 115, 117 a 121, Optika 1, Elementární částice 4 a 16).

## Stav pokrytí

Všechny kapitoly publikace Mornstein, Dostál, Slaninová (2018) jsou posouzené: každá úloha je použitá, nebo je u ní v této mapě uveden důvod vyřazení (varianta, duplicita s jinou sadou, sporný nebo chybějící klíč, nečitelné OCR). Kvíz LF MU obsahuje 786 otázek, další ID by bylo 787.

Druhý soubor `877344967-LF-MU-Modelove-Otazky-New.pdf` je podle vlastníka (21. 11. 2026) stejná publikace jako hlavní soubor Mornstein a kol. Samostatně se nepokrývá; zdrojem kvízu LF MU je jen hlavní soubor.
