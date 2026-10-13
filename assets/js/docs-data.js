"use strict";
/* The documents (documents.html) and knowledge-base articles (knowledge.html) of the site.
 * A knowledge item's optional ref/refDescription is its deep reference (knowledge/reference/), shown as a
 * third button on the same card. Adding or renaming a document or article means updating this file;
 * validate_repo.py checks every file/fileHu/ref path here exists. */
const DOCS = [
  {title:"README",file:"README.md",description:"Projektáttekintés, profilok, Bluetooth Scale Edition.",icon:'<path d="M12 6.5c-1.7-1-4-1.3-6-1v12c2 0 4.3.3 6 1.3 1.7-1 4-1.3 6-1.3V5.5c-2-.3-4.3 0-6 1Z"/><path d="M12 6.5v12"/>'},
  {title:"Összefoglaló",file:"docs/profiles/summary.md",description:"Aktuális profilok, ízjegyek és könyvtárszerkezet.",icon:'<path d="M8 6h10M8 12h10M8 18h10"/><circle cx="4.5" cy="6" r="1"/><circle cx="4.5" cy="12" r="1"/><circle cx="4.5" cy="18" r="1"/>'},
  {title:"Brew Guidelines",file:"docs/brewing/brew-guidelines.md",description:"Dózis, hozam, őrlés, puck prep és dial-in.",icon:'<path d="M7.5 4.5h9v6.8a4.5 4.5 0 0 1-9 0V4.5Z"/><path d="M16.5 7h1.3a2.7 2.7 0 0 1 0 5.4h-1.5M5 19.5h14"/>'},
  {title:"Darálási útmutató",file:"docs/brewing/grinder-guidelines.md",description:"DF64V Gen 2 és SSP Sweet Lab Espresso V3.",icon:'<circle cx="12" cy="12" r="3"/><path d="M12 3v2M12 19v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M3 12h2M19 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"/>'},
  {title:"Setup / berendezés",file:"docs/equipment/setup.md",description:"Gép és daráló dokumentáció: Gaggia Classic Pro 2025, GaggiMate Pro, DF64V, kosár-összehasonlítás.",icon:'<rect x="4" y="3.5" width="16" height="13" rx="2"/><path d="M9 20.5h6M12 16.5v4"/>'},
  {title:"Bluetooth Scale Workflow",file:"docs/equipment/bluetooth-scale-workflow.md",description:"BOOKOO párosítás, kalibráció és hibakeresés.",icon:'<path d="M7 7l10 10L12 22V2l5 5L7 17"/>'},
  {title:"Profilkészítési útmutató",file:"docs/profiles/profile-creation-guide.md",description:"GaggiMate JSON séma, fázisok és új profil készítése.",icon:'<path d="M14.5 6.5a3.5 3.5 0 0 1-4.6 4.6L5 16l3 3 4.9-4.9a3.5 3.5 0 0 1 4.6-4.6l-2.3 2.3-2-2 2.3-2.3Z"/>'},
  {title:"Fájlelnevezés",file:"docs/profiles/file-naming.md",description:"Mappa-, JSON-, PNG-, recipe- és changelog-nevek.",icon:'<path d="M12.6 3H6a1 1 0 0 0-1 1v6.6a1 1 0 0 0 .3.7l9 9a1 1 0 0 0 1.4 0l6.3-6.3a1 1 0 0 0 0-1.4l-9-9a1 1 0 0 0-.4-.3Z"/><circle cx="8.5" cy="8.5" r="1.2"/>'},
  {title:"Projekt changelog",file:"CHANGELOG.md",description:"Repository-szintű változások.",icon:'<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>'},
  {title:"Feldolgozások",file:"docs/coffee/speciality-kave-feldolgozasok.md",description:"Washed, natural, honey, anaerob és carbonic.",icon:'<path d="M19 5c-8 0-13 5-13 13 8 0 13-5 13-13Z"/><path d="M7 17c3-3 6-6 11-11"/>'},
  {title:"Kávévíz recept",file:"docs/brewing/kaveviz-5l-epsom-bikarbonat.md",description:"5 literes vízprofilok Epsom-sóval és szódabikarbónával.",icon:'<path d="M12 3.5s6 6.6 6 10.8a6 6 0 0 1-12 0C6 10.1 12 3.5 12 3.5Z"/>'},
  {title:"Shot Log Viewer",file:"shot-logs/shot-viewer.html",description:"Letöltött GaggiMate shot logok grafikus megjelenítése – nyomás, flow, hőmérséklet és mérleg görbék.",icon:'<path d="M4 19h16M7 16V9m5 7V5m5 11v-5"/>',external:true}
];

// Topic pictograms of the knowledge-base cards (24×24, stroked); a deep reference uses its topic's icon.
const KB_ICONS={
  baskets:'<path d="M3.5 8h17"/><path d="M5 8l1.3 8.2A3 3 0 0 0 9.3 19h5.4a3 3 0 0 0 3-2.8L19 8"/><path d="M9 11.5h.01M12 11.5h.01M15 11.5h.01M10.5 14.8h.01M13.5 14.8h.01"/>',
  freshness:'<path d="M7.5 3h9l1.5 4v12a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V7Z"/><path d="M6 7h12"/><circle cx="12" cy="13.5" r="2.2"/>',
  brewing:'<path d="M7.5 4.5h9v6.8a4.5 4.5 0 0 1-9 0V4.5Z"/><path d="M16.5 7h1.3a2.7 2.7 0 0 1 0 5.4h-1.5M5 19.5h14"/>',
  tasting:'<ellipse cx="8.5" cy="8.5" rx="4" ry="4.8" transform="rotate(-45 8.5 8.5)"/><path d="m11.6 11.6 8.4 8.4"/>',
  extraction:'<path d="M9.5 3h5M10.5 3v6.2L5.2 18a2 2 0 0 0 1.7 3h10.2a2 2 0 0 0 1.7-3l-5.3-8.8V3"/><path d="M7.4 15h9.2"/>',
  profile:'<path d="M3.5 19.5h17"/><path d="M4 16l4-7 4 3.5 4-7.5 4 5"/>',
  milk:'<path d="M7.5 3.5h8l-.8 3 2.3 3.5v9a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2v-9l2.3-3.5Z"/><path d="M6 12.5h11"/>',
  pressure:'<path d="M4.3 17a8.5 8.5 0 1 1 15.4 0"/><path d="m12 13.5 4-4.5"/><circle cx="12" cy="13.5" r="1.3"/><path d="M7 17h10"/>',
  library:'<path d="m12 3.5 8.5 4.5-8.5 4.5L3.5 8Z"/><path d="m3.5 12 8.5 4.5 8.5-4.5"/><path d="m3.5 16 8.5 4.5 8.5-4.5"/>',
  screens:'<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5h.01M8 10h.01M16 10h.01M12 12h.01M9 14.8h.01M15 14.8h.01M12 16.5h.01"/>',
  special:'<path d="m12 3.5 2.5 5.3 5.8.7-4.3 4 1.1 5.8L12 16.5l-5.1 2.8 1.1-5.8-4.3-4 5.8-.7Z"/>',
  grinder:'<circle cx="12" cy="12" r="3"/><path d="M12 3v2M12 19v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M3 12h2M19 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"/>'
};
const KNOWLEDGE=[
  {group:"Alapok",items:[
    {title:"Kosarak",file:"knowledge/BASKETS.md",fileHu:"knowledge/hu/BASKETS.md",description:"Kosarak hatása az extrakcióra – gyors referencia dialing közben.",ref:"knowledge/reference/BASKETS_REFERENCE.md",refDescription:"Részletes kosárspecifikációk, összehasonlítás és geometria.",icon:KB_ICONS.baskets},
    {title:"Kávé frissesség és tárolás",file:"knowledge/BEAN_FRESHNESS_AND_STORAGE.md",fileHu:"knowledge/hu/BEAN_FRESHNESS_AND_STORAGE.md",description:"Frissességi ablakok, ultra-friss kávé kezelése, vizuális jelek.",ref:"knowledge/reference/BEAN_FRESHNESS_REFERENCE.md",refDescription:"Degazálás tudománya, tárolási módszerek, fagyasztási protokollok, romlási jelek.",icon:KB_ICONS.freshness},
    {title:"Espresso brewing alapok",file:"knowledge/ESPRESSO_BREWING_BASICS.md",fileHu:"knowledge/hu/ESPRESSO_BREWING_BASICS.md",description:"Alapváltozók, hangolási stratégiák és diagnosztika dialing közben.",ref:"knowledge/reference/ESPRESSO_BREWING_REFERENCE.md",refDescription:"Shot stílusok, extrakciós elmélet, dialing-in módszertan, haladó technikák.",icon:KB_ICONS.brewing},
    {title:"Kóstolási útmutató",file:"knowledge/ESPRESSO_TASTING_GUIDE.md",fileHu:"knowledge/hu/ESPRESSO_TASTING_GUIDE.md",description:"Shot értékelése és visszajelzés adása kóstoláskor.",ref:"knowledge/reference/ESPRESSO_TASTING_REFERENCE.md",refDescription:"Ízkerék, palettafejlesztés, aromaértékelés, hibás ízek, palate fatigue.",icon:KB_ICONS.tasting},
    {title:"Extrakciótudomány",file:"knowledge/EXTRACTION_SCIENCE.md",fileHu:"knowledge/hu/EXTRACTION_SCIENCE.md",description:"Daráló-profil összefüggés, channeling megelőzés, pre-infúzió, vizuális diagnózis.",ref:"knowledge/reference/EXTRACTION_SCIENCE_REFERENCE.md",refDescription:"Az extrakciótudomány elméleti háttere a gyors útmutató mögött.",icon:KB_ICONS.extraction},
    {title:"GaggiMate profilkészítési útmutató",file:"knowledge/GAGGIMATE_PROFILE_CREATION_GUIDE.md",fileHu:"knowledge/hu/GAGGIMATE_PROFILE_CREATION_GUIDE.md",description:"GaggiMate profil JSON séma, pumpa módok, stop feltételek, példák.",ref:"knowledge/reference/PROFILE_CREATION_REFERENCE.md",refDescription:"JSON séma, pumpa módok, stop feltételek részletesen, példákkal.",icon:KB_ICONS.profile},
    {title:"Tej és tejes italok",file:"knowledge/MILK_AND_DRINKS.md",fileHu:"knowledge/hu/MILK_AND_DRINKS.md",description:"Gőzölési technika, hőmérséklet küszöbök, italreceptek, single-boiler workflow.",ref:"knowledge/reference/MILK_AND_DRINKS_REFERENCE.md",refDescription:"Tejgőzölés és italkészítés részletes háttere.",icon:KB_ICONS.milk},
    {title:"Nyomás útmutató",file:"knowledge/PRESSURE_GUIDE.md",fileHu:"knowledge/hu/PRESSURE_GUIDE.md",description:"Nyomás hatása az ízre, pörkölési fok és feldolgozás szerint.",ref:"knowledge/reference/PRESSURE_REFERENCE.md",refDescription:"Nyomásmátrix, shot stílus paraméterek, döntési keretrendszer.",icon:KB_ICONS.pressure},
    {title:"Profilkönyvtár",file:"knowledge/PROFILE_LIBRARY.md",fileHu:"knowledge/hu/PROFILE_LIBRARY.md",description:"Kész, általános GaggiMate Pro extrakciós profilsablonok.",ref:"knowledge/reference/PROFILE_LIBRARY_REFERENCE.md",refDescription:"Profil összefoglaló táblázat, kiválasztási útmutatók, paraméterek.",icon:KB_ICONS.library},
    {title:"Puck screenek",file:"knowledge/PUCK_SCREENS.md",fileHu:"knowledge/hu/PUCK_SCREENS.md",description:"Puck screen hatása az extrakcióra – gyors referencia.",ref:"knowledge/reference/PUCK_SCREENS_REFERENCE.md",refDescription:"Puck screenek részletes háttere a gyors útmutató mögött.",icon:KB_ICONS.screens},
    {title:"Speciális kategóriák",file:"knowledge/SPECIAL_CATEGORIES.md",fileHu:"knowledge/hu/SPECIAL_CATEGORIES.md",description:"Decaf és blendek extrakciós stratégiái.",ref:"knowledge/reference/SPECIAL_CATEGORIES_REFERENCE.md",refDescription:"Decaf hangolási táblák, blend hőmérséklet-stratégiák, archetípusok.",icon:KB_ICONS.special}
  ]},
  {group:"Darálók",items:[
    {title:"DF64V referencia",file:"knowledge/grinders/DF64V.md",fileHu:"knowledge/hu/grinders/DF64V.md",description:"DF64V Gen-3 + SSP Cast Lab Sweet V3 Red Speed daráló beállítási referencia.",ref:"knowledge/reference/DF64V_REFERENCE.md",refDescription:"DF64V részletes háttér a gyors referencia mögött.",icon:KB_ICONS.grinder}
  ]}
];
const KB_ITEMS=KNOWLEDGE.flatMap(g=>g.items);
