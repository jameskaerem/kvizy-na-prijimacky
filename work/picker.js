// Presentation only: styled section pickers. The native <select> stays the source of truth,
// so saved section keys, change handlers and backups keep working unchanged.
(function () {
  if (typeof document.querySelectorAll !== 'function') return;
  const pickers = [];
  let uid = 0;

  function parts(text) {
    const at = text.lastIndexOf(' · ');
    return at < 0 ? {name: text, count: ''} : {name: text.slice(0, at), count: text.slice(at + 3)};
  }

  function build(select) {
    const wrap = select.closest('.school-picker');
    const label = wrap && wrap.querySelector('label');
    const id = 'picker' + (++uid);
    const box = document.createElement('div');
    box.className = 'picker';
    const button = document.createElement('button');
    button.type = 'button';
    button.id = id + 'Button';
    button.className = 'picker-button';
    button.setAttribute('aria-haspopup', 'listbox');
    button.setAttribute('aria-expanded', 'false');
    button.setAttribute('aria-controls', id + 'List');
    const current = document.createElement('span');
    current.className = 'picker-current';
    const chevron = document.createElement('span');
    chevron.className = 'picker-chevron';
    chevron.setAttribute('aria-hidden', 'true');
    chevron.textContent = '›';
    button.append(current, chevron);
    const list = document.createElement('ul');
    list.id = id + 'List';
    list.className = 'picker-list';
    list.setAttribute('role', 'listbox');
    list.tabIndex = -1;
    list.hidden = true;
    if (label) {
      if (!label.id) label.id = id + 'Label';
      button.setAttribute('aria-labelledby', label.id + ' ' + button.id);
      list.setAttribute('aria-labelledby', label.id);
      label.htmlFor = button.id;
    }
    const items = [...select.options].map((option, index) => {
      const li = document.createElement('li');
      li.id = id + 'Option' + index;
      li.className = 'picker-option';
      li.setAttribute('role', 'option');
      li.dataset.value = option.value;
      li.style.setProperty('--i', String(Math.min(index, 12)));
      const {name, count} = parts(option.textContent);
      const nameEl = document.createElement('span');
      nameEl.className = 'picker-name';
      nameEl.textContent = name;
      li.append(nameEl);
      if (count) {
        const countEl = document.createElement('span');
        countEl.className = 'picker-count';
        countEl.textContent = count;
        li.append(countEl);
      }
      li.addEventListener('click', () => choose(index));
      li.addEventListener('mousemove', () => highlight(index));
      return li;
    });
    list.append(...items);
    box.append(button, list);
    select.classList.add('picker-native');
    select.tabIndex = -1;
    select.setAttribute('aria-hidden', 'true');
    select.after(box);

    let active = 0;
    const picker = {select, box, button, list, items, sync};

    function sync() {
      const index = Math.max(0, select.selectedIndex);
      const {name, count} = parts(select.options[index] ? select.options[index].textContent : '');
      current.replaceChildren();
      const nameEl = document.createElement('span');
      nameEl.className = 'picker-name';
      nameEl.textContent = name;
      current.append(nameEl);
      if (count) {
        const countEl = document.createElement('span');
        countEl.className = 'picker-count';
        countEl.textContent = count;
        current.append(countEl);
      }
      items.forEach((li, i) => li.setAttribute('aria-selected', String(i === index)));
    }
    function highlight(index) {
      active = Math.max(0, Math.min(items.length - 1, index));
      items.forEach((li, i) => li.classList.toggle('active', i === active));
      list.setAttribute('aria-activedescendant', items[active].id);
      const top = items[active].offsetTop, bottom = top + items[active].offsetHeight;
      if (top < list.scrollTop) list.scrollTop = top - 6;
      else if (bottom > list.scrollTop + list.clientHeight) list.scrollTop = bottom - list.clientHeight + 6;
    }
    function open() {
      if (!list.hidden) return;
      pickers.forEach(other => other !== picker && other.close());
      list.hidden = false;
      box.classList.add('open');
      button.setAttribute('aria-expanded', 'true');
      highlight(Math.max(0, select.selectedIndex));
      list.focus({preventScroll: true});
    }
    function close(focusButton) {
      if (list.hidden) return;
      list.hidden = true;
      box.classList.remove('open');
      button.setAttribute('aria-expanded', 'false');
      list.removeAttribute('aria-activedescendant');
      if (focusButton) button.focus({preventScroll: true});
    }
    picker.close = close;
    function choose(index) {
      const changed = select.selectedIndex !== index;
      select.selectedIndex = index;
      close(true);
      sync();
      if (changed) select.dispatchEvent(new Event('change', {bubbles: true}));
    }

    button.addEventListener('click', () => (list.hidden ? open() : close(true)));
    button.addEventListener('keydown', event => {
      if (['ArrowDown', 'ArrowUp', 'Enter', ' '].includes(event.key)) { event.preventDefault(); open(); }
    });
    let typed = '', typedAt = 0;
    list.addEventListener('keydown', event => {
      const key = event.key;
      if (key === 'ArrowDown') highlight(active + 1);
      else if (key === 'ArrowUp') highlight(active - 1);
      else if (key === 'Home') highlight(0);
      else if (key === 'End') highlight(items.length - 1);
      else if (key === 'PageDown') highlight(active + 5);
      else if (key === 'PageUp') highlight(active - 5);
      else if (key === 'Enter' || key === ' ') choose(active);
      else if (key === 'Escape') close(true);
      else if (key === 'Tab') { close(false); return; }
      else if (key.length === 1) {
        const now = Date.now();
        typed = (now - typedAt > 700 ? '' : typed) + key.toLowerCase();
        typedAt = now;
        const found = items.findIndex(li => li.textContent.toLowerCase().startsWith(typed));
        if (found >= 0) highlight(found);
      } else return;
      event.preventDefault();
    });
    list.addEventListener('focusout', event => {
      if (!box.contains(event.relatedTarget)) close(false);
    });
    sync();
    pickers.push(picker);
  }

  document.querySelectorAll('.school-picker select').forEach(build);
  document.addEventListener('pointerdown', event => {
    pickers.forEach(picker => { if (!picker.box.contains(event.target)) picker.close(false); });
  });

  const baseUpdateSubjectUI = updateSubjectUI;
  updateSubjectUI = function () {
    const result = baseUpdateSubjectUI.apply(this, arguments);
    pickers.forEach(picker => { picker.close(false); picker.sync(); });
    return result;
  };
})();
