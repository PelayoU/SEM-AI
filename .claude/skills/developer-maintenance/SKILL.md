---
name: developer-maintenance
description: "Maintain and enhance legacy code under Capers Jones BP #48's 23-work-type taxonomy (enhancements, defect repairs, complexity analysis, dead-code removal, error-prone-module surgery, refactoring, renovation, migration, conversion, retirement, etc.) and the 14+ legacy best-practice inventory (maintenance specialists, renovation workbenches, formal change management, regression-test libraries, complexity analysis, error-prone-module identification, dead-code identification, renovate-before-enhance rule). Use whenever about to enhance or repair a legacy module, planning a major release on aging code, deciding whether to refactor before enhancing, identifying error-prone modules, removing dead code, or planning legacy retirement / migration. Triggers include phrases like 'maintain this', 'enhance the legacy', 'refactor before adding', 'dead code', 'error-prone module', 'renovate before', 'why is this code so buggy', 'legacy enhancement', 'should we rewrite', 'migration', 'retire the legacy app'."
---

# developer-maintenance

## Purpose

Maintenance is the dominant expense of the entire software industry (Jones BP #48 p. 163) yet "maintenance" hides 23 different kinds of work (BP #48 pp. 161–162). Without taxonomy, the team confuses defect-repair with enhancement, dead-code removal with refactoring, migration with conversion — and prices, plans, and executes the wrong thing. This skill lets the Developer handle legacy work explicitly: classify against the 23-type inventory, apply the renovate-before-enhance rule, surgically remove error-prone modules (~5% of modules cause ~50% of defects), and choose maintenance specialists over generalists when the catalog allows.

## When this skill applies

- A defect repair, minor enhancement, or major enhancement on an existing application.
- A release plan on legacy code where renovation may be needed before the work.
- A defect investigation reveals an error-prone module (high complexity + high defect history).
- Dead code or dormant applications are suspected to consume effort without value.
- A migration / conversion / refactoring / retirement decision is open.
- A maintenance outsourcing or in-source decision is open.
- ITIL or similar service-management framework is being adopted.

## Formal criteria

A maintenance pass is acceptable only if all of the following hold:

1. **Work classified against the 23-type taxonomy** *(Jones BP #48 pp. 161–162)* — the work is named as one (or a coherent combination) of:
   1. Major enhancements (new features >50 FP).
   2. Minor enhancements (new features <5 FP).
   3. Maintenance (defect repairs for good will).
   4. Warranty repairs (defect repairs under contract).
   5. Customer support (phone / problem-report response).
   6. Error-prone module removal.
   7. Mandatory changes (statutory / regulatory).
   8. Complexity / structural analysis.
   9. Code restructuring (reducing cyclomatic and essential complexity).
   10. Optimization (performance / throughput).
   11. Migration (one platform to another).
   12. Conversion (interface / file structure changes).
   13. Reverse engineering (extracting latent design from code).
   14. Reengineering / renovation (transforming legacy to modern).
   15. Dead code removal.
   16. Dormant application elimination.
   17. Nationalization.
   18. Mass updates (Euro, Year 2000, similar).
   19. Refactoring (clarity).
   20. Retirement (withdrawing from active service).
   21. Field service.
   22. Reporting defects to vendors.
   23. Installing vendor updates.
   Multiple types in one release is normal (Jones observed 6–10 simultaneous in large applications, p. 162).
2. **Renovate-before-enhance rule respected** *(Jones BP #48 p. 163 + BP #28 p. 108 practice 12)* — for major enhancements on aging legacy applications, perform renovation / refactoring + error-prone-module removal before the enhancement. Enhancing unrenovated legacy inherits its complexity and defect debt.
3. **14+ legacy best practices walked** *(Jones BP #48 p. 162–163)* — for each:
   1. Use maintenance specialists rather than developers (when distinction matters at scale).
   2. Consider maintenance outsourcing to specialized maintenance companies.
   3. Use maintenance renovation workbenches.
   4. Use formal change management procedures (cross-link `po-change-control`).
   5. Use formal change management tools.
   6. Use formal regression test libraries.
   7. Perform automated complexity analysis of legacy applications.
   8. Search out and eliminate all error-prone modules.
   9. Identify all dead code.
   10. Renovate or refactor applications prior to major enhancements.
   11. Use formal design and code inspections on major updates.
   12. Track all customer-reported defects.
   13. Track response time from submission to defect repair.
   14. Track response time from submission to change-request completion.
   15. Track all maintenance activities and costs.
   16. Track warranty costs for commercial software.
   17. Track availability of software to customers.
4. **Error-prone-module rule** *(Jones BP #48 p. 163 + Table 9-22 #26)* — "less than 5 percent of the modules in large systems will receive more than 50 percent of defect reports." These modules are usually unfixable; surgical removal + replacement is the normal therapy. Error-prone module analysis 60% DRE on the defect concentration.
5. **Maintenance-quality multiplier** *(Jones BP #48 p. 163 + BP #35 p. 123)* — every reduction of 120 delivered defects ≈ one fewer maintenance staff person; every 240 ≈ one fewer customer-support staff person. Pre-release quality investment compounds in maintenance savings.
6. **Outsourcing rule** *(Jones BP #48 p. 163)* — maintenance outsourcing is more successful than development outsourcing in Jones's data. Development outsourcing ends up in litigation ~5% of contracts; maintenance outsourcing far fewer. Consider for non-strategic legacy.
7. **ITIL referenced for service-management aspects** *(Jones BP #48 p. 162)* — change management, reliability, availability, daily-use customer issues. ITIL is mentioned by Jones as a relevant framework but is not in audited bibliography; cite Jones for the principle, ITIL as practitioner convention.

## How you proceed

1. **Classify the work** against the 23 types. Multiple-type combinations are normal; name each. The classification drives estimation (`po-cost-estimating`), planning (`po-project-planning`), and tooling.
2. **Run complexity analysis on the affected modules** (practice 7). Cyclomatic + essential complexity. Modules above ceiling (10 / 20) are flagged for refactor before enhancement.
3. **Identify error-prone modules in the impacted area** (practice 8). The 5% / 50% rule: ranked defect history per module surfaces the candidates. Surgical removal + replacement is the working response.
4. **Identify dead code** (practice 9). Static analysis + execution tracing. Remove rather than route around.
5. **Apply the renovate-before-enhance rule** for major enhancements (practice 10). Renovation work runs first; the enhancement follows on cleaner ground.
6. **Schedule formal inspections on major updates** (practice 11 + cross-link `qa-inspections-program`). Bad-fix injection rate ~5% (Table 9-22); re-inspection catches it.
7. **Maintain the regression test library** (practice 6). The library is itself an artifact — apply test-library hygiene rules from `developer-unit-testing`.
8. **Track the operational metrics** (practices 12–17). Defect-by-customer logs, defect-to-repair time, change-request-to-completion time, maintenance cost, warranty cost, availability. Feed `qa-measurements`.
9. **Decide outsourcing or in-source** (practice 2). For non-strategic legacy, outsourcing has better historical outcomes. For strategic legacy or systems with concentrated domain knowledge, in-source.
10. **For retirement / migration / conversion**, treat as a separate effort with its own estimation + plan + risk register. These are not "small maintenance."

## Pitfalls to avoid

- **Treating "maintenance" as one thing.** 23 work types with different effort drivers, different ownership, different acceptance criteria. Aggregate "maintenance bucket" estimates are reliably wrong.
- **Enhancing unrenovated legacy.** The enhancement inherits the legacy's complexity and error-prone modules. Net cost > renovation + enhancement done separately.
- **Patching error-prone modules instead of replacing.** Jones (p. 163): error-prone modules are usually unfixable; surgical removal + replacement is the therapy. Repeated patches keep the defect concentration.
- **Skipping complexity analysis on legacy.** Aging applications drift up in complexity ~8%/year (general software-growth rate per Jones Ch 7). Without analysis, the team works on the wrong modules.
- **Skipping dead-code analysis.** Dead code consumes inspection + test + maintenance effort with zero functional value.
- **Maintaining without regression test library.** Each fix risks regressing prior work; without a library the risk is invisible.
- **Single inspector for "major update".** Bad-fix injection ~5% (Table 9-22). Re-inspection is part of the work, not an optional polish.
- **Maintenance outsourcing of strategic legacy.** Jones (BP #48 p. 163) supports maintenance outsourcing in general but not for systems with concentrated domain knowledge; surface the strategic-vs-non-strategic distinction before deciding.
- **ITIL as authority.** ITIL is referenced by Jones (p. 162) but not in audited bibliography. Cite Jones for the principle; ITIL is practitioner convention.

## Source

- **Best Practice #48 — *Software Maintenance and Enhancement* (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, pp. 161–164).** 23 work-type taxonomy; 14+ legacy best-practice inventory; renovate-before-enhance rule; error-prone-module rule (5% modules / 50% defects, surgical removal); maintenance-quality multiplier (120 defects ≈ 1 FTE, 240 ≈ 1 customer-support FTE); ITIL reference (p. 162); maintenance-outsourcing success rate vs development outsourcing.
- **Best Practice #28 — *Programming or Coding* (Jones 2010, pp. 107–109)** — practice 12 (renovate legacy before enhancement); practice 13 (error-prone module removal).
- **Best Practice #47 — *Software Change Management After Release* (Jones 2010, p. 160)** — 10-tool list for post-release change (complexity analysis, static analysis, error-prone module ID, dead code ID, data mining, code conversion, renovation workbenches). Cross-link `devops-post-release-change` (M5).
- **Chapter 5 Table 5-2** — referenced by catalog as the 23 forms-of-maintenance source; replicated in BP #48 pp. 161–162 text.
- **Chapter 9 Table 9-22** — Refactoring of code: 62% DRE (#25). Error-prone module analysis: 60% DRE (#26). Legacy code inspections: 83% DRE (#10).
- **Cross-references**: `developer-coding-practices` (practices 12–13 specifically); `qa-inspections-program` (re-inspection after change); `po-change-control` (formal change management procedures); `po-cost-estimating` (separate estimation for the 23 work types); `developer-unit-testing` (regression test library hygiene).
- Out-of-bibliography (convention pointers only): ITIL v3 / v4 service management framework, COBIT, Relativity Technologies renovation workbench (named in Jones p. 163 but the product itself not in `sources/`).
- Full traceability: `bibliography/skill-references.md` § `developer-maintenance`.
