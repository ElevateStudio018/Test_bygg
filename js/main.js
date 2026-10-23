(function () {
  const body = document.body;
  const items = document.querySelectorAll('[data-menu]');
  const menuBtn = document.querySelector('.menu-btn');
  const desktop = window.matchMedia('(min-width: 1024px)');

  const overlay = document.createElement('div');
  overlay.className = 'nav-overlay';
  body.appendChild(overlay);

  function closeAll(except) {
    items.forEach((item) => {
      if (item === except) return;
      item.classList.remove('open');
      item.querySelector('.menu-toggle').setAttribute('aria-expanded', 'false');
    });
    if (!except) body.classList.remove('menu-open');
  }

  function toggle(item) {
    const open = !item.classList.contains('open');
    closeAll(item);
    item.classList.toggle('open', open);
    item.querySelector('.menu-toggle').setAttribute('aria-expanded', String(open));
    body.classList.toggle('menu-open', open && desktop.matches);
  }

  items.forEach((item) => {
    item.querySelector('.menu-toggle').addEventListener('click', () => toggle(item));
  });

  overlay.addEventListener('click', () => closeAll());

  menuBtn.addEventListener('click', () => {
    const open = body.classList.toggle('nav-open');
    menuBtn.setAttribute('aria-expanded', String(open));
    menuBtn.setAttribute('aria-label', open ? 'Stäng menyn' : 'Öppna menyn');
  });

  document.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape') return;
    closeAll();
    body.classList.remove('nav-open');
    menuBtn.setAttribute('aria-expanded', 'false');
  });

  // Close menus when following an in-page link
  document.querySelectorAll('.menu a').forEach((a) => {
    a.addEventListener('click', () => {
      closeAll();
      body.classList.remove('nav-open');
    });
  });

  desktop.addEventListener('change', () => {
    closeAll();
    body.classList.remove('nav-open');
  });

  // Offertformulär: bygg ett färdigt mejl eftersom sajten saknar server
  const form = document.querySelector('.quote-form');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const subject = `Offertförfrågan: ${data.get('tjanst')} – ${data.get('namn')}`;
      const body = [
        `Namn: ${data.get('namn')}`,
        `Telefon: ${data.get('telefon') || '-'}`,
        `E-post: ${data.get('epost')}`,
        `Ort: ${data.get('ort') || '-'}`,
        `Tjänst: ${data.get('tjanst')}`,
        '',
        data.get('meddelande'),
      ].join('\n');
      const note = form.querySelector('.form-note');
      note.hidden = false;
      note.textContent = `Ditt e-postprogram öppnas med förfrågan ifylld. Öppnas inget? Mejla oss på ${form.dataset.email}.`;
      window.location.href = `mailto:${form.dataset.email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    });
  }

  document.getElementById('year').textContent = new Date().getFullYear();
})();
