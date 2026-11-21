// Presentation only: subject colour and smooth transitions. Stored progress is not touched.
(function () {
  const root = document.documentElement;
  const reduced = () => {
    try { return window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (error) { return true; }
  };
  function play(el, frames, duration) {
    if (!el || typeof el.animate !== 'function' || reduced()) return;
    try { el.animate(frames, {duration: duration || 340, easing: 'cubic-bezier(.2,.75,.25,1)'}); } catch (error) {}
  }
  function markSubject() {
    if (root && root.setAttribute) root.setAttribute('data-subject', activeSubject);
  }
  function viewKey() {
    return activeSubject + ':' + (activeSubject === 'budejovice' ? schoolSection : activeSubject === 'muni' ? muniSection : '');
  }
  let shownKey = viewKey();
  let shownQuestion = data.session && !data.session.completed ? data.session.currentId : null;

  const baseUpdateSubjectUI = updateSubjectUI;
  updateSubjectUI = function () {
    const previous = shownKey;
    const result = baseUpdateSubjectUI.apply(this, arguments);
    markSubject();
    shownKey = viewKey();
    if (previous !== shownKey) {
      const before = previous.split(':')[0];
      const step = subjectIds.indexOf(activeSubject) - subjectIds.indexOf(before);
      const offset = step > 0 ? '18px' : step < 0 ? '-18px' : '0';
      play(document.getElementById('subjectPanel'), [
        {opacity: 0, transform: 'translateX(' + offset + ') translateY(' + (step ? '0' : '8px') + ')'},
        {opacity: 1, transform: 'none'},
      ], 380);
    }
    return result;
  };

  const baseRenderQuestion = renderQuestion;
  renderQuestion = function () {
    const result = baseRenderQuestion.apply(this, arguments);
    const session = data.session;
    const id = session && !session.completed ? session.currentId : null;
    if (screen === 'quiz' && id !== null && id !== shownQuestion) {
      play(document.getElementById('quiz'), [
        {opacity: 0, transform: 'translateY(14px) scale(.985)'},
        {opacity: 1, transform: 'none'},
      ], 360);
    }
    shownQuestion = id;
    return result;
  };

  const baseRenderResults = renderResults;
  renderResults = function () {
    const result = baseRenderResults.apply(this, arguments);
    shownQuestion = null;
    const scoreBox = document.getElementById('results');
    const score = scoreBox && scoreBox.querySelector ? scoreBox.querySelector('.result-score') : null;
    if (score && score.style && score.style.setProperty) {
      const rate = parseInt(score.textContent, 10) || 0;
      score.style.setProperty('--p', String(reduced() ? rate : 0));
      if (!reduced()) requestAnimationFrame(() => requestAnimationFrame(() => score.style.setProperty('--p', String(rate))));
    }
    return result;
  };

  // Light / dark / system appearance. Stored separately from learning progress.
  const THEME_KEY = 'quiz-theme';
  const THEMES = {
    auto: {next: 'light', icon: '◐', label: 'Vzhled: podle systému. Přepnout na světlý.'},
    light: {next: 'dark', icon: '☀', label: 'Vzhled: světlý. Přepnout na tmavý.'},
    dark: {next: 'auto', icon: '☾', label: 'Vzhled: tmavý. Přepnout podle systému.'},
  };
  function readTheme() {
    try { const value = String(localStorage.getItem(THEME_KEY) || '').replace(/"/g, ''); return value === 'light' || value === 'dark' ? value : 'auto'; } catch (error) { return 'auto'; }
  }
  function applyTheme(mode) {
    if (root && root.setAttribute) {
      if (mode === 'auto') root.removeAttribute('data-theme'); else root.setAttribute('data-theme', mode);
    }
    const button = document.getElementById('themeToggle');
    const icon = button.querySelector ? button.querySelector('.theme-icon') : null;
    if (icon) icon.textContent = THEMES[mode].icon;
    button.setAttribute('aria-label', THEMES[mode].label);
    button.setAttribute('title', THEMES[mode].label);
    button.dataset.mode = mode;
  }
  document.getElementById('themeToggle').addEventListener('click', () => {
    const mode = THEMES[readTheme()].next;
    try { localStorage.setItem(THEME_KEY, mode); } catch (error) {}
    if (root && root.classList && !reduced()) {
      root.classList.add('theme-switching');
      setTimeout(() => root.classList.remove('theme-switching'), 450);
    }
    applyTheme(mode);
  });
  applyTheme(readTheme());

  markSubject();
})();
