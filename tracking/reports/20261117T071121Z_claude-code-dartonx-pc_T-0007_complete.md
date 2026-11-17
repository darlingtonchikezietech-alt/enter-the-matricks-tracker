---
time: 2026-11-17T07:11:21Z
agent: claude-code-dartonx-pc
task: T-0007
kind: complete
commits: 4472fb2
---

Seated rig pawn done in code. Calibration moves only the XR origin; nothing writes to the camera. Recenter seats the head at the design eye point (also on the first tracked frame and after a system recenter). Forward re-anchor (P-11) re-aligns facing without moving the head in the rig. Per-hand aim offsets are clamped and saved to slot ETM_Calibration. Cannons hold aim when a controller loses tracking.
Verified: Built ETMEditor Win64 Development on UE 5.8.4, zero errors and warnings. 5 automation tests (ETM.Player.Calibration.*) pass in a headless editor. No headset, no VR Preview, no pause menu exists yet, so recenter and re-anchor are verified by maths only.
Remaining: On-device check of recenter, re-anchor and offset feel (with T-0006). DesignEyeLocation (0,0,120) and the offset clamp range are prototype values to tune with the T-0008 blockout. Pause menu wiring is T-0030/T-0031. T-0023 may absorb the calibration save slot. Branch agent/claude-code-dartonx-pc/t-0007 needs a PR into main.
Next: Review T-0007. Ready now: T-0011 (brace and integrity), T-0009 and T-0012 after T-0007 is approved, T-0006 once the engine has the Android target and the Quest 2 has Developer Mode.
