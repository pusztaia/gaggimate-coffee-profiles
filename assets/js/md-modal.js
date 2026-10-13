"use strict";
/* The in-page Markdown reader (recipes, changelogs, documents, knowledge base) shared by
 * index.html, documents.html and knowledge.html. Builds its own modal markup; needs esc,
 * fetchText, renderMarkdown and resolveRelativePath (profile-common.js, or index.html's
 * inline copy). Links between .md files open inside the same reader. */
let mdDocBase="";
function ensureMarkdownModal(){
  let backdrop=document.getElementById("modalBackdrop");
  if(backdrop)return backdrop;
  backdrop=document.createElement("div");
  backdrop.className="modal-backdrop";
  backdrop.id="modalBackdrop";
  backdrop.setAttribute("role","presentation");
  backdrop.innerHTML='<article class="modal" role="dialog" aria-modal="true" aria-labelledby="modalTitle"><header class="modal-head"><h2 id="modalTitle">Dokumentum</h2><button class="modal-close" id="modalClose" aria-label="Bezárás">×</button></header><div class="modal-body" id="modalBody"></div></article>';
  document.body.append(backdrop);
  backdrop.addEventListener("click",event=>{if(event.target===backdrop||event.target.closest("#modalClose"))closeModal();});
  return backdrop;
}
async function openMarkdown(file,title){
  const backdrop=ensureMarkdownModal(),body=document.getElementById("modalBody");
  document.getElementById("modalTitle").textContent=title||file;
  body.innerHTML="<p>Betöltés…</p>";backdrop.classList.add("open");document.body.style.overflow="hidden";
  try{
    body.innerHTML=renderMarkdown(await fetchText(file));mdDocBase=file;
    // images and plain links in the document are relative to the .md file, not to this page
    const relative=url=>url&&!/^([a-z]+:|\/|#)/i.test(url);
    body.querySelectorAll("img[src]").forEach(img=>{const src=img.getAttribute("src");if(relative(src))img.setAttribute("src",resolveRelativePath(file,src));});
    body.querySelectorAll("a[href]:not(.nested-md)").forEach(a=>{const href=a.getAttribute("href");if(relative(href))a.setAttribute("href",resolveRelativePath(file,href));});
  }
  catch(error){body.innerHTML=`<blockquote><strong>Nem sikerült betölteni.</strong><br>${esc(error.message)}<br><code>${esc(file)}</code></blockquote>`;}
}
function closeModal(){const backdrop=document.getElementById("modalBackdrop");if(backdrop)backdrop.classList.remove("open");document.body.style.overflow="";}
document.addEventListener("click",event=>{
  const nested=event.target.closest(".nested-md");
  if(nested){event.preventDefault();openMarkdown(resolveRelativePath(mdDocBase,nested.dataset.file),nested.textContent.trim());}
});
document.addEventListener("keydown",event=>{if(event.key==="Escape")closeModal();});
