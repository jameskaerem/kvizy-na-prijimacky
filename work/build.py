from pathlib import Path
import json,re
from school_sections import group_questions

ROOT=Path(__file__).resolve().parent.parent
ORIGINAL=ROOT/'work/somatologie-base-1.12.0.html'
original=ORIGINAL.read_text(encoding='utf-8')
bio=json.loads((ROOT/'work/biology-001-050.json').read_text(encoding='utf-8'))
bio+=json.loads((ROOT/'work/biology-051-100.json').read_text(encoding='utf-8'))
bio+=json.loads((ROOT/'work/biology-101-150.json').read_text(encoding='utf-8'))
bio+=json.loads((ROOT/'work/biology-151-200.json').read_text(encoding='utf-8'))
bio+=json.loads((ROOT/'work/biology-201-250.json').read_text(encoding='utf-8'))
bio+=json.loads((ROOT/'work/biology-251-300.json').read_text(encoding='utf-8'))
bio+=json.loads((ROOT/'work/biology-301-350.json').read_text(encoding='utf-8'))
bio+=json.loads((ROOT/'work/biology-351-400.json').read_text(encoding='utf-8'))
bio+=json.loads((ROOT/'work/biology-401-450.json').read_text(encoding='utf-8'))
bio+=json.loads((ROOT/'work/biology-451-500.json').read_text(encoding='utf-8'))
bio+=json.loads((ROOT/'work/biology-501-550.json').read_text(encoding='utf-8'))
bio+=json.loads((ROOT/'work/biology-551-600.json').read_text(encoding='utf-8'))
bio+=json.loads((ROOT/'work/biology-601-650.json').read_text(encoding='utf-8'))
bio+=json.loads((ROOT/'work/biology-651-700.json').read_text(encoding='utf-8'))
bio+=json.loads((ROOT/'work/biology-701-750.json').read_text(encoding='utf-8'))
bio+=json.loads((ROOT/'work/biology-751-800.json').read_text(encoding='utf-8'))
bio+=json.loads((ROOT/'work/biology-801-850.json').read_text(encoding='utf-8'))
bio+=json.loads((ROOT/'work/biology-851-900.json').read_text(encoding='utf-8'))
assert len(bio)==900 and [q['id'] for q in bio]==list(range(1,901))
school = []
for batch in sorted((ROOT / 'work').glob('budejovice-*.json')):
    school.extend(json.loads(batch.read_text(encoding='utf-8')))
assert [q['id'] for q in school] == list(range(1, len(school) + 1)) and school
s=original.replace('<title>Somatologie · malý krok, velké pochopení</title>','<title>Studijní kvízy · Procvičování</title>')
s=s.replace('content="630 otázek ze somatologie s vysvětlením a chytrým opakováním. Chyby a tipy častěji, zvládnuté otázky s odstupem."','content="Somatologie, biologie a přijímací testy z Českých Budějovic. Tři kvízy s vysvětlením, chytrým opakováním a samostatným ukládáním pokroku."')
import base64 as _b64
_icon_svg=(ROOT/'work/icon/icon.svg').read_text(encoding='utf-8').strip()
_icon_png=_b64.b64encode((ROOT/'work/icon/apple-touch-icon.png').read_bytes()).decode()
s=s.replace('<title>','<link rel="icon" type="image/svg+xml" href="data:image/svg+xml;base64,'+_b64.b64encode(_icon_svg.encode()).decode()+'">\n  <link rel="apple-touch-icon" href="data:image/png;base64,'+_icon_png+'">\n  <title>',1)
s=s.replace('<meta name="theme-color" content="#f6f3ee">','<meta name="theme-color" content="#f6f7f9">',1)
s=s.replace('<div class="brand-name">Somatologie</div>','<div class="brand-name">Studijní kvízy</div>')
s=s.replace('</style>','''
.subject-tabs{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:7px;padding:6px;background:#eae9e1;border-radius:18px;margin:23px 0 10px}.subject-tab{min-height:56px;border:0;border-radius:13px;background:transparent;color:#56635b;font-size:14px;font-weight:700;padding:10px 8px;line-height:1.3}.subject-tab[aria-selected="true"]{background:var(--paper);color:#344e43;box-shadow:0 2px 8px #32463712}.subject-tab small{display:block;font-weight:500;font-size:11px;margin-top:4px;color:var(--muted)}.subject-context{font-size:12px;color:var(--muted);margin:0 3px 17px;line-height:1.65}.subject-tabs+.intro{margin-top:20px}.book-number{text-align:right;overflow-wrap:anywhere}.brand-name{font-size:19px}@media(max-width:360px){.brand-name{font-size:17px}.offline{font-size:10px}.subject-tab{font-size:12px;padding:7px 2px}}
</style>''')
s=s.replace('</style>','.brand>div:nth-child(2){min-width:0;flex:1}.brand-name{font-size:18px;line-height:1.25}.offline{flex-shrink:0}\n</style>')
s=s.replace('</style>', '''.school-picker{display:grid;gap:6px;margin:0 0 16px}
.school-picker[hidden]{display:none}
.school-picker label{font-size:13px;font-weight:700}
.school-picker select{width:100%;min-height:44px;padding:8px 12px;border:1px solid #b4bdb4;border-radius:10px;background:var(--paper);color:inherit;font:inherit}
</style>''')
tabs='''
  <div class="subject-tabs" role="tablist" aria-label="Vyber předmět">
    <button type="button" id="tab-somatologie" class="subject-tab" role="tab" aria-selected="true" aria-controls="subjectPanel" tabindex="0">Somatologie<small>630 otázek</small></button>
    <button type="button" id="tab-biologie" class="subject-tab" role="tab" aria-selected="false" aria-controls="subjectPanel" tabindex="-1">Biologie<small>900 otázek</small></button>
    <button type="button" id="tab-budejovice" class="subject-tab" role="tab" aria-selected="false" aria-controls="subjectPanel" tabindex="-1">České Budějovice<small>SCHOOL_COUNT otázek</small></button>
  </div>
  <div id="subjectPanel" role="tabpanel" aria-labelledby="tab-somatologie">
  <p id="subjectContext" class="subject-context"></p>
  <div id="schoolPicker" class="school-picker" hidden>
    <label for="schoolSection">Kvíz pro České Budějovice</label>
    <select id="schoolSection"><option value="all">Všechny otázky · SCHOOL_COUNT</option></select>
  </div>
'''
s=s.replace('  <section class="intro">',tabs.replace('SCHOOL_COUNT',str(len(school)))+'  <section class="intro">',1)
s=s.replace('</main>','  </div>\n</main>',1)
s=s.replace('<h3>Test všech 630</h3>','<h3 id="allTitle">Test všech 630</h3>')
s=s.replace('<details class="sources"><summary>O otázkách a zdrojích</summary>','<details class="sources" id="subjectSources"><summary>O otázkách a zdrojích</summary>',1)
s=s.replace('Vymazat celý uložený pokrok</button>','Vymazat pokrok tohoto předmětu</button>')
s=s.replace('Vymazání dole resetuje celé učení.','Vymazání dole resetuje pouze právě vybraný předmět.')
s=s.replace('<summary>Uložený pokrok</summary>', '<summary>Záloha a přenos pokroku</summary>', 1)
s=s.replace('<button class="reset" id="reset">', '''
<div class="backup-actions">
  <button type="button" class="reset" id="backupExport">Stáhnout zálohu</button>
  <button type="button" class="reset" id="backupImport">Načíst zálohu</button>
  <input id="backupFile" type="file" accept=".json,application/json" hidden>
</div>
<p>Stáhni soubor a ulož ho mimo toto zařízení. Na druhém zařízení ho můžeš načíst. Záloha zahrnuje všechny předměty a rozpracovaná kola.</p>
<p id="backupStatus" role="status"></p>
<button class="reset" id="reset">''', 1)
s=s.replace('</style>', (ROOT/'work/design.css').read_text(encoding='utf-8')+'\n</style>', 1)
s=s.replace('const QUESTIONS = [','const SOMATOLOGY_QUESTIONS = [',1)
s=s.replace('QUESTIONS.push(', 'SOMATOLOGY_QUESTIONS.push(')
bank_code='''const BIOLOGY_QUESTIONS = BIO_DATA;
const SCHOOL_QUESTIONS = SCHOOL_DATA;
const SCHOOL_TOPICS = SCHOOL_TOPIC_DATA;
let activeSubject='somatologie';
let QUESTIONS=SOMATOLOGY_QUESTIONS;
let BANK_SIZE=QUESTIONS.length;
let STORAGE_KEY='somatologie-learning-v2';
let byId=new Map(QUESTIONS.map(q=>[q.id,q]));
const SUBJECTS={
 budejovice:{name:'České Budějovice',questions:SCHOOL_QUESTIONS,key:'budejovice-learning-v2',context:'Procvičování podle přijímacích testů Zdravotně sociální fakulty JU.'},
 somatologie:{name:'Somatologie',questions:SOMATOLOGY_QUESTIONS,key:'somatologie-learning-v2',context:'630 otázek z původní sady. Hodnocení podle tištěného klíče; upozornění na nepřesnosti najdeš ve vysvětlení.'},
 biologie:{name:'Biologie',questions:BIOLOGY_QUESTIONS,key:'biologie-learning-v2',context:'900 nově vytvořených otázek podle výkladu knihy Biologie člověka. Každá otázka má právě jednu správnou odpověď.'}
};
'''.replace('SCHOOL_DATA',json.dumps(school,ensure_ascii=False)).replace('BIO_DATA',json.dumps(bio,ensure_ascii=False,indent=2)).replace('SCHOOL_TOPIC_DATA',json.dumps(group_questions(school),ensure_ascii=False))
s=s.replace('const $ = id => document.getElementById(id);',bank_code+'\nconst $ = id => document.getElementById(id);',1)
for text in ["const BANK_SIZE = QUESTIONS.length;","const STORAGE_KEY = 'somatologie-learning-v2';","const byId = new Map(QUESTIONS.map(q => [q.id,q]));"]:
    assert s.count(text)==1,text
    s=s.replace(text,'')
s=s.replace("function migrateOld(){","function migrateOld(subject=activeSubject, byId=globalQuestionMap()){\n  if(subject!=='somatologie')return null;",1)
s=s.replace('function validSession(s){','function validSession(s, byId=globalQuestionMap()){',1)
start_validation=s.index('function validSession(')
end_validation=s.index('function storageUnavailable()',start_validation)
validation=s[start_validation:end_validation].replace('s.target>BANK_SIZE','s.target>byId.size')
validation=validation.replace('function validData(d){','function validData(d, byId=globalQuestionMap()){').replace('validSession(d.session)','validSession(d.session,byId)')
s=s[:start_validation]+validation+s[end_validation:]
s=s.replace('JSON.stringify(data));}catch(e){storageUnavailable();}',"JSON.stringify(activeSubject==='budejovice'?schoolStorageData():data));}catch(e){storageUnavailable();}",1)
s=s.replace("target:mode==='smart'?10:ids.length","target:mode==='smart'?Math.min(10,BANK_SIZE):ids.length",1)
s=s.replace("+' / '+BANK_SIZE+' · '+(q.bookRef", "+' · '+(q.bookRef",1)
s=s.replace('return;data=freshData();save();renderHome();scrollTop();','return;if(activeSubject===\'budejovice\'){if(schoolSection!==\'all\')return;schoolSessions={};}data=freshData();save();renderHome();scrollTop();',1)
# Dynamic wording preserves the original printed-key distinction for somatology.
s=s.replace("'✕ Tentokrát ne. Podle klíče je správně '","'✕ Tentokrát ne. '+(activeSubject!=='somatologie'?'Správně je ':'Podle klíče je správně ')")
s=s.replace("'. Správně podle klíče'","'. Správně'+(activeSubject!=='somatologie'?'':' podle klíče')")
s=s.replace("'. Tvoje odpověď, nesprávně podle klíče.'","'. Tvoje odpověď, nesprávně'+(activeSubject!=='somatologie'?'.':' podle klíče.')")
s=s.replace("'Nesprávně podle klíče. Správná odpověď je '","'Nesprávně. Správná odpověď je '")
s=s.replace("'Podle klíče: '+correctLabel(q)","(activeSubject!=='somatologie'?'Správná odpověď: ':'Podle klíče: ')+correctLabel(q)")
s=s.replace("'Opravdu vymazat celý uložený pokrok všech '+BANK_SIZE+' otázek? Tento krok nejde vrátit.'","'Opravdu vymazat pokrok předmětu '+SUBJECTS[activeSubject].name+' ('+BANK_SIZE+' otázek)? Tento krok nejde vrátit.'")
# Startup and the source list are handled per subject below.
s=s.replace('data=load();save();renderHome();','data=load();save();updateSubjectUI();renderHome();',1)
start=s.index('const uniqueSources=new Map();')
end=s.index('</script>',start)
s=s[:start]+'''
const somatologySourceHTML=$('subjectSources').innerHTML;
const schoolSourceHTML='<summary>O otázkách a zdrojích</summary><p>České Budějovice test 2019 oprava6.pdf (Všeobecná sestra) a České Budějovice TESTY 2019, 2021, 2022.pdf (biologie, všeobecná informovanost a motivační testy 2020 a testy 2021, Fyzioterapie; Biologie a Všeobecná informovanost 2019, Radiologický asistent) a České Budějovice TESTY 2024 nové.pdf (ošetřovatelství, sociální práce, management, biologie, společenské vědy, informatika, chemie a fyzika), České Budějovice testy 2024 oprava6.pdf a České Budějovice testy 2024.pdf. Sada zahrnuje i doplnění z archivu prilohy_6393.zip. Opakované otázky jsou v bance zastoupené jednou. Otázky jsou upravené pro čtyři možnosti. Čísla u otázky odkazují na úlohu, tištěnou stranu a stránku PDF.</p>';
const biologySourceHTML=`<summary>O otázkách a zdrojích</summary><p>Ivan Novotný, Michal Hruška: <em>Biologie člověka pro gymnázia</em>, Fortuna, 4. přepracované vydání, 2007, ISBN 978-80-7373-007-9.</p><p>První sada obsahuje 50 vlastních testových otázek vytvořených podle výkladu na tištěných stranách 15–29 (PDF strany 8–15). Nejde o přepis hotových otázek A–D ani o oficiální klíč učebnice. Referenci na konkrétní stránku najdeš u každé otázky.</p><p>Témata: úvod, organizace těla a regulace; pojiva; stavba a růst kostí; kostní dřeň; klouby; páteř a hrudník; lebka; kosti končetin. Formulace i vysvětlení jsou napsaná pro tento kvíz. Další sady budou navazovat po 50 otázkách.</p><p>Otázky mají vždy jednu správnou odpověď. Vysvětlení vychází z příslušného výkladu; záměrně se netestují problematická zobecnění, například zařazení zubní skloviny mezi pojiva.</p><p>Samotný HTML soubor funguje bez internetu. Každý předmět má samostatné výsledky, opakování i rozpracované kolo. Pokrok se ukládá v tomto prohlížeči na stejné adrese.</p><ul class="source-list" id="sourceList"></ul>`;
function updateSubjectUI(){
 const config=SUBJECTS[activeSubject];
 const isSchool=activeSubject==='budejovice';
 const topic=isSchool&&schoolTopics.get(schoolSection);
 document.title=(topic?topic.name+' · '+config.name:config.name)+' · Procvičování';
 $('schoolPicker').hidden=!isSchool;
 $('reset').hidden=Boolean(topic);
 $('reset').textContent=isSchool?'Vymazat celý pokrok Českých Budějovic':'Vymazat pokrok tohoto předmětu';
 for(const id of Object.keys(SUBJECTS)){
  const button=$('tab-'+id);button.setAttribute('aria-selected',String(id===activeSubject));button.tabIndex=id===activeSubject?0:-1;
 }
 $('subjectPanel').setAttribute('aria-labelledby','tab-'+activeSubject);
 $('subjectContext').textContent=config.context;
 document.querySelector('.offline').textContent=BANK_SIZE+' otázek';
 $('allTitle').textContent='Test všech '+BANK_SIZE;
 $('subjectSources').innerHTML=activeSubject==='budejovice'?schoolSourceHTML:activeSubject==='biologie'?biologySourceHTML:somatologySourceHTML;
 const uniqueSources=new Map();
 QUESTIONS.forEach(q=>[...(q.source?[q.source]:[]),...(q.sources||[])].forEach(source=>uniqueSources.set(source.url,source)));
 for(const source of uniqueSources.values()){const li=element('li');const a=element('a','',source.label);a.href=source.url;a.target='_blank';a.rel='noopener noreferrer';li.append(a);$('sourceList').append(li);}
}
function switchSubject(id,initial=false){
 if(!Object.hasOwn(SUBJECTS,id)||(!initial&&id===activeSubject))return;
 if(!initial)save();
 activeSubject=id;const config=SUBJECTS[id];QUESTIONS=config.questions;BANK_SIZE=QUESTIONS.length;STORAGE_KEY=config.key;byId=new Map(QUESTIONS.map(q=>[q.id,q]));
 storageOK=true;$('storageNotice').hidden=true;$('recoveryNotice').hidden=true;
 $('saveStatus').textContent='Pokrok se ukládá v tomto prohlížeči. Bez účtu a registrace.';
 data=load();
 if(id==='budejovice'){
  loadSchoolSections();
  selectSchoolSection(savedSchoolSection());
 }
 save();updateSubjectUI();renderHome();$('announcement').textContent='';
 try{localStorage.setItem('market-quiz-subject',id);}catch(e){}
 if(!initial)scrollTop();
}
const subjectIds=['somatologie','biologie','budejovice'];
subjectIds.forEach(id=>{
 const button=$('tab-'+id);
 button.addEventListener('click',()=>switchSubject(id));
 button.addEventListener('keydown',event=>{
  if(!['ArrowLeft','ArrowRight','Home','End'].includes(event.key))return;
  event.preventDefault();let index=subjectIds.indexOf(id);
  if(event.key==='Home')index=0;else if(event.key==='End')index=subjectIds.length-1;else index=(index+(event.key==='ArrowRight'?1:-1)+subjectIds.length)%subjectIds.length;
  switchSubject(subjectIds[index]);$('tab-'+subjectIds[index]).focus();
 });
});
let initialSubject='somatologie';try{const saved=localStorage.getItem('market-quiz-subject');if(Object.hasOwn(SUBJECTS,saved))initialSubject=saved;}catch(e){}
''' + (ROOT/'work/school_sections.js').read_text(encoding='utf-8') + '\nswitchSubject(initialSubject,true);\n' + (ROOT/'work/progress-backup.js').read_text(encoding='utf-8') + '\n' + (ROOT/'work/motion.js').read_text(encoding='utf-8') + '\n' + (ROOT/'work/picker.js').read_text(encoding='utf-8') + s[end:]
s=s.replace('První sada obsahuje 50 vlastních testových otázek vytvořených podle výkladu na tištěných stranách 15–29 (PDF strany 8–15).','Banka obsahuje 900 vlastních testových otázek vytvořených podle výkladu na tištěných stranách 15–230 (PDF strany 8–116).')
s=s.replace('kosti končetin. Formulace i vysvětlení','kosti končetin; svalstvo; tělní tekutiny; krev a krevní skupiny; imunita; oběhové okruhy, cévy a činnost srdce; regulace oběhu, cévní pojmy, mízní soustava, dýchací cesty, plíce, ventilace a transport dýchacích plynů; trávicí soustava od úst po střeva a játra; metabolismus, výživa, ledviny a tvorba moči; kůže, termoregulace a úvod do nervové soustavy, membránový potenciál, synapse, vzruchy a reflexy, mícha, mozkový kmen, mozeček, mezimozek a mozková kůra, řízení motoriky, autonomní nervstvo, základní pojmy nemocí nervové soustavy a hormonální řízení, hormony hypofýzy, štítná žláza, příštítná tělíska, nadledviny a endokrinní slinivka; smyslové receptory, hmat, propriocepce, rovnováha, sluch, zrak, chuť, čich, kožní čití a rozmnožování, vývoj člověka a zdraví; v dokončené sadě také principy praktických cvičení a vybrané souhrnné údaje příloh. Formulace i vysvětlení')
# Avoid accessing source HTML constants before their initialization.
s=s.replace('data=load();save();updateSubjectUI();renderHome();','// Initialized after subject UI constants.',1)
from muni_integration import integrate
s=integrate(s,ROOT)
from uk_integration import integrate as integrate_uk
s=integrate_uk(s,ROOT)
# Design 3.0: equally sized subject tabs; the full LF MU title stays in the panel text.
import re as _re
s,n=_re.subn(r'(id="tab-muni" class="subject-tab muni-tab"[^>]*)>[^<]*<small>(\d+) otázek</small>', lambda m: m.group(1)+' title="Modelové testové otázky k přijímacím zkouškám na LF MU (fyzika, chemie, biologie)">LF MU<small>Modelové otázky · '+m.group(2)+'</small>', s, count=1)
assert n==1
s=s.replace('<header class="brand">','<header class="brand">',1)
theme_button='<button type="button" class="theme-toggle" id="themeToggle" aria-label="Vzhled: podle systému" title="Vzhled: podle systému"><span class="theme-icon" aria-hidden="true"></span></button>\n  </header>'
assert s.count('</header>')==1
s=s.replace('</header>',theme_button,1)
boot="<script data-theme-boot>try{var t=String(localStorage.getItem('quiz-theme')||'').replace(/\x22/g,'');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t);}catch(e){}</script>\n"
assert s.count('<body>')==1
s=s.replace('<body>',boot+'<body>',1)
(ROOT/'index.html').write_text(s,encoding='utf-8')
assert 'Markét' not in s and 'James' not in s
print(f'Built 630 somatology, 900 biology and {len(school)} school questions.')
