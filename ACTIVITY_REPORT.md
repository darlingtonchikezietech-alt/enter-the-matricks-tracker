# Activity Report

_Brief log of what happened, newest first. Generated from `tracking/reports/`. Add entries with `tools/agent.py log` or `complete`._

- **2026-11-18 18:53Z** · `claude-code-dartonx-pc` · T-0056 · _complete_ · commits: 9be1ed2
  Faster stand-in spawns (gaps 1.5-2.5 s, shorter slots), drones from left and right, muzzle flash 40 cm past the muzzle at half size, dimmer and at most every 0.25 s, cannon mounts 65 cm to each side. Branch stacked on t-0031.
  Verified: All 83 ETM tests pass (new: rapid-fire flash rate/position, stand-in spawn gaps and drone lanes); APK installed on the Quest 3. Owner headset check pending.
  Remaining: Owner headset check
- **2026-11-18 18:48Z** · `claude-code-dartonx-pc` · T-0056 · _claim_
  Owner asked to fix all three
- **2026-11-18 18:44Z** · `owner` · T-0031 · _review_
  Approved. Owner played the full loop on the Quest 3 and approved in chat. Recorded on the owner's behalf by claude-code-dartonx-pc.
- **2026-11-18 18:39Z** · `claude-code-dartonx-pc` · T-0031 · _complete_ · commits: 9e22f91,909c365,a14c5ab,18f33a7
  Campaign flow (9e22f91) plus three fixes from the owner's headset tests: panel text lit (909c365), rig placed on the range instead of the Entry map's player start so panels are reachable (a14c5ab), rig on a 1 m mount with a lower objective bulk so all lanes are visible (18f33a7).
  Verified: All 83 ETM tests pass (incl. cannon reach to every button and a clear centre-lane sightline); owner on Quest 3: START button works, all lanes visible.
  Remaining: Owner run through the whole loop (results, relocation fade, Level 2, ending, campaign results); visible pause indicator; failure screen
- **2026-11-18 18:23Z** · `claude-code-dartonx-pc` · T-0031 · _claim_
  Owner headset test: the rig spawned above the panel
- **2026-11-18 18:07Z** · `claude-code-dartonx-pc` · T-0031 · _complete_ · commits: 9e22f91,909c365
  Campaign flow (9e22f91) plus a lighting fix (909c365): panel text faced away from the light and rendered black on the headset.
  Verified: All 83 ETM tests pass; PC render of the title stage shows the panel text lit and readable; APK reinstalled on the Quest 3. Owner headset play-through pending.
  Remaining: Owner headset run of the full loop; a visible pause indicator (the menu-button pause shows nothing yet)
- **2026-11-18 18:07Z** · `claude-code-dartonx-pc` · T-0031 · _claim_
  Fix from the owner's headset video: panel text was unlit
- **2026-11-18 08:43Z** · `claude-code-dartonx-pc` · T-0031 · _complete_ · commits: 9e22f91
  Campaign flow on the game instance: Title -> L1 -> brief results -> relocation fade -> L2 -> ending -> campaign results -> title, plus practice. Shootable world-space menu panels. Results tracked (shots, hits, weak-point hits, brace-absorbed damage, retries, time), saved, provisional score. Until real arenas exist, both levels are short stand-in encounters in the sandbox range; the fade dims the range's only light; sun moved behind the rig so panels and enemies are lit.
  Verified: Editor build; all 83 ETM tests pass incl. 5 new ETM.Core.Flow tests (full loop with map loads, run tracking, sandbox stages/panels with a real cannon shot on START, stand-in levels finite); APK packaged and installed on Quest 3. Headset play-through by the owner pending.
  Remaining: Owner headset run of the full loop; text facing and readability on device; failure screen, pause-menu quit, continue-from-checkpoint on the title, interrupted-attack damage for P-30, real arena maps and a fade that works with baked lighting
- **2026-11-18 08:33Z** · `claude-code-dartonx-pc` · T-0031 · _claim_
  Owner picked T-0031 next; T-0006 waits on a Quest 2
- **2026-11-18 08:25Z** · `owner` · T-0043 · _review_
  Approved. Owner asked in chat to close it. Recorded on the owner's behalf by claude-code-dartonx-pc.
- **2026-11-18 08:25Z** · `claude-code-dartonx-pc` · T-0043 · _complete_ · commits: 9586ea3
  Fix shipped inside T-0055: StepHeat carries the fire-cooldown remainder; 72 Hz parity test tightened to one frame and 1%.
  Verified: ETM.Weapons.HeatParity.Quest72Hz passes at the tightened tolerance; owner headset test
- **2026-11-18 08:25Z** · `claude-code-dartonx-pc` · T-0043 · _claim_
  Closing: fix shipped in T-0055 (9586ea3, PR #21)
- **2026-11-18 08:25Z** · `owner` · T-0054 · _review_
  Approved. Approved by the owner in chat after the headset tests; merged via PR #21. Recorded on the owner's behalf by claude-code-dartonx-pc.
- **2026-11-18 08:25Z** · `owner` · T-0053 · _review_
  Approved. Approved by the owner in chat after the headset tests; merged via PR #21. Recorded on the owner's behalf by claude-code-dartonx-pc.
- **2026-11-18 08:12Z** · `owner` · T-0055 · _review_
  Approved. Owner retested on the Quest 3: feels good, approved in chat. Recorded on the owner's behalf by claude-code-dartonx-pc.
- **2026-11-18 01:24Z** · `claude-code-dartonx-pc` · T-0043 · _note_
  Done inside T-0055 (commit 9586ea3): StepHeat carries the cooldown remainder; 72 Hz parity test tightened to one frame and 1%. Can be closed when T-0055 is approved.
- **2026-11-18 01:24Z** · `claude-code-dartonx-pc` · T-0055 · _complete_ · commits: 9586ea3
  P-34 rapid fire in code (10/s, 25 dmg, heat 1 -> 100 shots in 9.9 s), fire-cooldown remainder carried (T-0043), Gatebreaker core 6500 (phase 3 at 1950), design eye Z 110, barrels/muzzle 80 cm, HUD heat bar at 63, sandbox objective 3.5 m and entrances 18 m. Branch stacked on t-0053 (sandbox).
  Verified: Editor build; all 78 ETM automation tests pass (72 Hz heat parity now within one frame and 1%); Android APK packaged and installed on the Quest 3. Standalone g++ heat test updated but not run (no compiler on this PC). Owner retest in the headset pending.
  Remaining: Owner retest on the headset
- **2026-11-18 01:17Z** · `claude-code-dartonx-pc` · T-0055 · _claim_
  Owner's headset feedback
- **2026-11-18 00:41Z** · `claude-code-dartonx-pc` · T-0053 · _note_
  T-0053 branch now also carries T-0054's Android build fixes for the sandbox; review them together.
- **2026-11-18 00:41Z** · `claude-code-dartonx-pc` · T-0054 · _complete_ · commits: 890a0ba
  Android (Clang) build fixes on the T-0053 branch: the sandbox uses ALight::GetLightComponent (ADirectionalLight::GetComponent is editor-only), and three one-pass 'first actor' loops (sandbox ShouldBuildSandbox, interruption FindRig and BindMenuButton) became single iterator checks, since Clang's -Wunreachable-code-loop-increment is an error on Android. Supersedes the earlier completion, which named the wrong commit.
  Verified: Android arm64 Development C++ compiles (the build reaches Gradle, which then fails on Java 25: a toolchain issue, not code). Editor build clean; all 78 ETM tests pass.
  Remaining: Packaging needs JDK 21 (T-0006). Merge with T-0053 (same branch).
  Next: Review with T-0053.
- **2026-11-18 00:41Z** · `claude-code-dartonx-pc` · T-0054 · _claim_
  Re-claimed: previous completion recorded before the commit existed
- **2026-11-18 00:41Z** · `claude-code-dartonx-pc` · T-0054 · _complete_ · commits: 5e733a1
  Replaced the two one-pass 'first actor' loops in UETMInterruptionSubsystem (FindRig, BindMenuButton) with a single iterator check. Clang treats -Wunreachable-code-loop-increment as an error on Android; MSVC accepted them.
  Verified: Android arm64 Development C++ now compiles (the build reaches Gradle; Gradle then fails on Java 25, a separate toolchain issue). Editor build clean and all 78 ETM tests pass. Same branch as T-0053.
  Remaining: None for this fix. Packaging still needs JDK 21 (T-0006).
  Next: Review with T-0053 (same branch).
- **2026-11-18 00:38Z** · `claude-code-dartonx-pc` · T-0054 · _claim_
  Done on the T-0053 branch
- **2026-11-18 00:37Z** · `claude-code-dartonx-pc` · T-0006 · _claim_
  Packaging the T-0053 sandbox for the connected Quest 3; Quest 2 not attached
- **2026-11-18 00:37Z** · `claude-code-dartonx-pc` · T-0053 · _complete_ · commits: 5e733a1
  AETMSandboxGameMode (Source/ETM/Core/Game) is the project default (GlobalDefaultGameMode in Config/DefaultEngine.ini). Player = AXRSeatedRigPawn + ARigPlayerController; each rig is registered with the mission at StartPlay and on RestartPlayer. On the Entry map (the boot map) with no objective present it builds a range in code: one movable shadowless directional light, a 60 m floor, distance posts at 5/15/30/45 m down three lanes (-35, 0, +35 deg), the objective 4.5 m ahead at floor level with a block for its bulk, three target-point entrances 25 m out facing the rig, and an encounter director running one hour-long practice phase (Shardlings from left and centre, Needle Drones from the right, max 5 active), with automatic retry 3 s after a mission failure.
  Verified: Built on UE 5.8.4, zero errors and warnings; all 78 ETM tests pass, 2 new (ETM.Core.Sandbox.*) using FTestWorldWrapper: the default game mode is the sandbox and does not build the range in non-Entry worlds; BuildSandbox gives an objective ahead and below the eye, three valid entrances, one light without shadows, more than 15 range actors; enemies arrive within 10 s of real world ticks; a rig failure retries by itself and restores the rig; building twice is a no-op. Not yet seen in VR Preview or on a headset.
  Remaining: Placeholder grey shapes on default materials; no sky or ambient light, so faces away from the light are dark. The local editor-rewritten DefaultEngine.ini on the build PC also needs GlobalDefaultGameMode set to the sandbox (done locally, not committed). Real arenas replace the range (T-0020/T-0027); the campaign flow (T-0031) will set its own game mode. Branch agent/claude-code-dartonx-pc/t-0053 needs a PR.
  Next: Review T-0053. Then T-0006: package this as the first APK once the engine's Android target is installed.
- **2026-11-18 00:21Z** · `claude-code-dartonx-pc` · T-0053 · _claim_
  Claimed T-0053: Sandbox game mode: rig pawn, floor and distance markers, practice encounter (first playable for VR Preview and the first APK)
- **2026-11-17 14:30Z** · `owner` · T-0010 · _review_
  Approved. Approved by the owner in chat on 2026-11-17 (approve T-0010). Recorded on the owner's behalf by claude-code-dartonx-pc.
- **2026-11-17 14:16Z** · `owner` · T-0030 · _review_
  Approved. Approved by the owner in chat on 2026-11-17 (Approve both). Recorded on the owner's behalf by claude-code-dartonx-pc.
- **2026-11-17 14:16Z** · `owner` · T-0052 · _review_
  Approved. Approved by the owner in chat on 2026-11-17 (Approve both). Recorded on the owner's behalf by claude-code-dartonx-pc.
- **2026-11-17 14:13Z** · `claude-code-dartonx-pc` · T-0030 · _complete_ · commits: a00f2dd
  UETMInterruptionSubsystem (Source/ETM/Platform), a tickable world subsystem that keeps running while paused. Reasons (any combination): Menu (the rig controller's menu button toggles it; ResumeFromMenu for the pause menu), HeadsetRemoved (VRHeadsetRemovedFromHead / PutOnHead from the OpenXR plugin), Background (VRHeadsetLost/Reconnected, app deactivate/background), SystemFocus (FApp::HasVRFocus while an HMD is active), TrackingLost (either controller untracked for 0.3 s, once tracking has been established, headset only). Any reason pauses immediately; when the last clears, a 3 s countdown runs with gameplay still frozen, and a new interruption cancels it. Pause is the engine's world pause via a dedicated pauser player state, so all actor and component ticks stop together and resume unchanged. RequestRecenter / RequestForwardReAnchor work only while paused.
  Verified: Built on UE 5.8.4, zero errors and warnings; all 74 tests pass, 3 new (ETM.Platform.Interruptions.*) that tick a real game world built with the engine's FTestWorldWrapper (game instance, game mode): world ticking moves an enemy and the director's clock; during a 20 s pause the enemy's attack timer, the rig's health, the brace timer and the mission clock do not change; the countdown keeps it frozen for 3 s; afterwards the attack lands braced exactly as left. Headset off/on, removal during the countdown, multiple reasons (menu plus background), lost/reconnected headset, tracking grace, start-up and editor cases, recenter refused during play. Platform events were raised by broadcasting the engine delegates in the test; nothing tried on a headset.
  Remaining: Needs a headset to confirm the real events: whether Quest's OpenXR runtime sends user-presence (headset on/off) events, and how focus changes when the Meta menu opens. Pause menu UI and the countdown display are T-0031. Audio is not explicitly paused (world pause stops gameplay sounds started by ticking code; looping sounds may continue). The 3 s countdown and 0.3 s grace are my values. The first test attempt exposed that the older test files step components by hand rather than ticking a world; T-0049 (shared test-world helper) should move them to FTestWorldWrapper. Branch agent/claude-code-dartonx-pc/t-0030 needs a PR.
  Next: Review T-0030 and T-0052.
- **2026-11-17 14:08Z** · `claude-code-dartonx-pc` · T-0030 · _claim_
  Claimed T-0030: Pause, tracking loss, headset removal, resume countdown
- **2026-11-17 14:07Z** · `claude-code-dartonx-pc` · T-0052 · _complete_ · commits: 93e2da5
  UETMSaveStore gains two static entry points for other systems' slots: SaveChecked (synchronous write of the length+CRC32-wrapped save to the slot and its backup) and LoadChecked (main copy if its header and CRC are intact, else the backup, else null; damaged bytes never reach the engine's parser). AXRSeatedRigPawn::SaveCalibration/LoadCalibration and ARigPlayerController's control-scheme save and load now use them.
  Verified: Built on UE 5.8.4, zero errors and warnings; all 73 ETM tests pass, 2 new (ETM.Save.OtherSlots.*): each slot is written with the ETMS header plus a backup, survives a restart (new pawn / new controller reads it at BeginPlay), recovers from a damaged main copy via the backup, and gives defaults with no crash when both copies are damaged (including a fake engine-format header). The real slots are moved aside during the test and restored afterwards.
  Remaining: Raw-format calibration or input files left from earlier development are now treated as damaged and give defaults once (no migration, on purpose: reading them is the crash path). The T-0007 calibration save test still round-trips the save class through the engine's plain functions on its own test slot; harmless, not changed (outside these paths).
  Next: Review T-0052. T-0030 next.
- **2026-11-17 14:05Z** · `claude-code-dartonx-pc` · T-0052 · _claim_
  Claimed T-0052: Move the calibration and control-scheme saves to the checked save format (damaged files crash the engine's loader)
- **2026-11-17 14:02Z** · `owner` · T-0051 · _review_
  Approved. Approved by the owner in chat on 2026-11-17 (Approve both). Recorded on the owner's behalf by claude-code-dartonx-pc.
- **2026-11-17 14:02Z** · `owner` · T-0023 · _review_
  Approved. Approved by the owner in chat on 2026-11-17 (Approve both). Recorded on the owner's behalf by claude-code-dartonx-pc.
- **2026-11-17 14:00Z** · `claude-code-dartonx-pc` · T-0051 · _complete_ · commits: 6d38507
  UMissionStateSubsystem::ResumeFromCheckpoint(checkpoint): restores exactly like a retry (enemies parked, brace reset, health or the P-04 boss preset, OnRetryStarted so the director rebuilds the phase) without counting as a retry. Retry and resume share one private RestoreLastCheckpoint.
  Verified: Covered by ETM.Save.Checkpoint.BossPresetAfterRestart (director jumps to the phase, preset applied, retry count 0) and the existing ETM.Objectives tests; all 71 pass.
  Remaining: None. Merge with T-0023 (same branch).
  Next: Review with T-0023.
- **2026-11-17 14:00Z** · `claude-code-dartonx-pc` · T-0023 · _complete_ · commits: 8ae601b
  Source/ETM/Save. FETMSettings (difficulty, haptics, reduced flash, three volumes, subtitles and size, aim smoothing, target assistance, toggle-to-vent, hand swap; sanitised on load), FETMSavedCheckpoint (map, FMissionCheckpoint with phase, time, seed, boss flag and health, difficulty, time saved), FETMMissionResult (completion, duration, shots, hits, weak-point hits, damage prevented, retries, score) with last and best completed run per level. UETMSaveStore reads and writes them; UETMSaveSubsystem (game instance) loads at startup, applies settings when a world begins play (feedback haptics and flash, Assisted boss floor 80% and reduced incoming damage), and binds to the mission so every checkpoint is saved. ResumeInto restores a saved checkpoint after restart via the mission (T-0051): boss checkpoints give the P-04 preset. Every slot is written as length+CRC32 header around the engine's save data, to the slot and a backup slot, on a worker thread (stale queued writes dropped). Loading checks the header before the engine parses anything, falls back to the backup, then to defaults.
  Verified: Built on UE 5.8.4, zero errors and warnings; all 71 tests on this branch pass, 5 new (ETM.Save.*), restarts simulated by a fresh store reading the files back from disk: every setting survives and out-of-range values are clamped; checkpoint saved automatically through the mission, survives restart with phase/seed/boss flag/health/difficulty, resumes into a director at the boss phase with rig 300 and objective 60% (80% on Assisted), not a retry; a midpoint resumes exact values; cleared checkpoint stays cleared; results keep best and last with P-30 stats; settings applied to a real rig pawn and mission. Found and fixed: a damaged save file made the engine assert (crash) inside LoadGameFromSlot; now garbage, truncated and fake-engine-header files fall back to the backup or defaults with no crash. Async writes are not exercised by the tests (they write synchronously); nothing tested on a headset's storage.
  Remaining: The calibration (ETM_Calibration) and control scheme (ETM_Input) slots from T-0007 and T-0012 still use the engine's plain load, so a damaged copy of either could still crash the game: filed as a follow-up. Score is computed by the results screen (T-0031); the stats themselves are not yet collected during play. Continue flow (load map, start encounter, ResumeInto) belongs to T-0031. Assisted damage scale 0.7 is my value; the bible only says 'reduced'. Branch agent/claude-code-dartonx-pc/t-0023 also carries T-0051.
  Next: Review T-0023 and T-0051 (same branch), then the slot follow-up.
- **2026-11-17 13:53Z** · `claude-code-dartonx-pc` · T-0051 · _claim_
  Resume entry point for T-0023, same branch
- **2026-11-17 13:52Z** · `claude-code-dartonx-pc` · T-0023 · _claim_
  Claimed T-0023: Save system: settings, checkpoints incl. boss presets (P-04), results
- **2026-11-17 13:43Z** · `owner` · T-0050 · _review_
  Approved. Approved by the owner in chat on 2026-11-17 (Approve all three). Recorded on the owner's behalf by claude-code-dartonx-pc.

_55 older entries in `tracking/reports/`._
