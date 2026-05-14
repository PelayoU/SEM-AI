---
category: spec
id: spec-034-substrate-as-portable-unit
parent: "[[feature-034-substrate-as-portable-unit]]"
artifacts:
  # No concrete substrate — this node describes an abstract property
  # without a single artefact owner. See CLAUDE.md § Substrate traceability.
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Spec 034 — Substrate as portable unit

> Parent: [[feature-034-substrate-as-portable-unit]].

## Stories covered

- [[story-034-A-substrate-self-sufficient]] — AC-A1

## Acceptance Criteria

- **AC-A1:** The substrate (`.claude/` + `_obsidian/` + `bibliography/` + `CLAUDE.md` + `LICENSE`) is self-sufficient: no skill / agent / template references an external resource not shipped in the substrate.

## Gherkin spec

```gherkin
Feature: Substrate as a portable unit

  Scenario: AC-A1 — No skill / agent references unshipped resource
    Given all SKILL.md and agent.md files
    When I extract their citations / source references
    Then every cited file is either in the substrate paths or explicitly flagged as out-of-bibliography convention
```

## Source

Cucumber `gherkin-reference.pdf` pp. 1–9. Parent: [[feature-034-substrate-as-portable-unit]].
