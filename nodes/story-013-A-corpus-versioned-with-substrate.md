---
category: story
id: story-013-A-corpus-versioned-with-substrate
parent: "[[feature-013-audited-pdf-sources-corpus]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Story 013-A — Bibliographic corpus ships with the substrate

> Parent: [[feature-013-audited-pdf-sources-corpus]].

## Cohn statement

As a **fork author taking SEM-IA to a new project**, I want **the audited PDF corpus shipped *with* the substrate (not as external dependency)**, so that **my forked framework retains its bibliographic anchor without chasing dead links to external libraries**.

## Conditions of Satisfaction

- 12 PDF files present under `bibliography/sources/` in the repo.
- Each PDF is the audited primary-source version (not a summary).

## INVEST self-check

✅ I · ✅ N · ✅ V (offline bibliographic integrity) · ✅ E · ✅ S · ✅ T (`ls bibliography/sources/`).

## Source

- GISF slides 124, 128, 125.
- Parent feature: [[feature-013-audited-pdf-sources-corpus]].
- [[adr-004-substrate-content-separation]].
