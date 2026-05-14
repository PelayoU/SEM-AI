---
category: session
id: <YYYY-MM-DD>-<topic-slug>
date: <YYYY-MM-DD>
participants: []
related-nodes: []
---

# <Session topic>

> A session is a thread of work. It lives on git branch `session/<id>` and ends with `/session-close` (which decides merge / PR / discard). Session state is branch state — if you read this on a `session/*` branch, the session is open; if you read it on `main`, the work is closed and this document is the historical record.
>
> The body is a chronological narrative. Each role contribution is appended in order. No rigid sections, no handoff ceremony — agents know how to work.

## Context

> What prompted this session: a question, a problem, a planning need. One paragraph. Written by the role that opened the session.

## Log

> Chronological log of what happened. Each entry is dated and tagged by the contributing role. Format suggestion (not mandatory):
>
> ```
> ### YYYY-MM-DD HH:MM — <role>
> What was done, what was decided, what artifacts were touched.
> Cite skills applied (`<role>-<skill>`) and nodes affected
> (`[[node-id]]`).
> ```

### <YYYY-MM-DD HH:MM> — <role>

<contribution>

## Artifacts touched

> Running list of nodes created or edited during this session. Populated as work happens; kept current.

- Created `nodes/<path>` — <one-line description>.
- Edited `nodes/<path>` — <what changed>.

## Subagent consultations

> When a role invokes another role via the `Task` tool, log the consultation here (optional but helpful for audit). The consulting role retains scope authority; the consulted role provides information only.

- `<consulting role>` → `<consulted role>` — Question: `<…>`. Response summary: `<…>`.

## Closing summary

> Filled in at `/session-close`. What was accomplished, what is left pending, and the recommended next step.

**Outcome:** <what was achieved>.

**Pending / next steps:** <what is left for a future session>.

**Merge decision:** <merged to main | open PR #N | discarded with reason>.
