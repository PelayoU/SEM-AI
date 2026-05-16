---
name: developer-reuse-application
description: "Apply already-certified reusable code, designs, or other artifacts when implementing a feature — pulling from the project's certified reuse library (curated by Architect) and respecting the strict hazard rule that uncertified reuse can produce the worst negative ROI in the industry. Use whenever the Developer is about to implement functionality that may already exist as a reusable artifact, evaluating whether a candidate library / class / pattern from the reuse catalog fits the current need, or pushing back on a request to use an uncertified reusable source. Triggers include phrases like 'can we reuse this', 'is there a library for', 'should we adopt this component', 'use the reuse library', 'plug in a reusable module', 'why can't we just use X', 'reusable design', 'reuse this pattern'."
---

# developer-reuse-application

## Purpose

Reuse is the highest-ROI lever in software (Jones BP #26, p. 100: +300% ROI for certified reuse) and the most negative when applied wrong (-300% for uncertified buggy reuse). Architect designs the reusability strategy (`architect-reusability-strategy`) and runs the certification gate (`architect-reuse-certification`); Developer is the *consumer* of the resulting reuse library. This skill operationalizes the consumer side: how to find the right reusable artifact for the work at hand, plug it in correctly, and refuse uncertified candidates that look attractive but are hazardous.

## When this skill applies

- Implementing a feature that overlaps with functionality already in the reuse library.
- A teammate or stakeholder proposes pulling a library / framework / class / module that is not in the certified library.
- A pattern or design is being applied and the question is whether the project has it already standardized.
- The reuse library lists a candidate whose fit for this case must be evaluated.
- An open-source / commercial dependency is being considered.

## Formal criteria

A reuse application pass is acceptable only if all of the following hold:

1. **Reuse before custom-code** *(Jones BP #28 p. 109)* — the work checks the certified reuse library first; custom coding is the fallback, not the default. Jones: "the software industry will continue with high costs and high error rates so long as software applications are custom-coded."
2. **Certified status verified** *(Jones BP #27 p. 101 + Ch 8 p. 522)* — the candidate artifact carries the certification certificate from `architect-reuse-certification`. Uncertified reuse is hazardous; Jones (Ch 8 p. 522): "uncertified reuse is hazardous and can be more expensive than custom development of the same module — hence, the reason the uncertified reuse can have a significant negative return on investment."
3. **Fit evaluated against the present need** — certification verifies the artifact is bug-free + secure; fit verifies it does what the current feature needs. The two are independent. A well-certified artifact applied to the wrong problem produces defects of misuse.
4. **License + provenance checked** *(Jones BP #27 p. 103)* — copyright, patent, license constraints (especially for open-source) must be compatible with the project's distribution model. Cross-link to `architect-reuse-certification` for the warranty record.
5. **Defect-density expectation calibrated** *(Jones Ch 8 p. 522)* — certified zero-defect-targeted code carries defect potentials around 1/100th of custom code (typical custom: 15 defects per KLOC; certified reuse can be ~0.15/KLOC). Uncertified code at >1 defect/KLOC plugged into >10 applications has negative combined-debugging ROI.
6. **Code reuse extends beyond source code** *(Jones BP #26 p. 100 + Ch 8 p. 522)* — when applying reuse, consider also reusable designs, test cases, HELP text, work breakdown structures associated with the code module. The package travels together.
7. **Modification minimized** — modifying certified reusable code voids its certification. Either the modification goes through re-certification (cross-link `architect-reuse-certification`) or the artifact is forked from the library and re-baselined as a project-local artifact. Silent modification of library artifacts is forbidden.
8. **Familiarity gap acknowledged** *(Jones Ch 8 p. 522)* — "it is much harder for software engineers to debug someone else's unfamiliar code than it is to debug their own." Reuse imports debugging burden if defects do appear; the gain (defect prevention via lower defect-potential) only outweighs the burden when certification is genuine.

## How you proceed

1. **Identify the need.** What functional contract must the new code satisfy? Functional signature, performance budget, security constraints. Pull from the parent Gherkin spec (`product-manager-spec-gherkin`).
2. **Search the certified reuse library.** Architect curates it (cross-link `architect-reusability-strategy`). Match against name, taxonomy, contract.
3. **Verify certification status.** Certificate present, version pinned, dependencies tracked, known-defect log accessible. If any is missing, the candidate is *not yet admissible*; refer back to `architect-reuse-certification`.
4. **Evaluate fit.** Does the artifact's contract match the feature's contract? Examine inputs, outputs, side effects, threading model, error semantics. Mismatches large enough to require modification mean either re-certification or reject + custom code.
5. **Check license + provenance** for third-party artifacts. The Architect's certification record carries warranties (BP #27 p. 103 practice 11).
6. **Plug it in without modification** when fit is good. Document the version and the certification reference in the consuming module so post-release recall can reach this site.
7. **If modification is unavoidable**, either:
   - Submit the modification request to Architect for re-certification of the modified artifact, or
   - Fork the artifact into the project's local code with explicit "no longer claimed as certified library artifact" marker.
8. **Record the reuse instance.** Per Jones BP #27 p. 102 practice 9: every reuse distribution is recorded so a defect / vulnerability post-admission triggers recall to this site.
9. **Reject uncertified candidates with a written reason.** Track refusals — the gap may motivate a future certification effort if the candidate is high-value.

## Pitfalls to avoid

- **Pulling from popular OSS without certification.** Popularity is not certification (Jones BP #27 p. 101). A package with 10 million downloads can still have undisclosed defects or back doors (Jones Ch 8 p. 522).
- **Modifying library artifacts silently.** Voids certification and breaks the recall pipeline. Either re-certify or fork explicitly.
- **Reusing only source code.** The 14 other reusable artifact types (designs, tests, HELP text, etc.) often compound the gain (Jones BP #26 p. 100).
- **Plugging a certified artifact into the wrong problem.** Certification verifies the artifact is bug-free; fit is a separate check.
- **Ignoring the familiarity-gap debugging cost.** When defects do appear in reused code, debugging is more expensive than for own code. The certification-derived prevention must be high enough to offset this.
- **Combining many uncertified reusable modules.** Each adds independent defect probability; aggregate quality drops fast. Jones (Ch 8 p. 522): >1 defect/KLOC × >10 applications → negative ROI.
- **Out-of-bibliography frameworks adopted as authority.** "Just use Spring" / "use this React library" — the decision needs the certification gate, not the brand. Cite Jones BP #27, not the library's marketing.

## Source

- **Best Practice #26 — *Software Reusability* (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, pp. 99–101)** — 15 reusable artifact types, ±300% ROI swing, <25% industry-average reuse vs >85% target, related to `architect-reusability-strategy`.
- **Best Practice #27 — *Certification of Reusable Materials* (Jones 2010, pp. 101–103)** — certification authority model, 11 supporting practices, security back-door warning (p. 102), warranty record requirement, distribution record for recall.
- **Best Practice #28 — *Programming or Coding* (Jones 2010, pp. 107–109)** — reuse-before-custom rule, custom-coding cost framing, reusable-objects as the leverage point for industry-wide cost reduction.
- **Chapter 8 § *Code reuse as defect prevention* (Jones 2010, p. 522)** — certified reuse defect potentials ~1/100th of custom; uncertified reuse hazardous → negative ROI; familiarity-gap debugging cost; 50:1 ratio of uncertified to certified sources.
- **Cross-references**: `architect-reusability-strategy` (library design), `architect-reuse-certification` (admission gate), `developer-coding-practices` (when to choose reuse vs custom), `qa-defect-removal-efficiency` (certified reuse as a defect-prevention layer).
- Out-of-bibliography (convention pointers only): npm / PyPI / Maven Central reputation signals (not certification), Software Bill of Materials (SBOM) standards.
- Full traceability: `bibliography/skill-references.md` § `developer-reuse-application`.
