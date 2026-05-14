---
category: story
id: story-001-A-parent-pointer-authoring
parent: "[[feature-001-parent-pointer-convention]]"
artifacts:
  - "[[CLAUDE.md]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 001-A — Parent declared in frontmatter

> Authored via `po-feature-decomposition`. Parent: [[feature-001-parent-pointer-convention]].

## Cohn statement (slide 124)

As a **node author**, I want **every non-root node to declare its parent in frontmatter via `[[wikilink]]`**, so that **the audit chain is automatically navigable without external metadata**.

## Conditions of Satisfaction (slide 125)

- The `parent:` field exists in every node except `vision-sem-ia`.
- The wikilink target resolves to an existing file under `nodes/`.
- Templater (or manual authoring) enforces presence at node-creation time.

## INVEST self-check (slide 128)

✅ I — independent of any sibling story. ✅ N — the convention is negotiable (frontmatter field name could change). ✅ V — the *so that* clause names audit-by-navigation. ✅ E — trivially small to estimate. ✅ S — atomic substrate property. ✅ T — `grep '^parent:' nodes/*.md` plus wikilink-resolution check encodes the test.

## Source

- Cohn format + INVEST + CoS via GISF `gisf-delivery-backlog-management.pdf` slides 124, 128, 125.
- Parent feature: [[feature-001-parent-pointer-convention]].
