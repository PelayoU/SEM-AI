---
category: feature
id: feature-009-role-catalog-design-doc
parent: "[[cap-02-role-scoped-agents]]"
artifacts:
  - "[[.claude/sem-role-catalog.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 009 — Role catalog design document (`sem-role-catalog.md`)

> Authored via `po-feature-decomposition`. Delivers part of [[cap-02-role-scoped-agents]].

## What it delivers

`.claude/sem-role-catalog.md` is the design document that defines the role catalog: the 5 core roles, the Tier-3 specialized roles (Security, Designer — planned), the Tier-4 emergence cases (separate BA and PM activation conditions), and the BP↔skill mapping for every Capers Jones Best Practice operationalized in SEM-IA. Source of truth for `.claude/agents/<role>.md` identities and `.claude/skills/<role>-<skill>/SKILL.md` specifications.

## Story Map position

- **Activity (Epic):** Role substrate governance.
- **Task:** This feature (role catalog).
- **Release slice:** Walking skeleton — design doc upstream of every role-agent file.

## Stories (children)

- [[story-009-A-role-catalog-source-of-truth]] — As a framework maintainer, I want a single design document defining the role catalog, so additions or changes to roles are anchored to one auditable source.

## Spec sibling

- [[spec-009-role-catalog-design-doc]]

## 5 Cs cycle reminder

Card → Conversation (the multi-session debate that produced the 5 core + Tier-3 + Tier-4 structure) → Confirmation (BP-to-skill mapping cross-checks against Jones's 50 BPs) → Construction (file exists) → Consequences (every role-agent ultimately traces back here).

## Notes

Architectural anchor: [[adr-006-super-po-fusion]] (super-PO at Tier-1; Tier-4 split documented as emergence). Tier-3 roles (Security, Designer) tracked here as "planned, not yet implemented" — see [[cap-02-role-scoped-agents]] *non-coverage* and the deferred capabilities 15 and 16 captured in session log.

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-006-super-po-fusion]].
- Substrate evidence: `.claude/sem-role-catalog.md`.
- Bibliography anchors: Capers Jones (2010) Ch 5 (specialist taxonomy), Ch 5 Table 5-1, Ch 5 § SQA Organizations; Cagan *Empowered* (super-PO model via GISF).
