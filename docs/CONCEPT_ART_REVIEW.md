# Concept Art Review

Files: `docs/concept-art/CA-01_cockpit_ballistic.png`, `CA-02_cockpit_beams.png`, `CA-03_third_person.png`.

**Ruling:** these images are **mood references only**. Where they disagree with `PRODUCT_BIBLE.md`, the bible wins. Do not hand them to an artist or an image model as a spec without the corrections below.

## Keep (these match the bible)

- Weathered industrial steel, welded plates, yellow/black hazard stencils (§12 human tech).
- The twin-weapon composition from a seated first-person view, with the hands connected to handles (§4).
- **Heat bars on the cannon housings and a central lower frame panel.** This is exactly the HUD placement in §11.
- Amber/orange muzzle discharge (§2, §5).
- A lit underground settlement below. This is a good starting point for Haven Nine's mood.
- Cyan friendly UI (§12 palette).

## Change (these contradict the bible)

| # | Seen in | Concept art shows | Bible says | Correction for the next art pass |
|---|---|---|---|---|
| 1 | CA-01, CA-02 | Enclosed cockpit with a glass canopy and a ceiling bar | Open-frame seat, mostly unobstructed forward view (§4) | Remove the canopy and roof. Show the knee guard, hydraulic braces and open sky/cavern above. |
| 2 | CA-01, CA-02 | "L-GUN 482 / R-GUN 468" ammo counters | Unlimited ammo; heat is the only limit (§5) | Remove the ammo readouts. Show heat only. |
| 3 | CA-01 | Rotary miniguns with belt-fed rounds | HCP-40 pulse cannon: one heavy shot + a thick tracer (§5) | Single heavy barrel with ionisation coils. No belts. |
| 4 | CA-02 | Continuous beams converging on one target | Explicitly *not* a continuous beam (§5) | Short, thick amber tracers with a visible gap between shots. |
| 5 | CA-01–03 | Red-eyed, many-tentacled flying machines in swarms | Veyr = folded mineral plates, ceramic cores, off-centre symmetry. Avoid recognisable *Sentinel* silhouettes (§2, §12) | Redesign from the §7 silhouettes: low triangle (Shardling), diamond with fins (Needle), etc. **No tentacles, no red eye-dots.** |
| 6 | CA-01, CA-02 | "WAVE 03/10", "ENEMIES 047", dozens of enemies on screen | 2 missions, authored phases, **≤8 active enemies** (§14) | Show at most about 8 readable enemies. Remove wave/enemy counters. |
| 7 | CA-01, CA-02 | Screen-space HUD panels in the corners | Diegetic, world-space HUD on the frame, 1–2 m away (§11) | Move information onto the frame and the cannon housings. VR has no screen corners. |
| 8 | CA-01, CA-02 | Labels "NEON SWARM VR", "EXOSUIT MX-7" | Title ETM (codename); rig is RIG-6 | Use RIG-6. Use no title text until the name is cleared. |
| 9 | CA-03 | Third-person camera, walking legged mech | First-person only. RIG-6's walking system is damaged and it is a seated, anchored frame (§3, §4) | Acceptable only as marketing key art *after* the redesign. Never as gameplay reference. |
| 10 | CA-03 | **"Defend Zion"**, **"Repel the Sentinel wave"**, green radar | Franchise names and green-code identity are banned (§2) | **Remove at once.** This is a direct IP risk in a public repo (see P-16). |
| 11 | All | Very dark scenes lit by emissives | "Avoid excessive darkness; headset readability first" (§12) | Raise ambient light. Attack cues must be the brightest thing in frame. |

## Brief for the next concept pass (copy-paste)

> First-person, seated in an open industrial lifting frame (no canopy, no roof). Two single-barrel heavy pulse cannons on articulated arms, heat gauges on each housing, no ammo counters. Underground civil-defence chamber, emergency amber lighting, readable mid-tone exposure. 4–6 alien machines made of folded graphite mineral plates with pale ceramic cores. Asymmetric, unfolding geometry. No tentacles, no glowing red eyes. Short, thick amber tracers. All UI is attached to the frame. No text, logos, or franchise references.
