---
category: skill-references
id: skill-references
status: active
created: 2026-05-13
updated: 2026-05-13
---

# Skill references — academic traceability

For every SEM-IA skill, the specific bibliographic sources that anchor its criteria. This file is for **the human constructor (Pelayo) + external audit** (TFM defense, papers, etc.). AI agents executing a skill do NOT read this file — each `SKILL.md` is self-contained with its `## Source` section.

**Citation convention**: `<pdf-file>` (under `sources/`) + slide / page + section.

The 15 super-Product-Owner skills are organized in four buckets (Strategic, Discovery, Tactical, Process), matching the structure of `.claude/agents/product-owner.md`.

---

## Bucket 1 — Strategic

### po-vision

**Skill**: create / refine / validate the product vision.

**Source layout**:

- ★ **Ten Principles of Product Vision** — Marty Cagan, *Inspired*, captured verbatim in `gisf-discovery.pdf` slide 89.
- ★ **Definition (future 2–10 years, "act of faith")** — `gisf-discovery.pdf` slide 82.
- ★ **Five-step vision construction method** — `gisf-discovery.pdf` slide 86.
- ★ **Vision positioning template (For / Who / The / That / Unlike / Our product)** — `gisf-discovery.pdf` slide 84.
- ★ **Canonical definition of *vision*** — `gisf-life-cycle.pdf` slide 54.
- Complement: Simon Sinek, *Start with Why* (Portfolio, 2009) — origin of "Start with why" (Principle 1). Book itself not in `bibliography/sources/`.

---

### po-goals

**Skill**: create / refine / validate product goals under the vision.

**Source layout**:

- ★ **Canonical definition of *goal*** — `gisf-life-cycle.pdf` slide 54.
- ★ **SMART criteria + "In order to GOAL as STAKEHOLDER I want { capabilities }"** — `gisf-discovery.pdf` slide 95. SMART origin: Doran, G. T. (1981), *There's a S.M.A.R.T. way to write management's goals and objectives*, Management Review (not in `sources/`).
- ★ **Goal-driven leadership stance (Patton quote)** — `gisf-discovery.pdf` slide 94.
- ★ **Popping the "why stack"** — `gisf-discovery.pdf` slide 96.
- ★ **Multilevel hierarchical planning (Roadmap 1–2y / Release 2–9mo / Iteration 1–4w)** — `gisf-delivery-planning.pdf` slide 150.
- Out of audited bibliography: Doerr, *Measure What Matters* (OKR framework). Not cited as authority; available as future addition.

---

### po-capabilities

**Skill**: derive / refine / validate capabilities under a goal.

**Source layout**:

- ★ **Canonical definition of *capability*** — `gisf-life-cycle.pdf` slide 54 (*"Gives stakeholders the ability to achieve some goal or fulfill some task, regardless of implementation. Don't imply a particular implementation."*).
- ★ **Capability filtering → MVP → Go/No-go** — `gisf-life-cycle.pdf` slide 69.
- ★ **Capability listing format ("In order to / as / I want { … }")** — `gisf-discovery.pdf` slides 97–99.
- ★ **Pyramid Vision → Goals → Capabilities → Features → Stories → AC → Examples** — `gisf-life-cycle.pdf` slide 53; restated in `gisf-delivery-backlog-management.pdf` slide 121.
- ★ **Cagan four risks (Go/No-go discriminator)** — `gisf-life-cycle.pdf` slide 64.

---

### po-value-analysis

**Skill**: assess tangible + intangible value of capabilities / features.

**Source layout**:

- ★ **Best Practice #18 — *Software Project Value Analysis*** — Capers Jones, *Software Engineering Best Practices* (McGraw-Hill 2010), pp. 83–84. Tangible Financial Value (10 items) + Intangible Value (9 items) + value-point metric scaling (financial = $1,000; per-customer ≈ 10 value points; logarithmic for priceless items).
- ★ **Cagan four risks (value / usability / viability / business viability)** — `gisf-life-cycle.pdf` slide 64.
- Out of audited bibliography: Christensen *Jobs to be Done*. Not cited as authority.

---

### po-risk-analysis

**Skill**: identify / classify / mitigate project risks.

**Source layout**:

- ★ **Best Practice #17 — *Software Project Risk Analysis*** — Jones 2010, pp. 81–83. 14-category empirical risk inventory, 7 state-of-the-art practices, size-based escalation (1k FP optional / 10k FP mandatory / 100k FP malpractice), human cognitive limit ~2 variables, automated models ~10.
- ★ **Cagan four risks** — `gisf-life-cycle.pdf` slide 64.
- ★ **Critical-topic status of project management** — Jones 2010, Ch. 1, p. 19.

---

## Bucket 2 — Discovery

### po-requirements-discovery

**Skill**: elicit / analyze / validate software requirements.

**Source layout**:

- ★ **Best Practice #11 — *Requirements of Software Applications*** — Jones 2010, pp. 70–72. 14 state-of-the-art practices (JAD, QFD, prototypes, legacy mining, full-time user, requirements inspections, change control board, traceability, multirelease, automated tools, etc.); 2%/month churn empirics; 80% replacement case; success/failure determined at requirements phase (p. 73).
- ★ **Definition of requirements through "Features/stories" as deliverable functionality** — `gisf-life-cycle.pdf` slide 54.
- Out of audited bibliography: Teresa Torres, *Continuous Discovery Habits* (Opportunity Solution Tree). Not cited as authority.

---

### po-user-involvement

**Skill**: design and manage user participation throughout the project.

**Source layout**:

- ★ **Best Practice #12 — *User Involvement in Software Projects*** — Jones 2010, pp. 72–74. 12-form inventory (JAD, QFD, legacy review, embedded full-time, requirements review, change control board, contractor doc reviews, design reviews, prototypes, training, defect reporting, acceptance testing); user-effort ratio 5%–50% (avg 20%, satisfaction risk below 10%); scale rules (embedded for small / surveys + focus groups + usability labs for mass-user); "no one-size-fits-all" closing.
- ★ **Stakeholder decomposition (Future Users / Indirectly Affected / Decision Makers and Blockers)** — `gisf-discovery.pdf` slides 78–80.
- ★ **Persona sketches** — Jeff Patton, *User Story Mapping* (O'Reilly, 2014). Concept summary in `user-story-mapping.pdf` p. 1.

---

## Bucket 3 — Tactical

### po-feature-decomposition

**Skill**: decompose capability into features, feature into stories.

**Source layout**:

- ★ **Canonical definition (features/stories at same level)** — `gisf-life-cycle.pdf` slide 54 (also `gisf-delivery-backlog-management.pdf` slide 121).
- ★ **Cohn story format (*As / I want / so that*)** — `gisf-delivery-backlog-management.pdf` slide 124. Origin: Mike Cohn, *User Stories Applied* (Addison-Wesley, 2004) — book itself not in `sources/`.
- ★ **INVEST criteria (literal)** — `gisf-delivery-backlog-management.pdf` slide 128. Origin attribution: Bill Wake (2003).
- ★ **5 Cs cycle (Card / Conversation / Confirmation / Construction / Consequences)** — `gisf-life-cycle.pdf` slide 56 (cites Antonio Machado) + `agile-story-essentials.pdf` p. 1.
- ★ **Stories are for telling — origin Kent Beck late 1990s** — `agile-story-essentials.pdf` p. 1.
- ★ **Shared Understanding ≠ Shared Documents** — `agile-story-essentials.pdf` p. 1.
- ★ **User Story Map structure (Activity / Task / Sub-task; backbone narrative flow; release slices; "think cake" / "da Vinci" splitting)** — `user-story-mapping.pdf` pp. 1–2; restated in `gisf-delivery-backlog-management.pdf` slide 132.
- ★ **PBI types (Feature, Change, Defect, Technical improvement, Knowledge acquisition)** — `gisf-delivery-backlog-management.pdf` slide 137.

---

### po-spec-gherkin

**Skill**: produce or refine the Gherkin spec for a feature.

**Source layout**:

- ★ **Examples → Acceptance Criteria of a feature** — `gisf-life-cycle.pdf` slide 54.
- ★ **Worked Gherkin example ("Transferring money between accounts", two Scenarios)** — `gisf-delivery-backlog-management.pdf` slide 126.
- ★ **Gherkin reference (Cucumber official) — primary and secondary keywords, Feature, Rule (v6+), Example/Scenario, Given/When/Then/And/But, Background, Scenario Outline + Examples, Doc Strings (`"""`), Data Tables (`|`), Tags (`@`), Comments (`#`), one Feature per file, localised languages** — `gherkin-reference.pdf` pp. 1–9.
- ★ **"Before you build, agree on what test confirms done"** — `agile-story-essentials.pdf` p. 1.
- Out of audited bibliography: Gojko Adzic, *Specification by Example* (Manning, 2011). Concept captured via GISF slide 126; book not in `sources/`.

---

### po-change-control

**Skill**: manage scope changes before release.

**Source layout**:

- ★ **Best Practice #33 — *Software Change Control Before Release*** — Jones 2010, pp. 117–119. 16 state-of-the-art practices (owners, locked masters, multi-release planning, FP-quantified changes, joint client/dev CCB, JAD/inspections/prototypes upstream, automated tools, etc.); 1%–3%/month change-rate empirics; 50% cumulative growth; 10-FP re-estimation threshold; JAD reduces unplanned changes below 1%/month; cross-artifact ripple inventory.
- ★ **Critical-topic status of change control** — Jones 2010, Ch. 1, p. 19.
- Cross-references: `po-requirements-discovery` (BP #11), `po-cost-estimating` (BP #16 for re-estimation), `po-risk-analysis` (category 6 — requirements churn).

---

## Bucket 4 — Process

### po-early-sizing

**Skill**: size the application early.

**Source layout**:

- ★ **Best Practice #6 — *Early Sizing and Scope Control of Software Applications*** — Jones 2010, pp. 51–53. FP best practice / LOC malpractice; pattern matching for novel applications; light FP analysis (minutes vs ~400 FP/day for full count); ISBSG critical mass ~5,000 applications; tier-based release strategy (1k single, 10k–100k multi-release at 12–18 months, Agile sprints 100–200 FP); growth-rate prediction.
- ★ **ISBSG reference** — Jones 2010 BP #31, pp. 113–114 (depth in `po-benchmarks-baselines`).
- ★ **Growth-rate empirics (1%–3%/month, 50% cumulative)** — Jones 2010 BP #11, p. 71.

---

### po-cost-estimating

**Skill**: estimate effort, cost, schedule, quality.

**Source layout**:

- ★ **Best Practice #16 — *Software Project Cost Estimating*** — Jones 2010, pp. 79–81. Manual ≈ automated below 1,000 FP; automated mandatory above 10,000 FP (manual = malpractice); 14 state-of-the-art elements (FP-primary sizing, LOC secondary, screens/reports tertiary, reusable materials, supply chain, travel, benchmark comparison, trained specialists, tools CHECKPOINT/COCOMO/KnowledgePlan/Price-S/SEER/SLIM/SoftCost, changing requirements, quality, risk, PM tasks, plans/specs/tracking); manual estimates 95% optimistic on test schedules >10k FP; political-rejection-of-accurate-estimate ⇒ 80% failure / 99% overrun.
- ★ **Historical benchmarks as defense** — Jones 2010 BP #31, pp. 112–115 (depth in `po-benchmarks-baselines`).
- ★ **Critical-topic status of quality + project management** — Jones 2010, Ch. 1, p. 19.

---

### po-project-planning

**Skill**: create and maintain the project plan (WBS, activity network, critical path).

**Source layout**:

- ★ **Best Practice #15 — *Software Project Planning*** — Jones 2010, pp. 77–79. 11 state-of-the-art elements (WBS, historical benchmarks, project office, staff turnover, automated tools Artemis/MS Project, requirements time, change time, multirelease, outsourcing, supply chain, quality, risk); 5 common planning failures (change handling, staff turnover, requirements time, inspections/testing time, ignored risks); planning vs estimating distinction.
- ★ **Multilevel hierarchical planning (Roadmap 1–2y / Release 2–9mo / Iteration 1–4w)** — `gisf-delivery-planning.pdf` slide 150.
- ★ **Critical-topic status of project management** — Jones 2010, Ch. 1, p. 19.

---

### po-milestone-tracking

**Skill**: track progress against milestones; react strongly to surfaced problems.

**Source layout**:

- ★ **Best Practice #32 — *Software Project Milestone and Cost Tracking*** — Jones 2010, pp. 115–117. Milestone = formal closure of reviewed deliverable (NOT calendar date); 13 canonical milestones for 10k FP project (requirements review, project plan review, cost/quality estimate review, external/database/internal design reviews, quality+test plan reviews, doc plan, deployment plan, training plan, code inspections, each test stage, customer acceptance test); strong-reaction-to-problems mandate; cosmetic green status diagnostic of litigated projects; "project tracking was inadequate in every case" (Jones p. 116).
- ★ **Critical-topic status of project management (tracking is its operational expression)** — Jones 2010, Ch. 1, p. 19.

---

### po-benchmarks-baselines

**Skill**: establish and compare against benchmarks and baselines.

**Source layout**:

- ★ **Best Practice #31 — *Software Benchmarks and Baselines*** — Jones 2010, pp. 112–115. Benchmark / baseline distinction; 25-topic full inventory + 10-topic partial; ISBSG ~5,000 projects (+500/year), IT/web-weighted, military classified absent; full on-site ~2 days vs remote partial ~2–3 hours; FP variants (IFPUG, COSMIC, Finnish, Netherlands); self-submission lack-of-validation caveat; "every major project should start by reviewing benchmark information" + "every process improvement plan should start by creating a quantitative baseline" mandates.
- ★ **High-speed FP methods (pattern matching, light FP analysis)** — Jones 2010 BP #6, pp. 51–52 (depth in `po-early-sizing`).
- ★ **Benchmarks as defense for estimates** — Jones 2010 BP #16, p. 80 (depth in `po-cost-estimating`).

---

## Summary — sources NOT cited as authority

The following sources were referenced in the earlier (pre-reset) skill set or in design discussions but are NOT present in `bibliography/sources/`. Therefore the current 15 skills do not cite them as authority; if they are added to `sources/` in the future, the relevant skills are updated and this section reflects it.

- **Cagan, *Inspired* + *Empowered*** (Wiley) — the books themselves are not in `sources/`. The 10 Vision Principles and the 4-risks framework are captured in GISF `gisf-discovery.pdf` slide 89 and `gisf-life-cycle.pdf` slide 64 respectively. Skills cite GISF as the immediate source.
- **Sinek, *Start with Why*** (Portfolio, 2009) — not in `sources/`. The "Start with why" Principle 1 of Cagan's Ten Vision Principles is captured via GISF slide 89.
- **Rumelt, *Good Strategy / Bad Strategy*** — not in `sources/`. Not cited as authority.
- **Doerr, *Measure What Matters*** (OKR framework) — not in `sources/`. Mentioned only as an out-of-bibliography note in `po-goals`.
- **Doran (1981), SMART** — original 1981 article not in `sources/`; SMART captured verbatim in `gisf-discovery.pdf` slide 95 and cited from there.
- **Torres, *Continuous Discovery Habits*** (OST) — not in `sources/`. Mentioned only as out-of-bibliography in `po-requirements-discovery`.
- **Christensen, Jobs to be Done** — not in `sources/`. Mentioned only as out-of-bibliography in `po-value-analysis`.
- **Adzic, *Specification by Example*** — book not in `sources/`. The SbE concept is captured via GISF slide 126; the executable Gherkin form via `gherkin-reference.pdf`. Skills cite these.
- **Cohn, *User Stories Applied*** — book not in `sources/`. Cohn's story format is captured in GISF `gisf-delivery-backlog-management.pdf` slide 124.
- **Wake, INVEST origin** — INVEST captured verbatim in `gisf-delivery-backlog-management.pdf` slide 128.
- **Patton, *User Story Mapping*** (O'Reilly 2014) — concept summary in `user-story-mapping.pdf` (pp. 1–2 of the Story Map Concepts handout, Comakers 2013); the full book is not in `sources/`. Cited skills use the handout pages.
- **Kent Beck, *Extreme Programming Explained*** — book not in `sources/`. Late-1990s origin of stories as "tokens for conversation" captured in `agile-story-essentials.pdf` p. 1.

---

# M2 — Architect (5 skills)

5 Architect skills in 3 buckets, matching `.claude/agents/architect.md`. Tier-2 role, mandatory above ~10,000 FP.

## Bucket — Structural

### architect-architecture-design

**Skill**: draft / refine / audit application architecture against the seven fundamental topics and Zachman schema.

**Source layout**:

- ★ **Best Practice #14 — *Software Architecture and Design*** — Capers Jones, *Software Engineering Best Practices* (McGraw-Hill 2010), pp. 75–77. Size-driven importance, Zachman 6×6 schema (Table 2-2), 40+ design notation alternatives, reusable design patterns, industry portfolio similarity ~80%.
- ★ **Chapter 7 § *Software Architecture*** — Jones 2010, pp. 470–475. Seven fundamental topics (overall structure / data structure / interfaces / decomposition / linkage / performance / security); Table 7-7 size-importance scaling (1 FP: not needed; 1,000 FP: useful; 10,000 FP: important; 100,000 FP: critical); architectural-style evolution (Dijkstra/Parnas 1968 → Mary Shaw / David Garlan); modern styles (monolithic / client-server / 3-tier / N-tier / event-driven / peer-to-peer / model-driven / pattern-based / SOA / cloud); architect assignment scope 5,000–100,000 FP; Jones's explicit warning that style-evaluation criteria are "too hazy" for universal verdicts (p. 474).
- ★ **Chapter 9 Table 9-23** — Jones 2010, p. 621. Architect impact: 100,000 FP assignment scope, defect prevention 17%, defect removal 12%. Enterprise Architect: 250,000 FP, 25%, 20%.
- Out of audited bibliography (cited as convention only, not authority): Nygard, *Documenting Architecture Decisions* (ADRs); Bass, *Software Architecture in Practice* (quality attributes); Ford, *Building Evolutionary Architectures* (fitness functions); Ousterhout, *Philosophy of Software Design*; Martin, *Clean Architecture*.

### architect-methodology-selection

**Skill**: select a development methodology or methodology mix using a five-axis suitability matrix.

**Source layout**:

- ★ **Best Practice #9 — *Selecting Software Methods, Tools, and Practices*** — Jones 2010, pp. 59–61. Full methodology list (~18: Agile, clean-room, Crystal, DSDM, XP, hybrid, iterative, OO, pattern-based, PSP, RAD, RUP, spiral, structured, TSP, V-model, waterfall); partial method list (~10: code inspections, data-state design, design inspections, flow-based programming, JAD, Lean Six Sigma, pair programming, QFD, requirements inspections, Six Sigma for software); five-axis suitability evaluation (size / type / nature / attribute / activity); hybrid permission; benchmark-as-input mandate; "fad-driven adoption" failure mode.
- ★ **ISBSG benchmark reference** — Jones BP #31 (depth in `po-benchmarks-baselines`).
- ★ **Legacy-replacement reality** (~80% of new applications) — Jones BP #11, p. 70.

## Bucket — Reuse

### architect-reusability-strategy

**Skill**: plan reuse across the 15 reusable artifact types with explicit ROI swing awareness.

**Source layout**:

- ★ **Best Practice #26 — *Software Reusability*** — Jones 2010, pp. 99–101. 15 reusable artifact inventory (architecture, requirements, source code, designs, help, data, training, cost estimates, screens, project plans, test plans, test cases, test scripts, user documents, human interfaces); quality precondition list (inspections + static analysis + testing + certification certificates); tracking column requirements (customers, defects, releases, certifications, updates); ±300% ROI swing empirics; <25% industry-average reuse vs >85% target / >95% for common types; SOA / OO class library / ERP skepticism; outsource vendor reuse pattern (~50%+).
- ★ **Pattern-rich industry similarity** (~80%) — Jones BP #14, p. 77 (depth in `architect-architecture-design`).
- ★ **Reuse certification cross-reference** — Jones BP #27 (depth in `architect-reuse-certification`).

### architect-reuse-certification

**Skill**: certification gate for admitting candidate reusable artifacts.

**Source layout**:

- ★ **Best Practice #27 — *Certification of Reusable Materials*** — Jones 2010, pp. 101–103. Two-edged-sword framing; central certification authority model (Underwriters-Laboratories-like); 11 supporting-practice inventory (taxonomy, standard interfaces, HELP text, test cases + scripts, defect repository, source identification, change records, variation records, distribution records, charging method, warranties); security caveats including deliberate back doors (p. 102); Table 2-4 economic value of certified reuse on a 10,000-FP application (p. 103).
- ★ **15 reusable artifact types + ±300% ROI swing cross-reference** — Jones BP #26 (depth in `architect-reusability-strategy`).

## Bucket — Quality

### architect-performance-analysis

**Skill**: plan + execute performance analysis with profiling, instrumentation, and the perf↔quality↔security overlap.

**Source layout**:

- ★ **Best Practice #39 — *Software Performance Analysis*** — Jones 2010, pp. 134–135. Profiler / instrumentation / dynamic-analysis tool inventory; instrumentation-overhead caveat; heisenbug / bohrbug / mandelbug / schrodenbug taxonomy (named after Heisenberg / Bohr / Mandelbrot / Schrödinger); performance↔quality↔security overlap (Jones: "performance best practices overlap best practices in quality control and security control"); mean-time-to-failure framing; business-cycle effects (quarter-end / year-end); specialist threshold above 100,000 FP.
- ★ **Chapter 9 Table 9-23** — Jones 2010, p. 621. Performance Specialist: 20,000 FP assignment scope, defect prevention 10%, defect removal 12%.
- ★ **Cross-reference: architecture decides the performance budget** — Jones Ch 7 § Software Architecture, topic 6 (depth in `architect-architecture-design`).

---

# M3 — QA (5 skills)

5 QA skills in 2 buckets, matching `.claude/agents/qa.md`. Tier-2 role, mandatory above ~2,500 FP. **Independence imperative**: reports to senior VP of quality outside dev chain (Jones Ch 5 p. 282).

## Bucket — Program

### qa-sqa-program

**Skill**: design / audit the SQA organization.

**Source layout**:

- ★ **Best Practice #35 — *SQA*** — Capers Jones 2010, pp. 120–124. 12-role SQA inventory; IBM independence model; 3–5% staff ratio; release approval authority + appeal path; 9 cost-of-quality components; economic value of quality empirics (120 delivered defects ≈ 1 maintenance FTE, 240 ≈ 1 customer support FTE).
- ★ **Chapter 5 § *SQA Organizations*** — Jones 2010, pp. 342–348. Four organizational patterns (50% test-only / 35% true SQA / 10% none / 5% figurehead); 10 traditional SQA activities; 1–3% staff ratio (IBM model); ~5,000 full-time SQA personnel in U.S. (2009); mandatory threshold >2,500 FP.
- ★ **Chapter 5 p. 282** — Independence imperative quote: *"QA personnel need to be protected from coercion ... separate from the development organization all the way up to the level of a senior vice president of quality."*
- ★ **Chapter 9 Table 9-23** — QA: 10k FP scope, 15% defect prevention, 40% defect removal.

### qa-measurements

**Skill**: design the quality + productivity measurement program.

**Source layout**:

- ★ **Best Practice #30 — *Measurements and Metrics*** — Jones 2010, pp. 110–112. 9-measure state-of-the-art inventory (effort, costs, milestone progress, dev productivity, maintenance productivity, requirements churn, defects by origin, DRE, earned value); FP as primary size metric; LOC + cost-per-defect as forbidden metrics; DRE definition + worked example (900 + 100 = 90%); industry-leader >95%, U.S. average ~85%; "measurement is professional malpractice" framing (p. 112).
- ★ **Best Practice #35** — Jones 2010, pp. 120–124. Severity levels; 9 cost-of-quality components; economic-value-of-quality empirics; 5-category defect origins (requirements / design / code / documents / bad fixes).
- ★ **Best Practice #11** — Jones 2010, pp. 70–72. Requirements-churn empirics for measure 6.
- ★ **ISBSG as benchmark source** — Jones BP #31 (depth in `po-benchmarks-baselines`).
- Out-of-bibliography (convention pointers only): Crosby Cost of Quality (cited via Jones BP #35), PMI/IEEE/ISO metric standards.

## Bucket — Removal

### qa-inspections-program

**Skill**: plan / schedule / moderate formal inspections.

**Source layout**:

- ★ **Best Practice #36 — *Inspections and Static Analysis*** — Jones 2010, pp. 124–128. Fagan-origin (IBM 35+ years, Fagan + Priven + Radice + Stewart); 5 inspection preconditions (moderator, recorder, prep time, defect log, no-appraisal-use); 3–6 participants per session; 8 inspectable artifacts (architecture / requirements / design / DB / code / test plan / test case / user doc); per-artifact DRE 65–85% average + 88% peak (Gilb); static analysis ~87% on C/Java family coding defects; defect-origin → optimal-removal table; remote inspections allowed.
- ★ **Chapter 9 Table 9-22** — Jones 2010, pp. 615–617. DRE values: automated static analysis 87% (#1), requirements inspections 85% (#2), external design 85% (#3), internal design 85% (#5), new code inspections 85% (#6), reuse certification 84% (#7), test case inspection 83% (#8), legacy code 83% (#10), architecture inspections 80% (#14), test plan 80% (#15), test script 78% (#16).
- ★ **Chapter 9 Table 9-23** — Inspection Moderators: 1,000 FP scope, 27% defect prevention, 35% defect removal.
- ★ **Cross-reference: requirements defects need requirements inspections** — Jones BP #11.
- Out-of-bibliography (convention pointers only): Tom Gilb books on inspections, IEEE 1028.

### qa-testing-strategy

**Skill**: design the testing portfolio (20+ test forms).

**Source layout**:

- ★ **Best Practice #37 — *Testing and Test Library Control*** — Jones 2010, pp. 128–132. 20+ test forms inventory (developer / specialist-SQA / customer ownership groups); 3–12 forms typically applied; testing-alone cumulative <80% DRE; 20–40% of dev effort; black/white/gray box framing; defect prevention list (18 practices); defect removal list (17 practices); test-library hygiene (Jones: more errors in test cases than in software in some IBM samples); test coverage ~75% typical; successful project 4.0 defects/FP × 95% removal = 0.2 delivered/FP; failing project 7.0/FP × 80% = 1.4 delivered/FP.
- ★ **Chapter 9 Table 9-22** — DRE per test form: PSP/TSP unit 52% (#38), subroutine 50% (#39), system 40% (#42), new function 35% (#43), regression 30% (#44), unit 25% (#45); specialized: virus 98% (#51), spyware 98% (#52), security 90% (#53), penetration 90% (#55), reusability 88% (#56), firewall 87% (#57), performance 80% (#58); user testing: usability 65% (#66), beta 40% (#69), acceptance 25–30% (#70–72).
- ★ **Chapter 9 Table 9-23** — Testers: 10k FP scope, 15% defect prevention, 50% defect removal (highest of any role).
- ★ **Gherkin acceptance contract** — Cucumber `gherkin-reference.pdf` (depth in `po-spec-gherkin`).
- Out-of-bibliography (convention pointers only): IEEE 829 test docs, ISTQB body of knowledge, Crispin/Gregory agile testing quadrants.

### qa-defect-removal-efficiency

**Skill**: compose the DRE program to meet >95% safe / >99% leader target.

**Source layout**:

- ★ **Best Practice #35** — Jones 2010, pp. 120–124. DRE bands (leaders >95%, top performers 95–99%+, U.S. avg ~85%, laggards <50%); 5-category defect origins; severity scale.
- ★ **Best Practice #36 — synergy quote** — Jones 2010, p. 125: *"a combination of formal inspections of requirements and design, static analysis, formal testing by test specialists, and a formal (and active) software quality assurance (SQA) group are the methods most often associated with projects achieving a cumulative defect removal efficiency higher than 99 percent."*
- ★ **Best Practice #37** — Jones 2010, pp. 128–132. Testing alone <80% cumulative; >95% safe minimum requires combination; 18-practice defect prevention list + 17-practice defect removal list; 10k-FP project empirics (4.0 vs 7.0 defects/FP × 95% vs 80% removal).
- ★ **Chapter 9 Table 9-22** — 80 defect removal activities ranked, organized in 6 groups (37 static-analysis-and-inspection avg 66.92%, 8 general testing avg 41.00%, 5 automatic testing avg 45.40%, 15 specialized testing avg 70.07%, 7 user testing avg 42.14%, 8 litigation analysis avg 77.14%); bad-fix injection rate ~5% average.
- ★ **Chapter 9 Table 9-23** — full role-impact data: QA 40%, Testers 50%, Inspection Moderators 35%, Architects 12%, Performance Specialists 12%, Risk Analysts 25%, Six Sigma 30%.
- Out-of-bibliography (convention pointers only): Crosby Cost of Quality, Six Sigma DMAIC, CMMI specific practices, ISO 9000 family.

---

# M4 — Developer (5 skills)

5 Developer skills in 3 buckets, matching `.claude/agents/developer.md`. Tier-1 (core) role: every project has at least one Developer.

## Bucket — Coding

### developer-coding-practices

**Skill**: apply Jones's 13 programming best practices when writing new code.

**Source layout**:

- ★ **Best Practice #28 — *Programming or Coding*** — Capers Jones 2010, pp. 107–109. 13 state-of-the-art coding practices (language selection / structured programming / certified reuse / security / spaghetti-bowl avoidance / complexity minimization / clear comments / static analysis / test cases before-or-concurrent / formal code inspections / re-inspection after change / legacy renovation / error-prone module removal); >700-language inventory; manual-and-error-prone framing; cost analogy (10× yachts, 100× Indy cars); pair-programming evaluation; self-review-does-not-work; reusable-objects as the leverage point.
- ★ **Chapter 8 § *Forms of Programming Defect Prevention*** — Jones 2010, pp. 519–525. Code reuse as prevention (~1/100th defects); patterns as prevention (~50% reduction for inexperienced); inspections as prevention (~80% reduction after participation); static analysis as prevention (~85%+ DRE; ~50 of 2,500 languages supported; ~100 tools).
- ★ **Chapter 9 Table 9-22** — Refactoring 62% DRE (#25); error-prone module analysis 60% DRE (#26).
- Out-of-bibliography (convention pointers only): SPR language taxonomy (www.SPR.com referenced by Jones BP #28 p. 108), Martin Clean Code, GoF design patterns, SOLID, Beck Extreme Programming Explained, McConnell Code Complete.

### developer-reuse-application

**Skill**: apply already-certified reusable artifacts (consumer side; Architect curates the library).

**Source layout**:

- ★ **Best Practice #26 — *Software Reusability*** — Jones 2010, pp. 99–101. 15 reusable artifacts; ±300% ROI swing.
- ★ **Best Practice #27 — *Certification of Reusable Materials*** — Jones 2010, pp. 101–103. Security back-door warning (p. 102); 11 supporting practices; warranty + distribution record requirements.
- ★ **Best Practice #28 — *Programming or Coding*** — Jones 2010, pp. 107–109. Reuse-before-custom rule; custom-coding cost framing.
- ★ **Chapter 8 § *Code reuse as defect prevention*** — Jones 2010, p. 522. Certified reuse ~1/100th custom defect rate; uncertified reuse hazardous → negative ROI; familiarity-gap debugging cost; 50:1 ratio uncertified-to-certified sources.
- Out-of-bibliography (convention pointers only): npm / PyPI / Maven Central reputation signals; SBOM standards.

## Bucket — Removal

### developer-static-analysis

**Skill**: run automated static analysis (~87% DRE on coding defects) as both removal + prevention.

**Source layout**:

- ★ **Best Practice #36 — *Inspections and Static Analysis*** — Jones 2010, pp. 124–128. Static analysis best practice for supported languages; ~87% DRE on common coding defects; false-positive tuning rule; code-inspection-after-static-analysis sequence.
- ★ **Chapter 8 § *Automated static analysis as defect prevention*** — Jones 2010, pp. 523–524. Dual role (removal + prevention); programmer-learning effect; ~50 supported languages out of ~2,500; ~100 tools in 2009; open-source community adoption.
- ★ **Chapter 9 Table 9-22 #1** — Automated static analysis: 87% DRE, 2% bad-fix injection.
- ★ **Chapter 9 p. 618** — Table 9-22 figures are maxima; real-life DRE often less than half.
- Out-of-bibliography (convention pointers only): SonarQube, Coverity, Fortify, FindBugs / SpotBugs, Checkstyle, clang-tidy, pylint, ESLint, Semgrep, OWASP rule sets.

### developer-unit-testing

**Skill**: write and run developer-owned tests (subroutine / module / unit).

**Source layout**:

- ★ **Best Practice #37 — *Testing and Test Library Control*** — Jones 2010, pp. 128–132. Three developer-owned test forms (subroutine ~50% DRE / module / unit 25% plain, 52% PSP/TSP); test cases sometimes have higher error density than code (IBM samples); coverage typically ~75%; black/white/gray box framing; 20–40% of effort.
- ★ **Best Practice #28 — *Programming or Coding*** — Jones 2010, p. 108. Practice 9: test cases before or concurrent with code.
- ★ **Chapter 9 Table 9-22** — PSP/TSP unit testing 3.5 cases/FP, 52% DRE (#38); subroutine 0.25 cases/FP, 50% DRE (#39); XP testing 2.0 cases/FP, 40% DRE (#40); unit testing 3.0 cases/FP, 25% DRE (#45); test-case inspection 83% DRE (#8).
- ★ **Chapter 9 p. 618** — figures are maxima.
- Out-of-bibliography (convention pointers only): xUnit family, ISTQB body of knowledge, Crispin & Gregory agile testing quadrants.

## Bucket — Maintenance

### developer-maintenance

**Skill**: maintain and enhance legacy code under the 23-work-type taxonomy.

**Source layout**:

- ★ **Best Practice #48 — *Software Maintenance and Enhancement*** — Capers Jones 2010, pp. 161–164. 23 work-type taxonomy (enhancements / defect repairs / customer support / error-prone module removal / mandatory changes / complexity analysis / code restructuring / optimization / migration / conversion / reverse engineering / reengineering / dead code removal / dormant app elimination / nationalization / mass updates / refactoring / retirement / field service / vendor reporting / vendor updates); 14+ legacy best-practice inventory; renovate-before-enhance rule; error-prone module rule (5% modules cause 50% defects, surgical removal); maintenance-quality multiplier (120 defects ≈ 1 maintenance FTE, 240 ≈ 1 customer-support FTE); ITIL reference (p. 162); maintenance-outsourcing more successful than development-outsourcing.
- ★ **Best Practice #28 — *Programming or Coding*** — Jones 2010, pp. 107–109. Practice 12 (renovate before enhancement); practice 13 (error-prone module removal).
- ★ **Best Practice #47 — *Software Change Management After Release*** — Jones 2010, p. 160. 10-tool post-release change list (cross-link to future `devops-post-release-change` M5).
- ★ **Chapter 5 Table 5-2** — 23 forms of maintenance work (referenced by catalog; replicated in BP #48 text).
- ★ **Chapter 9 Table 9-22** — Refactoring 62% DRE (#25); error-prone module analysis 60% DRE (#26); legacy code inspections 83% DRE (#10).
- Out-of-bibliography (convention pointers only): ITIL v3/v4 (referenced by Jones p. 162 but spec not in `sources/`), COBIT, Relativity Technologies renovation workbench (named in Jones p. 163).

---

# M5 — DevOps (7 skills)

7 DevOps skills in 4 buckets, matching `.claude/agents/devops.md`. Tier-2 role. Aggregates three Jones specialties (Config Control 1.5% + Maintenance ops portion of 31.5% + Customer Support 2.0%) + Humble & Farley Continuous Delivery body of practice.

## Bucket — Control

### devops-configuration-control

**Source layout**:

- ★ **Best Practice #34** — Jones 2010, p. 119. 1950s DoD weapons-systems origin; mechanical activity supported by automation; covers all deliverables (reqs / specs / code / tests / user docs); unique IDs + cross-deliverable mapping + master-copy locking + formal-method updates; ISO 10007-2003 + IEEE 828-1998 standards; CMM/CMMI key practice area; out-of-scope: judging change value (BP #33).
- Out-of-bibliography (convention pointers only): ISO 10007-2003 full standard; IEEE 828-1998 full standard; CMMI CM process area; git / SVN / Polarion / Jama Connect.

## Bucket — Pipeline

### devops-deployment

**Source layout**:

- ★ **Best Practice #43** — Jones 2010, pp. 154–155. Deployment-is-poorly-covered observation; ERP-class baseline ($1M+ / 12 months / 25 consultants + 30 in-house); 10 deployment best practices; side-by-side run pattern; customization-as-norm for large applications.
- ★ **GISF UC3M `gisf-pipeline-devops.pdf`** — Deployment Pipeline model (slide 30, citing Humble & Farley *Continuous Delivery*); 7-stage model; generic-process detailed instrumentation (slide 32); 5-axis strategy framework (slide 34: branching / build / test / release / deployment); Gitflow worked example (slides 35–38).
- Out-of-bibliography (convention pointers only): Humble & Farley *Continuous Delivery* book; Kim et al *Phoenix Project* / Three Ways; DORA *State of DevOps Report*; Jenkins / GitLab CI / GitHub Actions / ArgoCD / Spinnaker / Tekton.

### devops-releases

**Source layout**:

- ★ **Best Practice #49** — Jones 2010, pp. 164–165. Three release-driving forces; 16 named anti-patterns; 11 theoretical-but-correct best practices; mainframe-vs-PC support dichotomy.
- ★ **Best Practice #45** (cross-link) — release volume drives support volume.
- ★ **GISF UC3M `gisf-pipeline-devops.pdf`** — Release strategies (slide 34).
- Out-of-bibliography (convention pointers only): semantic versioning, release notes conventions, EULA standards.

## Bucket — Customer

### devops-customer-support

**Source layout**:

- ★ **Best Practice #45** — Jones 2010, pp. 157–158. Empirical staffing (1/10kFP, 1/150 customers, drifting to 1/1,000 at scale); 220-defect ≈ 1 support FTE per year multiplier; support-as-most-commonly-outsourced; AI virtual support / e-mail triage / standardized HELP / SOA-reusable HELP scale levers.
- ★ **Best Practice #49** (cross-link) — release-side anti-patterns + practices interacting with support model.
- Out-of-bibliography (convention pointers only): ITIL service desk; Zendesk / Salesforce Service Cloud / Intercom; CSAT / NPS.

## Bucket — Maintenance

### devops-post-release-change

**Source layout**:

- ★ **Best Practice #47** — Jones 2010, pp. 160–161. "Less rigorous than pre-release" observation; spec-staleness empirics (~5 years); 10-tool renovation inventory (complexity / static analysis / error-prone module ID / dead code ID / data mining / code conversion / FP enumeration / renovation workbenches / automated test gen / coverage analysis); inspection-after-renovation rule.
- ★ **Best Practice #48 + BP #28 practice 12** (cross-link) — renovate-before-enhance.
- ★ **Chapter 9 Table 9-22** — DRE values for tool categories.
- Out-of-bibliography (convention pointers only): Relativity Technologies renovation workbench, SonarQube / Coverity / Understand legacy-analysis tooling.

### devops-maintenance-operations

**Source layout**:

- ★ **Best Practice #48** — Jones 2010, pp. 161–164. 23 maintenance work-type taxonomy; ITIL reference (p. 162); 14+ legacy best practices (operational tracking metrics in practices 12–17); maintenance-quality multiplier (120 defects ≈ 1 maintenance FTE); maintenance-outsourcing success rate.
- ★ **Best Practice #35** — Jones 2010, pp. 120–124. Economic-value-of-quality empirics: 120 + 240 defect-multipliers.
- ★ **Chapter 5 Table 5-1** — Maintenance specialists 31.5%; Configuration Control 1.5%; Customer Support 2.0%. DevOps aggregates these.
- ★ **GISF UC3M `gisf-delivery-control-and-monitoring.pdf`** — Release Kanban board (slide 210: To Do / In Progress / Delivered); Release Burn-Up Chart (slide 211); Daily stand-up (slide 93 + slide 240).
- Out-of-bibliography (convention pointers only): ITIL v3/v4 full standard; COBIT; DORA MTTR metric; Google SRE Book.

## Bucket — Retirement

### devops-legacy-retirement

**Source layout**:

- ★ **Best Practice #50** — Jones 2010, pp. 166–167. Long-lifespan empirics (30+ years air traffic control, 20+ years large IT); commercial-vendor sunset anti-patterns (Microsoft/Intuit/Symantec); 8 retirement best practices (mine business rules; survey users; search alternatives; stabilize legacy; SOA evaluation; certified reuse; automated language conversion; static analysis); dead-language problem; replacement-causes-trouble rule.
- ★ **Best Practice #47** (cross-link) — 10-tool inventory applicable to retirement.
- Out-of-bibliography (convention pointers only): Strangler Fig pattern (Fowler), Anti-Corruption Layer (DDD), COBOL-to-Java conversion tools.

---

## Sources in `sources/` referenced but not yet used in 15 super-PO skills

- `gisf-delivery-control-and-monitoring.pdf` — Three Ways DevOps, daily stand-up, Release Kanban. Will be relevant when QA / DevOps roles are built (M3 / M5).
- `gisf-delivery-review-and-retrospectives.pdf` — Product Review activities + Retrospective 5 activities + Inspect and Adapt. Will be relevant for retrospective skills (future).
- `gisf-pipeline-devops.pdf` — Deployment pipeline (Humble & Farley), Continuous Integration, Continuous Delivery, Agile testing quadrants. Will be relevant to DevOps role (M5).
- `gisf-agile-teams-and-roles.pdf` — CRACK criteria for PO, Coacher responsibilities, Agile Team Values. Will be relevant when adding more roles (M2 Architect, M4 Developer, etc.).
- `se-best-practices.pdf` (Capers Jones) — Cumulative BPs cited across all 5 milestones (PO + Architect + QA + Developer + DevOps): #6, #9, #11, #12, #14, #15, #16, #17, #18, #19, #26, #27, #28, #30, #31, #32, #33, #34, #35, #36, #37, #39, #43, #45, #47, #48, #49, #50 (28 of 50 Best Practices used), plus Ch 1 p. 19 critical topics, Ch 5 § SQA Organizations pp. 342–348 + p. 282, Ch 5 Table 5-1 (specialist distribution), Ch 5 Table 5-2 (23 forms of maintenance), Ch 7 § Architecture (pp. 470–475), Ch 8 § Forms of Programming Defect Prevention (pp. 519–525), Ch 9 Table 9-22 (pp. 615–617), Ch 9 Table 9-23 (p. 621). Remaining BPs for future role expansion:
  - **Chapter 4 (Specialists)** — to be cited if the role catalog rationale needs deeper anchoring.
  - **Chapter 5 (Team Organization, beyond SQA Organizations + Table 5-2 already used)** — relevant to future role-design conversations.
  - **Chapter 7 § Requirements + BA + Design** (beyond Architecture already used) — relevant to potential future skills.
  - **Chapter 8 (Programming, Defects, sections beyond Defect Prevention already used)** — relevant to additional Developer skills if scope grows.
  - **Chapter 9 (Quality + Specialists, sections beyond Tables 9-22 + 9-23 already used)** — relevant to deeper QA / Security work.
  - Remaining BPs to distribute (M5 + later): #29 (Governance — non-skill per catalog), #34 (Configuration Control → DevOps M5), #38 (Security → Security Officer), #42 (Threats → Security), #43 (Deployment → DevOps M5), #44 (Customer training → DevOps / PO), #47 (Change Management After Release → DevOps M5, partial use in M4 Developer maintenance), #49 (Updates and Releases → DevOps M5), #50 (Terminating Legacy → DevOps M5).
