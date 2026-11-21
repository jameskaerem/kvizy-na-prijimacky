const BACKUP_FORMAT = 'studijni-kvizy-progress';
const SUBJECT_PREFERENCE = 'market-quiz-subject';
const SECTION_PREFERENCE = 'budejovice-section';

function globalQuestionMap() {
  return byId;
}

function backupProgress() {
  const subjects = {};
  for (const id of subjectIds) {
    const raw = id === activeSubject ? null : localStorage.getItem(SUBJECTS[id].key);
    if (id === activeSubject) {
      subjects[id] = id === 'budejovice' ? schoolStorageData() : data;
    } else {
      const questions = new Map(SUBJECTS[id].questions.map(q => [q.id, q]));
      subjects[id] = raw === null ? migrateOld(id, questions) || freshData() : JSON.parse(raw);
    }
  }
  const backup = {
    format: BACKUP_FORMAT,
    version: 1,
    exportedAt: new Date().toISOString(),
    activeSubject,
    schoolSection: activeSubject === 'budejovice' ? schoolSection : savedSchoolSection(),
    subjects,
  };
  if (!validBackup(backup)) throw new Error('Neplatný uložený pokrok.');
  return backup;
}

function validBackup(backup) {
  if (!backup || backup.format !== BACKUP_FORMAT || backup.version !== 1 ||
      !subjectIds.includes(backup.activeSubject) ||
      !(backup.schoolSection === 'all' || schoolTopics.has(backup.schoolSection)) ||
      !backup.subjects || Object.keys(backup.subjects).length !== subjectIds.length) return false;
  for (const id of subjectIds) {
    const saved = backup.subjects[id];
    const questions = new Map(SUBJECTS[id].questions.map(q => [q.id, q]));
    if (!validData(saved, questions)) return false;
    if (id === 'budejovice' && Object.hasOwn(saved, 'sections')) {
      if (!saved.sections || typeof saved.sections !== 'object' || Array.isArray(saved.sections)) return false;
      for (const [section, round] of Object.entries(saved.sections)) {
        const topic = schoolTopics.get(section);
        if (!topic || !validSession(round, new Map(topic.questions.map(q => [q.id, q])))) return false;
      }
    }
  }
  return true;
}

function restoreProgress(backup) {
  if (!validBackup(backup)) return false;
  const updates = new Map(subjectIds.map(id => [SUBJECTS[id].key, JSON.stringify(backup.subjects[id])]));
  updates.set(SUBJECT_PREFERENCE, backup.activeSubject);
  updates.set(SECTION_PREFERENCE, backup.schoolSection);
  const original = new Map([...updates.keys()].map(key => [key, localStorage.getItem(key)]));
  const written = [];
  try {
    for (const [key, value] of updates) {
      localStorage.setItem(key, value);
      written.push(key);
    }
  } catch (error) {
    for (const key of written.reverse()) {
      const value = original.get(key);
      if (value === null) localStorage.removeItem(key);
      else localStorage.setItem(key, value);
    }
    throw error;
  }
  // Reload the restored subject without saving the old in-memory state first.
  switchSubject(backup.activeSubject, true);
  return true;
}

$('backupExport').addEventListener('click', () => {
  const status = $('backupStatus');
  try {
    const backup = backupProgress();
    const file = new Blob([JSON.stringify(backup, null, 2)], {type:'application/json'});
    const url = URL.createObjectURL(file);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'studijni-kvizy-pokrok-' + backup.exportedAt.slice(0,10) + '.json';
    link.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    status.textContent = 'Záloha je připravená ke stažení. Ulož ji třeba na soukromý cloudový disk.';
  } catch (error) {
    status.textContent = 'Zálohu se nepodařilo vytvořit. Zkontroluj, že prohlížeč povoluje místní úložiště.';
  }
});

$('backupImport').addEventListener('click', () => $('backupFile').click());
$('backupFile').addEventListener('change', async event => {
  const input = event.currentTarget;
  const file = input.files[0];
  input.value = '';
  if (!file) return;
  const status = $('backupStatus');
  let backup;
  try {
    if (file.size > 10 * 1024 * 1024) throw new Error('Příliš velký soubor.');
    backup = JSON.parse(await file.text());
  } catch (error) {}
  if (!validBackup(backup)) {
    status.textContent = 'Tento soubor není platná záloha pro tuto verzi kvízu.';
    return;
  }
  if (!confirm('Načtení zálohy nahradí pokrok všech předmětů v tomto prohlížeči. Pokud tu už máš pokrok, můžeš ho napřed zálohovat. Chceš pokračovat?')) {
    status.textContent = 'Načtení bylo zrušeno.';
    return;
  }
  try {
    restoreProgress(backup);
    status.textContent = 'Pokrok všech předmětů a rozpracovaná kola jsou načtené.';
  } catch (error) {
    status.textContent = 'Zálohu se nepodařilo uložit. Zkontroluj nastavení nebo volné místo v prohlížeči.';
  }
});
