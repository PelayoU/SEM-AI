---
name: devops-post-release-change
description: "Manage software change after release using Capers Jones BP #47's 10-tool inventory for legacy renovation (complexity analysis, static analysis, error-prone module ID, dead code ID, data mining, code conversion, FP enumeration, renovation workbenches, automated test generation, test coverage analysis) — recognizing that post-release change management is empirically less rigorous than pre-release, that specs go stale, comments outdate, complexity creeps, and dead code accumulates. Use whenever a post-release change is being planned, when a long-lived application's specs are out of sync with code, when complexity has crept above ceilings, when planning a renovation cycle, or when tool-supported analysis of legacy code is needed before a major release. Triggers include phrases like 'post-release change', 'after-release', 'specs are out of date', 'complexity creep', 'renovation', 'legacy refresh', 'static analysis legacy', 'data mining business rules', 'extract algorithms', 'renovation workbench'."
---

# devops-post-release-change

## Purpose

Jones (BP #47 p. 160) observes that *"postrelease change management is often less rigorous than change management prior to the initial release."* Configuration control of code may continue, but specifications go stale, comments outdate, complexity creeps, dead code accumulates. After ~5 years of usage the application no longer has a full set of specifications, and updates depend on long-tenure maintenance staff's tribal knowledge. This skill lets DevOps run the post-release change function with the same rigor as pre-release: tool-supported renovation, business-rule extraction, error-prone-module surgery. The toolset Jones names (BP #47 p. 160) is the operational baseline.

## When this skill applies

- A post-release change is being planned and the team must decide between in-place patch and renovation.
- A long-lived application is being audited and the specs are years out of sync with the code.
- Complexity creep has crossed ceilings (>10 cyclomatic) on many modules.
- A major release on legacy code is being planned (cross-link `developer-maintenance`).
- Replacement is being considered and business-rule extraction from legacy is required first.
- Tool selection for renovation workbench / static analysis / data mining is open.

## Formal criteria

A post-release change pass is acceptable only if all of the following hold:

1. **Same rigor as pre-release change** *(Jones BP #47 p. 160)* — configuration control continues, specifications kept current, code comments updated, complexity tracked. Less-rigorous post-release change is the observed default; it is not acceptable.
2. **Tool inventory applied** *(Jones BP #47 p. 160)* — for the legacy application under change, evaluate each of:
   1. **Complexity analysis tools** illustrating all paths and branches.
   2. **Static analysis tools** finding bugs in legacy code (supported languages).
   3. **Static analysis tools** identifying error-prone modules for surgical removal.
   4. **Static analysis tools** identifying dead code for removal or isolation.
   5. **Data mining tools** extracting algorithms and business rules from code.
   6. **Code conversion tools** converting legacy languages to modern (Java, etc.).
   7. **Function point enumeration tools** calculating legacy application sizes.
   8. **Renovation workbenches** assisting with changes to existing software.
   9. **Automated testing tools** creating new test cases from code analysis.
   10. **Test coverage tools** showing gaps in current test libraries.
3. **Inspection of legacy artifacts when current** *(Jones BP #47 p. 161)* — formal inspections of source code, test libraries, and other artifacts assuming the artifacts are kept current. If artifacts are stale, inspect after renovation, not before.
4. **Renovate-before-enhance discipline** *(Jones BP #47 p. 161 + BP #48 + BP #28 practice 12)* — major enhancements on poorly structured legacy are not cost-effective; analyze structure first, renovate, then enhance.
5. **Cross-coordinated with Developer maintenance work** — Developer handles the code-level changes (cross-link `developer-maintenance`); DevOps handles the tool selection, deployment of renovated artifacts, and operational coordination across the change.
6. **Cross-coordinated with configuration control** (cross-link `devops-configuration-control`) — every renovation change goes through formal CM; locked masters apply post-release too.

## How you proceed

1. **Audit the artifact state.** Specs current? Comments current? Complexity measured? Dead code mapped? Test coverage known? Most legacy applications fail multiple of these.
2. **Apply complexity analysis** (tool 1). Map all paths + branches. Cyclomatic / essential complexity per module. Flag above-ceiling modules.
3. **Apply static analysis** (tools 2–4). Find bugs, identify error-prone modules (5% / 50% rule per BP #48), identify dead code.
4. **Apply data mining** (tool 5) if specs are stale or if replacement is being considered. Extract business rules and algorithms from code; carry them forward.
5. **Apply FP enumeration** (tool 7) to size the legacy application properly. Most legacy applications have been operating without a current FP count; estimation works better with one.
6. **Apply renovation workbench** (tool 8) for guided change. Tools named by Jones include Relativity Technologies' workbench (p. 163).
7. **Apply automated test generation + coverage analysis** (tools 9–10) to backfill the test library that legacy applications typically lack.
8. **Sequence**: renovation first, then the post-release change rides on the renovated baseline. Cross-link `developer-maintenance` for the actual code changes.

## Pitfalls to avoid

- **Patching unrenovated legacy.** Inherits the legacy's complexity + error-prone modules. Net cost > renovation + patch separately.
- **Specs left to rot.** After ~5 years specs no longer match code (BP #47 p. 160). Either keep them current via post-release CM or accept that the next replacement project starts with data mining from code.
- **Tool inventory cherry-picked.** All 10 tools have specific purposes; using only static analysis without data mining or renovation workbench misses the leverage of the combination.
- **Inspection of stale artifacts.** Inspection on outdated specs / tests inspects fiction. Renovate first, inspect after.
- **Tribal-knowledge dependency.** Depending on long-tenure maintenance staff for legacy knowledge (BP #47 p. 160) creates key-person risk. Data mining + documentation refresh during renovation reduces it.
- **Tool brand as authority.** Specific products (Relativity Technologies, SonarQube, etc.) are convention; Jones BP #47 + #48 are the anchored authority for the tool *categories*.

## Source

- **Best Practice #47 — *Software Change Management After Release* (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, pp. 160–161).** "Less rigorous than pre-release" observation; spec-staleness empirics (~5 years); 10-tool renovation inventory; inspection-after-renovation rule; recession-context economic argument for keeping legacy running.
- **Best Practice #48 — *Maintenance and Enhancement* (Jones 2010, pp. 161–164)** — 23 maintenance work types; error-prone module 5%/50% rule; renovation workbench (Relativity Technologies cited).
- **Best Practice #28 — *Programming or Coding* (Jones 2010, p. 108)** — practice 12 (renovate before enhance).
- **Chapter 9 Table 9-22** — Complexity analysis tools, static analysis, error-prone module analysis, refactoring DRE numbers (cross-link `qa-defect-removal-efficiency`).
- **Cross-references**: `developer-maintenance` (code-side of legacy work), `devops-configuration-control` (post-release CM), `devops-maintenance-operations` (operational side), `product-manager-change-control` (CR pipeline applies post-release too).
- Out-of-bibliography (convention pointers only): Relativity Technologies renovation workbench (named in Jones p. 163, product spec not in `sources/`), SonarQube / Coverity / Understand legacy-analysis tooling.
- Full traceability: `bibliography/skill-references.md` § `devops-post-release-change`.
