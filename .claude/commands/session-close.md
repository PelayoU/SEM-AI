---
description: Close the current session — multi-role review of the diff, finalize the doc, the human decides merge / PR / discard.
allowed-tools: Bash, Read, Edit, Write, Task
---

Close the current session. Steps, in order.

1. **Confirm an active session.** Run `git branch --show-current`. If it does not start with `session/`, stop and report: "Not on a session branch — nothing to close." Do not proceed.

2. **Locate and read the doc.** Branch `session/<id>` → `sessions/<id>.md`. Read it in full.

3. **Multi-role review of the diff (consultation only).**

   a. Compute the work: `git diff main...HEAD --stat`, then the full `git diff main...HEAD`. Exclude noise (`.obsidian/`, the session doc itself).

   b. Decide which built roles' domains the diff plausibly touches (`.claude/agents/*.md`). Use the framework's *Working as roles* jurisdiction map as the shared definition. When in doubt, include the role.

   c. Dispatch each selected role as a **subagent** (`Task`, `subagent_type` = the agent name) with the diff: *"Reviewing only as <role>: does this diff contain anything that needed your role's decision but was made without it — a structural/methodology change with no ADR, a scope change with no governing node, code with no test/inspection consideration, an operations/config change with no plan? List concrete findings with file references, or state 'no concerns'. Report only — never author."*

   d. Record each role's result as a **Log** entry, third-person and attributed: `### <timestamp> — <Role> (close review)` then `<Role> reviewed the session diff: <findings, or "no concerns">.` Advisory only — nothing is auto-fixed and the close is not blocked.

4. **Finalize the doc.**

   a. Append a final **Log** entry, third-person, for the closing role: what the session achieved.

   b. Rewrite **Handoff** as the closing state: *Outcome* (1–3 sentences); *Pending* — every unresolved review finding as an explicit item; *Merge decision* — `pending — human decides`.

   c. Update frontmatter: `participants:` = every role appearing in the Log; `related-nodes:` = every `[[id]]` touched.

5. **Commit on the session branch:** `git add sessions/<id>.md && git commit -m "close session: <id>"`.

6. **Present the options neutrally and stop. The human decides — do not recommend, do not default, do not pick if they are uncertain. Wait for an explicit choice.**

   - **merge** — `git checkout main && git merge --no-ff session/<id>` (preserves the session boundary). Delete the branch only if the human explicitly says so.
   - **pr** — if `gh` is available: `gh pr create --base main --head session/<id> --title "session: <id>" --body "<Handoff Outcome>"`. Otherwise push the branch and give the manual PR steps.
   - **discard** — abandon the work. Confirm twice (this loses everything on the branch). Then `git checkout main && git branch -D session/<id>`.

7. **After the human chooses,** set Handoff *Merge decision* to the chosen action (`merged to main` / `PR #N` / `discarded: <reason>`), commit it on the appropriate branch, and execute the choice.

8. **Report final state:** the branch you ended on; what happened to the session branch; the doc path as the historical record.
