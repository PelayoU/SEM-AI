---
category: story
id: story-016-B-out-of-biblio-flagged
parent: "[[feature-016-claude-md-citation-mandate]]"
artifacts:
  - "[[CLAUDE.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 016-B — Out-of-bibliography references flagged with disclaimer

> Parent: [[feature-016-claude-md-citation-mandate]].

## Cohn statement

As a **skill author considering a framework not in `bibliography/sources/`**, I want **the flagging rule explicit in CLAUDE.md ("named, not borrowed silently")**, so that **I add a disclaimer rather than treat the framework as anchored authority**.

## Conditions of Satisfaction

- CLAUDE.md "Skills convention" section names the out-of-bibliography flagging rule.
- All 37 existing skills flag out-of-bibliography references explicitly.

## INVEST self-check

✅ I · ✅ N · ✅ V (rigour preservation) · ✅ E · ✅ S · ✅ T (`grep "out-of-bibliography" .claude/skills/*/SKILL.md`).

## Source

- GISF slides 124, 128, 125.
- Parent feature: [[feature-016-claude-md-citation-mandate]].
- [[adr-003-citation-mandate]] (corollary: out-of-bibliography flagging).
