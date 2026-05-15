---
category: feature
id: feature-073-claude-md-orientation-and-governance
parent: "[[cap-01-vision-to-code-audit]]"
artifacts:
  - "[[CLAUDE.md]]"
status: implemented
created: 2026-05-15
updated: 2026-05-15
---

# Feature 073 — CLAUDE.md orientation + governance contract

> Authored via `po-feature-decomposition`. **Relates to, does not duplicate:** [[feature-010-claude-md-role-scope-section]], [[feature-025-claude-md-subagent-rule]], [[feature-028-claude-md-adr-cross-cut-rule]], [[adr-004-substrate-content-separation]], [[adr-005-subagent-dispatch-not-authority-transfer]], [[adr-010-human-directed-ai-maintained]]. Delivers the `2026-05-14` session's deferred *graph-vs-substrate operating rule* improvement candidate. `CLAUDE.md` is already governed by ~30 nodes; this is the home for *this* change only.

## What it delivers

Hoists to the top of `CLAUDE.md`, and adds: (1) an `## Orient here before anything else` block (substrate IS the framework; `nodes/`+`sessions/` are the traceability layer) — the node-traced re-application of the reverted out-of-process edit; (2) a `## Role jurisdiction` table for the 5 roles, mirroring `.claude/role-scope.json`; (3) a graph-vs-substrate operating principle; (4) a decision-verification operating principle; (5) the node-before-artifact + active-role hard rule, naming the enforcing hook, non-overridable.

## Story Map position

- **Activity:** make the contract self-sufficient and enforced at read time.
- **Task:** this feature. **Release slice:** walking skeleton.

## Stories (children)

- `[[story-073-A-fresh-session-orientation]]`
- `[[story-073-B-role-jurisdiction-table]]`
- `[[story-073-C-decision-verification-principle]]`

## Spec sibling

- `[[spec-073-claude-md-orientation-and-governance]]`

## Notes

The orient content equals the reverted block (Phase B) restored verbatim-equivalent + one sentence that substrate changes are hard-gated. The § Session-bootstrap "no command/hook exists" pre-existing drift is **out of scope** — flag, do not fix.

## Source

- Skill: `po-feature-decomposition`. GISF UC3M `gisf-life-cycle.pdf` slide 54 + slide 56. Governance node — light `## Source`.
