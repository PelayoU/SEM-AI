---
category: goal
id: goal-02-tfm-public-artifact
parent: "[[vision-sem-ia]]"
status: draft
horizon: release
created: 2026-05-14
updated: 2026-05-14
---

# Goal 02 — TFM defended and SEM-IA published as a public artifact

> Authored via `po-goals`. Canonical criteria: SMART (GISF `gisf-discovery.pdf` slide 95) + multilevel planning horizons (GISF `gisf-delivery-planning.pdf` slide 150) + why-stack discipline (slide 96) + slide 95 stakeholder form. Goal definition: GISF `gisf-life-cycle.pdf` slide 54.

## Statement (slide 95 form)

In order to **defend SEM-IA academically and publish it as a public artifact**,
as **the SEM-IA author and TFM candidate**,
I want **capabilities that produce a defendable thesis document, a public repository, a positioning README, and a complete bibliographic-traceability table**.

## Horizon (slide 150)

**Release** (2–9 months). Target completion: **July 2026 — externally fixed by the TFM defense date**. This is the only hard-deadline goal in the current roadmap; G1 and G3 are pinned around it.

## Why-stack trace (slide 96)

- Why this goal? → Because the TFM defense is the external trigger that forces SEM-IA to become defendable and public; without it the framework remains a private artifact.
- Why does the framework need to become public? → Because the parent vision claims SEM-IA is **infrastructure** — usable by anyone running a software engineering effort. A private artifact cannot be infrastructure; infrastructure must be reachable, readable, citable.
- Why does that matter? → Because Cagan Principle 10 (*"Evangelize continuously and relentlessly"*) is non-negotiable: a vision that nobody outside the author can read or repeat cannot become real.
- Lands on **[[vision-sem-ia]]** → *Statement* + *Principle 10 (evangelize)* + *Positioning statement* (target audience is anyone, not the author). ✅

## SMART self-check (slide 95, attributed to Doran 1981)

- **S — Specific:** ✅ — Two coupled deliverables clearly bounded:
  1. *Academic*: TFM document defended in front of the tribunal.
  2. *Public*: SEM-IA repo public, README in place positioning *"AI as infrastructure"*, bibliographic traceability complete.
- **M — Measurable:** ✅ — Boolean checklist:
  - TFM document submitted by the academic deadline.
  - Defense scheduled, presented and graded.
  - Repository public (default branch readable without auth).
  - `README.md` present at repo root, opening with the "AI as infrastructure" positioning (one-breath statement from [[vision-sem-ia]] step 4 of the 5-step trace).
  - `bibliography/skill-references.md` complete — every skill in `.claude/skills/` traced to its primary sources (Jones BP # / Cagan principle / GISF slide / etc.).
  - At least 1 external reader (peer, mentor, advisor) has read the artifact prior to defense and given feedback.
- **A — Achievable:** ✅ — Two months. The TFM document is already substantially drafted by virtue of the framework existing in code form; the work is consolidation + write-up + defense rehearsal. Risk: the publishing-the-repo step is often skipped under TFM pressure — explicit non-skip clause.
- **R — Relevant:** ✅ — Operationalises Principle 10 of [[vision-sem-ia]]. Without this goal, the vision's claim that SEM-IA is infrastructure is unfalsifiable (nobody can try it). Vision-retirement test: if the vision were retired, this goal would lose its anchor; the goal exists *for* the vision.
- **T — Time-bound:** ✅ — **July 2026** (hard, externally imposed by TFM defense calendar). Slippage on T is the most expensive failure in the roadmap.

## Parent vision anchor

`vision-sem-ia` Statement: *"Anyone running a software engineering effort, from solo builder to large enterprise, operates with the discipline of a full SE organization…"*. "Anyone" presupposes accessibility. Accessibility presupposes publication. G2 is the act that converts the vision's *anyone* from rhetorical into actual.

Also anchored on Principle 10 (evangelize) and the positioning statement (target audience is the world, not the author).

## Non-goals

- **Not a marketing campaign.** Public artifact + README is enough; paid promotion, conference circuit, growth-hacking are out of scope.
- **Not external community building.** Issue tracker open, PRs accepted in principle, but moderation, contributor onboarding, governance documents are post-G2.
- **Not internationalisation.** Single-language (English) artifact is sufficient.
- **Not a polished website.** GitHub README is the artifact. A standalone documentation site (Docusaurus, MkDocs, etc.) is post-G2.
- **Not a paper submission.** Academic publication beyond the TFM document is out of scope.

## Source

- Skill: `po-goals`.
- GISF UC3M `gisf-discovery.pdf` slides 94–96 (goal-driven leadership, SMART, why-stack).
- GISF UC3M `gisf-delivery-planning.pdf` slide 150 (multilevel planning horizons).
- GISF UC3M `gisf-life-cycle.pdf` slide 54 (canonical *goal* definition).
- Cagan Principle 10 ("Evangelize continuously and relentlessly"), via GISF `gisf-discovery.pdf` slide 89.
- SMART origin: Doran, G. T. (1981) — cited via GISF.
- Parent vision: [[vision-sem-ia]].
