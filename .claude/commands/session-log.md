---
description: Append a Log entry to the current session doc. Use at every Log entry trigger — significant decision, artifact created, subagent consultation, or before stepping away / handing off to another role.
argument-hint: [optional one-line note]
allowed-tools: Bash, Read, Edit
---

Append a Log entry to the current session document.

Follow these steps in order:

1. **Confirm there is an active session.** Run `git branch --show-current`. If the branch does not start with `session/`, stop and report: "Not on a session branch — no session to log to." Do not proceed.

2. **Extract the session id and locate the doc.** Branch `session/<id>` → doc `sessions/<id>.md`. Read it in full so you have current state.

3. **Capture the moment.** Run `date +"%Y-%m-%d %H:%M"` for the timestamp. The role tag is the role currently active in this conversation (the role assumed at bootstrap or via `claude --agent <role>`).

4. **Compose the entry body.**

   - **If `$ARGUMENTS` is provided** — use it as the narrative verbatim, but still add the structured tail (skills / artifacts / next) if you can infer them from recent activity.
   - **If `$ARGUMENTS` is empty** — draft a 1–2 paragraph narrative summarising what has happened since the previous Log entry: decisions made, artifacts created or modified, subagent consultations performed. Cite skills applied as `<role>-<skill>`. Cite nodes touched as `[[node-id]]`. If this is a handoff, end with an explicit pointer to what the next role should pick up.

5. **Append to the `## Log` section** using exactly this format:

   ```
   ### <timestamp> — <role>

   <narrative>
   Skills applied: `<role>-<skill>`, ...
   Artifacts: [[node-id]], ...
   Next: <pending pointer, or "—">.
   ```

   Insert at the end of `## Log`, before the next `##` header. Preserve any prior entries.

6. **Update `## Artifacts touched`** if new nodes were created or modified — append bullets in the form `- Created `nodes/<path>` — <one-line description>.` or `- Edited `nodes/<path>` — <what changed>.`. Do not duplicate existing entries.

7. **Update frontmatter `participants:`** to include the current role if not already present. Update frontmatter `related-nodes:` to include any new nodes touched.

8. **Do NOT commit.** Logging is not a commit moment — the human commits when natural, and `/session-close` will commit the final state on close. Leave the working tree dirty.

9. **Report back** to the human:
   - The session doc path.
   - A one-line summary of what was appended.
   - A reminder that the entry is uncommitted.

If the human is invoking this command at a role-handoff moment, make the `Next:` line explicit and concrete — that line is what the incoming role will read first.
