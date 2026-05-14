---
category: story
id: story-008-A-new-role-from-template
parent: "[[feature-008-agent-meta-template]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 008-A — Scaffold a new role-agent from meta-template

> Parent: [[feature-008-agent-meta-template]].

## Cohn statement

As a **framework maintainer adding a new role (Security, Designer, or Tier-4 emergent)**, I want **to scaffold the new role-agent by copying `.claude/templates/agent.md.template`**, so that **consistency with the 5 existing roles is structural rather than copy-pasted**.

## Conditions of Satisfaction

- `agent.md.template` exists with all required sections.
- New roles created from it pass the audit grid (Identity, When to invoke, Skills, Workflow, Interaction, Gotchas, Source).

## INVEST self-check

✅ I · ✅ N · ✅ V (extensibility) · ✅ E · ✅ S · ✅ T (instantiate template; check sections present).

## Source

- GISF `gisf-delivery-backlog-management.pdf` slides 124, 128, 125.
- Parent feature: [[feature-008-agent-meta-template]].
