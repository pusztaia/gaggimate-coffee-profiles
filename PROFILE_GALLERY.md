# Profile Gallery

## Általános célú profilok

### 9 Bar Espresso

![9 Bar Espresso](profiles/9-bar/profile-9bar-profile.png)

### Cremina lever machine

![Cremina lever machine](profiles/cremina-lever/profile-lever-profile.png)

### Damian's LM Leva

![Damian's LM Leva](profiles/damians-lm-leva/profile-lmleva-profile.png)

---

## Time Based profilok (V3)

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

---

## Bluetooth Scale Edition profilok (V4)

Ezek a profilok BOOKOO Themis Ultra Bluetooth mérleggel automatikusan megállnak a céltömegnél. A grafikonok a fázis/nyomás/flow értékeket mutatják – a tényleges shot hossza a mérleg stopjától függ.

### Wangera Stable Start 94.5C – Scale V4

![Wangera Scale V4 94.5C](profiles/wangera/wangera-stable-38s-945c-scale-v4-profile.png)

### Wangera Stable Start 94.0C – Scale V4

![Wangera Scale V4 94.0C](profiles/wangera/wangera-stable-38s-scale-v4-profile.png)

### Burundi Mubuga Melon Currant – Scale V4

![Burundi Mubuga Scale V4](profiles/burundi-mubuga/burundi-mubuga-38s-scale-v4-profile.png)

### Colombia Manos Juntas Jam Mango – Scale V4

![Colombia Manos Juntas Scale V4](profiles/colombia-manos-juntas/colombia-manos-juntas-39s-scale-v4-profile.png)

### Kirinyaga PB Tea Rose – Scale V4

![Kirinyaga Scale V4](profiles/kirinyaga/kirinyaga-tea-rose-37s-scale-v4-profile.png)

### Twenty Eight Finca el Recreo Caturron Flavor – Scale V4

![Twenty Eight Caturron Scale V4](profiles/twenty-eight-caturron/caturron-flavor-42s-scale-v4-profile.png)

---

## Megjegyzés a V4 grafikonokhoz

A V4 Scale Edition grafikonokat a `tools/render_profiles.py` script generálja a `*-scale-v4.json` fájlokból:

```bash
python3 tools/render_profiles.py
```

A V4 grafikonok az időalapú V3 grafikonokhoz hasonlók (azonos fázis/nyomás/flow értékek), de a fázisok duration értékei hosszabbak, mivel a tényleges shot stop a mérleg által vezérelt.
