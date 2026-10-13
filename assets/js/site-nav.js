"use strict";
/* The site's main navigation, the same on every page: renders the menu into the page's
 * .topbar-inner (after .brand), the ☰ button into .topbar-end and the narrow-screen menu
 * dialog. The links live only here. Links of the form index.html#x become in-page anchors on index.html. */
(function(){
  const LINKS=[
    {label:"Profilkatalógus",href:"index.html"},
    {label:"Profilkereső",href:"finder.html"},
    {label:"Összehasonlítás",href:"compare.html"},
    {label:"Kávévíz",href:"water.html"},
    {label:"Dokumentáció",href:"documents.html"},
    {label:"Tudásbázis",href:"knowledge.html"},
    {label:"Új profil",href:"add-profile.html"}
  ];
  const inner=document.querySelector(".topbar-inner");
  if(!inner)return;
  const page=(location.pathname.split("/").pop()||"index.html").toLowerCase();
  const onIndex=page==="index.html";
  const hrefFor=link=>onIndex&&link.href.startsWith("index.html#")?link.href.slice("index.html".length):link.href;
  const isCurrent=link=>link.href.toLowerCase()===page;
  const esc=value=>String(value).replace(/[&<>"']/g,ch=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[ch]));
  const linksHTML=()=>LINKS.map(link=>`<a href="${esc(hrefFor(link))}"${isCurrent(link)?' aria-current="page"':""}>${esc(link.label)}</a>`).join("");

  const nav=document.createElement("nav");
  nav.className="site-nav";
  nav.setAttribute("aria-label","Fő navigáció");
  nav.innerHTML=linksHTML();
  const anchor=inner.querySelector(".home-link")||inner.querySelector(".brand");  // brew keeps its back link next to the brand
  if(anchor)anchor.after(nav);else inner.prepend(nav);

  let end=inner.querySelector(".topbar-end");
  if(!end){end=document.createElement("div");end.className="topbar-end";inner.append(end);}
  const menuBtn=document.createElement("button");
  menuBtn.type="button";
  menuBtn.className="icon-btn site-menu-btn";
  menuBtn.setAttribute("aria-label","Menü megnyitása");
  menuBtn.setAttribute("aria-haspopup","dialog");
  menuBtn.setAttribute("aria-expanded","false");
  menuBtn.setAttribute("aria-controls","siteMenu");
  menuBtn.title="Menü";
  menuBtn.textContent="☰";
  end.prepend(menuBtn);

  const dialog=document.createElement("dialog");
  dialog.id="siteMenu";
  dialog.className="site-menu";
  dialog.setAttribute("aria-label","Fő navigáció");
  dialog.innerHTML=`<div class="site-menu-head"><strong>Menü</strong><button type="button" class="icon-btn site-menu-close" aria-label="Bezárás">×</button></div><nav class="site-menu-links">${linksHTML()}</nav>`;
  document.body.append(dialog);

  menuBtn.addEventListener("click",()=>{dialog.showModal();menuBtn.setAttribute("aria-expanded","true");});
  dialog.addEventListener("close",()=>{menuBtn.setAttribute("aria-expanded","false");menuBtn.focus();});
  dialog.addEventListener("click",event=>{if(event.target===dialog)dialog.close();});
  dialog.querySelector(".site-menu-close").addEventListener("click",()=>dialog.close());
  dialog.querySelectorAll("a").forEach(a=>a.addEventListener("click",()=>dialog.close()));
})();
