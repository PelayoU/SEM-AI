---
category: story
id: story-028-A-adr-cross-cut-rule-loaded
parent: "[[feature-028-claude-md-adr-cross-cut-rule]]"
artifacts:
  - "[[CLAUDE.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 028-A — ADR cross-cut rule loaded from CLAUDE.md

> Parent: [[feature-028-claude-md-adr-cross-cut-rule]].

## Cohn statement

As an **Architect choosing where to parent an ADR**, I want **the "ADRs can hang from any backbone node" rule loaded at session start**, so that **I attach to the highest applicable backbone level rather than forcing a hierarchical fit**.

## Conditions of Satisfaction

- CLAUDE.md `## The graph` section names the rule.
- Phase-1 ADRs are parented to vision / goal / cap levels (a mix, none forced under a feature).

## INVEST self-check

✅ I · ✅ N · ✅ V (correct ADR altitude) · ✅ E · ✅ S · ✅ T (audit Phase-1 ADR parents).

## Source

- GISF slides 124, 128, 125.
- Parent feature: [[feature-028-claude-md-adr-cross-cut-rule]].
- [[adr-002-backbone-hierarchy-parent-edges]].
