(()=>{
const dropdowns=[...document.querySelectorAll(".nav-dropdown")];
const mobileMenu=document.querySelector(".mobile-menu");
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
