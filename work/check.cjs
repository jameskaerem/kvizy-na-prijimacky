const fs=require('fs'),vm=require('vm'),assert=require('assert/strict'),zlib=require('zlib');
function historical(path,version){
 return fs.existsSync(path) ? fs.readFileSync(path,'utf8') :
  zlib.gunzipSync(fs.readFileSync(`work/fixtures/${version}.html.gz`)).toString('utf8');
}
const html=fs.readFileSync('index.html','utf8');
const previousHtml=historical('work/index-before-2.17.0.html','biology-850');
const old=fs.readFileSync('work/somatologie-base-1.12.0.html','utf8');
const script=h=>h.match(/<script>([\s\S]*?)<\/script>/)[1];
// Minimal DOM adapter runs the actual application/controller without a browser.
class Element{
 constructor(tag='div'){this.tagName=tag;this.hidden=false;this.disabled=false;this.checked=false;this.children=[];this.style={};this.dataset={};this.attributes={};this.events={};this.textContent='';this._html='';this.className='';this.classList={add:(c)=>{this.className+=' '+c}};}
 set innerHTML(v){this._html=v;this.children=[];}get innerHTML(){return this._html;}
 setAttribute(k,v){this.attributes[k]=String(v);}getAttribute(k){return this.attributes[k]??null;}
 addEventListener(k,fn){this.events[k]=fn;}append(...children){this.children.push(...children);}replaceChildren(...children){this.children=children;}
 focus(){}scrollIntoView(){}
}
function app(source,storage=new Map(),blocked=false){
 const ids=new Map();for(const m of source.matchAll(/id="([^"]+)"/g))ids.set(m[1],new Element());
 const offline=new Element();let confirmMessage='';
 const doc={hidden:false,title:'',getElementById:id=>{if(!ids.has(id))throw Error('Missing ID '+id);return ids.get(id)},querySelector:s=>{assert.equal(s,'.offline');return offline},createElement:t=>new Element(t),createTextNode:text=>({textContent:text}),addEventListener(){}};
 ids.get('subjectSources')&&(ids.get('subjectSources').innerHTML=source.match(/<details class="sources" id="subjectSources">([\s\S]*?)<\/details>/)[1]);
 const context=vm.createContext({document:doc,localStorage:{getItem:k=>{if(blocked)throw Error('blocked');return storage.get(k)||null},setItem:(k,v)=>{if(blocked)throw Error('blocked');storage.set(k,v)},removeItem:k=>storage.delete(k)},window:{scrollTo(){},matchMedia(){return{matches:true}}},confirm:t=>{confirmMessage=t;return true},setInterval(){return 1},console,Date,Map,Set,Intl});
 vm.runInContext(script(source),context);
 return {run:code=>vm.runInContext(code,context),storage,ids,read:code=>JSON.parse(JSON.stringify(vm.runInContext(code,context))),confirmMessage:()=>confirmMessage};
}
const originalQuestions=vm.runInNewContext(script(old).split('const $ =')[0]+';JSON.stringify(QUESTIONS)');
let a=app(html);
assert.equal(a.run('JSON.stringify(SOMATOLOGY_QUESTIONS)'),originalQuestions);
assert.equal(a.run('SOMATOLOGY_QUESTIONS.length'),630);
assert.equal(a.run('BIOLOGY_QUESTIONS.length'),900);
assert.ok(!/Markét|James/.test(html));
assert.ok(html.includes('Studijní kvízy'));
const bio=[...JSON.parse(fs.readFileSync('work/biology-001-050.json','utf8')),...JSON.parse(fs.readFileSync('work/biology-051-100.json','utf8')),...JSON.parse(fs.readFileSync('work/biology-101-150.json','utf8')),...JSON.parse(fs.readFileSync('work/biology-151-200.json','utf8')),...JSON.parse(fs.readFileSync('work/biology-201-250.json','utf8')),...JSON.parse(fs.readFileSync('work/biology-251-300.json','utf8')),...JSON.parse(fs.readFileSync('work/biology-301-350.json','utf8')),...JSON.parse(fs.readFileSync('work/biology-351-400.json','utf8')),...JSON.parse(fs.readFileSync('work/biology-401-450.json','utf8')),...JSON.parse(fs.readFileSync('work/biology-451-500.json','utf8')),...JSON.parse(fs.readFileSync('work/biology-501-550.json','utf8')),...JSON.parse(fs.readFileSync('work/biology-551-600.json','utf8')),...JSON.parse(fs.readFileSync('work/biology-601-650.json','utf8')),...JSON.parse(fs.readFileSync('work/biology-651-700.json','utf8')),...JSON.parse(fs.readFileSync('work/biology-701-750.json','utf8')),...JSON.parse(fs.readFileSync('work/biology-751-800.json','utf8')),...JSON.parse(fs.readFileSync('work/biology-801-850.json','utf8')),...JSON.parse(fs.readFileSync('work/biology-851-900.json','utf8'))];
assert.equal(new Set(bio.map(q=>q.question)).size,900);
bio.forEach((q,i)=>{assert.equal(q.id,i+1);assert.equal(q.options.length,4);assert.equal(new Set(q.options).size,4);assert.ok(q.answer>=0&&q.answer<4);assert.equal(q.paragraphs.length,3);assert.ok(q.memory&&q.sourcePages);});
// Upgrade the existing 850-question biology version without changing content or progress.
const previous=app(previousHtml);previous.run("switchSubject('biologie');start('all');choose(0);nextQuestion();$('guess').checked=true;choose(1);nextQuestion();applyReview(50,true,false);save()");
const biologyBefore=previous.storage.get('biologie-learning-v2');
const upgraded=app(html,previous.storage);
assert.equal(upgraded.run('BANK_SIZE'),900);
assert.equal(upgraded.storage.get('biologie-learning-v2'),biologyBefore);
assert.equal(upgraded.run('data.session.target'),850);
assert.equal(upgraded.run('JSON.stringify(BIOLOGY_QUESTIONS.slice(0,850))'),previous.run('JSON.stringify(BIOLOGY_QUESTIONS)'));
// The earlier deployed 50-question release remains a supported upgrade path.
const earlier=app(historical('work/index-before-2.1.0.html','biology-50'));
earlier.run("switchSubject('biologie');start('all');choose(0);nextQuestion();save()");
const earlierRaw=earlier.storage.get('biologie-learning-v2');
const earlierUpgraded=app(html,earlier.storage);
assert.equal(earlierUpgraded.storage.get('biologie-learning-v2'),earlierRaw);
assert.equal(earlierUpgraded.run('data.session.target'),50);
// The historical 400-question release must also retain its progress and original session target.
const delivered400=app(historical('work/index-before-2.8.0.html','biology-400'));
delivered400.run("switchSubject('biologie');start('all');choose(0);nextQuestion();save()");
const delivered400Raw=delivered400.storage.get('biologie-learning-v2');
const delivered400Upgraded=app(html,delivered400.storage);
assert.equal(delivered400Upgraded.storage.get('biologie-learning-v2'),delivered400Raw);
assert.equal(delivered400Upgraded.run('data.session.target'),400);
assert.equal(delivered400Upgraded.run('JSON.stringify(BIOLOGY_QUESTIONS.slice(0,400))'),delivered400.run('JSON.stringify(BIOLOGY_QUESTIONS)'));
// Retain direct upgrade support from the delivered release preceding the two latest batches.
const deliveredEarlier=app(historical('work/index-before-2.10.0.html','biology-500'));
const deliveredEarlierSize=deliveredEarlier.run('BIOLOGY_QUESTIONS.length');
deliveredEarlier.run("switchSubject('biologie');start('all');choose(0);nextQuestion();save()");
const deliveredEarlierRaw=deliveredEarlier.storage.get('biologie-learning-v2');
const deliveredEarlierUpgrade=app(html,deliveredEarlier.storage);
assert.equal(deliveredEarlierUpgrade.storage.get('biologie-learning-v2'),deliveredEarlierRaw);
assert.equal(deliveredEarlierUpgrade.run('data.session.target'),deliveredEarlierSize);
assert.equal(deliveredEarlierUpgrade.run(`JSON.stringify(BIOLOGY_QUESTIONS.slice(0,${deliveredEarlierSize}))`),deliveredEarlier.run('JSON.stringify(BIOLOGY_QUESTIONS)'));
// Complete the old 850-question round after expansion; new questions wait for a new round.
const oldRoundIds=new Set(upgraded.read('data.session.attempts').map(a=>a.id));
while(upgraded.run('!data.session.completed')){
 const id=upgraded.run('data.session.currentId');assert.ok(id<=850);
 if(upgraded.run('data.session.currentAnswer===null')){assert.ok(!oldRoundIds.has(id));oldRoundIds.add(id);upgraded.run('choose(byId.get(data.session.currentId).answer)');}
 upgraded.run('nextQuestion()');
}
assert.equal(oldRoundIds.size,850);
// Real old controller creates an interrupted round with mixed results and a guess.
const oldApp=app(old);oldApp.run("start('all');choose(0);nextQuestion();$('guess').checked=true;choose(1);nextQuestion();applyReview(630,true,false)");
const oldRaw=oldApp.storage.get('somatologie-learning-v2');
a=app(html,oldApp.storage);
assert.equal(a.storage.get('somatologie-learning-v2'),oldRaw);
assert.equal(a.run("$('recoveryNotice').hidden"),true);
const somato=a.read('data');
a.run("switchSubject('biologie');start('all')");
assert.equal(a.run('BANK_SIZE'),900);assert.equal(a.run('STORAGE_KEY'),'biologie-learning-v2');
assert.equal(a.run('summary().seen'),0);assert.equal(a.run('data.session.target'),900);
const firstBio=a.run('data.session.currentId');
a.run("$('guess').checked=true;choose(byId.get(data.session.currentId).answer)");
assert.equal(a.run('progress(data.session.currentId).lastResult'),'guess');
const bioSaved=a.read('data');a.run("switchSubject('somatologie')");assert.deepEqual(a.read('data'),somato);
a.run("switchSubject('biologie')");assert.deepEqual(a.read('data'),bioSaved);
assert.ok(!a.ids.get('resume').hidden);
a.run('renderQuestion()');assert.equal(a.run('data.session.currentId'),firstBio);assert.equal(a.run("$('next').disabled"),false);
// Reload selects biology and preserves both interrupted rounds.
a=app(html,a.storage);assert.equal(a.run('activeSubject'),'biologie');assert.deepEqual(a.read('data'),bioSaved);
// Complete every biology question once; mixed correct/wrong choices and duplicate click protection.
let counts={correct:1,wrong:0};const visited=new Set([firstBio]);
a.run('nextQuestion()');
while(a.run('!data.session.completed')){
 const id=a.run('data.session.currentId');assert.ok(!visited.has(id));visited.add(id);
 const good=visited.size%5!==0;const index=a.run('byId.get(data.session.currentId).answer');
 a.run(`choose(${good?index:(index+1)%4})`);counts[good?'correct':'wrong']++;
 const turns=a.run('data.turn');a.run('choose(0)');assert.equal(a.run('data.turn'),turns);
 const buttons=a.ids.get('answers').children;assert.ok(buttons[index].className.includes('correct'));assert.ok(buttons.every(b=>b.disabled));
 assert.equal(a.ids.get('explanation').children.length,5);
 a.run('nextQuestion()');
}
assert.equal(visited.size,900);assert.equal(a.run('score().correct'),counts.correct);assert.equal(a.run('summary().seen'),900);assert.equal(a.run('summary().weak'),counts.wrong+1);
assert.equal(a.storage.get('somatologie-learning-v2'),oldRaw);
// Reset cannot erase the other subject.
a.ids.get('reset').events.click();assert.ok(a.confirmMessage().includes('Biologie'));assert.equal(a.run('summary().seen'),0);assert.equal(a.storage.get('somatologie-learning-v2'),oldRaw);
a.run("switchSubject('somatologie')");assert.deepEqual(a.read('data'),somato);
// Legacy migration must never seed the biology subject.
const legacy=new Map([['somatologie-first10-v1',JSON.stringify({version:1,answers:{1:0}})],['market-quiz-subject','biologie']]);
const migrated=app(html,legacy);assert.equal(migrated.run('summary().seen'),0);migrated.run("switchSubject('somatologie')");assert.equal(migrated.run('summary().seen'),1);
// Corrupt subject data is isolated; unavailable storage keeps a functioning in-memory quiz.
const corrupt=new Map([['biologie-learning-v2','broken'],['market-quiz-subject','biologie'],['somatologie-learning-v2',oldRaw]]);
const repaired=app(html,corrupt);assert.equal(repaired.run('summary().seen'),0);assert.equal(corrupt.get('somatologie-learning-v2'),oldRaw);
const unavailable=app(html,new Map(),true);unavailable.run("switchSubject('biologie');start('smart');choose(0)");assert.equal(unavailable.run('data.turn'),1);assert.equal(unavailable.run('storageOK'),false);
// Subject tabs support left/right and preserve independent state.
const keyboard=app(html);keyboard.ids.get('tab-somatologie').events.keydown({key:'ArrowRight',preventDefault(){}});assert.equal(keyboard.run('activeSubject'),'biologie');
const full=app(html);full.run("start('all')");const originalVisited=new Set();
while(full.run('!data.session.completed')){const id=full.run('data.session.currentId');assert.ok(!originalVisited.has(id));originalVisited.add(id);full.run('choose(byId.get(data.session.currentId).answer);nextQuestion()');}
assert.equal(originalVisited.size,630);assert.equal(full.run('score().correct'),630);
const smart=app(html);smart.run("switchSubject('biologie');start('smart');choose((byId.get(data.session.currentId).answer+1)%4)");
const failed=smart.run('data.session.currentId');assert.equal(smart.run('summary().weak'),1);
smart.run('nextQuestion()');assert.notEqual(smart.run('data.session.currentId'),failed);
smart.run(`applyReview(${failed},true,true)`);assert.equal(smart.run(`progress(${failed}).level`),0);
smart.run(`applyReview(${failed},true,false,Date.now()+86400000)`);assert.equal(smart.run(`progress(${failed}).level`),1);
const invalid=app(html,new Map([['market-quiz-subject','__proto__']]));assert.equal(invalid.run('activeSubject'),'somatologie');
const baseline=app(historical('outputs/biologie-somatologie-v2.17.0/index.html','biology-900'));
assert.deepEqual(a.read('BIOLOGY_QUESTIONS'),baseline.read('BIOLOGY_QUESTIONS'));
const school=app(html);
school.run("start('smart');choose(0);switchSubject('biologie');start('all');choose(1);switchSubject('budejovice');start('all')");
const savedOthers=['somatologie','biologie'].map(id=>school.storage.get(id+'-learning-v2'));
const bank=school.read('QUESTIONS');
assert.ok(bank.length>=683);
const expandedExplanations = new Set([31,95,103,107,109,113,114,119,130,173,445,599,654]);
for (const [version,size] of [['2.18.0',50],['2.19.0',100],['2.20.0',150],['2.21.0',200],['2.22.0',250],['2.23.0',300],['2.24.0',350],['2.25.0',400],['2.26.0',450],['2.27.0',500],['2.28.0',550],['2.29.0',600],['2.30.0',608],['2.31.0',612],['2.32.0',620],['2.33.0',628],['2.34.0',635],['2.35.0',647],['2.36.0',654],['2.37.0',660],['2.38.0',683]]) {
 const lastRelease=app(historical(`outputs/studijni-kvizy-v${version}/index.html`,version));
 lastRelease.run("switchSubject('budejovice');start('all');choose(0);nextQuestion();save()");
 const previousBank=lastRelease.read('QUESTIONS');
 for(const [index,previous] of previousBank.entries()){
  const current=bank[index];
  if(expandedExplanations.has(current.id)){
   assert.deepEqual(current.paragraphs.slice(0,previous.paragraphs.length),previous.paragraphs);
   assert.deepEqual({...current,paragraphs:previous.paragraphs},previous);
  }else{
   assert.deepEqual(current,previous);
  }
 }
 const beforeExpansion=lastRelease.read('data');
 const expanded=app(html,lastRelease.storage);
 assert.deepEqual(expanded.read('data'),beforeExpansion);
 assert.equal(expanded.run('data.session.target'),size);
 while(!expanded.run('data.session.completed')){
  assert.ok(expanded.run('data.session.currentId')<=size);
  expanded.run('choose(0);nextQuestion()');
 }
 assert.equal(expanded.run('data.session.attempts.length'),size);
}
assert.equal(new Set(bank.map(q=>q.question)).size,bank.length);
for(const [i,q] of bank.entries()){
 assert.equal(q.id,i+1);assert.equal(new Set(q.options).size,4);assert.equal(q.options.length,4);
 assert.ok(q.title===q.options[q.answer] && q.memory && q.paragraphs.length && q.bookRef);
}
school.run('choose((byId.get(data.session.currentId).answer+1)%4);nextQuestion()');
const savedRound=school.read('data.session');
school.run("switchSubject('biologie');switchSubject('budejovice')");
assert.deepEqual(school.read('data.session'),savedRound);
const resumed=app(html,school.storage);
assert.deepEqual(resumed.read('data.session'),savedRound);
while(!resumed.run('data.session.completed'))resumed.run('choose(byId.get(data.session.currentId).answer);nextQuestion()');
assert.equal(resumed.run('score().correct'),bank.length-1);
resumed.run("start('weak')");assert.equal(resumed.run('data.session.target'),1);
resumed.ids.get('reset').events.click();
assert.equal(resumed.run('summary().seen'),0);
assert.deepEqual(['somatologie','biologie'].map(id=>school.storage.get(id+'-learning-v2')),savedOthers);
const topical=app(html);
topical.run("switchSubject('budejovice');start('all');choose(0);nextQuestion()");
const oldSchoolRound=topical.read('data.session');
const topics=topical.read('SCHOOL_TOPICS');
assert.deepEqual(Object.values(topics).flatMap(topic=>topic.ids).sort((a,b)=>a-b),bank.map(question=>question.id));
function pickTopic(app,key){
 const picker=app.ids.get('schoolSection');
 picker.value=key;
 picker.events.change();
}
for(const [key,topic] of Object.entries(topics)){
 pickTopic(topical,key);
 topical.run("start('all')");
 assert.deepEqual(topical.read('[data.session.currentId,...data.session.queue]').sort((a,b)=>a-b),topic.ids);
}
pickTopic(topical,'physics');
topical.run('choose(byId.get(data.session.currentId).answer);nextQuestion()');
const physicsRound=topical.read('data.session');
const reloadedTopic=app(html,topical.storage);
assert.equal(reloadedTopic.run('schoolSection'),'physics');
assert.deepEqual(reloadedTopic.read('data.session'),physicsRound);
assert.equal(reloadedTopic.ids.get('reset').hidden,true);
pickTopic(reloadedTopic,'all');
assert.deepEqual(reloadedTopic.read('data.session'),oldSchoolRound);
assert.equal(reloadedTopic.run('data.turn'),2);
reloadedTopic.ids.get('reset').events.click();
pickTopic(reloadedTopic,'physics');
assert.equal(reloadedTopic.run('data.session'),null);
assert.equal(reloadedTopic.run('summary().seen'),0);
const result={status:'PASS',unchangedSomatology:630,unchangedOriginalBiology:900,school:bank.length,schoolTopics:Object.fromEntries(Object.values(topics).map(topic=>[topic.name,topic.ids.length])),biology:900,personalNameRemoved:true,somatologyQuestionsExercised:originalVisited.size,biologyQuestionsExercised:visited.size,oldBiologyProgressExactMatch:true,oldProgressExactMatch:true,independentSessions:true,reload:true,isolatedReset:true,legacyMigration:true,corruptStorage:true,blockedStorage:true,keyboardTabs:true,smartReview:true,invalidSubjectRecovery:true,method:'Actual application JavaScript with minimal DOM adapter; no browser visual verification'};
const sourceDevice=app(historical('outputs/studijni-kvizy-v2.38.0/index.html','2.38.0'));
sourceDevice.run("start('all');choose((byId.get(data.session.currentId).answer+1)%4);nextQuestion();switchSubject('biologie');start('smart');choose(byId.get(data.session.currentId).answer);switchSubject('budejovice');start('all');choose(byId.get(data.session.currentId).answer)");
pickTopic(sourceDevice,'physics');
sourceDevice.run("start('all');$('guess').checked=true;choose(byId.get(data.session.currentId).answer)");
const exported=app(html,sourceDevice.storage).read('backupProgress()');
assert.equal(exported.subjects.somatologie.session.attempts[0].good,false);
assert.equal(exported.subjects.budejovice.sections.physics.attempts[0].guessed,true);
const destination=app(html);
assert.ok(destination.run(`restoreProgress(${JSON.stringify(exported)})`));
const reload=app(html,destination.storage);
assert.deepEqual(reload.read('backupProgress().subjects'),exported.subjects);
assert.equal(reload.run('activeSubject'),exported.activeSubject);
assert.equal(reload.run('schoolSection'),exported.schoolSection);
const beforeInvalid=new Map(reload.storage);
exported.subjects.budejovice.sections.physics.queue.push(-1);
assert.equal(reload.run(`restoreProgress(${JSON.stringify(exported)})`),false);
assert.deepEqual(reload.storage,beforeInvalid);
assert.equal(migrated.read('backupProgress().subjects.somatologie.turn'),1);
result.progressBackupRoundTrip=true;
fs.mkdirSync('tmp',{recursive:true});
fs.writeFileSync('tmp/check-results.json',JSON.stringify(result,null,2));console.log(JSON.stringify(result));
