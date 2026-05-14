---
description: Open a new SEM-IA session — creates a git branch and the session document.
argument-hint: <topic-slug>
allowed-tools: Bash, Read, Write
---

Open a new SEM-IA session.

**Topic slug provided:** `$ARGUMENTS`

Follow these steps in order:

1. **Validate the slug.** If `$ARGUMENTS` is empty, ask the human for a topic slug and stop until they answer. The slug should be kebab-case (lowercase, hyphens). If the human gives spaces, normalize them to hyphens; if they give camelCase, accept as-is.

2. **Compute the session id.** Run `date +%Y-%m-%d` via Bash to get today's date. The session id is `<today>-<slug>`. For example, if today is 2026-05-14 and slug is `vision-draft`, the id is `2026-05-14-vision-draft`.

3. **Check current branch state.** Run `git branch --show-current`. If you are already on a `session/*` branch, warn the human: nested sessions are unusual and may indicate the previous session should be closed first. Ask them to confirm before continuing. If on `main` (or any non-session branch), proceed.

4. **Create and switch to the session branch:**
   ```
   git checkout -b "session/<id>"
   ```
   Verify the branch was created and you're now on it.

5. **Create the session document.** Read `_obsidian/templates/session.md` to get the structure. Write `sessions/<id>.md` with placeholders filled:
   - Frontmatter `id:` → the computed id.
   - Frontmatter `date:` → today's date.
   - Frontmatter `participants:` → leave as `[]` (it populates as roles contribute).
   - Frontmatter `related-nodes:` → leave as `[]`.
   - The title line `# <Session topic>` → derive a human-readable title from the slug (replace hyphens with spaces, capitalize first letter). E.g., `vision-draft` → "Vision draft".
   - Keep the `## Context`, `## Log`, `## Artifacts touched`, `## Subagent consultations`, `## Closing summary` sections as the template defines them, with their placeholder comments intact (the role contributing now or later will fill them).

6. **Commit the initial session doc on the new branch:**
   ```
   git add sessions/<id>.md
   git commit -m "open session: <id>"
   ```

7. **Report back to the human.** Confirm:
   - The branch you are now on (`session/<id>`).
   - The session document path (`sessions/<id>.md`).
   - Remind them that the role they are currently working as should begin by filling the `## Context` section of the session doc, then proceed with the actual work.

Do not attempt to fill the `## Context` yourself unless the human asks — the human (and the role currently active) author that section.
