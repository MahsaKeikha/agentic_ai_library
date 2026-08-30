(()=>{
'use strict';
const page=(location.pathname.split('/').pop()||'index.html').toLowerCase();
const signatureHref='agewell-city.html';

function addOriginStory(){
  if(page!==signatureHref||document.querySelector('.agewell-signature-origin'))return;
  const intro=document.querySelector('.aw-intro');
  if(!intro)return;
  const section=document.createElement('section');
  section.className='agewell-signature-origin';
  section.innerHTML=`<div class="container agewell-origin-grid"><div class="agewell-origin-copy"><span class="agewell-origin-badge">SIGNATURE FLAGSHIP / BUILT FROM A REAL CARE VISION</span><h2>Connected Care was the beginning. AGEWELL CITY expands the idea from one home to an entire human environment.</h2><p>Connected Care began with a practical question: how can technology help an older adult remain safer, more independent and more connected while reducing the coordination burden around everyday care? AGEWELL CITY carries that same idea beyond the home. It treats housing, mobility, caregivers, assisted living, community services, accessibility and city infrastructure as one connected human experience.</p><div class="agewell-lineage"><article><span>CONNECTED CARE</span><div><strong>Start with the person at home</strong><p>Understand daily patterns, support caregivers, surface changes that deserve attention and preserve the person's dignity.</p></div></article><article><span>AGEWELL CITY</span><div><strong>Extend intelligence into the community</strong><p>Coordinate home, accessible mobility, assisted living, buildings, community services and authorized care support around the resident.</p></div></article><article><span>AGEWELL 01</span><div><strong>Build the first real pilot</strong><p>Connect one community or age friendly district in read only mode first, prove the shared state, then add a small number of reversible support actions.</p></div></article></div></div><aside class="agewell-manifesto"><span>THE IDEA I WANT THIS FLAGSHIP TO PROVE</span><blockquote>Living longer should not mean surrendering more of your independence to institutions, software or surveillance.</blockquote><p>The most powerful version of AGEWELL CITY is not the one that watches an older person most closely. It is the one that coordinates the environment so well that the person can keep living more of the life they choose.</p><div class="agewell-difference"><div><b>NOT SURVEILLANCE</b><small>Consent, purpose limits and minimum necessary data.</small></div><div><b>NOT MEDICAL AUTOMATION</b><small>Observation, coordination and escalation without replacing qualified care.</small></div><div><b>NOT ONE INSTITUTION</b><small>Support can follow a person across home, community and assisted living.</small></div><div><b>NOT A DASHBOARD ONLY</b><small>Executable coordination, tool limits, evidence and human authority.</small></div></div></aside></div>`;
  intro.insertAdjacentElement('beforebegin',section);

  const badge=document.querySelector('.aw-badge');
  if(badge)badge.innerHTML='<i></i>ATLAS SIGNATURE FLAGSHIP / HUMAN CENTERED AGING';
}

function addFlagshipFeature(){
  if(page!=='flagships.html'||document.querySelector('.agewell-signature-card'))return;
  const hero=document.querySelector('.flagship-hero');
  if(!hero)return;
  const card=document.createElement('section');
  card.className='agewell-signature-card';
  card.innerHTML=`<div class="sig-mark"><span>SIGNATURE FLAGSHIP</span><strong>AGEWELL</strong><small>Independent living + assisted living + age friendly city intelligence</small></div><div class="sig-copy"><span class="agewell-signature-ribbon">CONNECTED CARE → AGEWELL CITY → AGEWELL 01</span><h2>Design the intelligent city around a longer human life.</h2><p>AGEWELL CITY coordinates independent living, assisted living, accessible mobility, caregivers, community services, home environment and privacy around the resident. It is deliberately designed to support independence without turning aging into surveillance or giving software clinical authority.</p><div class="sig-actions"><a class="primary" href="agewell-city.html">Launch AGEWELL CITY</a><a href="AGEWELL_CITY_REAL_WORLD_PILOT.md">Read AGEWELL 01 pilot</a></div></div>`;
  hero.insertAdjacentElement('afterend',card);
}

addOriginStory();
addFlagshipFeature();
})();