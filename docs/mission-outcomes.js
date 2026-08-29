(()=>{
"use strict";
const page=(location.pathname.split('/').pop()||'').toLowerCase();
const supported=new Set(['client-project.html','client-clinical.html','client-industrial.html','client-research.html','client-space.html']);
if(!supported.has(page))return;
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const result=$('#execution-result');
if(!result)return;

const config={
  'client-project.html':{
    label:'CLIENT DECISION PACKAGE',
    heldTitle:'Customer case held for accountable review',
    approvedTitle:'Protected action package approved in sandbox',
    authority:'Customer support or business owner with the organization’s delegated authority',
    heldWhy:'The workflow detected unresolved evidence, policy, evaluation, or safety conditions. It preserved the case package instead of converting uncertainty into a refund or outbound customer action.',
    approvedWhy:'The automated checks reached an eligible state and the accountable reviewer approved the protected sandbox action. The decision remains attributable to the human reviewer.',
    next:'Validate the evidence package, resolve any remaining policy exception, and only then authorize the real customer or financial action through the organization’s approved systems.',
    stepsHeld:['Inspect the blocker events and supporting records in the mission trace.','Resolve missing order, policy, account, or safety evidence without inventing facts.','Have the accountable business reviewer confirm the corrected package.','Re-run the same scenario and compare the new event trace before any real action.'],
    stepsApproved:['Export the decision package and preserve the review trail.','Compare the recommendation with the organization’s actual support policy and account evidence.','Execute any real refund or outbound response only through approved authenticated business systems.','Monitor the outcome and feed reviewer corrections back into evaluation.']
  },
  'client-clinical.html':{
    label:'QUALIFIED TRIAL REVIEW PACKAGE',
    heldTitle:'Trial operation held pending qualified review',
    approvedTitle:'Trial operations package cleared for controlled follow-up',
    authority:'Principal investigator, sponsor, clinical operations, safety, data-management, IRB or ethics, or other qualified authority as applicable',
    heldWhy:'The workflow found unresolved protocol, approval, consent, training, source-data, deviation, compliance, or safety evidence. The system therefore held progression rather than fabricating or backdating trial evidence.',
    approvedWhy:'The synthetic operational evidence satisfied the demo gates and the qualified-review package was approved for the next controlled step. This is not clinical, IRB, regulatory, or medical authorization.',
    next:'Correct the source evidence through the authorized trial process, preserve audit history, obtain the required qualified review, and re-run the operational package before progression.',
    stepsHeld:['Inspect the exact protocol, consent, training, deviation, or source-data blocker in the trace.','Correct the underlying trial record through the authorized process. Never backdate, conceal, or manufacture evidence.','Route the updated package to the appropriate qualified trial authority.','Re-run the mission and confirm that the blocker clears before progression.'],
    stepsApproved:['Export and archive the operational decision package.','Verify protocol version, approval, consent, training, source-data, and deviation evidence against the authoritative trial systems.','Proceed only through the sponsor/site’s approved clinical and regulatory workflow.','Continue monitoring for deviations, data-quality issues, safety events, and required escalation.']
  },
  'client-industrial.html':{
    label:'ENGINEERING DECISION PACKAGE',
    heldTitle:'Engineering mission held for revision',
    approvedTitle:'Maintenance planning package approved for controlled follow-up',
    authority:'Qualified reliability, maintenance, controls, operations, and safety personnel under the facility’s approved procedures',
    heldWhy:'One or more engineering, evidence, controls, or safety conditions remain unresolved. The system preserved the analysis package and intentionally created no operational action, controller write, work order, interlock change, shutdown, or restart command.',
    approvedWhy:'The synthetic evidence package reached the qualified-review gate and the planning package was accepted for controlled follow-up. Approval of analysis is not permission to alter or operate physical equipment.',
    next:'Resolve the engineering evidence gap, validate the condition against real asset data and procedures, obtain qualified review, and only then decide what authorized maintenance or operational action should occur.',
    stepsHeld:['Inspect the blocker events, sensor evidence, twin state, controls review, and safety findings above.','Correct sensor quality, timestamp synchronization, model uncertainty, interlock, or hazard evidence as applicable.','Have the responsible engineer or safety owner review the revised package.','Re-run the same mission and compare the trace before any work order or equipment decision.'],
    stepsApproved:['Export the engineering package and preserve its provenance.','Compare the recommendation with inspection findings, maintenance history, OEM limits, and current operating context.','Create any real work order, shutdown, setpoint, or controls change only through authorized plant processes.','Monitor post-maintenance evidence and use the outcome to evaluate future recommendations.']
  },
  'client-research.html':{
    label:'RESEARCH DECISION PACKAGE',heldTitle:'Research mission held for revision',approvedTitle:'Research package approved for the next reviewed stage',authority:'The accountable researcher, project lead, data owner, or other qualified reviewer',heldWhy:'The workflow preserved unresolved evidence, provenance, methodological, or review blockers instead of converting them into a confident research conclusion.',approvedWhy:'The synthetic research package passed the configured review gate for the next controlled stage.',next:'Resolve the evidence or methodology gap, preserve provenance, and re-run the reviewed workflow.',stepsHeld:['Inspect the failed evidence or methodology condition.','Correct the source or analysis package without hiding uncertainty.','Obtain the required qualified review.','Re-run and compare the trace.'],stepsApproved:['Export the package.','Verify sources and assumptions.','Proceed through the approved research workflow.','Monitor downstream findings and corrections.']
  },
  'client-space.html':{
    label:'MISSION DESIGN DECISION PACKAGE',heldTitle:'Mission design held for engineering revision',approvedTitle:'Mission design package approved for the next reviewed phase',authority:'Qualified mission, systems, safety, operations, and program authorities',heldWhy:'One or more design, evidence, interface, verification, or mission-safety conditions remain unresolved. The system intentionally preserved the design package without creating an operational command or launch authority.',approvedWhy:'The synthetic mission-design package passed the configured review gates for the next controlled phase. This is not flight, launch, command, or mission authorization.',next:'Resolve the design or verification blocker, obtain the appropriate engineering review, and re-run the mission package before progression.',stepsHeld:['Inspect the failed design, interface, verification, or safety evidence.','Revise the engineering package and preserve assumptions and provenance.','Obtain the required mission or systems review.','Re-run the same case and compare the updated trace.'],stepsApproved:['Export the mission-design package.','Validate interfaces, assumptions, verification evidence, and margins.','Proceed only through the program’s authorized review and configuration process.','Continue verification and mission-risk monitoring.']
  }
}[page];
if(!config)return;

function download(name,text){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([text],{type:'application/json'}));a.download=name;document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},0)}
function isHeld(status,html){return /hold|held|block|blocked|escalat|reject|stop|denied/i.test(`${status} ${html}`)}
function currentScenario(){const select=$('#scenario');return select?.selectedOptions?.[0]?.textContent?.trim()||'Current mission scenario'}
function getMetrics(){return {run_id:$('#run-id')?.textContent?.trim()||'not started',status:$('#run-status')?.textContent?.trim()||'UNKNOWN',handoffs:$('#handoffs')?.textContent?.trim()||'0',tool_calls:$('#tool-calls')?.textContent?.trim()||'0',blockers:$('#blockers')?.textContent?.trim()||'0',events:$$('#trace button').length,scenario:currentScenario()}}
function scrollTrace(){const trace=$('#trace');trace?.scrollIntoView({behavior:'smooth',block:'center'});const search=$('#mission-trace-search');if(search){search.value='block';search.dispatchEvent(new Event('input',{bubbles:true}));setTimeout(()=>search.focus(),500)}}
function resetMission(){const reset=$('#reset-case');reset?.click();setTimeout(()=>$('.case-control')?.scrollIntoView({behavior:'smooth',block:'center'}),120)}
function compareCases(){const btn=document.querySelector('[data-op="compare"]');if(btn){btn.click();return}document.querySelector('.mission-comparison')?.scrollIntoView({behavior:'smooth',block:'center'})}
function exportPackage(held){const m=getMetrics();const payload={exported_at:new Date().toISOString(),page,mission_package:config.label,outcome:held?'HELD_FOR_REVIEW':'APPROVED_FOR_CONTROLLED_FOLLOW_UP',...m,authority_boundary:config.authority,why:held?config.heldWhy:config.approvedWhy,next_review:config.next,visible_trace:$$('#trace button').map(b=>({event:b.querySelector('span')?.textContent||'',actor:b.querySelector('b')?.textContent||'',summary:b.querySelector('small')?.textContent||''}))};download(`${page.replace('.html','')}-${m.run_id}-decision-package.json`,JSON.stringify(payload,null,2))}

function enhance(){
  if(result.hidden)return;
  if(result.querySelector('.mission-outcome-panel'))return;
  const m=getMetrics();
  const held=isHeld(m.status,result.innerHTML);
  const panel=document.createElement('section');
  panel.className=`mission-outcome-panel ${held?'outcome-held':'outcome-cleared'}`;
  panel.innerHTML=`
    <div class="mission-outcome-command">
      <div><span>${config.label}</span><h3>${held?config.heldTitle:config.approvedTitle}</h3><p>${held?config.heldWhy:config.approvedWhy}</p></div>
      <div class="mission-outcome-state"><i></i><span>${held?'HELD / HUMAN REVIEW REQUIRED':'REVIEWED / CONTROLLED FOLLOW-UP'}</span></div>
    </div>
    <div class="mission-outcome-telemetry">
      <div><span>RUN ID</span><b>${m.run_id}</b></div><div><span>SCENARIO</span><b>${m.scenario}</b></div><div><span>FINAL STATE</span><b>${m.status}</b></div><div><span>BLOCKERS</span><b>${m.blockers}</b></div><div><span>TRACE EVENTS</span><b>${m.events}</b></div>
    </div>
    <div class="mission-outcome-grid">
      <article><span>WHAT HAPPENS NEXT</span><p>${config.next}</p></article>
      <article><span>AUTHORITY BOUNDARY</span><p>${config.authority}. The AI system prepares evidence and recommendations. It does not inherit that authority.</p></article>
    </div>
    <div class="mission-revision-checklist"><span>${held?'REVISION CHECKLIST':'CONTROLLED FOLLOW-UP CHECKLIST'}</span><ol>${(held?config.stepsHeld:config.stepsApproved).map(x=>`<li>${x}</li>`).join('')}</ol></div>
    <div class="mission-outcome-actions"><button type="button" data-outcome-evidence>REVIEW BLOCKER EVIDENCE</button><button type="button" data-outcome-export>EXPORT DECISION PACKAGE</button><button type="button" data-outcome-reset>${held?'REVISE + RE-RUN':'RUN ANOTHER CASE'}</button><button type="button" data-outcome-compare>COMPARE SCENARIOS</button><a href="client-project-guide.html">IMPLEMENTATION GUIDE ↗</a></div>`;
  result.appendChild(panel);
  panel.querySelector('[data-outcome-evidence]').addEventListener('click',scrollTrace);
  panel.querySelector('[data-outcome-export]').addEventListener('click',()=>exportPackage(held));
  panel.querySelector('[data-outcome-reset]').addEventListener('click',resetMission);
  panel.querySelector('[data-outcome-compare]').addEventListener('click',compareCases);
  panel.scrollIntoView({behavior:'smooth',block:'nearest'});
}

const observer=new MutationObserver(()=>requestAnimationFrame(enhance));
observer.observe(result,{subtree:true,childList:true,attributes:true,attributeFilter:['hidden','class']});
enhance();
})();
