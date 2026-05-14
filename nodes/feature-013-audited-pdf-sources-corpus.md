---
category: feature
id: feature-013-audited-pdf-sources-corpus
parent: "[[cap-08-citation-discipline]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 013 — Audited PDF sources corpus (12 documents)

> Authored via `po-feature-decomposition`. Delivers part of [[cap-08-citation-discipline]].

## What it delivers

`bibliography/sources/` holds the 12 audited primary-source PDFs that anchor every authoritative claim across SEM-IA: Capers Jones *Software Engineering Best Practices* (McGraw-Hill 2010); 8 GISF UC3M PDFs (life-cycle, discovery, agile-teams-and-roles, delivery-planning, delivery-backlog-management, delivery-control-and-monitoring, delivery-review-and-retrospectives, pipeline-devops); Cucumber `gherkin-reference.pdf`; Patton `user-story-mapping.pdf`; Comakers/Patton `agile-story-essentials.pdf`.

## Story Map position

- **Activity (Epic):** Bibliographic infrastructure.
- **Task:** This feature (the corpus).
- **Release slice:** Walking skeleton — no citation possible without the corpus.

## Stories (children)

- [[story-013-A-corpus-versioned-with-substrate]] — As a fork author taking SEM-IA to a new project, I want the corpus shipped *with* the substrate, so my forked framework retains its bibliographic anchor without external dependencies.

## Spec sibling

- [[spec-013-audited-pdf-sources-corpus]]

## 5 Cs cycle reminder

Card → Conversation (which sources are tier-1 authority vs convention pointers) → Confirmation (every skill cites at least one corpus PDF) → Construction (PDFs committed to repo) → Consequences (citation latency bounded; no broken links to external libraries).

## Notes

Architectural anchor: [[adr-003-citation-mandate]] + [[adr-004-substrate-content-separation]] (the corpus is substrate, not project content). Cagan books, Sinek, Doerr, etc. are **not** in the corpus — they're convention pointers cited via GISF or as out-of-bibliography disclaimers.

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-003-citation-mandate]], [[adr-004-substrate-content-separation]].
- Substrate evidence: 12 PDF files under `bibliography/sources/`.
