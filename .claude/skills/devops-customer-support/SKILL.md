---
name: devops-customer-support
description: "Size and run the customer-support function using Capers Jones BP #45's empirical staffing baseline (1 support person per 10,000 function points; 1 per 150 customers) with the explicit recognition that ratios drift to 1 per 1,000 as customer count grows — meaning defect-prevention upstream (reducing delivered defects by 220 saves 1 support FTE per year) is the only sustainable lever. Use whenever sizing the support team for a release, deciding whether to outsource L1 support, planning support tiers (L0 self-service / L1 first-call / L2 specialist / L3 engineering), evaluating long phone wait complaints, or arguing for quality investment by support-savings math. Triggers include phrases like 'customer support', 'support staffing', 'how many support people', 'L1 L2 L3', 'help desk', 'first-line support', 'why are wait times so long', 'support outsourcing', 'AI support agent', 'support tier'."
---

# devops-customer-support

## Purpose

Customer support is "almost universally unsatisfactory" (Jones BP #45 p. 157) — labor-intensive, expensive, and economically unsustainable at the 1-support-per-150-customers ratio Jones reports as the empirical baseline. As customer count grows, ratios drift to 1-per-1,000 → long wait times. The only sustainable lever is defect-prevention upstream: every 220 delivered defects fewer ≈ 1 support FTE saved per year (Jones p. 157). This skill lets DevOps size the support function correctly against Jones's empirical ratios, plan the tier structure, evaluate AI / e-mail / phone channel mix, and surface the support-cost-vs-quality-investment trade-off to PO.

## When this skill applies

- A new release is being planned and support staffing must be sized.
- An existing support function has long wait times and the diagnosis is open.
- Outsourcing L1 support is being evaluated.
- The team is debating fee-for-support vs free-for-support.
- An AI-based first-tier support model is being designed.
- Quality investment is being justified by support-savings math.

## Formal criteria

A customer-support plan is acceptable only if all of the following hold:

1. **Staffing sized against Jones's empirical ratios** *(Jones BP #45 p. 157)* — baseline: 1 support person per 10,000 function points OR 1 per 150 customers (whichever is the relevant constraint). Above ~thousands of customers the ratio drifts upward to ~1 per 1,000 — long wait times are then expected.
2. **Defect-prevention-to-support-FTE multiplier acknowledged** *(Jones BP #45 p. 157)* — 1 bug ≈ 30 customers find it ≈ 1 day of one support FTE; 220 working days per year → 220 delivered-defect reduction = 1 fewer support FTE per year. Quality investment (cross-link `qa-defect-removal-efficiency`) is the leverage; staffing is the consequence.
3. **Tier model declared** — L0 (self-service: knowledge base, FAQ, web bug-status), L1 (first-call: ~60% resolution per BP #49 practice 4), L2 (specialist for complex issues), L3 (engineering for code defects). Volume distribution + staffing per tier.
4. **Channel mix declared** — phone (with ≤5 min wait per BP #49 practice 3) + e-mail (with ≤48h response per BP #49 practice 2) + accessible channels for hearing-impaired (BP #49 practice 5) + web self-service.
5. **Outsourcing decision documented** *(Jones BP #45 p. 157)* — "one of the most common activities outsourced to countries with low labor costs." For non-strategic support, outsourcing reduces cost but may degrade quality; for strategic / regulated / privileged-data support, in-source.
6. **Fee-for-support scope limited** *(BP #49 anti-pattern 5 + practice 6)* — fee-based support excludes bug reports and vendor-caused problems. Charging for bug reports is named anti-pattern 5 and drives customer dissatisfaction.
7. **Innovation track for scale** *(BP #45 p. 158)* — for large applications with millions of customers, scale-only-by-headcount fails. AI / virtual support / standardized HELP screens / e-mail triage are scale levers Jones names explicitly.

## How you proceed

1. **Get the customer count and FP size.** Cross-link `po-early-sizing`. Apply both Jones ratios; the more restrictive sets the baseline.
2. **Project the next year's defect-discovery rate.** Defect potentials × delivered defects (cross-link `qa-defect-removal-efficiency`). Tickets ≈ delivered-defect count × 30 (Jones's discovery factor).
3. **Plan the tier model** with volume distribution. Web self-service (L0) deflects the highest-volume / lowest-complexity tickets; L1 handles ~60% of the rest; L2 + L3 carry the residual.
4. **Pick the channel mix.** Phone + e-mail + accessible + self-service. Wait-time targets from BP #49 (≤5 min phone, ≤48h e-mail).
5. **Decide outsourcing** for L1 if appropriate. Non-strategic, non-privileged-data, language-aligned with customer base.
6. **Cost the support function.** FTE × labor cost. Compute the trade-off against upstream quality investment (220-defect rule).
7. **Plan innovation for scale.** For >100k customers consider AI first-tier + e-mail triage + reusable HELP-screen libraries (Jones BP #45 p. 158).
8. **Surface to PO** as part of release planning (`po-cost-estimating`, `po-project-planning`). Support cost is part of release cost.

## Pitfalls to avoid

- **Staffing only by customer count, ignoring FP size.** Both ratios apply; the more restrictive holds. A 100,000-FP application with 1,000 customers is constrained by FP, not customer count.
- **Linear scaling assumption.** 1-per-150 cannot be sustained at million-customer scale (BP #45 p. 157). Plan for 1-per-1,000 and the wait times that come with it, OR invest upstream in quality.
- **Quality investment treated as separate from support cost.** The 220-defect rule (BP #45 p. 157) makes them the same conversation.
- **Fee for bug reports.** Anti-pattern (BP #49 #5). Charges customers for the vendor's mistake; reliably drives dissatisfaction.
- **Phone-only.** Anti-patterns 2 + 3 (BP #49). Hearing-impaired excluded; e-mail not available.
- **No L0 self-service.** Highest-volume tickets are routine; deflecting them via web KB / FAQ / known-bugs page saves L1 capacity.
- **Outsourcing strategic / privileged-data support.** The cost reduction can be real but the privacy / quality risk can exceed it.
- **AI support as full replacement.** AI deflection of L0 + e-mail triage is supported by BP #45 p. 158 as a scale lever; AI as full replacement of L1 is not yet supported by evidence.

## Source

- **Best Practice #45 — *Customer Support of Software Applications* (Capers Jones, *Software Engineering Best Practices*, McGraw-Hill 2010, pp. 157–158).** Empirical staffing ratios (1/10kFP, 1/150 customers, drifting to 1/1,000 at scale); 220-defect ≈ 1 support FTE per year multiplier; support-as-most-commonly-outsourced; AI virtual support / e-mail triage / standardized HELP / SOA-reusable HELP scale levers; small-company-better-support observation.
- **Best Practice #49 — *Updates and Releases* (Jones 2010, pp. 164–165)** — release-side anti-patterns + practices that interact with support model (16 anti-patterns and 11 practices, especially #2 e-mail SLA, #3 phone SLA, #4 60% first-tier resolution, #5 hearing-impaired, #6 fee scope).
- **Cross-references**: `qa-defect-removal-efficiency` (quality investment is the support-cost lever); `po-cost-estimating` (support is part of release cost); `po-early-sizing` (FP needed for ratio); `devops-releases` (release plan triggers support volume).
- Out-of-bibliography (convention pointers only): ITIL service desk model, Zendesk / Salesforce Service Cloud / Intercom tooling, customer-satisfaction (CSAT / NPS) metrics.
- Full traceability: `bibliography/skill-references.md` § `devops-customer-support`.
