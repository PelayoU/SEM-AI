---
category: session
id: 2026-05-15-hard-enforcement-layer
date: 2026-05-15
participants: [architect, product-owner]
related-nodes:
  - "[[feature-072-node-before-artifact-gate]]"
  - "[[feature-073-claude-md-orientation-and-governance]]"
  - "[[feature-074-agent-decision-verification]]"
  - "[[feature-075-hard-role-jurisdiction]]"
  - "[[feature-076-per-turn-role-reinforcement]]"
  - "[[adr-011-hard-enforcement-no-human-override]]"
  - "[[adr-012-mandatory-active-role-hard-jurisdiction]]"
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

### 2026-05-15 — product-owner + architect (Phase C: nodes first)

Authored **26 governing nodes**, parents before children, all `draft`/`proposed`, light `## Source` per template (no skill-grade citation apparatus — citation guard honoured). PO authored the 5 features + 14 stories + 5 specs (`po-feature-decomposition`, `po-spec-gherkin`); Architect authored adr-011/adr-012 (`architect-architecture-design`) — logged as cross-role co-authoring within the session, not a Task subagent dispatch. C0 search-before-create applied: relate-not-duplicate to feature-007/010/024/025/028, adr-004/005/010; this work delivers the `2026-05-14` deferred *graph-vs-substrate operating rule* (→ feature-073) and *consultation matrix* (→ feature-074) candidates; pre-existing ungoverned `.claude/settings.json` closed by feature-072/076; legacy `session-start.sh` gap flagged, not retro-fixed. Parent-chain sanity: 26/26 present, all parents resolve. **No substrate touched yet.**

Skills applied: `po-feature-decomposition`, `po-spec-gherkin`, `architect-architecture-design`.
Artifacts: 26 nodes under `nodes/` (feature/story/spec-072..076, adr-011, adr-012); this session doc.
Next: Phase D — implement substrate in deadlock-safe order, each path already governed by these nodes.

## Artifacts touched

- Created `sessions/2026-05-15-hard-enforcement-layer.md` — this session doc.
- Reverted `CLAUDE.md` — discarded the out-of-process 15-line "Orient here" block (no governing node); content re-applied node-traced in Phase D.
- Created 26 nodes — `feature-072..076`, their `story-*` (14) and `spec-072..076`, `adr-011`, `adr-012` — the governing graph for the hard-enforcement substrate.

## Subagent consultations

> When a role invokes another role via the `Task` tool, log the consultation here (optional but helpful for audit). The consulting role retains scope authority; the consulted role provides information only.

- (none yet)

## Closing summary

> Filled in at `/session-close`. What was accomplished, what is left pending, and the recommended next step.

**Outcome:** <pending>.

**Pending / next steps:** <pending>.

**Merge decision:** <pending>.
