---
category: design-doc
id: sem-role-catalog
status: draft
created: 2026-05-13
---

# SEM-IA Role Catalog (Layer A — Pure SEM)

Design document derived from Capers Jones (2010) *Software Engineering Best Practices* + GISF UC3M apuntes. Defines the role catalog that constitutes Layer A of SEM-IA: **what roles exist** in software engineering and **what skills each role exercises** — agnostic of whether implemented by humans or AI agents.

This document is the source of truth for `.claude/agents/<role>.md` identity definitions and `.claude/skills/<role>-<skill>/SKILL.md` skill specifications. When implementation diverges from this catalog, this document is updated first; agents/skills follow.

---

## Design principles

1. **Empirical anchoring**. Every role and every skill cites primary bibliographic source. No invention without evidence.
2. **Operational filter**. A role-skill exists only if it can be exercised concretely on artefacts (code, specs, tests, infrastructure). HR/sociological/legal/strategic topics are excluded from the operational catalog — they are policies, not skills.
3. **Domain-agnostic**. Catalog applies equally to FinTech, health-tech, SaaS, gaming, embedded systems. Domain specialization happens through bibliographic complements per skill, not through different roles.
4. **Tiered adoption**. Roles cluster in tiers by project size and complexity. Small projects (<1000 FP) need only Tier 1. Medium (1k–10k FP) add Tier 2. Large (>10k FP) add Tier 3. Very large (>100k FP) add Tier 4.
5. **Quality independence**. Per Jones Ch5 § SQA Organizations, the QA role reports independently of the development chain — this is structural, not stylistic.
6. **No coach as AI agent**. Coacher/Scrum Master functions distribute to (a) the engine codifying the process and (b) the human user playing the coach role. Consistent with modern Cagan *Empowered*.

---

## The 8 roles (5 core + 3 specialized)

**Design rationale for fusion**. The Product Owner absorbs all functions that Jones taxonomy assigns to separate Business Analyst and Project Manager roles. Rationale:

1. **Cagan-consistent**. The modern empowered PO in *Inspired* + *Empowered* explicitly absorbs PM functions (Cagan rejects bureaucratic Scrum/PM overhead). Cagan's "missionary product team" has no BA — BA functions distribute to PO + Designer + Engineers during discovery.
2. **"No Coacher" consistency**. The pre-compact decision to exclude Scrum Master rests on: *engine codifies the process + human plays the coach*. Same logic applies to PM tracking/reporting (engine + bases + queries handle it) and to BA liaison (a bibliographically-anchored AI agent does it well).
3. **Jones ratios are HUMAN ratios**. The empirical recommendation to separate PM/BA/PO at scale (e.g., 75 PMs per 100k FP) stems from human cognitive bandwidth limits. An AI agent does not share those limits.
4. **Skill cohesion preserved**. The risk of fusion is skill blur. Mitigation: organize the PO's skill catalog into 4 explicit scope buckets (Strategic / Discovery / Tactical / Process). Each skill has a precise Anthropic-style description for accurate triggering.

The PO is therefore a "super PO" covering Product Manager + Product Leader + Business Analyst + Project Manager. Jones's BA and PM specialties do not appear as separate SEM-IA roles.

### Tier 1 — Mandatory core (every SEM-IA project)

#### 1. Product Owner (extended super-PO)

**Identity**. Single custodian of product, business analysis, and project management dimensions. Fuses Cagan's Product Manager + Product Leader + Business Analyst + Project Manager. Owns the entire product hierarchy (vision → goals → capabilities → features → stories → specs) AND the process spine (sizing, estimating, planning, tracking, benchmarks) AND the discovery loop (requirements elicitation, JAD facilitation, user involvement, legacy mining).

**Scope**. Product + business + process. The PO is the **default operator** for all 15 skills organized in 4 buckets:

- **Strategic** (5 skills) — vision, goals, capabilities, value analysis, risk analysis
- **Discovery** (2 skills) — requirements discovery, user involvement
- **Tactical** (3 skills) — feature decomposition, spec Gherkin, change control
- **Process** (5 skills) — early sizing, cost estimating, project planning, milestone tracking, benchmarks

In organizations where workload exceeds one PO's effective scope OR where org politics require separation, a separate **Business Analyst** or **Project Manager** role can emerge as a Tier-4 specialization — but this is the exception, not the default.

**Bibliographic basis**.
- Cagan, *Inspired* + *Empowered* (PM + Product Leader fused; rejects bureaucratic PM separation — referenced indirectly via GISF; see `bibliography/skill-references.md`).
- Capers Jones, *SE Best Practices*: BP #6 (Early Sizing & Scope), BP #11 (Requirements — absorbs BA role), BP #12 (User Involvement — absorbs BA liaison), BP #15 (Project Planning — absorbs PM), BP #16 (Cost Estimating — absorbs PM), BP #17 (Risk Analysis), BP #18 (Value Analysis), BP #19 (Cancelling Troubled Projects — postmortem), BP #31 (Benchmarks & Baselines — absorbs PM), BP #32 (Milestone Tracking — absorbs PM), BP #33 (Change Control Before Release).
- GISF UC3M: `gisf-discovery.pdf` (vision principles, Cagan 10 principles), `gisf-life-cycle.pdf` (pyramid Vision→Goals→Capabilities→Features→Stories), `gisf-delivery-planning.pdf` (multilevel hierarchical planning), `gisf-delivery-backlog-management.pdf` (Cohn INVEST, Patton story mapping), `agile-story-essentials.pdf` (5 Cs cycle, conversation > documents), `user-story-mapping.pdf` (Patton process), `gherkin-reference.pdf` (Cucumber Gherkin for spec).

**Equivalent in Jones taxonomy**. Conceptually fuses five Jones specialties: Business analyst (Table 5-1 #10) + Scope manager (#11) + Project planning specialist (#14) + Cost estimating specialist (#17) + senior product decision-making (no direct Jones equivalent — sits above Jones's operational layer).

#### 2. Developer

**Identity**. Builder of production software. Writes code, runs static analysis, writes and runs unit tests, participates in inspections, repairs defects.

**Scope**. Code dimension. From feature implementation through deployment-ready artifact.

**Bibliographic basis**.
- Capers Jones, *SE Best Practices*: BP #28 (Programming/Coding — 13 practices), BP #36 (Inspections & Static Analysis — participates as inspectee + inspector), BP #37 (Testing — developer-side: subroutine, module, unit), BP #48 (Maintenance & Enhancement — operational coding side).
- Chapter 8 § Forms of Programming Defect Prevention: certified code reuse, patterns, inspections, static analysis, TDD, high-level languages, disposable prototypes, structured programming, PSP/TSP measurement discipline. **Synergistic combination > any single method**.
- GISF UC3M: `gisf-delivery-backlog-management.pdf` (story decomposition, INVEST validation as code targets), `gisf-pipeline-devops.pdf` (continuous integration practices), `agile-story-essentials.pdf` (5 Cs cycle).

**Equivalent in Jones taxonomy**. Development software engineers (Table 5-1 #2, 27.5% of staff). The dominant role numerically.

---

### Tier 2 — Strongly recommended (>1000 FP projects)

#### 3. Architect

**Identity**. Custodian of technical dimension. Owns structural decisions, design patterns, performance and security characteristics, technology selection, reusability strategy. Writes and curates Architecture Decision Records (ADRs).

**Scope**. Technical: structure, data, interfaces, decomposition, linkage, performance, security (the 7 fundamental topics from Jones Ch7 § Software Architecture, p.471).

**Bibliographic basis**.
- Capers Jones, *SE Best Practices*: BP #9 (Selecting Methods/Tools/Practices — taxonomy-driven), BP #14 (Architecture & Design — Zachman schema), BP #26 (Reusability — 15 reusable artifacts), BP #27 (Certifying Reusable Materials), BP #39 (Performance Analysis).
- Chapter 7 § Software Architecture (pp.470–475): "Architecture critical >100k FP, important 10–100k FP, useful 1–10k FP". 40+ design methods catalogued (UML, use-cases, flowcharts, Nassi-Schneiderman, Jackson, state-change, etc.). Design inspections most powerful defect removal (Table 5-6).
- Chapter 9 Table 9-23: Architect assignment scope 100,000 FP; defect prevention impact 17%; defect removal impact 12%. Enterprise Architect: 250,000 FP, prevention 25%, removal 20%.
- Nygard, *Documenting Architecture Decisions* (ADR origin — not in Jones bibliography but standard convention).

**Equivalent in Jones taxonomy**. Architects (Table 5-1 #15, 0.4% of staff — 4 per 1000-person org). Enterprise architects separate (Table 9-23 #2).

**Sub-role**. For organizations with >500 applications, **Enterprise Architect** emerges as separate sub-role (1 per ~1000 applications; assignment scope 500k–2M FP).

#### 4. QA (Quality Assurance)

**Identity**. Custodian of quality dimension. Independent from development chain — reports to senior VP of quality, NOT to dev management. Power to recommend against release. Roles: defect estimation, removal efficiency measurement, inspections moderation, root-cause analysis, Six Sigma/QFD facilitation, standards adherence (ISO 9000 etc.).

**Scope**. Quality: prevention (methods, training, embedded users, structured coding) + removal (inspections, static analysis, multi-phase testing). Owns the goal of >95% cumulative defect removal efficiency.

**Bibliographic basis**.
- Capers Jones, *SE Best Practices*: BP #30 (Measurements & Metrics), BP #35 (SQA — 12 SQA roles), BP #36 (Inspections & Static Analysis — moderates), BP #37 (Testing & Test Library Control — strategy).
- Chapter 5 § SQA Organizations (pp.342–348): Independence imperative. SQA staff = 1–3% of dev personnel in the IBM model. **In about 35% of companies SQA reports to its own VP of quality** (best practice); 50% confuse SQA with testing org; 15% have minimal or no SQA.
- Chapter 9: defect prevention + removal combinations approach 99% efficiency. Table 9-22: 80 defect removal activities ranked. Table 9-23: QA assignment scope 10,000 FP; defect removal impact 40% (second only to Testers' 50%).
- GISF UC3M: `gisf-delivery-control-and-monitoring.pdf` (Inspect & Adapt, daily stand-up control), `gherkin-reference.pdf` (acceptance test contract).

**Equivalent in Jones taxonomy**. Quality assurance specialists (Table 5-1 #5, 2.5%) — fuses with Testing specialists (Table 5-1 #3, 12.5%) when org doesn't separate them. Inspection moderators (Table 9-23 #20).

**Critical organizational fact**. *"QA personnel need to be protected from coercion in order to maintain a truly objective view of quality. Therefore, the QA organization needs to be separate from the development organization all the way up to the level of a senior vice president of quality."* (Jones Ch5 p.282).

#### 5. DevOps

**Identity**. Custodian of operations dimension. Owns deployment, configuration control, releases, post-release change management, monitoring, customer-facing operational support, legacy retirement.

**Scope**. From "code merged" to "running in production and through end-of-life". Pipelines, infrastructure as code, observability, incident response.

**Bibliographic basis**.
- Capers Jones, *SE Best Practices*: BP #34 (Configuration Control — ISO 10007, IEEE 828), BP #43 (Deployment & Customization — 11 practices), BP #45 (Customer Support — multi-tier, 1 per 10k FP or 1 per 150 customers), BP #47 (Change Management After Release — 10 tools), BP #48 (Maintenance & Enhancement — operational side; 23 forms of maintenance work, Table 5-2), BP #49 (Updates & Releases), BP #50 (Terminating Legacy).
- GISF UC3M: `gisf-pipeline-devops.pdf` (Humble & Farley *Continuous Delivery* — Three Ways DevOps: Flow, Feedback, Learning; Deployment Pipeline). `gisf-delivery-control-and-monitoring.pdf` (Release Kanban).

**Equivalent in Jones taxonomy**. Configuration control specialists (Table 5-1 #8, 1.5%) + portions of Maintenance specialists (Table 5-1 #1, 31.5%) + Customer support (Table 5-1 #7, 2.0%). Modern DevOps role didn't exist in Jones's 2009 taxonomy but maps cleanly to these three Jones specialties.

---

### Tier 3 — Specialized (specific contexts)

#### 6. Security Officer

**Identity**. Custodian of security dimension. Threat modeling, secure coding standards enforcement, vulnerability management, security inspections, compliance (when intersecting with technical decisions — pure compliance is not a skill).

**Scope**. Security analysis from architecture through deployment. Penetration testing strategy. Incident response (security side).

**Bibliographic basis**.
- Capers Jones, *SE Best Practices*: BP #38 (Security Analysis & Control — 10 practices), BP #42 (Viruses/Spyware/Hacking — threat catalog).
- Chapter 9 Table 9-23: Security specialist assignment scope 50,000 FP; **defect prevention impact 70%** (highest of any role) — security investment pays off massively in prevention.
- Hamer-Hodges, *Authorization Oriented Architecture* (cited in Jones Ch2 p.140); Caja (Google); Principle of Least Authority; capability-based security.
- ISO 17799; the E programming language (high-security).

**Equivalent in Jones taxonomy**. Security specialists (Table 5-1 #23, 0.3% — 3 per 1000-person org). Encryption specialists (Table 5-1 #25, 0.2%) and Risk analysis specialists (Table 9-23 #1) overlap.

#### 7. Designer / UX (optional — Tier 3 for user-facing products)

**Identity**. Custodian of usability dimension. Owns UI/UX design, user flows, interaction patterns, accessibility, usability testing. Participates in requirements via prototypes and user research.

**Scope**. User-facing aspects: screens, interactions, accessibility, end-user documentation strategy.

**Bibliographic basis**.
- Capers Jones, *SE Best Practices*: BP #12 (User Involvement — usability-side), BP #44 (Training Clients).
- Chapter 9 Table 9-23: Usability specialists assignment 100,000 FP; defect prevention 10%; defect removal 15%.
- Patton, *User Story Mapping* (in `bibliography/sources/user-story-mapping.pdf` — narrative flow, slicing).
- Nielsen heuristics, Cooper interaction patterns (not in Jones bibliography; reference for skill complements).

**Equivalent in Jones taxonomy**. User interface specialists (Table 5-1 #16, 0.4%); Usability specialists (Table 9-23 #6); Graphical artists (Table 5-1 #21, 0.3%).

---

### Tier 4 — Emergence exceptions (very large or politically sensitive orgs)

The default SEM-IA catalog has 5 core + 3 specialized = 8 roles. In two specific contexts, the super-PO can split:

**Business Analyst as separate role** — only when:
- Domain is heavily regulated and requires a specialized analyst who deeply knows compliance frameworks (e.g., FDA medical device, banking regulation), AND
- The volume of business-side discovery work exceeds what one PO can handle, AND
- Organizational politics require a stakeholder-facing role distinct from product decision-making.

Bibliographic basis when activated: Jones Ch7 § Business Analysis (pp.468–470); IIBA + BABOK reference.

**Project Manager as separate role** — only when:
- Project size exceeds 100k FP, AND
- Multiple teams need coordination beyond what the PO can track via the graph + bases, AND
- Cost/schedule reporting must go to executives independent of product decisions.

Bibliographic basis when activated: Jones Ch6 (entire chapter); BP #15, #16, #25, #30, #31, #32.

In both cases, the activated role inherits the relevant skills from the PO's catalog (e.g., a separate BA inherits `po-requirements-discovery` + `po-user-involvement`; a separate PM inherits the 5 Process-bucket skills). The skills do not change — only the agent that exercises them.

---

## Roles NOT included as AI agents

The following Jones specialties are **deliberately excluded** from the SEM-IA role catalog:

| Excluded role | Reason |
|---|---|
| Coacher / Scrum Master | Per pre-compact decision: functions distribute to engine + human user. Not an AI agent in SEM-IA. |
| Business Analyst (as separate role) | Absorbed by super-PO. Emerges as separate role only in Tier-4 exception cases (heavily regulated domains + workload overflow + org politics). |
| Project Manager (as separate role) | Absorbed by super-PO. Emerges as separate role only in Tier-4 exception cases (>100k FP + multi-team coordination + independent exec reporting). |
| Executive Management | Sociological (BP #13 explicitly is "Executive Management Support" — not an operational skill). |
| HR / Selection / Hiring | BP #1, #4, #5 are HR policy, not engineering. |
| Compliance Officer | Pure regulatory mapping. When compliance affects technical decisions (encryption, audit logs), Security Officer + Architect handle it. |
| Sales / Marketing / Customer Liaison (non-support) | Outside engineering scope. |
| Technical Writer | Important specialty in Jones (Table 5-1 #6, 2.3%), but in SEM-IA the writing of artifacts (specs, docs, ADRs) is distributed across other roles. Could emerge as Tier 4 role if needed. |
| Maintenance Specialist (separate from Developer) | In Jones the largest specialty (Table 5-1 #1, 31.5%), but in SEM-IA covered by Developer (code maintenance) + DevOps (operational maintenance). May emerge as separate role for organizations with very large legacy portfolios. |
| Performance Specialist | In Jones recommended for >100k FP. In SEM-IA covered by Architect's performance scope. May emerge as separate role for performance-critical domains (HFT, real-time systems). |
| Database Administrator | Recommended in Jones for large data-heavy applications. In SEM-IA covered by Architect (data architecture) + Developer (data access code). May emerge as separate role for data-intensive domains. |

These are all valid software engineering specialties per Jones — exclusion from the SEM-IA AI-agent catalog does NOT mean they don't exist in real organizations. It means they are not operationalized as AI agents in this iteration.

---

## Best Practice → Skill mapping (the 50 BPs)

The following table maps each of Jones's 50 Best Practices to the SEM-IA role and skill that operationalizes it. "NOT a skill" means the BP is sociological, strategic, regulatory, or industry-level and therefore not operationalized as an AI agent skill.

| BP # | Title (Jones, p.) | Role(s) | Skill name | Notes |
|---|---|---|---|---|
| 1 | Minimizing Harm from Layoffs (p.41) | — | NOT a skill | HR policy |
| 2 | Motivation Technical Staff (p.45) | — | NOT a skill | HR policy |
| 3 | Motivation Mgrs/Executives (p.47) | — | NOT a skill | HR policy |
| 4 | Selection & Hiring (p.50) | — | NOT a skill | HR policy |
| 5 | Appraisals & Career Planning (p.50) | — | NOT a skill | HR policy |
| 6 | **Early Sizing & Scope Control (p.51)** | PO | `po-early-sizing` | Northern/Southern Scope methods; function-point sizing; ISBSG benchmarks |
| 7 | Outsourcing (p.53) | — | NOT a skill | Strategic make-vs-buy decision |
| 8 | Contractors & Consultants (p.58) | — | NOT a skill | Strategic |
| 9 | **Selecting Methods/Tools/Practices (p.59)** | Architect | `architect-methodology-selection` | 4-layer software taxonomy + 25-topic methodology taxonomy |
| 10 | Certifying Methods/Tools/Practices (p.64) | — | NOT a skill | Industry-level certification |
| 11 | **Requirements (p.70)** | PO | `po-requirements-discovery` | JAD, QFD, prototypes, legacy mining, requirements inspections, 7 fundamental topics + 30 supplemental from Ch7. Super-PO absorbs BA function here. |
| 12 | **User Involvement (p.72)** | PO (+ Designer for UX side) | `po-user-involvement` | 12 forms: JAD, QFD, focus groups, embedded users, change boards, prototypes, design reviews, doc reviews, defect reporting, acceptance testing, etc. |
| 13 | Executive Mgmt Support (p.74) | — | NOT a skill | Sociological |
| 14 | **Architecture & Design (p.75)** | Architect | `architect-architecture-design` | Zachman schema (6×6 matrix); 7 fundamental topics (structure, data, interfaces, decomposition, linkage, performance, security); design inspections |
| 15 | **Project Planning (p.77)** | PO | `po-project-planning` | WBS, historical benchmarks, 5 common failures to avoid. Super-PO absorbs PM function here. |
| 16 | **Cost Estimating (p.79)** | PO | `po-cost-estimating` | Automated tools mandatory >10k FP (COCOMO/KnowledgePlan/SEER/SLIM/Price-S/SoftCost); manual estimation = malpractice for >10k FP. Super-PO absorbs PM function here. |
| 17 | **Risk Analysis (p.81)** | PO + Architect + Security | `po-risk-analysis` (PO leads, others contribute) | Above 100k FP, failure to perform = professional malpractice |
| 18 | **Value Analysis (p.83)** | PO | `po-value-analysis` | Tangible Financial Value + Intangible Value; value points metric |
| 19 | Cancelling Troubled Projects (p.84) | PO | `po-postmortem` | Formal postmortem, business rule extraction from failed code |
| 20 | Org Structures (p.87) | — | NOT a skill | Organizational design (Table 2-3 staffing patterns is reference data) |
| 21 | Training Mgrs (p.89) | — | NOT a skill | HR |
| 22 | Training Technical Personnel (p.91) | — | NOT a skill | HR (but the 15-topic learning catalog informs skill scope) |
| 23 | Use of Specialists (p.92) | — | NOT a skill | Architectural decision (informs THIS catalog) |
| 24 | Certifying Engineers/Specialists (p.94) | — | NOT a skill | HR + industry certification |
| 25 | **Communication During Projects (p.97)** | All roles | `shared-status-reporting` | "NO SURPRISES" rule (Geneen); 15+ communication channels; monthly exec / weekly client / daily Scrum |
| 26 | **Reusability (p.99)** | Architect + Developer | `architect-reusability-strategy` + `developer-reuse-application` | 15 reusable artifact types; 80% reuse cuts 10k FP TCO from $62M to $12M |
| 27 | **Certifying Reusable Materials (p.101)** | Architect | `architect-reuse-certification` | Certified reuse = best ROI; uncertified reuse = hazardous, negative ROI |
| 28 | **Programming/Coding (p.107)** | Developer | `developer-coding-practices` | 13 practices: language selection, structured programming, certified reuse, security planning, complexity <10 cyclomatic, comments, static analysis, TDD, formal code inspections, etc. |
| 29 | Project Governance (p.109) | — | NOT a skill | SOX legal/regulatory |
| 30 | **Measurements & Metrics (p.110)** | QA + PM | `qa-measurements` | 9 measure types: effort, costs, milestones, productivity, reqs change volume, defects by origin, defect removal efficiency, earned value |
| 31 | **Benchmarks & Baselines (p.112)** | PO | `po-benchmarks-baselines` | 25-topic full benchmark + 10-topic partial; ISBSG remote. Super-PO absorbs PM function here. |
| 32 | **Milestone & Cost Tracking (p.115)** | PO | `po-milestone-tracking` | 13 milestone reviews: req review, plan review, design reviews, test plan review, code inspections, etc. Super-PO absorbs PM function here. |
| 33 | **Change Control Before Release (p.117)** | PO + Architect | `po-change-control` | 16+ practices: owners, locked masters, multi-release planning, JAD/inspections/prototypes for downstream change reduction |
| 34 | **Configuration Control (p.119)** | DevOps | `devops-configuration-control` | ISO 10007-2003; IEEE 828-1998; master copies locked |
| 35 | **SQA (p.120)** | QA | `qa-sqa-program` | 12 SQA roles; independent reporting to senior VP of quality; mandatory >2500 FP |
| 36 | **Inspections & Static Analysis (p.124)** | QA + Developer | `qa-inspections-program` + `developer-static-analysis` | Fagan-origin formal inspections; 65-85% defect removal efficiency vs 35% for testing alone; applies to architecture, requirements, design, DB design, code, test plans, test cases, user docs |
| 37 | **Testing & Test Library Control (p.128)** | QA + Developer | `qa-testing-strategy` + `developer-unit-testing` | 20+ forms of testing; cumulative <80% without inspections; combination of inspections + static analysis + 8-form testing approaches 99% removal |
| 38 | **Security Analysis & Control (p.132)** | Security | `security-analysis` | 10 practices including security inspections, secure languages (E), static analysis for vulnerabilities, formal security plan for internet-connected apps |
| 39 | **Performance Analysis (p.134)** | Architect (or Performance Specialist Tier 4) | `architect-performance-analysis` | Profilers, instrumentation, dynamic analysis; specialist recommended >100k FP |
| 40 | International Standards (p.136) | — | NOT a skill | Compliance reference (ISO 9001, ISO 25030, IEEE 730, etc.) |
| 41 | Protecting IP (p.136) | — | NOT a skill | Legal (NDAs, patents, encryption strategy) |
| 42 | **Viruses/Spyware/Hacking (p.139)** | Security | `security-threat-defense` | Threat catalog: adware, ACLs, back doors, botnets, DoS, hacking, identity theft, malware, phishing, rootkits, spam |
| 43 | **Deployment & Customization (p.154)** | DevOps | `devops-deployment` | 11 practices; ERP-class costs $1M+, 25 consultants + 30 in-house |
| 44 | Training Clients/Users (p.156) | Designer (or Tech Writer Tier 4) | `designer-user-training` | 9 learning material topics |
| 45 | **Customer Support (p.157)** | DevOps | `devops-customer-support` | Multi-tier L0–L3; 1 support per 10k FP or 1 per 150 customers; every 220 latent defects reduced = 1 fewer support person |
| 46 | Warranties & Recalls (p.158) | — | NOT a skill | Legal (EULA, warranty terms) |
| 47 | **Change Mgmt After Release (p.160)** | DevOps + Developer | `devops-post-release-change` + `developer-maintenance` | 10 tools: complexity analysis, static analysis, error-prone module ID, dead code ID, data mining, code conversion, renovation workbenches |
| 48 | **Maintenance & Enhancement (p.161)** | Developer + DevOps | `developer-maintenance` + `devops-maintenance-operations` | 23 forms of maintenance work (Table 5-2); 14 practices; ITIL reference |
| 49 | **Updates & Releases (p.164)** | DevOps | `devops-releases` | 12 anti-patterns + 11 best practices |
| 50 | **Terminating Legacy (p.166)** | DevOps + Architect | `devops-legacy-retirement` | Business rule mining, user surveys, SOA evaluation, automated language conversion |

**Skill count by role**:
- **Product Owner (super-PO)**: **15 skills** in 4 buckets:
  - Strategic (5): `po-vision`, `po-goals`, `po-capabilities`, `po-value-analysis`, `po-risk-analysis`
  - Discovery (2): `po-requirements-discovery`, `po-user-involvement`
  - Tactical (3): `po-feature-decomposition`, `po-spec-gherkin`, `po-change-control`
  - Process (5): `po-early-sizing`, `po-cost-estimating`, `po-project-planning`, `po-milestone-tracking`, `po-benchmarks-baselines`
- **Architect**: ~6 skills (with `architect-enterprise-architecture` for very large orgs)
- **Developer**: ~5 skills
- **QA**: ~5 skills
- **DevOps**: ~7 skills
- **Security** (Tier 3): ~2 skills
- **Designer** (Tier 3): ~2 skills

**Total operational skills**: ~38 skills across 5 core + 2 typical Tier 3 roles.

---

## GISF complements per role

GISF UC3M material complements Jones with modern Cagan, Patton, Cohn, Adzic where Jones is silent or dated. Each skill cites both Jones (primary, empirical) and GISF (complement) where applicable.

| Role | GISF complement focus |
|---|---|
| Product Owner | `gisf-discovery.pdf` (Cagan 10 vision principles, modern Cagan 3 principles); `gisf-life-cycle.pdf` (Vision→Goals→Capabilities→Features→Stories pyramid + Examples→AC flow); `gisf-delivery-planning.pdf` (multilevel hierarchical planning); `gisf-delivery-backlog-management.pdf` (Cohn INVEST + Patton story mapping); `agile-story-essentials.pdf` (5 Cs); `user-story-mapping.pdf` (Patton process) |
| Architect | `gisf-life-cycle.pdf` (Zachman schema + 40+ design methods); ADR convention (Nygard) |
| Developer | `gisf-pipeline-devops.pdf` (CI, deployment pipeline practices); `gisf-life-cycle.pdf` (story format Cohn + INVEST as code targets); `agile-story-essentials.pdf` (5 Cs cycle, conversation > documents) |
| QA | `gherkin-reference.pdf` (Cucumber Gherkin acceptance test contract); `gisf-delivery-control-and-monitoring.pdf` (Inspect & Adapt, control loops); `gisf-delivery-review-and-retrospectives.pdf` (5 retro activities) |
| DevOps | `gisf-pipeline-devops.pdf` (Humble & Farley Three Ways DevOps; Continuous Integration; Continuous Delivery; Agile Testing Quadrants); `gisf-delivery-control-and-monitoring.pdf` (Release Kanban) |
| Security | (Jones is primary; ISO 17799 + Caja + Authorization Oriented Architecture cited from Jones) |
| Designer | `user-story-mapping.pdf` (Patton); Nielsen heuristics + Cooper interaction patterns (not in current bibliography — would be added if Designer skills require depth) |
| Business Analyst | `gisf-delivery-backlog-management.pdf` (requirements decomposition); IIBA + BABOK reference (not in current bibliography) |

---

## Implementation order (milestones)

Per plan file `/Users/pelayo/.claude/plans/hola-estoy-hablando-con-hazy-scroll.md`:

| Milestone | Role | Skills count | Rationale |
|---|---|---|---|
| M1 | **Super Product Owner** | 15 | Most central role; absorbs PM + BA. PO already partially in place (placeholder). All other roles depend on PO outputs. |
| M2 | Architect | ~6 | Architectural decisions enable Developer + QA + DevOps + Security work. |
| M3 | QA | ~5 | Quality is the most economically valuable dimension per Jones (Table 9-23: QA defect removal impact 40%, second only to Testers). Without QA, downstream defect cost overwhelms the system. |
| M4 | Developer | ~5 | Operational; needs PO specs + Architect decisions + QA strategy in place to operate well. |
| M5 | DevOps | ~7 | Operational; needs Developer-produced artifacts + Architect's infrastructure decisions. |
| M6+ (optional) | Security, Designer | ~4 | Activated based on user priority and project complexity. |

---

## Open questions to revisit

1. **Tech Writer**. Jones gives this specialty significant weight (2.3% of staff, separate org for career reasons). Should it become a Tier 3 SEM-IA role, or remain distributed across other roles? Open. Reconsider when documentation production becomes a friction point.

2. **Performance Specialist**. Jones recommends separate for >100k FP. Currently folded into Architect. Reconsider for performance-critical domains.

3. **Maintenance Specialist**. The single largest Jones specialty (31.5%). Currently distributed between Developer (code maintenance) and DevOps (operational). Reconsider for organizations with very large legacy portfolios.

4. **Designer / UX scope**. Currently Tier 3. Could promote to Tier 2 if the SEM-IA project's primary domains are user-facing products (vs. infrastructure, APIs, embedded). Domain-dependent.

5. **Risk Analysis Specialist**. Highest defect prevention impact in Jones Table 9-23 (75%) due to ability to stop bad projects before they start. Currently distributed across PO, Architect, Security. Reconsider for risk-heavy domains (FinTech, defense, medical).

These are not blocking decisions. The Tier 1–2 catalog is sufficient to start implementation.
