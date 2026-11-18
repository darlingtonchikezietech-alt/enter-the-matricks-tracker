---
time: 2026-11-18T00:37:00Z
agent: claude-code-dartonx-pc
task: T-0053
kind: complete
commits: 5e733a1
---

AETMSandboxGameMode (Source/ETM/Core/Game) is the project default (GlobalDefaultGameMode in Config/DefaultEngine.ini). Player = AXRSeatedRigPawn + ARigPlayerController; each rig is registered with the mission at StartPlay and on RestartPlayer. On the Entry map (the boot map) with no objective present it builds a range in code: one movable shadowless directional light, a 60 m floor, distance posts at 5/15/30/45 m down three lanes (-35, 0, +35 deg), the objective 4.5 m ahead at floor level with a block for its bulk, three target-point entrances 25 m out facing the rig, and an encounter director running one hour-long practice phase (Shardlings from left and centre, Needle Drones from the right, max 5 active), with automatic retry 3 s after a mission failure.
Verified: Built on UE 5.8.4, zero errors and warnings; all 78 ETM tests pass, 2 new (ETM.Core.Sandbox.*) using FTestWorldWrapper: the default game mode is the sandbox and does not build the range in non-Entry worlds; BuildSandbox gives an objective ahead and below the eye, three valid entrances, one light without shadows, more than 15 range actors; enemies arrive within 10 s of real world ticks; a rig failure retries by itself and restores the rig; building twice is a no-op. Not yet seen in VR Preview or on a headset.
Remaining: Placeholder grey shapes on default materials; no sky or ambient light, so faces away from the light are dark. The local editor-rewritten DefaultEngine.ini on the build PC also needs GlobalDefaultGameMode set to the sandbox (done locally, not committed). Real arenas replace the range (T-0020/T-0027); the campaign flow (T-0031) will set its own game mode. Branch agent/claude-code-dartonx-pc/t-0053 needs a PR.
Next: Review T-0053. Then T-0006: package this as the first APK once the engine's Android target is installed.
