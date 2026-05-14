---
category: feature
id: feature-034-substrate-as-portable-unit
parent: "[[cap-13-portability]]"
status: implemented
created: 2026-05-14
updated: 2026-05-14
---

# Feature 034 — Substrate as a single portable distribution unit

> Authored via `po-feature-decomposition`. Delivers part of [[cap-13-portability]].

## What it delivers

The substrate (`.claude/` + `_obsidian/` + `bibliography/` + `CLAUDE.md` + `LICENSE`) ships as **one cohesive distribution unit** — versioned together, copied together, forked together. No external dependencies beyond the AI harness (Claude Code) and the editor (Obsidian, recommended). The combination of [[feature-032-substrate-content-directory-separation]] + [[feature-008-agent-meta-template]] + [[feature-015-skill-meta-template]] + [[feature-013-audited-pdf-sources-corpus]] makes the substrate self-sufficient as the unit of portability.

## Story Map position

- **Activity (Epic):** Portability substrate.
- **Task:** This feature (substrate as distribution unit).
- **Release slice:** Walking skeleton for goal-03.

## Stories (children)

- [[story-034-A-substrate-self-sufficient]] — As a new-project author taking SEM-IA's substrate, I want everything I need (agents, skills, templates, bibliography, contract) to come together as one unit, so I don't chase external dependencies.

## Spec sibling

- [[spec-034-substrate-as-portable-unit]]

## 5 Cs cycle reminder

Card → Conversation → Confirmation (verifiable by cloning the repo, copying substrate paths to a new repo, instantiating fresh content) → Construction (in force) → Consequences (portability operationally simple).

## Notes

This feature is the *aggregate property* that emerges from the structural separation + meta-templates + bundled bibliography. It is the load-bearing claim of [[adr-004-substrate-content-separation]] and the vision's *"the SEM-IA substrate ships with the code, not separately"*. Goal-03 (portability proof) is the explicit test.

## Source

- Skill: `po-feature-decomposition`.
- ADRs: [[adr-004-substrate-content-separation]].
- Cross-link: [[vision-sem-ia]] Statement.
- Substrate evidence: clone-and-fork operationally tested in the future goal-03 secondary-project work.
