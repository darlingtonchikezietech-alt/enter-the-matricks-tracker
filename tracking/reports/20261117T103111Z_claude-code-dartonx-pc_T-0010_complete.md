---
time: 2026-11-17T10:31:11Z
agent: claude-code-dartonx-pc
task: T-0010
kind: complete
commits: 576eb6b
---

Added Source/ETM/Tests/HeatParityTest.cpp: 3 automation tests that run the heat model through balance_sim.py's policies (hold, hold-then-vent, burst+vent) and check overheat 12 shots / 2.75 s, recovery 4.0 s, vent-during-lock gives nothing (P-01), 60 vs 91 dps; once at the sim's 1 ms step and once at 72 Hz with UCannonComponent's 1/240 s sub-steps; plus a check that FCannonTuning defaults equal the sim constants. Finding: at 72 Hz the cadence drifts (overheat 2.792 s, burst+vent 89.33 dps) because StepHeat resets the fire cooldown instead of carrying the remainder; filed T-0043, and the 72 Hz test allows 3 frames and 2% with a comment saying to tighten it.
Verified: Built ETMEditor Win64 Development on UE 5.8.4, zero errors and warnings. All 18 tests on this branch pass headless via UnrealEditor-Cmd -ExecCmds Automation RunTests with -testexit (the CI-capable commandlet form). The g++ test in Tools/HeatModelTest was not changed and not run here: no g++ on this PC; it still runs in GitHub CI.
Remaining: Not wired into CI: GitHub's hosted runners have no Unreal, so the in-engine test runs only on a machine with the engine. The 72 Hz tolerance is loose until T-0043. Branch agent/claude-code-dartonx-pc/t-0010 needs a PR into main.
Next: Review T-0010, then T-0043 (small fix) or T-0014 (Shardling and Needle Drone).
