---
category: session
id: 2026-05-14-sem-ia-self-bootstrap
date: 2026-05-14
participants: [product-owner]
related-nodes:
  - "[[vision-sem-ia]]"
  - "[[goal-01-self-bootstrap-validation]]"
  - "[[goal-02-tfm-public-artifact]]"
  - "[[goal-03-portability-proof]]"
---

# SEM-IA self-bootstrap — derive the framework's own graph

## Context

SEM-IA exists as code, skills, agents, templates and bibliography, but `nodes/` is empty: the framework has not yet been modelled in its own graph. This session bootstraps that graph by reverse-engineering the framework as a product — vision → goals → (later) capabilities → features → stories → specs. The exercise is meta-recursive and serves as a hard validation of SEM-IA: if SEM-IA can describe itself within its own backbone hierarchy (GISF `gisf-life-cycle.pdf` slide 53), the framework is internally consistent. Once the existing reality is captured as nodes, subsequent sessions can use those nodes as the basis for improving SEM-IA itself.

Scope of *this* session: draft `vision` (root) and 2–4 SMART `goals` under it. Capabilities and below are deferred to follow-up sessions.

## Log

### 2026-05-14 — product-owner

Opened the session. Confirmed slug `sem-ia-self-bootstrap` with the human. Next: apply skill `po-vision` to draft the root vision node, following Cagan's 10 principles via GISF `gisf-discovery.pdf` slides 82, 84, 86, 89 and the GISF 5-step construction method.

Next: draft `nodes/vision-sem-ia.md` and present to the human for validation.

### 2026-05-14 — product-owner

Applied skill `po-vision`. Dialog with the human surfaced the structural thesis behind SEM-IA: it is not a product-for-a-persona but **infrastructure** — AI-as-infrastructure replacing the older "AI-as-tool" / "AI-as-employee" framings. The unmet need is the AI-specific cost (review burden, hallucination, scope drift, context loss) that today blocks enterprise adoption and prevents freelancers from scaling. The vision absorbs an earlier TFM thesis paragraph by the author, reformulated as infrastructure and aligned with the current role catalog (5 implemented + Security + Designer planned; Coach and Quant dropped as legacy). Horizon fixed at 5 years (2031). One-breath statement: *"SEM-IA is AI-as-infrastructure: one homologous agent per classical SE role, vault-mediated, human-directed, making software engineering rigor available at any scale."* All 10 Cagan principles self-checked ✅ in the node. The paradigm name "AI as infrastructure" is flagged as out-of-bibliography (human author's formulation, not audited citation).

Skills applied: `po-vision`.
Artifacts: [[vision-sem-ia]].
Next: apply skill `po-goals` to derive 2–4 SMART goals under the vision, anchored on GISF multilevel horizons (Roadmap 1–2 years, Release 2–9 months).

### 2026-05-14 — product-owner

Applied skill `po-goals`. Dialog with the human refined the goal set through several iterations: (a) clarified goal-vs-capability boundary — "support full product lifecycle" and "portable to harnesses" reclassified as capabilities, not goals; (b) consolidated TFM-defence and public-artifact into a single goal because the TFM is conceptual and only ~2 months out, so the documentation goal coincides with the academic milestone; (c) reframed "first external case study" as a portability proof on a second project authored by pelayo (concierge testing) — the genuinely external user case moves to the next roadmap. Defect-prevention proof folded into G3 as a success criterion rather than a separate goal (no baseline measurable without a case).

Final set: 3 release-horizon goals covering May-2026-to-mid-2027.

- **G1** [[goal-01-self-bootstrap-validation]] — target July 2026. SEM-IA's own graph derived in SEM-IA; full role coverage; primary-source citations on every claim.
- **G2** [[goal-02-tfm-public-artifact]] — target July 2026 (hard deadline). TFM defended + public repo + README positioning "AI as infrastructure" + complete bibliographic traceability.
- **G3** [[goal-03-portability-proof]] — target November 2026. SEM-IA applied end-to-end to a non-SEM-IA project (same author); comparative report with defect-prevention evidence.

SMART pass: all five axes ✅ on G1 and G2; G3 carries ⚠️ on Achievability (4-month post-TFM window, contingent on tight scope-fixing for the secondary project). All three why-stacks land on `vision-sem-ia` (Statement + Principles 2/9/10 + positioning).

Skills applied: `po-goals`.
Artifacts: [[goal-01-self-bootstrap-validation]], [[goal-02-tfm-public-artifact]], [[goal-03-portability-proof]].
Next: apply skill `po-capabilities` to derive capabilities under each goal — keep them implementation-agnostic, filterable into an MVP, separated from features.

## Artifacts touched

- Created `nodes/vision-sem-ia.md` — root vision for SEM-IA framed as AI-as-infrastructure; horizon 5 years; positioning statement written; 10 Cagan principles self-checked.
- Created `nodes/goal-01-self-bootstrap-validation.md` — release-horizon goal targeting July 2026; the self-modelling test of the framework.
- Created `nodes/goal-02-tfm-public-artifact.md` — release-horizon goal with hard deadline July 2026; academic defense + public release.
- Created `nodes/goal-03-portability-proof.md` — release-horizon goal targeting November 2026; second-project concierge test with defect-prevention evidence.

## Subagent consultations

- (none yet)

## Closing summary

> Filled in at `/session-close`.

**Outcome:** —

**Pending / next steps:** —

**Merge decision:** —
