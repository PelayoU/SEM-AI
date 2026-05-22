---
type: goal
parent: vision-001-sem-ai
status: draft
created: 2026-05-14
updated: 2026-05-22
maintained_by_role: product-manager
labels:
  - horizon:release
---

# Goal 03 — Portability proof (second-project, same author)

> Authored via `po-goals`. Canonical criteria: SMART (GISF `gisf-discovery.pdf` slide 95) + multilevel planning horizons (GISF `gisf-delivery-planning.pdf` slide 150) + why-stack discipline (slide 96) + slide 95 stakeholder form. Goal definition: GISF `gisf-life-cycle.pdf` slide 54.

## Statement (slide 95 form)

In order to **validate that SEM-IA is portable beyond its own bootstrap**,
as **the SEM-IA author acting as my own first user on a different project**,
I want **capabilities that let me apply SEM-IA end-to-end on a non-SEM-IA project of mine and produce a comparative report against prior similar work without the framework, including defect-prevention evidence**.

## Horizon (slide 150)

**Release** (2–9 months). Target completion: **November 2026** (~6 months from session opening 2026-05-14; ~4 months after the [[goal-02-tfm-public-artifact]] anchor). Concierge-testing pattern: same-author / different-project is the strongest validation achievable without the additional uncertainty of a third-party user. A different-author case study belongs to the next roadmap (post-November 2026).

## Why-stack trace (slide 96)

- Why this goal? → To prove that SEM-IA works on a project other than itself — that the framework is genuinely *project-agnostic*, not implicitly fitted to SEM-IA.
- Why prove project-agnosticism? → Because the parent vision claims SEM-IA is **infrastructure**. Infrastructure is by definition multi-project; a framework that only works on its own bootstrap is a thought experiment, not infrastructure.
- Why does that matter? → Because without portability evidence, the entire vision is unfalsifiable in practice — the "anyone running a software engineering effort" claim collapses. And without a defect-prevention comparison, the vision's central promise (absorb the AI-specific cost: review burden, hallucination, scope drift, context loss) remains untested.
- Lands on **[[vision-sem-ia]]** → *Statement* (infrastructure claim) + *Principle 2 (love the problem — AI-specific cost)* + *Principle 9 (act of faith requires evidence)* + *Positioning statement* (target = anyone, any project). ✅

## SMART self-check (slide 95, attributed to Doran 1981)

- **S — Specific:** ✅ — Scope = exactly 1 non-SEM-IA project authored by pelayo, modelled as a SEM-IA graph and executed end-to-end. Comparative report against a chosen baseline (a similar prior project without SEM-IA). Project to be **named explicitly in a sub-decision (ADR or backlog spec) before work begins** — without naming, the goal is unfalsifiable.
- **M — Measurable:** ✅ — Checklist:
  - 1 non-SEM-IA project chosen, named, scope-declared in a node (`adr` or `spec` under this goal).
  - That project has its own SEM-IA-style graph: ≥ 1 vision + ≥ 1 goal + ≥ 1 capability + ≥ 1 feature + ≥ 1 story + ≥ 1 spec → code.
  - ≥ 4 roles contributed to the secondary project's graph (minimum PO + Architect + Developer + QA; DevOps if the project ships).
  - Comparative report exists, addressing each axis the parent vision names as a promise of the substrate. Metric design per axis is QA-scope at execution time (cross-link `qa-measurements`); PO's responsibility here is only to declare the axes as non-negotiable:
    - **Review burden** — does the framework reduce the human effort spent reviewing AI output, vs the baseline of working on a similar prior project without SEM-IA?
    - **Hallucination** — does the framework prevent or surface AI hallucinations that would otherwise have reached the artifact?
    - **Scope drift** — does the framework prevent or surface scope drift before it lands in committed work?
    - **Context loss** — does the framework eliminate re-explanation of prior project context to contributors (human or AI) joining or returning to the work?
    - **Deployment-readiness / maintainability** — does the secondary project produce an artifact that ships and is maintainable, not only code that runs? (This axis materialises the vision's *"programming and product-building diverge at deployment"* claim.)
  - Decision-traceability: every significant project decision traces back to a node in the graph via the `parent:` chain. This is the operational instantiation of the vision's *"audit becomes inspection of the substrate"* claim.
  - Report includes honest counter-evidence: ≥ 1 friction point or anti-pattern observed (where SEM-IA imposed cost without commensurate value).
- **A — Achievable:** ⚠️ — 4 months post-TFM (July → November 2026). Achievability depends critically on **project sizing**: must be non-trivial enough to exercise the framework, small enough to complete end-to-end in 4 months by one person. Risk: scope creep on the secondary project. **Mitigation: a hard sub-decision at G3-kickoff that fixes secondary-project scope at ≤ 5 stories, with the project's own retro at the midpoint.**
- **R — Relevant:** ✅ — The portability claim and the defect-prevention claim are the two strongest predictions the vision makes. G3 tests both simultaneously. Vision-retirement test: if the vision were retired, this goal would be retired with it; the goal exists *for* the vision.
- **T — Time-bound:** ✅ — Target **November 2026** (6 months from now, 4 months post-TFM). Slippage on G3 is recoverable (no external deadline), unlike G2.

## Parent vision anchor

`vision-sem-ia` Statement: *"Anyone running a software engineering effort, from solo builder to large enterprise, operates with the discipline of a full SE organization, because the organizational layer that used to depend on human bandwidth has been reformulated as a substrate of homologous AI agents… The agents absorb the cost specific to working with AI (review burden, hallucination, scope drift, context loss); the human keeps authorship, judgement and the right to sign."*

G3 is the empirical test of both halves of that statement: portability ("anyone, any project") and cost-absorption ("review burden, hallucination, scope drift, context loss"). Without G3, both halves are claims without evidence.

## Non-goals

- **Not a different-author case study.** A genuinely external user (someone who is not pelayo) belongs to the next roadmap. This is concierge testing, deliberately.
- **Not a tool-portability test.** Whether SEM-IA runs on other AI harnesses (Cursor, Aider, custom) is a separate capability question, not part of G3.
- **Not a statistically significant defect-prevention study.** N=1 case study cannot deliver statistical significance; G3's evidence is qualitative-plus-counts, not p-values.
- **Not a productization step.** No commercial packaging, licensing model, or partner onboarding.
- **Not a SEM-IA refactor.** Improvements to SEM-IA prompted by friction surfaced in G3 are *outputs* (backlog items for a future roadmap), not the goal itself.

## Source

- Skill: `po-goals`.
- GISF UC3M `gisf-discovery.pdf` slides 94–96 (goal-driven leadership, SMART, why-stack).
- GISF UC3M `gisf-delivery-planning.pdf` slide 150 (multilevel planning horizons).
- GISF UC3M `gisf-life-cycle.pdf` slide 54 (canonical *goal* definition).
- Cagan Principles 2, 9, 10 + Positioning statement, via GISF `gisf-discovery.pdf` slides 84, 89.
- "Concierge testing" is convention (Eric Ries / Lean Startup); not in audited `bibliography/sources/`. Flagged for traceability.
- SMART origin: Doran, G. T. (1981) — cited via GISF.
- Parent vision: [[vision-sem-ia]].
