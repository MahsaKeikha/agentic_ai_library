(()=>{
'use strict';
const page=(location.pathname.split('/').pop()||'').toLowerCase();
const isLegacy=page==='atlas-mars.html';
const isSpace=page==='atlas-space.html';
if(!isLegacy&&!isSpace)return;

if(isLegacy&&window.top===window.self){
  location.replace('atlas-space.html');
  return;
}

if(isLegacy&&window.top!==window.self){
  document.querySelectorAll('a').forEach(a=>a.setAttribute('target','_top'));
}

document.title='ATLAS: SPACE | Autonomous Multi-Agent Space Operations';
const setMeta=(selector,value)=>{const el=document.querySelector(selector);if(el)el.setAttribute('content',value);};
setMeta('meta[name="description"]','ATLAS: SPACE is an executable multi-agent space operations flagship for autonomous mission coordination, robotics, habitats, logistics, digital twins, safety, evaluation, and human authority. The current public mission module is Mars Surface Operations.');
setMeta('meta[property="og:title"]','ATLAS: SPACE | Autonomous Multi-Agent Space Operations');
setMeta('meta[property="og:description"]','How far can autonomous intelligence operate when Earth cannot answer in time? Explore a tested multi-agent space operations runtime.');
setMeta('meta[property="og:url"]','https://multiagentaiatlas.com/atlas-space.html');
const canonical=document.querySelector('link[rel="canonical"]');
if(canonical)canonical.href='https://multiagentaiatlas.com/atlas-space.html';

document.querySelectorAll('a[href="atlas-mars.html"]').forEach(a=>{a.href='atlas-space.html';if(/ATLAS:\s*MARS/i.test(a.textContent))a.textContent=a.textContent.replace(/ATLAS:\s*MARS/ig,'ATLAS: SPACE');});

const badge=document.querySelector('.mars-badge');
if(badge)badge.innerHTML='<i></i>ATLAS FLAGSHIP / SPACE AUTONOMOUS OPERATIONS';
const eyebrow=document.querySelector('.mars-hero .eyebrow');
if(eyebrow)eyebrow.textContent='SPACE OPERATIONS + MULTI-AGENT AUTONOMY';
const title=document.querySelector('.mars-hero h1');
if(title)title.textContent='How far can autonomous intelligence operate when Earth cannot answer in time?';
const lede=document.querySelector('.mars-lede');
if(lede)lede.textContent='ATLAS: SPACE is a governed multi-agent operating architecture for missions where communications delay, scarce resources, robotics, habitats, logistics, model uncertainty and safety constraints must be coordinated locally. The current executable public mission module is Mars Surface Operations.';
const claim=document.querySelector('.claim-note');
if(claim)claim.textContent='Executable browser simulation with synthetic space mission telemetry. The current public module models a Mars surface habitat. No SpaceX, Tesla, xAI, NASA, or other organization affiliation is claimed. No real spacecraft, robot, habitat, life-support system, or command network is connected.';

const card=document.querySelector('.mars-command-card');
if(card){
  const label=card.querySelector(':scope > span');
  if(label)label.textContent='CURRENT MISSION MODULE / MARS SURFACE';
  const h2=card.querySelector('h2');
  if(h2)h2.textContent='SPACE OPERATIONS CONTROL';
}

const runtimeEyebrow=document.querySelector('.mars-console-title .eyebrow');
if(runtimeEyebrow)runtimeEyebrow.textContent='02 / CURRENT MODULE: MARS SURFACE OPERATIONS';
const runtimeTitle=document.querySelector('.mars-console-title h2');
if(runtimeTitle)runtimeTitle.textContent='Stress the mission. Watch the agents negotiate what happens next.';

const topology=document.querySelector('.mars-topology-section .section-heading-dark h2');
if(topology)topology.textContent='Many intelligences. Different objectives. One accountable space mission state.';

const statusBand=document.querySelector('.mars-status-band');
if(statusBand)statusBand.setAttribute('aria-label','Current space mission module status');
})();