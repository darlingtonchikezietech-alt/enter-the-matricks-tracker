# AGENTS.md: How AI agents work on Enter The Matricks

Any AI or human contributor follows this protocol. It lets several agents work in parallel without overwriting each other.

## The two repos

| Repo | Holds | Clone to |
|---|---|---|
| `enter-the-matricks-tracker` (this one) | Bible, plan, review, task board, claims, activity reports, tools | `./enter-the-matricks-tracker` |
| `enter-the-matricks` | The Unreal project (C++, config, content via Git LFS) | `./enter-the-matricks` (sibling folder) |

Clone both **side by side**. `etm.config.json` expects the game repo at `../enter-the-matricks`.

## Golden rules

1. **Read `RESUME_HERE.md` first, every session.** Then `docs/PRODUCT_BIBLE.md` for the sections your task touches.
2. **One task at a time.** Claim it before touching any file. No claim, no edits.
3. **Stay inside your task's `paths`.** The game repo's pre-commit hook enforces this. If you need a file outside your paths, either ask the claim holder (via `log`) or add a new task.
4. **The bible is the spec.** If the spec is wrong or ambiguous, don't silently diverge. Log it, propose a patch in `docs/PLAN_REVIEW.md` with a new `P-xx` ID, and mark your task `--blocked` if you can't proceed.
5. **Verify, then report honestly.** `complete --verified` states what you actually ran (compiled? ran on Quest 2? editor only?). Never claim device verification you didn't do.
6. **Don't hand-edit generated files**: `BOARD.md`, `ACTIVITY_REPORT.md`, and the AUTO block in `RESUME_HERE.md`. Run `python3 tools/agent.py render`.
7. **No franchise IP.** Never use "Zion", "Sentinel", "the Matrix", green code rain, or copied silhouettes, in assets, names, prompts, or comments (bible §2, P-16).

## The loop

```bash
export ETM_AGENT=claude-a            # unique, stable name per agent instance
cd enter-the-matricks-tracker

python3 tools/agent.py sync           # pull the latest board
python3 tools/agent.py next           # ready tasks: deps done, unclaimed, no path conflict
python3 tools/agent.py show T-0005    # read the task: paths, acceptance, dependencies
python3 tools/agent.py claim T-0005 --push      # lock it (creates tracking/claims/T-0005.json)

# --- work in the game repo, on the branch the claim printed ---
cd ../enter-the-matricks
git switch -c agent/$ETM_AGENT/t-0005
# ...edit only your task's paths...
git commit -m "[T-0005] Compile scaffold on UE 5.x; fix include paths"   # hook checks paths + tag
git push -u origin agent/$ETM_AGENT/t-0005      # then open a PR into main

# --- long task? refresh the claim at least every few hours ---
cd ../enter-the-matricks-tracker
python3 tools/agent.py heartbeat T-0005 --note "Editor compiles; Android packaging next" --push

# --- done ---
python3 tools/agent.py complete T-0005 --push \
  --summary "Scaffold compiles on UE 5.x Development Editor" \
  --commits "a1b2c3d" \
  --verified "Built Development Editor Win64; no device test" \
  --remaining "Android packaging not tried" \
  --next "T-0006 deploy to Quest 2"
```

`complete` moves the task to **review**. A *different* agent (or the owner) approves it:

```bash
python3 tools/agent.py review T-0005 --approve --note "Checked build log" --push
python3 tools/agent.py review T-0005 --reject  --note "Toolchain doc missing NDK version" --push
```

When a task is approved its dependants become ready. If nothing is ready for you, review someone's work.

## Stuck or stopping

```bash
python3 tools/agent.py release T-0005 --reason "Context limit; WIP pushed on branch" --push   # back to todo
python3 tools/agent.py release T-0005 --blocked --reason "Needs owner decision on UE version" --push
```

Before ending a session **always** either `complete` or `release`, and push your WIP branch. Claims without a heartbeat for 24 h are **stale**. Another agent may take them over with `claim T-xxxx --force`. Takeovers are logged.

## How conflicts are prevented

| Mechanism | Prevents |
|---|---|
| A claim is a separate file per task | Two agents claiming one task: the second push hits a conflict and `agent.py` aborts |
| Task `paths` + overlap check at claim time | Two agents editing the same files (especially binary `.uasset`s, which can't merge) |
| Game-repo pre-commit hook (`check-staged`) | Committing outside your claimed paths |
| Commit-msg hook | Commits without a `[T-xxxx]` tag (no traceability) |
| One file per activity entry | Merge conflicts in the activity log |
| Generated board/report | Editing races on summary files (on conflict, just run `render`) |
| `validate` in CI | Broken deps, cycles, orphan claims, overlapping claims |

## New work

Found something that needs doing? Add a task instead of scope-creeping your current one:

```bash
python3 tools/agent.py add --title "Bulwark shield deflect VFX" --milestone M2 --area vfx \
  --paths "Content/ETM/VFX/Bulwark/**" --acceptance "Deflect reads at 20 m" --depends T-0022 --push
```

## Commit and PR conventions

- Commits: `[T-0012] imperative summary`. One task per commit.
- Branches: `agent/<agent>/<task-id>`. PR into `main`; title starts with the task ID.
- Binary assets: tracked by Git LFS (see the game repo's `.gitattributes`). Never commit a `.uasset` outside your claimed paths.
- Tracker commits are made by `agent.py` itself. Don't commit `tracking/` by hand except to fix a mistake.

## Setup for a new agent (once)

```bash
git clone https://github.com/darlingtonchikezietech-alt/enter-the-matricks-tracker
git clone https://github.com/darlingtonchikezietech-alt/enter-the-matricks
cd enter-the-matricks && git lfs install && git config core.hooksPath .githooks
```
