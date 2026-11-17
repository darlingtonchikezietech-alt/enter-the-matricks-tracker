---
time: 2026-11-17T13:42:07Z
agent: claude-code-dartonx-pc
task: T-0019
kind: complete
commits: f1f82ed
---

UHUDPresenterComponent (Source/ETM/UI), event-driven, on the rig pawn. Placement per bible section 11: heat bar on each cannon housing near the muzzle plus a lock bracket when overheated; rig integrity bar and 'RIG n' on the central lower frame; brace readiness bar on the frame (full ready, empty in use, refills through the cooldown); objective marker 'POWER n%' above the equipment, pulsing while it is under attack; enemy warnings as '! seconds' markers above each source, the 3 most urgent (soonest, rig attacks win ties), with an edge arrow for sources more than 50 deg off view; '[ OPEN seconds ]' on exposed Gatebreaker weak points; a short objective line; a secondary line for score/narrative that is hidden whenever a critical warning is up. Binds to enemies, bosses and the objective by scanning every 0.5 s (and catches attacks already running). Pure ranking and priority rules in UI/HudModel.h.
Verified: Built on UE 5.8.4, zero errors and warnings; all 60 tests on this branch pass, 5 new (ETM.UI.*): ranking, tie-break, cap, secondary expiry, view cone; frame elements 1-2 m from the design eye, below eye height, on the frame, rig bar central; heat and lock per housing; rig text; brace 1 -> 0 -> 0.5 at 8 s -> 1; objective marker text and alarm; 4 attacks -> 3 markers above sources with countdowns, edge arrow only for the off-view one, queued warning moves up, warnings end with their attacks, secondary hidden then back then expires, late-bound attack still warned; boss marker on the open node, gone when it closes. Not seen in a headset: text orientation, size and angular readability are unverified.
Remaining: Text faces the seat by a fixed 180 deg turn and world markers face the head each frame; readability at 1-2 m must be checked on a headset (bible: angular readability tests). Placeholder bars and engine text, no UI art (T-0034). Subtitles (T-0032) and results panel (T-0031) are not here. Warnings for attacks against the objective show as normal warnings; Lance and Bomber designated targets are known but not shown. Scanning every 0.5 s: a warning can appear up to 0.5 s late only for an enemy spawned and attacking within that time. Branch agent/claude-code-dartonx-pc/t-0019 also carries T-0050.
Next: Review T-0019 and T-0050 (same branch).
