let schoolSection = 'all';
let schoolSessions = {};
const schoolTopics = new Map(Object.entries(SCHOOL_TOPICS).map(([key, topic]) => [
  key, {name: topic.name, questions: topic.ids.map(id => SCHOOL_QUESTIONS[id - 1])}
]));

for (const [key, topic] of schoolTopics) {
  const option = element('option', '', topic.name + ' · ' + topic.questions.length);
  option.value = key;
  $('schoolSection').append(option);
}

function savedSchoolSection() {
  try {
    const key = localStorage.getItem('budejovice-section');
    if (schoolTopics.has(key)) return key;
  } catch (error) {}
  return 'all';
}

function schoolSessionMatches(session, questions) {
  if (!validSession(session)) return false;
  if (session === null) return true;
  const ids = new Set(questions.map(question => question.id));
  return session.target <= ids.size && ids.has(session.currentId) &&
    session.queue.every(id => ids.has(id)) && session.attempts.every(attempt => ids.has(attempt.id));
}

function loadSchoolSections() {
  const saved = data.sections || {};
  schoolSessions = {all: data.session};
  for (const [key, topic] of schoolTopics) {
    schoolSessions[key] = schoolSessionMatches(saved[key], topic.questions) ? saved[key] : null;
  }
  delete data.sections;
}

function schoolStorageData() {
  schoolSessions[schoolSection] = data.session;
  const {all, ...sections} = schoolSessions;
  return { ...data, session: all, sections };
}

function selectSchoolSection(key) {
  schoolSection = schoolTopics.has(key) ? key : 'all';
  QUESTIONS = schoolTopics.get(schoolSection)?.questions || SCHOOL_QUESTIONS;
  BANK_SIZE = QUESTIONS.length;
  data.session = schoolSessions[schoolSection] ?? null;
  $('schoolSection').value = schoolSection;
}

$('schoolSection').addEventListener('change', () => {
  schoolSessions[schoolSection] = data.session;
  selectSchoolSection($('schoolSection').value);
  save();
  try { localStorage.setItem('budejovice-section', schoolSection); } catch (error) {}
  updateSubjectUI();
  renderHome();
  $('announcement').textContent = '';
});
