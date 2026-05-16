---
name: product-manager-early-sizing
description: "Size a software application early using function-point methods (full IFPUG/COSMIC counting, light FP approximation, pattern-matching size estimation against ISBSG-class historical data) so cost estimation, schedule planning, and risk analysis can proceed on quantitative ground rather than guesswork. Use whenever a project is starting, before any cost estimate, when scope needs quantification, when 'how big is this?' becomes a stakeholder question, or when comparing two scope alternatives. Triggers include phrases like 'how big is this project', 'size estimate', 'function points', 'FP', 'ISBSG', 'pattern matching size', 'how long will it take', 'is this a single release or multi-release', 'too big for one sprint'."
---

# product-manager-early-sizing

## Purpose

Until 2008–2009, application size could only be calculated once requirements were known — too late for the initial cost and schedule decisions that shape the project. Three modern instruments changed this: full IFPUG / COSMIC function-point counting, "light" function-point approximation, and pattern-matching against historical applications (ISBSG-class databases of ~5,000 projects). This skill lets the Product Manager produce a defensible size in function points before requirements are complete, so cost estimating (`product-manager-cost-estimating`), planning (`product-manager-project-planning`), and risk analysis (`product-manager-risk-analysis`) have quantitative ground to stand on. Without early sizing, the first cost estimate is a guess and every downstream decision inherits the guess.

## When this skill applies

- A new project starts and no FP figure exists.
- A capability or release needs scoping before commitment.
- A stakeholder asks for cost or schedule without an existing size estimate.
- An application size approaches the 1,000 / 10,000 / 100,000 FP boundaries where behaviour changes (single release ↔ multi-release).
- A risk analysis (`product-manager-risk-analysis`) needs the size tier to apply the right escalation rule.

## Formal criteria

A sizing pass is acceptable only if all of the following hold:

1. **Output in function points, not lines of code** *(Jones BP #6, p. 51)* — Jones is explicit: function points are best practice, lines of code is malpractice as a size metric. Code-line counts may appear as a secondary or tertiary metric but never as the primary size.
2. **Method matches the available information** *(Jones BP #6, pp. 51–52)* —
   - **Pattern matching** when requirements are not yet known (sizes against similar applications by external description).
   - **Light function-point analysis** when partial requirements exist (minutes vs the ~400-FP/day of full counting).
   - **Full IFPUG / COSMIC counting** when requirements are complete.
   Choosing a method that requires more inputs than you have is the most common defect.
3. **Tier-aware release strategy** *(Jones BP #6, pp. 52–53)* —
   - **Below ~1,000 FP**: single release is the norm.
   - **10,000 – 100,000 FP**: multi-release at 12–18 month intervals.
   - **Agile sprints**: 100–200 FP per sprint.
   The release strategy is a direct consequence of the size tier; producing a size without naming the implied release strategy is incomplete.
4. **ISBSG cross-check or explicit gap statement** *(Jones BP #6, p. 51; BP #31)* — when the application class is represented in ISBSG, the sizing carries an ISBSG comparison. When it is not (military classified, embedded niche), state that explicitly so downstream estimators do not over-trust the figure.
5. **Growth-rate prediction included** *(Jones BP #6, p. 52)* — pattern matching also predicts the rate at which requirements are likely to grow during development. The sizing output names both an initial FP and an expected growth band (compatible with BP #11's 1%–3%/month).
6. **Documented assumptions** — every sizing carries the assumptions on which it depends (class of application, level of reuse, presence of supply chain, similar applications referenced). Without these, the figure cannot be reproduced or audited.

## How you proceed

1. **Identify the input set you actually have.** None, partial, or complete requirements? The method (pattern matching / light FP / full counting) is selected from this answer, not from preference.
2. **Pick the method.**
   - No requirements yet → pattern matching against external descriptions of similar applications.
   - Partial requirements → light function-point analysis.
   - Complete requirements → full IFPUG (or COSMIC) counting.
3. **Produce the FP figure with a band, not a point.** Early sizing is intrinsically uncertain; present low–central–high values rather than a single number. The width of the band shrinks as the method's input requirement is more fully satisfied.
4. **Cross-reference ISBSG (or its equivalent) where the class is represented** *(BP #31)*. Include comparable projects and their actual FP, schedule, and cost.
5. **Predict growth rate** *(BP #6, p. 52 + BP #11 empirics)*. State the expected requirements-creep band (0.5%–3%/month per Jones BP #11) and accumulate it across the planned development duration.
6. **Name the release strategy implied by the tier.** Below 1,000 FP → plan for single release. 10k–100k FP → plan multi-release at 12–18 month intervals and split features across them.
7. **Record secondary and tertiary sizing if relevant.** LOC count by language, screens/reports/database tables count. These supplement but never replace the FP figure.
8. **Hand off to downstream skills.** Cost estimation, project planning, and risk analysis all consume this figure. Tag the artifact so they can find it.

## Pitfalls to avoid

- **Sizing in lines of code.** Jones's verdict (p. 51): "lines of code approach is malpractice." Use FP. LOC is a code-density artifact, not a size measure for projects.
- **Single-number sizing.** Sizing without a band over-claims precision. State the uncertainty.
- **Choosing the wrong method for the input.** Asking for full IFPUG counting when only the external description exists wastes effort; offering pattern matching when complete requirements exist under-uses the data.
- **Ignoring growth.** A size produced today is not the size at delivery — Jones BP #11 reports cumulative growth of 50% by deployment for 10,000-FP applications. The size record must include the growth band.
- **Skipping ISBSG when the class is represented.** Internal sizings without external benchmarks are systematically optimistic.
- **No assumptions log.** A sizing without explicit assumptions cannot be audited and cannot be re-run when assumptions change.

## Source

- **Best Practice #6 — *Early Sizing and Scope Control of Software Applications* (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, pp. 51–53).** FP-best-practice / LOC-malpractice distinction; pattern matching for novel applications; light FP analysis; ISBSG critical mass (~5,000 applications); tier-based release strategy (1k single, 10k–100k multi-release at 12–18 months, Agile sprints 100–200 FP); growth-rate prediction as part of sizing output.
- **ISBSG as remote benchmark source** — Capers Jones BP #31, pp. 113–114 (more detail in `product-manager-benchmarks-baselines`).
- **Growth-rate empirics (1%–3%/month, up to 50% cumulative)** — Capers Jones BP #11, p. 71.
- Full traceability: `bibliography/skill-references.md` § `product-manager-early-sizing`.
