# Enter The Matricks: Tracker

Planning and coordination repo for **Enter The Matricks** (codename **ETM**), a seated dual-cannon VR survival shooter for Meta Quest 2 built in Unreal Engine 5.

> ⚠️ *Working title.* It is close to an existing franchise title. Don't use it publicly until clearance is done (see `docs/PLAN_REVIEW.md` P-16).

| Start here | |
|---|---|
| 🧭 **[RESUME_HERE.md](RESUME_HERE.md)** | Handoff note + live snapshot: read first, every session |
| 🤖 **[AGENTS.md](AGENTS.md)** | Multi-agent protocol: claim → work → commit → complete |
| 📋 **[BOARD.md](BOARD.md)** | Task board with progress per milestone (generated) |
| 📝 **[ACTIVITY_REPORT.md](ACTIVITY_REPORT.md)** | Brief activity log, newest first (generated) |
| 🗺️ [docs/DEVELOPMENT_PLAN.md](docs/DEVELOPMENT_PLAN.md) | Milestones, gates, calendar, parallel streams |
| 📖 [docs/PRODUCT_BIBLE.md](docs/PRODUCT_BIBLE.md) | The spec (v1.1) |
| 🔍 [docs/PLAN_REVIEW.md](docs/PLAN_REVIEW.md) | The 22 fixes applied to v1.0 |
| 🎨 [docs/CONCEPT_ART_REVIEW.md](docs/CONCEPT_ART_REVIEW.md) | What to keep and change from the concept art |

**Game source:** [enter-the-matricks](https://github.com/darlingtonchikezietech-alt/enter-the-matricks)

## Tools (Python 3.9+, no dependencies)

```bash
python3 tools/agent.py next --agent me      # what can I work on?
python3 tools/agent.py status               # full board in the terminal
python3 tools/agent.py validate             # integrity check (runs in CI)
python3 tools/balance_sim.py --check        # verifies the bible's combat maths (runs in CI)
```
