---
title: Product Manager discipline — this instance's methodology
anchors:
  - Marty Cagan — *Inspired* (2018) + *Empowered* (2020)
  - Capers Jones — *Software Engineering Best Practices* (2009)
  - Mike Cohn — *User Stories Applied* (2004) + *Agile Estimating and Planning* (2005)
  - Jeff Patton — *User Story Mapping* (2014)
  - GISF UC3M (`gisf-discovery.pdf`, `gisf-life-cycle.pdf`, `gisf-delivery-planning.pdf`)
  - IFPUG Counting Practices Manual + COSMIC Measurement Manual + ISBSG repository
referenced_by:
  - .claude/agents/product-manager.md § Sub-disciplines you cover
status: written
---

# Product Manager discipline — this instance's methodology

This playbook holds the **criteria + pitfalls + anchors** for each of the 15 Product-Manager sub-disciplines this instance adopts. The `.claude/agents/product-manager.md` agent file is framework-clean (methodology-blind); it points here for *what makes an artifact valid*.

A different product running SEM-AI swaps this file for its own (SAFe, OKRs, Modern Agile, etc.) — the framework, the engine, and the agent.md set stay the same.

> **Deeper dives.** Two sub-disciplines have standalone playbooks because they recur across multiple sub-disciplines and earn their own page: `fp-sizing.md` (used by Early sizing, Cost estimating, Benchmarks) and `fagan-inspections.md` (used by QA's Inspections and by Security Officer's Requirements & inspection). The rest live here.

---

## 1. Vision

The future state the product creates over a 2–10 year horizon — not the mission, not the positioning statement, not the roadmap.

**Criteria.**
- Future-as-system (how the customer lives differently), not future-as-feature list.
- Inspirational enough that competent engineers want to join; believable without yet being provable.
- Time horizon stated and **between 2 and 10 years** (Cagan's canonical band; `instance/thresholds.yaml::vision`).
- Grounded in observable trends the team believes will hold.
- Repeatable in one breath by everyone on the team.

**Pitfalls.** Confusing vision with mission. Anchoring in today's technology rather than the horizon. Using "act of faith" as an excuse to skip customer-hypothesis validation.

**Anchor.** Cagan's 10 principles of product vision + the 2 structural criteria (horizon, system-not-feature) + GISF 5-step construction.

## 2. Goals

Time-bounded outcomes one level below the vision, one above the capabilities.

**Criteria.**
- **SMART**: specific, measurable, achievable, relevant, time-bound (validate each letter).
- Parent vision referenced; orphan goals forbidden.
- Planning horizon declared (**Roadmap 1–2y · Release 2–9mo · Iteration 1–4w**, `instance/thresholds.yaml::goal`).
- Why-stack defensible — asking *"why?"* lands on the vision, not on another goal.
- Numbers, not adjectives (without numbers SMART degenerates).

**Pitfalls.** Confusing goals with capabilities (the most common error). Skipping the horizon. Goal-stacking instead of why-stacking.

**Anchor.** SMART framework + GISF 3 horizons + why-stack discipline.

## 3. Capabilities

What the product enables stakeholders to do, *implementation-agnostic*, filtered into MVP by business and product risk.

**Criteria.**
- Names an ability, not a UI element or technology; **two plausible implementations** must exist.
- Parent goal referenced.
- Stakeholder-framed: *"In order to [goal] as [stakeholder] I want {…}"*.
- Filterable via the **Cagan four-risks discriminator** (value · usability · feasibility · viability); Go / No-Go recorded.
- Non-overlapping with siblings under the same goal.

**Pitfalls.** Treating UI elements or specific technologies as capabilities. Pre-committing implementation in the name. Skipping the MVP filter. Restating the goal as the capability.

**Anchor.** Cagan four-risks filter + implementation-agnostic test (two implementations).

## 4. Feature decomposition

Capability → features → stories with narrative flow and INVEST stories.

**Criteria.**
- Story format: ***As [role], I want [capability], so that [benefit]*** with Conditions of Satisfaction on the back (Cohn).
- **INVEST** per story: Independent, Negotiable, Valuable, Estimable, Small, Testable (Cohn).
- Story Map hierarchy: **Activity → Task → Sub-task** respects left-to-right narrative order (Patton USM).
- Release slices are thin and horizontal (end-to-end workflow), not vertical (one module deep).
- **5 Cs** honoured: Card, Conversation, Confirmation, Construction, Consequences (Jeffries).

**Pitfalls.** Decomposing vertically. Card-as-spec (the card is the token, not the contract). Skipping the *so that* clause (fails *Valuable* in INVEST). Story map without narrative order.

**Anchor.** Cohn INVEST + Patton User Story Mapping + Jeffries 5 Cs.

## 5. Specs (Gherkin acceptance contract)

Executable AC for a feature — same language the team, the user, and the test runner read.

**Criteria.**
- Story-to-AC traceability: every scenario maps to a story id (`AC-A1`, `AC-A2`, …).
- One Feature per spec node; description below the Feature header.
- *Then* names observable outcomes only (state, output, side effect), never implementation.
- 3–5 steps per scenario; longer means it tests multiple things.
- Happy path + alternatives + error cases all covered.

**Pitfalls.** Multiple Features in one file. Background as a kitchen sink. Implementation in *Then*. Scenarios that test multiple things.

**Anchor.** Cucumber Gherkin reference + Specification by Example.

## 6. Requirements discovery

Elicit, analyse, and validate requirements, accounting for ~2 %/month churn and legacy mining on replacements.

**Criteria.**
- Structured elicitation (**JAD-class**) as baseline above ~1 000 FP; lightweight below.
- **Quality requirements (QFD)** and **security requirements (SRD)** explicit, never "best effort".
- Prototypes for high-risk or novel features before written spec.
- Legacy mining on replacement work (~80 % of new applications replace something).
- Formal inspections scheduled; stable IDs through design, code, test.

**Pitfalls.** Unstructured interviews as the only elicitation above 1 000 FP. Skipping legacy mining on replacements. Spec circulated for "comments" without inspection. Pretending requirements freeze; ~2 %/month churn is the empirical default.

**Anchor.** Jones BP #14 (14 practices: JAD, QFD, prototypes, legacy mining, inspections, traceability, churn budgeting, multi-release segmentation).

## 7. User involvement

A portfolio of participation forms scaled to size and user-base, with the satisfaction loop closed at acceptance.

**Criteria.**
- The **12 forms** considered explicitly (JAD · QFD · legacy-code review · embedded user · requirements review · CCB · contractor-doc review · design review · prototypes · training · defect reporting · acceptance testing).
- Effort ratio **10–50 %** of dev effort; below is satisfaction risk, above is committee overhead.
- Technique matches scale: embedded user for small Agile; surveys + focus groups + usability labs for mass-user products.
- Stakeholder map exists (Future Users · Indirectly Affected · Decision Makers).
- Persona sketch per user type; defect-reporting + acceptance-testing loops include users.

**Pitfalls.** "The PM talks to users" as the entire plan. One embedded user for a mass-user product. Forgetting indirectly affected parties. Skipping defect reporting and acceptance testing.

**Anchor.** Jones's 12-form involvement inventory + scale-aware technique selection.

## 8. Value analysis

Separate tangible financial value from intangible strategic value so competing work compares on defensible grounds.

**Criteria.**
- Both buckets analysed: **tangible** (cost reduction · revenue · market share · productivity · error reduction) and **intangible** (harm avoidance · competitive disruption · prestige · morale · satisfaction).
- Tangible items quantified or explicitly marked unquantifiable; adjectives are not values.
- At least one alternative scored (this work vs do-nothing, or this work vs next-best).
- Same time horizon across alternatives.
- Cagan four-risks cross-check (value · usability · feasibility · business viability).

**Pitfalls.** Adjective math. Skipping intangibles because harder (strategic work is intangible-heavy). Different horizons across alternatives. Single-column scoring.

**Anchor.** Jones's 10-item tangible value list + 8-item intangible list + Cagan four-risks lens.

## 9. Risk analysis

Project-execution risks + product-discovery risks, mitigated and refreshed.

**Criteria.**
- **Jones's 14 categories** swept; Cagan's **4 product-discovery risks** layered.
- Size escalation: optional below 1k FP · mandatory above 10k FP · evidence of malpractice to skip above 100k FP (`instance/thresholds.yaml::arch_tier`).
- Mitigation per active risk (what changes, who owns, re-evaluation trigger).
- Early-and-often scheduling (release boundary minimum; on-warning-sign as needed).
- 10+ cross-cutting risks grouped by theme, not tracked flat.

**Pitfalls.** One-shot registers never updated. Confident estimate without risks (risk-less estimates are usually wrong). Skipping security and external risks as "rare". Owner = "the team" (mitigations without named-role owners do not happen).

**Anchor.** Jones BP #14 (14-category risk inventory) + Cagan 4 discovery risks + 7 BP for risk management.

## 10. Early sizing

Function-point size before requirements are complete.

→ **Deep dive: [`fp-sizing.md`](./fp-sizing.md).** The playbook covers the 3 input regimes (pattern matching · light FP · full IFPUG/COSMIC counting), tier-aware release strategy, ISBSG cross-check, growth-rate empirics (1–3 %/month), and the engine's auto-estimate fallback.

## 11. Cost estimating

Effort, cost, schedule, quality — backed by historical benchmarks above 1 000 FP.

**Criteria.**
- Automated tooling above 1 000 FP (CHECKPOINT, COCOMO, SEER, SLIM, Price-S, KnowledgePlan, SoftCost).
- Primary input is function points; quality estimation included.
- Changing requirements factored in (1–3 %/month creep band).
- Historical benchmarks supplied as defence (ISBSG or in-house).
- All overhead included (project management, specs, tracking, defect repair).

**Pitfalls.** Manual estimating on > 10k FP work. Estimating only code (testing, paperwork, defect repair under-estimated). No historical benchmark. Skipping quality estimation.

**Anchor.** Automated estimating tools (COCOMO II, SEER, SLIM, CHECKPOINT) + ISBSG benchmark + quality and risk components.

## 12. Project planning

WBS + activity network + critical path, across three planning horizons.

**Criteria.**
- **Work Breakdown Structure** decomposes to activities estimable and trackable.
- Three GISF horizons coexist: **Roadmap (1–2y) · Release (2–9mo) · Iteration (1–4w)**.
- Critical path identified; slack on non-critical chains named.
- Five most-skipped categories allotted explicitly: requirements analysis · changing requirements · inspections · testing + defect repair · risk reserve.
- Historical benchmark calibration; staff hiring and turnover modelled.

**Pitfalls.** Roadmap-less Agile (iterations finish, releases don't converge). Release-less waterfall (18+ months single release; change absorption catastrophic). No critical path. Implicit 10% buffer absorbing skipped categories.

**Anchor.** Jones's 11 planning best practices + GISF 3-horizon hierarchy + critical-path identification.

## 13. Milestone tracking

Closure of formally reviewed deliverables — not dates.

**Criteria.**
- Milestone = formal review closure of deliverable, not a calendar date.
- Canonical **13-milestone set** covered (or explicitly skipped with rationale): requirements · plan · estimates · design (×3) · QA plan · docs · deployment · training · code inspections · test stages · acceptance.
- No completion claimed without review artifact (minutes, defect log, signoff).
- Strong, immediate reaction to reported problems (surfaced → corrective action).
- Cost tracking parallel to milestone status.

**Pitfalls.** Date-as-milestone. Cosmetic green status (the diagnostic sign of litigated projects). Skimpy reviews (15 minutes on 200 pages is theatre). Problem reports without corrective action.

**Anchor.** Jones's canonical 13 milestones + formal review discipline (not status meetings).

## 14. Benchmarks and baselines

External cross-org comparison + internal SPI snapshot.

**Criteria.**
- Term used precisely: **benchmark** = external cross-org · **baseline** = internal progress snapshot.
- Function-point metrics, not LOC.
- Full benchmark covers **25 topics**; partial covers **10** (FP size · schedule · cost · defect potentials · DRE · staffing · reuse).
- ISBSG cross-check or explicit gap statement (military · embedded · classified sparsely covered).
- Validation discipline matched to source (full on-site validated; ISBSG self-submission unvalidated).

**Pitfalls.** Conflating benchmark and baseline. LOC-only data (cross-language collapses). Trusting ISBSG self-submission without caveat. Skipping FP counting because slow.

**Anchor.** Jones's 25-topic full benchmark + 10-topic partial form + ISBSG.

## 15. Change control

CRs routed through a joint client/development board, quantified in FP.

**Criteria.**
- **Joint Client/Development Change Control Board** evaluates each change; single-sided decisions are litigated-project fingerprint.
- Owners assigned per deliverable (requirements · design · code · manuals · tests).
- Function-point quantification per CR.
- **Re-estimation mandatory above 10 FP** (`instance/thresholds.yaml::change_control`); below 10 FP can absorb but FP count recorded.
- Multi-release assignment (default route for late CRs is next release, not current).

**Pitfalls.** "Small change" without FP quantification. CCB of one. Side-channel edits outside the CR pipeline. Single-release sink (silently consumes slack).

**Anchor.** Jones BP #16 (16-practice change-control inventory) + 10-FP threshold + multi-release segmentation.

---

## Cross-cutting notes

**Out-of-instance frameworks.** This instance does NOT adopt as primary authority: Torres CDH · Christensen JTBD · Doerr OKRs · Rumelt · full Adzic SbE · full Patton USM book chapters beyond Activity/Task/Sub-task · full Cohn USA book chapters beyond INVEST + estimation. If a workflow needs one, the PM surfaces the gap and proposes adding it to `instance/methodology/_out-of-instance/`.

**Numeric thresholds.** Every number in this file (2–10 years vision horizon, 2 %/month churn, 10 FP CR trigger, 25-topic benchmark, 13 canonical milestones, etc.) is canonically duplicated in `instance/thresholds.yaml` so the engine's `forbidden`/`required_fields` validators enforce them mechanically.
