# Extrakciós tudomány

Gyakorlati táblázatok a daráló-profil kölcsönhatáshoz, channeling megelőzéshez, pre-infúzió mechanikájához, frissességi útmutatóhoz és vizuális diagnózishoz.

> *A mély "miért" – TDS/EY elmélet, őrlési tudomány, részecskeeloszlás, channeling fizika, CO2 degazálás – lásd [`reference/EXTRACTION_SCIENCE_REFERENCE.md`](../reference/EXTRACTION_SCIENCE_REFERENCE.md).*

---

## Miért számít a daráló választása a profil tervezésében

A különböző darálók alapvetően eltérő szemcseágyat eredményeznek – ezt elsősorban a **fines tartalom** határozza meg. A daráló lemez alakja (flat vs. kónikus) laza proxy a fines tartalomra, de a konkrét lemezpár dönti el a tényleges eredményt:

| Fines szint | Profil megfontolások |
|-------------|----------------------|
| **Magas fines** (tipikus kónikusok: Sette 270, Niche) | 7–8 bar extrakcióból, lágyabb ramp-ból vagy hosszabb pre-infúzióból profitálhat, hogy elkerüljük a fines túlzott összepréselődését |
| **Alacsony fines flat** (pl. EK43, egyes SSP lemezpárok – *a fines kibocsátás modellenként eltér; nem minden flat alacsony fines-ű*) | Konzisztensen bírja a 9 bar-t; finomabb őrlésre lehet szükség a fines hiányának kompenzálására; a nyomáscsökkenés kevésbé kritikus |
| **Unimodális darálók** | Gyakran flow-alapú profilokat igényelnek a nyomás-alapúak helyett; a turbo-stílusú shotok különösen jól működnek |

> **Csésze karakter (test vs. tisztaság):** A lemez alakja önmagában nem jósolja meg tisztán a test/tisztaság eredményt – ez vitatott és a konkrét lemezpártól függ. Az adott darálóhoz tartozó lemez-karakter jegyzetet nézd meg a saját setupodra vonatkozó tendenciáért.

Ezért fordulhat elő, hogy egy profil, ami tökéletesen működik az egyik setupon, alulteljesít egy másikon – a daráló a rendszer része.

> *A darálódhoz tartozó beállításokért és karbantartásért lásd az adott daráló referenciáját (a `user-setup.md` Grinder mezője szerint).*

---

## Channeling megelőzés

### Megelőzési hierarchia

**Elosztás > Tamp > Nyomás**

1. **Elosztás (a legfontosabb)** – A WDT feloldja a csomókat és egyenletesen elosztja a kávéőrleményt. Semmilyen tamp nem javítja az egyenetlen elosztást.
2. **Tamp (fontos, de másodlagos)** – Sima felületet hoz létre. A konzisztens nyomás fontosabb, mint a nagy nyomás (15–30 lbs megfelelő).
3. **Nyomásprofil (harmadlagos)** – Az alacsonyabb nyomás elnézőbb. A lágy ramp lehetővé teszi, hogy a puck "beálljon" a teljes nyomás előtt. A pre-infúzió átitatja az egész ágyat, mielőtt az extrakciós erő hatna rá.

### Puck prep eszközök

| Eszköz | Mit csinál | Mit nem old meg |
|------|--------------|---------------------|
| **WDT (tűs eszköz)** | Feloldja a csomókat, újraelosztja az őrleményt, egyenletes sűrűséget hoz létre | Nem javítja a túl finom őrlést vagy a daráló rossz egyenletességét |
| **Disztribútor/leveler** | Sima felületet hoz létre, enyhe újraelosztás | Nem oldja fel a belső csomókat (előbb használj WDT-t) |
| **Papírfilter a puck alatt** | Megfogja a vándorló fines-t, megakadályozza a tömör réteget, tisztább csésze | Nem javítja az elosztási problémákat |
| **Puck screen felül** | Lásd [PUCK_SCREENS.md](PUCK_SCREENS.md) | — |

**Ajánlott kombó:** WDT → könnyű koppintás a leülepedéshez → tamp → (opcionális: puck screen felül – lásd [PUCK_SCREENS.md](PUCK_SCREENS.md))

A papírfilterek a puck alatt különösen hatékonyak magas fines-ű darálóknál – megakadályozzák, hogy a fines felhalmozódjon a kosár lyukainál és egyenetlen flow-t okozzon.

---

## Pre-infúzió mechanikája

A pre-infúzió megelőzi a channelinget azáltal, hogy **teljes átitatást ér el az extrakciós nyomás alkalmazása előtt**.

**A fizika:**
1. A száraz kávé hidrofób – a víz szívesebben folyik körülötte, mint át rajta
2. Teljes nyomás egy száraz puckon → a víz bármely gyenge ponton átfolyik → azonnali channeling
3. Az alacsony nyomású pre-infúzió (1–3 bar) időt ad a víznek, hogy egyenletesen átnedvesítse az összes kávét
4. Ha a puck átitatott, nincsenek "gyenge pontok", amiket a víz kihasználhatna
5. Tartsd a pre-infúziót kb. 4 bar alatt. **Megjegyzés ehhez a számhoz:** a 4 bar egy széles körben használt *fázisváltási alapérték* a DE1-eredetű profilokban (ahol a flow kontroll átadja a helyét a nyomáskontrollnak), nem egy mért fizikai küszöb, amelynél a puck összenyomódása elkezdődik. Nem található olyan fizikai forrás, amely megállapítana egy összenyomódás-kezdeti nyomást. Kezeld a ~4 bar-t bevett konvencióként, és ne hivatkozz rá mért állandóként.

**Bloom fázis (kiterjesztett pre-infúzió):**
- Töltsd fel alacsony nyomáson/flow-n, amíg a puck nedves nem lesz
- Állítsd le a szivattyút, várj 5–15 másodpercet
- Lehetővé teszi, hogy a víz teljesen átjárja az összes részecskét
- Különösen hatékony friss szemeknél (lehetővé teszi, hogy a CO2 távozzon extrakció előtt)

> *A nyomás részleteiért, beleértve, hogy mikor történik a puck összenyomódása, lásd a `PRESSURE_GUIDE.md`-t*

---

## Frissességi útmutató

| Napok a pörkölés óta | Útmutatás |
|----------------|----------|
| 1–3 nap | Nagyon friss – számíts inkonzisztenciára. Használj hosszú bloom-ot (10–15s), nagyon lassú pre-infúziót |
| 4–7 nap | Friss – bloom profil ajánlott, hosszabb pre-infúzió |
| 7–14 nap | Édes zóna a legtöbb espressóhoz. A standard profilok jól működnek |
| 14–21 nap | Csúcskomplexitás sok kávénál. Rövidebb pre-infúzió használható |
| 21–30 nap | Még jó, az ízek egyszerűsödhetnek. A standard profilok rendben vannak |
| 30+ nap | Figyelj az állottságra, de sok kávé még mindig kiváló marad |

A világos pörkölések lassabban degazálnak, mint a sötét pörkölések (a sűrűbb szerkezet tovább tartja meg a gázt), így hosszabb pihenési időre vagy kiterjesztett bloom fázisra lehet szükségük.

> *Az átfogó frissesség-kezelésért – csúcs ízvilág ablakok, tárolási módszerek és fagyasztási protokollok – lásd a `BEAN_FRESHNESS_AND_STORAGE.md`-t.*

---

## Vizuális diagnózis (fenéktelen portafilter)

| Mit látsz | Mit jelent | Megoldás |
|--------------|---------------|-----|
| Egyenletes, középre fókuszált espresso kúp | Jó extrakció – a puck ellenállása egyenletes | Folytasd, amit csinálsz |
| Spriccelés/oldalirányú fröcskölés | Channel alakult ki azon a helyen | Jobb WDT, ellenőrizd az elosztást |
| Szőke csíkok sötét espresszóban | A channel túlextrahál egy foltot | Elosztási probléma, esetleg őrlési egyenetlenség |
| Az espresso az egyik oldalról indul el először | Egyenetlen tamp vagy elosztás | Egyenes tamp, újraelosztás |
| Holt/száraz foltok a puck alján (shot után) | A víz teljesen megkerülte azt a területet | Jelentős channeling – komoly elosztási javítás szükséges |
| Nagyon gyors flow vékony crema mellett | Túl durva őrlés vagy súlyos channeling | Finomabb őrlés, jobb prep |

> *Shotonkénti hibaelhárításért lásd a diagnose skill-t vagy a `reference/PROFILE_CREATION_REFERENCE.md` hibaelhárítási szekcióját*

---

*A mély tudományért – TDS/EY képletek, brewing control chart, részecskeeloszlás, channeling fizika, CO2 degazálás – lásd [`reference/EXTRACTION_SCIENCE_REFERENCE.md`](../reference/EXTRACTION_SCIENCE_REFERENCE.md). Gyakorlati beállítási stratégiákért lásd az `ESPRESSO_BREWING_BASICS.md`-t. Nyomás kiválasztásához lásd a `PRESSURE_GUIDE.md`-t.*
