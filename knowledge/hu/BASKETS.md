# Espresso szűrőkosarak

Gyors referencia arról, hogy a kosár hogyan befolyásolja az extrakciót dial-in közben.

---

## Mit jelent valójában a "22g"

A kosárméret (15g, 18g, 20g, 22g) a **névleges dózis kapacitást** jelöli — azt a mennyiségű őrölt kávét, amelyre a kosarat tervezték, miközben megfelelő légrést tart a puck és a shower screen között.

- **Dózis = kosárméret.** Egy 22g-os kosarat 22g kávéval kell dózisolni. Ne underdose-olj.
- **Tolerancia tartomány:** A VST ±1g-ot specifikál (21-23g egy 22g-os kosárnál). Az IMS valamivel szélesebb tartományt enged.
- **Underdosing kockázatai:** Túl sok légrés a puck és a shower screen között → a víz megáll a puck felett → egyenetlen szaturáció → channeling.
- **Overdosing kockázatai:** A puck hozzáér a shower screenhez → lenyomat a pucköln ("screen kiss") → korlátozott flow → egyenetlen extrakció és potenciális ellennyomás.

**Hogyan ellenőrizd a légrést:** Shot után nézd meg a puck tetejét. Simának és laposnak kell lennie, screen lenyomat nélkül. Ha hálómintát látsz a felületbe nyomva, csökkentsd a dózist 0.5g-mal. Ha puck screen van felszerelve, ez az ellenőrzés nem látható — hagyatkozz inkább a flow viselkedésére és a mért légrésre.

---

## Mélység és átmérő

Minden standard 58mm-es kosár ugyanazt az átmérőt osztja meg. A méretek közötti különbség a **mélység** — egy 22g-os kosár (28mm mély IMS-nél) több kávét tartalmaz, mint egy 18g-os (24mm), mert a puck magasabb, nem szélesebb.

Egy mélyebb pucknak eltérő extrakciós jellemzői vannak:

- **Egyenletesebb flow** — a víznek több kávén kell keresztülhaladnia, ami egyenletesebb ellenállást hoz létre a teljes ágyon
- **Kevesebb channeling** — a vastagabb pucköt nehezebb a víznek megkerülnie (shortcut)
- **Nagyobb ellenállás** — mélyebb puck = hosszabb kontaktidő ugyanazon őrlési beállítás mellett, így lehet, hogy kicsit durvábbra kell őrölni
- **Az optimális mélység-szélesség arány** nagyjából 2:3, a kiegyensúlyozott ellenállás és az egyenletes vízeloszlás érdekében

---

## Precíziós kosarak és puck prep

A precíziós kosarak egyenletesebbek, de kevésbé megbocsátóak is. Az egyenletes lyukmintázat azt jelenti, hogy a víz egyenletesen folyik *ha* a puck egyenletesen van eloszlatva — de ugyanilyen hűen fel is tárja az eloszlási hibákat.

**Stock kosárral:** Az egyenetlen lyukméretek miatt a vízfolyás már eleve egyenetlen. A te elosztásod kevésbé számít, mert a kosár a nagyobb változó.

**Precíziós kosárral:** A kosár már nem a leggyengébb láncszem. Most a puck prep lesz a korlátozó tényező. Ez azt jelenti:

- **A WDT fontosabbá válik** — azok a csomók, amelyeket egy stock kosár elfedhet, precíziós kosárral látható channelinget okoznak
- **Az egyenletes tamp jobban számít** — egy döntött tamp vékonyabb szekciót hoz létre, ami elsőként channelel
- **A dózis konzisztencia jobban számít** — mert a precíziós kosaraknak szűkebb dózis-ablakuk van

Ez egy funkció, nem hiba. Egy precíziós kosár megemeli az extrakció felső határát, de a puck preppel neked is hozzá kell tenned a magadét, hogy elérd azt. A precíziós kosár + jó WDT + egyenletes tamp kombinációja az, ami valóban egyenletes extrakciókat eredményez.

---

*A kosártípus specifikációiért (IMS, VST, stock), összehasonlításokért, ridged vs ridgeless és falgeometriáért lásd a `reference/BASKETS_REFERENCE.md` fájlt.*
