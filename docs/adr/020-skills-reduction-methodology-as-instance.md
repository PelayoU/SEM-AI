---
type: adr
parent: vision-001-sem-ai
status: accepted
created: 2026-05-22
updated: 2026-05-22
maintained_by_role: architect
supersedes:
  - adr-009-skill-as-canonical-method
---

# ADR 020 — Reduce skills · methodology lives in the instance

## Context & forces

v0.1 carried 41+ Claude Code skills (`.claude/skills/<role>-<topic>/SKILL.md`), each absorbing one methodology page (Cagan vision principles, Jones BP #14 risk categories, Fagan 5 preconditions, etc.). Each agent.md preloaded its role's 5-7 skills.

Two problems crystallised in the v0.2 reframe:

- **Token economy**. Loading 5-7 skills × ~250 lines × 6 roles = ~7 500 lines of methodology context at every session start, of which the agent uses ~5% in a typical interaction. The cost compounded as the framework matured.
- **Methodology lock-in**. Skills were authored against Cagan + Jones + Fagan + Cohn / Patton + Humble & Farley + Nygard. A product using a different methodology (SAFe, Modern Agile, custom) would have to fork the entire skill tree to adopt the framework — exactly the lock-in ADR 017 (engine/instance split) was designed to dissolve.

The user named the conflation directly: *"el framework en sí, la visión. no son las skills ni tampoco lo que contiene el agent.md de cada uno. es decir, a lo mejor hay gente que tiene prácticas distintas a Jones o lo que sea. el framework real es cómo trabajar con la IA para crear productos de software."*

## Decision

**Drastically reduce skills. Absorb the generic role discipline into agent.md; move methodology specifics to `instance/methodology/*.md`.**

- `.claude/skills/` keeps **only** the `framework` skill (the contract every agent preloads). All `<role>-<topic>` skill directories are removed from `main` (preserved on the `archive/v0.1-sqlite-experiment` branch).
- Each `.claude/agents/<role>.md` (Day 1.9) absorbs its role's *generic role discipline* — a `## Discipline` mega-section with one sub-discipline per former skill, each with generic criteria + pitfalls + a forward pointer like `→ Methodology: instance/methodology/fp-sizing.md`.
- `instance/methodology/*.md` carries the citation-rich playbooks (Method, Generic criteria recap, Bibliographic anchors, Worked example, Common pitfalls). **Not** preloaded into agent context — read on-demand when the agent needs deeper material than what is in agent.md.

## Overall structure

Two-layer documentation: agent.md (always loaded) + instance/methodology/ (loaded on demand).

## Data structure

agent.md body has 6 mandatory sections: Identity / Jurisdiction / Discipline / Workflow / Interaction with other roles / Gotchas. The `## Discipline` section has 5-15 sub-disciplines per role (PM has 15; Architect / Developer / QA / Security Officer have 5 each; DevOps has 7).

Each instance/methodology/*.md file has YAML frontmatter (title, anchor, referenced_by, status) + 5 sections (Method, Generic criteria recap, Bibliographic anchors, Worked example, Common pitfalls).

## Interfaces to the outside world

Agents read `.claude/agents/<role>.md` at session start. They read `instance/methodology/<file>.md` via the Read tool when a sub-discipline's `→ Methodology` pointer is followed.

## Decomposition into functional components

15 PM sub-disciplines · 5 Architect · 5 Developer · 5 QA · 7 DevOps · 5 Security Officer = 42 sub-disciplines → 42 forward references → ~42 methodology playbooks. Two ship in this commit (`fp-sizing.md` + `fagan-inspections.md`); the rest TODO with row in `instance/methodology/README.md`.

## Linkage / information transmission

agent.md references playbooks by relative path. Playbooks reference back via the `referenced_by:` frontmatter (audit trail: which agent.md section depends on this playbook).

## Performance attributes

Token economy: agent.md is now 140-280 lines per role (PM 283 / Architect 140 / Developer 148 / QA 148 / DevOps 175 / Security Officer 152) = ~1 050 lines, replacing the v0.1 ~7 500 of preloaded skills. ~7× context reduction per session start.

## Security attributes

Dispatched to Security Officer.

- Methodology playbooks are reference docs, not executed code; no security surface.
- Security-officer.md absorbs `security-officer-security-program/architecture/testing-and-static-analysis/threats-and-defenses/requirements-and-inspection` skills via the same sub-discipline pattern.
- The Security gate of a release is **dispatched-authored** (PM owns the release node; Security Officer authors the gate section), preserving the section-contribution discipline.

## Style: chosen + rejected

- **Chosen**: agent.md absorption + on-demand methodology playbooks.
- **Rejected**: keep skills, optimise context (e.g., lazy load). Symptom-fix: still locks the framework to one methodology school.
- **Rejected**: empty agent.md + methodology preload. Loses the "discipline criteria visible at every session" property.
- **Rejected**: full skill removal (no playbooks). Loses the citation pack — methodology becomes folklore.

## Consequences

- Agent context drops ~7× per session start.
- A product using a different methodology adopts the framework by replacing `instance/` only.
- The bibliography (`bibliography/skill-references.md` from v0.1) is preserved in main as historical record; the citations migrate into the methodology playbooks as they are authored.
- Loss: each agent.md is longer (140-280 lines vs the previous ~70). Acceptable — it is the *source of truth* for the role now. Section headers (`## Identity / ## Jurisdiction / ## Discipline / ## Workflow / ## Interaction / ## Gotchas`) keep it scannable.

## Design inspection

Verification test on Day 3.8: dispatch `claude --agent qa` to record a DRE measurement. The agent must call `mcp__sem_ai_engine__create_node(type="measurement", ...)`, not improvise a markdown report. If it improvises, agent.md § Discipline / 2. Measurements is insufficient and gets tightened. Mechanical evidence that the reduction did not lose the discipline.
