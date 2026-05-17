---
name: product-manager-value-analysis
description: "Assess the tangible and intangible value of a capability or feature using Capers Jones's Value Analysis framework and the Cagan four-risks lens. Use whenever the human wants to prioritize work by business value, justify investment to stakeholders, decide between competing capabilities, build a business case, or compute return on investment for a piece of scope. Triggers include phrases like 'is this worth building?', 'business value', 'ROI', 'value points', 'prioritize by value', 'how do we justify this?', 'cost of not doing this?', 'value risk', 'is this strategic?'."
---

# product-manager-value-analysis

## Purpose

Most teams confuse "we want this" with "this is valuable." Value analysis forces the distinction: it separates the financial side (cost reduction, revenue, market share) from the intangible side (national security, morale, customer satisfaction, harm avoidance) and produces a defensible comparison across competing scope. This skill lets the Product Manager make value explicit before prioritization, so the backlog reflects value-weighted choice rather than loudest voice.

## When this skill applies

- Two or more capabilities compete for the same MVP slot and a Go/No-go must be defended.
- A stakeholder asks for a feature whose value is unstated.
- A business case is needed for funding, ROI, or total cost of ownership.
- The team feels "everything is priority 1" — value-weighting is the way out.
- A capability with a high effort estimate must be justified or dropped.

## Formal criteria

A value analysis passes review only if all of the following hold:

1. **Both buckets analyzed** — the analysis covers Tangible Financial Value **and** Intangible Value. Skipping intangible value silently kills strategic work (compliance, safety, national defense) that has weak short-term financials.
2. **Tangible items quantified or explicitly marked unquantifiable** — for each of the ten tangible items below, either a number with units is provided or the item is marked *"not quantifiable in this iteration"* with a one-line reason. Adjectives ("significant", "large") are not values.
3. **Intangible items mapped to value points** — intangible value is expressed on a value-point scale (a useful convention: a financial value point ≈ USD 1,000; per-customer added/lost ≈ 10 value points; lives / national defense on a logarithmic scale). Choosing different ratios is allowed if documented.
4. **Cagan value-risk framing cross-checked** — the analysis names which of Cagan's four risks the work resolves: **value risk** (will customers buy/use it?), **usability risk** (can they figure it out?), **feasibility risk** (can engineers build it with current technology and skills?), **business viability risk** (can sales/marketing/legal/finance cope?). High-value work that resolves only feasibility risk is an engineering bet, not a value bet.
5. **Comparable to alternatives** — every value analysis is comparative. A standalone score has no decision power; produce at least two columns (this work vs. doing nothing, or this work vs. the next-best capability).
6. **Time horizon stated** — value accrues over time. State the horizon (12 months, 3 years, life-of-product) and use the same horizon across alternatives.

## How you proceed

1. **Confirm what is being valued.** A capability? A feature? A whole release? The unit of analysis must be explicit — pricing apples vs. oranges is the most common defect.
2. **Walk the Tangible Financial Value list.** For each item, attempt a number for the chosen horizon:
   - Cost reductions from the new application.
   - Direct revenue from the new application.
   - Indirect revenue (e.g., hardware sales pulled along).
   - "Drag along" revenue in companion applications.
   - Domestic market share increase.
   - International market share increase.
   - Competitive market share decrease (taking share from competitors).
   - Increase in number of users due to new features.
   - User performance increases.
   - User error reductions.
   Mark each *quantified* (with units), *estimated band* (e.g., $50k–$200k/year), or *not quantifiable* (with one-line reason).
3. **Walk the Intangible Value list.** For each item, decide if it applies; if it does, attach a value-point estimate using the scaling convention:
   - Potential harm if competitors instead of you build the application.
   - Potential harm if competitors build a similar application.
   - Potential gain if your application is first to market.
   - Synergy with existing applications already released.
   - Benefits to national security.
   - Benefits to human health or safety.
   - Benefits to corporate prestige.
   - Benefits to employee morale.
   - Benefits to customer satisfaction.
4. **Map to the Cagan four risks.** Tag the work as resolving primarily value, usability, feasibility, or business viability risk. Work that resolves value risk early is disproportionately valuable; work that only resolves feasibility risk is plumbing.
5. **Score alternatives side-by-side.** Present at least two columns: the proposed work and at least one alternative (the next-best capability, the do-nothing baseline, or both).
6. **Compute ROI or value-points-per-cost.** Value points integrate financial and intangible inputs into a single comparable scalar. ROI = (value − cost) / cost. Do not present a value analysis without at least one ratio against cost.
7. **State assumptions and confidence.** Every estimate carries assumptions. Make them explicit in the node body so the analysis can be re-run when assumptions change.

## Pitfalls to avoid

- **Adjective math.** "Significant impact" and "huge opportunity" are not values. Refuse to mark items as quantified unless they carry units.
- **Skipping intangibles because they are harder.** The financial side alone may be suspect; the intangible side covers the strategically important items. Strategic work is most often intangible-heavy.
- **Pricing apples vs. oranges.** Comparing capability A over 12 months with capability B over 5 years inverts conclusions. Lock the horizon first.
- **Hidden discount rates.** If the comparison stretches beyond two years, name the discount rate explicitly. Different rates change the winner.
- **Single-column scoring.** A standalone score gives no decision power. Always score against at least one alternative.
- **Importing a value framework the project has not audited.** Jobs-to-be-Done can be useful framing but is not this skill's governing body of knowledge. Surface the gap if the human wants it applied formally.
