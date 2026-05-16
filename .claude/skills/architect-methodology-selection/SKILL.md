---
name: architect-methodology-selection
description: "Select a software development methodology (or methodology mix) for a project by evaluating candidates against Capers Jones's five-axis suitability matrix: size, application type, application nature, quality attribute, and lifecycle activity. Use whenever the human asks 'Agile or waterfall?', 'should we use TSP / RUP / XP / Crystal / DSDM / pair programming / JAD / Six Sigma?', 'is this methodology right for our project size?', or wants to evaluate a methodology proposal against historical benchmarks before committing. Triggers include phrases like 'pick a methodology', 'Agile vs', 'development process', 'methodology selection', 'should we adopt X', 'is X right for us', 'TSP', 'RUP', 'XP', 'V-model', 'Lean Six Sigma'."
---

# architect-methodology-selection

## Purpose

Capers Jones observes that careful selection of methods, tools, and practices "seldom occurs in the software industry" — most teams inherit whatever was already in place or chase the latest fad. This skill lets the Architect run a structured five-axis suitability check (size / type / nature / attribute / activity) anchored in benchmark data, so the project picks a methodology empirically rather than fashionably, and surfaces hybrid combinations when no single methodology fits all axes.

## When this skill applies

- A new project is starting and the methodology is undecided.
- A team proposes adopting a methodology fashionable in the moment (latest Agile variant, the newest hybrid).
- A project on a methodology that no longer fits (e.g., Agile on a 100,000-FP system, waterfall on a 500-FP applet) needs reassessment.
- A regulatory or quality requirement forces methodology review (e.g., medical, defense, aviation).
- A hybrid combination is on the table and its coherence needs validation.

## Formal criteria

A methodology choice is acceptable only if all of the following hold:

1. **Benchmark-anchored, not fashion-driven** — the selection starts from benchmark data on similar applications (ISBSG or in-house). Jones is explicit: "either applications are developed using methods already in place, or there is rush to adopt the latest fad". Choosing because the methodology is trendy is the dominant failure mode.
2. **Five-axis suitability evaluated** —
   - **Size**: how the candidate performs from 10 FP to 100,000 FP. Agile works well small; TSP and RUP work well large.
   - **Type**: embedded / systems / web / IT / commercial / military / games / scientific.
   - **Nature**: new development / enhancements / warranty repairs / legacy renovation. The majority of "new" applications are really replacements for aging legacy applications — methodology must support legacy mining if so.
   - **Attribute**: defect prevention, defect removal efficiency, security vulnerability minimization, performance, user-interface excellence. A development method without quality control and quality measurement "is really unsuitable for critical software applications" (Jones).
   - **Activity**: requirements, architecture, design, code, reusability, pretest inspections, static analysis, testing, configuration control, QA, user information, post-release maintenance / enhancement / customer support.
3. **Candidate list is comprehensive** — the comparison covers the full methodologies (Agile, clean-room, Crystal, DSDM, XP, hybrid, iterative, OO, pattern-based, PSP, RAD, RUP, spiral, structured, TSP, V-model, waterfall) plus the partial methods used as components (code inspections, data-state design, design inspections, flow-based programming, JAD, Lean Six Sigma, pair programming, QFD, requirements inspections, Six Sigma for software).
4. **Hybrid is a valid output** — a coherent hybrid (e.g., TSP-for-process + JAD-for-elicitation + Gherkin-for-spec) is often better than any pure choice.
5. **Quality coverage validated** — the chosen methodology (or hybrid) includes both quality control and quality measurement. If it does not, the methodology fails the criterion regardless of how well it scores on the other axes.
6. **Lifecycle activity coverage validated** — the methodology must cover (or be supplemented to cover) all activities the project performs, including the often-omitted post-release activities (maintenance, enhancement, customer support).

## How you proceed

1. **Pull the project parameters.** Size in FP (from `product-manager-early-sizing`), application type, nature (new vs replacement), critical attributes (Cagan's four risks via `product-manager-risk-analysis` give hints), activity scope.
2. **Acquire benchmark data.** ISBSG remote benchmark for comparable applications + methodology. Cross-link to `product-manager-benchmarks-baselines`. Without benchmarks the selection is fiction.
3. **Build the five-axis scorecard.** Columns are candidate methodologies; rows are the five axes. For each cell, score on three levels (Strong fit / Adequate / Poor fit) with one-line rationale.
4. **Score the candidates.** No single candidate typically wins all five axes — that is the prompt to consider hybrids.
5. **Compose the hybrid if needed.** Combine a primary full methodology with partial methods to fill the gaps. Example: TSP for process discipline + JAD for elicitation + formal requirements inspections + Gherkin for acceptance contract + Lean Six Sigma for measurement.
6. **Validate quality coverage.** Walk the chosen methodology against quality prevention + quality measurement (axis 4). Add inspections / static analysis / metrics where the methodology is silent.
7. **Validate lifecycle activity coverage.** Walk the chosen methodology against the activity list. Most methodologies are weak on maintenance + post-release. Patch with explicit add-ons.
8. **Document the decision and the trade-offs.** Record what was rejected and why. Methodology choice is auditable; the rationale is part of the record.

## Pitfalls to avoid

- **Fashion-driven choice.** "Everyone is doing Agile" or "we should adopt SAFe because it's the new thing" is the failure mode Jones documents. Demand benchmark evidence before adoption.
- **Single-methodology purity for non-trivial projects.** Above ~1,000 FP, almost no project is well-served by a pure methodology. Hybrids are normal; deny them at your peril.
- **Skipping the legacy-replacement nature check.** ~80% of new applications are replacements. A methodology that does not support data mining of legacy applications is the wrong fit for the majority of projects.
- **No quality coverage.** A methodology silent on quality control and measurement fails axis 4 and is unsuitable for critical applications.
- **No post-release coverage.** Many methodologies cover initial delivery only. The project's maintenance + enhancement phase is years long; the methodology must cover it or be explicitly supplemented.
- **Hybrid without coherence.** Stacking five partial methods on top of a full methodology without integration produces process theatre. Each partial method must address a specific gap.
