---
time: 2026-11-17T14:07:58Z
agent: claude-code-dartonx-pc
task: T-0052
kind: complete
commits: 93e2da5
---

UETMSaveStore gains two static entry points for other systems' slots: SaveChecked (synchronous write of the length+CRC32-wrapped save to the slot and its backup) and LoadChecked (main copy if its header and CRC are intact, else the backup, else null; damaged bytes never reach the engine's parser). AXRSeatedRigPawn::SaveCalibration/LoadCalibration and ARigPlayerController's control-scheme save and load now use them.
Verified: Built on UE 5.8.4, zero errors and warnings; all 73 ETM tests pass, 2 new (ETM.Save.OtherSlots.*): each slot is written with the ETMS header plus a backup, survives a restart (new pawn / new controller reads it at BeginPlay), recovers from a damaged main copy via the backup, and gives defaults with no crash when both copies are damaged (including a fake engine-format header). The real slots are moved aside during the test and restored afterwards.
Remaining: Raw-format calibration or input files left from earlier development are now treated as damaged and give defaults once (no migration, on purpose: reading them is the crash path). The T-0007 calibration save test still round-trips the save class through the engine's plain functions on its own test slot; harmless, not changed (outside these paths).
Next: Review T-0052. T-0030 next.
