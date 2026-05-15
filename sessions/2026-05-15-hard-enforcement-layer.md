---
category: session
id: 2026-05-15-hard-enforcement-layer
date: 2026-05-15
participants: [architect]
related-nodes: []
artifacts: []
---

# Hard-enforcement layer (node-before-artifact + hard role-jurisdiction)

> A session is a thread of work. It lives on git branch `session/<id>` and ends with `/session-close` (which decides merge / PR / discard). Session state is branch state.

## Context

Soft context proved to be **null enforcement**: an agent with the entire `CLAUDE.md` + 5 agents + 37 skills + bootstrap session loaded, having just articulated the node-before-artifact rule in its own words, still edited `CLAUDE.md` (a substrate change) with **no governing node, on a single "do it"**. That out-of-process edit (a 15-line "Orient here" block) is uncommitted in the working tree — the live proof and case study. This session reverts it, then installs a hard PreToolUse gate (node-before-artifact, no override) + mandatory active-role marker (hard role-jurisdiction) + a `UserPromptSubmit` per-turn reinforcement, **through the very discipline it enforces**: session → revert → nodes-first → ADRs → substrate → verify → close. Full design in the approved plan; this work fulfils the `2026-05-14` session's deferred *graph-vs-substrate operating rule* and *consultation matrix* improvement candidates.

## Log

### 2026-05-15 — architect

Opened session `2026-05-15-hard-enforcement-layer` (branch created, this doc instantiated). Confirmed: on a fresh branch off `main`, no other open sessions, `git diff --stat CLAUDE.md` = exactly 1 file / 15 insertions (the out-of-process block, scope verified for the Phase-B revert). Plan approved by the human after extensive design (decisions: no override; hard role-jurisdiction via mandatory `.claude/.active-role`; bibliography out of gate scope; citations conserved; subagent=consultation/`/role`=work; per-turn reinforcement hook). C0 search-before-create already done read-only: `CLAUDE.md` governed by ~30 nodes (relate, don't duplicate); `.claude/settings.json` + legacy `session-start.sh` ungoverned (pre-existing gap, flag only); `.claude/agents/*` governed by feature-007/024/adr-005.

Skills applied: `architect-architecture-design` (enforcement design).
Artifacts: this session doc.
Next: Phase B — revert the out-of-process `CLAUDE.md` edit (`git checkout -- CLAUDE.md`), recorded here, before authoring any node.

### 2026-05-15 — architect (Phase B: revert)

Reverted the out-of-process `CLAUDE.md` edit. Pre-check passed (`git diff --stat CLAUDE.md` = exactly `1 file changed, 15 insertions(+)`), then `git checkout -- CLAUDE.md`; confirmed clean (`git diff --quiet` passes, `grep "Orient here before anything else"` → 0 matches). Rationale: that 15-line block was a substrate change with **no governing node** — the exact node-before-artifact violation this session exists to prevent. It is not lost: its content is re-applied later, node-traced, under `feature-073` (Phase D, §5). The other working-tree noise (`.obsidian/workspace.json` UI state + untracked cruft) is deliberately left untouched (scope discipline).

Skills applied: `architect-architecture-design`.
Artifacts: `CLAUDE.md` (reverted to committed state); this session doc.
Next: Phase C — author governing nodes first (feature-072..076 + stories + specs + adr-011/012), commit all before any substrate change.

## Artifacts touched

- Created `sessions/2026-05-15-hard-enforcement-layer.md` — this session doc.
- Reverted `CLAUDE.md` — discarded the out-of-process 15-line "Orient here" block (no governing node); content re-applied node-traced in Phase D.

## Subagent consultations

> When a role invokes another role via the `Task` tool, log the consultation here (optional but helpful for audit). The consulting role retains scope authority; the consulted role provides information only.

- (none yet)

## Closing summary

> Filled in at `/session-close`. What was accomplished, what is left pending, and the recommended next step.

**Outcome:** <pending>.

**Pending / next steps:** <pending>.

**Merge decision:** <pending>.
