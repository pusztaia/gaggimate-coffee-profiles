# Profile Gallery

## Általános célú profilok

### 9 Bar Espresso

![9 Bar Espresso](profiles/9-bar/profile-9bar-profile.png)

### Cremina lever machine

![Cremina lever machine](profiles/cremina-lever/profile-lever-profile.png)

### Damian's LM Leva

![Damian's LM Leva](profiles/damians-lm-leva/profile-lmleva-profile.png)

### Adaptive v2

![Adaptive v2](profiles/adaptive-v2/profile-adapt-profile.png)

---

## Time Based profilok (V1)

Ezek a profilok időalapúak. A shot a beállított másodpercig fut; a hozamot külön mérlegen kell figyelni.

### Wangera Stable Start 38s 94.5C – Time Based

![Wangera Stable Start 38s 94.5C](profiles/wangera/wangera-profile.png)

### Burundi Mubuga Melon Currant 38s – Time Based

![Burundi Mubuga Melon Currant 38s](profiles/burundi-mubuga/burundi-mubuga-profile.png)

### Colombia Manos Juntas Jam Mango 39s – Time Based

![Colombia Manos Juntas Jam Mango 39s](profiles/colombia-manos-juntas/colombia-manos-juntas-profile.png)

### Kirinyaga PB Tea Rose 37s – Time Based

![Kirinyaga PB Tea Rose 37s](profiles/kirinyaga/kirinyaga-profile.png)

### Twenty Eight Finca el Recreo Caturron Flavor 42s – Time Based

![Twenty Eight Finca el Recreo Caturron Flavor 42s](profiles/twenty-eight-caturron/twenty-eight-caturron-profile.png)

### El Salvador Ochupse Grape Rose 31s 93C – Time Based

![El Salvador Ochupse Grape Rose 31s 93C](profiles/el-salvador-ochupse/el-salvador-ochupse-31s-93c-profile.png)

---

## Bluetooth Scale Edition profilok (V2)

Ezek a profilok BOOKOO Themis Ultra Bluetooth mérleggel automatikusan megállnak a céltömegnél. A grafikonok a fázis/nyomás/flow értékeket mutatják – a tényleges shot hossza a mérleg stopjától függ.

### Wangera Stable Start 94.5C – Scale V2

![Wangera Scale V2 94.5C](profiles/wangera/wangera-stable-38s-945c-scale-v2-profile.png)

### Wangera Stable Start 94.0C – Scale V2

![Wangera Scale V2 94.0C](profiles/wangera/wangera-stable-38s-scale-v2-profile.png)

### Burundi Mubuga Melon Currant – Scale V2

![Burundi Mubuga Scale V2](profiles/burundi-mubuga/burundi-mubuga-38s-scale-v2-profile.png)

### Colombia Manos Juntas Jam Mango – Scale V2

![Colombia Manos Juntas Scale V2](profiles/colombia-manos-juntas/colombia-manos-juntas-39s-scale-v2-profile.png)

### Kirinyaga PB Tea Rose – Scale V2

![Kirinyaga Scale V2](profiles/kirinyaga/kirinyaga-tea-rose-37s-scale-v2-profile.png)

### Twenty Eight Finca el Recreo Caturron Flavor – Scale V2

![Twenty Eight Caturron Scale V2](profiles/twenty-eight-caturron/caturron-flavor-42s-scale-v2-profile.png)

### El Salvador Ochupse Grape Rose – Scale V2

![El Salvador Ochupse Scale V2](profiles/el-salvador-ochupse/el-salvador-ochupse-31s-93c-scale-v2-profile.png)

### Honduras Las Calaveras – Scale V2

![Honduras Las Calaveras Scale V2](profiles/honduras-las-calaveras/honduras-las-calaveras-scale-v2-profile.png)

---

## Megjegyzés a V2 grafikonokhoz

A V2 Scale Edition grafikonokat a `tools/render_profiles.py` script generálja a `*-scale-v2.json` fájlokból:

```bash
python3 tools/render_profiles.py
```

A V2 grafikonok az időalapú V1 grafikonokhoz hasonlók (azonos fázis/nyomás/flow értékek), de a fázisok duration értékei hosszabbak, mivel a tényleges shot stop a mérleg által vezérelt.
