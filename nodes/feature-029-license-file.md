---
category: feature
id: feature-029-license-file
parent: "[[cap-12-public-publication]]"
artifacts:
  - "[[LICENSE]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 029 — `LICENSE` file at repo root

> Authored via `po-feature-decomposition`. Delivers part of [[cap-12-public-publication]]; also serves [[cap-13-portability]] (permits forks).

## What it delivers

`LICENSE` at the repo root declares the terms under which the SEM-IA substrate is published. The presence of the file is a precondition for [[cap-12-public-publication]] — public repositories without a license fall under default copyright (no reuse rights). The specific license choice is currently a placeholder pending PO decision (flagged by Architect in Phase 1 concerns); the structural slot exists.

## Story Map position

- **Activity (Epic):** Publication substrate.
- **Task:** This feature (LICENSE file).
- **Release slice:** Walking skeleton — required by goal-02 publication step.

## Stories (children)

- [[story-029-A-license-at-repo-root]] — As an external reader cloning the repo, I want a LICENSE file at the root, so I know what reuse rights I have without contacting the author.

## Spec sibling

- [[spec-029-license-file]]

## 5 Cs cycle reminder

Card → Conversation (license choice pending PO decision) → Confirmation (file exists) → Construction → Consequences (legally publishable; permits forks per [[cap-13-portability]]).

## Notes

Architect flagged in Phase 1: "No ADR for LICENSE choice. When PO picks a license, capture as ADR." Currently a placeholder slot; the substantive license selection is a deferred PO decision (improvement candidate). Cross-cap serving: [[cap-13-portability]] depends on the license permitting forks.

## Source

- Skill: `po-feature-decomposition`.
- Substrate evidence: `LICENSE` file at repo root.
- Convention pointer: SPDX license identifiers, OSI-approved licenses (out-of-bibliography).
