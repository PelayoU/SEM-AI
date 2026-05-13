---
name: developer-coding-practices
description: "Apply Capers Jones's 13 programming best practices when writing new code — language selection, structured programming, certified reuse, security in code, complexity ceilings (cyclomatic <10 safe, >20 dangerous), clear comments, static analysis, TDD, formal code inspections, re-inspection after change, legacy renovation, error-prone module removal. Use whenever the human is about to write new code, picking a programming language for a new module or module set, deciding whether to refactor a module that has crossed a complexity ceiling, applying secure coding practices, or designing the code-author cadence for the project (TDD vs test-after, pair vs solo). Triggers include phrases like 'how should we code this', 'pick a language', 'cyclomatic complexity', 'code style', 'pair programming', 'TDD', 'test-first', 'secure coding', 'should we refactor', 'spaghetti code', 'self-review'."
---

# developer-coding-practices

## Purpose

Jones (BP #28, p. 107) frames programming as a *manual and error-prone activity* that places software *"among the most expensive of all human-built products"* — closer to custom racing yachts (10× normal yachts) or Indy cars (100× sedans) than to assembly-line production. The thirteen best practices Jones inventories are the empirical guard against the failure modes that drive that cost. This skill lets the Developer apply them deliberately when writing new code, so each module ships with the prevention layer (language fit, structure, complexity ceiling, security awareness) and the early-removal layer (static analysis, TDD, code inspection) already engaged.

## When this skill applies

- A new module / package / service is starting and language + structure must be chosen.
- Code is being audited and the question is which best practices are missing.
- Cyclomatic complexity has crossed a threshold and refactor-vs-test decision is open.
- A team is debating pair programming vs solo + inspection + static analysis.
- Security-relevant code is being written and the language / pattern choice matters.
- TDD adoption is being decided for new development.

## Formal criteria

A coding pass is acceptable only if all of the following hold:

1. **13 Best Practices walked for the work in scope** *(Jones BP #28, p. 108)*. For each, the work either applies the practice or marks it not applicable with one-line reason:
   1. **Selection of programming language to match application needs.** From >700 candidates; typical large applications combine 3–15 languages.
   2. **Utilization of structured programming practices** for procedural code.
   3. **Selection of reusable code from certified sources before starting to code** (cross-link `developer-reuse-application` + `architect-reuse-certification`).
   4. **Planning for and including security topics in code**, including secure languages such as E where appropriate.
   5. **Avoidance of "spaghetti bowl" code.** No deeply nested control flow or tangled goto-equivalents.
   6. **Minimizing cyclomatic complexity and essential complexity.** Working ceilings: <10 safe, 10–20 caution + refactor candidate, >20 dangerous + must refactor before test.
   7. **Including clear and relevant comments in the source code.** Comment density: cover non-obvious decisions, public API contracts, complexity-justified algorithms; do not narrate trivial code.
   8. **Using automated static analysis tools for Java and dialects of C** (and other supported languages). Cross-link `developer-static-analysis`.
   9. **Creating test cases before or concurrently with the code** (TDD / test-first when methodology supports it; concurrent test design when not).
   10. **Formal code inspections of all modules.** Cross-link `qa-inspections-program`. Average DRE 65–85%, peak 88%.
   11. **Re-inspection of code after significant changes or updates.** Bad-fix injection rate ~5% average; re-inspection catches them (Table 9-22 #21: 70% DRE).
   12. **Renovating legacy code before starting major enhancements.** Cross-link `developer-maintenance`.
   13. **Removing error-prone modules from legacy code.** ~5% of modules cause ~50% of defects; surgical removal is the leverage point.
2. **Complexity ceiling enforced** *(Jones BP #28 + Ch 8)* — modules above cyclomatic complexity ~10 are flagged for refactor; modules above ~20 are refactored before being shipped or inspected. Essential complexity is checked alongside cyclomatic; both metrics are reported.
3. **Reuse-before-custom rule** *(Jones BP #28 p. 109)* — before custom-coding any module, check the certified reuse library (cross-link `developer-reuse-application`). Custom-coding is the most expensive option; certified reuse offers the highest ROI of any known technology.
4. **Self-review is complementary, not substitutive** *(Jones BP #28 p. 108)* — "people do not find their own errors with high efficiency, primarily because they think many errors are correct and don't realize that they are wrong." Inspection / static analysis / pair review by a different person is mandatory before code is considered done.
5. **Pair programming is not the entire quality strategy** *(Jones BP #28 p. 108)* — Jones is explicit: pair programming has "anecdotal evidence" of higher quality but is "intrinsically inefficient"; solo development + static analysis + peer review reaches "better than average quality at somewhat lower costs." Pair programming as the only review mechanism is suboptimal.

## How you proceed

1. **Confirm the parent feature has INVEST-passing stories and a Gherkin spec** (cross-link `po-feature-decomposition` + `po-spec-gherkin`). Coding above shaky stories propagates ambiguity.
2. **Confirm Architect decisions are in place** (cross-link `architect-architecture-design`). Architectural style, decomposition, design notation, performance + security budgets are inputs to coding decisions, not afterthoughts.
3. **Pick or confirm the programming language(s)** (practice 1). Use Jones's 5-axis suitability matrix (cross-link `architect-methodology-selection`) at language scope: size of code involved, application type, application nature (new / replacement / maintenance), attribute fit (especially security and performance), activity fit. Multiple languages are normal for large applications.
4. **Walk the prevention layer.** Structured programming (practice 2). Certified reuse check (practice 3 + cross-link). Security planning (practice 4). Spaghetti-bowl avoidance (practice 5). Complexity ceilings (practice 6).
5. **Walk the documentation + tooling layer.** Comments at the right density (practice 7). Static analysis configured for the language (practice 8 + cross-link). Test cases concurrent or first (practice 9; cross-link `developer-unit-testing`).
6. **Walk the removal layer.** Schedule code inspection (practice 10). Plan re-inspection after change (practice 11).
7. **Walk the legacy layer** if applicable. Renovation before enhancement (practice 12 + cross-link `developer-maintenance`). Error-prone module surgical removal (practice 13).
8. **Re-evaluate after each major refactor.** Complexity metrics, defect-density per module, test coverage. Cross-link `qa-measurements` for the metric definitions.

## Pitfalls to avoid

- **Custom-coding before checking the reuse library.** Most expensive default. Cross-link `developer-reuse-application`.
- **Cyclomatic complexity treated as a soft warning.** Above 10, refactor before test. Above 20, refactor before inspect. Soft thresholds become hard problems at maintenance time.
- **Self-review as the only review.** Jones is explicit (BP #28 p. 108) it does not work.
- **Pair programming as the entire strategy.** Adds cost; does not replace static analysis or formal inspection (BP #28 p. 108).
- **Testing without inspection + static analysis.** Cumulative testing-only <80% DRE; safe minimum 95% requires the stack (cross-link `qa-defect-removal-efficiency`).
- **Skipping renovation before major enhancement of legacy code.** Inherits the legacy's complexity and error-prone modules.
- **Treating static-analysis output as cosmetic.** The ~87% DRE figure refers to real defect detection (boundary, calls, links). Ignoring it loses one of the highest-leverage prevention + removal activities.
- **Mixing too many languages without taxonomy.** 12–15 languages in one application is observed in Jones's data (BP #28 p. 108) but increases integration defects and onboarding cost. Justify each language choice.
- **Comments at trivial density.** Cargo-cult commenting ("// increment i") is noise; absent commenting on non-obvious decisions is debt. Density follows non-obviousness, not line count.
- **Adopting fashionable practices from out-of-bibliography sources as authority.** Robert C. Martin Clean Code, GoF design patterns, SOLID — useful as convention; not in audited `bibliography/sources/`. Cite Jones; reference these as practitioner convention.

## Source

- **Best Practice #28 — *Programming or Coding* (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, pp. 107–109).** 13 state-of-the-art coding practices; >700-language inventory; manual-and-error-prone framing; custom-coding cost analogy (10× yachts, 100× Indy cars); pair-programming evaluation (anecdotal +; intrinsically inefficient); self-review-does-not-work; reusable-objects-are-the-leverage-point.
- **Chapter 8 § *Forms of Programming Defect Prevention* (Jones 2010, pp. 519–525).** Code reuse as defect prevention (certified ~1/100th defect rate); patterns as defect prevention (~50% reduction for inexperienced developers); inspections as defect prevention (~80% reduction after participation); automated static analysis as defect prevention (~85%+ DRE; ~50 of 2,500 languages supported; ~100 tools).
- **Chapter 9 Table 9-22** — Refactoring of code: 62% DRE (#25); error-prone module analysis: 60% DRE (#26).
- **Cross-references**: BP #36 inspections (depth in `qa-inspections-program`), BP #37 testing (depth in `developer-unit-testing` + `qa-testing-strategy`), BP #26 reuse (depth in `architect-reusability-strategy` + `developer-reuse-application`), BP #48 maintenance (depth in `developer-maintenance`).
- Out-of-bibliography (convention pointers only): SPR language taxonomy (www.SPR.com, referenced by Jones BP #28 p. 108), Robert C. Martin Clean Code, Gamma et al. GoF patterns, SOLID principles, Beck Extreme Programming Explained, McConnell Code Complete.
- Full traceability: `bibliography/skill-references.md` § `developer-coding-practices`.
