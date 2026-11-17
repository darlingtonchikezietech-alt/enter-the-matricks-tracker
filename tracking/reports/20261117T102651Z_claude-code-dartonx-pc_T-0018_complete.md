---
time: 2026-11-17T10:26:51Z
agent: claude-code-dartonx-pc
task: T-0018
kind: complete
commits: 8336fbd
---

Objective and mission failure done (Source/ETM/Objectives). AMissionObjective: 500 integrity, accepts damage only from designated attackers (actor tag ETM.InfrastructureAttacker or DesignatedAttackerClasses), refuses cannon fire and sourceless damage and counts refusals; marker anchor, IsUnderAttack, last attacker location and an OnUnderAttack cue for the HUD. UMissionStateSubsystem: StartMission, RecordCheckpoint (phase, time, seed, health), fails once on rig or objective depletion, RetryFromLastCheckpoint parks every enemy (pooled or not), resets the brace, restores saved health, or the P-04 preset at boss checkpoints (rig full, objective at least 60%, 80% on Assisted), and fires OnRetryStarted with the phase for the director.
Verified: Built ETMEditor Win64 Development on UE 5.8.4, zero errors and warnings. 4 new automation tests (ETM.Objectives.*) pass in a headless editor with a test world, real AEnemyBase attackers and the real integrity and brace components; all 19 tests on main plus this branch pass. No headset, no level, no HUD.
Remaining: Archetypes must tag infrastructure attackers (Shardling, Siphon, Bulwark, Cradle and Lance when targeting the objective) in T-0014/T-0022. Nothing registers the rig with the mission yet: AXRSeatedRigPawn or a game mode must call RegisterRig (outside this task's paths). The director (T-0017) must call StartMission and RecordCheckpoint and rebuild the phase on OnRetryStarted. Midpoint repair (+60 rig, P-05) belongs to the director's schedule. The failure screen that calls Retry is T-0031; checkpoints are in memory only until T-0023. The marker visual is T-0019.
Next: Review T-0018. Pending reviews: T-0009, T-0012, T-0013 (merged), T-0018.
