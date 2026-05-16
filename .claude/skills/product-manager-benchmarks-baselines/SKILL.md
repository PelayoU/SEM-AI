---
name: product-manager-benchmarks-baselines
description: "Establish and compare against software benchmarks (cross-organization comparisons against ISBSG-class historical data) and baselines (organization-internal quality and productivity snapshots) using Capers Jones's 25-topic full-benchmark inventory and 10-topic partial-benchmark short form. Use whenever an estimate needs historical defense, when a process-improvement initiative needs a starting baseline, when comparing the team's performance against industry norms, or after a release closes and the data must be captured for the next project's calibration. Triggers include phrases like 'benchmark', 'baseline', 'industry comparison', 'how do we compare', 'ISBSG', 'historical data', 'productivity rate', 'defect removal efficiency', 'are we any good at this', 'post-release data'."
---

# product-manager-benchmarks-baselines

## Purpose

Every major project should start by reviewing available benchmark information from ISBSG or other sources, and every process-improvement plan should start by creating a quantitative baseline against which progress can be measured. Yet most teams skip both. This skill lets the Product Manager establish baselines at project start, capture benchmark data at release close, and use both as the empirical defense layer for `product-manager-cost-estimating` and `product-manager-risk-analysis`. Without benchmarks, estimates are political fictions; without baselines, process-improvement is rhetoric.

## When this skill applies

- A new project is starting and needs reference data from comparable applications.
- An estimate is being challenged and needs historical defense.
- A process-improvement initiative is launching and needs a quantitative baseline.
- A release closed and the benchmark data must be captured before the team forgets the numbers.
- The team is asked to compare productivity, defect potentials, or schedule against industry norms.

## Formal criteria

A benchmark or baseline pass is acceptable only if all of the following hold:

1. **Term used precisely** — a *benchmark* compares a project or organization against similar projects from other companies; a *baseline* is a snapshot of quality and productivity at a specific time, used to evaluate progress during process improvement. Do not conflate.
2. **Function-point metrics, not LOC** — both ISBSG and Jones express data in function points (IFPUG and COSMIC variants supported). LOC-only metrics are not usable for cross-language comparison.
3. **Full benchmark covers the 25 topics, partial covers the 10** —
   **Full (on-site, ~2 days):**
   1. Industry codes (e.g., NAIC).
   2. Development countries and locations.
   3. Application taxonomy (nature, scope, class, type).
   4. Complexity (problem, data, code).
   5. Application size in function points.
   6. Application size in logical source code statements.
   7. Programming languages used.
   8. Amount of reusable material.
   9. Ratio of LOC to function points.
   10. Development methodology (Agile, RUP, TSP, …).
   11. Project management and estimating tools used.
   12. Capability maturity level (CMMI).
   13. Chart of accounts for development activities.
   14. Activity-level productivity in FP.
   15. Overall net productivity in FP.
   16. Cost data in FP.
   17. Overall staffing.
   18. Number and kinds of specialists employed.
   19. Overall schedule.
   20. Activity schedules (development, testing, documentation, …).
   21. Defect potentials by origin (requirements, design, code, documents, bad fixes).
   22. Defect removal activities used (inspections, static analysis, testing).
   23. Number of test cases created.
   24. Defect removal efficiency levels.
   25. Delays and serious problems noted.

   **Partial (remote / web survey, ~2–3 hours):** topics 5, 8, 10, 12, 15, 16, 17, 19 plus delays/serious problems and customer-reported bugs.
4. **ISBSG cross-check or explicit gap statement** — ISBSG holds ~5,000 projects (growing ~500/year) but is heavily weighted toward IT and web applications; military, embedded, systems software, classified military, and applications above 10,000 FP are sparse or absent. The pass states whether ISBSG covers the class or notes the gap.
5. **Validation discipline matched to source** — full on-site benchmarks include validation interviews with managers and team. ISBSG self-submission has no formal validation; account for that uncertainty when citing ISBSG comparisons.
6. **Function-point counting cost respected** — full FP counting is slow (~400 FP/day). For >10,000-FP applications use the high-speed methods (pattern matching, light FP analysis) rather than skipping the FP metric.

## How you proceed

1. **Decide whether you need a benchmark or a baseline.** External comparison → benchmark. Internal progress snapshot for SPI → baseline. Same 25 topics, different use.
2. **Pick full or partial.** Below the resources for a full ~2-day on-site collection, use the 10-topic partial via remote / survey. Recognize the limitation: partial benchmarks lack the granularity for a full and complete statistical analysis.
3. **Locate the source.**
   - **External (benchmark)**: ISBSG remote dataset; in-house cross-project repository; commercial benchmark consulting (David Consulting Group, Software Productivity Research, Galorath, etc.).
   - **Internal (baseline)**: own historical project data; current snapshot.
4. **Collect the 25 (full) or 10 (partial) topics.** For full benchmarks, the canonical method is on-site, ~2 days, interviews with the PM and ~6 team members. For partial benchmarks, the data can be self-reported within 2–3 hours after the application is complete.
5. **Validate where possible.** Cross-check the FP count with another method (high-speed FP); confirm defect counts against the QA defect log; sanity-check schedules against the project plan and milestone log.
6. **State the class and ISBSG coverage.** If the application class (military classified, embedded niche) is sparsely covered by ISBSG, note it so downstream consumers do not over-trust the comparison.
7. **Use the benchmark as defense for estimates and risk analysis.** Benchmarks are perceived as being more real than estimates — make this defense explicit when stakeholders push back on cost or schedule. Depth in `product-manager-cost-estimating`.
8. **Use baselines to track process improvement.** A baseline taken pre-SPI vs post-SPI on the same 25 topics shows real progress; an SPI without quantitative baseline cannot demonstrate value.
9. **Feed organizational learning.** Each release's benchmark feeds the next release's baseline. Continuous capture is cheap; one-shot capture is expensive and rarely happens.

## Pitfalls to avoid

- **Conflating benchmark and baseline.** They serve different decisions. Cross-organization comparison is benchmark; internal progress is baseline.
- **LOC-only data.** Cross-language comparison collapses with LOC. Use FP; cite LOC only as a secondary metric.
- **Trusting ISBSG self-submission without caveat.** No formal validation; obvious errors corrected, subtler ones may not be. Useful as overall productivity reference, weaker for quality data.
- **Skipping the FP count because it's slow.** Use the high-speed FP methods — pattern matching, light FP analysis — rather than abandoning FP for LOC.
- **Partial benchmark presented as full.** The 10-topic partial cannot support the regression analysis a 25-topic full benchmark can. State which form was used.
- **No baseline before SPI.** Process improvement without a baseline cannot show progress; you spent the budget and have no evidence.
- **One-shot benchmark, never updated.** Empirical reference data ages. Capture at every release boundary, not just at project end.
