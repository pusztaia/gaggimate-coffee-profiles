# Impresso Colombia Manos Juntas Jam Mango 18.5-43 – Scale V4

**Kávé:** Impresso Colombia Manos Juntas  
**Feldolgozás:** anaerobic natural  
**Eredet:** Colombia, Cauca, Manos Juntas micromill  
**Ízjegyek:** vörösáfonya dzsem · karamell · mangó  
**Setup:** DF64V Gen 2 + SSP Sweet Lab Espresso V3 / Gaggia Classic Pro 2025 + GaggiMate Pro / IMS B682TH24.5M kosár / BOOKOO Themis Ultra  
**Őrlőskála:** 0-90, egész jelölések  
**Fordulat:** 1200 RPM baseline  
**Stop:** Bluetooth-mérleggel, kétlépcsős beverage-weight target alapján  
**Verzió:** Scale V4 – 2026-07-17, javított automatikus megállás; a V4 fájlnév változatlan

---

## Profil grafikon

![Profile graph](colombia-manos-juntas-profile.png)

---

## Cél ízprofil

Dzsemes vörösáfonya, mangó és karamelles édesség. A shot legyen szirupos és gyümölcsös, de ne legyen fermentáltan nehéz, alkoholos vagy száraz.

---

## Alap recept

| Paraméter | Érték |
|---|---:|
| Dózis | **18.5 g** |
| Cél végső hozam | **43.0 g** |
| Várható tartomány | **42.5-43.5 g** |
| Arány | **kb. 1:2.32** |
| Hőmérséklet | **94.5 °C** |
| Őrlés indulás | **10 körül** |
| Őrlés tartomány | **10-11** |
| Fordulat | **1200 RPM** |
| Kosár | **IMS B682TH24.5M** |
| Finish indulása | **38.0 g** |
| Pumpa leállítása | **41.5 g** |
| Teljes biztonsági hard cap | **47 s** |

### Első shot

**18.5 g be · grind 10 körül · 1200 RPM · 94.5 °C · 38.0 g-nál Caramel Finish · 41.5 g-nál pumpastop · várhatóan kb. 43.0 g a csészében**

---

## Miért két tömeg-target van?

A GaggiMate `pro` profilban a `targets` tömb csak az aktuális fázist zárja le.

Ha a 43.0 g-os target kizárólag a Jam Extraction fázisban lenne:

1. 43.0 g-nál lezárulna a Jam Extraction;
2. elindulna a Caramel Finish;
3. a gép még tovább pumpálna;
4. a végső hozam jelentősen 43 g fölé futhatna.

A javított Scale V4 logika ezért kétlépcsős:

1. **38.0 g-nál** a Jam Extraction véget ér, és elindul a Caramel Finish.
2. **41.5 g-nál** a Caramel Finish is véget ér, ezért a pumpa leáll.
3. A stop utáni kifolyás várhatóan **42.5-43.5 g** körüli végső hozamot ad.

---

## GaggiMate Pro fázisok

| # | Fázis | Maximum idő | Hő | Pump target | Nyomás / Flow | Stop trigger |
|---:|---|---:|---:|---|---:|---|
| 1 | Jam Wetting | **5 s** | 94.5 °C | flow | 8.0 ml/s | idő |
| 2 | Mango Saturation | **8 s** | 94.5 °C | pressure | 2.3 bar / 4.5 ml/s | idő |
| 3 | Sweet Bloom | **4 s** | 94.5 °C | pressure | 0.5 bar / 0 ml/s | idő |
| 4 | Soft Ramp | **6 s** | 94.5 °C | pressure | 7.3 bar / 2.4 ml/s | idő |
| 5 | Jam Extraction | **16 s** | 94.5 °C | pressure | 7.3 bar / 2.1 ml/s | **38.0 g** |
| 6 | Caramel Finish | **8 s** | 94.5 °C | pressure | 5.5 bar / 1.7 ml/s | **41.5 g** |
|  | **Teljes hard cap** | **47 s** |  |  |  |  |

A `duration` értékek hard capek. Aktív BOOKOO mérleggel a tömeg-targetek várhatóan hamarabb lezárják az utolsó két fázist.

---

## Scale V4 profil

**Profilfájl:** [`colombia-manos-juntas-39s-scale-v4.json`](colombia-manos-juntas-39s-scale-v4.json)

A verziószám szándékosan **V4 maradt**. A fájl a javított, kétlépcsős stop-logikát tartalmazza.

### Stop-logika

| Fázis | Target | Funkció |
|---|---:|---|
| Jam Extraction | **38.0 g** | átváltás az alacsonyabb nyomású Caramel Finish fázisra |
| Caramel Finish | **41.5 g** | pumpa leállítása |
| Stop utáni kifolyás | kb. **1.0-2.0 g** | várható végső hozam kb. 43 g |

---

## Dial-in logika

| Eredmény | Következő lépés |
|---|---|
| **42.5-43.5 g, dzsemes/mangós/karamelles, szirupos** | Marad a profil és a 10 körüli őrlés. |
| **44 g fölé fut** | A Caramel Finish targetet csökkentsd **41.0 g-ra**. |
| **42 g alatt áll meg** | A Caramel Finish targetet emeld **42.0 g-ra**. |
| **Túl savas, kevés mangó/édesség** | Először emeld a végső stop targetet **42.0 g-ra**; csak utána próbálj 95 °C-ot. |
| **Túl nehéz, alkoholos vagy fermentált** | Csökkentsd a végső stop targetet **41.0 g-ra**, vagy a hőt 94.0 °C-ra. |
| **40 g alatt marad / hard cap lép be** | Bluetooth kapcsolat, tare és puck prep ellenőrzése; ha minden stabil, menj kissé 11 felé. |
| **Túl gyors, vékony vagy spriccel** | WDT/tamp/screen ellenőrzés; szükség esetén menj 10 felé finomabbra. |

---

## BOOKOO shot workflow

1. Kapcsold be a BOOKOO Themis Ultra mérleget.
2. Ellenőrizd a GaggiMate felületén, hogy a mérleg **Connected**.
3. Tedd fel az üres csészét.
4. Nullázd a mérleget.
5. Töltsd be a `colombia-manos-juntas-39s-scale-v4.json` profilt.
6. Indítsd el a shotot.
7. Ellenőrizd, hogy kb. **38.0 g-nál** elindul-e a Caramel Finish.
8. A pumpának kb. **41.5 g-nál** le kell állnia.
9. Jegyezd fel a teljes időt, a végső tömeget és az ízt.

---

## Rövid menthető recept

**Colombia Manos Juntas Jam Mango – Scale V4**

**18.5 g · grind 10 körül · 1200 RPM · 94.5 °C · finish 38.0 g · pumpastop 41.5 g · várható végső hozam kb. 43.0 g**
