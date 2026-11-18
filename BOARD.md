# Task Board

_Generated 2026-11-18T22:19:44Z by `tools/agent.py render`. Do not edit by hand._

**Progress:** 32/58 done (55%) · todo: 25 · in_progress: 0 · review: 0 · blocked: 1 · done: 32

| Milestone | Done | Total | Progress |
|---|---:|---:|---|
| M0 | 6 | 10 | `██████░░░░` |
| M1 | 13 | 17 | `████████░░` |
| M2 | 11 | 15 | `███████░░░` |
| M3 | 2 | 8 | `██░░░░░░░░` |
| M4 | 0 | 5 | `░░░░░░░░░░` |
| M5 | 0 | 3 | `░░░░░░░░░░` |

## Active claims

_None. Every task is free._

## Blocked (1)

| ID | P | Milestone | Area | Repo | Title | Depends on | Owner |
|---|---|---|---|---|---|---|---|
| T-0015 | 2 | M1 | vfx | game | Weapon feel: muzzle, tracer, impact, haptics, placeholder audio | T-0009 |  |

## Todo (25)

| ID | P | Milestone | Area | Repo | Title | Depends on | Owner |
|---|---|---|---|---|---|---|---|
| T-0002 🟢 ready | 1 | M0 | producer | tracker | Owner: set team start date and turn M0-M5 weeks into calendar dates | - |  |
| T-0003 🟢 ready | 1 | M0 | producer | tracker | Owner: kick off naming/trademark clearance for the title (P-16) | - |  |
| T-0004 🟢 ready | 2 | M0 | art | tracker | Revised concept art pass using the CONCEPT_ART_REVIEW brief | - |  |
| T-0008 🟢 ready | 2 | M0 | art | game | Open-frame rig blockout mesh (seat, knee guard, weapon arms) | T-0006 |  |
| T-0016 | 1 | M1 | qa | tracker | M1 gate: 3-minute combat test on Quest 2 (comfort, readability, perf capture) | T-0014, T-0015, T-0012, T-0010 |  |
| T-0047 🟢 ready | 1 | M1 | qa | tracker | Verify on a physical Quest 3 or 3S: install, tracking, Touch Plus input, 72 Hz, short combat test (P-31) | T-0006, T-0046 |  |
| T-0057 🟢 ready | 1 | M1 | platform | game | Deploy the packaged build to a physical Quest 2: install, 72 Hz, tracking, input (split from T-0006) | - |  |
| T-0025 | 1 | M2 | qa | tracker | M2 gate: vertical slice validated on hardware | T-0020, T-0021, T-0022, T-0023, T-0024, T-0019 |  |
| T-0042 | 1 | M2 | input | tracker | Measure accidental-vent rate for both control schemes in the M1 playtest and record the winner as an ADR (P-12) | T-0016 |  |
| T-0024 🟢 ready | 2 | M2 | perf | game | Performance capture tooling + 30-minute soak script | T-0006 |  |
| T-0049 🟢 ready | 3 | M2 | qa | game | Test worlds: run garbage collection after destroying them, so reserved GPU memory stops climbing during the test run | - |  |
| T-0026 | 1 | M3 | encounters | game | Level 1 full schedule (51 enemies, timeline, gating P-14) | T-0025 |  |
| T-0027 | 1 | M3 | level | game | Level 2 arena greybox | T-0025 |  |
| T-0028 | 1 | M3 | boss | game | Conductor boss incl. pairing reset (P-07), rig sweep (P-08), emitter fallback (P-06) | T-0025 |  |
| T-0029 | 1 | M3 | encounters | game | Level 2 full schedule + train gating (P-14) | T-0027, T-0028 |  |
| T-0033 | 1 | M3 | qa | tracker | M3 gate: both missions end to end in a packaged build | T-0026, T-0029, T-0030, T-0031 |  |
| T-0032 🟢 ready | 3 | M3 | audio | game | Placeholder VO (Mara, RIG-6) and subtitles with speaker labels | T-0031 |  |
| T-0038 | 1 | M4 | qa | tracker | 10-player playtest: duration, comprehension, comfort | T-0034, T-0035, T-0036, T-0037 |  |
| T-0034 | 2 | M4 | art | game | Final enemy and boss art + animation | T-0004, T-0033 |  |
| T-0035 | 2 | M4 | art | game | Environment art kits for both arenas | T-0033 |  |
| T-0036 | 2 | M4 | audio | game | Sound design and music beds | T-0033 |  |
| T-0037 | 2 | M4 | settings | game | Accessibility and comfort settings | T-0033 |  |
| T-0039 | 1 | M5 | perf | game | Optimization pass to §14 budgets | T-0038 |  |
| T-0040 | 1 | M5 | qa | tracker | Release candidate: regression, soak, acceptance criteria evidence | T-0039 |  |
| T-0041 | 1 | M5 | release | tracker | Store submission package (before Quest 2 cutoff, P-15) | T-0040, T-0003 |  |

## Done (32)

| ID | P | Milestone | Area | Repo | Title | Depends on | Owner |
|---|---|---|---|---|---|---|---|
| T-0001 | 1 | M0 | producer | tracker | Bootstrap repos, patched bible v1.1, tracker and Unreal scaffold | - | claude-bootstrap |
| T-0005 | 1 | M0 | engine | game | Compile the scaffold and lock the toolchain (UE version, Meta XR/OpenXR plugin, SDK/NDK/JDK) | - | claude-code-dartonx-pc |
| T-0006 | 1 | M0 | engine | game | Package an empty VR scene and deploy it to a physical Quest 2 | T-0005 | claude-code-dartonx-pc |
| T-0007 | 1 | M0 | player | game | Seated rig pawn: XR origin, controller tracking, seated calibration, Forward re-anchor (P-11) | T-0005 | claude-code-dartonx-pc |
| T-0053 | 1 | M0 | engine | game | Sandbox game mode: rig pawn, floor and distance markers, practice encounter (first playable for VR Preview and the first APK) | - | claude-code-dartonx-pc |
| T-0054 | 1 | M0 | engine | game | Fix Android (Clang) build errors in the interruption subsystem and the sandbox game mode | - | claude-code-dartonx-pc |
| T-0009 | 1 | M1 | weapons | game | Cannon component: aim envelope ±65/-30..+45, servo, cadence, muzzle trace, heat per P-01 | T-0007 | claude-code-dartonx-pc |
| T-0010 | 1 | M1 | qa | game | Automation test: cannon heat parity with tools/balance_sim.py | T-0009 | claude-code-dartonx-pc |
| T-0011 | 1 | M1 | combat | game | Brace (DefenseComponent) and Integrity components | T-0005 | claude-code-dartonx-pc |
| T-0012 | 1 | M1 | input | game | Enhanced Input mapping with grip-vent threshold 0.85/100ms and alternative A/B mapping (P-12) | T-0007 | claude-code-dartonx-pc |
| T-0013 | 1 | M1 | enemies | game | Enemy base: lifecycle states, damage interface, weak points, pooling | T-0011 | claude-code-dartonx-pc |
| T-0014 | 1 | M1 | enemies | game | Shardling (ground) and Needle Drone (flying) prototypes | T-0013 | claude-code-dartonx-pc |
| T-0044 | 1 | M1 | engine | game | Keep the ETM module building once it passes 32 source files (unity-build name clashes in tests) | - | claude-code-dartonx-pc |
| T-0046 | 1 | M1 | engine | game | Quest 3/3S: pin device profiles to the Quest 2 baseline and document supported headsets (P-31) | - | claude-code-dartonx-pc |
| T-0055 | 1 | M1 | weapons | game | First headset test changes: P-34 rapid fire in code, fire-cadence carry (T-0043), eye height, barrel length, closer sandbox range | - | claude-code-dartonx-pc |
| T-0056 | 1 | M1 | weapons | game | Second headset test: faster stand-in spawns, muzzle flash away from the eyes, drones from both sides | - | claude-code-dartonx-pc |
| T-0058 | 1 | M1 | enemies | game | Third headset test: small explosion when enemies die; Needle Drones drift around their hover point | - | claude-code-dartonx-pc |
| T-0043 | 2 | M1 | weapons | game | Heat model: carry fire-cooldown remainder so cadence does not drift at 72 Hz | T-0010 | claude-code-dartonx-pc |
| T-0048 | 2 | M1 | vfx | game | Shot feedback component in C++: recoil, muzzle flash, tracer, impact flash, haptics, placeholder sound (for T-0015) | T-0009 | claude-code-dartonx-pc |
| T-0017 | 1 | M2 | encounters | game | Encounter director: authored phases, spawn budgets, attack tokens, early-transition rule (P-13) | T-0013 | claude-code-dartonx-pc |
| T-0018 | 1 | M2 | objective | game | Objective integrity, world marker, failure and retry | T-0011 | claude-code-dartonx-pc |
| T-0021 | 1 | M2 | boss | game | Gatebreaker boss prototype (P-02, P-09, P-10) | T-0017 | claude-code-dartonx-pc |
| T-0045 | 1 | M2 | enemies | game | Attack tokens in the enemy base: cap simultaneous attacks (bible section 14: max 2 dangerous attacks) | - | claude-code-dartonx-pc |
| T-0052 | 1 | M2 | save | game | Move the calibration and control-scheme saves to the checked save format (damaged files crash the engine's loader) | T-0023 | claude-code-dartonx-pc |
| T-0019 | 2 | M2 | ui | game | Diegetic HUD presenter: heat on housings, integrity on frame, warnings at source | T-0009, T-0011 | claude-code-dartonx-pc |
| T-0020 | 2 | M2 | level | game | Level 1 arena greybox (three lanes, transfer equipment in front, P-22) | T-0006 | claude-code-dartonx-pc |
| T-0022 | 2 | M2 | enemies | game | Bulwark, Lance Walker, Siphon, Cradle Bomber | T-0014 | claude-code-dartonx-pc |
| T-0023 | 2 | M2 | save | game | Save system: settings, checkpoints incl. boss presets (P-04), results | T-0018, T-0017 | claude-code-dartonx-pc |
| T-0050 | 2 | M2 | ui | game | Wire the HUD presenter into the rig pawn (for T-0019) | - | claude-code-dartonx-pc |
| T-0051 | 2 | M2 | objective | game | Mission state: resume from a saved checkpoint after an app restart (for T-0023) | - | claude-code-dartonx-pc |
| T-0030 | 1 | M3 | platform | game | Pause, tracking loss, headset removal, resume countdown | T-0023 | claude-code-dartonx-pc |
| T-0031 | 2 | M3 | flow | game | Campaign flow: menus, relocation fade, results, ending | T-0019 | claude-code-dartonx-pc |

