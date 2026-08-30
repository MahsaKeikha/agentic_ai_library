(()=>{
const handbookHref="ai-engineering-handbooks.html";
const missionHref="client-missions.html";
const spaceHref="atlas-space.html";
const cityHref="smart-city-agentic-ai.html";
const agewellHref="agewell-city.html";
const currentPage=(location.pathname.split("/").pop()||"index.html").toLowerCase();
const dropdowns=[...document.querySelectorAll(".nav-dropdown")];
const mobileMenu=document.querySelector(".mobile-menu");

const findMenu=name=>dropdowns.find(menu=>menu.querySelector("summary")?.textContent.trim().toLowerCase().startsWith(name));
const addBefore=(panel,href,text,beforeHref)=>{if(!panel||panel.querySelector(`a[href="${href}"]`))return;const link=document.createElement("a");link.href=href;link.textContent=text;const before=beforeHref?panel.querySelector(`a[href="${beforeHref}"]`):null;if(before)panel.insertBefore(link,before);else panel.appendChild(link);};
const markActive=(panel,href,menu)=>{if(currentPage!==href)return;menu?.classList.add("group-active");const link=panel?.querySelector(`a[href="${href}"]`);link?.classList.add("active");link?.setAttribute("aria-current","page");};

const learnDropdown=findMenu("learn"),learnPanel=learnDropdown?.querySelector(".nav-dropdown-panel");
addBefore(learnPanel,handbookHref,"AI Engineering Handbooks","training.html");
markActive(learnPanel,handbookHref,learnDropdown);

const exploreDropdown=findMenu("explore"),explorePanel=exploreDropdown?.querySelector(".nav-dropdown-panel");
addBefore(explorePanel,cityHref,"Smart City Agentic AI",spaceHref);
addBefore(explorePanel,agewellHref,"AGEWELL CITY",spaceHref);
addBefore(explorePanel,spaceHref,"ATLAS: SPACE","demo-lab.html");
markActive(explorePanel,cityHref,exploreDropdown);
markActive(explorePanel,agewellHref,exploreDropdown);
markActive(explorePanel,spaceHref,exploreDropdown);

const servicesDropdown=findMenu("services"),servicesPanel=servicesDropdown?.querySelector(".nav-dropdown-panel");
addBefore(servicesPanel,missionHref,"Client Mission Controls","book.html");
markActive(servicesPanel,missionHref,servicesDropdown);

const mobilePanel=mobileMenu?.querySelector(".mobile-menu-panel");
function addMobile(labelName,href,text,beforeHref){if(!mobilePanel||mobilePanel.querySelector(`a[href="${href}"]`))return;const labels=[...mobilePanel.querySelectorAll(".mobile-menu-label")];const label=labels.find(x=>x.textContent.trim().toLowerCase()===labelName);if(!label)return;let cursor=label.nextElementSibling,before=null;while(cursor&&!cursor.classList.contains("mobile-menu-label")){if(beforeHref&&cursor.matches?.(`a[href="${beforeHref}"]`)){before=cursor;break;}cursor=cursor.nextElementSibling;}const link=document.createElement("a");link.href=href;link.textContent=text;if(before)mobilePanel.insertBefore(link,before);else label.insertAdjacentElement("afterend",link);}
addMobile("learn",handbookHref,"AI Engineering Handbooks","training.html");
addMobile("explore",cityHref,"Smart City Agentic AI",spaceHref);
addMobile("explore",agewellHref,"AGEWELL CITY",spaceHref);
addMobile("explore",spaceHref,"ATLAS: SPACE","demo-lab.html");
addMobile("services",missionHref,"Client Mission Controls","book.html");
[handbookHref,missionHref,spaceHref,cityHref,agewellHref].forEach(href=>{if(currentPage===href){const link=mobilePanel?.querySelector(`a[href="${href}"]`);link?.classList.add("active");link?.setAttribute("aria-current","page");}});

if([agewellHref,"flagships.html"].includes(currentPage)){
  if(!document.querySelector('link[href^="agewell-signature.css"]')){const css=document.createElement("link");css.rel="stylesheet";css.href="agewell-signature.css?v=20260829.1";document.head.appendChild(css);}
  if(!document.querySelector('script[src^="agewell-signature.js"]')){const s=document.createElement("script");s.src="agewell-signature.js?v=20260829.1";s.defer=true;document.body.appendChild(s);}
}

if(currentPage===agewellHref){document.querySelectorAll('.aw-arabic').forEach(node=>node.remove());}
if(currentPage===cityHref){document.querySelectorAll('.city-arabic').forEach(node=>node.closest('article')?.remove());}

const missionPages={"client-missions.html":"Overview","client-project.html":"01 Commerce","client-clinical.html":"02 Clinical","client-industrial.html":"03 Industrial","client-research.html":"04 Research","client-space.html":"05 Space"};
if(missionPages[currentPage]){
  if(!document.querySelector('link[href^="mission-suite.css"]')){const css=document.createElement("link");css.rel="stylesheet";css.href="mission-suite.css?v=20260829.3";document.head.appendChild(css);}
  if(!document.querySelector('link[href^="mission-mobile-fix.css"]')){const css=document.createElement("link");css.rel="stylesheet";css.href="mission-mobile-fix.css?v=20260829.1";document.head.appendChild(css);}
  let nav=document.querySelector(".mission-switcher");if(!nav){nav=document.createElement("nav");nav.className="mission-switcher";nav.setAttribute("aria-label","Client mission controls");const header=document.querySelector("header.nav-shell")||document.querySelector("header");header?.insertAdjacentElement("afterend",nav);}
  if(nav){const wrap=document.createElement("div");wrap.className="container";const label=document.createElement("span");label.className="suite-label";label.textContent="MISSION CONTROL SUITE";wrap.appendChild(label);Object.entries(missionPages).forEach(([href,text])=>{const a=document.createElement("a");a.href=href;a.textContent=text;if(href===currentPage){a.classList.add("active");a.setAttribute("aria-current","page");}wrap.appendChild(a);});nav.replaceChildren(wrap);}
}
if(currentPage==="client-space.html"&&!document.querySelector('link[href*="space-contrast-fix-20260829.css"]')){const css=document.createElement("link");css.rel="stylesheet";css.href="space-contrast-fix-20260829.css?v=4";document.head.appendChild(css);}
const interactiveMissionPages=new Set(["client-project.html","client-clinical.html","client-industrial.html","client-research.html","client-space.html"]);
if(interactiveMissionPages.has(currentPage)){
  if(!document.querySelector('link[href^="mission-enhancements.css"]')){const css=document.createElement("link");css.rel="stylesheet";css.href="mission-enhancements.css?v=20260829.1";document.head.appendChild(css);}
  if(!document.querySelector('script[src^="mission-enhancements.js"]')){const s=document.createElement("script");s.src="mission-enhancements.js?v=20260829.1";s.defer=true;document.body.appendChild(s);}
  if(!document.querySelector('link[href^="mission-outcomes.css"]')){const css=document.createElement("link");css.rel="stylesheet";css.href="mission-outcomes.css?v=20260829.1";document.head.appendChild(css);}
  if(!document.querySelector('script[src^="mission-outcomes.js"]')){const s=document.createElement("script");s.src="mission-outcomes.js?v=20260829.1";s.defer=true;document.body.appendChild(s);}
}

if(currentPage==="index.html"){
  const hero=document.querySelector(".hero .hero-actions");
  if(hero&&!hero.querySelector(`a[href="${agewellHref}"]`)){const a=document.createElement("a");a.className="button secondary";a.href=agewellHref;a.textContent="Run AGEWELL CITY";hero.insertBefore(a,hero.firstChild);}
  if(hero&&!hero.querySelector(`a[href="${cityHref}"]`)){const a=document.createElement("a");a.className="button secondary";a.href=cityHref;a.textContent="Run Smart City Agentic AI";hero.insertBefore(a,hero.firstChild);}
  if(hero&&!hero.querySelector(`a[href="${spaceHref}"]`)){const a=document.createElement("a");a.className="button secondary";a.href=spaceHref;a.textContent="Run ATLAS: SPACE";hero.insertBefore(a,hero.firstChild);}
}
if(currentPage===missionHref){const status=document.querySelector(".suite-status");if(status&&!document.querySelector(`.suite-hero a[href="${cityHref}"]`)){const actions=document.createElement("div");actions.className="hero-actions";actions.innerHTML=`<a class="button inverted" href="${cityHref}">Launch Smart City Agentic AI</a><a class="button ghost" href="${agewellHref}">Launch AGEWELL CITY</a><a class="button ghost" href="${spaceHref}">Launch ATLAS: SPACE</a>`;status.insertAdjacentElement("afterend",actions);}}

const closeAll=except=>dropdowns.forEach(menu=>{if(menu!==except)menu.removeAttribute("open")});
dropdowns.forEach(menu=>{menu.addEventListener("toggle",()=>{if(menu.open)closeAll(menu)});menu.querySelectorAll("a").forEach(link=>link.addEventListener("click",()=>menu.removeAttribute("open")));});
document.addEventListener("click",e=>{if(!e.target.closest(".nav-dropdown"))closeAll();});
document.addEventListener("keydown",e=>{if(e.key!=="Escape")return;const open=dropdowns.find(menu=>menu.open);closeAll();mobileMenu?.removeAttribute("open");open?.querySelector("summary")?.focus();});
mobileMenu?.querySelectorAll("a").forEach(link=>link.addEventListener("click",()=>mobileMenu.removeAttribute("open")));
window.matchMedia("(min-width: 981px)").addEventListener?.("change",()=>{closeAll();mobileMenu?.removeAttribute("open");});
})();