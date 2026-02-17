/**
 * levels.js — Level data and UI navigation.
 *
 * Builds the nav bar and scale bar from levels.json,
 * handles level switching via click and arrow keys.
 */

let levels = [];
let cur = 0;

async function loadLevels() {
  const resp = await fetch('data/levels.json');
  levels = await resp.json();
  // Parse hex color strings to integers
  levels.forEach(l => {
    l.color = parseInt(l.color, 16);
  });
  buildNav();
  buildScaleBar();
  setLevel(0);
}

function buildNav() {
  const nav = document.getElementById('nav');
  levels.forEach((l, i) => {
    const b = document.createElement('div');
    b.className = 'nb';
    b.textContent = l.title.split('=')[0].trim();
    b.addEventListener('click', () => setLevel(i));
    nav.appendChild(b);
  });
}

function buildScaleBar() {
  const bar = document.getElementById('scale-bar');
  levels.forEach((l, i) => {
    const s = document.createElement('div');
    s.className = 'sbar';
    s.id = 'sb-' + i;
    const num = parseInt(l.count.replace(/,/g, '')) || 1;
    const pct = Math.log10(num) / 11;
    s.style.height = Math.max(2, pct * 60) + 'px';
    const label = document.createElement('div');
    label.className = 'sbar-label';
    label.textContent = l.count.length > 6
      ? l.count.substring(0, 4) + '...'
      : l.count;
    s.appendChild(label);
    bar.appendChild(s);
  });
}

function setLevel(i) {
  cur = i;
  const l = levels[i];
  document.querySelectorAll('.nb').forEach((b, j) =>
    b.className = 'nb' + (j === i ? ' on' : '')
  );
  document.getElementById('ltitle').textContent = l.title;
  document.getElementById('lsub').textContent = l.sub;
  document.getElementById('ldesc').innerHTML = l.desc;
  document.getElementById('cube-count').textContent = l.count;
  document.getElementById('cube-unit').textContent = l.unit;
  document.getElementById('brain-part').innerHTML = l.brain;
  document.querySelectorAll('.sbar').forEach((s, j) => {
    s.className = 'sbar' + (j <= i ? ' on' : '');
  });
  rebuildViz(i);
}

document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight' && cur < levels.length - 1) setLevel(cur + 1);
  if (e.key === 'ArrowLeft' && cur > 0) setLevel(cur - 1);
});
