# CLAUDE.md

Read `RESUME_HERE.md`, then follow `AGENTS.md` exactly. Summary:

- Set a unique identity: `export ETM_AGENT=claude-<something>`.
- Never edit files without a claim: `python3 tools/agent.py next` → `claim T-xxxx --push`.
- Work in the sibling game repo `../enter-the-matricks`, only inside your task's `paths`; commit as `[T-xxxx] ...`.
- Finish with `complete` (or `release`) and `--push` before your session ends.
- Don't hand-edit `BOARD.md`, `ACTIVITY_REPORT.md`, or the AUTO block in `RESUME_HERE.md`.
- `docs/PRODUCT_BIBLE.md` is the spec. Propose spec changes as `P-xx` entries in `docs/PLAN_REVIEW.md`.
