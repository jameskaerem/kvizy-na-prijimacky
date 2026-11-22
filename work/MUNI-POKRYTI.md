# LF MU — modelové testové otázky (2018)

Zdroj: `916110468-Modelove-Testove-Otazky-k-Prijimacim-Zkouskam-Na-LF-MU-fyzika-chemie-biologie-Vojtech-Mornstein-Jiri-Dostal-Iva-Slaninov.pdf`, Vojtěch Mornstein, Jiří Dostál, Iva Slaninová, ISBN 978-80-210-9045-3. Čísla stran jsou tištěná (PDF = strana + 1).

| Oddíl | Tištěné strany | Klíč | Stav |
|---|---|---|---|
| Fyzika | 7–59 | 60 | 34 otázek (jednotky; kinematika, dynamika, práce, otáčivý pohyb, gravitace), další otevřené |
| Chemie | 62–119 | 120 | 34 otázek (názvosloví, výpočty, stavba atomu, chemická vazba), další otevřené |
| Biologie | 122–153 | 154 | 32 otázek (historie, biologie buňky), další otevřené |

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

Druhý soubor `877344967-LF-MU-Modelove-Otazky-New.pdf` je podle vlastníka (21. 11. 2026) stejná publikace jako hlavní soubor Mornstein a kol. Samostatně se nepokrývá; zdrojem kvízu LF MU je jen hlavní soubor.
