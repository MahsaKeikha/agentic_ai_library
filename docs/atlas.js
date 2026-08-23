const DOMAIN_RANGES = [
  { min: 1, max: 30, name: 'Executive & Strategy' },
  { min: 31, max: 40, name: 'AI Engineering' },
  { min: 41, max: 50, name: 'Software & Cloud' },
  { min: 51, max: 60, name: 'Healthcare' },
  { min: 61, max: 70, name: 'Neuroscience' },
  { min: 71, max: 80, name: 'Robotics' },
  { min: 81, max: 90, name: 'Science' },
  { min: 91, max: 100, name: 'Education' },
  { min: 101, max: 110, name: 'Legal & Compliance' },
  { min: 111, max: 120, name: 'Manufacturing' },
  { min: 121, max: 130, name: 'Marketing' },
  { min: 131, max: 140, name: 'Creative & Media' },
  { min: 141, max: 150, name: 'Public Sector' },
  { min: 151, max: 160, name: 'Finance & Risk' },
  { min: 161, max: 170, name: 'Personal Intelligence' }
];

const README_URL = 'https://raw.githubusercontent.com/MahsaKeikha/agentic_ai_library/main/README.md';
const grid = document.getElementById('atlas-grid');
const filters = document.getElementById('atlas-filters');
const search = document.getElementById('atlas-search');
const count = document.getElementById('atlas-result-count');
const total = document.getElementById('atlas-total');
const empty = document.getElementById('atlas-empty');
const error = document.getElementById('atlas-error');
const reset = document.getElementById('atlas-reset');

let systems = [];
let activeDomain = 'All';

function domainFor(id) {
  const n = Number(id.replace('F', ''));
  return DOMAIN_RANGES.find(d => n >= d.min && n <= d.max)?.name || 'Other';
}

function parseReadme(markdown) {
  const entries = [];
  const lines = markdown.split('\n');
  const seen = new Set();

  for (const line of lines) {
    const match = line.match(/^\|\s*\*\*(F\d{2,3})\*\*\s*\|\s*\*\*(.*?)\*\*\s*\|.*?\((https:\/\/github\.com\/MahsaKeikha\/[^)]+)\)/)
      || line.match(/^\|\s*(F\d{2,3})\s*\|\s*(.*?)\s*\|.*?\((https:\/\/github\.com\/MahsaKeikha\/[^)]+)\)/);
    if (!match) continue;

    const id = match[1].trim();
    const name = match[2].replace(/\*\*/g, '').trim();
    const url = match[3].trim();
    if (seen.has(id)) continue;
    seen.add(id);
    entries.push({ id, name, url, domain: domainFor(id) });
  }

  return entries.sort((a, b) => Number(a.id.slice(1)) - Number(b.id.slice(1)));
}

function createFilters() {
  const names = ['All', ...DOMAIN_RANGES.map(d => d.name)];
  filters.innerHTML = names.map(name => `<button type="button" data-domain="${name}" class="atlas-filter${name === 'All' ? ' is-active' : ''}">${name}</button>`).join('');
  filters.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', () => {
      activeDomain = button.dataset.domain;
      filters.querySelectorAll('button').forEach(b => b.classList.toggle('is-active', b === button));
      render();
    });
  });
}

function systemCard(system) {
  return `
    <article class="atlas-card">
      <div class="atlas-card-meta">
        <span class="atlas-id">${system.id}</span>
        <span class="atlas-domain">${system.domain}</span>
      </div>
      <h2>${system.name}</h2>
      <div class="atlas-card-footer">
        <span>Standalone reference architecture</span>
        <a href="${system.url}" target="_blank" rel="noopener">Open repository →</a>
      </div>
    </article>`;
}

function render() {
  const query = search.value.trim().toLowerCase();
  const filtered = systems.filter(system => {
    const domainMatch = activeDomain === 'All' || system.domain === activeDomain;
    const queryMatch = !query || `${system.id} ${system.name} ${system.domain}`.toLowerCase().includes(query);
    return domainMatch && queryMatch;
  });

  grid.innerHTML = filtered.map(systemCard).join('');
  count.textContent = `${filtered.length} of ${systems.length} systems`;
  empty.hidden = filtered.length !== 0;
}

search.addEventListener('input', render);
reset.addEventListener('click', () => {
  search.value = '';
  activeDomain = 'All';
  filters.querySelectorAll('button').forEach(b => b.classList.toggle('is-active', b.dataset.domain === 'All'));
  render();
});

async function init() {
  createFilters();
  try {
    const response = await fetch(README_URL, { cache: 'no-store' });
    if (!response.ok) throw new Error(`GitHub returned ${response.status}`);
    const markdown = await response.text();
    systems = parseReadme(markdown);
    if (systems.length < 150) throw new Error(`Only ${systems.length} systems parsed`);
    total.textContent = systems.length;
    render();
  } catch (err) {
    console.error(err);
    count.textContent = 'Catalog unavailable';
    error.hidden = false;
  }
}

init();
