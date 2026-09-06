# DF64V Grinder Reference

> **Quick lookup:** For the adjustment system, espresso range table, and quick adjustment guide, see [`../grinders/DF64V.md`](../grinders/DF64V.md).

Detailed single-dosing workflow, seasoning schedule, commissioning, maintenance, and troubleshooting for the **DF64V Gen-3 variable-speed grinder** with factory-fitted **SSP Cast Lab Sweet V3 Red Speed espresso burrs** (64 mm flat, pre-installed).

---

## Single-Dosing Workflow

The DF64V is designed as a dedicated single-dose grinder. Retention is very low — typically **~0.1 g** — which is one of the machine's key features. Achieving that figure requires consistent bellows use.

### RDT (Ross Droplet Technique)

Static and clumping are common with flat burrs, especially in dry conditions or with light roasts:

- Add 1–2 drops of water to beans before grinding, or mist lightly with a spray bottle
- Alternatively, rub a damp finger over the beans
- RDT is not mandatory but significantly reduces static scatter and clumping; try it first before assuming a static problem is hardware

### Bellows: Mandatory, Not Optional

**Bellows use is mandatory** to achieve the ~0.1 g retention figure. The included bellows clear residual grounds from the grinding chamber and exit chute after the grind sounds complete:

1. When grinding sounds complete, **squeeze the bellows 3–5 times** into the exit chute
2. Without bellowing, residual grounds sit in the chamber and chute — retention climbs noticeably and your output weight becomes inconsistent
3. WDT the grounds after bellowing to break any clumps before tamping

### Full Single-Dose Workflow

1. Weigh beans to target dose — no retention allowance needed when bellows technique is consistent
2. Add RDT moisture if desired
3. Load beans into the dosing funnel/cup
4. Start the motor and confirm RPM (see [`../grinders/DF64V.md`](../grinders/DF64V.md))
5. Pour beans through the funnel
6. When grinding sounds complete, squeeze bellows 3–5 times
7. WDT grounds, tamp, and proceed

> **Dose allowance note:** With consistent bellows technique, dose input equals output. If output is consistently ~0.1 g short, either add that to the input dose or increase bellows count. Do not adjust grind setting to compensate for retention — they are independent variables.

---

## Seasoning Schedule

New SSP Cast Lab Sweet burrs (factory-installed or user-swapped) require a meaningful break-in period before grind settings are stable enough to trust:

| Phase | Coffee throughput | What to expect |
|-------|-------------------|----------------|
| Initial break-in | 0 – ~2 kg | Zero drifts coarser noticeably as surfaces bed in. Settings re-mean themselves week over week. Do not dial against early readings as if they are stable. |
| Early use | ~2 – ~5 kg | Settings begin to stabilise. The chirp point becomes more repeatable. Begin logging your zero-epoch anchor. |
| Settled | ~5 – ~10 kg | Full settling. Settings are reproducible shot-to-shot. Logged values from this phase carry forward reliably within the same zero-epoch. |

**Key points:**

- Break in with **coffee only** — not rice, not cleaning tablets. Rice does not correctly bed in espresso burrs and can skew the surface finish; cleaning tablets are a maintenance tool, not a seasoning medium.
- The ~5–10 kg settling range is drawn from DF64V + SSP Cast user experience (Home-Barista thread reports of ~7–9 kg). Earlier generic-SSP guidance (~2–3 kg) reflects lower-fines SSP lines and understates this burr's break-in requirement.
- **During break-in, treat all grind settings as provisional.** A grind logged at N marks from chirp at 1 kg throughput does not reproduce the same cup at 7 kg — the zero itself has drifted coarser. See [`../grinders/_NOTATION.md`](../grinders/_NOTATION.md) for the epoch-binding and row-superseding conventions.
- If your shot time is drifting coarser week-over-week without any intentional change, you are still in break-in. Do not keep chasing the drift by going finer without acknowledging the epoch drift in your log.

---

## Commissioning & Factory Alignment

### What Is Pre-Installed

The DF64V ships with the SSP Cast Lab Sweet V3 Red Speed burrs **factory-installed and factory-aligned**. There is **no user self-install step required**. Out of the box, you do not need to:

- Re-seat or re-torque the burrs
- Perform a full alignment procedure before first use
- Season the burrs on another grinder first

Unbox, run the chirp/zero procedure, and begin seasoning.

### Verify Alignment Within Your Return Window

Factory alignment is generally good but not guaranteed to be optimal for every unit. Verify alignment **within your return window** (typically 30 days from purchase) before putting significant coffee through the machine:

1. **Marker test:** Run a felt-tip marker across the flat face of the lower burr, then briefly run the grinder dry until the chirp point. Disassemble and inspect — even marker removal around the full circumference indicates good alignment; uneven removal indicates a high point on that side.
2. If pronounced misalignment is found, contact the vendor for a replacement unit or alignment shim set before the window closes.
3. Minor asymmetry is common and often self-corrects through break-in. Pronounced misalignment manifests as channeling, a wide spread of shot times, and an inability to grind fine enough for espresso — these are alignment symptoms, not burr limitations.

### "Can't Grind Fine Enough"

If the grinder cannot reach a fine enough setting to pull a normal-length espresso shot, the most common causes are:

1. **Misalignment or burr-face debris** — run the marker test; clean any coffee oil buildup from burr faces
2. **Still in early break-in** — surfaces are not yet bedded in; the zero may be coarser than its long-run position
3. **Zero-finding error** — re-zero carefully with the motor running, approaching slowly to the first chirp; an incorrectly found (too coarse) zero shifts the entire usable range coarser

This is **not a burr specification limit.** The Cast Lab Sweet V3 is an espresso-cut burr — the V3 re-cut adds approximately 15% more cutting edges compared to the filter-oriented V2. When properly aligned and broken in, it is fully capable of fine espresso settings.

---

## Motor Speed & Stall: Extended Notes

*(The RPM operating range is summarised in [`../grinders/DF64V.md`](../grinders/DF64V.md). This section provides troubleshooting depth.)*

### Low-RPM Stall

The DF64V occasionally stalls mid-grind. Understanding the actual cause is important — the common explanation is not the correct one:

**What the stall is:**
- Largely a **control-board protection mechanism** — the board cuts motor power when current draw exceeds a threshold. This is a safeguard, not a fundamental motor-torque limit.
- An early production run (~20 units, primarily 110V) shipped with a **defective pre-production control board** that triggered this protection far more aggressively than intended. If your unit stalls frequently even at 1000+ RPM with normal single doses, check your serial number with the vendor — a replacement board was made available for affected units.
- On correctly-functioning units, stalling at very low RPM (~600–800 RPM range) with a large, dense light-roast dose fed all at once is a known edge case, not a defect.

**What the stall is not:**
- A fundamental DC motor torque limitation
- A property of the SSP Cast burrs specifically
- Eliminated by fitting SSP Multipurpose burrs — the stall-elimination reported for some SSP Multipurpose users reflects that burr's lower fines production, not a board-level fix. The Cast line produces higher fines; this effect does not transfer.

**Mitigation:**
- Grind at **≥1000 RPM** for espresso — stall risk drops sharply above ~900 RPM
- Feed beans in **two half-doses** rather than all at once if stalling persists at normal RPM
- Avoid attempting very low RPM (below ~800) with dense light-roast single doses

### RPM as a Body/Clarity Lever

Higher RPM is sometimes presented as a way to add body (more RPM → more fines → fuller texture). This is **contested and partly contradicted by measurement**:

- One rigorous independent measurement (McKeon Aloe) found higher RPM shifted the distribution *coarser* with fewer fines — the opposite of the vendor-reported direction
- The "RPM is a body lever" framing is rated "a hot topic of debate" by independent reviewers
- Hoffmann's blind tasting found no clean burr-shape → body/clarity correlation

**Treat RPM as a coarse operational setting, not a calibrated body dial.** The primary practical consequence of changing RPM is that your grind setting needs a re-dial (RPM affects the flow-time at a given collar position). Use ~1000–1200 RPM as your default; experiment carefully and note any cup-character changes, but don't dial against RPM as if the vendor framing is confirmed.

---

## Maintenance Schedule

### Before Each Session
- Check the dosing funnel is clear of any yesterday's fines
- Quick bellows squeeze to purge any stale grounds from the chute

### Daily (Active Use)
- Brush the exit chute and residual grounds from the funnel
- Empty and wipe the dosing cup

### Weekly
- Remove the dosing funnel; brush fines from around the upper burr carrier lip
- Wipe the accessible burr face with a dry cloth or soft brush
- Check for static buildup on the exterior

### Monthly
- **Full access clean:** Remove the upper burr carrier (follow vendor procedure); brush both burr faces and the grinding chamber; vacuum out the chamber carefully (do not use compressed air directly on the burrs)
- Inspect burr faces for embedded coffee oils — excessive oil buildup can affect grind distribution and mask wear
- Re-zero after reassembly — **always re-zero after any disassembly**

### Every 500–1000 kg (or When Wear Is Evident)
- Burr replacement (see Burr Wear Indicators below)
- Full chamber clean and inspection

---

## Burr Wear Indicators

Replace the SSP Cast Lab Sweet V3 burrs when you observe:

- **Grind requires noticeably finer setting for the same shot time**, in a settled (post-break-in) grinder with no recipe changes — this is true zero drift, not break-in drift
- **Increased fines and clumping** that cleaning does not resolve
- **Visible edge dulling** on the cutting teeth under strong magnification or a loupe
- **Cup character shift** — a well-known coffee starts tasting flat or muddled without a recipe change, and the problem persists after a thorough clean

Typical life for espresso-grade SSP burrs: **500–1000 kg**, varying by roast level (darker roasts are softer and cause slower burr wear; lighter roasts are harder and cause faster wear).

---

## Common Issues

### Grinder Does Not Start / No Motor Response
- Check the dosing funnel or lid is properly seated — the DF64V has a safety interlock that prevents the motor from starting if the top is not correctly fitted
- Check the power connection and on/off switch
- If the motor hums but does not spin, the control board protection may have tripped; power-cycle with a 30-second wait before restarting

### Stall Mid-Grind
See *Low-RPM Stall* in the Motor Speed section above. Quick mitigation: increase RPM to ≥1000, split the dose into two half-feeds, and retry.

### Inconsistent Shot Times (Shot-to-Shot)
- Most common during **break-in** — the zero is drifting coarser; log the epoch and treat settings as provisional until the 5–10 kg settled phase
- Inconsistent bellows technique produces variable output weight, which produces variable shot time — standardise the bellows count first before adjusting grind
- Check for channeling (this is a puck prep issue, not a grind issue — see CLAUDE.md Core Rules)

### Grounds Scattering / Excessive Static
- Use RDT before grinding
- Check ambient humidity — very dry conditions amplify static significantly
- A metal or glass dosing cup reduces scatter compared to plastic

### Grinder Hums but Burrs Do Not Turn
- Foreign object lodged in the burr gap — **do not force the motor**; power off immediately and disassemble to clear
- If no object is found, contact the vendor (possible motor or board fault)

---

*For your personal successful settings, see `grind-map.md` in the project root. For the logging format and epoch conventions, see [`../grinders/_NOTATION.md`](../grinders/_NOTATION.md).*
