"use strict";
/* Shared, DOM-independent helpers for rendering a GaggiMate profile JSON
 * (phase list, mini SVG chart, markdown) and for resolving catalog.json
 * entry paths. Used by profile.html; index.html still carries its own
 * inline copy pending the Phase 0 asset-extraction migration step. */

function esc(value){return String(value??"").replace(/[&<>"']/g,ch=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[ch]));}

async function fetchJSON(url){
  const response=await fetch(url,{cache:"no-store"});
  if(!response.ok)throw new Error(`${response.status} ${response.statusText}`);
  return response.json();
}
async function fetchText(url){
  const response=await fetch(url,{cache:"no-store"});
  if(!response.ok)throw new Error(`${response.status} ${response.statusText}`);
  return response.text();
}

function pathFor(entry,file){return `profiles/${entry.folder}/${file}`;}
function defaultVariant(entry){return entry.variants.find(v=>v.default)||entry.variants[0];}
function hasKind(entry,kind){return entry.variants.some(v=>v.kind===kind);}
function isGeneral(entry){return entry.variants.every(v=>v.kind==="general");}
function recipeFile(entry){return `${entry.folder}-recipe.md`;}
function changelogFile(entry){return `${entry.folder}-changelog.md`;}
function pngFile(variant){return variant.file.replace(/\.json$/i,"-profile.png");}
function kindLabel(variant){
  if(variant.kind==="scale")return "Scale";
  if(variant.kind==="manual")return "Manual";
  return "Általános";
}

function formatNumber(value,digits=1){const n=Number(value);return Number.isFinite(n)?n.toLocaleString("hu-HU",{maximumFractionDigits:digits}):"—";}
function resolveTemperature(phase,root){const value=Number(phase?.temperature||0);return value===0?Number(root||0):value;}
function totalDuration(profile){return (profile?.phases||[]).reduce((sum,p)=>sum+Math.max(0,Number(p.duration)||0),0);}
function lastWeightTarget(profile){let result=null;(profile?.phases||[]).forEach(p=>(p.targets||[]).forEach(t=>{if(t?.type==="volumetric"&&Number(t.value)>0)result=Number(t.value);}));return result;}
function peakPressure(profile){let peak=0;(profile?.phases||[]).forEach(p=>{const v=Number(p?.pump?.pressure);if(Number.isFinite(v)&&v>=0)peak=Math.max(peak,v);});return peak;}

function targetText(phase){
  const parts=(phase.targets||[]).map(t=>{
    const unit={volumetric:"g",pressure:"bar",flow:"ml/s",pumped:"ml"}[t.type]||"";
    const op=t.operator==="lte"?"≤":"≥";
    return `${t.type} ${op} ${formatNumber(t.value)}${unit}`;
  });
  return parts.join(" · ");
}
function phasesHTML(profile){
  if(!profile?.phases?.length)return '<div class="phase-row"><strong>JSON betöltésre vár</strong><span>—</span><span class="target">—</span></div>';
  return profile.phases.map((p,index)=>{
    const pump=p.pump||{};
    const target=pump.target==="flow"?`${formatNumber(pump.flow)} ml/s`:`${formatNumber(pump.pressure)} bar`;
    return `<div class="phase-row"><strong>${index+1}. ${esc(p.name||"Fázis")}</strong><span>${esc(target)} · ${formatNumber(p.duration,0)} s</span><span class="target">${esc(targetText(p))}</span></div>`;
  }).join("");
}

function easing(kind,p){
  p=Math.max(0,Math.min(1,p));
  if(kind==="linear")return p;
  if(kind==="ease-in")return p*p;
  if(kind==="ease-out")return 1-(1-p)*(1-p);
  if(kind==="ease-in-out")return .5*(1-Math.cos(Math.PI*p));
  return 1;
}
function curveSeries(profile,variable){
  const phases=profile.phases||[];let t=0;let previous=0;const points=[];
  phases.forEach(phase=>{
    const d=Math.max(0,Number(phase.duration)||0),pump=phase.pump||{},value=Number(pump[variable]);
    if(pump.target!==variable||!Number.isFinite(value)||value<0){points.push([t,null],[t+d,null]);t+=d;return;}
    const tr=phase.transition||{},rd=Math.min(d,Math.max(0,Number(tr.duration)||0));
    if(tr.type&&tr.type!=="instant"&&rd>0){
      const steps=Math.max(8,Math.round(rd*4));
      for(let i=0;i<=steps;i++){const p=i/steps;points.push([t+rd*p,previous+(value-previous)*easing(tr.type,p)]);}
      points.push([t+d,value]);
    }else{points.push([t,previous],[t,value],[t+d,value]);}
    previous=value;t+=d;
  });
  return points;
}
function tempSeries(profile){
  let t=0,prev=null;const points=[];
  (profile.phases||[]).forEach(phase=>{const d=Math.max(0,Number(phase.duration)||0),value=resolveTemperature(phase,profile.temperature);if(prev!==null)points.push([t,prev]);points.push([t,value],[t+d,value]);prev=value;t+=d;});
  return points;
}
function pathData(points,xScale,yScale){
  let out="",open=false;
  points.forEach(([x,y])=>{if(y===null||!Number.isFinite(y)){open=false;return;}out+=(open?"L":"M")+xScale(x).toFixed(1)+" "+yScale(y).toFixed(1)+" ";open=true;});
  return out.trim();
}
function renderMiniChart(profile,title,accent){
  const W=760,H=260,pad={l:44,r:42,t:20,b:34},total=Math.max(1,totalDuration(profile));
  const p=curveSeries(profile,"pressure"),f=curveSeries(profile,"flow"),temp=tempSeries(profile);
  const leftVals=[...p,...f].map(v=>v[1]).filter(Number.isFinite),leftMax=Math.max(10,...leftVals)+1;
  const temps=temp.map(v=>v[1]).filter(Number.isFinite),tMin=Math.min(...temps),tMax=Math.max(...temps),tPad=tMin===tMax?1:Math.max(.6,(tMax-tMin)*.25);
  const x=v=>pad.l+(W-pad.l-pad.r)*(v/total),y=v=>H-pad.b-(H-pad.t-pad.b)*(v/leftMax),yt=v=>H-pad.b-(H-pad.t-pad.b)*((v-(tMin-tPad))/((tMax+tPad)-(tMin-tPad)));
  let bands="",cursor=0;(profile.phases||[]).forEach((phase,i)=>{const d=Math.max(0,Number(phase.duration)||0);if(i%2)bands+=`<rect x="${x(cursor)}" y="${pad.t}" width="${Math.max(0,x(cursor+d)-x(cursor))}" height="${H-pad.t-pad.b}" fill="currentColor" opacity=".035"/>`;bands+=`<line x1="${x(cursor)}" y1="${pad.t}" x2="${x(cursor)}" y2="${H-pad.b}" stroke="currentColor" opacity=".12"/>`;cursor+=d;});
  const grid=[0,.25,.5,.75,1].map(fr=>`<line x1="${pad.l}" y1="${pad.t+(H-pad.t-pad.b)*fr}" x2="${W-pad.r}" y2="${pad.t+(H-pad.t-pad.b)*fr}" stroke="currentColor" opacity=".10"/>`).join("");
  return `<svg class="mini-chart" viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(title)} profilgrafikon" style="--card-accent:${esc(accent||"var(--accent)")}">
    <rect x="${pad.l}" y="${pad.t}" width="${W-pad.l-pad.r}" height="${H-pad.t-pad.b}" rx="15" fill="var(--surface2)"/>
    <g color="var(--text)">${grid}${bands}<line x1="${W-pad.r}" y1="${pad.t}" x2="${W-pad.r}" y2="${H-pad.b}" stroke="currentColor" opacity=".12"/></g>
    <path d="${pathData(p,x,y)}" fill="none" stroke="var(--blue)" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
    <path d="${pathData(f,x,y)}" fill="none" stroke="var(--flow)" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
    <path d="${pathData(temp,x,yt)}" fill="none" stroke="var(--card-accent)" stroke-width="3" stroke-dasharray="9 7" stroke-linejoin="round"/>
    <g fill="var(--muted)" font-size="12"><text x="${pad.l}" y="${H-10}">0 s</text><text x="${W-pad.r}" y="${H-10}" text-anchor="end">${formatNumber(total,0)} s max</text><text x="8" y="${pad.t+8}">${formatNumber(leftMax-1,0)}</text><text x="18" y="${H-pad.b}">0</text><text x="${W-6}" y="${pad.t+8}" text-anchor="end">${formatNumber(tMax,1)} °C</text><text x="${W-6}" y="${H-pad.b}" text-anchor="end">${formatNumber(tMin,1)} °C</text></g>
  </svg>`;
}

function phaseBoundaries(profile){
  let t=0;
  return (profile?.phases||[]).map(phase=>{
    const d=Math.max(0,Number(phase.duration)||0),start=t;t+=d;
    return {name:phase.name||"Fázis",start,end:t,phase};
  });
}
function buildChartModel(profile){
  return {
    total:Math.max(1,totalDuration(profile)),
    phases:phaseBoundaries(profile),
    pressure:curveSeries(profile,"pressure"),
    flow:curveSeries(profile,"flow"),
    temperature:tempSeries(profile),
    weightTarget:lastWeightTarget(profile)
  };
}
function valueAtTime(points,t){
  for(let i=0;i<points.length-1;i++){
    const [x0,y0]=points[i],[x1,y1]=points[i+1];
    if(t<x0||t>x1)continue;
    if(y0===null||y1===null)return null;
    if(x1===x0)return y1;
    return y0+(y1-y0)*((t-x0)/(x1-x0));
  }
  return null;
}
function phaseAtTime(model,t){
  return model.phases.find(p=>t>=p.start&&t<=p.end)||model.phases[model.phases.length-1]||null;
}

function inlineMarkdown(text){
  const protectedParts=[];
  const protect=fragment=>`\uE000${protectedParts.push(fragment)-1}\uE001`;
  let source=String(text);
  source=source.replace(/!\[([^\]]*)\]\(([^)]+)\)/g,(_,alt,src)=>protect(`<img src="${esc(src)}" alt="${esc(alt)}">`));
  source=source.replace(/\[([^\]]+)\]\(([^)]+)\)/g,(_,label,href)=>{
    if(/\.md(?:[?#].*)?$/i.test(href))return protect(`<a href="#" class="nested-md" data-file="${esc(href)}">${esc(label)}</a>`);
    return protect(`<a href="${esc(href)}" target="_blank" rel="noopener">${esc(label)}</a>`);
  });
  source=source.replace(/`([^`]+)`/g,(_,code)=>protect(`<code>${esc(code)}</code>`));
  let html=esc(source).replace(/\*\*([^*]+)\*\*/g,"<strong>$1</strong>").replace(/__([^_]+)__/g,"<strong>$1</strong>").replace(/\*([^*]+)\*/g,"<em>$1</em>");
  return html.replace(/\uE000(\d+)\uE001/g,(_,i)=>protectedParts[Number(i)]);
}
function isTableSep(line){return /^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$/.test(line);}
function splitRow(line){return line.trim().replace(/^\|/,"").replace(/\|$/,"").split("|").map(c=>c.trim());}
function slugifyHeading(text){
  return String(text).toLowerCase().normalize("NFKD").replace(/[̀-ͯ]/g,"")
    .replace(/[^a-z0-9]+/g,"-").replace(/^-+|-+$/g,"")||"section";
}
function renderMarkdown(markdown,buildToc=true){
  const lines=String(markdown).replace(/\r\n?/g,"\n").split("\n"),out=[];let i=0,inCode=false,code=[],para=[],list=[],ordered=false,quote=[];
  const headings=[],usedIds=new Set();
  const flushP=()=>{if(para.length){out.push(`<p>${inlineMarkdown(para.join(" "))}</p>`);para=[];}};
  const flushL=()=>{if(list.length){out.push(`${ordered?"<ol>":"<ul>"}${list.map(x=>`<li>${inlineMarkdown(x)}</li>`).join("")}${ordered?"</ol>":"</ul>"}`);list=[];}};
  const flushQ=()=>{if(quote.length){out.push(`<blockquote>${renderMarkdown(quote.join("\n"),false)}</blockquote>`);quote=[];}};
  while(i<lines.length){
    const line=lines[i],trim=line.trim();
    if(trim.startsWith("```")){flushP();flushL();flushQ();if(inCode){out.push(`<pre><code>${esc(code.join("\n"))}</code></pre>`);code=[];inCode=false;}else inCode=true;i++;continue;}
    if(inCode){code.push(line);i++;continue;}
    if(!trim){flushP();flushL();flushQ();i++;continue;}
    if((trim==="---"||trim==="***"||trim==="___")){flushP();flushL();flushQ();out.push("<hr>");i++;continue;}
    if(trim.includes("|")&&i+1<lines.length&&isTableSep(lines[i+1])){flushP();flushL();flushQ();const rows=[line,lines[i+1]];i+=2;while(i<lines.length&&lines[i].trim().includes("|")&&lines[i].trim())rows.push(lines[i++]);const head=splitRow(rows[0]),body=rows.slice(2).map(splitRow);out.push(`<table><thead><tr>${head.map(c=>`<th>${inlineMarkdown(c)}</th>`).join("")}</tr></thead><tbody>${body.map(r=>`<tr>${r.map(c=>`<td>${inlineMarkdown(c)}</td>`).join("")}</tr>`).join("")}</tbody></table>`);continue;}
    const h=trim.match(/^(#{1,6})\s+(.+)$/);
    if(h){
      flushP();flushL();flushQ();
      const level=h[1].length,text=h[2];
      let id="";
      if(buildToc){
        id=slugifyHeading(text);
        let unique=id,n=2;
        while(usedIds.has(unique))unique=`${id}-${n++}`;
        id=unique;usedIds.add(id);
        headings.push({level,text,id});
      }
      out.push(`<h${level}${id?` id="${id}"`:""}>${inlineMarkdown(text)}</h${level}>`);
      i++;continue;
    }
    const q=trim.match(/^>\s?(.*)$/);if(q){flushP();flushL();quote.push(q[1]);i++;continue;}
    const ul=trim.match(/^[-*+]\s+(.+)$/),ol=trim.match(/^\d+\.\s+(.+)$/);if(ul||ol){flushP();flushQ();const now=Boolean(ol);if(list.length&&ordered!==now)flushL();ordered=now;list.push((ul||ol)[1]);i++;continue;}
    flushL();flushQ();para.push(trim);i++;
  }
  if(inCode)out.push(`<pre><code>${esc(code.join("\n"))}</code></pre>`);flushP();flushL();flushQ();
  let result=out.join("\n");
  if(buildToc&&headings.length>=4){
    const tocHtml=`<nav class="md-toc" aria-label="Tartalomjegyzék"><strong>Tartalom</strong><ul>${headings.filter(h=>h.level<=3).map(h=>`<li class="toc-level-${h.level}"><a href="#${h.id}">${esc(h.text)}</a></li>`).join("")}</ul></nav>`;
    result=tocHtml+result;
  }
  return result;
}
function resolveRelativePath(base,rel){
  if(/^([a-z]+:)?\/\//i.test(rel)||rel.startsWith("#"))return rel;
  const stack=(base||"").split("/").slice(0,-1);
  rel.split("/").forEach(part=>{
    if(part===""||part===".")return;
    if(part==="..")stack.pop();
    else stack.push(part);
  });
  return stack.join("/");
}
