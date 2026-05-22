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

# Goal 01 — Self-bootstrap validation

> Authored via `po-goals`. Canonical criteria: SMART (GISF `gisf-discovery.pdf` slide 95) + multilevel planning horizons (GISF `gisf-delivery-planning.pdf` slide 150) + why-stack discipline (slide 96) + slide 95 stakeholder form. Goal definition: GISF `gisf-life-cycle.pdf` slide 54.

## Statement (slide 95 form)

In order to **validate that SEM-IA is internally consistent before public defense**,
as **the SEM-IA author and TFM candidate**,
I want **capabilities that derive the framework's own vision, goals, capabilities, features, stories and specs as nodes in the SEM-IA graph, with full role coverage and primary-source citations on every authoritative claim**.

## Horizon (slide 150)

**Release** (2–9 months). Target completion: **July 2026** (~2 months from session opening 2026-05-14). Sits within the broader May-2026-to-mid-2027 roadmap together with [[goal-02-tfm-public-artifact]] and [[goal-03-portability-proof]].

## Why-stack trace (slide 96)

- Why this goal? → To prove that SEM-IA is internally consistent — that the framework can model itself in its own graph without breaking the parent chain or the citation discipline.
- Why prove internal consistency? → Because the parent vision claims SEM-IA is infrastructure that traces vision-to-code; if SEM-IA cannot trace itself, that core claim is unfounded.
- Why does that matter? → Because per Cagan principle 9, the vision is an act of faith — and an act of faith needs at least one concrete piece of evidence before public defense. Self-modelling is the cheapest, strongest such evidence available.
- Lands on **[[vision-sem-ia]]** → *Statement* + *Principle 9 (act of faith)* + *Principle 2 (love the problem)*. ✅

## SMART self-check (slide 95, attributed to Doran 1981)

- **S — Specific:** ✅ — Scope = the SEM-IA framework itself, modelled as a complete SEM-IA graph. Boundaries: all backbone categories (vision, goal, capability, feature, story, spec) represented; all five implemented roles (PO, Architect, QA, Developer, DevOps) have authored ≥ 1 node; every authoritative claim cites a primary source (Jones / Cagan / GISF / Patton / Cohn / Cucumber).
- **M — Measurable:** ✅ — Boolean / count checklist:
  - 1 `vision` node exists.
  - ≥ 3 `goal` nodes exist (this set).
  - ≥ N `capability` nodes covering the goals (N to be set during capability decomposition; minimum 1 per goal, target 2–4 per goal).
  - ≥ 1 `feature`, ≥ 1 `story`, ≥ 1 `spec` exist, chained correctly (parent edges + story-to-AC trace).
  - ≥ 1 `adr` node exists, exercising the architectural-decision template under SEM-IA's own substrate (the specific decision topic is Architect-scope at authoring time, not declared here).
  - All 5 implemented roles have authored or co-authored ≥ 1 node.
  - Citation audit passes: every authoritative claim across all nodes carries a primary-source citation traceable to `bibliography/`. The audit method is QA-scope (cross-link to `qa-inspections-program` and `qa-measurements`) at audit time; PO's responsibility here is only to declare the outcome required.
  - End-to-end navigation from `vision-sem-ia` to a spec-affecting code node succeeds with no broken `parent:` edges.
- **A — Achievable:** ✅ — Session `2026-05-14-sem-ia-self-bootstrap` opened the work today; ~2 months of available focus to TFM defense. Risk: scope creep within each layer (capabilities exploding into 10+ instead of 3–5). Mitigation: discipline of stopping each layer at the minimum that satisfies the level above.
- **R — Relevant:** ✅ — Directly advances `vision-sem-ia` Statement (*"framework that traces vision through code"*) and Principle 9 (*"vision is an act of faith"* — this goal converts faith into evidence). Vision-retirement test: if the vision were retired, this goal would be retired with it; the goal exists *for* the vision.
- **T — Time-bound:** ✅ — Target **2026-07** (window: July 2026, aligned with TFM defense window per [[goal-02-tfm-public-artifact]]).

## Parent vision anchor

`vision-sem-ia` Statement: *"… reformulated as a substrate of homologous AI agents that read, write and verify on the project's vault…"*. The vault for SEM-IA itself is the `nodes/` graph of SEM-IA. G1 produces that vault. Without G1, the vision describes a property the framework does not yet exhibit.

Also anchored on Principle 9 (act of faith — needs evidence) and Principle 2 (love the problem — proving traceability is the structural evidence the problem is real and solved).

## Non-goals

- **Not a complete feature/story/spec inventory.** The minimum-viable demonstration is enough: ≥ 1 feature + ≥ 1 story + ≥ 1 spec to prove the chain works. Exhaustive decomposition is post-G1.
- **Not a tool-portability test.** Whether SEM-IA can run on harnesses other than Claude Code is out of scope for G1; belongs to a future roadmap (post-November 2026).
- **Not an external-user validation.** G3 ([[goal-03-portability-proof]]) covers second-project validation; this goal is strictly self-bootstrap.
- **Not a performance / scale benchmark.** Internal consistency, not throughput.

## Source

- Skill: `po-goals`.
- GISF UC3M `gisf-discovery.pdf` slides 94–96 (goal-driven leadership, SMART, why-stack).
- GISF UC3M `gisf-delivery-planning.pdf` slide 150 (multilevel planning horizons).
- GISF UC3M `gisf-life-cycle.pdf` slide 54 (canonical *goal* definition).
- SMART origin: Doran, G. T. (1981) — book not in audited `bibliography/sources/`; cited via GISF.
- Parent vision: [[vision-sem-ia]].
