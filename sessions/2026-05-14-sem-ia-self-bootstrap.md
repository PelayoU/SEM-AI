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
  - "[[cap-01-vision-to-code-audit]]"
  - "[[cap-02-role-scoped-agents]]"
  - "[[cap-03-apply-po-discipline]]"
  - "[[cap-04-apply-architect-discipline]]"
  - "[[cap-05-apply-qa-discipline]]"
  - "[[cap-06-apply-developer-discipline]]"
  - "[[cap-07-apply-devops-discipline]]"
  - "[[cap-08-citation-discipline]]"
  - "[[cap-09-session-continuity]]"
  - "[[cap-10-subagent-consultation]]"
  - "[[cap-11-adr-capture]]"
  - "[[cap-12-public-publication]]"
  - "[[cap-13-portability]]"
  - "[[adr-001-sessions-as-git-branch]]"
  - "[[adr-002-backbone-hierarchy-parent-edges]]"
  - "[[adr-003-citation-mandate]]"
  - "[[adr-004-substrate-content-separation]]"
  - "[[adr-005-subagent-dispatch-not-authority-transfer]]"
  - "[[adr-006-super-po-fusion]]"
  - "[[adr-007-obsidian-as-editor-surface]]"
  - "[[adr-008-markdown-frontmatter-data-format]]"
  - "[[adr-009-skill-as-canonical-method]]"
  - "[[adr-010-human-directed-ai-maintained]]"
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

### 2026-05-14 — product-owner

Conversation with the human surfaced two structural insights about the vision and triggered a full audit + refinement pass before descending to capabilities:

1. *Programming ≠ product-building.* The vision was sharpened to name the moment-of-truth at deployment as the cost SEM-IA closes (Cagan principle 1 — start with why — operationalised).
2. *The framework is the entire stack, not just the graph.* The vision was further sharpened (structurally, without enumerating components, per Cagan principle 8) to state that the SEM-IA substrate ships with the code and audit becomes inspection of the substrate.

The human then loaded the full SEM-IA stack into PO context (~50 files: 5 agents, 8 templates, 37 skills, 2 bibliography indices, role catalog) because the substrate inventory was needed to reason about capabilities. This loading produced **PO contamination**: when running an audit pass on the 4 existing nodes (vision + 3 goals), the PO began prescribing inspection mechanisms (QA-scope) and measurement units (QA-scope) instead of restricting itself to outcome declaration. The human caught the contamination; the PO retracted and reformulated three audit findings in PO-only scope.

Final corrected audit findings, applied as edits:

- **G1-A** — Add `≥ 1 adr` to the cobertura de categorías in G1's M-criterion. The specific ADR topic is Architect-scope at authoring time, not declared in the goal.
- **G1-B** — Replace "0 authoritative claims without a primary-source citation (audit pass)" with an outcome-only formulation that defers the audit *method* to QA at audit time.
- **G3-A** — Replace the (a)/(b)/(c) generic axes with five axes derived 1:1 from the vision Statement: review burden, hallucination, scope drift, context loss, deployment-readiness/maintainability. Metric design per axis is QA-scope; PO declares only that all five axes are non-negotiable. Decision-traceability is kept as a separate criterion (operational instantiation of the vision's "audit becomes inspection of the substrate" claim).

Three improvement candidates captured during the conversation (deferred — not acted on in this session):

- *Consultation matrix*: the PO-agent's `agent.md` has a coarse hand-off table for cross-role interaction but no fine-grained per-skill / per-node-type rule, nor a "consider consultation" gate in the workflow. Codification deferred to a post-bootstrap session.
- *Next-roadmap adoption milestone*: a future goal (post-Nov-2026) along the lines of *"1 software product shipped publicly with its complete SEM-IA substrate as part of the distribution"* — adoption-level outcome, belongs to the next roadmap not this one.
- *Graph-vs-substrate operating rule*: the framework should declare explicitly that the project graph (nodes/) is the navigation surface for any role-agent operating on the project, while the substrate (.claude/skills/, .claude/agents/) is for substrate maintainers only. Cross-role information flows through the graph, not through the substrate. This rule, codified, prevents the contamination observed in this session — and dissolves once the bootstrap completes, because future PO sessions will operate on the graph.

Skills applied: `po-vision` (audit pass), `po-goals` (audit pass).
Artifacts: [[vision-sem-ia]] (3 edits), [[goal-01-self-bootstrap-validation]] (2 edits), [[goal-03-portability-proof]] (1 edit).
Next: apply skill `po-capabilities` to derive capabilities under each goal.

### 2026-05-14 — product-owner (capabilities first attempt — rolled back)

Applied skill `po-capabilities` top-down, deriving 9 candidate capabilities from the 3 release-horizon goals. Each candidate passed the implementation-agnostic test, MVP Go/No-go via Cagan four risks, parent-goal anchoring, and non-overlap with siblings. Wrote 9 nodes (cap-01 to cap-09).

Human review surfaced three problems before commit:

1. **No subagent consultation** despite earlier explicit commitment to invoke Architect when a capability touches Architect-scope (cap-04 vault, cap-07 ADR, cap-09 substrate/content separation were all candidates).
2. **Top-down framing assumed without offering the choice.** GISF slide 53 permits *"top-down + bottom-up loop"*; the human's instinct was bottom-up.
3. **Coverage gap.** Of 37 existing skills in the substrate, ~25 do not map to any of the 9 capabilities (most Developer, QA, DevOps, and half the PO skills are orphans). The 9 capabilities cover **meta-capabilities** (how the framework operates) but miss **object-capabilities** (what the framework lets the user do *inside their project*).

Decision: rollback all 9 cap nodes. Restart with bottom-up audit pass: enumerate substrate (37 skills + 5 agents + 8 templates + bibliography + CLAUDE.md + commands), group bottom-up into capability clusters, map each to its parent goal, identify cases that need additional goals (likely scenario: the framework has capabilities not demanded by the current 3 release-horizon goals, so either new goals are surfaced or the substrate is flagged as latent).

Skills applied: `po-capabilities` (then rolled back).
Artifacts created and deleted: cap-01 through cap-09.
Next: bottom-up audit pass — first inventorise substrate, then cluster into capabilities, then map.

### 2026-05-14 — product-owner (capabilities second attempt — bottom-up)

Restarted `po-capabilities` with a bottom-up audit pass. **Phase A (inventory):** enumerated 81 substrate items (CLAUDE.md + 5 agents + 37 skills + 8 node templates + 2 meta-templates + 3 slash commands + 14 bibliography items + 1 role catalog + 1 settings.json + 1 LICENSE + 8 `.obsidian/` config files + 1 `_obsidian/bases/` placeholder). The human confirmed `.obsidian/` config IS part of the substrate (Obsidian is the recommended editor surface).

**Phase B (cluster):** grouped features bottom-up by user-ability delivered. Surfaced **16 capability candidates** — 13 implemented + 3 planned-but-unimplemented. The bottom-up pass surfaced **5 capabilities the first top-down attempt missed**: one *"Apply audited X discipline"* per implemented role (PO, Architect, QA, Developer, DevOps). These are the **object-capabilities** that the previous attempt's pure-meta framing had occluded.

**Phase C (map to goals):** distribution G1 = 9, G2 = 3, G3 = 1 for implemented capabilities. 0 of the 81 substrate items remained as orphans — every implemented feature falls under at least one capability.

**Phase D (Architect consultation decision):** The PO decided **not** to invoke Architect at the capability level. Reasoning: (1) capability description is PO scope; (2) Architect-content (specific ADRs, structural decisions) is feature-level work, not capability-level; (3) cost of unnecessary consultation is contamination of strategic scope by technical framing. Architect consultation is flagged as appropriate when features are decomposed under cap-04 (Apply audited Architect discipline) and cap-11 (ADR capture), which will happen in a subsequent session.

Capabilities written (13, all `mvp: go`):

| ID | Title | Parent goal |
|---|---|---|
| cap-01 | Vision-to-code navigation and audit | G1 |
| cap-02 | Role-scoped AI agents with explicit custody | G1 |
| cap-03 | Apply audited Product / BA / PM discipline | G1 |
| cap-04 | Apply audited Architect discipline | G1 |
| cap-05 | Apply audited QA discipline | G1 |
| cap-06 | Apply audited Developer discipline | G1 |
| cap-07 | Apply audited DevOps discipline | G2 |
| cap-08 | Primary-source citation discipline | G2 |
| cap-09 | Work-thread continuity via sessions | G1 |
| cap-10 | Cross-role consultation (not authority transfer) | G1 |
| cap-11 | Architectural-decision capture (ADRs) | G1 |
| cap-12 | Public publication of the substrate | G2 |
| cap-13 | Portability to projects other than SEM-IA | G3 |

Three planned capabilities **captured as deferred items** (improvement candidate #10 — not written as nodes in this session; belong to next-roadmap goals when goals exist that demand them):

- **cap-14 (deferred)** — Filtered graph views via Obsidian Bases. `_obsidian/bases/` scaffolding exists; no `.base` files yet.
- **cap-15 (deferred)** — Security role coverage (Tier-3 per sem-role-catalog.md). Security agent + skills not implemented.
- **cap-16 (deferred)** — Designer role coverage (Tier-3 per sem-role-catalog.md). Designer agent + skills not implemented.

Skills applied: `po-capabilities` (bottom-up).
Artifacts: cap-01 through cap-13 (13 nodes).
Next: `po-feature-decomposition` to decompose each capability into features and stories under INVEST + Patton Story Map. Architect consultation appropriate at feature level under cap-04 (Architect discipline) and cap-11 (ADR capture).

### 2026-05-14 — product-owner (capabilities audit pass — surfaced)

Surfaced the formal audit of the 13 capabilities against the 7 `po-capabilities` skill criteria (GISF slide 54 canonical definition; slide 69 MVP filter; slides 97–99 stakeholder framing form; slide 64 Cagan four risks; non-overlap with siblings; decomposable into features; parent goal anchoring). **All 13 pass all 7 criteria.**

One borderline acknowledged: **cap-01** fuses *backbone hierarchy* (structural property) with *audit-by-navigation* (behavioural property). Defended as a single capability because audit is the *use* of traceability; flagged here in case future review prefers to split into cap-01a (structural) + cap-01b (navigation surface).

### 2026-05-14 — product-owner (Phase 1: ADRs via Architect)

PO dispatched **Architect via Task subagent** with the 8 candidate architectural decisions identified during the bootstrap conversation. Architect authored **10 ADRs** (8 of the PO's list + 1 merged + 3 new not on PO's list). All `status: accepted` (each captures a decision already de facto in force in the substrate). PO did NOT author any ADR content — Architect-scope honoured.

ADRs created:

| ID | Title | Parent | Origin |
|---|---|---|---|
| adr-001 | Sessions = git branch | goal-01 | PO list #1 |
| adr-002 | Backbone hierarchy with parent edges | vision-sem-ia | PO list #2 |
| adr-003 | Citation mandate + out-of-bibliography flagging | cap-08 | PO list #3 + #7 **merged** (Architect's call: flagging is the negative space of the mandate, inseparable) |
| adr-004 | Substrate vs content directory separation | cap-13 | PO list #4 |
| adr-005 | Subagent dispatch ≠ authority transfer | cap-10 | PO list #5 |
| adr-006 | Super-PO fusion at Tier-1 | vision-sem-ia | PO list #6 |
| adr-007 | Obsidian as recommended editor surface | cap-01 | PO list #8 (recommendation, not mandate — editor-agnostic data layer documented as load-bearing portability property) |
| adr-008 | Markdown body + YAML frontmatter as canonical data format | vision-sem-ia | **Architect-added** — Jones Ch 7 topic 2 (data structure) was silent without this |
| adr-009 | Skill = canonical method for one operation | vision-sem-ia | **Architect-added** — functional decomposition of every role's catalog |
| adr-010 | Human directs, AI maintains | vision-sem-ia | **Architect-added** — operational anchor of the AI-as-infrastructure paradigm; CLAUDE.md operating principle #1 |

Concerns Architect flagged for PO follow-up (captured here, not acted upon in this phase):

1. **Nygard ADR convention is tier-2 (out-of-bibliography).** Every ADR repeats the flag. Adding Nygard's *Documenting Architecture Decisions* to `bibliography/sources/` would promote ADRs to tier-1 — PO decision.
2. **No ADR directly parented to goal-02 or goal-03.** Cap-level parenting is structurally cleaner; not an omission.
3. **Cross-goal wikilinks in cap bodies** (e.g., "also serves goal-X") are honoured per ADR 002 (frontmatter edge is the single `parent:`; cross-references live in body). Working as designed.
4. **No ADR for `claude --agent <role>` as harness choice.** Out-of-scope per cap-13's non-coverage clause; can be authored quickly if PO wants the current harness captured for TFM completeness.
5. **No ADR for `LICENSE` choice** (file is currently a placeholder). When PO picks a license, that decision should be captured as an ADR.
6. **The 10 ADRs are paradigm-defining only.** Downstream architectural decisions (slash-command interaction model, session-doc closing semantics, etc.) get their own ADRs as features and stories are decomposed.

Skills applied (PO-side): `po-capabilities` (no new skill; consultation was Architect's exercise of `architect-architecture-design`).
Artifacts: 10 ADR nodes.
Next: Phase 2 — structural features.

## Artifacts touched

- Created `nodes/vision-sem-ia.md` — root vision for SEM-IA framed as AI-as-infrastructure; horizon 5 years; positioning statement written; 10 Cagan principles self-checked. **Edited** to add programming-vs-product framing (Statement) and substrate-ships-with-code framing (Statement closing + Step 2 of 5-step trace).
- Created `nodes/goal-01-self-bootstrap-validation.md` — release-horizon goal targeting July 2026; the self-modelling test of the framework. **Edited** to add `adr` coverage and to reformulate the citation audit as outcome-only (QA-scope for method).
- Created `nodes/goal-02-tfm-public-artifact.md` — release-horizon goal with hard deadline July 2026; academic defense + public release. (No audit edits required.)
- Created `nodes/goal-03-portability-proof.md` — release-horizon goal targeting November 2026; second-project concierge test with defect-prevention evidence. **Edited** to map the comparative-report axes 1:1 to the vision's named costs (review burden, hallucination, scope drift, context loss, deployment-readiness), with metric design deferred to QA.
- *(Capabilities first attempt: cap-01 through cap-09 written then rolled back — see Log entry above. Coverage gap and missing subagent consultations diagnosed; bottom-up audit pass followed.)*
- Created `nodes/cap-01-vision-to-code-audit.md` — vision-to-code navigation surfaced through editor. Parent G1.
- Created `nodes/cap-02-role-scoped-agents.md` — AI agents with bounded role custody. Parent G1.
- Created `nodes/cap-03-apply-po-discipline.md` — audited Product / BA / PM discipline (15 PO skills as features). Parent G1.
- Created `nodes/cap-04-apply-architect-discipline.md` — audited Architect discipline (5 Architect skills as features). Parent G1.
- Created `nodes/cap-05-apply-qa-discipline.md` — audited QA discipline with independence imperative (5 QA skills as features). Parent G1.
- Created `nodes/cap-06-apply-developer-discipline.md` — audited Developer discipline (5 Developer skills as features). Parent G1.
- Created `nodes/cap-07-apply-devops-discipline.md` — audited DevOps discipline (7 DevOps skills as features). Parent G2.
- Created `nodes/cap-08-citation-discipline.md` — primary-source citation across all authoritative claims. Parent G2.
- Created `nodes/cap-09-session-continuity.md` — work-thread continuity via sessions. Parent G1.
- Created `nodes/cap-10-subagent-consultation.md` — cross-role consultation without authority transfer. Parent G1.
- Created `nodes/cap-11-adr-capture.md` — architectural decisions as cross-cutting durable artifacts. Parent G1.
- Created `nodes/cap-12-public-publication.md` — substrate accessibility for external readers. Parent G2.
- Created `nodes/cap-13-portability.md` — substrate operates on projects other than SEM-IA. Parent G3.
- Created `nodes/adr-001-sessions-as-git-branch.md` through `nodes/adr-010-human-directed-ai-maintained.md` — 10 Architect-authored ADRs covering the cross-cutting architectural decisions: sessions = branch, backbone hierarchy, citation mandate + flagging (merged), substrate/content separation, subagent dispatch ≠ authority transfer, super-PO fusion, Obsidian editor surface, markdown+YAML data format, skill = canonical method, human directs AI maintains.

## Subagent consultations

- `product-owner` → `architect` — Question: author the cross-cutting ADRs that capture the architectural decisions de facto in force in SEM-IA's substrate. PO supplied 8 candidate decisions; Architect was given authority to redefine the set, merge candidates, add Architect-identified decisions, and decide `accepted` vs `proposed` per ADR. Response summary: 10 ADRs authored, all `status: accepted`. ADR 003 merged candidates #3 + #7 (citation mandate + out-of-bibliography flagging). ADRs 008, 009, 010 added by Architect (data format / skill-as-method / human-directed AI-maintained). 6 concerns flagged for PO follow-up captured in the Phase 1 Log entry above.

## Closing summary

> Filled in at `/session-close`.

**Outcome:** —

**Pending / next steps:** —

**Merge decision:** —
