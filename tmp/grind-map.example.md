# Grind Map

A record of grind settings from rated shots. When you rate a shot with a grind setting, it gets added here automatically. The Rating column tells you whether the shot worked.

## Shot History

| Coffee | Roast | Process | Origin | Days Off Roast | Grind | RPM | Profile | Ratio | Temp | Rating | Date | Puck Screen? |
|--------|-------|---------|--------|----------------|-------|-----|---------|-------|------|--------|------|--------------|
| Example Roaster Ethiopia Yirgacheffe | Light | Washed | Ethiopia | 21 | 14 | 1100 | Bloom Slide | 1:2.5 | 94°C | 5 | Jan 15 |  |

*Grind = marks open from chirp zero (DF64V); recorded as a bare integer. See `knowledge/grinders/_NOTATION.md` for the full notation contract, epoch-binding convention, and seasoning caveats.*

*RPM — variable-speed grinder RPM as an integer (e.g. `1100`); leave blank for fixed-speed grinders.*

*Days Off Roast is optional—use "—" when roast date is unknown.*

*Puck Screen? — "Y" if a screen was installed, blank if unknown. Blank is NOT "no screen" — use "N" to record explicit absence; this distinction matters because new rows from /shot-feedback are blank-as-unknown for back-compat.*

---

*This file is automatically updated when you rate shots with grind settings provided.*
