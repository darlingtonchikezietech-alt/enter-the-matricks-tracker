---
time: 2026-11-17T10:42:23Z
agent: claude-code-dartonx-pc
task: T-0044
kind: complete
commits: 9fa05eb
---

ETM.Build.cs: bUseUnity = false, with a comment explaining why. Unreal merges a game module's .cpp files once it has 32 or more source files (TargetRules.MinGameModuleSourceFilesForUnityBuild = 32); the test files' file-local helpers (Frame72, FTestWorld) then clash.
Verified: From an empty worktree of main (25 source files): builds clean both with and without the fix, 15 tests pass. On the T-0014 tree (38 source files, Intermediate for ETM deleted): fails without the fix with C2374/C2011 redefinitions, builds clean with it, all 24 tests pass.
Remaining: Merge this before T-0014 and before the other pending branches; merging those first would push main past 32 files and break clean builds. Renaming the helpers per file would also work, but touches six test files owned by other tasks.
Next: Merge order: T-0044, then T-0009, T-0012, T-0018, T-0010, then T-0014 (stacked on T-0018).
