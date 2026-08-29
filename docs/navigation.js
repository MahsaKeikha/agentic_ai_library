(()=>{
const handbookHref="ai-engineering-handbooks.html";
const missionHref="client-missions.html";
const currentPage=(location.pathname.split("/").pop()||"index.html").toLowerCase();
const dropdowns=[...document.querySelectorAll(".nav-dropdown")];
const mobileMenu=document.querySelector(".mobile-menu");

const learnDropdown=dropdowns.find(menu=>menu.querySelector("summary")?.textContent.trim().toLowerCase().startsWith("learn"));
const learnPanel=learnDropdown?.querySelector(".nav-dropdown-panel");
if(learnPanel&&!learnPanel.querySelector(`a[href="${handbookHref}"]`)){
  const link=document.createElement("a");link.href=handbookHref;link.textContent="AI Engineering Handbooks";const training=learnPanel.querySelector('a[href="training.html"]');if(training)learnPanel.insertBefore(link,training);else learnPanel.appendChild(link);
}
if(currentPage===handbookHref){learnDropdown?.classList.add("group-active");const desktopLink=learnPanel?.querySelector(`a[href="${handbookHref}"]`);desktopLink?.classList.add("active");desktopLink?.setAttribute("aria-current","page");}

const servicesDropdown=dropdowns.find(menu=>menu.querySelector("summary")?.textContent.trim().toLowerCase().startsWith("services"));
const servicesPanel=servicesDropdown?.querySelector(".nav-dropdown-panel");
if(servicesPanel&&!servicesPanel.querySelector(`a[href="${missionHref}"]`)){
  const link=document.createElement("a");link.href=missionHref;link.textContent="Client Mission Controls";const booking=servicesPanel.querySelector('a[href="book.html"]');if(booking)servicesPanel.insertBefore(link,booking);else servicesPanel.appendChild(link);
}
if(currentPage===missionHref){servicesDropdown?.classList.add("group-active");const link=servicesPanel?.querySelector(`a[href="${missionHref}"]`);link?.classList.add("active");link?.setAttribute("aria-current","page");}

const mobilePanel=mobileMenu?.querySelector(".mobile-menu-panel");
if(mobilePanel&&!mobilePanel.querySelector(`a[href="${handbookHref}"]`)){
  const labels=[...mobilePanel.querySelectorAll(".mobile-menu-label")];const learnLabel=labels.find(label=>label.textContent.trim().toLowerCase()==="learn");if(learnLabel){let cursor=learnLabel.nextElementSibling,training=null;while(cursor&&!cursor.classList.contains("mobile-menu-label")){if(cursor.matches?.('a[href="training.html"]')){training=cursor;break;}cursor=cursor.nextElementSibling;}const link=document.createElement("a");link.href=handbookHref;link.textContent="AI Engineering Handbooks";if(training)mobilePanel.insertBefore(link,training);else learnLabel.insertAdjacentElement("afterend",link);}
}
if(mobilePanel&&!mobilePanel.querySelector(`a[href="${missionHref}"]`)){
  const labels=[...mobilePanel.querySelectorAll(".mobile-menu-label")];const servicesLabel=labels.find(label=>label.textContent.trim().toLowerCase()==="services");if(servicesLabel){let cursor=servicesLabel.nextElementSibling,booking=null;while(cursor&&!cursor.classList.contains("mobile-menu-label")){if(cursor.matches?.('a[href="book.html"]')){booking=cursor;break;}cursor=cursor.nextElementSibling;}const link=document.createElement("a");link.href=missionHref;link.textContent="Client Mission Controls";if(booking)mobilePanel.insertBefore(link,booking);else servicesLabel.insertAdjacentElement("afterend",link);}
}
if(currentPage===handbookHref){const mobileLink=mobilePanel?.querySelector(`a[href="${handbookHref}"]`);mobileLink?.classList.add("active");mobileLink?.setAttribute("aria-current","page");}
if(currentPage===missionHref){const mobileLink=mobilePanel?.querySelector(`a[href="${missionHref}"]`);mobileLink?.classList.add("active");mobileLink?.setAttribute("aria-current","page");}

const missionPages={"client-missions.html":"Overview","client-project.html":"01 Commerce","client-clinical.html":"02 Clinical","client-industrial.html":"03 Industrial","client-research.html":"04 Research","client-space.html":"05 Space"};
if(missionPages[currentPage]){
  if(!document.querySelector('link[href^="mission-suite.css"]')){const css=document.createElement("link");css.rel="stylesheet";css.href="mission-suite.css?v=20260829.3";document.head.appendChild(css);}
  let nav=document.querySelector(".mission-switcher");if(!nav){nav=document.createElement("nav");nav.className="mission-switcher";nav.setAttribute("aria-label","Client mission controls");const header=document.querySelector("header.nav-shell")||document.querySelector("header");header?.insertAdjacentElement("afterend",nav);}
  if(nav){const wrap=document.createElement("div");wrap.className="container";const label=document.createElement("span");label.className="suite-label";label.textContent="MISSION CONTROL SUITE";wrap.appendChild(label);Object.entries(missionPages).forEach(([href,text])=>{const a=document.createElement("a");a.href=href;a.textContent=text;if(href===currentPage){a.classList.add("active");a.setAttribute("aria-current","page");}wrap.appendChild(a);});nav.replaceChildren(wrap);}
}

const interactiveMissionPages=new Set(["client-project.html","client-clinical.html","client-industrial.html","client-research.html","client-space.html"]);
if(interactiveMissionPages.has(currentPage)){
  if(!document.querySelector('link[href^="mission-enhancements.css"]')){const css=document.createElement("link");css.rel="stylesheet";css.href="mission-enhancements.css?v=20260829.1";document.head.appendChild(css);}
  if(!document.querySelector('script[src^="mission-enhancements.js"]')){const script=document.createElement("script");script.src="mission-enhancements.js?v=20260829.1";script.defer=true;document.body.appendChild(script);}
}

const closeAll=except=>dropdowns.forEach(menu=>{if(menu!==except)menu.removeAttribute("open")});
dropdowns.forEach(menu=>{menu.addEventListener("toggle",()=>{if(menu.open)closeAll(menu)});menu.querySelectorAll("a").forEach(link=>link.addEventListener("click",()=>menu.removeAttribute("open")));});document.addEventListener("click",event=>{if(!event.target.closest(".nav-dropdown"))closeAll()});document.addEventListener("keydown",event=>{if(event.key!=="Escape")return;const openMenu=dropdowns.find(menu=>menu.open);closeAll();mobileMenu?.removeAttribute("open");openMenu?.querySelector("summary")?.focus();});
mobileMenu?.querySelectorAll("a").forEach(link=>link.addEventListener("click",()=>mobileMenu.removeAttribute("open")));const desktopView=window.matchMedia("(min-width: 981px)");desktopView.addEventListener?.("change",()=>{closeAll();mobileMenu?.removeAttribute("open")});
})();