---
name: catch-up
description: "Digest of changes in the graph since the last invocation (or a custom timeframe). Surfaces Issue updates and PR merges grouped by category, so a returning agent can orient quickly without scanning the full Issue list. Examples: 'catch me up on what changed', 'what's new since last week', '/catch-up --since 7d'."
---

# catch-up

## Purpose

When you return to the project after a break — minutes, hours, days — you need to know what changed in the graph. `SessionStart` injects the current session doc, but doesn't tell you about **work that happened elsewhere**: Issues someone else updated, PRs that merged, comments that landed on Issues you care about.

This skill produces a structured digest of those changes since a chosen point in time (defaulting to your last `catch-up` invocation).

## When to invoke

- At the start of a session that has been paused for a meaningful time.
- After being away from the project (the catch-up tells you what to read first).
- As a periodic check during long sessions.
- When the framework's SessionStart context isn't enough — `SessionStart` is small on purpose; this skill is the on-demand deeper read.

## How to use

```bash
.venv/bin/python scripts/skills/catch_up.py [--since <when>]
```

The `--since` argument accepts:

- **No argument**: defaults to the last time you ran `catch-up` (persisted in `.sem-ai/last-catch-up.json`), or 24 hours ago if it's the first run.
- **Relative duration**: `24h`, `7d`, `2w`, `30m` (h=hours, d=days, w=weeks, m=minutes).
- **ISO timestamp**: e.g. `2026-05-01T00:00:00Z`.

Examples:

```bash
# Since last invocation (default)
.venv/bin/python scripts/skills/catch_up.py

# Last 7 days
.venv/bin/python scripts/skills/catch_up.py --since 7d

# Since a specific moment
.venv/bin/python scripts/skills/catch_up.py --since 2026-05-20T12:00:00Z

# Don't update the state file (e.g. just peek)
.venv/bin/python scripts/skills/catch_up.py --since 7d --no-state
```

## What the output looks like

```markdown
# Catch-up — changes since 2026-05-20 14:30 UTC

## Issues updated (12)

### goal (2)
- #5 [open] _2026-05-22 09:14_ — Increase Q3 retention
- #6 [open] _2026-05-21 17:02_ — Reduce time-to-first-value

### capability (4)
- #12 [open] _2026-05-23 11:45_ — Onboarding flow rebuild
- #14 [open] _2026-05-22 16:30_ — Self-serve billing
- ...

### feature (5)
- ...

### bug (1)
- #99 [closed] _2026-05-21 08:30_ — Login page 500 on Safari

## PRs merged (3)
- PR #42 _2026-05-23 11:45_ — feat: rebuild onboarding stepper
- PR #44 _2026-05-22 09:20_ — fix: safari login redirect
- ...
```

Issues are grouped by type (vision / goal / capability / feature / story / spec / adr / bug). Within each group, sorted by last update time.

## How to read it

- **Glance at the categories first.** If 10 goals changed and 0 features, the strategic layer moved; if 0 goals and 20 features changed, day-to-day delivery happened.
- **Open Issues with state changes.** A `[closed]` on a feature you were tracking is a signal to read what happened.
- **Cross-reference with your in-play list.** If your session's `in-play` contains #42 and the digest shows #42 was updated, open it.
- **PRs merged matter for artifacts.** If a PR closed an Issue you care about, the artifact derivation hook posted a 📦 comment with the changed files.

## State file

`.sem-ai/last-catch-up.json` stores the last invocation timestamp. The file is small (`{"last_invocation": "..."}` ) and `.gitignore`-suitable — but the framework doesn't require it to be ignored. Per-dev local state is fine to commit if the team prefers; not committing it means each dev has their own catch-up baseline.

## What this skill does NOT do

- Does not subscribe to GitHub Notifications or run continuously. It's a pull, not a push.
- Does not filter by your in-play Issues automatically (the digest is project-wide). If you only want your in-play, look at those Issues directly via `mcp__sem_ai_engine__get_node`.
- Does not include comments — only Issue updates and PR merges. Comments-on-Issues you care about are best seen by opening the Issue directly.

## Related

- `framework/SKILL.md` § Sessions and the SessionStart hook — for the always-on bootstrap
