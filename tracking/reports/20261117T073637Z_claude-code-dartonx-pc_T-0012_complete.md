---
time: 2026-11-17T07:36:37Z
agent: claude-code-dartonx-pc
task: T-0012
kind: complete
commits: afea961
---

Input mapping done in code. ARigPlayerController (Source/ETM/Input) builds the Enhanced Input actions and mapping context in C++ for the Oculus Touch profile and drives AXRSeatedRigPawn. A pure router applies either scheme: GripVent (bible mapping, grip above 0.85 for 100 ms, A or X braces) or ButtonVent (P-12 alternative: X/A hold vents, stick click braces). SetControlScheme switches at runtime and saves to slot ETM_Input. Thumbstick axes are unmapped (P-11). Per-scheme counters record vents opened while firing or shorter than 0.3 s, logged as VentStats lines when play ends.
Verified: Built ETMEditor Win64 Development on UE 5.8.4, zero errors and warnings. 5 new automation tests (ETM.Input.*) pass in a headless editor: grip gate timing, both schemes, edge-triggered brace/confirm/pause, vent statistics, mapping context contents, scheme save round-trip. NOT verified: reading real controller values through Enhanced Input (needs a local player and a headset), and the full path controller to pawn to cannon in a running game.
Remaining: Two of the three acceptance items are NOT met and cannot be met in code: the accidental-vent rate measurement and the ADR. They need the M1 playtest (T-0016), which depends on this task, so I split them into a new follow-up task. Also: no input assets were made under Content/ETM/Core/Input (mappings live in code); a game mode must set ARigPlayerController and AXRSeatedRigPawn as defaults (Config or a GameMode class, outside this task's paths); the settings UI that calls SetControlScheme is T-0037; a 0.75 release point and 0.5/0.4 trigger thresholds are my additions, not bible values.
Next: Review T-0012 with the split in mind. Reviewer should reject if the playtest and ADR must stay inside this task.
