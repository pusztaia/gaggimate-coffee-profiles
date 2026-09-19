# Bluetooth Scale Workflow

**Hardware:** BOOKOO Themis Ultra + GaggiMate Pro + Gaggia Classic Pro 2025

---

## 1. Pairing

### Prerequisites

- Latest GaggiMate Pro firmware installed
- BOOKOO Themis Ultra scale charged (min. 50%)
- GaggiMate Web UI available on the local network

### Pairing steps

1. Turn on the BOOKOO Themis Ultra scale
2. Open the GaggiMate Web UI (IP address shown on the GaggiMate display)
3. Navigate to the **Settings → Scale** menu
4. Click the **Scan** button – the BOOKOO Themis Ultra should appear in the list
5. Select it and click **Connect**
6. Connection success is indicated by the Web UI status bar and the scale LED
7. The GaggiMate remembers the scale; it will reconnect automatically on the next power-up

### Verification

- In the GaggiMate Web UI, the scale status should be **Connected**
- Place a known-weight object on the scale and confirm that the weight appears in the Web UI
- If the scale does not appear in the Scan list: turn it off and on again, then retry

---

## 2. Calibration

### When to calibrate?

- Before first use
- If the measured value differs from reality by more than ±0.5 g
- If the scale has been dropped or struck
- Monthly sanity check is recommended

### Calibration steps

1. Turn on the scale and let it warm up for 2–3 minutes
2. Make sure the scale is sitting on a level surface
3. Remove all objects from the scale
4. Press and hold the **Tare** button to zero it
5. For internal calibration of the BOOKOO Themis Ultra: see the scale manual
6. Verification: place a known calibration weight on the scale

### Tare workflow per shot

1. Place the cup on the scale
2. **Tare** (zero) – the display should read 0.0 g
3. Insert the portafilter into the machine
4. Start the shot

> Important: Always perform tare before starting the shot, with the cup in place. GaggiMate measures the beverage weight after tare.

---

## 3. Shot workflow

### Full workflow (V2 Scale Edition profile)

1. **Turn on the scale** – let it stabilize for 1–2 minutes
2. **GaggiMate Web UI** – confirm that the scale status is Connected
3. **Load the profile** – import the desired `*-scale-v2.json` file in the Web UI (**Profiles → Import**)
4. **Dose the coffee** – 18.5 g (DF64V Gen 2, according to the profile labeling)
5. **Puck prep** – WDT, tamp, puck screen (dry and clean)
6. **Insert the portafilter**
7. **Place the cup on the scale** – empty cup, then tare the scale
8. **Start the shot** – the GaggiMate starts the profile
9. **Automatic stop** – the GaggiMate stops when the beverage weight reaches the `stop_at_g` value
10. **Yield check** – the scale displays the final value; record it in the shot log

### V2 profile stop logic (GaggiMate 1.8.1 firmware)

| Phase | Stop trigger | Notes |
|---|---|---|
| Preinfusion (Wetting, Saturation, Bloom) | Time-based (duration hard cap) | No volumetric target configured |
| Ramp | Time-based (duration hard cap) | No volumetric target configured |
| Extraction | **Volumetric target (grams)** | OR condition: when the target fires, the phase ends |
| Extraction – fallback | Duration hard cap | If scale is disconnected or target does not fire |
| Finish | Time-based (duration hard cap) | Only if the Extraction target fired |

**How the `targets` work in the firmware:**

- The `targets` array is **phase-scoped** – each phase can define its own target
- Evaluation: every **100 ms**
- OR logic: the first firing target immediately closes the phase
- For `pro` type, `duration` is always a **hard cap** – the target can only stop sooner, never keep the phase open longer
- A `volumetric` target works only when an active Bluetooth scale is connected and brew-by-weight mode is enabled; if these are missing, the target silently does not fire and the duration takes over as the stop condition

---

## 4. Typical issues and troubleshooting

### The scale does not appear in the Scan list

**Possible causes and solutions:**

| Cause | Solution |
|---|---|
| Scale is off | Turn it on and wait 5 seconds |
| Bluetooth distance is too large | Move the scale closer to the GaggiMate |
| Another device is occupying Bluetooth | Turn off Bluetooth on all other devices |
| Firmware version is not correct | Update the GaggiMate firmware |

### Bluetooth connection drops during a shot

**Symptoms:** The safety timeout kicks in; the shot does not stop at the target weight.

**Solutions:**

1. Check the distance – max. 1–2 meters recommended
2. Remove nearby electrical interference (microwave, WiFi router)
3. Update the BOOKOO Themis Ultra firmware (BOOKOO app)
4. If it keeps disconnecting: re-pair the scale

### Measured yield differs from expected

**Symptoms:** The scale stops at 42.0 g, but the actual yield is different.

**Possible causes:**

| Cause | Solution |
|---|---|
| Tare was not zeroed | Always tare after placing the cup |
| Cup shifted | Secure the cup |
| Scale is not level | Check and adjust the scale feet |
| Dripping after stop | Normal; reducing the final pressure on the GaggiMate may help |

### The shot stops earlier than the target weight

**Causes:**

- The beverage weight trigger fires early in extraction (rare if there is early dripping)
- Scale zeroing issue

**Solution:** Check the tare value before the shot; if necessary, increase `stop_at_g` by 0.5–1.0 g.

### The safety timeout triggers (not beverage weight)

**Symptoms:** The shot stops at the timeout duration rather than the target weight.

**Causes and solutions:**

| Cause | Solution |
|---|---|
| Bluetooth connection dropped | Check pairing and proximity |
| Flow too slow (restricted puck) | Check WDT, tamp, and puck screen; grind coarser if needed |
| Safety timeout too short | Increase the `safety_timeout_s` value in the JSON |

---

## 5. Troubleshooting summary

| Symptom | Likely cause | Solution |
|---|---|---|
| Scale does not connect | Firmware, distance | Update, move closer |
| Disconnect during shot | Interference, distance | Move closer, re-pair |
| Yield differs | Tare error, uneven scale | Check tare, level surface |
| Safety timeout triggers | BT drop / restricted flow | Pairing + puck prep |
| Shot too short | Early trigger | Increase `stop_at_g` by 0.5 g |
| Shot too long | Timeout expires | Check Bluetooth, improve flow |

---

## 6. Recommended settings by profile

| Profile | stop_at_g | safety_timeout_s |
|---|---:|---:|
| Kenya Wangera 94.5C | 42.0 g | 45 s |
| Kenya Wangera 94.0C | 42.0 g | 45 s |
| Burundi Mubuga | 42.5 g | 45 s |
| Colombia Manos Juntas | 43.0 g | 47 s |
| Kenya Kirinyaga PB | 43.0 g | 45 s |
| 28 Caturron | 42.0 g | 50 s |

You can adjust the `stop_at_g` and `safety_timeout_s` values in the JSON profile if your dial-in requires a different yield.
