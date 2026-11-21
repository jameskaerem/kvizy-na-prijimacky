# Spolupráce na studijních kvízech

Před prací si přečti [BRIEF.md](BRIEF.md) a [README.md](README.md). Veškerý text pro studenty piš česky.

## Kdo na čem pracuje

- Codex doplňuje otázky, porovnává je s existující bankou, aktualizuje mapy zdrojů a zveřejňuje ověřené dávky do 50 otázek.
- Claude může na zadání navrhovat a provádět změny designu, přístupnosti nebo drobného chování. Může také kontrolovat otázky nebo doplnit otázky, které mu vlastník výslovně zadá. Při revizi uveď předmět, ID, konkrétní problém, návrh opravy a zdroj. Změny zachyť v samostatné větvi nebo pull requestu, aby šly zkontrolovat před nasazením.

## Sestavení

- Vzhled upravuj v `work/design.css`. Větší změny struktury dělej v `work/somatologie-base-1.12.0.html` a `work/build.py`. `index.html` je výstup sestavení a nasazuje se na GitHub Pages.
- Po změně spusť `python work/build.py` a `node work/check.cjs` z kořene repozitáře. Do stejného commitu přidej zdrojové změny i vygenerovaný `index.html`.
- Design ověř na mobilní i široké obrazovce a z klávesnice. Zachovej ovládání předmětů, čitelnost výsledků, stavy správných a chybných odpovědí, užitečné popisky, fokus a ovládání zálohy.

## Smlouva pro uložený pokrok

- Zachovej klíče `somatologie-learning-v2`, `biologie-learning-v2`, `budejovice-learning-v2`, `market-quiz-subject` a `budejovice-section`, schéma v2 i migraci ze `somatologie-first10-v1`.
- ID existující otázky a pořadí jejích možností patří k historii uložených odpovědí. Novým otázkám přiděluj nová ID. Opravu správné odpovědi, změnu zařazení nebo odstranění existující otázky nejdřív posuď se správcem i z hlediska rozpracovaných kol. Změna vyžaduje cílený migrační test.
- U českobudějovických sekcí zachovej jejich identifikátory a oddělená kola. Výsledky otázky se sdílejí v rámci jednoho předmětu mezi sekcemi.
- Změny úložiště ověř na reálných uložených stavech, včetně chyb, tipů, rozpracovaných kol a exportu a importu. Pro testování používej syntetický pokrok nebo testovací profil.
- Před přechodem na novou doménu zveřejni zálohování na původní adrese. Původní adresu ponech přístupnou pro export po dobu migrace. Zálohy studenta obsahují jeho historii a patří do jeho soukromého úložiště.

## Obsah a podklady

- Otázka má čtyři různé možnosti, jednu obhajitelnou správnou odpověď, vlastní srozumitelné vysvětlení a referenci na položku nebo stránku. Duplicity kontroluj podle znalosti, kterou otázka testuje. Nové dávky ukládej do odpovídajících JSON souborů s pořadovými ID.
- Aktualizuj mapu pokrytí, když se změní přiřazení. Pochybný klíč řeš přesnou přeformulací nebo zaznamenej důvod vyřazení. Výsledek funkčního testu vypovídá o chování kvízu. Správnost otázek ověřuj vůči zdroji.
- [Soupis originálů](work/SOURCES.json) obsahuje relativní cesty, velikosti a SHA-256. Originály jsou oddělené od veřejného webu. Přístup k nim řeší vlastník podle oprávnění ke sdílení. Modelové otázky MUNI (Mornstein, Dostál, Slaninová) jsou zdrojem kvízu LF MU. Druhý soubor MUNI je evidovaný jako kandidát pro samostatné budoucí pokrytí.
