---
type: capability
parent: goal-02-tfm-public-artifact
status: draft
created: 2026-05-14
updated: 2026-05-22
maintained_by_role: product-manager
labels:
  - mvp:go
---

# Capability 08 — Primary-source citation discipline

> Authored via `po-capabilities`. Canonical definition: GISF `gisf-life-cycle.pdf` slide 54. MVP filter: slide 69. Cagan four risks: slide 64.

## Statement (slides 97–99 form)

In order to **defend every authoritative claim made under the framework against bibliographic audit** (parent goal [[goal-02-tfm-public-artifact]] — TFM defense rests on this — also serves [[goal-01-self-bootstrap-validation]] (G1's citation-audit M-criterion) and [[goal-03-portability-proof]]),
as **the SEM-IA author and any future reader / auditor / academic committee**,
I want **the ability to trace any authoritative statement made by an agent (formal criterion, threshold, anti-pattern, decision rule) back to a specific primary source — Capers Jones BP # / page, Cagan principle # via GISF slide, GISF slide #, Cucumber page, Patton page, Cohn via GISF — without exception, with out-of-bibliography frameworks explicitly flagged as convention rather than authority**.

## Implementation-agnostic test

- **Implementation A** (current): each skill's `## Formal criteria` and `## Source` cite verbatim references; `bibliography/skill-references.md` carries per-skill traceability; `bibliography/sources/` holds the 12 audited PDFs; meta-template `.claude/templates/SKILL.md.template` encodes the citation discipline for new skills.
- **Implementation B** (alternative): automated citation linter as a pre-commit hook that blocks merges on uncited authoritative claims; structured citation metadata in a separate annotations file consumed by tooling.

A third plausible: runtime tool that blocks an agent from outputting an authoritative statement unless tagged with a citation pointer. The capability is *citation as a non-negotiable property of authoritative reasoning*, not the enforcement mechanism.

## MVP Go / No-go

- **Value risk:** Without this capability, the TFM defense is unfounded and the framework reduces to *"another set of opinions"*. Highest-value capability for the academic dimension.
- **Usability risk:** Moderate — the human must know what counts as a primary source and where to find it; the bibliography indices help.
- **Viability risk:** Proven — 37 skills currently anchored to Jones / Cagan (via GISF) / GISF UC3M / Cucumber / Patton / Cohn (via GISF).
- **Business viability risk:** N/A.

**Decision: Go** — necessary for G2 and reinforcing for G1 + G3.

## Non-overlap with sibling capabilities

- Sibling (same parent): [[cap-12-public-publication]] — independent. Publication makes the artifact reachable; citation discipline is the *property of the artifact*.
- Sibling (different parent): [[cap-01-vision-to-code-audit]] — adjacent. Audit traversal is *navigation*; citation discipline is *content rigor*.
- Sibling (different parent): [[cap-05-apply-qa-discipline]] — adjacent. The audit *method* (how citations are verified at audit time) is QA-scope; this capability is *that the citation property exists* in the substrate.

## Non-coverage

- **Not about the audit method.** How citations are verified at audit time is QA-scope (G1-B M-criterion explicitly defers method to QA).
- **Not about out-of-bibliography frameworks.** When the human uses a framework not in audited `bibliography/sources/` (Cagan books themselves, Nygard ADRs, ITIL, Clean Code, etc.), the capability still applies via the flagging discipline (disclaimer in `## Source`); it does not block use of such frameworks.
- **Not about absence of opinion.** Authoritative claims are cited; conversational opinion, hypothesis, and conjecture do not need citation when explicitly marked as such.

## Source

- Skill: `po-capabilities`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54, slide 69; `gisf-discovery.pdf` slides 97–99.
- Cagan four risks: `gisf-life-cycle.pdf` slide 64.
- CLAUDE.md operating principle: *"Citation is mandatory. Every authoritative claim traces to a primary source."*
- Features delivering this capability: 12 audited PDFs in `bibliography/sources/`; `bibliography/INDEX.md` (navigable map); `bibliography/skill-references.md` (per-skill traceability); every skill's `## Source` section; `.claude/templates/SKILL.md.template` (citation discipline for new skills).
- Cross-link to [[vision-sem-ia]] Step 2 *"each agent has its own scope, custody, bibliography and skills"*.
