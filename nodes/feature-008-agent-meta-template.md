---
category: feature
id: feature-008-agent-meta-template
parent: "[[cap-02-role-scoped-agents]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 008 — Agent meta-template for creating new role-agents

> Authored via `po-feature-decomposition`. Delivers part of [[cap-02-role-scoped-agents]]; also serves [[cap-13-portability]] as the extensibility mechanism for new role coverage.

## What it delivers

`.claude/templates/agent.md.template` encodes the canonical structure every role-agent must follow: frontmatter (`name`, `description`, `model`, `color`), required body sections (Identity, When to invoke, Skills table, Workflow, Interaction with other roles, Gotchas, Source). New roles (Security, Designer when implemented; future Tier-3 emergence cases) scaffold from this template.

## Story Map position

- **Activity (Epic):** Role substrate extensibility.
- **Task:** This feature (meta-template).
- **Release slice:** Thickening release — only relevant when adding new roles.

## Stories (children)

- [[story-008-A-new-role-from-template]] — As a framework maintainer, I want to scaffold a new role-agent by copying the meta-template, so consistency with the 5 existing roles is structural rather than copy-pasted.

## Spec sibling

- [[spec-008-agent-meta-template]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (spec encodes the required sections) → Construction (template extracted from observed structure of existing 5 agents) → Consequences (extensions are conformant by design).

## Notes

Cross-cap usage: [[cap-13-portability]] depends on this template for "substrate-as-portable-unit" (a new project lifting SEM-IA's substrate can extend the role catalog without reverse-engineering). Architectural anchors: [[adr-008-markdown-frontmatter-data-format]], [[adr-009-skill-as-canonical-method]] (skills table is mandatory in every agent).

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-008-markdown-frontmatter-data-format]], [[adr-009-skill-as-canonical-method]].
- Substrate evidence: `.claude/templates/agent.md.template`.
