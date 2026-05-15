---
category: feature
id: feature-075-hard-role-jurisdiction
parent: "[[cap-02-role-scoped-agents]]"
artifacts:
  - "[[.claude/commands/role.md]]"
  - "[[.claude/role-scope.json]]"
  - "[[.claude/hooks/enforce-node-before-artifact.sh]]"
  - "[[CLAUDE.md]]"
status: implemented
created: 2026-05-15
updated: 2026-05-15
---

# Feature 075 — Hard role-jurisdiction via mandatory active-role marker

> Authored via `po-feature-decomposition`. **Relates to:** [[feature-007-five-role-agent-identities]], [[adr-005-subagent-dispatch-not-authority-transfer]], [[adr-012-mandatory-active-role-hard-jurisdiction]]. The harness exposes no active-role signal to hooks, so jurisdiction is made hard via an explicit, mandatory marker.

## What it delivers

- `.claude/.active-role` — runtime marker (one role name); **gate-ignored** (always writable; resolves the bootstrap paradox).
- `.claude/commands/role.md` — `/role <name>` ceremony: validates against the 5 roles, writes the marker.
- `.claude/role-scope.json` — declarative `{role: [path-glob,…]}` map; **authoritative** for the gate; CLAUDE.md § Role jurisdiction table mirrors it.
- The gate (shared hook) gains: deny all substrate writes if the marker is absent; deny a write whose path is outside the active role's globs.

## Story Map position

- **Activity:** structural role discipline. **Task:** this feature. **Release slice:** thickening.

## Stories (children)

- `[[story-075-A-declare-active-role]]`
- `[[story-075-B-deny-without-active-role]]`
- `[[story-075-C-deny-wrong-role-for-path]]`
- `[[story-075-D-allow-correct-role]]`

## Spec sibling

- `[[spec-075-hard-role-jurisdiction]]`

## Notes

Residual risk = marker/reality desync (correctness, not bypass) — recorded in [[adr-012-mandatory-active-role-hard-jurisdiction]]. Initial map: `architect` owns governance/structural substrate (`CLAUDE.md`, `.claude/hooks/**`, `.claude/settings.json`, `.claude/agents/**`, `.claude/commands/**`, `.claude/role-scope.json`, `.claude/sem-role-catalog.md`); `po` owns `_obsidian/templates/**`; qa/developer/devops per the table. `bibliography/**` gate-ignored → no entry.

## Source

- Skill: `po-feature-decomposition`. GISF UC3M `gisf-life-cycle.pdf` slide 54 + slide 56. Light `## Source` per template.
