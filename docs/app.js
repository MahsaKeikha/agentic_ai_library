const questions=[
['Agent roles are explicit, non-overlapping, and include prohibited authority.','specialization'],
['The system has defined escalation paths for ambiguous or high-impact decisions.','specialization'],
['Orchestration, handoffs, retries, and failure states are explicit and testable.','orchestration'],
['Agent disagreement or unavailable dependencies have deterministic fallback behavior.','orchestration'],
['External tools use structured inputs, validation, least privilege, and bounded side effects.','controls'],
['Consequential tool actions are separated from ordinary analytical actions.','controls'],
['Memory has explicit scope, retention, correction, deletion, and sensitive-data rules.','memory'],
['Material memory or retrieved evidence retains source and provenance.','memory'],
['The system has repeatable held-out tests that cover normal and failure paths.','evaluation'],
['Adversarial tests include prompt injection, corrupted context, stale evidence, and tool failures.','evaluation'],
['Traces capture agent outputs, tool calls, approvals, errors, and external actions.','observability'],
['Operators can identify, investigate, and reconstruct failed workflows.','observability'],
['Security and privacy controls include least privilege, secret protection, and data minimization.','security'],
['The system has tested controls for prompt injection, privilege escalation, and unsafe tool use.','security'],
['Protected actions are formally defined and cannot execute outside their authorization model.','authority'],
['Human approvals are meaningful, attributable, and placed before consequential execution.','authority'],
['Material claims and decisions preserve evidence lineage, assumptions, and decision records.','provenance'],
['The system can distinguish known facts, model inference, external evidence, and unresolved uncertainty.','provenance'],
['Release criteria, rollback, incident response, ownership, and regression controls are documented.','lifecycle'],
['Production changes are monitored and reevaluated when models, tools, prompts, policies, or dependencies change.','lifecycle']
];

const labels=['No evidence','Ad hoc','Partial','Managed','Strong'];
const form=document.getElementById('readiness-form');
questions.forEach((q,i)=>{
  const wrap=document.createElement('div');wrap.className='question';
  wrap.innerHTML=`<p>${i+1}. ${q[0]}</p><div class="options">${labels.map((l,v)=>`<label><input type="radio" name="q${i}" value="${v}" ${v===0?'required':''}><span>${v} · ${l}</span></label>`).join('')}</div>`;
  form.appendChild(wrap);
});
const btn=document.createElement('button');btn.type='submit';btn.className='button primary score-button';btn.textContent='Calculate readiness score';form.appendChild(btn);
form.addEventListener('submit',e=>{
  e.preventDefault();let total=0;
  questions.forEach((_,i)=>{const v=form.querySelector(`input[name=q${i}]:checked`);total+=Number(v?.value||0)});
  const score=Math.round(total/80*100);
  let band='Experimental',summary='The system appears early-stage. Focus first on explicit agent boundaries, deterministic authority controls, repeatable evaluation, and basic traceability before expanding autonomy.';
  if(score>=90){band='Gold Standard Candidate';summary='The self-assessment indicates high engineering maturity. A formal evidence review should verify that critical controls, protected actions, adversarial evaluations, and production operations actually perform as claimed.'}
  else if(score>=75){band='Production Candidate';summary='The system shows meaningful production-oriented maturity. Identify the weakest dimensions, verify critical blockers, and strengthen evidence before consequential deployment.'}
  else if(score>=60){band='Managed';summary='The architecture has useful controls but still contains material maturity gaps. Prioritize authority boundaries, adversarial evaluation, observability, memory governance, and incident readiness.'}
  else if(score>=40){band='Emerging';summary='The system has some structured practices but remains inconsistent. Standardize orchestration, permissions, evaluation, provenance, and human approval before increasing autonomy.'}
  document.getElementById('score-number').textContent=score;
  document.getElementById('score-band').textContent=band;
  document.getElementById('score-summary').textContent=summary;
  const shell=document.getElementById('result-shell');shell.hidden=false;shell.scrollIntoView({behavior:'smooth',block:'center'});
});