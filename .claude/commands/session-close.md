---
description: Close the current SEM-IA session — finalize the document and decide merge / PR / discard.
allowed-tools: Bash, Read, Edit, Write
---

Close the current SEM-IA session.

Follow these steps in order:

1. **Confirm there is an active session.** Run `git branch --show-current`. If the branch does not start with `session/`, stop and report: "Not on a session branch — nothing to close." Do not proceed.

2. **Extract the session id and locate the session doc.** The branch name is `session/<id>`. The session doc is at `sessions/<id>.md`. Read it in full.

3. **Update the session document with the closing state.** Edit `sessions/<id>.md` to:

   a. **Append a final log entry** under `## Log` summarising the role-contribution that is happening now (the role closing the session). Use the date+time + role format the template suggests.

   b. **Update `participants:`** in frontmatter to reflect every role that has contributed during the session (read the `## Log` to compile the list).

   c. **Update `related-nodes:`** in frontmatter to reflect every node created or edited during the session (check the `## Artifacts touched` section + any `[[wikilinks]]` mentioned in `## Log`).

   d. **Fill the `## Closing summary` section:**
      - **Outcome:** what was accomplished in this session (1–3 sentences).
      - **Pending / next steps:** what is left for a future session, if anything.
      - **Merge decision:** to be filled in step 5 below. For now, leave as `<pending>`.

4. **Commit the updated session doc on the session branch:**
   ```
   git add sessions/<id>.md
   git commit -m "close session: <id>"
   ```

5. **Ask the human for the merge decision.** Present three options clearly:

   - **`merge`** — fold the session work into `main`. Use `git checkout main && git merge --no-ff session/<id>` (no-fast-forward preserves the session boundary in history). Optionally `git branch -d session/<id>` after, if the human confirms.
   - **`pr`** — open a pull request for review. If `gh` CLI is available, run `gh pr create --base main --head session/<id> --title "session: <id>" --body "<closing summary>"`. If `gh` is not available, push the branch and provide the manual PR creation steps.
   - **`discard`** — abandon the session work. Confirm twice with the human (this loses everything on the session branch). Then `git checkout main && git branch -D session/<id>`.

6. **After the human chooses, update the `## Closing summary` `Merge decision:` field** with the chosen action (e.g., `merged to main`, `PR #42 opened`, `discarded: <reason>`), commit that change on whichever branch is appropriate, and execute the chosen action.

7. **Report final state** to the human:
   - The branch you ended on.
   - What happened to the session branch (merged + deleted? merged + kept? PR open? deleted without merge?).
   - The path to the session doc as the historical record.

If at any point the human seems uncertain about merge vs PR vs discard, default to `merge` for solo workflows or `pr` for collaborative workflows — but ask first, do not assume.
