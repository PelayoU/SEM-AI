---
description: Re-read the current session document into context (anti-context-drift for long sessions).
allowed-tools: Bash, Read
---

Re-load the current SEM-IA session context.

Use this when a conversation has gone long and you want to re-anchor on what the session was about, who has contributed, and what is pending.

Follow these steps:

1. **Detect the active session.** Run `git branch --show-current`. If the branch does not start with `session/`, report: "Not on a session branch — no active session to re-read." Then stop.

2. **Locate and read the session document.** The session doc is at `sessions/<id>.md` where `<id>` is everything after `session/` in the branch name. Read it in full.

3. **Summarise back to the human** in this exact structure:

   - **Session:** `<id>` — `<topic from the title>`.
   - **Date opened:** `<date from frontmatter>`.
   - **Participants so far:** `<list from frontmatter>` (if `[]`, say "none recorded yet").
   - **Related nodes:** `<list from frontmatter>` (if `[]`, say "none yet").
   - **Context (as stated when the session opened):** `<first paragraph of the `## Context` section>`.
   - **Most recent log entries (up to 3):** list the last 3 entries from `## Log`, each on its own line, with the date+role tag and a 1-line summary.
   - **Outstanding next steps:** if `## Closing summary` has been started or `## Log` mentions pending items, list them. If nothing pending is recorded, say "none recorded".

4. **Confirm reload.** End the response with: "Context re-loaded. What would you like to do next?"

Do not propose actions or modify any files. This command is read-only — its purpose is to surface context back to the human and to the model.
