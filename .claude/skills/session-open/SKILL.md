---
name: session-open
description: "Open a new framework session — creates a `session/<id>` branch, scaffolds the session doc with Context + Decisions + Handoff, and posts 📍 lifecycle comments on each Issue entering `in-play`. Use whenever a unit of work starts that will cross multiple roles or sustained turns. Examples: 'open a session for the checkout flow', 'start a session on feature #42', '/session-open redis-cache-spike'. See `framework/SKILL.md` § Sessions for the model."
---

# session-open

## Purpose

A **session** is a unit of work that may cross multiple roles (per framework SKILL § Sessions). Opening a session creates the three artifacts that persist across role handoffs:

- A git branch `session/<YYYY-MM-DD>-<slug>` that isolates the session's commits.
- A doc `sessions/<YYYY-MM-DD>-<slug>.md` with the 3-part scaffold (Context, Decisions, Handoff).
- A 📍 lifecycle comment on every Issue entering `in-play`, so the graph remembers this session touched them.

This skill performs all three steps atomically. Run it at the **start** of any meaningful work block. Don't open a session for a single-Issue edit (e.g. updating a status); that's overhead.

## When to invoke

- The work will cross several conversations (different roles, different days).
- The work touches multiple Issues that need to be tracked as a unit.
- You will make binding decisions worth recording in a Decisions log.
- Conversely: **don't open a session** for a trivial edit, a single comment, or a read-only exploration.

## How to use

1. **Ensure you're on `main`** with a clean working tree. The script branches off the current branch (default `main`); make sure it is clean.

2. **Run the script** with a short slug and the Issues that enter in-play:

   ```bash
   .venv/bin/python scripts/skills/session_open.py <slug> \
       --context "Why this session exists, one paragraph" \
       --in-play "#42,#43" \
       --role product-manager \
       --next "First concrete step the role takes"
   ```

   - `<slug>` is a short identifier (e.g. `checkout-flow`, `redis-cache-spike`). The date gets prepended automatically.
   - `--context`: stable paragraph saying *why* this session exists. Edited rarely.
   - `--in-play`: Issues already known to be touched. More can be added during the session by editing the doc.
   - `--role`: the role you intend to start with (defaults to `product-manager`).
   - `--next`: one-line description of the first step you'll take.

3. **Verify the output** lists:
   - The branch name (e.g. `session/2026-05-24-checkout-flow`)
   - The doc path
   - How many 📍 comments posted (should equal the count in `--in-play`)

4. **Open the doc** (`sessions/<id>.md`) and refine the Context paragraph + Handoff if needed. The scaffolded text is a starting point; you own it.

5. **Continue working on the new branch.** The next conversation that opens on this branch will be greeted by the SessionStart hook, which injects the doc as context.

## The three artifacts

After this skill completes:

- **Branch** `session/<id>` is checked out and contains an initial commit with the doc.
- **Doc** at `sessions/<id>.md` has the structure:
  ```
  ---
  id: <id>
  opened: <today>
  in-play: ["#42", "#43"]
  ---

  ## Context
  ...

  ## Decisions

  ## Handoff
  Active role: ...
  In play: ...
  Next: ...
  ```
- **📍 Issue comments** on each in-play reference, linking back to the session doc.

## What this skill does NOT do

- It does not validate that the slug is unique against existing branches — if a branch with the same name exists, `git checkout -b` fails and the script exits non-zero. Pick a fresh slug.
- It does not open any PRs. That's `/session-close`'s territory if you decide to PR the branch at the end.
- It does not commit anything beyond the session doc itself. Your work commits during the session are normal.

## Related

- `framework/SKILL.md` § Sessions — the full session model
- `/session-close` skill — the counterpart that closes the session
- `/catch-up` skill — for digesting changes that happened while you were away
