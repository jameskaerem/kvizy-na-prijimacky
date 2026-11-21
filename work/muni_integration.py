import json

TITLE='Modelové testové otázky k přijímacím zkouškám na LF MU (fyzika, chemie, biologie)'

def integrate(s, root):
    bank=[]
    for batch in sorted((root/'work').glob('muni-*.json')):
        bank.extend(json.loads(batch.read_text(encoding='utf-8')))
    assert [q['id'] for q in bank]==list(range(1,len(bank)+1))
    topics={key:{'name':name,'ids':[q['id'] for q in bank if q['subject']==name]} for key,name in [('physics','Fyzika'),('chemistry','Chemie'),('biology','Biologie')]}
    assert sum(len(t['ids']) for t in topics.values())==len(bank)
    def replace(old,new):
        nonlocal s
        assert old in s,old
        s=s.replace(old,new,1)
    replace('const SUBJECTS={', 'const MUNI_QUESTIONS='+json.dumps(bank,ensure_ascii=False)+';\nconst MUNI_TOPICS='+json.dumps(topics,ensure_ascii=False)+';\nconst SUBJECTS={\n muni:{name:'+json.dumps(TITLE,ensure_ascii=False)+',questions:MUNI_QUESTIONS,key:"muni-learning-v2",context:"Modelové úlohy LF MU, vydání 2018. Vyber všechny předměty nebo jeden z nich."},')
    replace('  </div>\n  <div id="subjectPanel"',f'    <button type="button" id="tab-muni" class="subject-tab muni-tab" role="tab" aria-selected="false" aria-controls="subjectPanel" tabindex="-1">{TITLE}<small>{len(bank)} otázek</small></button>\n  </div>\n  <div id="subjectPanel"')
    replace('</style>', '.muni-tab{grid-column:1/-1;overflow-wrap:anywhere}.muni-tab small{display:block}\n</style>')
    replace('  <section class="intro">',f'  <div id="muniPicker" class="school-picker" hidden><label for="muniSection">Předmět LF MU</label><select id="muniSection"><option value="all">Všechny otázky · {len(bank)}</option></select></div>\n  <section class="intro">')
    replace("const isSchool=activeSubject==='budejovice';", "const isSchool=activeSubject==='budejovice';\n const isMuni=activeSubject==='muni';")
    replace('const topic=isSchool&&schoolTopics.get(schoolSection);','const topic=isSchool?schoolTopics.get(schoolSection):isMuni?muniTopics.get(muniSection):null;')
    replace("$('schoolPicker').hidden=!isSchool;", "$('schoolPicker').hidden=!isSchool;\n $('muniPicker').hidden=!isMuni;")
    replace("$('subjectSources').innerHTML=activeSubject===", "$('subjectSources').innerHTML=isMuni?'<summary>O otázkách a zdrojích</summary><p>"+TITLE+". Vojtěch Mornstein, Jiří Dostál, Iva Slaninová. Masarykova univerzita, 2018, ISBN 978-80-210-9045-3. Vlastní otázky podle modelových úloh, s referencí na kapitolu a číslo úlohy.</p>':activeSubject===")
    replace("activeSubject==='budejovice'?schoolStorageData():data", "activeSubject==='budejovice'?schoolStorageData():activeSubject==='muni'?muniStorageData():data")
    replace("schoolSessions={};}data=freshData()", "schoolSessions={};}if(activeSubject==='muni'){if(muniSection!=='all')return;muniSessions={};}data=freshData()")
    replace("selectSchoolSection(savedSchoolSection());\n }", "selectSchoolSection(savedSchoolSection());\n }else if(id==='muni'){loadMuniSections();selectMuniSection(savedMuniSection());}")
    replace("const subjectIds=['somatologie','biologie','budejovice'];", "const subjectIds=['somatologie','biologie','budejovice','muni'];")
    replace('switchSubject(initialSubject,true);', (root/'work/school_sections.js').read_text(encoding='utf-8').replace('school','muni').replace('School','Muni').replace('SCHOOL','MUNI').replace('budejovice-section','muni-section')+'\nswitchSubject(initialSubject,true);')
    replace("id === 'budejovice' ? schoolStorageData() : data", "id === 'budejovice' ? schoolStorageData() : id === 'muni' ? muniStorageData() : data")
    replace("subjects,\n  };", "muniSection: activeSubject === 'muni' ? muniSection : savedMuniSection(),\n    subjects,\n  };")
    replace('Object.keys(backup.subjects).length !== subjectIds.length', "Object.keys(backup.subjects).some(id=>!subjectIds.includes(id)) || (backup.muniSection!==undefined && backup.muniSection!=='all' && !muniTopics.has(backup.muniSection))")
    replace('const saved = backup.subjects[id];', "const saved = backup.subjects[id];\n    if(id==='muni' && saved===undefined && backup.activeSubject!=='muni')continue;")
    replace("if (id === 'budejovice' && Object.hasOwn(saved, 'sections'))", "if (['budejovice','muni'].includes(id) && Object.hasOwn(saved, 'sections'))")
    replace('const topic = schoolTopics.get(section);', "const topic = (id==='muni'?muniTopics:schoolTopics).get(section);")
    replace('JSON.stringify(backup.subjects[id])', 'JSON.stringify(backup.subjects[id] ?? freshData())')
    replace('updates.set(SECTION_PREFERENCE, backup.schoolSection);', "updates.set(SECTION_PREFERENCE, backup.schoolSection);\n  updates.set('muni-section',backup.muniSection || 'all');")
    replace("document.createTextNode(q.memory));", "document.createTextNode(q.memory || q.paragraphs[0]));")
    return s
