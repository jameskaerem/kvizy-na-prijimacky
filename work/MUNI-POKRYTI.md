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

Druhý soubor `877344967-LF-MU-Modelove-Otazky-New.pdf` nebyl 21. 11. 2026 v připojené složce MUNI na počítači (je tam jen publikace Mornstein a kol.). Zůstává nepokrytý, dokud nebude dostupný.
