"use strict";
/* Registers sw.js and shows a small "update available" banner instead of
 * silently reloading — a shot-logging form or a half-filled taste-feedback
 * form losing input on an unannounced reload would be a bad surprise. */
function showUpdateBanner(registration){
  if(document.getElementById("swUpdateBanner"))return;
  const bar=document.createElement("div");
  bar.id="swUpdateBanner";
  bar.style.cssText="position:fixed;left:0;right:0;bottom:0;z-index:300;background:#7d1d2f;color:#fff;padding:.8rem 1rem;display:flex;gap:.8rem;align-items:center;justify-content:center;flex-wrap:wrap;font:14px/1.4 system-ui,-apple-system,BlinkMacSystemFont,sans-serif;box-shadow:0 -6px 20px rgba(0,0,0,.25)";
  bar.innerHTML='<span>Új verzió érhető el.</span><button id="swUpdateBtn" style="background:#fff;color:#7d1d2f;border:0;border-radius:999px;padding:.45rem 1rem;font-weight:800;cursor:pointer">Frissítés most</button>';
  document.body.appendChild(bar);
  document.getElementById("swUpdateBtn").addEventListener("click",()=>{
    registration.waiting?.postMessage({type:"SKIP_WAITING"});
  });
}
if("serviceWorker" in navigator){
  window.addEventListener("load",()=>{
    navigator.serviceWorker.register("sw.js").then(registration=>{
      if(registration.waiting&&navigator.serviceWorker.controller)showUpdateBanner(registration);
      registration.addEventListener("updatefound",()=>{
        const newWorker=registration.installing;
        if(!newWorker)return;
        newWorker.addEventListener("statechange",()=>{
          if(newWorker.state==="installed"&&navigator.serviceWorker.controller){
            showUpdateBanner(registration);
          }
        });
      });
    }).catch(()=>{/* PWA install is an enhancement, not a hard requirement — fail silently */});
  });
  let reloaded=false;
  navigator.serviceWorker.addEventListener("controllerchange",()=>{
    if(reloaded)return;
    reloaded=true;
    location.reload();
  });
}
