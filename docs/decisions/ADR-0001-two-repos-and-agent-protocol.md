# ADR-0001: Two repos and a file-based multi-agent protocol

- **Status:** Accepted · 2026-11-16 · decided by the owner (repo layout) and Claude (protocol)

## Context
Several AI agents will work in parallel. Unreal binary assets (`.uasset`, `.umap`) can't be merged, so two agents editing one asset loses work (bible §18 risk). The owner chose two public repos on the personal account.

## Decision
- `enter-the-matricks` holds only the Unreal project. `enter-the-matricks-tracker` holds the plan, tasks, claims, reports and tools.
- Coordination is plain files in git (no external service), so any AI that can run Python and git can join.
- A claim is one file per task. Each task declares owned path globs; overlapping claims are refused.
- The game repo's hooks enforce claimed paths and `[T-xxxx]` commit tags.
- Completed work goes to `review` and a different agent approves it.

## Consequences
- An agent must clone both repos side by side.
- Path globs are compared conservatively (prefix overlap), so occasionally two unrelated tasks are treated as conflicting. That is safer than the reverse.
- The board and activity report are generated. Merge conflicts in them are fixed by re-running `render`.
