---
title: Function-point sizing
anchor: |
  Capers Jones — *Software Engineering Best Practices* (2009);
  IFPUG Counting Practices Manual; COSMIC Measurement Manual; ISBSG repository.
referenced_by:
  - .claude/agents/product-manager.md § Discipline / 10. Early sizing
  - .claude/agents/product-manager.md § Discipline / 11. Cost estimating
  - .claude/agents/product-manager.md § Discipline / 14. Benchmarks and baselines
status: written
---

# Function-point sizing

## Method

A size figure is produced by **matching the method to the input you actually have**:

1. **No requirements yet → pattern matching.** Size against the external description of similar applications in ISBSG (or in-house portfolio). Output: an FP band (low–central–high) with the comparison projects named. Also produces a growth-rate prediction (typical 1–3 %/month requirements creep).
2. **Partial requirements → light function-point analysis.** Minutes per application instead of the ~400 FP/day of full IFPUG. Output: an FP band tighter than pattern matching, with the assumption set documented.
3. **Complete requirements → full IFPUG / COSMIC counting.** Counts External Inputs (EI), External Outputs (EO), External Inquiries (EQ), Internal Logical Files (ILF), External Interface Files (EIF) per the IFPUG manual, applies VAF adjustment. Output: a single FP figure with the counting sheet.

In all three cases the output **includes**:

- An FP figure (band, not single number).
- A tier-aware release strategy (below ~1 000 FP → single release · 10 000–100 000 FP → multi-release at 12–18 month intervals · 100 000+ FP → enterprise with Zachman-grade architecture).
- A growth-rate band (typical 1–3 %/month; for a 12-month project that compounds to ~13–43 % accumulated growth at delivery).
- An ISBSG cross-check, OR an explicit gap statement (military / classified / embedded niche where ISBSG coverage is sparse).
- A documented assumption set (class of application, level of reuse, presence of supply chain, similar applications referenced).

## Generic criteria recap (mirror of agent.md)

- Output in function points, **not lines of code** (LOC is malpractice as a primary size measure).
- Method matches the input available — choosing a method that demands more inputs than you have is the most common defect.
- Tier-aware release strategy named.
- ISBSG cross-check or explicit gap statement.
- Growth-rate prediction included.

## Tier table

| FP range | Tier | Single / multi-release | Architecture rigor |
|---|---|---|---|
| < 100 | Trivial | Single | No formal architecture |
| 100 – 1 000 | Light | Single | Lightweight design notes |
| 1 000 – 10 000 | Important | Single or 2-3 releases | Formal architecture; ADR per topic |
| 10 000 – 100 000 | Critical | Multi-release at 12–18 mo intervals | Zachman 6×6; full Jones 7 topics |
| ≥ 100 000 | Enterprise | Multi-release at 18+ mo intervals | Enterprise Architecture; Architect specialises into Enterprise Architect |

Source: `instance/thresholds.yaml::arch_tier`.

## Bibliographic anchors

- **IFPUG counting** — IFPUG, *Counting Practices Manual*, v4.3.1 §§ 6–10 (full procedure for EI/EO/EQ/ILF/EIF).
- **COSMIC counting** — COSMIC, *Measurement Manual*, v4.0.2 §§ 3–5 (functional-process-based CFP figure).
- **Light FP analysis** — Jones, *Software Engineering Best Practices* (2009), Section 13, table 13-19 (high-speed sizing methods).
- **Pattern matching** — Jones, ibid., Section 13, p. 408 *seq.* (pattern-matching against ~5 000 historical projects).
- **ISBSG cross-check** — ISBSG, *International Software Benchmarking Standards Group Repository*, releases R12 onward; matched on application type, primary language, size band.
- **Growth rate** — Jones, ibid., Section 14, *Requirements churn empirics* (1–3 %/month).
- **Tier escalation** — Jones, ibid., Section 5, *Sizing software projects*.

## Worked example

> *"How big is this new lead-management tool we're scoping?"*

**Input set:** partial requirements (~30 stories sketched, no detailed AC yet).

**Method selected:** light FP analysis (input set rules out full IFPUG; richer than no-requirements pattern matching).

**Walk-through:**

1. Enumerate the stories. ~30 stories, ~1.5 unique input forms per story → ~45 EI candidates.
2. Each story shows ~1 output / 1 inquiry → ~30 EO + ~30 EQ.
3. Data model sketched: 8 entities → ~6 ILF (some merged), ~2 EIF (CRM + email service).
4. Apply Jones's light-FP coefficients: ~4 unadjusted FP per EI on average, ~5 per EO/EQ, ~10 per ILF, ~7 per EIF.
   - 45 × 4 + 30 × 5 + 30 × 5 + 6 × 10 + 2 × 7 = 180 + 150 + 150 + 60 + 14 = **554 FP unadjusted**.
5. VAF estimate (general system characteristics: medium complexity, online, data communications) → factor 1.05 → **~580 FP**.
6. Band: ±25 % (light-FP precision empirics) → **~440 – 730 FP**.
7. Tier: Light (< 1 000 FP) → single release.
8. Growth: 1.5 %/month (medium-novelty domain) → at 6-month delivery, ~10 % accumulation → final ~640 – 800 FP, plan against ~700 FP.
9. ISBSG cross-check: CRM-adjacent applications in the 500–800 FP band cluster around 4–6 person-months effort, schedule ~3 months elapsed → useful as a sanity bound.

**Output handed off to cost estimating + project planning + risk analysis:** *~700 FP, band 440–800, tier Light, single release, growth 1.5 %/mo, ISBSG class CRM-adjacent (4 comparable projects in repo).*

## Common pitfalls (extends agent.md)

- **Sizing in lines of code.** Malpractice as primary size; cross-language comparison collapses (Assembler at ~320 LOC/FP vs Python at ~50 LOC/FP makes the same application look 6× larger in Assembler). LOC may appear as secondary or tertiary metric.
- **Single-number sizing.** Without a band, downstream estimates over-claim precision and risk-reserves are skipped. Early sizing is intrinsically uncertain; communicate the uncertainty.
- **Wrong method for the input.** Demanding full IFPUG when only the external description exists wastes effort; offering pattern matching when complete requirements exist under-uses the data.
- **Ignoring growth.** A size produced today is not the size at delivery — for a 10 000 FP application a typical 50 % accumulation by deployment is the empirical norm. The size record must include the growth band.
- **Skipping ISBSG when the class is represented.** Internal sizings without external benchmarks are systematically optimistic by ~10–30 %.
- **No assumptions log.** A sizing without explicit assumptions cannot be audited and cannot be re-run when assumptions change. This is the single highest leverage source of optimism in projects that overrun.
- **Counting reuse as new code.** A 40 % certified-reuse application contributes only the new 60 % to size for productivity computations; mixing them inflates productivity figures and corrupts benchmarks downstream.
- **Treating an automated estimate as a count.** The engine's `estimate_size` MCP tool produces an *approximation* prefixed with `≈`; it is bootstrapping data for the tier decision, not an audited count. Replace with a manual count in `release.## Sizing` as soon as one exists.
