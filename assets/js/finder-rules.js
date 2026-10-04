"use strict";
/* Deterministic Profile Finder rule engine. Not a generator — it recommends an
 * existing profile archetype (a real coffee already in profiles/) plus a
 * starting recipe, using the documented process/temperature/pressure/ratio
 * relationships from PROFILE_CREATION_GUIDE.md ("Feldolgozás és profil
 * összefüggések", "Paraméterek és ízhatásuk", "Kiindulópont kiválasztása").
 * Fixed rules, no scoring/confidence percentage — only explicit reasoning. */

const PROCESS_TABLE={
  washed:{tempLow:93.5,tempHigh:94.5,pressureLow:7.4,pressureHigh:7.6,yieldLow:42,yieldHigh:44,archetype:"kirinyaga",label:"Washed"},
  natural:{tempLow:93.5,tempHigh:94.5,pressureLow:7.0,pressureHigh:7.4,yieldLow:41,yieldHigh:43,archetype:"burundi-mubuga",label:"Natural"},
  honey:{tempLow:94.0,tempHigh:94.5,pressureLow:7.2,pressureHigh:7.5,yieldLow:42,yieldHigh:43,archetype:"colombia-manos-juntas",label:"Honey"},
  anaerobic:{tempLow:94.0,tempHigh:94.5,pressureLow:7.0,pressureHigh:7.4,yieldLow:42,yieldHigh:44,archetype:"colombia-manos-juntas",label:"Anaerobic"},
  other:{tempLow:94.0,tempHigh:94.5,pressureLow:7.0,pressureHigh:7.6,yieldLow:41,yieldHigh:43,archetype:"wangera",label:"Általános"}
};
const ARCHETYPES={
  "kirinyaga":{title:"Kirinyaga PB (Tea Rose)",reason:"washed Kenya/Ethiopia kávékhoz dokumentált alap (PROFILE_CREATION_GUIDE.md)"},
  "burundi-mubuga":{title:"Burundi Mubuga",reason:"natural Burundi/Ethiopia kávékhoz dokumentált alap"},
  "colombia-manos-juntas":{title:"Colombia Manos Juntas",reason:"anaerobic/honey Colombia kávékhoz dokumentált alap"},
  "twenty-eight-caturron":{title:"28 · Caturron",reason:"natural Guatemala / Közép-Amerika kávékhoz dokumentált alap"},
  "wangera":{title:"Kenya Wangera (Stable Start)",reason:"általános washed baseline, ha nincs jobban illő specifikus archetípus"},
  "9-bar":{title:"9 Bar Espresso (klasszikus)",reason:"hagyományos, magas nyomású (9 bar) espresso stílushoz dokumentált baseline"}
};
const ROAST_SHIFT={
  "light":"+0.3 °C a sáv tetejéhez közelebb — világos pörkölésnél a magasabb hő segít kihozni az aromaélénkséget (PROFILE_CREATION_GUIDE.md: 94.5–95 °C sáv).",
  "medium-light":"a sáv közepe felé — nincs erős ok elmozdulni egyik irányba sem.",
  "medium":"a sáv közepe.",
  "medium-dark":"-0.2 °C a sáv aljához közelebb — a keserűség kockázatának csökkentésére.",
  "dark":"-0.3 °C a sáv aljához közelebb — sötét pörkölésnél a magasabb hő feleslegesen növeli a keserűség kockázatát (93–94 °C sáv logikája)."
};
const BEAN_AGE_NOTE={
  "very-fresh":"Nagyon friss kávénál (sok maradék CO₂) érdemes hosszabb/óvatosabb bloomot hagyni, hogy a gázkiáramlás ne okozzon csatornázást — ez a profil kiválasztását nem, csak a bloom-fázis időzítését érinti.",
  "rested":"Pihentetett (kb. 1–3 hetes) kávénál a dokumentált alaptartományok közvetlenül alkalmazhatók.",
  "older":"Régebbi, már kevésbé gázos kávénál gyakran picit magasabb hőmérséklet vagy finomabb őrlés kompenzálja a halványuló aromákat."
};
const CUP_STYLE_TABLE={
  "fruity-clarity":{pressureBias:"high",timeRange:"38–39 s",ratio:"~1:2.3",reason:"Tisztább, gyümölcsösebb csészéhez a sáv felső nyomástartománya és a közepesnél kicsit hosszabb hozam segít (PROFILE_CREATION_GUIDE.md ratio/idő táblázat)."},
  "balanced":{pressureBias:"mid",timeRange:"38–39 s",ratio:"~1:2.2–1:2.3",reason:"Kiegyensúlyozott csészéhez a dokumentált standard idő/arány tartomány illik."},
  "sweet":{pressureBias:"low",timeRange:"35–37 s",ratio:"~1:2.2",reason:"Lágyabb, édesebb csészéhez alacsonyabb főnyomás és rövidebb profilidő véd az extra keserűségtől (6.5–7.0 bar sáv logikája)."},
  "body":{pressureBias:"high",timeRange:"40–42 s",ratio:"~1:2.3–1:2.4",reason:"Testesebb csészéhez magasabb nyomás és valamivel hosszabb hozam ad több kivonatot (7.6–8.5 bar sáv logikája)."},
  "traditional":{pressureBias:"traditional",timeRange:"~28 s",ratio:"~1:2",reason:"Hagyományos espresso stílushoz a 9 bar-os klasszikus profil a dokumentált baseline, nem a GaggiMate adaptív preinfúziós sávjai."}
};

function pickArchetype(process,origin,cupStyle){
  if(cupStyle==="traditional")return "9-bar";
  if(process==="natural"&&origin==="central-south-america")return "twenty-eight-caturron";
  return PROCESS_TABLE[process]?.archetype||"wangera";
}

function findProfileRecommendation(input){
  const process=PROCESS_TABLE[input.process]?input.process:"other";
  const table=PROCESS_TABLE[process];
  const cupStyle=CUP_STYLE_TABLE[input.cupStyle]||CUP_STYLE_TABLE.balanced;
  const primaryId=pickArchetype(process,input.origin,input.cupStyle);
  const primary=ARCHETYPES[primaryId];
  const alternativeId=primaryId==="wangera"?PROCESS_TABLE[process].archetype:"wangera";
  const alternative=ARCHETYPES[alternativeId]||ARCHETYPES.wangera;

  const reasoning=[
    `Feldolgozás: ${table.label} → dokumentált hőtartomány ${table.tempLow}–${table.tempHigh} °C, főnyomás ${table.pressureLow}–${table.pressureHigh} bar, hozam ${table.yieldLow}–${table.yieldHigh} g (PROFILE_CREATION_GUIDE.md).`,
    `Pörkölési fok (${input.roast}): ${ROAST_SHIFT[input.roast]||ROAST_SHIFT.medium}`,
    `Kávé kora: ${BEAN_AGE_NOTE[input.beanAge]||BEAN_AGE_NOTE.rested}`,
    `Kívánt csésze-stílus (${input.cupStyle}): ${cupStyle.reason}`,
    `Archetípus-választás: ${primary.title} — ${primary.reason}.`
  ];

  return {
    primary:{id:primaryId,title:primary.title,reason:primary.reason},
    alternative:primaryId!==alternativeId?{id:alternativeId,title:alternative.title,reason:alternative.reason}:null,
    recipe:{
      doseG:18.5,
      tempRange:`${table.tempLow}–${table.tempHigh} °C`,
      pressureRange:cupStyle.pressureBias==="traditional"?"9 bar (klasszikus, nem adaptív)":`${table.pressureLow}–${table.pressureHigh} bar`,
      yieldRange:`${table.yieldLow}–${table.yieldHigh} g`,
      ratio:cupStyle.ratio,
      timeRange:cupStyle.timeRange
    },
    reasoning,
    disclaimer:"Ez egy determinisztikus, a PROFILE_CREATION_GUIDE.md dokumentált szabályaiból levezetett kiindulópont-javaslat, nem egy validált, az adott kávéra mért recept. A tényleges dial-in (őrlés, pontos hozam) mindig a kóstolás alapján finomhangolandó."
  };
}
