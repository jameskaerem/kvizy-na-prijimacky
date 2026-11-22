# Studijní kvízy

Verze 2.78.0 • 22. 11. 2026

Somatologie (630), Biologie (900), České Budějovice (683), Modelové testové otázky k přijímacím zkouškám na LF MU (769) a Modelové otázky 2. LF UK – Univerzita Karlova (937). Samostatný soubor HTML funguje offline. Všechny předměty mají chytré procvičování, opakování chyb a tipů a test celé sady.

## Formát odpovědí podle zkoušky

Od verze 2.74.0 odpovídá formát otázek skutečným přijímacím zkouškám. LF MU: každá otázka má pátou možnost E „Žádná odpověď není správná“ a správná je nejvýš jedna odpověď. Univerzita Karlova (2. LF UK): odpovědi se zaškrtávají, správných může být více, jedna i žádná a hodnotí se přesná shoda po kliknutí na Vyhodnotit odpověď. Ostatní předměty mají dál jednu správnou odpověď.

Nové otázky UK s více správnými odpověďmi mají v JSON pole `answers` (seřazené indexy). Otázky LF MU s klíčem „žádná“ mají `answer: 4` a `title` „Žádná odpověď není správná“. Uložený výběr u zaškrtávání je `16 + bitová maska`, takže starší uložené odpovědi (index 0–3), tipy, rozpracovaná kola i zálohy zůstávají platné bez migrace. Ověřuje to test přechodu z verze 2.73.0 v `work/check.cjs` (fixture `work/fixtures/2.73.0.html.gz`).

## Vzhled

Od verze 2.42.0 sdílí kvíz vzhled s aplikací se zápisky z hodin: každý předmět má vlastní barvu, režimy a rozbalovací panely jsou barevné karty a přepínání záložek, otázek a výsledků je plynule animované. Vpravo v hlavičce lze přepnout vzhled podle systému, světlý nebo tmavý. Volba se ukládá pod klíčem `quiz-theme` odděleně od pokroku. Při omezení pohybu v systému se animace vypínají. Styly jsou v `work/design.css`, animace a přepínač vzhledu v `work/motion.js`. Od verze 2.43.0 má kvíz vlastní ikonu pro záložku prohlížeče a plochu telefonu (`work/icon/`), vloženou přímo do HTML, takže funguje i offline. Od verze 2.45.0 mají výběry sekcí (České Budějovice, LF MU, Univerzita Karlova) vlastní rozbalovací seznam ve stylu stránky s ovládáním z klávesnice (`work/picker.js`). Původní `select` zůstává zdrojem hodnoty, takže uložené sekce se nemění.

## Záloha a přenos pokroku

Na stránce rozbal **Záloha a přenos pokroku** a zvol **Stáhnout zálohu**. Soubor JSON ulož i mimo zařízení, například na svůj soukromý cloudový disk. Na druhém zařízení otevři kvíz, zvol **Načíst zálohu** a vyber uložený soubor. Obnoví se stav ke chvíli exportu včetně chyb, tipů a rozpracovaných kol. Import po potvrzení nahradí pokrok ve všech předmětech na cílovém zařízení. Pokrok se mezi zařízeními automaticky nesynchronizuje.

Pokud se web v budoucnu přesune na jinou doménu, nejdřív stáhni zálohu na stávající adrese v prohlížeči, kde se učíš. Pak ji načti na nové adrese. Po exportu si ponech soubor i pro případ ztráty zařízení.

## Úpravy a podklady

Spusť `python work/build.py` a `node work/check.cjs` z kořene repozitáře. Stačí Python 3 a Node.js. Kvíz je v `index.html`. Vstupní soubory a pravidla pro zachování pokroku popisují [pravidla pro Claudea](CLAUDE.md) a [projektový brief](BRIEF.md).

[Soupis zdrojových souborů](work/SOURCES.json) pomůže vybrat originál pro kontrolu konkrétní otázky. Zdrojové PDF a ZIP má vlastník k dispozici odděleně.

## České Budějovice

Podrobná revize přidala osm otázek č. 613–620. [Mapa úloh ZIPu](work/BUDEJOVICE-MAPA-ZADANI-6393.md) a [mapa původních PDF](work/BUDEJOVICE-MAPA-PUVODNI-PDF.md) uvádějí přímo testovaná zadání, znalosti ve vysvětleních a důvody vyřazení. Následná revize velké sbírky 2019–2022 přidala otázky č. 621–660. [Soupis úloh této sbírky](work/BUDEJOVICE-2019-2022-ULOHY.csv) uvádí čísla úloh a stav přiřazení ke kvízu. Každé číslované zadání této sbírky má stav. Kontrola původně částečných přiřazení přidala otázky č. 661–683 z velké sbírky, dalších původních PDF a ZIPu.

V záložce České Budějovice je devět tematických kvízů a volba Všechny otázky. Každý kvíz má vlastní rozpracované kolo. Pokrok po jednotlivých otázkách je společný a staré kolo zůstává dostupné pod Všechny otázky. Z 38 příloh archivu přibylo po dvou kontrolách dvanáct dosud nepokrytých otázek. Přiřazení příloh je v [auditu archivu](work/BUDEJOVICE-ARCHIV-6393.md).

První dávka vychází ze souboru České Budějovice test 2019 oprava6.pdf. Dávka 51–100 dokončuje výběr ze všeobecné informovanosti 2019 a začíná biologii pro fyzioterapii 2020 ve sbírce České Budějovice TESTY 2019, 2021, 2022.pdf. Dávka 101–150 dokončuje výběr z biologie 2020 pro fyzioterapii a pokračuje všeobecnou informovaností téhož testového souboru. Dávka 151–200 zahrnuje závěr všeobecné informovanosti, motivační testy a další biologický test pro fyzioterapii 2020. Dávka 201–250 navazuje genetikou a oběma variantami všeobecné informovanosti pro fyzioterapii 2021. Dávka 251–300 zahrnuje ombudsmana a nové znalosti ze tří biologických testů 2021 pro fyzioterapii. Dávka 301–350 zahrnuje motivační testy 2021 pro fyzioterapii a biologii i všeobecnou informovanost 2019 pro radiologického asistenta. Dávka 351–400 zahrnuje odložené pojmy z roku 2021 a vybrané testy 2019 pro záchranáře a radiologické asistenty. Dávka 401–450 doplňuje sociologii, filozofii, dějiny a vybrané biologické pojmy ze sbírky 2019. Dávka 451–500 doplňuje anatomii a začíná ošetřovatelství, sociální práci a management z materiálu České Budějovice TESTY 2024 nové.pdf. Dávka 501–550 zahrnuje další anatomii, sociologii, informatiku, chemii a fyziku 2024. Dávka 551–600 uzavírá výběr ze všech pěti dodaných PDF včetně použitelných závěrečných poznámek. Duplicity nebyly přidávány opakovaně; chybné, nejednoznačné a neověřené časově citlivé položky jsou vyřazeny. Závěrečný audit je v work/BUDEJOVICE-AUDIT.md. Pokrytí a návaznost zaznamenává work/BUDEJOVICE.md. Nový klíč je budejovice-learning-v2.

## Nasazení

Kvíz se publikuje přes GitHub Pages z větve `main` repozitáře `jameskaerem/kvizy-na-prijimacky` na adrese https://jameskaerem.github.io/kvizy-na-prijimacky/. Nasazuje se vygenerovaný `index.html`, README slouží jako dokumentace. Původní adresa https://jameskaerem.github.io/somatologie-otazky/ zůstává během migrace dostupná, aby šlo stáhnout zálohu. Obě adresy leží na stejném webovém původu `jameskaerem.github.io`, takže ve stejném prohlížeči by měly sdílet uložený pokrok. Před prvním otevřením nové adresy přesto stáhni zálohu na původní adrese.

Každý předmět má samostatný pokrok a rozpracované kolo. Přepnutí záložky kolo neukončuje. Vymazání pokroku po potvrzení maže pouze právě vybraný předmět.

Pokrok je místní pro daný prohlížeč a webový původ. Jiná doména, jiný prohlížeč, soukromý režim nebo vymazání dat jej nepřenese. Stažené HTML a původní web nesdílejí automaticky stejné úložiště.

## Zdroj a rozsah biologie

Ivan Novotný, Michal Hruška: **Biologie člověka pro gymnázia**, Fortuna, 4. přepracované vydání, 2007, ISBN 978-80-7373-007-9. Zdrojový soubor: `623763327-biologie-cloveka.pdf`.

Jde o vlastní testy A–D vytvořené podle výkladu, nikoli přepis hotové testové banky nebo oficiálního klíče. Každá otázka má jednu správnou odpověď, číslo tištěné stránky, tři vysvětlující odstavce a paměťovou pomůcku. Zdroj byl přečten vizuálně ze skenu. Tištěná stránka a číslo stránky PDF se liší: PDF obsahuje převážně dvoustrany.

| Biologické otázky | Téma | Tištěné strany | PDF strany |
|---|---|---|---|
| 1–50 | Úvod, regulace, pojiva, kosti, klouby a kostra | 15–29 | 8–15 |
| 51–70 | Kosterní, srdeční a hladké svalstvo, mechanismus stahu | 30–35 | 16–18 |
| 71–80 | Oddíly tělesné vody, ionty, tkáňový mok, míza a výměna látek | 35–37 | 18–19 |
| 81–100 | Krev, krvinky, destičky, srážení, plazma/sérum, AB0 a Rh | 37–42 | 19–22 |
| 101–120 | Vrozená a adaptivní imunita, B/T-lymfocyty, protilátky, paměť a imunizace | 43–47 | 22–24 |
| 121–135 | Plicní a tělní oběh, vrátnice, tepny, žíly, kapiláry a žilní návrat | 48–51 | 25–26 |
| 136–150 | Srdeční cyklus, chlopně, ozvy, puls, tepový objem, koronární cévy, převod a EKG | 51–54 | 26–28 |
| 151–170 | Tlak, průtok, odpor, baroreflex a pojmy měření tlaku | 55–60 | 28–31 |
| 171–180 | Základní cévní pojmy: ateroskleróza, LDL/HDL, trombus, ischemie, infarkt, bypass a radikály | 60–62 | 31–32 |
| 181–190 | Mízní cesty, návrat tekutin, transport tuků, uzliny a slezina | 63–64 | 32–33 |
| 191–200 | Ventilace, metabolismus plynů, vodivé cesty, hltan, hrtan a průdušky | 65–67 | 33–34 |
| 201–215 | Stavba plic, pleura, alveoly a obrana dýchacích cest | 68–69 | 35 |
| 216–230 | Nádech/výdech, dýchací svaly, plicní objemy a mrtvý prostor | 69–71 | 35–36 |
| 231–240 | Řízení dýchání, reakce na CO₂, zotavení po zátěži a další funkce | 71–73 | 36–37 |
| 241–250 | Difuze plynů, přenos O₂, hemoglobin a transport CO₂ | 75–77 | 38–39 |
| 251–265 | Trávení a vstřebávání, ústní dutina, stavba zubu, chrup a sliny | 78–81 | 40–41 |
| 266–275 | Polykání, jícen, peristaltika, žaludek a žaludeční šťáva | 82–83 | 42 |
| 276–290 | Tenké střevo, klky, pankreas, žluč a zpracování živin | 84–87 | 43–44 |
| 291–300 | Tlusté střevo, mikrobiota, vyprazdňování a základní funkce jater | 87–90 | 44–46 |
| 301–317 | Metabolismus sacharidů, tuků a bílkovin, esenciální aminokyseliny a obnova tkání | 91–93 | 46–47 |
| 318–329 | Složky výživy, vláknina, esenciální mastné kyseliny, vitaminy, minerály a voda | 93–94 | 47–48 |
| 330–339 | Exkrece, osmoregulace, stavba ledviny a nefronu | 95–98 | 48–50 |
| 340–350 | Odvod moči, filtrace, resorpce, ADH a vyprazdňování měchýře | 98–100 | 50–51 |
| 351–355 | Močové kameny, selhání ledvin, princip hemodialýzy a anatomické souvislosti infekcí | 101 | 51 |
| 356–370 | Kůže, pokožka, škára, podkoží, pigment, mazové a potní žlázy, akné | 102–103 | 52 |
| 371–385 | Tvorba a výdej tepla, pocení, kožní průtok, hypotalamus a horečka | 104–106 | 53–54 |
| 386–400 | Nervová soustava, neuron, dendrity, axon, myelin, zakončení, glie a nervová vlákna | 107–109 | 54–55 |
| 401–410 | Klidový membránový potenciál, iontové gradienty, kanály a pumpy | 110–112 | 56–57 |
| 411–422 | Chemické synapse, receptory, depolarizace, hyperpolarizace a místní potenciály | 113–115 | 57–58 |
| 423–434 | Vznik a vedení vzruchu, kódování a integrace nervových signálů | 114–118 | 58–60 |
| 435–450 | Nervové obvody, reflexní oblouk, vrozené a podmíněné reflexy | 119–120 | 60–61 |
| 451–465 | Vývoj CNS, stavba míchy, kořeny míšních nervů a vzestupné/sestupné dráhy | 121–122 | 61–62 |
| 466–475 | Mozkový kmen, hlavové nervy, komory, likvor a mozkové pleny | 123–124 | 62–63 |
| 476–485 | Mozeček, střední mozek, talamus, hypotalamus a propojení s hypofýzou | 125–126 | 63–64 |
| 486–500 | Hemisféry, mozkový trámec, kůra a její oblasti, limbické struktury a bazální ganglia | 126–128 | 64–65 |
| 501–510 | Lokomoce, úrovně motorického řízení, kortikospinální dráha a zpětná vazba | 129–131 | 65–66 |
| 511–525 | Autonomní ganglia, sympatikus, parasympatikus a koordinace vnitřních funkcí | 131–134 | 66–68 |
| 526–535 | Plasticita a základní pojmy cévních, infekčních a degenerativních onemocnění CNS | 134–137 | 68–69 |
| 536–550 | Endokrinní/exokrinní sekrece, hormony, receptory a uspořádání hypofýzy | 138–141 | 70–71 |
| 551–560 | Růstový hormon, prolaktin, ACTH, gonadotropiny a účinky oxytocinu | 140–141 | 71 |
| 561–575 | Štítná žláza, T3/T4, kalcitonin, příštítná tělíska a řízení vápníku | 141–143 | 71–72 |
| 576–586 | Kůra a dřeň nadledvin, kortizol, aldosteron, katecholaminy a zátěž | 141, 143–145 | 71–73 |
| 587–600 | Endokrinní slinivka, inzulin/glukagon, pohlavní žlázy, placenta a melatonin | 145–146 | 73–74 |
| 601–615 | Smyslové receptory, adekvátní podněty, hmat a propriocepce | 147–149 | 74–75 |
| 616–630 | Vnitřní ucho, labyrinty, rovnovážné váčky, kanálky a řízení rovnováhy | 149–151 | 75–76 |
| 631–640 | Zvuk, frekvence, hlasitost, barva tónu, boltec, zvukovod a bubínek | 151–153 | 76–77 |
| 641–650 | Sluchové kůstky, okénka, sluchová trubice, hlemýžď, Cortiho orgán a nerv | 152–154 | 77–78 |
| 651–665 | Stavba oka, optická prostředí, sítnice, tyčinky a čípky | 155–156 | 78–79 |
| 666–685 | Zrakové pigmenty a zpracování, akomodace, ochrana oka a optické vady | 156–159 | 79–80 |
| 686–696 | Chuť, čich, souhra kožního čití a nociceptivní zakončení | 160–162 | 81–82 |
| 697–700 | Gamety, meióza, zygota a obnovení diploidního počtu chromozomů | 162–163 | 82 |
| 701–750 | Pohlavní chromozomy, genetická variabilita, pohlavní orgány, gametogeneze, cyklus a oplození | 163–175 | 82–88 |
| 751–800 | Časný vývoj, placenta, těhotenství, porod, antikoncepce a období lidského života | 176–192; doplnění 173, 229 | 89–97; 87, 115 |
| 801–850 | Zdraví, alkohol, závislosti, kouření, infekce, genetické choroby a prostředí; doplnění respiračních infekcí | 193–203; doplnění 74–75 | 97–102; 38 |
| 851–900 | Principy praktických cvičení a doplnění příloh: hlavové nervy, vitaminy, kostra a skupiny látek | 204–230 | 103–116 |

Přehled popisuje použité zdroje, nikoli záruku, že každý odstavec těchto stran už má samostatnou otázku. Přesný celkový počet smysluplných testů nelze určit jen z počtu stran. Biologie je tematicky dokončena: všechny hlavní výkladové kapitoly (15–203), principy praktické části (204–218) a témata příloh (219–230) jsou zastoupeny novými nebo dřívějšími otázkami. Neznamená to samostatnou otázku ke každému odstavci či každé buňce tabulky. Předmluva, obsah a rejstřík nejsou samostatná testovaná témata. Podrobný audit je v `work/COVERAGE_AUDIT.md`. Přehled každé nové dávky bude uveden také ve zprávě v chatu.

Problematická zobecnění zdroje se nepřebírají do testovaných správných odpovědí: například srdce má nervovou regulaci, přestože tvoří vlastní rytmus; tkáňový mok není zcela bez bílkovin; ne všichni tkáňoví makrofágové nutně vznikají z cirkulujících monocytů. Vysvětlení rozlišují školní model a jeho meze.

## Ověření

Automatické kontroly ověřují shodu všech původních otázek, zachování uložených dat z předchozích verzí obou předmětů, starší nedokončená kola, nová kola všech 630 a 900 otázek, hodnocení, ochranu před dvojím započtením, nezávislé přepínání a reset, chytré opakování, klávesové ovládání a fungování při poškozeném či blokovaném úložišti. Kontroluje se také absence osobního názvu a integrita ZIPu.

Testy vykonávají skutečný JavaScript aplikace s minimálním adaptérem DOM. Chrome v offline režimu ověřil zobrazení záložek při šířkách 320, 375, 768 a 1280 px, odpověď s vysvětlením a obnovení rozehraného kola po načtení. Ve verzi 2.40.0 Chromium znovu ověřil, že všechny čtyři záložky předmětů jsou při těchto šířkách viditelné bez vodorovného posunu. ZIP obsahuje pouze `index.html` a `README.md`, aplikace nevyžaduje externí knihovny.

Nové otázky jsou založeny na učebnici. Sporné obecné údaje o antikoncepci a přenosu HIV byly porovnány s primárními zdroji; zastaralé dávky, léčebné postupy a právní informace se netestují. Doplňkové ověření: [WHO – antikoncepce](https://www.who.int/health-topics/contraception/), [WHO – HIV/AIDS](https://www.who.int/news-room/fact-sheets/detail/hiv-aids/), [NHGRI – chromozomové odchylky](https://www.genome.gov/about-genomics/fact-sheets/Chromosome-Abnormalities-Fact-Sheet).
## Modelové testové otázky k přijímacím zkouškám na LF MU (fyzika, chemie, biologie)

Čtvrtá záložka obsahuje 769 vlastních otázek podle publikace Mornstein, Dostál, Slaninová (Masarykova univerzita, 2018, ISBN 978-80-210-9045-3): 312 fyzika, 318 chemie, 139 biologie. Dávky 101–150 až 751–769 přibyly ve verzích 2.48.0, 2.50.0, 2.52.0, 2.54.0, 2.56.0, 2.58.0, 2.60.0, 2.62.0, 2.64.0, 2.66.0, 2.68.0, 2.70.0, 2.72.0 a 2.73.0; publikace je tím posouzená celá. Výběr všech otázek nebo jednotlivého předmětu, vlastní uložený pokrok a rozpracovaná kola podle sekcí. Starší zálohy tří předchozích sad zůstávají kompatibilní. Evidence zdrojů a další postup v [mapě LF MU](work/MUNI-POKRYTI.md).

## Univerzita Karlova – modelové otázky 2. LF UK (fyzika, chemie, biologie)

Pátá záložka (od verze 2.44.0) obsahuje 937 vlastních otázek podle modelových otázek 2. lékařské fakulty UK (Karolinum): 34 fyzika (Amler a kol., 2023, jen ukázka knihy, už vyčerpaná), 391 chemie (Blanický, Pelouch, 2019) a 512 biologie (Kočárek a kol., 2019). Od ID 738 jsou otázky ve formátu zkoušky se zaškrtáváním více správných odpovědí. Dávky 51–100 až 888–937 přibyly ve verzích 2.46.0, 2.47.0, 2.49.0, 2.51.0, 2.53.0, 2.55.0, 2.57.0, 2.59.0, 2.61.0, 2.63.0, 2.65.0, 2.67.0, 2.69.0, 2.71.0, 2.75.0, 2.76.0, 2.77.0 a 2.78.0. V rozbalovacím seznamu lze vybrat všechny otázky nebo jeden předmět, každý výběr má vlastní rozpracované kolo. Pokrok se ukládá pod novým klíčem `uk-learning-v2` a volba předmětu pod `uk-section`, stávající klíče se nemění. Záloha zahrnuje i tento kvíz a starší zálohy bez něj se dál načítají. Na širokém displeji je všech pět záložek v jedné řadě, na telefonu ve dvou řadách (3 + 2) se stejnou velikostí. Evidence zdrojů a další postup v [mapě UK](work/UK-POKRYTI.md).
