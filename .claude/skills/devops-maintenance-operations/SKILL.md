---
name: devops-maintenance-operations
description: "Run the operational side of software maintenance — coordination across the 23 maintenance work types (Capers Jones BP #48), ITIL-aligned service management (change / reliability / availability), and continuous flow visualization via the GISF Release Kanban (PBIs To Do / In Progress / Delivered) with Daily stand-up and Release Burn-Up Charts. Use whenever running the operational maintenance function (vs Developer's code-side maintenance), planning change response SLAs, deciding outsource vs in-source for maintenance, setting up release Kanban / burn-up tracking, coordinating daily ops, or sizing maintenance staffing. Triggers include phrases like 'maintenance operations', 'operational maintenance', 'ITIL', 'service desk', 'response SLA', 'change response time', 'maintenance Kanban', 'release Kanban', 'burn-up chart', 'daily stand-up', 'maintenance outsourcing', 'how many maintenance people'."
---

# devops-maintenance-operations

## Purpose

Jones (BP #48 p. 163) calls maintenance "the dominant expense of the entire software industry" — and observes that maintenance outsourcing is more successful than development outsourcing because aging software is less prone to catastrophic project risks. Where `developer-maintenance` handles the code-side (renovate, fix, remove error-prone modules), this skill handles the operations-side: ITIL-aligned change response, Release Kanban flow visualization, daily stand-up coordination, response-time tracking, maintenance-staff sizing.

## When this skill applies

- A maintenance operations function is being stood up or audited.
- Response-time SLAs for defect repair and change requests need defining.
- Maintenance outsourcing vs in-source is being decided.
- Release Kanban / burn-up tracking is being set up.
- Daily stand-up cadence is being designed.
- Maintenance staffing is being sized against Jones Table 5-1 ratios (Maintenance specialists 31.5%; the operational fraction of that).

## Formal criteria

A maintenance-operations pass is acceptable only if all of the following hold:

1. **23 maintenance work types acknowledged** *(Jones BP #48 pp. 161–162)* — the operational side coordinates across all 23 types; Developer handles the code work. Operations side names which work types fall to outsource, in-source, or hybrid (cross-link `developer-maintenance` for the canonical list).
2. **ITIL framework referenced** *(Jones BP #48 p. 162)* — Jones names ITIL as relevant for change management, reliability, availability. ITIL is out-of-bibliography for full standard but cited as practitioner framework.
3. **14+ legacy best practices coordinated** *(Jones BP #48 pp. 162–163)* — maintenance specialists vs developers; renovation workbenches; formal change management procedures + tools; formal regression test libraries; complexity analysis; error-prone module ID; dead code ID; renovate-before-enhance; inspections on major updates; customer-defect tracking; response-time tracking (defect repair AND change-request completion); cost tracking; warranty tracking; availability tracking.
4. **Response-time tracking in place** *(Jones BP #48 p. 163 practices 13–14)* — two distinct metrics: time from submission to defect repair, and time from submission to change-request completion. SLAs declared.
5. **Release Kanban for flow visualization** *(GISF `gisf-delivery-control-and-monitoring.pdf` slide 210)* — three-column board: PBIs To Do (highest priority at top) / PBIs In Progress / PBIs Delivered. Snapshot updated at iteration end.
6. **Release Burn-Up Chart for progress** *(GISF slide 211)* — accumulated delivered points over time vs total scope. Communicates progress in single chart.
7. **Daily stand-up coordination** *(GISF slide 93 + slide 240)* — daily fluid communication across the maintenance team and adjacent functions.
8. **Outsourcing decision documented** *(Jones BP #48 p. 163)* — Jones observes maintenance outsourcing has fewer failures and litigation cases than development outsourcing (5% dev-outsourcing litigation rate). Decision recorded with rationale.
9. **Maintenance-quality multiplier honored** *(Jones BP #48 p. 163 + BP #35 p. 123)* — every 120 delivered defects fewer ≈ 1 maintenance FTE saved; every 240 ≈ 1 customer-support FTE saved. Operations sizing is partly a function of upstream quality.

## How you proceed

1. **Audit existing maintenance ops.** Which of the 23 work types is the org actually handling? Which are unstaffed? Which fall through cracks?
2. **Decide the in-source / outsource split.** Strategic legacy + privileged-data → in-source. Non-strategic + commodity → outsource is empirically successful per Jones.
3. **Stand up the Release Kanban** (GISF slide 210). 3 columns; PBIs sized in points; highest priority at top of To Do. Refresh at iteration boundary.
4. **Build the Burn-Up Chart** (GISF slide 211). Cumulative delivered vs total scope plotted over iterations. Update at iteration end.
5. **Schedule the daily stand-up** for the maintenance team. ≤15 min; what was done yesterday / what is being done today / blockers.
6. **Set SLAs** for defect-repair time and change-request-completion time. Communicate to PO + customers.
7. **Set up the 14-practice tracking** (defects by customer, response time to repair, response time to CR completion, maintenance activities + costs, warranty costs, software availability).
8. **Size the team** against Jones Table 5-1 (Maintenance specialists 31.5% of staff) + the 120-defect multiplier (less delivered defects = less maintenance staff needed).
9. **Cross-coordinate** with `developer-maintenance` (code work), `devops-post-release-change` (renovation tool work), `devops-customer-support` (defect-flow from support intake).

## Pitfalls to avoid

- **Maintenance as one bucket.** 23 work types with different effort drivers. Aggregate "maintenance" budgets are reliably wrong.
- **No response-time tracking.** Both defect-repair and CR-completion times need explicit SLAs and measurement. Without them, customer dissatisfaction grows invisibly.
- **No flow visualization.** Without Release Kanban + Burn-Up, progress is invisible until a release crisis surfaces it.
- **Daily stand-up as status meeting.** ≤15 min; coordination, not reporting. Long stand-ups burn time.
- **Outsourcing strategic legacy.** Jones supports outsourcing for non-strategic maintenance; strategic / privileged-data systems are not appropriate.
- **Ignoring the 120-defect multiplier.** Maintenance staffing is partly a function of upstream quality. Operations sizing should surface the quality-investment trade-off to PO.
- **ITIL adopted as authority.** Cited by Jones as relevant but the standard itself is not in audited bibliography. Apply as convention; cite Jones for the principle.

## Source

- **Best Practice #48 — *Software Maintenance and Enhancement* (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, pp. 161–164).** 23 maintenance work-type taxonomy; ITIL reference; 14+ legacy best practices (practices 12–17 are the operational tracking metrics); maintenance-quality multiplier (120 defects ≈ 1 maintenance FTE); maintenance-outsourcing success rate.
- **Best Practice #35 — *SQA* (Jones 2010, pp. 120–124)** — economic-value-of-quality empirics: 120 + 240 defect-multipliers.
- **Chapter 5 Table 5-1** — Maintenance specialists 31.5% of software staff; Configuration Control specialists 1.5%; Customer Support specialists 2.0%. DevOps role aggregates these specialties.
- **GISF UC3M `gisf-delivery-control-and-monitoring.pdf`** — Release Kanban board (slide 210: PBIs To Do / In Progress / Delivered); Release Burn-Up Chart (slide 211); Daily stand-up meeting (slide 93 + slide 240).
- **Cross-references**: `developer-maintenance` (code-side of legacy work), `devops-post-release-change` (tool-supported renovation), `devops-customer-support` (defect inflow from support), `po-change-control` (CR pipeline), `qa-defect-removal-efficiency` (upstream quality drives downstream maintenance load).
- Out-of-bibliography (convention pointers only): ITIL v3/v4 full standard (cited by Jones but spec not in `sources/`), COBIT, DORA MTTR metric, Site Reliability Engineering (Google SRE Book).
- Full traceability: `bibliography/skill-references.md` § `devops-maintenance-operations`.
