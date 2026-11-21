from pathlib import Path
import json

# Subject, chapter, source item, printed page, prompt, correct answer, distractors, explanation.
rows = '''Fyzika|Jednotky|1–7|7|Která dvojice obsahuje výhradně základní jednotky SI?|kelvin a kandela|newton a metr|joule a sekunda|volt a kilogram|Kelvin a kandela patří mezi sedm základních jednotek; N, J a V jsou odvozené.
Fyzika|Jednotky|8–11|7|Která jednotka není jednotkou SI, byť se běžně používá?|kalorie|tesla|pascal|joule|Kalorie je mimo SI; tesla, pascal a joule jsou odvozené jednotky SI.
Fyzika|Jednotky|14,42|8–9|Jakou veličinu vyjadřuje součin výkonu a doby jeho působení?|energii|sílu|tlak|účinnost|E = P·t; wattsekunda je joule.
Fyzika|Jednotky|15,28|8|Jaký rozměr má hybnost tělesa?|kg·m/s|kg·m/s²|kg·m²/s²|kg/s|Hybnost p = mv, proto má jednotku kg·m/s.
Fyzika|Jednotky|16|8|Která jednotka odpovídá kg·m²·s⁻²?|joule|watt|pascal|newton|Práce je síla krát dráha; N·m = kg·m²·s⁻².
Fyzika|Jednotky|17|8|Jak lze vyjádřit pascal základními jednotkami SI?|kg·m⁻¹·s⁻²|kg·m·s⁻²|kg·m²·s⁻³|kg·m⁻²·s⁻¹|Tlak je síla na plochu; Pa = N/m².
Fyzika|Jednotky|19,29|8–9|V jaké jednotce SI se vyjadřuje účinnost stroje?|je bezrozměrná|watt|joule|pascal|Účinnost je poměr užitečné energie k dodané energii, často vyjádřený procenty.
Fyzika|Jednotky|20|8|Proč je příčné zvětšení čočky bez jednotky?|Je poměrem dvou délek.|Je součinem dvou sil.|Je podílem energie a času.|Je převrácenou hodnotou ohniskové vzdálenosti.|Zvětšení porovnává velikost obrazu s velikostí předmětu.
Fyzika|Jednotky|22–23|8|Jaká je jednotka momentu setrvačnosti?|kg·m²|N·m|kg·m/s|kg/m²|Moment setrvačnosti bodu je I = mr².
Fyzika|Jednotky|24,38|8–9|Jakou jednotku má povrchové napětí kapaliny?|N/m|N/m²|N·m|J/m|Povrchové napětí je síla vztažená k délce rozhraní.
Fyzika|Jednotky|26|8|Která jednotka vyjadřuje kapacitanci (kapacitní reaktanci)?|ohm|farad|henry|coulomb|Kapacitance Xc je druh reaktance, tedy má jednotku odporu, ohm; farad patří kapacitě.
Fyzika|Jednotky|27|8|Jakou jednotkou se měří magnetická indukce B?|tesla|weber|henry|ampér|Tesla je jednotka indukce, weber jednotka magnetického toku.
Fyzika|Jednotky|30,34|9|Který součin jednotek představuje elektrický výkon?|V·A|V/A|A·s|Ω·s|P = UI, takže volt krát ampér je watt.
Fyzika|Jednotky|33|9|Jaká je jednotka látkové koncentrace v základním vyjádření SI?|mol/m³|mol·m³|kg/mol|mol/m²|Koncentrace c = n/V, tedy látkové množství na objem.
Fyzika|Jednotky|35,41|9|Jaká jednotka je ekvivalentní ampérsekundě?|coulomb|volt|watt|farad|Náboj Q = It; 1 C = 1 A·s.
Fyzika|Jednotky|40|9|Proč nemá součinitel smykového tření jednotku?|Je poměrem třecí a normálové síly.|Je součinem síly a rychlosti.|Je poměrem hmotnosti a plochy.|Je převrácenou hodnotou tlaku.|μ = Ft/Fn; newtony se vykrátí.
Fyzika|Jednotky|44|9|Jakou jednotku má součin elektrického odporu a proudu?|volt|ampér|watt|coulomb|Z Ohmova zákona U = RI plyne Ω·A = V.
Chemie|Vzorce|1|62|Který vzorec odpovídá soli Cu⁺ a dusitanového aniontu?|CuNO₂|Cu(NO₂)₂|CuNO₃|Cu₂NO₂|Dusitan NO₂⁻ a Cu⁺ se vyrovnají v poměru 1 : 1.
Chemie|Vzorce|2|62|Jaký je vzorec chlornanu vápenatého?|Ca(ClO)₂|CaClO|Ca(ClO₃)₂|CaCl₂|Ca²⁺ vyžaduje dva anionty ClO⁻.
Chemie|Vzorce|3|62|Jaký je vzorec mangananu barnatého?|BaMnO₄|Ba(MnO₄)₂|BaMnO₃|Ba₂MnO₄|Manganan MnO₄²⁻ a Ba²⁺ tvoří poměr 1 : 1.
Chemie|Vzorce|4|62|Který vzorec patří jodistanu manganatému?|Mn(IO₄)₂|MnIO₄|Mn(IO₃)₂|MnI₂|Mn²⁺ potřebuje dva anionty IO₄⁻.
Chemie|Vzorce|5|62|Jaký vzorec má chlorečnan amonný?|NH₄ClO₃|NH₄ClO₄|(NH₄)₂ClO₃|NH₄ClO₂|Amonný NH₄⁺ a chlorečnan ClO₃⁻ mají opačné jednotkové náboje.
Chemie|Vzorce|6|62|Jaký je vzorec disiřičitanu vápenatého?|CaS₂O₅|CaSO₃|CaS₂O₇|Ca(HSO₃)₂|Disiřičitan S₂O₅²⁻ vyrovnává náboj Ca²⁺.
Chemie|Vzorce|7|62|Kolik iontů Fe²⁺ připadá na dva fosforečnanové anionty v neutrální soli?|3|2|1|6|Dva PO₄³⁻ dávají −6, tři Fe²⁺ dávají +6; Fe₃(PO₄)₂.
Chemie|Vzorce|8|62|Jaký vzorec má hydrogensíran chromitý?|Cr(HSO₄)₃|Cr(HSO₄)₂|Cr₂(SO₄)₃|CrHSO₄|Cr³⁺ vyžaduje tři HSO₄⁻.
Chemie|Vzorce|9|62|Jaký je vzorec difosforečnanu hořečnatého?|Mg₂P₂O₇|Mg₃(PO₄)₂|MgP₂O₇|Mg₂PO₄|Difosforečnan P₂O₇⁴⁻ potřebuje dva Mg²⁺.
Chemie|Vzorce|10|62|Jaký vzorec má jodistan železitý?|Fe(IO₄)₃|Fe(IO₄)₂|Fe(IO₃)₃|FeIO₄|Fe³⁺ vyžaduje tři IO₄⁻.
Chemie|Vzorce|11|62|Která sůl obsahuje dva amonné ionty na jeden dichromanový anion?|(NH₄)₂Cr₂O₇|NH₄Cr₂O₇|(NH₄)₂CrO₄|(NH₄)₃Cr₂O₇|Dichroman Cr₂O₇²⁻ má náboj −2 a NH₄⁺ náboj +1.
Chemie|Vzorce|12|62|Jaký vzorec má cíničitan vápenatý při aniontu SnO₃²⁻?|CaSnO₃|Ca(SnO₃)₂|CaSnO₂|Ca₂SnO₃|Ca²⁺ a SnO₃²⁻ se navzájem neutralizují.
Chemie|Vzorce|13|62|Jaký je vzorec tetrahydroxohlinitanu hořečnatého?|Mg[Al(OH)₄]₂|Mg[Al(OH)₄]|Mg₂[Al(OH)₄]|Mg₃[Al(OH)₄]₂|Komplex [Al(OH)₄]⁻ má náboj −1, takže jsou potřeba dva na Mg²⁺.
Chemie|Vzorce|15|62|Jaký vzorec má hydrogenfosforečnan vápenatý?|CaHPO₄|Ca(HPO₄)₂|Ca(H₂PO₄)₂|Ca₃(PO₄)₂|HPO₄²⁻ má náboj −2 a tvoří s Ca²⁺ neutrální sůl.
Chemie|Vzorce|16|62|Který vzorec patří arseničnanu barnatému?|Ba₃(AsO₄)₂|Ba₃(AsO₃)₂|BaAsO₄|Ba₂(AsO₄)₃|Tři Ba²⁺ a dva AsO₄³⁻ mají celkový náboj nula.
Chemie|Výpočty|28|63|Jaký je přibližný hmotnostní zlomek kyslíku v H₂O₂ (H = 1, O = 16)?|0,94|0,47|0,50|0,06|Kyslík přispívá 32 z celkových 34 jednotek hmotnosti; 32/34 ≈ 0,94.
Chemie|Výpočty|29|63|Kolik procent hmotnosti glukózy C₆H₁₂O₆ tvoří kyslík (Mr = 180, Ar(O) = 16)?|53,3 %|35,6 %|26,7 %|60,0 %|Šest atomů kyslíku přispívá 96; 96/180 × 100 ≈ 53,3 %.
Biologie|Historie|2|122|Ve kterém roce bylo publikováno narození ovce Dolly?|1997|1953|1977|2003|Dolly se narodila v roce 1996; výsledek byl publikován roku 1997.
Biologie|Historie|3|122|Kdo roku 1953 navrhl model dvojité šroubovice DNA?|J. D. Watson a F. Crick|Matthias Schleiden a Theodor Schwann|Gregor Mendel a Thomas Morgan|Louis Pasteur a Robert Koch|Watson a Crick navrhli model s využitím důležitých rentgenových dat Rosalind Franklinové a dalších badatelů.
Biologie|Historie|5|122|Který český badatel přispěl k rozvoji buněčné teorie?|Jan Evangelista Purkyně|Jan Janský|Antonín Holý|Otto Wichterle|Purkyně studoval buněčnou stavbu živočišných tkání a protoplazmu.
Biologie|Historie|10–11|122–123|Který objev předcházel publikaci klonování Dolly?|rozluštění genetického kódu|dokončení projektu lidského genomu|zveřejnění úplné sekvence lidského chromozomu T2T|objev CRISPR-Cas9 jako cíleného genomového nástroje|Genetický kód byl rozluštěn v 60. letech 20. století, Dolly byla publikována roku 1997.
Biologie|Buňka|6|123|Jaký protein je hlavní stavební složkou mikrofilament?|aktin|tubulin|kolagen|keratin|Mikrofilamenta jsou aktinová vlákna; mikrotubuly tvoří tubulin.
Biologie|Buňka|8|123|Která struktura má podobnou vnitřní stavbu jako pohyblivý eukaryotický bičík?|pohyblivá řasinka|bakteriální bičík|aktinové mikrofilamentum|ribozom|Řasinky a bičíky eukaryot mají zpravidla mikrotubulární uspořádání 9 + 2.
Biologie|Buňka|10|124|Která lidská buňka má přibližně desetinu milimetru v průměru a patří k největším kulovitým buňkám?|zralý oocyt|erytrocyt|lymfocyt|trombocyt|Oocyt je mimořádně velká buňka; erytrocyt má průměr přibližně 7–8 µm.
Biologie|Buňka|11,26|124–125|Které organely rostlinné buňky mají vlastní ribozomy?|mitochondrie a chloroplasty|vakuola a lysozom|Golgiho aparát a peroxizom|centrioly a jadérko|Mitochondrie a chloroplasty mají vlastní ribozomy a mohou syntetizovat část svých proteinů.
Biologie|Buňka|14|124|Které úseky pre-mRNA zůstávají po sestřihu ve zralé RNA?|exony|introny|centromery|telomery|Exony jsou zachovanými úseky RNA; ne všechny exony musejí kódovat bílkovinu.
Biologie|Buňka|30|125|Která struktura buněčného jádra nemá vlastní membránu?|jadérko|mitochondrie|lysozom|chloroplast|Jadérko je nemembránová jaderná struktura spojená s tvorbou ribozomálních podjednotek.
Biologie|Buňka|7|123|Jaký řád velikosti odpovídá typickému průměru tyčinkové bakterie?|jednotky mikrometrů|jednotky centimetrů|jednotky metrů|jednotky nanometrů|Bakteriální buňky mají obvykle mikrometrové rozměry.
Biologie|Buňka|3|123|Proč mohou mít svalová a kožní buňka stejného jedince rozdílnou funkci i při podobném genomu?|Liší se aktivitou genů.|Mají vždy rozdílný počet chromozomů.|Svalová buňka neobsahuje DNA.|Kožní buňka nemá ribozomy.|Diferenciace závisí především na tom, které geny buňka využívá.
Biologie|Buňka|23|125|Co se při běžném sestřihu pre-mRNA děje s introny?|Jsou odstraněny z RNA.|Přemění se na aminokyseliny.|Zdvojí se v chromozomu.|Přesunou se do mitochondrie.|Introny jsou vystřiženy z pre-mRNA, exony se spojují.
Biologie|Buňka|1|123|Co přímo ovlivňuje rychlost prosté difúze látky přes membránu?|koncentrační gradient|počet chromozomů|počet jadérek|fáze mitózy|Větší rozdíl koncentrací podporuje rychlejší čistý tok difúzí.
Biologie|Obecná biologie|6|122|Která posloupnost správně roste v úrovni biologické organizace?|buňka → orgán → organismus → společenstvo|orgán → buňka → organismus → společenstvo|organismus → orgán → společenstvo → buňka|společenstvo → organismus → buňka → orgán|Buňky vytvářejí tkáně a orgány, organismy tvoří společenstva.
Biologie|Buňka|27|125|Co zásadně ovlivňuje prostorovou strukturu bílkoviny?|pořadí aminokyselin|počet chromozomů|velikost jádra|počet nukleotidů v ribozomální RNA|Primární sekvence aminokyselin určuje interakce při skládání bílkoviny.'''

bank=[]
for i,line in enumerate(rows.splitlines(),1):
    subject,chapter,number,page,prompt,correct,d1,d2,d3,explanation=line.split('|')
    options=[correct,d1,d2,d3]
    answer=(i-1)%4
    options.insert(answer,options.pop(0))
    bank.append(dict(id=i,subject=subject,category=subject+' · '+chapter,bookRef=f'LF MU · {subject} · {chapter} {number} · str. {page}',sourcePages=page,sourceItem=number,question=prompt,options=options,answer=answer,title=correct,paragraphs=[explanation],memory=correct))
assert len(bank)==50
Path(__file__).with_name('muni-001-050.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
