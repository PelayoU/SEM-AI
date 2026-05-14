---
category: capability
id: cap-13-portability
parent: "[[goal-03-portability-proof]]"
status: draft
mvp: go
created: 2026-05-14
updated: 2026-05-14
---

# Capability 13 — Portability to projects other than SEM-IA

> Authored via `po-capabilities`. Canonical definition: GISF `gisf-life-cycle.pdf` slide 54. MVP filter: slide 69. Cagan four risks: slide 64.

## Statement (slides 97–99 form)

In order to **let SEM-IA's substrate operate on projects other than itself, without project-specific assumptions baked in** (parent goal [[goal-03-portability-proof]] — concierge-tested with a second project authored by pelayo; full external-author test in the next roadmap),
as **anyone running a software engineering effort that is not SEM-IA itself**,
I want **the ability to lift the SEM-IA substrate (universal contract, role agents, skills, templates, bibliography, meta-templates for extending) into a new project and have it work, with the new project's content (its own vision, goals, capabilities, etc.) populating the graph as a separate layer from the reusable substrate**.

## Implementation-agnostic test

- **Implementation A** (current, planned exercise for G3): fork-and-adapt — the new project copies the `.claude/`, `_obsidian/`, `bibliography/`, `CLAUDE.md`, `LICENSE` from SEM-IA's repo and starts a fresh `nodes/` graph; substrate stays identical, content is project-specific.
- **Implementation B** (alternative): substrate as installable package (`pip install sem-ia` or npm equivalent); project instantiation via a `sem-ia init` command that scaffolds the directories.

A third plausible: cookiecutter-style template generator producing a SEM-IA-scaffold for any new repo. The capability is *substrate reusability across projects*, not the lifting mechanism.

## MVP Go / No-go

- **Value risk:** Without this capability, SEM-IA is *"this project's framework"*, not infrastructure. The entire AI-as-infrastructure paradigm depends on portability being real.
- **Usability risk:** Moderate-to-high — the new-project author must understand the substrate/content distinction and not modify the substrate when they mean to modify content. The deferred *graph-vs-substrate operating rule* improvement candidate addresses this discipline structurally.
- **Viability risk:** **Highest of any capability in the current set.** Currently untested at the *use* level. The structural separation is there (substrate in `.claude/` + `_obsidian/` + `bibliography/` + `CLAUDE.md`; content in `nodes/` + `sessions/`), but real-world portability is the G3 measurement. **G3's ⚠️ on Achievability traces here.**
- **Business viability risk:** N/A.

**Decision: Go** — G3 demands it. The viability risk is the goal's risk; mitigating it is the goal's work.

## Non-overlap with sibling capabilities

- This capability is sibling-less under its parent goal — G3 has only this one capability because G3's success *is* exactly this property being demonstrated. The five role-discipline capabilities ([[cap-03-apply-po-discipline]] through [[cap-07-apply-devops-discipline]]) plus the other meta-capabilities are exercised within the second project to evidence portability, but they are owned by G1 and G2.
- Cross-goal sibling: [[cap-01-vision-to-code-audit]] (G1) — adjacent. cap-01 is *the property exercised within a project*; this capability is *the property of the substrate across projects*.

## Non-coverage

- **Not about harness portability.** Whether the substrate runs on Claude Code only, or also on Cursor / Aider / etc., is a separate (future) capability. Current scope: same harness, different project.
- **Not about scale portability.** Whether SEM-IA works at 100k FP vs 100 FP is a separate concern (tier-based catalog already addresses scale architecturally).
- **Not about domain portability.** Whether SEM-IA works for fintech / medical / gaming is a separate concern (currently the substrate is domain-agnostic by design but unproven cross-domain).
- **Not about external-author portability.** A different human as author is the *next* roadmap's concierge test, not this one (this G3 is same-author / different-project; the explicit non-goal in G3).

## Source

- Skill: `po-capabilities`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54, slide 69; `gisf-discovery.pdf` slides 97–99.
- Cagan four risks: `gisf-life-cycle.pdf` slide 64.
- Features delivering this capability: the substrate/content separation enforced by CLAUDE.md repo structure; `.claude/templates/agent.md.template` + `.claude/templates/SKILL.md.template` (allow extending the substrate to new contexts); `LICENSE` (permits forks).
- Cross-link to [[vision-sem-ia]] Statement *"anyone running a software engineering effort — from a solo builder to a large enterprise"* — the word *anyone* presupposes portability.
- "Concierge testing" framing flagged as out-of-bibliography (Eric Ries / Lean Startup) in the parent goal's `## Source`.
