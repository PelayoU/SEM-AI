---
name: session-close
description: "Close the current framework session — finalize the Handoff, post 🏁 lifecycle comments on in-play Issues, and decide the disposition of the branch (merge, PR, or discard). Use at the end of a session whether or not it produced value. Examples: 'close this session', 'wrap up the current session and PR it', '/session-close --outcome \"capability validated\"'. See `framework/SKILL.md` § Sessions."
---

# session-close

## Purpose

Closing a session is **deliberate**, not implicit. Per framework SKILL § Sessions, the close moment is when:

- The Handoff is finalized so it reflects the actual outcome (not the opening intent).
- Each in-play Issue receives a 🏁 comment recording what happened to it.
- The branch's disposition is decided: merge to main, open a PR for review, or discard.

This skill performs the close mechanics (Handoff + 🏁 + disposition prompt) but **the disposition decision is yours**. The script will print three options and the agent must execute the one the human chooses.

## When to invoke

- The session's work is complete (or has reached a meaningful stopping point worth recording).
- You're handing off the work to another role or to "tomorrow" — the doc has to reflect the final state, not the opening assumption.
- A session can also be closed when it failed to produce value — learning is the guaranteed output of every cycle, and closure preserves the learning.

**Don't auto-close on a context switch.** If you are pausing work but expect to return, leave the session open and rely on `SessionStart` to re-hydrate you. Only close when the work block is genuinely done.

## How to use

### Step 1: ensure the doc reflects the final state

Before running the close script, open the session doc (`sessions/<id>.md`) and update the **Handoff section** to reflect the actual final state — what was done, what was learned, what (if anything) is left for the next session.

If you made binding decisions during the session that aren't in **Decisions** yet, add them now. Decisions is the bridge to future readers; the close is the last chance to populate it honestly.

### Step 2: run the close script

```bash
.venv/bin/python scripts/skills/session_close.py \
    --outcome "One-line summary of what shipped or what was learned"
```

- `--outcome`: shows up in the 🏁 comments on each in-play Issue. Be specific: "capability validated; opening delivery feature #88" or "experiment invalidated the hypothesis; learning extracted to ADR-NN".
- `--no-comments`: skip posting comments (only use if the session didn't touch any Issue).

The script will:

1. Verify the current branch is a `session/*` branch.
2. Parse the in-play list from the doc's frontmatter.
3. Post 🏁 comments on each in-play Issue.
4. Print three disposition options for the branch.

### Step 3: decide disposition

The script does NOT execute the disposition. The human decides one of:

**Option A — Merge to main** (the common case when the work is done and reviewed):
```bash
git checkout main
git merge --no-ff session/<id>
git branch -d session/<id>
```

**Option B — Open a PR** (for code review or when other reviewers need to weigh in):
```bash
gh pr create --base main --head session/<id>
```
The PR's body should reference any specs/features it closes via `Closes #N` so the artifacts hook can derive them post-merge.

**Option C — Discard the branch** (when the session produced no useful commits — pure exploration that didn't crystallize):
```bash
git checkout main
git branch -D session/<id>
```
Note: the 🏁 Issue comments are still posted (the learning is recorded). The branch goes away; the trace remains in the Issue thread.

## What the 🏁 comment looks like

```
🏁 Session closed: [session/<id>](url) — <outcome>
```

This format is mechanical (the `🏁` marker is load-bearing for the framework's get_node_artifacts derivation). Don't customize the marker; customize only the outcome text via `--outcome`.

## What this skill does NOT do

- Does not auto-decide the disposition. That's the human's call.
- Does not auto-commit the final state of the doc — if you edited the Handoff just before running, **make sure you've committed those edits** (or the post-close branch will have an uncommitted modification).
- Does not advance Issue statuses (e.g. spec → done). That's `transition_status` and is the agent's call before closing the session.

## Related

- `/session-open` — the counterpart
- `framework/SKILL.md` § Sessions — the full model
- `node-templates/SKILL.md` § feature template — Value chain + Uncertainty addressed sections, the guidance before closing experimental features
