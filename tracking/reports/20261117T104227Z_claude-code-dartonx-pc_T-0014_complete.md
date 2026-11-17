---
time: 2026-11-17T10:42:27Z
agent: claude-code-dartonx-pc
task: T-0014
kind: complete
commits: 56bd975
---

Shardling and Needle Drone (Source/ETM/Enemies/Archetypes). Shardling: 80 HP, tagged ETM.InfrastructureAttacker, straight ground approach to the objective (finds the mission's objective if none is set; typed AMissionObjective so it can never target the rig), stops at 1.5 m, raises its cutting limbs over 1 s, cuts 20, then destroys itself. Needle Drone: 120 HP, flies to a hover point (assigned, or 4 m above spawn), faces the rig, shows an aiming line from drone to rig and a rising-pitch tone for 1.5 s, bursts 15 to the rig, then a 3 s cooldown; staggering it also starts the cooldown. Placeholder silhouettes from engine basic shapes: low cone body, four legs and two blades; cube diamond with two fins. Both reuse cleanly from the pool.
Verified: Built ETMEditor Win64 Development on UE 5.8.4 after a clean ETM intermediate delete, zero errors and warnings, with T-0044's unity fix applied locally (this branch fails to build without it). 5 new automation tests (ETM.Enemies.Archetypes.*) pass with real objective, rig integrity, brace and pool: values match bible section 7, cut lands only after the 1 s raise, rig never hit by Shardlings, kill mid-warning prevents the cut and the burst, burst 15 and braced 3.75, aiming line spans drone to rig, tone pitch rises, pooled reuse resets limbs, hover and aim line. All 24 tests pass. No headset, no level, nothing seen rendered.
Remaining: Telegraph sound: the audio components and pitch ramp exist, but no sound asset is assigned (none exists in the project), so the sound half of the shape+sound acceptance is wired but not audible. Shape cues are placeholders, not art. No navigation, lanes or obstacle avoidance: the director (T-0017) chooses spawn points and hover points. Attack tokens and the 6-drone cap are the director's. Move speeds 250/400 cm/s, attack range 1.5 m, drone cooldown 3 s and hover 4 m are my prototype values, not bible values. A Shardling's self-destruct broadcasts OnKilled like a player kill; scoring (T-0031) must tell them apart. Branch is stacked on T-0018 and needs T-0044 merged first.
Next: Review T-0014 and T-0044. Ready after approval: T-0017 (director), T-0022 (Bulwark, Lance, Siphon, Cradle).
