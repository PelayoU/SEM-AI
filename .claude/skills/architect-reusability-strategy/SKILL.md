---
name: architect-reusability-strategy
description: "Design a reusability strategy for the project or portfolio using Capers Jones's 15-artifact reuse inventory (architecture, requirements, source code, designs, help, data, training, cost estimates, screens, project plans, test plans, test cases, test scripts, user documents, human interfaces) with explicit awareness of the ±300% ROI swing between high-quality certified reuse and uncertified buggy reuse. Use whenever the team is asking which artifacts to make reusable, how to lift the average 25% reuse content to the 85–95% target, or whether the latest enthusiasm for SOA / ERP / OO class libraries will deliver on its promise. Triggers include phrases like 'reuse', 'reusable component', 'reusability', 'SOA reuse', 'object-oriented class library', 'pattern library', 'reusable design', 'should we build a component library', 'why isn't our reuse paying off'."
---

# architect-reusability-strategy

## Purpose

Reuse is the highest-ROI lever in software engineering when it works and the deepest-negative-ROI swamp when it does not. Capers Jones reports "plus or minus 300 percent ROIs have been observed" — the same technology produces opposite outcomes depending on quality. The 2009 industry average reusable content in typical applications was less than 25%; Jones's stated target is >85% on average and >95% for common application types. This skill lets the Architect plan reusability across the full 15-artifact inventory (not just source code, which is the topic most of the literature mistakenly fixates on) with quality preconditions and the ROI swing made explicit.

## When this skill applies

- The team is starting reuse work and only thinking about source code.
- A reuse initiative previously failed and the diagnosis is needed.
- The application belongs to a domain with strong portfolio similarity (insurance, banking, manufacturing, pharma) where industry reuse should already be ~50%+.
- The team is being asked to adopt SOA, an OO class library, or an ERP package on a reuse argument.
- A reuse repository is being planned and the artifact taxonomy must be decided.

## Formal criteria

A reusability strategy is acceptable only if all of the following hold:

1. **All 15 reusable artifact types considered, not just code** — strategy explicitly addresses each of: architecture, requirements, source code (zero-defect), designs, help information, data, training materials, cost estimates, screens, project plans, test plans, test cases, test scripts, user documents, human interfaces. Most reuse failures are reuse-of-code-only strategies; broader artifact reuse compounds.
2. **Quality precondition stated for each reusable artifact** — "buggy materials cannot safely be reused". The quality control set includes inspections of reusable text documents, inspections of reusable code segments, static analysis of reusable code segments, testing of reusable code segments, and publication of certification certificates. Reuse without these gates is *worse* than no reuse.
3. **Tracking requirements specified** — for every reusable artifact the strategy records: all customers/users (for recall), all bugs/defects in the artifact, all releases of the artifact, certification results, and all updates/changes. A reuse library without these tracking columns is a hazard, not an asset.
4. **ROI swing acknowledged and managed** — strategy states the expected ROI band and the certification approach that keeps the project on the positive side. The ±300% ROI swing is the operating reality, not a theoretical hazard.
5. **Industry-pattern leverage used when applicable** — for applications in industries with ~80% portfolio similarity (banking, insurance, manufacturing, pharma), industry reuse should be a starting assumption. Outsource vendors specializing in such domains regularly achieve 50%+ reuse from accumulated artifacts.
6. **Current-state baseline measured** — the strategy states the current reuse percentage (Jones reports industry average <25% in 2009) and the target (>85% average / >95% for common types). Without a baseline, progress cannot be measured.
7. **Reuse hype skepticism** — the strategy explicitly evaluates whether the proposed reuse vehicle (SOA, OO class libraries, ERP packages) has empirical track record or is still primarily marketing claim. Jones is explicit: "neither object-oriented class libraries nor other forms of reuse such as commercial enterprise resource planning (ERP) packages have been totally successful". SOA empirical data was unavailable in 2009.

## How you proceed

1. **Inventory the project's reuse surface against the 15 artifact types.** For each, mark current reuse percentage and target. Source code dominates current practice; the gains come from extending to requirements, designs, test materials, and documentation.
2. **Pull the industry baseline.** If the application is in a high-similarity industry, expect 50%+ portfolio reuse should be achievable from sector patterns. Cross-link to `architect-architecture-design` for the pattern catalog.
3. **Define quality preconditions per artifact category.** Code artifacts: inspection + static analysis + testing + certification certificate. Document artifacts: inspection + certification certificate. Test artifacts: defect history + execution history. No certification certificate = artifact not entered into the reuse library.
4. **Stand up the tracking schema.** Per artifact, record: source, certification status, customer list, defect log, version history, change log, distribution log. Cross-reference to `architect-reuse-certification` for the certification gate.
5. **Compute the expected ROI band.** Best case (high-quality certified): about +300%. Worst case (uncertified, buggy): about −300%. Project actuals depend on the certification rigour applied — make the assumption explicit.
6. **Evaluate proposed reuse vehicles skeptically.** SOA / OO class libraries / ERP / pattern catalogs each have specific failure modes. Jones is explicit about the historical disappointment; require empirical evidence for the specific vehicle, not generic claims.
7. **Plan the migration path.** Industry typical: <25% reuse → first target 50% → eventual 85%/95%. Jumping from <25% to >85% in one cycle has no historical evidence. Plan phased adoption.

## Pitfalls to avoid

- **Code-only reuse.** Most reuse literature is about source code; most of the ROI is in the other 14 artifact types (requirements, designs, test materials, documentation). Limiting strategy to code leaves the largest gains on the table.
- **Reuse without certification.** Jones is unambiguous: if the reused material is buggy, reuse becomes the worst-ROI technology in the industry. Certification is not optional.
- **No tracking schema.** A reuse library without customer-list, defect-log, version-history, and distribution-log is an attractive nuisance — when a defect is found in a reused artifact, every dependent application is affected and there is no way to recall.
- **Greenfield architecture in a pattern-rich industry.** Banking / insurance / pharma / manufacturing each have ~80% portfolio similarity. Starting from scratch ignores the sector's empirical reuse opportunity.
- **Hype-based vehicle adoption.** SOA, OO class libraries, and ERP packages all attracted enthusiasm without proportional empirical results. Adopt on evidence, not promises.
- **One-cycle jump to ≥85%.** No historical evidence supports this. Plan phases (e.g., +20% per release) with measurable checkpoints.
- **Failing to ride outsource vendor expertise.** Specialized outsource vendors (insurance, banking, etc.) often have 50%+ ready reuse — using them on the right work converts a build problem into an assembly problem.
