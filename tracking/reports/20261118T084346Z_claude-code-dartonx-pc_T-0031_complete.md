---
time: 2026-11-18T08:43:46Z
agent: claude-code-dartonx-pc
task: T-0031
kind: complete
commits: 9e22f91
---

Campaign flow on the game instance: Title -> L1 -> brief results -> relocation fade -> L2 -> ending -> campaign results -> title, plus practice. Shootable world-space menu panels. Results tracked (shots, hits, weak-point hits, brace-absorbed damage, retries, time), saved, provisional score. Until real arenas exist, both levels are short stand-in encounters in the sandbox range; the fade dims the range's only light; sun moved behind the rig so panels and enemies are lit.
Verified: Editor build; all 83 ETM tests pass incl. 5 new ETM.Core.Flow tests (full loop with map loads, run tracking, sandbox stages/panels with a real cannon shot on START, stand-in levels finite); APK packaged and installed on Quest 3. Headset play-through by the owner pending.
Remaining: Owner headset run of the full loop; text facing and readability on device; failure screen, pause-menu quit, continue-from-checkpoint on the title, interrupted-attack damage for P-30, real arena maps and a fade that works with baked lighting
