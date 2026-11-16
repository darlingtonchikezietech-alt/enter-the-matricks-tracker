# Development Plan

Derived from bible §16 (v1.1). Live task status is in `BOARD.md`. This file holds the *plan*: milestones, gates, calendar and parallel work streams.

## Calendar

| Item | Value |
|---|---|
| Team start date (Week 1) | **TBD — owner to set (T-0002)** |
| Quest 2 new-app submission cutoff | December 2027 (Meta announcement, Nov 2026, P-15) |
| Target store submission | No later than **end of Q3 2027** |
| Required slack before cutoff | ≥ 12 weeks (P-24) |

Once the start date is known, fill in the "Dates" column below. If Week 16 lands after **2027-09-30**, raise it as a risk immediately.

## Milestones

| Milestone | Weeks | Dates | Exit gate (needs evidence in `docs/reports/Mx/`) | Gate task |
|---|---|---|---|---|
| **M0 Foundation** | 1 | TBD | Scaffold compiles; packaged scene runs on Quest 2; seated pawn tracks correctly | — |
| **M1 Combat proof** | 2–3 | TBD | Comfortable, readable 3-minute combat test on device. **Stop/go.** | T-0016 |
| **M2 Vertical slice** | 4–6 | TBD | Sustained 72 Hz in representative combat; weapon feel validated | T-0025 |
| **M3 Campaign alpha** | 7–10 | TBD | Both missions playable end to end in a packaged build | T-0033 |
| **M4 Content beta** | 11–13 | TBD | No missing critical assets; 10-player timing/readability test | T-0038 |
| **M5 Release candidate** | 14–16 | TBD | All §17 acceptance criteria have evidence; zero blockers | T-0040 |

A milestone is complete only when its gate task is **done** (reviewed and approved), not when its last feature lands.

## Parallel work streams

Tasks declare owned paths, so these streams can run at the same time with separate agents:

```
Stream A  Engine/Platform   toolchain → deploy → perftools → interrupt → optimize
Stream B  Player/Weapons    pawn → cannon → heattest ; pawn → input
Stream C  Combat/Enemies    combat → enemybase → enemies2 → enemies4 ; combat → objective
Stream D  Encounters/Boss   director → gatebreaker ; (M3) conductor → l2full
Stream E  Levels/Art        concept art v2 (now) → rig blockout → greyboxes → art kits (M4)
Stream F  UI/Flow/Save      hud → flow → vo ; save
Stream G  Producer/QA       calendar, title clearance, gate reports, playtests, submission
```

Suggested agent count: **2–3 during M0–M1** (the dependency chain is narrow) and **4–6 during M2–M4**.

## Build order (bible §16, unchanged)

1. Packaged empty VR scene → 2. Seated rig + independent aim → 3. One cannon with weight → 4. Second cannon + independent heat → 5. Ground + flying enemy → 6. Objective damage + failure → 7. Three-minute mixed encounter → 8. Boss weak-point prototype → 9. Full Level 1 → 10. Full Level 2.

**Stop/go:** if the 3-minute combat proof is uncomfortable or misses the hardware budget, fix that before any final campaign assets are made.

## Reporting

Each task completion records (via `agent.py complete`): what changed, commits, verification performed, remaining problems, and next recommended action. That covers bible §16 "Progress reporting". Gate tasks also add a report under `docs/reports/Mx/`.
