---
name: devops-maintenance-operations
description: "Run the operational side of software maintenance — coordination across the 23 maintenance work types, ITIL-aligned service management (change / reliability / availability), and continuous flow visualization via the Release Kanban (PBIs To Do / In Progress / Delivered) with a Daily stand-up and Release Burn-Up Charts. Use whenever running the operational maintenance function (vs Developer's code-side maintenance), planning change response SLAs, deciding outsource vs in-source for maintenance, setting up release Kanban / burn-up tracking, coordinating daily ops, or sizing maintenance staffing. Triggers include phrases like 'maintenance operations', 'operational maintenance', 'ITIL', 'service desk', 'response SLA', 'change response time', 'maintenance Kanban', 'release Kanban', 'burn-up chart', 'daily stand-up', 'maintenance outsourcing', 'how many maintenance people'."
---

# devops-maintenance-operations

## Purpose

Maintenance is the dominant expense of the entire software industry — and Capers Jones observes that maintenance outsourcing is more successful than development outsourcing because aging software is less prone to catastrophic project risks. Where `developer-maintenance` handles the code-side (renovate, fix, remove error-prone modules), this skill handles the operations-side: ITIL-aligned change response, Release Kanban flow visualization, daily stand-up coordination, response-time tracking, maintenance-staff sizing.

## When this skill applies

- A maintenance operations function is being stood up or audited.
- Response-time SLAs for defect repair and change requests need defining.
- Maintenance outsourcing vs in-source is being decided.
- Release Kanban / burn-up tracking is being set up.
- Daily stand-up cadence is being designed.
- Maintenance staffing is being sized (maintenance specialists are the largest single software-staff specialty; the operational fraction of that).

## Formal criteria

A maintenance-operations pass is acceptable only if all of the following hold:

1. **23 maintenance work types acknowledged** — the operational side coordinates across all 23 types; Developer handles the code work. The operations side names which work types fall to outsource, in-source, or hybrid (cross-link `developer-maintenance` for the canonical list).
2. **ITIL framework referenced** — ITIL is a relevant practitioner framework for change management, reliability, and availability; it is not this skill's governing body of knowledge.
3. **The 14+ legacy best practices coordinated** — maintenance specialists vs developers; renovation workbenches; formal change management procedures + tools; formal regression test libraries; complexity analysis; error-prone module ID; dead code ID; renovate-before-enhance; inspections on major updates; customer-defect tracking; response-time tracking (defect repair AND change-request completion); cost tracking; warranty tracking; availability tracking.
4. **Response-time tracking in place** — two distinct metrics: time from submission to defect repair, and time from submission to change-request completion. SLAs declared.
5. **Release Kanban for flow visualization** — a three-column board: PBIs To Do (highest priority at top) / PBIs In Progress / PBIs Delivered. Snapshot updated at iteration end.
6. **Release Burn-Up Chart for progress** — accumulated delivered points over time vs total scope. Communicates progress in a single chart.
7. **Daily stand-up coordination** — daily fluid communication across the maintenance team and adjacent functions.
8. **Outsourcing decision documented** — maintenance outsourcing has fewer failures and litigation cases than development outsourcing. The decision is recorded with rationale.
9. **Maintenance-quality multiplier honored** — every ~120 delivered defects fewer ≈ 1 maintenance FTE saved; every ~240 ≈ 1 customer-support FTE saved. Operations sizing is partly a function of upstream quality.

## How you proceed

1. **Audit existing maintenance ops.** Which of the 23 work types is the org actually handling? Which are unstaffed? Which fall through the cracks?
2. **Decide the in-source / outsource split.** Strategic legacy + privileged-data → in-source. Non-strategic + commodity → outsource is empirically successful.
3. **Stand up the Release Kanban.** Three columns; PBIs sized in points; highest priority at top of To Do. Refresh at iteration boundary.
4. **Build the Burn-Up Chart.** Cumulative delivered vs total scope plotted over iterations. Update at iteration end.
5. **Schedule the daily stand-up** for the maintenance team. ≤15 min; what was done yesterday / what is being done today / blockers.
6. **Set SLAs** for defect-repair time and change-request-completion time. Communicate to Product Manager + customers.
7. **Set up the 14-practice tracking** (defects by customer, response time to repair, response time to CR completion, maintenance activities + costs, warranty costs, software availability).
8. **Size the team** against the maintenance-staff ratio + the ~120-defect multiplier (fewer delivered defects = less maintenance staff needed).
9. **Cross-coordinate** with `developer-maintenance` (code work), `devops-post-release-change` (renovation tool work), `devops-customer-support` (defect-flow from support intake).

## Pitfalls to avoid

- **Maintenance as one bucket.** 23 work types with different effort drivers. Aggregate "maintenance" budgets are reliably wrong.
- **No response-time tracking.** Both defect-repair and CR-completion times need explicit SLAs and measurement. Without them, customer dissatisfaction grows invisibly.
- **No flow visualization.** Without a Release Kanban + Burn-Up, progress is invisible until a release crisis surfaces it.
- **Daily stand-up as status meeting.** ≤15 min; coordination, not reporting. Long stand-ups burn time.
- **Outsourcing strategic legacy.** Outsourcing is supported for non-strategic maintenance; strategic / privileged-data systems are not appropriate.
- **Ignoring the ~120-defect multiplier.** Maintenance staffing is partly a function of upstream quality. Operations sizing should surface the quality-investment trade-off to Product Manager.
- **Security patches treated as ordinary maintenance work.** Security patches against critical CVEs have their own urgency tier: expedited update outside the regular maintenance cadence, with the release security gate (`security-officer-security-program`) reapplied. Dispatch `security-officer-threats-and-defenses` for CVE triage (severity, exploitability, exposure); cross-link `developer-maintenance` for the patch implementation. Treating a critical security CVE as "next maintenance window" extends the exposure window unacceptably.
- **Adopting a service-management framework as authority.** ITIL / COBIT / SRE are useful practitioner conventions for the operational aspects, not this skill's governing body of knowledge.
