---
time: 2026-11-17T10:46:34Z
agent: claude-code-dartonx-pc
task: T-0045
kind: complete
commits: 2c5541a
---

UAttackTokenSubsystem (Source/ETM/Enemies/Base): default limit 2 (bible section 14). AEnemyBase::BeginAttack takes a token and is refused while none is free; the archetypes already retry each frame. Tokens return when the attack resolves, the enemy is staggered, dies, is parked or is destroyed (stale holders are pruned). SetMaxConcurrentAttacks changes the limit without cancelling attacks in progress; bUsesAttackToken lets a harmless attack opt out; a refusal counter helps tuning. BeginAttack now also refuses outright from states that cannot deal damage.
Verified: Built on main (UE 5.8.4), zero errors and warnings. New test ETM.Enemies.Base.AttackTokens passes, plus all 15 existing tests on main. Not run together with the T-0014 archetypes yet (that happens on the T-0017 branch).
Remaining: Every attack counts, including Shardling cuts on the objective; if that makes enemies queue too much in playtests, give objective attacks their own limit or opt them out. Branch agent/claude-code-dartonx-pc/t-0045 needs a PR into main.
Next: T-0017 uses this to enforce the 2-attack cap.
