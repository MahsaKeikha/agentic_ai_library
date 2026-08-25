const DIMENSIONS=[
{id:"reliability",label:"Reliability",weight:18,help:"Repeatable task completion and tested behavior"},
{id:"safety",label:"Safety controls",weight:18,help:"Preventive, detective, and corrective controls"},
{id:"evidence",label:"Evidence quality",weight:12,help:"Source fidelity, traceability, and claim support"},
{id:"human_oversight",label:"Human oversight",weight:14,help:"Meaningful authority, review, and escalation"},
{id:"failure_handling",label:"Failure handling",weight:12,help:"Detection, containment, rollback, and recovery"},
{id:"observability",label:"Observability",weight:10,help:"Visible decisions, handoffs, tools, and outcomes"},
{id:"security",label:"Security and permissions",weight:10,help:"Least privilege, data boundaries, and authorization"},
{id:"interoperability",label:"Interoperability",weight:6,help:"Portable interfaces and replaceable components"}];
const GATES=[
{id:"human_owner",label:"Named human owner",help:"A specific person or role is accountable for deployment and operation."},
{id:"consequential_approval",label:"Human approval for consequential actions",help:"External actions with material impact require explicit authorization."},
{id:"least_privilege",label:"Documented least privilege",help:"Agents and tools receive only the permissions required for their task."},
{id:"audit_trail",label:"Auditable activity and handoffs",help:"Agent decisions, tool calls, approvals, and handoffs can be reconstructed."},
{id:"containment",label:"Tested stop, rollback, or containment",help:"Operators can halt the system and limit damage when behavior fails."},
{id:"claim_traceability",label:"Critical claim traceability",help:"High-impact claims can be traced to inspectable evidence."}];
const evidenceLabels=["No evidence","Claim only","Documented","Repeatably tested","Independent or production evidence"];
const README_URL="https://raw.githubusercontent.com/MahsaKeikha/agentic_ai_library/main/README.md";
const DOMAIN_RANGES=[{min:1,max:30,name:"Executive and Strategy"},{min:31,max:40,name:"AI Engineering"},{min:41,max:50,name:"Software and Cloud"},{min:51,max:60,name:"Healthcare"},{min:61,max:70,name:"Neuroscience"},{min:71,max:80,name:"Robotics"},{min:81,max:90,name:"Science"},{min:91,max:100,name:"Education"},{min:101,max:110,name:"Legal and Compliance"},{min:111,max:120,name:"Manufacturing"},{min:121,max:130,name:"Marketing"},{min:131,max:140,name:"Creative and Media"},{min:141,max:150,name:"Public Sector"},{min:151,max:160,name:"Finance and Risk"},{min:161,max:170,name:"Personal Intelligence"}];
const systemSelect=document.getElementById("system-name");
const systemLoadStatus=document.getElementById("system-load-status");
const selectedSystemRepo=document.getElementById("selected-system-repo");
let atlasSystems=[];
function parseAtlasSystems(markdown){
const entries=[],seen=new Set();
for(const line of markdown.split("\n")){
const match=line.match(/^\|\s*\*\*(F\d{2,3})\*\*\s*\|\s*\*\*(.*?)\*\*\s*\|.*?\((https:\/\/github\.com\/MahsaKeikha\/[^)]+)\)/)||line.match(/^\|\s*(F\d{2,3})\s*\|\s*(.*?)\s*\|.*?\((https:\/\/github\.com\/MahsaKeikha\/[^)]+)\)/);
if(!match)continue;
const id=match[1].trim(),name=match[2].replace(/\*\*/g,"").trim(),repository=match[3].trim();
if(seen.has(id))continue;
seen.add(id);entries.push({id,name,repository});
}
return entries.sort((a,b)=>Number(a.id.slice(1))-Number(b.id.slice(1)));
}
function selectedSystem(){
return atlasSystems.find(system=>systemSelect.value===system.id+" "+system.name);
}
function updateSelectedSystem(syncUrl=false){
const system=selectedSystem();
selectedSystemRepo.hidden=!system;
if(system)selectedSystemRepo.href=system.repository;
if(syncUrl){
const url=new URL(location.href);
if(system)url.searchParams.set("system",system.id+" "+system.name);else url.searchParams.delete("system");
history.replaceState(null,"",url);
}
}
async function loadAtlasSystems(preset){
try{
const response=await fetch(README_URL,{cache:"no-store"});
if(!response.ok)throw new Error("Repository list unavailable");
atlasSystems=parseAtlasSystems(await response.text());
if(atlasSystems.length<150)throw new Error("Complete repository list unavailable");
systemSelect.innerHTML='<option value="">Select a repository from F01 to F170</option>';
for(const range of DOMAIN_RANGES){
const group=document.createElement("optgroup");group.label=range.name;
for(const system of atlasSystems.filter(item=>{const n=Number(item.id.slice(1));return n>=range.min&&n<=range.max})){
const option=document.createElement("option");option.value=system.id+" "+system.name;option.textContent=system.id+" | "+system.name;group.appendChild(option);
}
systemSelect.appendChild(group);
}
systemSelect.disabled=false;
systemLoadStatus.textContent=atlasSystems.length+" repositories available";
const presetId=(preset||"").match(/F\d{2,3}/i)?.[0].toUpperCase();
const initial=atlasSystems.find(system=>system.id===presetId)||atlasSystems.find(system=>(system.id+" "+system.name).toLowerCase()===(preset||"").toLowerCase());
if(initial)systemSelect.value=initial.id+" "+initial.name;
updateSelectedSystem(false);
}catch(error){
console.error(error);
systemSelect.innerHTML='<option value="">Repository list could not be loaded</option>';
systemLoadStatus.textContent="Repository list unavailable. Please refresh the page.";
selectedSystemRepo.hidden=false;selectedSystemRepo.href="atlas.html";selectedSystemRepo.textContent="Open the 170 Systems Atlas";
}
}
const dimensionList=document.getElementById("dimension-list");
const gateList=document.getElementById("gate-list");
const form=document.getElementById("verification-form");
const verificationShell=document.getElementById("verification-shell");
const formStatus=document.getElementById("verification-form-status");
const verificationResult=document.getElementById("verification-result");
function clamp(value,min,max){return Math.min(max,Math.max(min,Number(value)||0))}
function adjustedScore(score,evidence){let value=clamp(score,0,5),level=clamp(evidence,0,4);if(level<2&&value>3)value=3;if(level<3&&value>4)value=4;return value}
function baseLevel(score){if(score>=90)return"Gold";if(score>=80)return"Verified";if(score>=65)return"Assessed";if(score>=40)return"Developing";return"Not Ready"}
function renderForm(){
dimensionList.innerHTML=DIMENSIONS.map(d=>`<div class="dimension-row"><div class="dimension-title"><strong>${d.label}</strong><small>${d.help} · Weight ${d.weight}%</small></div><div><label for="score-${d.id}">Score 0 to 5</label><input id="score-${d.id}" type="number" min="0" max="5" step="0.1" value="3" required></div><div><label for="evidence-${d.id}">Evidence</label><select id="evidence-${d.id}">${evidenceLabels.map((label,i)=>`<option value="${i}" ${i===2?"selected":""}>${label}</option>`).join("")}</select></div></div>`).join("");
gateList.innerHTML=GATES.map(g=>`<label class="gate-row"><input id="gate-${g.id}" type="checkbox"><span><strong>${g.label}</strong><small>${g.help}</small></span></label>`).join("");
}
function assess(){
const details=DIMENSIONS.map(d=>{const raw=clamp(document.getElementById(`score-${d.id}`).value,0,5),evidence=clamp(document.getElementById(`evidence-${d.id}`).value,0,4),adjusted=adjustedScore(raw,evidence);return{...d,raw,evidence,adjusted,points:(adjusted/5)*d.weight}});
const score=Number(details.reduce((sum,d)=>sum+d.points,0).toFixed(2));
const failed=GATES.filter(g=>!document.getElementById(`gate-${g.id}`).checked);
let level=baseLevel(score);
if(failed.length>=3&&["Gold","Verified","Assessed"].includes(level))level="Developing";
else if(failed.length&&["Gold","Verified"].includes(level))level="Assessed";
return{systemName:document.getElementById("system-name").value.trim()||"Unnamed system",score,level,details,failed};
}
function show(result){
verificationResult.hidden=false;
verificationShell.classList.remove("result-pending");
formStatus.className="verification-form-status is-success";
formStatus.textContent="Verification result calculated for "+result.systemName+".";
document.getElementById("verification-score").textContent=result.score;
document.getElementById("verification-level").textContent=result.level;
document.getElementById("verification-summary").textContent=`${result.systemName} received an evidence-adjusted score of ${result.score}. This self-assessment indicates ${result.level} readiness under version 0.1 of the public standard.`;
const gate=document.getElementById("gate-status");
gate.className=`gate-status ${result.failed.length?"is-fail":"is-pass"}`;
gate.textContent=result.failed.length?`${result.failed.length} hard gate${result.failed.length===1?"":"s"} failed. Certification eligibility is capped.`:"All six hard gates passed.";
document.getElementById("dimension-breakdown").innerHTML=result.details.map(d=>`<div class="breakdown-row"><span>${d.label}</span><strong>${d.points.toFixed(1)} / ${d.weight}</strong></div>`).join("");
document.getElementById("verification-result").dataset.copy=`${result.systemName}: ${result.score}/100, ${result.level}. Hard gates: ${result.failed.length?"failed "+result.failed.map(g=>g.label).join(", "):"all passed"}. Multi-Agent System Verification Standard v0.1.`;
}
renderForm();
const preset=new URLSearchParams(location.search).get("system");
loadAtlasSystems(preset);
systemSelect.addEventListener("change",()=>updateSelectedSystem(true));
form.addEventListener("submit",event=>{
event.preventDefault();
formStatus.className="verification-form-status";
formStatus.textContent="";
if(!selectedSystem()){
formStatus.className="verification-form-status is-error";
formStatus.textContent="Choose one repository from the F01 to F170 list before calculating.";
systemSelect.focus();
systemSelect.scrollIntoView({behavior:"smooth",block:"center"});
return;
}
const invalidScore=DIMENSIONS.map(d=>document.getElementById("score-"+d.id)).find(input=>input.value===""||Number(input.value)<0||Number(input.value)>5);
if(invalidScore){
formStatus.className="verification-form-status is-error";
formStatus.textContent="Every dimension needs a score from 0 to 5.";
invalidScore.focus();
invalidScore.scrollIntoView({behavior:"smooth",block:"center"});
return;
}
show(assess());
requestAnimationFrame(()=>verificationResult.scrollIntoView({behavior:"smooth",block:"start"}));
});
document.getElementById("reset-verification").addEventListener("click",()=>{const chosenSystem=systemSelect.value;form.reset();systemSelect.value=chosenSystem;updateSelectedSystem(false);verificationResult.hidden=true;verificationShell.classList.add("result-pending");formStatus.className="verification-form-status";formStatus.textContent="Assessment reset. Your selected repository was preserved.";document.getElementById("verification-score").textContent="0";document.getElementById("verification-level").textContent="Not assessed";document.getElementById("verification-summary").textContent="Complete the assessment to see the evidence-adjusted score and gate status.";document.getElementById("gate-status").textContent="Hard gates not yet evaluated";document.getElementById("gate-status").className="gate-status";document.getElementById("dimension-breakdown").innerHTML=""});
document.getElementById("copy-verification").addEventListener("click",async event=>{const text=document.getElementById("verification-result").dataset.copy;if(!text)return;try{await navigator.clipboard.writeText(text);event.currentTarget.textContent="Result copied";setTimeout(()=>event.currentTarget.textContent="Copy result",1600)}catch{event.currentTarget.textContent="Copy unavailable"}});
