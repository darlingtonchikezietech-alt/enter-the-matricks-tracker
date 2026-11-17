# ENTER THE MATRICKS
### VR Game Product Bible · Version 1.2

> v1.1 (2026-11-16) applies the patches logged in `docs/PLAN_REVIEW.md`. Patched passages carry a `[P-xx]` tag. The original is preserved at `docs/archive/PRODUCT_BIBLE_v1.0.md`.
> v1.2 (2026-11-17) adds P-31: Quest 3 and 3S ship in the first release, from the same build as Quest 2.
**Quest 2, 3 and 3S · Quest 2 sets the performance floor · Unreal Engine · Single-player survival shooter** **[P-31]**

> **Two cannons. One evacuation. Hold until the last signal.**

---

## 1. Product Definition

**Enter The Matricks** is a first-person VR survival shooter in which the player sits inside an open-frame industrial exoskeleton and operates two independently aimed heavy cannons during an alien-machine invasion.

The player’s body stays anchored while the battlefield erupts around them. Intensity comes from target prioritization, split-arm aiming, heat management, incoming attacks, and the responsibility of protecting an evacuation.

| Item | Definition |
|---|---|
| Primary platforms | Meta Quest 2, Quest 3 and Quest 3S, standalone, from one build. Quest 2 is the performance floor. **[P-31]** (New Quest 2 app submissions close December 2027; see P-15.) |
| Later platforms | PCVR; other headsets after validation **[P-31]** |
| Engine | Unreal Engine 5; version locked after hardware prototype |
| XR foundation | OpenXR, with platform-specific features behind adapters |
| Perspective | First-person, stereoscopic VR |
| Player position | Seated inside a fixed open-frame exoskeleton |
| Controls | Two tracked controllers; independent cannon aiming |
| Campaign | Two missions, approximately 10 minutes each |
| Intended successful run | Approximately 20 minutes, excluding menus, loading, pauses, and retries |
| Genre | Arcade survival defense with a short narrative |
| Initial scope | Offline single-player campaign and mission replay |
| Business model | Premium purchase; price decided after scope and market validation |
| Audience | Players who enjoy powerful weapons, readable combat, and short VR sessions |

**Product promise:** make the player feel physically connected to two massive weapons without requiring prolonged arm extension, artificial camera motion, or complex VR reloading.

### Design pillars

1. **Heavy firepower:** every shot has a distinct mechanical action, bright energy trail, and forceful impact.
2. **Independent hands:** the player can engage separate threats or concentrate both cannons.
3. **Readable chaos:** spectacle never hides attack warnings, weak points, or objectives.
4. **Comfortable intensity:** enemies and machinery move; the player’s viewpoint remains naturally tracked.
5. **Compact survival story:** every encounter advances the evacuation or reveals the invaders’ coordination.

### Explicitly outside the first release

Multiplayer, free-roaming locomotion, melee combat, hand tracking, procedural campaigns, crafting, inventory management, branching storylines, and a large upgrade tree.

---

## 2. Original IP Positioning

The game must establish its own visual language, fiction, terminology, and combat identity.

### Meaning of “Matricks”

Within the fiction, **MATRICKS** is the human nickname for a captured alien routing lattice: a physical machine network that synchronizes invasion units. The title refers to entering that network’s defensive perimeter.

This is a working fictional explanation. **[P-16]** The title is phonetically near-identical to *Enter the Matrix* (2003), an existing game in the franchise this bible tells us to avoid. Treat **ETM** as an internal codename only. No store page, trailer, domain, social handle or key art may use the title until naming and trademark clearance has a written result. Budget for a rename.

### Creative boundaries

| Establish | Avoid |
|---|---|
| Underground civil-defense infrastructure | Recognizable Matrix locations or compositions |
| Improvised industrial rescue technology | Franchise-specific exoskeleton designs |
| Alien machines built around folding mineral structures | Recognizable sentinels or other copied silhouettes |
| Amber weapon discharges and ceramic-white alien cores | Green code rain as the central identity |
| Evacuation, infrastructure failure, and survival | Chosen-one simulation mythology |
| Practical workwear and emergency markings | Signature franchise costumes, symbols, or dialogue |
| Heavy pulse-cannon combat | “Bullet time” presented through recognizable franchise staging |

**Visual signature:** exposed human hydraulics against alien machines that unfold like engineered mineral formations.

**Narrative signature:** a maintenance specialist buys time for ordinary people to escape.

**Gameplay signature:** two independently aimed heavy cannons, separate heat systems, and coordinated weak-point destruction.

---

## 3. World and Survival Narrative

### Setting

**Haven Nine** is an underground settlement beneath a devastated coastal industrial region. Its population survives through geothermal power, water recycling, and an old freight railway.

An extraterrestrial machine force, **the Veyr Assembly**, has reached the settlement. Its units dismantle infrastructure and rebuild it into relay structures. Their biological creators remain unseen.

The Assembly does not invade through speeches or negotiations. It measures, cuts, harvests, and connects.

### Principal characters

| Character | Role |
|---|---|
| **The Operator** | Player character; a maintenance specialist trained on industrial lifting frames |
| **Mara Venn** | Evacuation coordinator; delivers objectives and human stakes over radio |
| **RIG-6** | Exoskeleton diagnostic voice; concise operational feedback |
| **The Veyr Assembly** | Coordinated alien-machine invasion force |
| **The Conductor** | Local command machine directing the assault |

### Story synopsis

The outer wall of Haven Nine collapses during evacuation. Conventional defenses are already silent.

The Operator reaches **RIG-6**, a seated industrial exoskeleton retrofitted with two pulse cannons. Its walking system is damaged, but its stabilizers and weapons still function.

During **Level 1: The Breach**, the Operator holds a power-transfer chamber long enough to restore the evacuation railway. The attackers adapt with unsettling coordination. Destroying a siege machine reveals that every unit is responding to a local command signal.

Between missions, maintenance equipment relocates the exoskeleton during a brief fade to black.

During **Level 2: The Last Signal**, the Operator defends the railway’s final power junction and attacks the command machine through an exposed relay shaft. The evacuation train needs its power supply uninterrupted until departure.

The Operator destroys the Conductor’s synchronization core. Nearby machines lose coordination. The last train clears the tunnel as emergency shutters fall.

The ending confirms a local victory: the people of Haven Nine escape. A distant alien signal establishes that the wider invasion continues.

### Story delivery rules

- No forced camera movement or third-person cutscenes.
- Keep essential dialogue brief enough to understand during combat.
- Introduce objectives before peak combat.
- Repeat critical instructions through HUD text and spatial indicators.
- Use visible evacuation progress to make survival tangible.
- Avoid requiring the player to look away from active threats.

**Example opening line — Mara:**  
“RIG-6 still has weapons. Keep the transfer chamber alive, and I can move the train.”

**Example closing line — Mara:**  
“Last carriage is clear. You bought us a tomorrow.”

---

## 4. Player Embodiment and Controls

### The exoskeleton

RIG-6 is an **open-frame seated machine**, not an enclosed vehicle cockpit.

The player sees:

- A lower seat frame and protective knee structure.
- Two articulated weapon supports beside their arms.
- Independent cannon mechanisms and heat indicators.
- Hydraulic braces, cables, stabilizers, and limited protective plating.
- A mostly unobstructed forward battlefield.

The frame establishes scale and a stable reference without surrounding the player with opaque panels.

### First-person rules

- The headset controls the viewpoint directly.
- Cannons follow controller aim independently.
- Looking at a target does not automatically aim either cannon.
- Weapon recoil animates the cannon and support assembly, never the camera.
- No head bob, forced head rotation, impact camera shake, or artificial roll.
- Virtual hands connect to controls through inverse kinematics.
- Arm meshes must not stretch unnaturally when tracking reaches its limits.

### Input mapping

| Input | Action |
|---|---|
| Left trigger | Fire left cannon |
| Right trigger | Fire right cannon |
| Left grip | Vent left cannon while held |
| Right grip | Vent right cannon while held |
| A / equivalent primary button | Activate defensive brace |
| B / equivalent secondary button | Confirm contextual objective interaction |
| Left stick | Unassigned in combat **[P-11]** |
| Right stick | Unassigned in initial release |
| Menu button | Pause and comfort/settings menu |
| Pause-menu recenter | Recalibrate seated orientation and control offsets; includes **Forward re-anchor** (re-aligns the rig's forward to the player's current seated forward) **[P-11]** |

Platform-reserved controls remain reserved. Final mappings must be checked against the selected runtime and controller profile.

**[P-11] Why no snap rotation:** rotating the rig in combat swings the ±65° aiming envelope away from the authored lanes and the objective, so a player could turn the threats out of reach. Seated players who need a different forward use Forward re-anchor from pause.

**[P-12] Grip-to-vent risk:** players naturally squeeze grip while "holding" the handles the virtual hands are attached to. Vent triggers only above **0.85 analog grip** held for **100 ms**. M1 must test this against an alternative (vent on X/A hold with brace moved to stick-click) and record the winner in `docs/decisions/`.

### Reach and aiming

Prototype aiming envelope:

- Approximately **±65° horizontal per cannon**.
- Approximately **−30° to +45° vertical**.
- Critical threats remain within a comfortable forward combat sector.
- Controller direction drives a servo target; the visible barrel obeys mechanical limits.
- Show the actual barrel impact direction, including any mechanical clamp.
- Fire from the muzzle with obstruction checks; never allow shots through the frame or nearby walls.

Provide adjustable controller-to-cannon offsets and seated calibration. The player must be able to aim with elbows close to the torso.

---

## 5. Heavy Dual-Cannon Combat

### Weapon concept: HCP-40 pulse cannon

Each weapon accelerates a fictional high-mass penetrator inside a brief ionized discharge.

The effect reads as a **heavy high-caliber shot with a laser-like trail**, rather than a continuous beam or lightweight energy pellet.

### Shot presentation

A successful shot combines:

1. Barrel mechanism movement.
2. A brief, directional amber-white muzzle discharge.
3. A thick luminous tracer.
4. A strong impact flash and localized debris.
5. Mechanical recoil in the weapon mount.
6. A short controller haptic pulse.
7. A deep report with a metallic closing transient.

Gameplay hit resolution and tracer presentation are separate. Initial implementation uses muzzle-origin hitscan for reliable aiming, with a rapidly animated cosmetic tracer.

### Prototype tuning values

These are starting values for playtesting, not final balance commitments.

| Parameter | Starting value |
|---|---:|
| Fire rate | 4 shots/second per cannon |
| Base damage | 40 per shot |
| Both-cannon theoretical output | 320 damage/second |
| Weak-point multiplier | ×2, applied to every *designated* weak point: Bulwark side nodes, Lance charge chambers, Cradle pods, boss nodes, boss charge chambers and boss cores **[P-02]** |
| Armored-area multiplier | ×0.25 unless otherwise specified (Bulwark shield ×0.1; Gatebreaker armor immune) **[P-02]** |
| HP convention | All HP values are raw; multipliers apply on hit **[P-02]** |
| Effective engagement distance | 5–45 metres; trace length 60 m, no damage falloff **[P-18]** |
| Heat capacity | 100 per cannon |
| Heat per shot | 9 |
| Passive cooling | 18/second after 0.4 seconds without firing |
| Manual vent cooling | 40/second, replaces passive cooling (not additive); that cannon cannot fire **[P-01]** |
| Overheat trigger | The shot that brings heat to ≥100 still fires; heat clamps to 100 and the cannon locks **[P-01]** |
| Overheat recovery | Locked until heat falls to 35. **Venting is disabled while locked**; passive cooling only (≈4.0 s) **[P-01]** |
| Ammunition | Unlimited; heat is the primary limiter |

At continuous fire, a cold cannon reaches overheat after approximately three seconds. Alternating short bursts and venting should outperform holding both triggers indefinitely.

**[P-01] Verified by `tools/balance_sim.py`:** overheat after 2.75 s (12 shots). Sustained output per cannon: trigger held = 60 dps; burst + vent before lock = 91 dps (≈181 dps for both cannons, against the 320 dps theoretical peak). In v1.0, venting during a lock let "hold until lock, then vent" reach 98 dps and beat skilled play; that is why venting is now disabled during a lock.

### Defensive brace

A temporary protection field anchored to the frame:

- Duration: **2 seconds**.
- Cooldown: **12 seconds**, beginning when the field ends.
- Reduces incoming damage to the rig by **75%**.
- Does not protect the mission objective.
- Does not cancel attacks or reflect damage.
- Provides a clear audio and visual activation cue.

### Split aim and concentrated fire

**Split aim:** attack two weak enemies, interrupt a bomber while holding a lane, or expose paired boss components.

**Concentrated fire:** stagger armored enemies or exploit a short boss vulnerability window.

Do not require simultaneous precision beyond comfortable controller accuracy. Paired targets should be separated enough to reward two hands while remaining within the forward field of view.

---

## 6. Core Loop, Damage, and Progression

### Combat loop

**Read warning → prioritize target → aim one or both cannons → fire controlled bursts → confirm impact → vent/reposition aim → protect objective → survive escalation.**

### Mission loop

**Calibrate → receive objective → learn threat → combine threats → defeat boss → resolve evacuation milestone → receive results.**

### Health model

| Resource | Starting rule |
|---|---|
| Rig integrity | 300 |
| Mission objective integrity | 500 |
| Rig damage | Taken from clearly telegraphed attacks |
| Objective damage | Taken from enemies designated as infrastructure attackers |
| Repair | Fixed between selected encounter phases |
| Failure | Rig or objective integrity reaches zero |
| Recovery | Retry the most recent checkpoint |

Mission repair grants **60 rig integrity**, capped at maximum, at **each level's midpoint** (Level 1 at 05:00, Level 2 at 03:30). Objective integrity is never repaired mid-level. Entering Level 2 restores the rig and establishes a new objective health pool. **[P-05][P-19]**

### Checkpoints

- Level 1: start, midpoint (05:00), **boss start (07:15)**. **[P-04]**
- Level 2: start, midpoint (03:30), **boss start (05:00)**. **[P-04]**
- Boss checkpoints restore a documented preset state rather than preserving an unwinnable state. Preset (Standard): rig 300; objective = max(value when the checkpoint was saved, 60% of maximum); boss at full health. Assisted: objective at least 80%. **[P-04]**
- Store phase, health preset, difficulty, and encounter seed.
- Pause and headset removal stop gameplay timers and enemy damage.

### Encounter director

Use authored phases with limited adaptive spawning.

- Spawn from designated readable entrances.
- Never spawn a damaging enemy immediately behind the player.
- Respect active-enemy, projectile, and effect caps.
- Limit simultaneous high-priority warnings.
- Suppress new spawns when the active threat budget is full.
- Stop reinforcement spawning after phase completion conditions are met.
- Never silently delete visible enemies to meet a schedule.

### Difficulty

| Mode | Changes |
|---|---|
| Assisted | Reduced incoming damage, slower warnings, optional aim assistance |
| Standard | Baseline values and intended campaign timing |
| Veteran | More demanding compositions and reduced recovery windows within the same technical caps |

Difficulty must not increase spectacle beyond hardware limits.

### Replay progression

Initial release includes mission replay, accuracy, weak-point hits, damage prevented, and best score. **[P-30]** *Damage prevented* = rig damage absorbed by brace + damage from attacks interrupted before they resolved (Lance, furnace, bomber pods, sweep emitters).

No permanent stat upgrades are required to finish the campaign. Reward mastery without making later runs compulsory.

---

## 7. Enemy Taxonomy

Enemy numbers below are prototype values. Time-to-kill assumes accurate, unarmored body hits unless specified.

| Enemy | HP | Role and silhouette | Telegraph and response |
|---|---:|---|---|
| **Shardling** | 80 | Small four-legged cutter; low triangular profile | Scrapes forward, then raises cutting limbs for 1 second. Destroy before it reaches infrastructure. |
| **Needle Drone** | 120 | Floating diamond with two lateral fins | Aiming line and rising tone for 1.5 seconds. Shoot it or brace before its burst. |
| **Bulwark** | 480 | Broad shield carrier with a narrow central body | Shield takes ×0.1. Two side nodes (80 HP each, weak points) take ×2. Breaking either node drops the shield and opens the body. No ranged attack; on reaching the objective it slams every 4 s. **[P-09]** |
| **Lance Walker** | 320 | Tall, narrow artillery unit | Plants legs and charges a bright lance for 2 seconds. Its charge chamber (160 HP, weak point, 2 shots) interrupts the attack when broken. **[P-09]** |
| **Siphon** | 200 | Cable-bearing parasite attached to infrastructure | Visible tether and objective-drain warning. Destroy to stop sustained objective damage. |
| **Cradle Bomber** | 160 | Suspended circular carrier holding an explosive pod | Pod glows and descending tone sounds for 2 seconds. Destroy the pod (80 HP, weak point, 1 shot) or the carrier before release. **[P-09]** |
| **Gatebreaker** | Boss | Heavy six-legged siege platform | Sequential leg locks, shield nodes, and exposed furnace core |
| **The Conductor** | Boss | Suspended relay engine with unfolding antenna limbs | Paired synchronization nodes and a protected central command core |

### Enemy behavior rules

- All damaging attacks require a readable warning.
- Shield states use shape and animation as well as color.
- Enemies transition through spawn, approach, attack, stagger, and destruction states.
- Interrupted enemies show an unmistakable mechanical failure.
- Dying units stop dealing damage immediately.
- Cosmetic debris has short lifetimes and no gameplay collision.
- Offscreen attacks require directional audio and an advance indicator.
- Standard combat does not demand rapid rearward head turns.

### Initial damage values

- Shardling reaching objective: **20**, then destroys itself.
- Needle burst hitting rig: **15**.
- Lance strike: **35** to its designated target.
- Siphon drain: **5 objective integrity/second**.
- Bomber impact: **40** to its designated target.
- Bulwark slam: **30** to the objective every 4 s while in contact. **[P-09]**
- Shardlings target infrastructure only; they never damage the rig. **[P-09]**
- Gatebreaker furnace blast: **45** to the rig. Gatebreaker phase-3 artillery: **35** to the rig. **[P-09]**
- Conductor sweep: **40** to the rig (bracing reduces it to 10). **[P-08][P-09]**

Attack-token limits prevent several unavoidable hits from resolving simultaneously.

---

## 8. Campaign Timing Rules

The following storyboards target a successful **Standard** run of approximately 20 minutes.

- Level 1: **00:00–10:00**.
- Level 2: **00:00–10:00**.
- Timings include short in-world narrative beats.
- Loading, menus, pauses, and retries are excluded.
- Boss completion is gameplay-driven; the timeline is a pacing target.
- Finished phases may transition early after their narrative minimum, defined as **60% of the phase's storyboard slot** and every required line of phase dialogue finished. **[P-13]**
- Unfinished encounters may extend the run.
- Target first-successful-run range: **18–24 minutes** after onboarding comprehension is established.

The campaign should feel intense through variation, not twenty minutes of uninterrupted trigger holding.

---

## 9. Level 1 — The Breach

**Location:** Haven Nine power-transfer chamber.  
**Objective:** keep the transfer system operational until the railway receives power.  
**Emotional arc:** confusion → confidence → overload → desperate control.

### Arena composition

| Left lane | Centre lane | Right lane |
|---|---|---|
| Broken maintenance duct | Main blast door and boss entrance | Elevated conveyor and drone shaft |
| Ground attackers | Armored units | Flying attackers |
| Low pipe cover | Protected transfer equipment | Visible evacuation progress lights |

The transfer equipment sits **in front of and below** the player's rig in the centre lane, visible without looking behind. **[P-22]** Enemy routes remain separated enough to support independent aiming.

### Storyboard and encounter schedule

| Time | First-person scene | Player action and encounter | Completion / feedback |
|---|---|---|---|
| **00:00–00:45** | Emergency lighting reveals the frame, cannons, and damaged blast door. | Aim each cannon at a diagnostic target; fire and vent once. No incoming damage until both controls are understood. | RIG-6 confirms both weapon channels. Mara states the evacuation objective. |
| **00:45–02:00** | Cutters emerge through the left maintenance duct. | Defeat 8 Shardlings in small groups. Learn burst rhythm and objective protection. | Transfer indicator reaches its first stage; unmistakable hit and destruction feedback. |
| **02:00–03:30** | Drone silhouettes rise above the right conveyor. | 6 Needle Drones and 8 Shardlings across the phase; maximum 6 active. Split aim between aerial and ground threats. | First incoming aiming line teaches brace timing. |
| **03:30–05:00** | A shield carrier forces its way through the central door. | 2 Bulwarks, 6 Shardlings, 2 Siphons; maximum 7 active. Break side nodes and stop infrastructure drain. | Power rerouting completes. Midpoint checkpoint and capped repair. |
| **05:00–06:30** | Lights briefly stabilize; artillery legs unfold behind smoke. | 3 Lance Walkers supported by 4 Needle Drones and 4 Shardlings; maximum 7 active. Interrupt charged attacks. | Mara reports the first train carriages moving. |
| **06:30–07:15** | The blast door bows inward. Small enemies retreat from its path. | Short final wave: 6 Shardlings and 2 Siphons; maximum 6 active. Clear surviving threats and cool cannons. | Boss entrance begins only after the combat lane is readable. |
| **07:15–09:30** | Gatebreaker tears open the blast door and locks into the chamber. | Destroy shield nodes, interrupt furnace attacks, and exploit its core. Maximum 3 small adds alongside boss. | Boss collapse cuts the assault route. |
| **09:30–10:00** | Power channels ignite toward the evacuation railway. | Clear any remaining minor threats; watch railway lights advance. | Mission success, brief results, save, then fade for relocation. |

**Planned non-boss population:** 51 enemies across the mission (sum of the storyboard rows; v1.0 said 60), plus at most 6 boss reinforcements. **[P-03]** Counts are tuning targets, not simultaneous occupancy.

### Gatebreaker boss specification

**Purpose:** test alternating fire, target switching, and heat discipline.

| Phase | Behavior | Required response |
|---|---|---|
| **1 — Anchor** | Two shoulder shield nodes are exposed in alternating windows. Furnace attacks charge for 2 seconds. Ends when both nodes are destroyed. | Destroy both nodes; interrupt charge chambers when available. |
| **2 — Breach** | After **every** furnace attack, the core opens: **6 s if the attack was interrupted**, 4 s if it fired. **[P-10]** | Concentrate fire, then vent during closure. |
| **3 — Collapse** | Starts when the core falls to **≤30% (900 HP)**. The core keeps opening as in phase 2; one telegraphed artillery attack (35 rig damage) must still be respected. **[P-10]** | Finish the core while preserving rig integrity. |

Prototype damage pools:

- Two shield nodes: **600 HP each**.
- Furnace core: **3,000 HP** (≈2–3 exposures at 70% accuracy, per `tools/balance_sim.py`).
- Furnace charge chamber: **240 HP**, weak point; breaking it interrupts the attack. **[P-09]**
- Armor outside designated targets: immune, with clear deflection feedback.
- No hidden timed damage immunity after the core opens.
- Each exposure repeats until completed; missing a window does not cause automatic failure.

Boss pacing comes from exposures, interruptions, and cooling windows—not an oversized health bar alone.

---

## 10. Level 2 — The Last Signal

**Location:** railway power junction beneath an alien relay shaft.  
**Objective:** maintain evacuation power and destroy the local command machine.  
**Emotional arc:** determination → tactical pressure → apparent defeat → earned escape.

### Arena composition

| Left lane | Centre lane | Right lane |
|---|---|---|
| Railway service trench | Conductor suspended in relay shaft | Damaged transformer balcony |
| Siphons and ground pressure | Main boss silhouette | Drones and bombers |
| Train movement visible beyond safety barrier | Power objective in lower foreground | Readable elevated attack positions |

The environment shows the result of Level 1: the railway is moving. The player’s actions now protect a visible escape.

### Storyboard and encounter schedule

| Time | First-person scene | Player action and encounter | Completion / feedback |
|---|---|---|---|
| **00:00–00:30** | Fade in at the new stabilizer mount. The train moves beyond the barrier. | Reconfirm aim alignment and inspect the junction objective. | Mara identifies the command machine and remaining departure window. |
| **00:30–02:00** | Alien cables pierce the service trench. | 6 Siphons and 8 Shardlings across the phase; maximum 7 active. Prioritize sustained drain. | Power objective visually recovers as tethers break. |
| **02:00–03:30** | Bombers descend above shield carriers. | 4 Cradle Bombers, 2 Bulwarks, 4 Needle Drones; maximum 7 active. Use one cannon for pod interception. | Train carriage counter advances; bomber warnings remain distinct. |
| **03:30–05:00** | The relay shaft opens and reveals the Conductor’s silhouette. | 3 Lance Walkers, 6 Shardlings, 2 Siphons; maximum 8 active. Prevent combined burst and drain damage. | Midpoint checkpoint; fixed recovery state on retry. |
| **05:00–06:00** | The Conductor unfolds synchronization limbs. Two nodes illuminate. | Learn paired-node timing with 4 Needle Drones providing limited pressure. | RIG-6 explains that broken synchronization exposes the core. |
| **06:00–08:00** | The relay engine begins sweep attacks on the rig while its adds go for the junction. **[P-08]** | Main boss cycles begin. Maximum 4 adds, drawn from Shardlings and Siphons. | Each completed cycle visibly disrupts enemy coordination. |
| **08:00–09:30** | The final carriage approaches the tunnel exit. The core becomes unstable. | Finish remaining boss nodes and command core while defending the junction. | Command signal collapses when the core is destroyed. |
| **09:30–10:00** | Uncoordinated machines falter. The last carriage clears the exit. | Survive a short, reduced-pressure resolution; no new major threats. | Shutters close, Mara confirms escape, campaign results appear. |

**Planned pre-boss population:** 39 enemies, followed by up to 12 boss reinforcements. Reinforcements stop when the core is destroyed.

### The Conductor boss specification

**Purpose:** test independent aim, simultaneous target management, and defensive timing.

| Phase | Behavior | Required response |
|---|---|---|
| **1 — Synchronize** | Two separated nodes open together. Destroying one starts a 6-second pairing window. If the window expires, **both nodes reset to full HP** and reopen after 3 s. **[P-07]** | Destroy the second before the first regenerates. Damage persists within the active pairing attempt. |
| **2 — Command** | Successful pairing exposes the core for 5 seconds. A sweep attack **on the rig** receives a 2-second warning. **[P-08]** | Damage the core, brace against the sweep, and avoid overheating both weapons. |
| **3 — Sever** | Repeat with changed node positions and limited adds. Final core damage disables the relay. | Preserve objective integrity while completing the final exposure. |

Prototype pools:

- Three paired-node sets.
- Each node: **240 HP**.
- Central core: **3,600 HP**, damage persistent across exposures.
- **[P-06] Fallback exposure:** after all three node sets are destroyed, every sweep warning exposes a **sweep emitter** (160 HP, weak point). Breaking it staggers the Conductor and opens the core for 5 s. Unbroken sweeps repeat about every 10 s, so the player always gets another opening. At 50% accuracy the sim needs about 4 windows, so this fallback is load-bearing.
- No softlock if the player fails to finish during earlier openings.
- Assisted mode extends pairing windows to **10 seconds**.

The train’s narrative schedule must adapt to encounter completion. Do not punish a player because a cinematic countdown expires while a healthy boss remains.

**[P-14] Gating rule (both levels):** the visible evacuation progress (Level 1 railway power, Level 2 train position) is **capped at 90%** until the boss's final core is destroyed. The last 10% then plays over the 09:30–10:00 resolution beat. Progress never reaches 100% while a boss is alive, and a slow player never sees the train leave without them.

---

## 11. VR Comfort, Accessibility, and HUD

### Comfort defaults

- Seated play with a stable rig reference.
- No smooth locomotion in the first release.
- No snap rotation in combat; Forward re-anchor in pause covers seat alignment **[P-11]**.
- No camera shake, recoil displacement, head bob, forced roll, or artificial zoom.
- Relocation through fade-out, load, and fade-in.
- Recenter accessible from pause.
- Immediate pause on tracking loss, headset removal, or system interruption.
- Resume through an explicit countdown after tracking returns.
- Avoid enemies passing extremely close to the face.
- Keep essential weapon effects outside the central sightline.

### Physical accessibility

- Adjustable seated height and control offsets.
- Aim smoothing and optional target assistance.
- Toggle-to-vent alternative to holding grip.
- Adjustable haptic strength, including off.
- Subtitles with speaker labels and configurable size.
- Separate dialogue, effects, and music volume controls.
- Color-independent attack and weak-point cues.
- Reduced-flash setting.
- Left/right control remapping where runtime support permits.

A full one-handed mode requires separate design and testing; it is not promised in the first-release scope.

### HUD hierarchy

| Information | Placement |
|---|---|
| Left/right heat | Corresponding cannon housing |
| Rig integrity | Central lower frame |
| Objective integrity | World-space marker on protected equipment |
| Brace readiness | Small frame-mounted indicator |
| Enemy warning | Near the source, with directional edge cue if needed |
| Boss vulnerability | On the physical weak point |
| Current objective | Short frame-mounted line |
| Subtitles | Adjustable comfortable forward panel |
| Results | Stable world-space panel after combat |

Initial UI placement target: approximately **1–2 metres perceived distance**, verified on headset. Use angular readability tests rather than relying on desktop font size.

Limit simultaneous messages. Critical attack warnings override score popups and secondary narrative text.

---

## 12. Art and Audio Direction

### Art direction

**Human technology:** welded steel, worn ceramic insulation, exposed hydraulics, stencilled maintenance labels, emergency amber lights.

**Alien technology:** folded mineral plates, off-centre symmetry, porcelain-like cores, dark metallic ribs, mechanically precise unfolding.

**Palette:**

- Human infrastructure: desaturated steel, rust, amber.
- Friendly operational indicators: cool cyan with icon support.
- Alien armor: dark graphite and pale ceramic.
- Vulnerable components: bright white-orange with animated shape change.
- Danger: red-orange paired with movement and sound.

### Readability rules

- Enemies must be identifiable by silhouette at combat distance.
- Weak points must remain visible under muzzle effects.
- Background detail should be quieter than attack cues.
- Avoid excessive darkness; headset readability takes priority over cinematic screenshots.
- Use baked lighting and controlled emissive materials to establish mood.
- Favor localized destruction over large simulated collapses.

### Weapon effects

Use compact muzzle meshes, short-lived tracers, pooled impact effects, and restrained sparks. Heavy sensation should come from timing, sound, animation, and impact response rather than large translucent effects.

### Audio direction

| Layer | Direction |
|---|---|
| Cannons | Deep mechanical report, sharp energy crack, short servo recovery |
| Enemy warnings | Distinct rhythm and pitch per threat family |
| Impacts | Material-specific metal, ceramic, and infrastructure responses |
| Exoskeleton | Quiet hydraulics and cooling fans; louder under strain |
| Music | Sparse industrial pulse, escalating through encounter phases |
| Radio | Brief, intelligible, automatically ducking competing audio |
| Bosses | Recognizable charge signatures and structural movement |

Avoid relying on sub-bass alone; the weapons must retain weight through Quest’s built-in speakers.

Limit simultaneous voices and prevent repeated warning sounds from masking one another.

---

## 13. Unreal Engine Architecture

### Technical foundation

Begin with a minimal Unreal VR project and prove the complete gameplay path on Quest 2 before committing to final assets.

Lock the following together after the first device build:

- Unreal version.
- OpenXR and Meta integration versions.
- Android SDK, NDK, and Java toolchain.
- Rendering settings.
- Packaging and signing configuration.

Do not assume the latest engine release is the best production choice.

### Main systems

| System | Responsibility |
|---|---|
| `AXRSeatedRigPawn` | XR origin, camera, controller tracking, seated calibration |
| `UCannonComponent` ×2 | Aim limits, fire cadence, muzzle traces, heat and venting |
| `UDefenseComponent` | Brace state, cooldown, damage reduction |
| `UIntegrityComponent` | Rig/objective health, damage events, failure |
| `AEncounterDirector` | Phase state, spawn budgets, objective completion |
| `AEnemyBase` | Shared lifecycle, damage interface, pooling |
| Enemy behavior components | Archetype-specific movement and attack logic |
| `ABossController` | Boss phases, weak-point windows, interruptions |
| `UHUDPresenterComponent` | Event-driven UI and warnings |
| `UXRPlatformSubsystem` | Runtime capabilities, haptics, refresh-rate requests |
| `USaveGame` implementation | Settings, checkpoints, mission results |

### C++ and Blueprint division

**C++:** weapon timing, damage, pooling, save serialization, director state, platform abstraction, frequently executed logic.

**Blueprints:** encounter assembly, boss presentation, animation hooks, UI layout, audio events, level-specific scripting.

**Data assets:** weapons, enemies, attacks, encounter phases, difficulty modifiers, and performance tiers.

### Data flow

**Controller input → cannon component → muzzle trace → damage interface → enemy state → presentation events → HUD/audio/VFX.**

Encounter systems listen for events. Avoid polling every actor every frame.

### AI and spawning

- Ground enemies use authored lanes or a deliberately small navigation region.
- Flying enemies use authored paths with local offsets.
- Pool frequently spawned enemies, tracers, and impacts.
- Stagger AI updates where responsiveness permits.
- Use attack tokens to control simultaneous dangerous actions.
- Preload phase assets before combat begins.
- Boss geometry and animation must be tested under actual stereo rendering.

### Portability

Keep gameplay independent of headset-specific APIs. Use device profiles for quality settings and an adapter for refresh rate, haptics, and optional foveation.

OpenXR reduces integration differences; it does not eliminate platform certification, input, packaging, or performance work.

---

## 14. Quest 2 Performance Budgets

These are **project budgets for the prototype**, not universal platform limits.

**[P-31]** These budgets are the floor for every supported headset. Quest 3 and 3S run the same content and settings as Quest 2 until their own measurements justify more. A Quest 3 quality increase may never change gameplay, timing, enemy counts or the readability of warnings. Replace them with measured budgets after the vertical slice.

Meta identifies stable frame rate and constrained rendering costs as key Quest development concerns. Epic recommends mobile multiview and disabling Mobile HDR for mobile VR; Meta recommends the mobile forward rendering path and MSAA. [Meta optimization guidance](https://developers.meta.com/vr/documentation/unreal/ts-book-tools/), [Epic XR best practices](https://dev.epicgames.com/documentation/unreal-engine/xr-best-practices-in-unreal-engine), [Meta forward rendering guidance](https://developers.meta.com/vr/documentation/unreal/unreal-forward-renderer/).

| Category | Initial project target |
|---|---|
| Refresh rate | Stable native 72 Hz |
| Frame interval | 13.89 ms |
| CPU frame work | Target ≤11 ms at the 95th percentile |
| GPU frame work | Target ≤11 ms at the 95th percentile |
| Headroom | Approximately 2.9 ms against the frame interval |
| Rendering path | Mobile Forward, Mobile HDR off |
| Stereo | Mobile Multi-View after device validation |
| Anti-aliasing | Start with 4× MSAA; measure cost |
| Visible draw calls | Target ≤120; investigate sustained values above 150 |
| Visible triangles | Target ≤300,000 across the scene before stereo/pass multiplication |
| Active enemies | Normal cap 8; boss plus at most 4 adds |
| Simultaneous dangerous attacks | Maximum 2; avoid overlapping unavoidable damage |
| Texture residency | Initial target ≤450 MB |
| App memory | Initial measured process-memory target ≤1.8 GB |
| Audio voices | Initial cap 24, with priority stealing |
| Persistent real-time shadow lights | None in baseline |
| Destruction | Authored animation and pooled debris |
| Loading | Target ≤15 seconds per mission on device |

CPU and GPU budgets are parallel pipeline targets; they are not added together. Measure draw calls and geometry using a consistent tool definition, documenting stereo and additional-pass costs.

### Baseline exclusions

No Lumen, Nanite-dependent assets, real-time ray tracing, volumetric fog, screen-space reflections, motion blur, or depth of field in the Quest 2 baseline.

### Optimization order

1. Remove expensive translucent overdraw.
2. Reduce material complexity and draw calls.
3. Reduce visible geometry and skeletal cost.
4. Reduce active effects and cosmetic debris.
5. Adjust render scale or foveation after checking target readability.
6. Reassess encounter population only if other measures cannot achieve the budget.

Never reduce warning visibility or input responsiveness to preserve decoration.

### Device verification

Profile packaged builds on a physical Quest 2, including a **30-minute repeated-combat soak**. Before release, repeat the soak on a Quest 3 or 3S. **[P-31]** Record CPU/GPU timing, missed frames, thermal behavior, memory, and the exact build/settings.

Editor performance and PC-linked VR are insufficient evidence.

---

## 15. Initial Asset Inventory

Counts represent distinct production assets or kits. Variants should reuse materials and geometry where practical.

| Category | Initial inventory | Priority |
|---|---|---|
| Player rig | 1 open frame, seat, supports, hands/control interface | Critical |
| Weapons | 1 cannon design with left/right assembly variants | Critical |
| Common enemies | 6 archetypes | Critical |
| Bosses | Gatebreaker and Conductor | Critical |
| Environments | 2 modular arena kits | Critical |
| Structural modules | Approximately 24 shared walls, floors, beams, ducts, barriers | High |
| Objectives | Transfer unit, power junction, evacuation train components | Critical |
| Props | Approximately 20 reusable industrial props | Medium |
| Enemy animation | Spawn, movement, attack, stagger, death per archetype | Critical |
| Rig animation | Fire, vent, overheat, brace, damage response | Critical |
| Boss animation | Entrance, phase actions, exposure, stagger, defeat | Critical |
| VFX | Approximately 16 reusable systems/variants | High |
| UI | Calibration, pause, settings, HUD, warnings, results | Critical |
| Audio | Approximately 50–70 designed effects plus variants | High |
| Music | 2 mission beds, 2 boss layers, opening/ending stingers | Medium |
| Voice | Approximately 35–45 short lines across Mara and RIG-6 | Medium |
| Marketing | Logo, key art, screenshots, trailer captures | Later |

### Asset acceptance

Every gameplay asset needs:

- Consistent scale and pivots.
- Approved naming and folder placement.
- Collision appropriate to its purpose.
- LODs where useful.
- Material-slot review.
- Texture sizing appropriate to viewing distance.
- Readability check on headset.
- Source-file and usage-rights record.

### Suggested content structure

```text
Content/ETM/
  Core/
  Player/
  Weapons/
  Enemies/
  Bosses/
  Encounters/
  Environments/
  UI/
  Audio/
  VFX/
  Data/
  Maps/
```

---

## 16. Production Plan

Planning assumption: a small experienced team with Unreal engineering, technical art, environment/character art, design, audio support, and recurring hardware QA.

The schedule is an initial **16-week plan**, subject to the first hardware gate. **[P-24]** Weeks are relative to the team start date, recorded in `docs/DEVELOPMENT_PLAN.md`. The plan must keep at least **12 weeks of slack** before the December 2027 Quest 2 submission cutoff (see P-15).

| Milestone | Timing | Deliverable | Exit gate |
|---|---|---|---|
| **M0 — Foundation** | Week 1 | Packaged Quest 2 project, input, calibration, rig blockout | Stable tracked view and successful device deployment |
| **M1 — Combat proof** | Weeks 2–3 | Dual cannons, heat, vent, brace, two enemies | Comfortable, readable 3-minute combat test |
| **M2 — Vertical slice** | Weeks 4–6 | Representative arena, objective, mixed wave, boss prototype | Sustained hardware performance and validated weapon feel |
| **M3 — Campaign alpha** | Weeks 7–10 | Both missions playable end to end | All encounter phases, checkpoints, bosses, ending |
| **M4 — Content beta** | Weeks 11–13 | Art/audio integration and accessibility settings | No missing critical assets; timing and readability validated |
| **M5 — Release candidate** | Weeks 14–16 | Optimization, regression, packaging, release materials | Acceptance criteria met; no blocker defects |

### First build order

1. Packaged empty VR scene.
2. Seated rig and independent controller aim.
3. One cannon with correct weight and feedback.
4. Second cannon and independent heat.
5. One ground enemy and one flying enemy.
6. Objective damage and failure.
7. Three-minute mixed encounter.
8. Boss weak-point prototype.
9. Full Level 1.
10. Full Level 2.

**Stop/go gate:** if the three-minute combat proof is uncomfortable or fails the hardware budget, fix that before creating final campaign assets.

### Progress reporting

Each completed task should record:

- What changed.
- Files or assets affected.
- Verification performed.
- Remaining problems.
- Next recommended action.
- Commit or pull-request reference.

A milestone is complete only when its exit gate has evidence.

---

## 17. Acceptance Criteria

| Area | Required evidence |
|---|---|
| First-person embodiment | Head movement remains directly tracked; no artificial camera recoil or impact shake |
| Dual weapons | Each cannon aims, fires, heats, vents, and overheats independently |
| Weapon feel | At least 8 of 10 target-player testers identify the shots as heavy and powerful |
| Control comprehension | At least 8 of 10 new testers learn firing, venting, and brace without external coaching |
| Campaign completion | Both levels, bosses, checkpoints, failure, retry, and ending function in packaged builds |
| Duration | Median first successful Standard run falls within 18–24 minutes in a minimum 10-player test |
| Enemy readability | Testers distinguish each archetype and its attack warning at intended combat distance |
| Boss robustness | Missed exposure windows never create a permanent unwinnable state |
| Comfort | No forced viewpoint movement; any severe discomfort report triggers investigation and retest |
| Performance | 72 Hz target sustained in representative combat on Quest 2 and on Quest 3 or 3S **[P-31]**; CPU/GPU percentile budgets and missed-frame results documented |
| Stability | No crash, softlock, or progressive memory growth across a 30-minute combat soak |
| Interruptions | Pause, tracking loss, headset removal, and resume preserve a valid mission state |
| Accessibility | Subtitles, volume controls, reduced flash, haptic settings, and seated calibration verified |
| Save system | Settings, checkpoint, and mission results survive application restart |
| Art/audio | No missing materials, unintelligible critical dialogue, or misleading attack cues |
| Release quality | Zero open blocker or critical defects; major defects explicitly resolved or accepted |

For performance, adopt an internal target of **fewer than 1% missed application frames during representative active combat**, excluding identified loading transitions. Any sustained frame-rate drop is a failure requiring investigation, even if the aggregate percentage passes.

Testing validates the product; a small playtest is not a guarantee of comfort for every player.

---

## 18. Risks and Mitigations

| Risk | Impact | Mitigation / decision gate |
|---|---|---|
| Title resembles an established franchise **[P-16]** | **High**: possible forced rename, store rejection, or legal claim | Internal codename only; clearance before **any** public use; keep franchise terms (Zion, Sentinel, the Matrix, green code) out of all assets, including concept art and prompts |
| Concept art contradicts the bible **[P-17]** | Art pipeline builds the wrong game | `docs/CONCEPT_ART_REVIEW.md` governs; concept art is mood reference only until a revised brief is approved |
| Dual-cannon effects overwhelm Quest 2 | Frame drops and poor readability | Establish effects budgets in the combat proof; pool and simplify |
| Seated aiming causes shoulder fatigue | Shortened sessions and discomfort | Support elbows-close aiming, offset calibration, and cooling breaks |
| Independent aiming feels imprecise | Core fantasy fails | Test controller offsets, servo response, and optional assistance early |
| Fixed position becomes repetitive | Weak replay value | Vary lanes, threat roles, weak points, and objective pressure |
| Both guns overheat during danger | Frustration or unavoidable damage | Teach alternation early; keep defensive and cooling opportunities readable |
| Bosses become health sponges | Campaign pacing collapses | Tune exposure cycles and interruptions before adding health |
| Adaptive spawning breaks story timing | Long or inconsistent missions | Use bounded phases and measure successful-run duration |
| Engine/plugin incompatibility | Packaging delays | Lock a proven toolchain after first successful device build |
| Quest 2 distribution/support changes **[P-15]** | Hard release deadline | Meta has announced that Horizon OS v2.13 is the final feature release for Quest 2, and new apps supporting Quest 2 are accepted only **through December 2027**. Target store submission by **Q3 2027** to leave review buffer. Gameplay must not depend on any OS or SDK feature released after v2.13. Re-verify these dates at every milestone gate. Shipping on Quest 3/3S as well means a missed Quest 2 cutoff no longer stops the release outright **[P-31]**. |
| Binary asset conflicts | Lost work and integration delays | Assign asset ownership, use branches and Git LFS, avoid simultaneous edits |
| Scope expands beyond two missions | Schedule failure | Maintain exclusions and require explicit milestone changes |
| Porting begins too early | Baseline quality suffers | Quest 3/3S ship from the same build with Quest 2 settings, so supporting them costs device testing, not a port. Quest-3-only quality work waits for Quest 2 vertical-slice approval and measured headroom. PCVR and other headsets start after that approval. **[P-31]** |
| Quest 3 controllers or runtime behave differently **[P-31]** | Input or tracking bugs only some players see | Quest 3/3S use Touch Plus controllers. The engine's OpenXR plugin binds only the Oculus Touch profile, which Meta's runtime serves Touch Plus through. Verify input, tracking and 72 Hz on a physical Quest 3 or 3S at every hardware gate. |

---

## 19. Release and Expansion Strategy

### First release

Deliver the complete two-mission campaign with:

- Reliable seated controls.
- Powerful independent cannons.
- Six common enemy archetypes.
- Two distinct bosses.
- Checkpoints and replay scoring.
- Comfort and accessibility settings.
- Verified performance on Quest 2 and on Quest 3 or 3S. **[P-31]**

### Later platform work

**Quest 3/3S quality:** they ship in the first release (P-31). Later, use measured headroom for resolution, effects, and environmental detail, keeping gameplay parity.

**PCVR:** validate controller bindings and headset behavior, then add optional higher-quality shadows, textures, and effects.

**Other VR platforms:** evaluate input, runtime, certification, and commercial requirements individually.

Do not alter enemy timing or weak-point visibility simply because a higher-end platform can display more effects.

### Product success

The first release succeeds when players can immediately understand the situation, feel the weight of both cannons, complete a tense survival story comfortably, and want to replay to perform better.

**The central experience remains simple: sit in the frame, bring both weapons online, and keep the evacuation alive.**