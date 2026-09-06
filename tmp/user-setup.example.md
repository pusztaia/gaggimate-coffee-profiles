# User Setup

## Equipment

| Component | Details |
|-----------|---------|
| **Machine** | Gaggia Classic Pro + Gaggimate Standard |
| **Grinder** | Baratza Encore ESP (flat burr, stepped adjust) |
| **Basket** | IMS Baristapro Nanotech 18g (ridgeless) |
| **Scale** | Felicita Arc (Bluetooth), auto-stop enabled, 250ms predictive delay |
| **Puck Screen** | None |
| **Operating RPM** | |

## Workflow

- **Puck Prep**: WDT → OCD leveler → tamp
- **Shot Stop**: Automatic via Bluetooth scale

## Preferences

- **Primary Drinks**: Flat whites, lattes, americanos
- **Roast Preference**: Medium to medium-dark roasts
- **Flavor Profile**: Chocolate, caramel, and nutty notes — approachable and sweet

## Active Coffee

No active coffee. Use /new-coffee to set one, or tell me what you're brewing.

## Bluetooth Scale & Auto-Stop

The Felicita Arc connects to the Gaggimate via Bluetooth Low Energy (BLE) for automatic shot stopping.

**Scale specs:** 2000g capacity, 0.1g resolution, fast response time. Modes: Weight, Flow, Ratio, Auto.

**How predictive stop works:**
- The scale monitors real-time weight and flow rate during extraction
- When the flow rate and current weight indicate the target will be reached, the scale sends a BLE stop signal to the Gaggimate
- The **250ms predictive delay** is the time between the Gaggimate receiving the stop signal and the pump actually stopping — accounting for water already in transit through the puck and in the spout

**Calibration:**
- If shots consistently **overshoot** the target weight by >1g → increase the delay (e.g., 300ms) so the stop signal fires earlier
- If shots consistently **undershoot** the target weight → decrease the delay (e.g., 200ms) so the stop signal fires later
- Typical adjustment range: 100-300ms. Start at 250ms and adjust in 50ms increments based on results

**Troubleshooting:**
- **0g reads / very low dose out:** Cup was likely removed before the scale registered final weight
- **Connection drops:** Move scale closer to machine; avoid metal objects between scale and Gaggimate
- **Scale not found:** Ensure scale is awake and not connected to another app. Only one BLE connection at a time

## Notes

- **Dose = basket size.** With an 18g basket, dose 18g. Don't underdose.
- Medium roasts work well at 92-94°C — taste and adjust from there
- Encore ESP's stepped adjustment makes coarse moves easy; use half-steps for fine-tuning
- Gaggimate Standard enables pressure profiling — great for pre-infusion and gentle ramp profiles
- **Puck Screen (optional):** Default is "None" — leave as-is if you don't use one. Otherwise, fill in product details. Examples: `Normcore 58.5mm round-hole (0.8mm thin, 316 stainless)` or `Pesado Diffuser 58mm mesh (1.7mm thick)`.
- **Operating RPM (variable-speed grinders only):** Your current operating RPM — the home for the value skills read as a default and stamp into the grind map. Read the value as a plain **integer** = the current RPM; a missing/blank/`None`/non-integer value = unknown. This field is meaningful **only for variable-speed grinders** (e.g. the DF64V, signalled by a `## Motor Speed (RPM)` section in its `knowledge/grinders/` file); **fixed-speed grinders** (like the Baratza Encore ESP in this example) leave it blank or omit the row entirely. It is distinct from the grind map's per-shot historical RPM stamp: this field is the single current-value home, the grind map is the longitudinal record. **Create-if-absent:** when a skill needs to persist a new Operating RPM and the row is missing from `user-setup.md`, it adds the Operating RPM row — it does not assume the row already exists.
