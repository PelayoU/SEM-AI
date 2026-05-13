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

## Sources in `sources/` referenced but not yet used in 15 super-PO skills

- `gisf-delivery-control-and-monitoring.pdf` — Three Ways DevOps, daily stand-up, Release Kanban. Will be relevant when QA / DevOps roles are built (M3 / M5).
- `gisf-delivery-review-and-retrospectives.pdf` — Product Review activities + Retrospective 5 activities + Inspect and Adapt. Will be relevant for retrospective skills (future).
- `gisf-pipeline-devops.pdf` — Deployment pipeline (Humble & Farley), Continuous Integration, Continuous Delivery, Agile testing quadrants. Will be relevant to DevOps role (M5).
- `gisf-agile-teams-and-roles.pdf` — CRACK criteria for PO, Coacher responsibilities, Agile Team Values. Will be relevant when adding more roles (M2 Architect, M4 Developer, etc.).
- `se-best-practices.pdf` (Capers Jones) — Beyond the 11 BPs cited in the 15 super-PO skills (#6, #11, #12, #15, #16, #17, #18, #31, #32, #33, Ch. 1 p. 19 critical topics), the remaining BPs and chapters are not yet used:
  - **Chapter 4 (Specialists)** — to be cited when defining the role catalog rationale.
  - **Chapter 5 (Team Organization)** — same.
  - **Chapter 7 (Requirements, BA, Architecture, Design)** — relevant to Architect role (M2).
  - **Chapter 8 (Programming, Defects)** — relevant to Developer role (M4).
  - **Chapter 9 (Quality + Specialists)** — relevant to QA role (M3).
  - BPs #14, #26, #28, #29, #34, #35, #36, #37, #38, #43 etc. — distributed to Architect, Developer, QA, DevOps, Security roles.
