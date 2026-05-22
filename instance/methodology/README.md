# `instance/methodology/` — optional methodology playbooks

This directory holds **on-demand reference docs** the agents read when they need deeper material than what is in `.claude/agents/<role>.md`. Each agent.md absorbs the *generic role discipline* (criteria + pitfalls) and points here with `→ Methodology:` lines; this directory holds the **citation pack** — Jones / Cagan / Cohn / Patton / Fagan / Humble & Farley / ANSI-IEEE / Nygard / ISBSG / SRD references with worked examples.

**These files are NOT preloaded into the agent's context.** Loading 2000 lines of methodology at every prompt would defeat the framework's token economy. Agents read these files when:

- A sub-discipline's criteria + pitfalls in `agent.md` are not enough for the work at hand.
- The user asks for a citation or a worked example.
- The user wants to validate against the full bibliographic source.

**Status (v0.2 transition — 2026-05-22).**

The agent.md absorption (Day 1.9) put the *generic role discipline* into each role's identity file, sufficient for almost all workflows. The playbooks below are forward references — most are currently TODO. The first commit that authors one moves its row from TODO to ✓.

| Playbook | Owner role | Status | Anchor |
|---|---|---|---|
| `vision-cagan-10-principles.md` | PM | TODO | Cagan 10 principles + GISF 5-step construction |
| `smart-goals.md` | PM | TODO | SMART + GISF 3 horizons + why-stack |
| `cagan-discovery.md` | PM | TODO | Four-risks filter (value/usability/feasibility/viability) |
| `user-story-mapping.md` | PM | TODO | Cohn INVEST + Patton USM + 5 Cs |
| `gherkin-acs.md` | PM | TODO | Cucumber Gherkin reference + Specification by Example |
| `requirements-discovery-jones-bp14.md` | PM | TODO | Jones 14 practices |
| `user-involvement-12-forms.md` | PM | TODO | Jones 12-form inventory |
| `value-analysis.md` | PM | TODO | Jones 10 tangible + 8 intangible |
| `risk-register-jones14-cagan4.md` | PM | TODO | Jones 14 risk categories + Cagan 4 discovery risks |
| `fp-sizing.md` | PM | ✓ | IFPUG / COSMIC / light FP / pattern matching · ISBSG |
| `cost-estimating.md` | PM | TODO | Automated tools (COCOMO, SEER, SLIM, CHECKPOINT) |
| `project-planning-3-horizons.md` | PM | TODO | Jones 11 BP + GISF 3-horizon + critical-path |
| `milestones-jones13.md` | PM | TODO | Jones canonical 13 milestones |
| `benchmarks-baselines.md` | PM | TODO | Jones 25-topic / 10-topic + ISBSG |
| `change-control-ccb.md` | PM | TODO | Jones BP #16 + 10-FP threshold |
| `architecture-design.md` | Architect | TODO | Jones 7 fundamental topics + Zachman + Nygard ADR + ANSI/IEEE 1471 |
| `methodology-selection.md` | Architect | TODO | Jones 5-axis suitability matrix |
| `performance-analysis.md` | Architect | TODO | Performance↔quality↔security overlap + heisenbug taxonomy |
| `reusability-strategy.md` | Architect | TODO | 15-artifact reuse inventory + ±300% ROI |
| `reuse-certification.md` | Architect | TODO | 11 supporting practices + zero-defect target |
| `coding-practices.md` | Developer | TODO | Jones 13 coding best practices + complexity-ceiling table |
| `static-analysis.md` | Developer | TODO | Per-instance SAST config + DRE empirics |
| `unit-testing.md` | Developer | TODO | Subroutine / module / unit forms + DRE targets |
| `reuse-application.md` | Developer | TODO | Certified-reuse gate + defect-density empirics |
| `maintenance.md` | Developer | TODO | Jones 23-type taxonomy + renovate-before-enhance + 5/50 rule |
| `sqa-program-ibm-model.md` | QA | TODO | IBM-model SQA independence + 10-activity inventory |
| `measurements-9-types.md` | QA | TODO | Jones 9-measure inventory + forbidden-metric list |
| `fagan-inspections.md` | QA | ✓ | Fagan 5-precondition model + participant range + 8 artifact types |
| `testing-strategy.md` | QA | TODO | Jones 20+ test forms + ownership split + cumulative DRE |
| `dre-projection.md` | QA | TODO | Jones 80-activity inventory + cumulative DRE formula |
| `configuration-control.md` | DevOps | TODO | ISO 10007 / IEEE 828 + artifact-type inventory |
| `deployment-pipeline.md` | DevOps | TODO | Humble & Farley 7-stage pipeline + strategy axes |
| `release-practice.md` | DevOps | TODO | 16 anti-patterns + 11 best-practice SLAs + Security gate |
| `post-release-change.md` | DevOps | TODO | Tool-selection criteria + renovation-workbench integration |
| `maintenance-operations.md` | DevOps | TODO | 23 work-type taxonomy + SLA thresholds + 220-defect multiplier |
| `customer-support.md` | DevOps | TODO | Staffing ratios + tier definitions + channel SLAs |
| `legacy-retirement.md` | DevOps | TODO | 8-practice checklist + stabilisation-operations |
| `security-program-jones-bp38.md` | Security Officer | TODO | Jones 8 security practices + IBM independence pattern |
| `srd-requirements-and-inspection.md` | Security Officer | TODO | SRD method + requirements-inspection DRE + Fagan |
| `security-architecture-7th-topic.md` | Security Officer | TODO | 7-topic framework + Principle of Least Authority + capability logic |
| `security-testing-portfolio.md` | Security Officer | TODO | Security testing / ethical hacking / SAST DRE |
| `threat-catalogue.md` | Security Officer | TODO | Named vectors + anti-pattern list + threat-intel partners |

**Authoring convention** (when promoting a TODO row to ✓):

1. Front-matter at top:
   ```yaml
   ---
   title: Function-point sizing
   anchor: Capers Jones — *Software Engineering Best Practices* (2009)
   referenced_by:
     - .claude/agents/product-manager.md § Discipline / 10. Early sizing
     - .claude/agents/product-manager.md § Discipline / 11. Cost estimating
     - .claude/agents/product-manager.md § Discipline / 14. Benchmarks and baselines
   ---
   ```
2. Body sections:
   - `## Method` — the canonical procedure, step-by-step.
   - `## Generic criteria recap` — the same criteria already in agent.md, for self-contained reference.
   - `## Bibliographic anchors` — page / table / slide locators in the audited source.
   - `## Worked example` — a realistic application of the method on a small case.
   - `## Common pitfalls` — repeat from agent.md plus deeper failure modes from the literature.
3. Keep each file ~150-250 lines. If it grows past that, it is probably two playbooks fused — split.

**Out-of-instance references.** Methodology files (Bass, Ford, Ousterhout, Martin, GoF, ITIL, DORA, OWASP, NIST, MITRE, STRIDE/DREAD, OKRs, Torres CDH, etc.) that are NOT in this instance's audited bibliography go in `instance/methodology/_out-of-instance/` as practitioner-convention references; the agent.md gotchas cite them as convention, not authority.
