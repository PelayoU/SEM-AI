---
category: feature
id: feature-011-bibliography-index
parent: "[[cap-08-citation-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 011 — Bibliography INDEX as navigable map of audited sources

> Authored via `po-feature-decomposition`. Delivers part of [[cap-08-citation-discipline]].

## What it delivers

`bibliography/INDEX.md` is the navigable map of audited primary sources. Per-PDF tables (slide-by-slide for GISF; page-by-page for Jones; section-by-section for Cucumber) let a skill author locate the exact citation point without re-reading the source. Designed for the framework's *constructor* (skill author / human PO), not for the agent at runtime — skills are self-contained per [[cap-08-citation-discipline]]'s separation.

## Story Map position

- **Activity (Epic):** Bibliographic infrastructure.
- **Task:** This feature (INDEX as navigator).
- **Release slice:** Walking skeleton — required before any skill can claim citation discipline.

## Stories (children)

- [[story-011-A-locate-citation-via-index]] — As a skill author, I want to find the exact slide/page that anchors a specific concept, so I cite primary source verbatim without scanning the whole PDF.

## Spec sibling

- [[spec-011-bibliography-index]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (every skill's `## Source` cites entries traceable to INDEX) → Construction (`bibliography/INDEX.md`) → Consequences (citation latency near zero for the constructor).

## Notes

Architectural anchor: [[adr-003-citation-mandate]] (the rule); this feature is the *tooling* that makes the rule operationally cheap. Companion to [[feature-012-skill-references-traceability]] (per-skill traceability) and [[feature-013-audited-pdf-sources-corpus]] (the PDFs themselves).

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-003-citation-mandate]].
- Substrate evidence: `bibliography/INDEX.md`.
