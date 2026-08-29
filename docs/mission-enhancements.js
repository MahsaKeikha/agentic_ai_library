(()=>{
"use strict";
const page=(location.pathname.split('/').pop()||'').toLowerCase();
const missionPages=new Set(['client-project.html','client-clinical.html','client-industrial.html','client-research.html','client-space.html']);
if(!missionPages.has(page))return;
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const runtime=$('#runtime'); if(!runtime)return;
const pageLabel={
'client-project.html':'COMMERCE OPERATIONS',
'client-clinical.html':'CLINICAL TRIAL OPERATIONS',
'client-industrial.html':'INDUSTRIAL RELIABILITY',
'client-research.html':'AGENTIC RESEARCH TEAM',
'client-space.html':'SPACE MISSION DESIGN'
}[page];

function toast(text){const old=$('.mission-toast');old?.remove();const n=document.createElement('div');n.className='mission-toast';n.textContent=text;document.body.appendChild(n);setTimeout(()=>n.remove(),2200)}
function download(name,text,type='application/json'){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([text],{type}));a.download=name;document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},0)}

const bar=document.createElement('div');bar.className='mission-operator-bar';bar.innerHTML=`<div class="container"><div class="mission-operator-title"><i></i><b>${pageLabel}</b><small>operator console</small></div><button class="mission-operator-btn" data-op="tour">GUIDED TOUR</button><button class="mission-operator-btn" data-op="compare">COMPARE CASES</button><button class="mission-operator-btn" data-op="export">EXPORT TRACE</button><button class="mission-operator-btn" data-op="fullscreen">FULL SCREEN</button><span class="mission-live-clock" aria-label="Local time"></span></div><div class="mission-progress"><i></i></div>`;
const switcher=$('.mission-switcher');(switcher||$('header'))?.insertAdjacentElement('afterend',bar);
const clock=bar.querySelector('.mission-live-clock');const tick=()=>clock.textContent=new Date().toLocaleTimeString([],{hour:'2-digit',minute:'2-digit',second:'2-digit'});tick();setInterval(tick,1000);

const tools=document.createElement('div');tools.className='mission-console-tools';tools.innerHTML=`<input id="mission-trace-search" type="search" placeholder="Search trace, agent, tool, blocker..." aria-label="Search execution trace"><select id="mission-event-filter" aria-label="Filter event type"><option value="all">All events</option><option value="agent">Agent events</option><option value="tool">Tool calls</option><option value="gate">Gates / decisions</option><option value="artifact">Artifacts</option></select><button type="button" id="mission-copy-evidence">COPY EVIDENCE</button><button type="button" id="mission-clear-filter">CLEAR</button>`;
const trace=$('#trace');trace?.parentElement?.insertAdjacentElement('beforebegin',tools);

const compare=document.createElement('section');compare.className='mission-comparison';compare.hidden=true;compare.innerHTML=`<div class="mission-comparison-head"><div><span class="eyebrow">SCENARIO COMPARISON</span><h3>Compare expected system behavior before running a case.</h3></div><button class="mission-operator-btn" type="button" data-close-compare>Close</button></div><p>The three scenarios are intentionally designed to test nominal execution, incomplete evidence, and adversarial or unsafe instructions. This panel explains what a credible system should do differently in each case.</p><div class="mission-compare-grid"><article class="mission-compare-card"><span>NOMINAL CASE</span><strong>Proceed to human gate</strong><small>Evidence is sufficient, specialist stages complete, checks pass, and the protected action remains human-controlled.</small></article><article class="mission-compare-card"><span>EDGE CASE</span><strong>Hold on missing evidence</strong><small>The workflow should expose gaps, lower confidence, preserve blockers, and avoid manufacturing facts merely to finish the run.</small></article><article class="mission-compare-card"><span>ADVERSARIAL CASE</span><strong>Block and escalate</strong><small>Requests to bypass policy, fabricate evidence, conceal findings, defeat safety controls, or cross a command-authority boundary must be denied and recorded.</small></article></div>`;
runtime.querySelector('.container')?.insertAdjacentElement('afterbegin',compare);

const nodeDetail=document.createElement('aside');nodeDetail.className='mission-node-detail';nodeDetail.hidden=true;nodeDetail.innerHTML='<header><div><span class="eyebrow">PIPELINE NODE</span><h3 id="mnd-name">Agent stage</h3></div><button type="button" aria-label="Close node details">×</button></header><dl><div><dt>System</dt><dd id="mnd-system"></dd></div><div><dt>Responsibility</dt><dd id="mnd-role"></dd></div><div><dt>Runtime state</dt><dd id="mnd-state"></dd></div><div><dt>Evidence</dt><dd>Inspect matching events in the mission trace to see the exact inputs, outputs, tools, and blockers recorded for this stage.</dd></div></dl>';
document.body.appendChild(nodeDetail);nodeDetail.querySelector('button').onclick=()=>nodeDetail.hidden=true;

function pipelineProgress(){const nodes=$$('#agent-pipeline .agent-node');if(!nodes.length)return;const done=nodes.filter(n=>n.classList.contains('done')).length;const active=nodes.some(n=>n.classList.contains('active'));const pct=Math.min(100,Math.round(((done+(active?.5:0))/nodes.length)*100));bar.querySelector('.mission-progress i').style.width=pct+'%'}
const obs=new MutationObserver(()=>{pipelineProgress();applyTraceFilter();bindNodes()});obs.observe(runtime,{subtree:true,childList:true,attributes:true,attributeFilter:['class']});pipelineProgress();

function bindNodes(){
  $$('#agent-pipeline .agent-node').forEach((n,i)=>{
    if(n.dataset.enhanced)return;n.dataset.enhanced='1';n.tabIndex=0;n.setAttribute('role','button');n.setAttribute('aria-label',`Inspect ${n.textContent.trim()}`);
    const open=()=>{$$('#agent-pipeline .agent-node').forEach(x=>x.classList.remove('node-selected'));n.classList.add('node-selected');const b=n.querySelector('b')?.textContent||'Agent';const strong=n.querySelector('strong')?.textContent||`Stage ${i+1}`;const small=n.querySelector('small')?.textContent||'';nodeDetail.querySelector('#mnd-name').textContent=strong;nodeDetail.querySelector('#mnd-system').textContent=b;nodeDetail.querySelector('#mnd-role').textContent=small;nodeDetail.querySelector('#mnd-state').textContent=n.classList.contains('blocked')?'BLOCKED':n.classList.contains('done')?'COMPLETED':n.classList.contains('active')?'ACTIVE':'WAITING';nodeDetail.hidden=false;};
    n.addEventListener('click',open);n.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();open()}});
  });
}bindNodes();

function traceButtons(){return $$('#trace button')}
function applyTraceFilter(){const q=($('#mission-trace-search')?.value||'').toLowerCase();const f=$('#mission-event-filter')?.value||'all';traceButtons().forEach(b=>{const t=b.textContent.toLowerCase();let type=true;if(f==='agent')type=t.includes('agent.')||t.includes('agent ');if(f==='tool')type=t.includes('tool.call')||t.includes('tool');if(f==='gate')type=t.includes('gate')||t.includes('decision')||t.includes('approval')||t.includes('authority');if(f==='artifact')type=t.includes('artifact');b.classList.toggle('trace-hidden',!(type&&(!q||t.includes(q))))})}
$('#mission-trace-search')?.addEventListener('input',applyTraceFilter);$('#mission-event-filter')?.addEventListener('change',applyTraceFilter);$('#mission-clear-filter')?.addEventListener('click',()=>{$('#mission-trace-search').value='';$('#mission-event-filter').value='all';applyTraceFilter()});
$('#mission-copy-evidence')?.addEventListener('click',async()=>{const text=$('#inspector')?.textContent||'';if(!text||text.startsWith('Select an event')){toast('Select an event first');return;}try{await navigator.clipboard.writeText(text);toast('Evidence copied')}catch{toast('Copy is unavailable in this browser')}});

function exportTrace(){const runId=$('#run-id')?.textContent||'run';const rows=traceButtons().map(b=>({event:b.querySelector('span')?.textContent||'',actor:b.querySelector('b')?.textContent||'',summary:b.querySelector('small')?.textContent||''}));const evidence=$('#inspector')?.textContent||'';const payload={exported_at:new Date().toISOString(),mission:pageLabel,page,run_id:runId,status:$('#run-status')?.textContent||'',handoffs:$('#handoffs')?.textContent||'0',tool_calls:$('#tool-calls')?.textContent||'0',blockers:$('#blockers')?.textContent||'0',visible_trace:rows,current_evidence_inspector:evidence};download(`${page.replace('.html','')}-${runId}.json`,JSON.stringify(payload,null,2));toast('Mission trace exported')}

let fs=false;function toggleFull(){const layout=runtime.querySelector('.runtime-layout')||runtime;if(!fs){layout.classList.add('mission-console-fullscreen');const exit=document.createElement('button');exit.className='mission-operator-btn mission-fullscreen-exit';exit.textContent='EXIT FULL SCREEN';exit.onclick=toggleFull;document.body.appendChild(exit);fs=true;document.body.style.overflow='hidden'}else{layout.classList.remove('mission-console-fullscreen');$('.mission-fullscreen-exit')?.remove();fs=false;document.body.style.overflow=''}}

const tourSteps=[
['Mission architecture','Start by selecting the architecture cards. Each card exposes inputs, outputs, interfaces, authority boundaries, failure behavior, and the underlying repository.','#architecture'],
['Scenario input','Choose nominal, edge, or adversarial. The cases are intentionally different so you can see the system proceed, hold, or block rather than always succeeding.','.case-control'],
['Live pipeline','Run the mission. Each node changes state as responsibility moves through the agent system. Click any node to inspect its role.','#agent-pipeline'],
['Event trace','Every material runtime event is recorded. Search or filter the trace, then click an event to see structured evidence.','#trace'],
['Human authority','Protected actions remain behind an explicit human or qualified-review gate. Automated blockers must be resolved before an eligible approval can occur.','#human-gate']
];
function tour(){let i=0;const mask=document.createElement('div');mask.className='mission-tour-mask';const card=document.createElement('div');card.className='mission-tour-card';document.body.append(mask,card);const render=()=>{const [title,copy,sel]=tourSteps[i];card.innerHTML=`<span class="eyebrow">${i+1} / ${tourSteps.length}</span><h3>${title}</h3><p>${copy}</p><div class="mission-tour-actions"><button type="button" data-tour-close>Close</button><div><button type="button" data-tour-prev ${i===0?'disabled':''}>Back</button> <button class="primary" type="button" data-tour-next>${i===tourSteps.length-1?'Finish':'Next'}</button></div></div>`;const target=$(sel);target?.scrollIntoView({behavior:'smooth',block:'center'});card.querySelector('[data-tour-close]').onclick=close;card.querySelector('[data-tour-prev]').onclick=()=>{if(i>0){i--;render()}};card.querySelector('[data-tour-next]').onclick=()=>{if(i===tourSteps.length-1)close();else{i++;render()}}};const close=()=>{mask.remove();card.remove()};mask.onclick=close;render()}

bar.querySelector('[data-op="tour"]').onclick=tour;bar.querySelector('[data-op="compare"]').onclick=()=>{compare.hidden=!compare.hidden;compare.scrollIntoView({behavior:'smooth',block:'center'})};compare.querySelector('[data-close-compare]').onclick=()=>compare.hidden=true;bar.querySelector('[data-op="export"]').onclick=exportTrace;bar.querySelector('[data-op="fullscreen"]').onclick=toggleFull;

document.addEventListener('keydown',e=>{if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();$('#mission-trace-search')?.focus()}if(e.key==='Escape'&&fs)toggleFull();});
})();