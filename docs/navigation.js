(()=>{
const handbookHref="ai-engineering-handbooks.html";
const currentPage=(location.pathname.split("/").pop()||"index.html").toLowerCase();
const dropdowns=[...document.querySelectorAll(".nav-dropdown")];
const mobileMenu=document.querySelector(".mobile-menu");

const learnDropdown=dropdowns.find(menu=>menu.querySelector("summary")?.textContent.trim().toLowerCase().startsWith("learn"));
const learnPanel=learnDropdown?.querySelector(".nav-dropdown-panel");
if(learnPanel&&!learnPanel.querySelector(`a[href="${handbookHref}"]`)){
  const link=document.createElement("a");
  link.href=handbookHref;
  link.textContent="AI Engineering Handbooks";
  const training=learnPanel.querySelector('a[href="training.html"]');
  if(training)learnPanel.insertBefore(link,training);else learnPanel.appendChild(link);
}
if(currentPage===handbookHref){
  learnDropdown?.classList.add("group-active");
  const desktopLink=learnPanel?.querySelector(`a[href="${handbookHref}"]`);
  desktopLink?.classList.add("active");
  desktopLink?.setAttribute("aria-current","page");
}

const mobilePanel=mobileMenu?.querySelector(".mobile-menu-panel");
if(mobilePanel&&!mobilePanel.querySelector(`a[href="${handbookHref}"]`)){
  const labels=[...mobilePanel.querySelectorAll(".mobile-menu-label")];
  const learnLabel=labels.find(label=>label.textContent.trim().toLowerCase()==="learn");
  if(learnLabel){
    let cursor=learnLabel.nextElementSibling;
    let training=null;
    while(cursor&&!cursor.classList.contains("mobile-menu-label")){
      if(cursor.matches?.('a[href="training.html"]')){training=cursor;break;}
      cursor=cursor.nextElementSibling;
    }
    const link=document.createElement("a");
    link.href=handbookHref;
    link.textContent="AI Engineering Handbooks";
    if(training)mobilePanel.insertBefore(link,training);else learnLabel.insertAdjacentElement("afterend",link);
  }
}
if(currentPage===handbookHref){
  const mobileLink=mobilePanel?.querySelector(`a[href="${handbookHref}"]`);
  mobileLink?.classList.add("active");
  mobileLink?.setAttribute("aria-current","page");
}

const closeAll=except=>dropdowns.forEach(menu=>{if(menu!==except)menu.removeAttribute("open")});
dropdowns.forEach(menu=>{
menu.addEventListener("toggle",()=>{if(menu.open)closeAll(menu)});
menu.querySelectorAll("a").forEach(link=>link.addEventListener("click",()=>menu.removeAttribute("open")));
});
document.addEventListener("click",event=>{if(!event.target.closest(".nav-dropdown"))closeAll()});
document.addEventListener("keydown",event=>{
if(event.key!=="Escape")return;
const openMenu=dropdowns.find(menu=>menu.open);
closeAll();
mobileMenu?.removeAttribute("open");
openMenu?.querySelector("summary")?.focus();
});
mobileMenu?.querySelectorAll("a").forEach(link=>link.addEventListener("click",()=>mobileMenu.removeAttribute("open")));
const desktopView=window.matchMedia("(min-width: 981px)");
desktopView.addEventListener?.("change",()=>{closeAll();mobileMenu?.removeAttribute("open")});
})();
