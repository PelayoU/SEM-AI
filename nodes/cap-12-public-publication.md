---
category: capability
id: cap-12-public-publication
parent: "[[goal-02-tfm-public-artifact]]"
status: draft
mvp: go
created: 2026-05-14
updated: 2026-05-14
---

# Capability 12 — Public publication of the substrate

> Authored via `po-capabilities`. Canonical definition: GISF `gisf-life-cycle.pdf` slide 54. MVP filter: slide 69. Cagan four risks: slide 64.

## Statement (slides 97–99 form)

In order to **make the SEM-IA substrate accessible to anyone — academic auditor, future user, fork author, casual reader** (parent goal [[goal-02-tfm-public-artifact]] — operationalises Cagan principle 10 *"evangelize continuously"*),
as **the SEM-IA author, the academic committee, and any future external reader**,
I want **the ability to publish the entire substrate (universal contract, role agents, skills, templates, bibliography, the project's graph and sessions) as a readable, navigable artifact gated by nothing more than a network connection and the willingness to read**.

## Implementation-agnostic test

- **Implementation A** (proposed for G2): public git repository on GitHub (or equivalent) with default branch readable without auth; README at root opening with the AI-as-infrastructure positioning; LICENSE permits forks; bibliography-traceability complete.
- **Implementation B** (alternative): published static site export of the substrate (MkDocs / Docusaurus / Obsidian Publish) navigable as web pages with stable URLs.

A third plausible: packaged release artifact (zip, container, language package) with a manifest; institutional repository deposit. The capability is *substrate accessibility*, not the publication channel.

## MVP Go / No-go

- **Value risk:** Without this capability, the framework remains private property and the *"infrastructure for anyone"* vision claim is unfalsifiable.
- **Usability risk:** Low — the user only needs to follow a public URL.
- **Viability risk:** Low — git hosting, static-site generators, package registries are all mature; `LICENSE` already in place at repo root.
- **Business viability risk:** N/A (open-source-friendly licensing already in place).

**Decision: Go** — required for G2 and operationalises the positioning statement.

## Non-overlap with sibling capabilities

- Sibling (same parent): [[cap-08-citation-discipline]] — independent. Citation discipline is *content rigor*; publication is *access path*.
- Sibling (same parent): [[cap-07-apply-devops-discipline]] — adjacent. DevOps discipline is *how the publication is run as a release event*; this capability is *that the substrate becomes publicly accessible*.
- Sibling (different parent): [[cap-01-vision-to-code-audit]] — adjacent. Publication makes the substrate reachable; audit-by-navigation then becomes possible for external readers.

## Non-coverage

- **Not about marketing or growth.** Publication ≠ promotion. Driving adoption is out of scope for the current roadmap (covered by the deferred next-roadmap *adoption milestone* candidate captured in the session log).
- **Not about community management.** Issue triage, PR review, contributor onboarding are governance, not the publication capability.
- **Not about translations.** Single-language publication is sufficient.

## Source

- Skill: `po-capabilities`.
- GISF UC3M `gisf-life-cycle.pdf` slide 54, slide 69; `gisf-discovery.pdf` slides 97–99.
- Cagan four risks: `gisf-life-cycle.pdf` slide 64.
- Cagan principle 10 (*"evangelize continuously and relentlessly"*) via GISF `gisf-discovery.pdf` slide 89.
- Features delivering this capability: `LICENSE` at repo root; (planned) README; public git hosting (convention, not Jones-anchored).
- Cross-link to [[vision-sem-ia]] Statement *"the SEM-IA substrate ships with the code, not separately"*.
