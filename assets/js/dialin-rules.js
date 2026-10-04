"use strict";
/* Deterministic, explainable dial-in rule engine. No AI/LLM involved —
 * a fixed decision tree over the taste-feedback fields, so behavior is
 * reproducible and auditable. Designed to be replaced/extended later
 * (e.g. by a real profile-engine) without changing the calling code:
 * the only contract is suggestAdjustments(feedback) -> {adjustments, primary, confidence}.
 *
 * feedback shape:
 * { acidity: 'too_sour'|'bright'|'balanced'|'muted',
 *   bitterness: 'low'|'balanced'|'high',
 *   sweetness: 'low'|'medium'|'high',
 *   body: 'tea-like'|'medium'|'syrupy',
 *   dryness: 'none'|'slight'|'high',
 *   flavors: string[],
 *   observations: string[] }
 */
function suggestAdjustments(feedback){
  const obs=feedback.observations||[];
  if(obs.includes("channeling")||obs.includes("spraying")||obs.includes("unstable-stream")){
    return {
      adjustments:[],
      primary:"Egyenetlen extrakció jele (csatornázás / fröcskölés / instabil sugár). Mielőtt bármilyen profil- vagy őrlésparamétert módosítanál, először a puck-előkészítést ellenőrizd: WDT, egyenletes tamp, puck screen illeszkedése.",
      confidence:"erős jel (mechanikai, nem íz-alapú)"
    };
  }
  const underSignals=[feedback.acidity==="too_sour",feedback.dryness==="high",feedback.bitterness==="low"].filter(Boolean).length;
  const overSignals=[feedback.bitterness==="high",feedback.dryness==="high",feedback.acidity==="muted"].filter(Boolean).length;
  const adjustments=[];
  if(underSignals>=1&&underSignals>overSignals){
    adjustments.push({variable:"Őrlésfokozat",direction:"1 kattintással finomabb",reason:"Savanyú, vékony vagy csersavas jelleg tipikusan alulextrahált shotra utal; finomabb őrléssel nő az ellenállás és az extrakciós hatásfok."});
    adjustments.push({variable:"Hozam",direction:"+1.5–2 g hosszabb",reason:"Hosszabb hozammal több idő jut az extrakcióra a dózis vagy a profil módosítása nélkül."});
  }else if(overSignals>=1&&overSignals>underSignals){
    adjustments.push({variable:"Őrlésfokozat",direction:"1 kattintással durvább",reason:"Keserű és/vagy csersavas jelleg tipikusan túlextrahált shotra utal."});
    adjustments.push({variable:"Hozam",direction:"-1.5–2 g rövidebb",reason:"Rövidebb hozammal csökken a túlextrahált vegyületek aránya a csészében."});
  }else if(feedback.sweetness==="low"&&feedback.body==="tea-like"){
    adjustments.push({variable:"Őrlésfokozat vagy dózis",direction:"kicsit finomabb őrlés, vagy +0.3–0.5 g dózis",reason:"Vékony test és alacsony édesség gyakran alacsony kivonat-koncentrációra utal."});
  }
  if(!adjustments.length){
    return {adjustments:[],primary:"A visszajelzés alapján a shot kiegyensúlyozottnak tűnik — nincs egyértelmű, a küszöböt elérő javasolt módosítás.",confidence:"nincs erős jel"};
  }
  return {adjustments:adjustments.slice(0,2),primary:null,confidence:"heurisztika egy korábbi shot visszajelzéséből — nem garantált eredmény, egyszerre csak egy változtatást érdemes kipróbálni"};
}
