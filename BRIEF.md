# Studijní kvízy

- Cílový web je https://jameskaerem.github.io/kvizy-na-prijimacky/ ze zdrojového repozitáře `jameskaerem/kvizy-na-prijimacky`, větev `main`. Původní adresa https://jameskaerem.github.io/somatologie-otazky/ zůstává během migrace dostupná pro export zálohy.
- Stav k 22. 11. 2026: 630 původních otázek somatologie, 900 otázek biologie, 683 otázek České Budějovice a 250 modelových otázek LF MU (111 fyzika, 71 chemie, 68 biologie) a 300 modelových otázek 2. LF UK (34 fyzika, 167 chemie, 99 biologie; ukázka fyziky vyčerpaná). Další dávky dle [mapy LF MU](work/MUNI-POKRYTI.md) a [mapy UK](work/UK-POKRYTI.md).
- Codex navazuje na banku otázek a audity. Claude upravuje zejména design, drobné funkce nebo provádí revizi obsahu. Pravidla a kontrolní příkazy jsou v [CLAUDE.md](CLAUDE.md).
- Samostatný HTML vzniká z `work/build.py`, zdrojové šablony, stylů, JS a bank v JSON. Nasazení používá vygenerovaný `index.html`.
- Úložiště běží v prohlížeči. Záloha ve formátu JSON přenáší chyby, tipy, opakování a rozpracovaná kola všech předmětů i sekcí. Změnu domény plánuj až po zpřístupnění a vyzkoušení exportu na původním webu.
- Pět původních PDF a 38 souborů v ZIPu mají mapy pokrytí. [Biologický audit](work/COVERAGE_AUDIT.md) popisuje tematické pokrytí učebnice. [Soupis originálů](work/SOURCES.json) eviduje 13 souborů včetně modelových otázek MUNI (Mornstein, Dostál, Slaninová), které kvíz LF MU používá, a tří modelových sbírek 2. LF UK (fyzika jen jako ukázka). Druhý soubor MUNI je podle vlastníka stejná publikace, samostatně se nepokrývá.
- Originální PDF a ZIP jsou ve složce vlastníka. GitHub nese kód, vlastní otázky a evidenci pokrytí.
