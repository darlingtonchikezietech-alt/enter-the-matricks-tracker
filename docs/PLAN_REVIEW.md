# Plan Review: Product Bible v1.0 → v1.1

**Reviewed:** 2026-11-16 · **Reviewer:** Claude (AI) · **Result:** 22 patches applied to `docs/PRODUCT_BIBLE.md`, each tagged `[P-xx]` in the text.

How the review was done:
- Read the bible end to end and checked every cross-reference (timeline ↔ checkpoints ↔ health ↔ enemy values ↔ boss specs ↔ budgets).
- Recomputed every number with `tools/balance_sim.py`. It runs in CI with `--check`, so a future tuning change that breaks a design rule fails the build.
- Checked current platform facts. Meta has announced that Quest 2's final OS is v2.13 and that new Quest 2 app submissions close in December 2027.
- Compared the three concept images with the bible (see `CONCEPT_ART_REVIEW.md`).

Severity: **Blocker** = the plan contradicts itself or can't ship as written · **Major** = a designer or engineer would have to guess · **Minor** = clarity.

| ID | Sev | Area | Problem found (the "loop") | Patch applied |
|---|---|---|---|---|
| P-01 | Blocker | Heat (§5) | Venting was allowed during an overheat lock. The sim showed that "hold the trigger until it locks, then vent" makes 98 dps per cannon and beats skilled burst play (91 dps). That breaks the heat-discipline pillar. Vent vs passive stacking was also undefined. | Venting is disabled while locked. Vent replaces passive cooling (they don't stack). The shot that crosses 100 still fires. Burst play now wins: 91 vs 60 dps. |
| P-02 | Major | Damage (§5, §7, bosses) | It wasn't clear whether boss nodes and cores get the ×2 weak-point bonus. Boss time-to-kill swings by 2× depending on the reading. Bulwark's shield was only described as "highly resistant". | Defined the list of designated weak points (all ×2), raw-HP convention, Bulwark shield ×0.1. |
| P-03 | Major | Level 1 (§9) | The text said 60 non-boss enemies. The storyboard rows add up to **51**. | Changed to 51. CI checks it. |
| P-04 | Blocker | Checkpoints (§6) | "Boss checkpoints restore a preset" but the checkpoint list had no boss checkpoints. Dying to the Gatebreaker would replay 2+ minutes. | Added boss-start checkpoints (L1 07:15, L2 05:00) and defined the preset values. |
| P-05 | Major | Health (§6) | Repair was defined only for Level 1's midpoint, while Level 2 also has one. | +60 rig at both midpoints. The objective is never repaired mid-level. |
| P-06 | Blocker | Conductor | "Recurring attack interrupts reopen the core" had no mechanic behind it. At 50% accuracy the core needs about 4 windows, but only 3 node sets exist, so the boss could softlock. | Added a sweep emitter (160 HP) exposed at every sweep warning. Breaking it opens the core for 5 s. Sweeps repeat about every 10 s. |
| P-07 | Major | Conductor | Pairing failure state was undefined. | Both nodes reset to full and reopen after 3 s. |
| P-08 | Major | Conductor / brace | The storyboard said the Conductor "redirects attacks toward the junction", but players are told to brace against the sweep, and brace doesn't protect the objective. | The sweep targets the rig (braceable). Junction pressure comes from adds. |
| P-09 | Major | Enemies (§7) | Missing values: Bulwark has no attack, Lance chamber and bomber pod have no HP, Gatebreaker and Conductor attacks have no damage, Shardling's rig behaviour is unclear. | Filled in every value; see §7 "Initial damage values". |
| P-10 | Major | Gatebreaker | "Core opens after each *failed* attack cycle" was ambiguous (interrupted? completed?). The trigger for phase 3 was undefined. | The core opens after every furnace attack: 6 s if interrupted, 4 s if not. Phase 3 starts at ≤30% core. |
| P-11 | Major | Controls | Snap-rotating the rig swings the ±65° aiming envelope away from fixed lanes, so a player could rotate threats out of reach. | No snap rotation in combat. Forward re-anchor moved to the pause menu. |
| P-12 | Major | Controls | Grip-to-vent: players squeeze grip naturally while "holding" handles, which causes accidental vents that block firing. | 0.85 analog threshold + 100 ms hold. M1 A/B-tests an alternative mapping. |
| P-13 | Minor | Timing (§8) | "Narrative minimum" was undefined. | 60% of the phase slot + required dialogue finished. |
| P-14 | Blocker | Narrative timing | Train/power progress could visibly finish while the boss is still alive, or the train could leave a slow player behind. | Progress is capped at 90% until the final core dies. The last 10% plays in the resolution beat. |
| P-15 | Blocker | Platform | **New fact:** Meta has made Horizon OS v2.13 Quest 2's final feature release and accepts new Quest 2 apps only through **December 2027**. | Hard deadline added: target submission Q3 2027, no dependence on post-v2.13 features. |
| P-16 | Blocker | IP / title | "Enter The Matricks" is phonetically near-identical to *Enter the Matrix* (2003), an existing game in the very franchise §2 says to avoid. Concept art CA-03 also uses "Defend Zion" and "Sentinel". The repos are public. | Risk raised to High. ETM is an internal codename only. No public branding until clearance. Franchise terms banned from all assets and prompts. *Not legal advice.* |
| P-17 | Major | Concept art | The images contradict the bible on canopy, ammo, weapon type, enemies, HUD, and camera. | `CONCEPT_ART_REVIEW.md` governs. The images are mood reference only. |
| P-18 | Minor | Weapons | No max range or damage falloff defined. | 60 m trace, no falloff. |
| P-19 | Minor | Health | "Repair fixed between selected encounter phases" was vague. | Merged into P-05 with exact times. |
| P-22 | Minor | Level 1 arena | "Transfer equipment sits beyond the player's rig" could read as *behind*, which conflicts with "never look behind". | In front and below, centre lane. |
| P-24 | Major | Schedule | The 16-week plan had no calendar anchor, so it couldn't be checked against the P-15 deadline. | Weeks are anchored to the team start date in `DEVELOPMENT_PLAN.md`, with ≥12 weeks of slack before the cutoff. |
| P-30 | Minor | Scoring | "Damage prevented" was undefined. | Brace-absorbed damage + damage from interrupted attacks. |

(P-20, P-21, P-23 and P-25–P-29 were checked and need no change: overheat timing ≈3 s ✔, both-cannon peak 320 dps ✔, Needle Drone killable in its 1.5 s telegraph ✔, active caps match the performance budget ✔, Level 2 population 39 ✔, the 72 Hz frame maths ✔.)

## Key numbers after the patches (from `tools/balance_sim.py`)

- A cold cannon overheats after **2.75 s / 12 shots**. Overheat recovery takes **4.0 s** (passive only).
- Sustained output per cannon: trigger held **60 dps**, burst + vent **91 dps**. Both cannons ≈ **181 dps** against a 320 dps theoretical peak. Encounter designers should plan around about 180, not 320.
- Gatebreaker core: **~2.2 exposures** at 70% accuracy. Conductor core: **~2.7** at 70% and **~3.8** at 50% (so the P-06 fallback is needed).

## Open questions for the owner (not decided by this review)

1. Final title and naming-clearance budget (P-16).
2. Team start date. Without it, M0–M5 can't be put on a calendar (P-24).
3. Should PCVR or Quest 3 become the *lead* platform if the Quest 2 deadline slips? This would be a scope decision, logged as an ADR.
