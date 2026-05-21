---
name: devops-customer-support
description: "Size and run the customer-support function using Capers Jones's empirical staffing baseline (1 support person per 10,000 function points; 1 per 150 customers) with the explicit recognition that ratios drift to 1 per 1,000 as customer count grows — meaning defect-prevention upstream (reducing delivered defects by ~220 saves 1 support FTE per year) is the only sustainable lever. Use whenever sizing the support team for a release, deciding whether to outsource L1 support, planning support tiers (L0 self-service / L1 first-call / L2 specialist / L3 engineering), evaluating long phone wait complaints, or arguing for quality investment by support-savings math. Triggers include phrases like 'customer support', 'support staffing', 'how many support people', 'L1 L2 L3', 'help desk', 'first-line support', 'why are wait times so long', 'support outsourcing', 'AI support agent', 'support tier'."
---

# devops-customer-support

## Purpose

Customer support is "almost universally unsatisfactory" — labor-intensive, expensive, and economically unsustainable at the 1-support-per-150-customers ratio Capers Jones reports as the empirical baseline. As customer count grows, ratios drift to 1-per-1,000 → long wait times. The only sustainable lever is defect prevention upstream: every ~220 delivered defects fewer ≈ 1 support FTE saved per year. This skill lets DevOps size the support function correctly against the empirical ratios, plan the tier structure, evaluate the AI / e-mail / phone channel mix, and surface the support-cost-vs-quality-investment trade-off to Product Manager.

## When this skill applies

- A new release is being planned and support staffing must be sized.
- An existing support function has long wait times and the diagnosis is open.
- Outsourcing L1 support is being evaluated.
- The team is debating fee-for-support vs free-for-support.
- An AI-based first-tier support model is being designed.
- Quality investment is being justified by support-savings math.

## Formal criteria

A customer-support plan is acceptable only if all of the following hold:

1. **Staffing sized against the empirical ratios** — baseline: 1 support person per 10,000 function points OR 1 per 150 customers (whichever is the relevant constraint). Above ~thousands of customers the ratio drifts upward to ~1 per 1,000 — long wait times are then expected.
2. **Defect-prevention-to-support-FTE multiplier acknowledged** — 1 bug ≈ 30 customers find it ≈ 1 day of one support FTE; ~220 working days per year → a ~220 delivered-defect reduction = 1 fewer support FTE per year. Quality investment (cross-link `qa-defect-removal-efficiency`) is the leverage; staffing is the consequence.
3. **Tier model declared** — L0 (self-service: knowledge base, FAQ, web bug-status), L1 (first-call: ~60% resolution), L2 (specialist for complex issues), L3 (engineering for code defects). Volume distribution + staffing per tier.
4. **Channel mix declared** — phone (≤5 min wait) + e-mail (≤48h response) + accessible channels for the hearing-impaired + web self-service.
5. **Outsourcing decision documented** — customer support is one of the most commonly outsourced activities. For non-strategic support, outsourcing reduces cost but may degrade quality; for strategic / regulated / privileged-data support, in-source.
6. **Fee-for-support scope limited** — fee-based support excludes bug reports and vendor-caused problems. Charging for bug reports is a named anti-pattern and drives customer dissatisfaction.
7. **Innovation track for scale** — for large applications with millions of customers, scale-only-by-headcount fails. AI / virtual support / standardized HELP screens / e-mail triage are scale levers.

## How you proceed

1. **Get the customer count and FP size.** Cross-link `product-manager-early-sizing`. Apply both ratios; the more restrictive sets the baseline.
2. **Project the next year's defect-discovery rate.** Defect potentials × delivered defects (cross-link `qa-defect-removal-efficiency`). Tickets ≈ delivered-defect count × ~30 (the discovery factor).
3. **Plan the tier model** with volume distribution. Web self-service (L0) deflects the highest-volume / lowest-complexity tickets; L1 handles ~60% of the rest; L2 + L3 carry the residual.
4. **Pick the channel mix.** Phone + e-mail + accessible + self-service. Wait-time targets: ≤5 min phone, ≤48h e-mail.
5. **Decide outsourcing** for L1 if appropriate. Non-strategic, non-privileged-data, language-aligned with the customer base.
6. **Cost the support function.** FTE × labor cost. Compute the trade-off against upstream quality investment (the ~220-defect rule).
7. **Plan innovation for scale.** For >100k customers consider AI first-tier + e-mail triage + reusable HELP-screen libraries.
8. **Surface to Product Manager** as part of release planning (`product-manager-cost-estimating`, `product-manager-project-planning`). Support cost is part of release cost.

## Pitfalls to avoid

- **Staffing only by customer count, ignoring FP size.** Both ratios apply; the more restrictive holds. A 100,000-FP application with 1,000 customers is constrained by FP, not customer count.
- **Linear scaling assumption.** 1-per-150 cannot be sustained at million-customer scale. Plan for 1-per-1,000 and the wait times that come with it, OR invest upstream in quality.
- **Quality investment treated as separate from support cost.** The ~220-defect rule makes them the same conversation.
- **Fee for bug reports.** A named anti-pattern. Charging customers for the vendor's mistake reliably drives dissatisfaction.
- **Phone-only.** Hearing-impaired excluded; e-mail not available — both named anti-patterns.
- **No L0 self-service.** Highest-volume tickets are routine; deflecting them via web KB / FAQ / known-bugs page saves L1 capacity.
- **Outsourcing strategic / privileged-data support.** The cost reduction can be real but the privacy / quality risk can exceed it.
- **AI support as full replacement.** AI deflection of L0 + e-mail triage is a supported scale lever; AI as a full replacement of L1 is not yet supported by evidence.
- **Security-related customer reports routed to L1 without security triage.** Suspected security incidents (data breach reports, vulnerability disclosures, account compromise, fraud) escalate directly to Security Officer (`security-officer-threats-and-defenses` for triage criteria), not through generic L1 → L2 → L3 escalation. Public disclosure of vulnerabilities follows a responsible-disclosure policy owned by Security; cross-link `security-officer-security-program` for the policy.
