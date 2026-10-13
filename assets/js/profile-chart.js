"use strict";
/* Profile charts in the Tools for GaggiMate style (index cards, profile.html, compare.html).
 * The SVG is drawn at the host's real pixel width, so it fills its frame instead of being
 * letterboxed, and is redrawn when the host is resized or first becomes visible (a closed
 * <details> has no width). Needs esc, formatNumber and pathData (profile-common.js or
 * index.html's inline copy). */

const chartObserver=typeof ResizeObserver==="function"?new ResizeObserver(entries=>{
  entries.forEach(entry=>{
    const host=entry.target,width=Math.round(entry.contentRect.width);
    // redraw on the next frame: drawing here changes the host's height inside the observer's own loop
    if(host.__chartDraw&&width>0&&width!==host.__chartWidth)requestAnimationFrame(()=>drawMountedChart(host));
  });
}):null;

/* Draws draw(width) into host now (if it has a width) and again whenever its width changes. */
function mountChart(host,draw){
  if(!host)return;
  host.__chartDraw=draw;
  host.__chartWidth=0;
  if(chartObserver)chartObserver.observe(host);
  drawMountedChart(host);
}
function drawMountedChart(host){
  const width=Math.round(host.clientWidth);
  if(width<=0&&chartObserver)return;  // hidden for now; the observer draws it once it has a size
  host.__chartWidth=width;
  host.__chartDraw(Math.max(280,width||760));
}

function niceStep(span,maxTicks){
  const raw=span/Math.max(1,maxTicks),pow=10**Math.floor(Math.log10(raw));
  return [1,2,5,10].map(m=>m*pow).find(s=>s>=raw)||10*pow;
}

/* opts: {width,height,total,phases:[{name,start,end}],series:[{points,axis:"left"|"temp",color,dash,width,fill}],
 *        label,ids:{svg,crosshair,overlay}}  →  {svg,x,pad,plotWidth} */
function profileChartSVG(opts){
  const W=opts.width,H=opts.height||260,pad={l:34,r:40,t:opts.phases?.length?24:12,b:26};
  const plotW=W-pad.l-pad.r,plotH=H-pad.t-pad.b,total=Math.max(1,opts.total);
  const left=opts.series.filter(s=>s.axis!=="temp"),temp=opts.series.filter(s=>s.axis==="temp");
  const leftVals=left.flatMap(s=>s.points.map(p=>p[1])).filter(Number.isFinite);
  const leftStep=niceStep(Math.max(10,...leftVals),5);
  const leftMax=Math.max(10,Math.ceil((Math.max(0,...leftVals)+.5)/leftStep)*leftStep);
  const temps=temp.flatMap(s=>s.points.map(p=>p[1])).filter(Number.isFinite);
  let tMin=temps.length?Math.min(...temps):0,tMax=temps.length?Math.max(...temps):1;
  if(tMax-tMin<2){const mid=(tMax+tMin)/2;tMin=mid-1;tMax=mid+1;}else{const p=(tMax-tMin)*.15;tMin-=p;tMax+=p;}
  const x=t=>pad.l+plotW*(t/total);
  const y=v=>pad.t+plotH*(1-v/leftMax);
  const yt=v=>pad.t+plotH*(1-(v-tMin)/(tMax-tMin));
  const f=v=>v.toFixed(1);
  let out="";
  // horizontal grid + left (bar · ml/s) scale
  for(let v=0;v<=leftMax+1e-9;v+=leftStep){
    out+=`<line x1="${pad.l}" y1="${f(y(v))}" x2="${W-pad.r}" y2="${f(y(v))}" stroke="var(--line)" stroke-width="1"/>`;
    if(left.length)out+=`<text x="${pad.l-7}" y="${f(y(v)+4)}" text-anchor="end">${formatNumber(v,1)}</text>`;
  }
  // right (°C) scale: three values
  if(temp.length)[tMin,(tMin+tMax)/2,tMax].forEach(v=>{
    out+=`<text x="${W-pad.r+7}" y="${f(yt(v)+4)}" text-anchor="start">${formatNumber(v,1)}</text>`;
  });
  // vertical time grid
  const tStep=niceStep(total,Math.max(2,Math.floor(plotW/80)));
  for(let t=0;t<=total+1e-9;t+=tStep){
    out+=`<line x1="${f(x(t))}" y1="${pad.t}" x2="${f(x(t))}" y2="${H-pad.b}" stroke="var(--line)" stroke-dasharray="3 5"/>`;
    out+=`<text x="${f(x(t))}" y="${H-8}" text-anchor="${t===0?"start":"middle"}">${formatNumber(t,0)} s</text>`;
  }
  // phase boundaries with names (only where the name fits)
  (opts.phases||[]).forEach((p,i)=>{
    const x0=x(p.start),wPx=x(p.end)-x0;
    if(i%2)out+=`<rect x="${f(x0)}" y="${pad.t}" width="${f(Math.max(0,wPx))}" height="${plotH}" fill="var(--text)" opacity=".035"/>`;
    if(i>0)out+=`<line x1="${f(x0)}" y1="${pad.t}" x2="${f(x0)}" y2="${H-pad.b}" stroke="var(--muted)" opacity=".45"/>`;
    const name=String(p.name||"");
    if(name&&wPx>name.length*5.6+10)out+=`<text class="phase" x="${f(x0+5)}" y="${pad.t-12}">${esc(name)}</text>`;
  });
  // curves: the left-axis ones may carry a soft fill down to 0
  opts.series.forEach(s=>{
    const scale=s.axis==="temp"?yt:y,d=pathData(s.points,x,scale);
    if(!d)return;
    if(s.fill){
      const segs=d.split(/(?=M)/).map(seg=>{const pts=seg.trim().slice(1).split("L").map(q=>q.trim().split(" "));const first=pts[0],last=pts[pts.length-1];return `M${first[0]} ${f(y(0))} L${seg.trim().slice(1)} L${last[0]} ${f(y(0))} Z`;}).join(" ");
      out+=`<path d="${segs}" fill="${s.color}" opacity=".08"/>`;
    }
    out+=`<path d="${d}" fill="none" stroke="${s.color}" stroke-width="${s.width||2.6}" stroke-linejoin="round" stroke-linecap="round"${s.dash?` stroke-dasharray="${s.dash}"`:""}/>`;
  });
  // units are in each chart's legend (Nyomás (bar), Flow (ml/s), Hőmérséklet (°C)), not repeated here
  const ids=opts.ids||{};
  if(ids.crosshair)out+=`<line id="${ids.crosshair}" x1="0" y1="${pad.t}" x2="0" y2="${H-pad.b}" stroke="var(--text)" opacity="0"/>`;
  if(ids.overlay)out+=`<rect id="${ids.overlay}" x="${pad.l}" y="${pad.t}" width="${plotW}" height="${plotH}" fill="transparent"/>`;
  const svg=`<svg class="mini-chart"${ids.svg?` id="${ids.svg}"`:""} width="100%" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(opts.label||"Profilgrafikon")}" font-size="11" fill="var(--gm-faint)" style="font-family:var(--gm-font);font-variant-numeric:tabular-nums">${out}</svg>`;
  return {svg,x,pad,plotWidth:plotW};
}
