# Activity Report

_Brief log of what happened, newest first. Generated from `tracking/reports/`. Add entries with `tools/agent.py log` or `complete`._

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
- **2026-11-17 13:43Z** · `owner` · T-0019 · _review_
  Approved. Approved by the owner in chat on 2026-11-17 (Approve all three). Recorded on the owner's behalf by claude-code-dartonx-pc.
- **2026-11-17 13:43Z** · `owner` · T-0022 · _review_
  Approved. Approved by the owner in chat on 2026-11-17 (Approve all three). Recorded on the owner's behalf by claude-code-dartonx-pc.
- **2026-11-17 13:42Z** · `claude-code-dartonx-pc` · T-0050 · _complete_ · commits: 003668d
  AXRSeatedRigPawn creates a UHUDPresenterComponent ('HUD') attached to its root.
  Verified: Covered by the ETM.UI.Presenter tests, which use the real rig pawn's HUD; all 60 tests pass.
  Remaining: None. Merge together with T-0019 (same branch).
  Next: Review with T-0019.
- **2026-11-17 13:42Z** · `claude-code-dartonx-pc` · T-0019 · _complete_ · commits: f1f82ed
  UHUDPresenterComponent (Source/ETM/UI), event-driven, on the rig pawn. Placement per bible section 11: heat bar on each cannon housing near the muzzle plus a lock bracket when overheated; rig integrity bar and 'RIG n' on the central lower frame; brace readiness bar on the frame (full ready, empty in use, refills through the cooldown); objective marker 'POWER n%' above the equipment, pulsing while it is under attack; enemy warnings as '! seconds' markers above each source, the 3 most urgent (soonest, rig attacks win ties), with an edge arrow for sources more than 50 deg off view; '[ OPEN seconds ]' on exposed Gatebreaker weak points; a short objective line; a secondary line for score/narrative that is hidden whenever a critical warning is up. Binds to enemies, bosses and the objective by scanning every 0.5 s (and catches attacks already running). Pure ranking and priority rules in UI/HudModel.h.
  Verified: Built on UE 5.8.4, zero errors and warnings; all 60 tests on this branch pass, 5 new (ETM.UI.*): ranking, tie-break, cap, secondary expiry, view cone; frame elements 1-2 m from the design eye, below eye height, on the frame, rig bar central; heat and lock per housing; rig text; brace 1 -> 0 -> 0.5 at 8 s -> 1; objective marker text and alarm; 4 attacks -> 3 markers above sources with countdowns, edge arrow only for the off-view one, queued warning moves up, warnings end with their attacks, secondary hidden then back then expires, late-bound attack still warned; boss marker on the open node, gone when it closes. Not seen in a headset: text orientation, size and angular readability are unverified.
  Remaining: Text faces the seat by a fixed 180 deg turn and world markers face the head each frame; readability at 1-2 m must be checked on a headset (bible: angular readability tests). Placeholder bars and engine text, no UI art (T-0034). Subtitles (T-0032) and results panel (T-0031) are not here. Warnings for attacks against the objective show as normal warnings; Lance and Bomber designated targets are known but not shown. Scanning every 0.5 s: a warning can appear up to 0.5 s late only for an enemy spawned and attacking within that time. Branch agent/claude-code-dartonx-pc/t-0019 also carries T-0050.
  Next: Review T-0019 and T-0050 (same branch).
- **2026-11-17 13:36Z** · `claude-code-dartonx-pc` · T-0050 · _claim_
  Wiring for T-0019, same branch
- **2026-11-17 13:35Z** · `claude-code-dartonx-pc` · T-0019 · _claim_
  Claimed T-0019: Diegetic HUD presenter: heat on housings, integrity on frame, warnings at source
- **2026-11-17 13:35Z** · `claude-code-dartonx-pc` · T-0022 · _complete_ · commits: 1c5e180
  Four archetypes in Source/ETM/Enemies/Archetypes with values from bible section 7 and P-09. Bulwark: 480 HP body covered by a x0.1 shield (passes to the body), two 80 HP weak-point nodes; breaking either drops the shield, opens the body and staggers it; walks to the objective and slams it for 30 every 4 s (1 s wind-up, shield heaves up); infrastructure attacker. Lance Walker: 320 HP; walks up to 6 m in, plants, charges 2 s with its 160 HP weak-point chamber exposed only while charging (2 shots interrupt); strike 35 to its designated target (rig by default; targeting the objective adds the infrastructure tag); lance swells as the cue. Siphon: 200 HP; crawls to the objective, 1.5 s latch warning with a visible tether, then drains 5/s in 0.25 s pulses until destroyed. Cradle Bomber: 160 HP carrier; hovers 6 m above its designated target, pod swells and tone falls 1.5 to 0.75 over 2 s, releases 40; one weak-point shot on the 80 HP pod destroys the carrier; re-arms after 5 s. Shared helpers in ArchetypeSupport.h.
  Verified: Built on UE 5.8.4, zero errors and warnings; all 61 ETM tests pass, 6 new: every bible value; Bulwark shield x0.1, covered body, slam timing 30 at 1 s then every 4 s, node breaks shield and cancels a wind-up, open body takes full damage; Lance plants within 6 m, chamber only hittable while charging, 35 strike, 2 shots interrupt, objective targeting and tag sync; Siphon tether during warning, no drain during it, ~5/s after, stops on death; Bomber hovers above target, pod and descending tone cues, 40 release, pod shot kills it, objective targeting; pooled reuse restores shield, nodes, chamber, pod and clears tags; silhouettes: every pair differs by 30%+ in a dimension (Shardling 125x68x63, Drone 159x100x94, Bulwark 360x112x230, Lance 297x153x415, Siphon 160x70x115, Bomber 180x180x137 cm). No headset, no art, no sound assets (cue sound slots empty).
  Remaining: Prototype values not in the bible: Bulwark 1 s wind-up, 120 cm/s, 2 m contact; Lance 6 m advance, 0.6 s plant, 4 s cooldown; Siphon 1.5 s latch warning, 200 cm/s; Bomber 5 s re-arm, 6 m hover, 300 cm/s. Bomber release hits instantly (no falling pod). Bulwark shield's x0.1 is applied by the enemy, so the cannon's shot result still reports x1 there. Silhouette distinctness is measured by bounding size, not seen at 5-45 m in a headset. Branch agent/claude-code-dartonx-pc/t-0022 needs a PR.
  Next: Review T-0022. T-0019 next (HUD), then T-0026 (Level 1 schedule) is unblocked once T-0022 is approved.

_48 older entries in `tracking/reports/`._
