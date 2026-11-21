import json

# Fifth subject: model questions of 2. LF UK (physics, chemistry, biology).
# Applied after muni_integration; reuses the section logic of school_sections.js under the 'uk' prefix.
TITLE='Modelové otázky k přijímacím zkouškám na 2. LF UK (fyzika, chemie, biologie)'
SOURCES=('<summary>O otázkách a zdrojích</summary>'
 '<p>'+TITLE+'. Vlastní otázky se čtyřmi možnostmi a jednou správnou odpovědí podle modelových otázek 2. lékařské fakulty Univerzity Karlovy (Nakladatelství Karolinum):</p>'
 '<ul><li>Evžen Amler a kol.: <em>Modelové otázky z fyziky pro přijímací zkoušky</em>, 8. vydání, 2023, ISBN 978-80-246-5740-0. K dispozici je ukázka (kapitola Základní pojmy a začátek Mechaniky I) bez klíče, odpovědi jsou ověřené výpočtem.</li>'
 '<li>Petr Blanický, Václav Pelouch: <em>Modelové otázky z chemie pro přijímací zkoušky</em>, 7. vydání, 2019, ISBN 978-80-246-4441-7.</li>'
 '<li>Eduard Kočárek a kol.: <em>Modelové otázky z biologie pro přijímací zkoušky</em>, 7. vydání, 2019, ISBN 978-80-246-4443-1.</li></ul>'
 '<p>V původních testech může být správných i více odpovědí. Otázky jsou proto přeformulované tak, aby měly právě jednu správnou odpověď. U každé otázky je kapitola, číslo úlohy (u chemie pořadí otázky na stránce) a tištěná strana.</p>')

def integrate(s, root):
    bank=[]
    for batch in sorted((root/'work').glob('uk-*.json')):
        bank.extend(json.loads(batch.read_text(encoding='utf-8')))
    assert [q['id'] for q in bank]==list(range(1,len(bank)+1))
    topics={key:{'name':name,'ids':[q['id'] for q in bank if q['subject']==name]} for key,name in [('physics','Fyzika'),('chemistry','Chemie'),('biology','Biologie')]}
    assert sum(len(t['ids']) for t in topics.values())==len(bank)
    def replace(old,new):
        nonlocal s
        assert s.count(old)==1,old
        s=s.replace(old,new,1)
    replace('const SUBJECTS={', 'const UK_QUESTIONS='+json.dumps(bank,ensure_ascii=False)+';\nconst UK_TOPICS='+json.dumps(topics,ensure_ascii=False)+';\nconst SUBJECTS={\n uk:{name:"Univerzita Karlova",questions:UK_QUESTIONS,key:"uk-learning-v2",context:"Modelové otázky 2. LF UK z fyziky, chemie a biologie. Vyber všechny předměty nebo jeden z nich."},')
    replace('  </div>\n  <div id="subjectPanel"',f'    <button type="button" id="tab-uk" class="subject-tab uk-tab" role="tab" aria-selected="false" aria-controls="subjectPanel" tabindex="-1" title="{TITLE}">Univerzita Karlova<small>Modelové otázky · {len(bank)}</small></button>\n  </div>\n  <div id="subjectPanel"')
    replace('  <section class="intro">',f'  <div id="ukPicker" class="school-picker" hidden><label for="ukSection">Předmět Univerzita Karlova</label><select id="ukSection"><option value="all">Všechny otázky · {len(bank)}</option></select></div>\n  <section class="intro">')
    replace("const isMuni=activeSubject==='muni';", "const isMuni=activeSubject==='muni';\n const isUk=activeSubject==='uk';")
    replace('isMuni?muniTopics.get(muniSection):null;','isMuni?muniTopics.get(muniSection):isUk?ukTopics.get(ukSection):null;')
    replace("$('muniPicker').hidden=!isMuni;", "$('muniPicker').hidden=!isMuni;\n $('ukPicker').hidden=!isUk;")
    replace("$('subjectSources').innerHTML=isMuni?", "$('subjectSources').innerHTML=isUk?"+json.dumps(SOURCES,ensure_ascii=False)+":isMuni?")
    replace("activeSubject==='muni'?muniStorageData():data", "activeSubject==='muni'?muniStorageData():activeSubject==='uk'?ukStorageData():data")
    replace("if(activeSubject==='muni'){if(muniSection!=='all')return;muniSessions={};}", "if(activeSubject==='muni'){if(muniSection!=='all')return;muniSessions={};}if(activeSubject==='uk'){if(ukSection!=='all')return;ukSessions={};}")
    replace("else if(id==='muni'){loadMuniSections();selectMuniSection(savedMuniSection());}", "else if(id==='muni'){loadMuniSections();selectMuniSection(savedMuniSection());}else if(id==='uk'){loadUkSections();selectUkSection(savedUkSection());}")
    replace("const subjectIds=['somatologie','biologie','budejovice','muni'];", "const subjectIds=['somatologie','biologie','budejovice','muni','uk'];")
    replace('switchSubject(initialSubject,true);', (root/'work/school_sections.js').read_text(encoding='utf-8').replace('budejovice-section','uk-section').replace('school','uk').replace('School','Uk').replace('SCHOOL','UK')+'\nswitchSubject(initialSubject,true);')
    replace("id === 'muni' ? muniStorageData() : data", "id === 'muni' ? muniStorageData() : id === 'uk' ? ukStorageData() : data")
    replace("subjects,\n  };", "ukSection: activeSubject === 'uk' ? ukSection : savedUkSection(),\n    subjects,\n  };")
    replace("!muniTopics.has(backup.muniSection))", "!muniTopics.has(backup.muniSection)) || (backup.ukSection!==undefined && backup.ukSection!=='all' && !ukTopics.has(backup.ukSection))")
    replace("if(id==='muni' && saved===undefined && backup.activeSubject!=='muni')continue;", "if(['muni','uk'].includes(id) && saved===undefined && backup.activeSubject!==id)continue;")
    replace("if (['budejovice','muni'].includes(id) && Object.hasOwn(saved, 'sections'))", "if (['budejovice','muni','uk'].includes(id) && Object.hasOwn(saved, 'sections'))")
    replace("const topic = (id==='muni'?muniTopics:schoolTopics).get(section);", "const topic = (id==='muni'?muniTopics:id==='uk'?ukTopics:schoolTopics).get(section);")
    replace("updates.set('muni-section',backup.muniSection || 'all');", "updates.set('muni-section',backup.muniSection || 'all');\n  updates.set('uk-section',backup.ukSection || 'all');")
    return s
