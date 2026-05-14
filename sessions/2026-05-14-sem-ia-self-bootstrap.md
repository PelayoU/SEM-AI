---
category: session
id: 2026-05-14-sem-ia-self-bootstrap
date: 2026-05-14
participants: [product-owner]
related-nodes: []
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

## Artifacts touched

- Created `nodes/vision-sem-ia.md` — root vision for SEM-IA framed as AI-as-infrastructure; horizon 5 years; positioning statement written; 10 Cagan principles self-checked.

## Subagent consultations

- (none yet)

## Closing summary

> Filled in at `/session-close`.

**Outcome:** —

**Pending / next steps:** —

**Merge decision:** —
