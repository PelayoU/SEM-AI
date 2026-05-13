---
type: research
id: library-index
title: "Índice bibliográfico — fundamento de skills SEM-IA"
status: draft
created: 2026-04-30
author: pelayo
tags: [bibliography, skills, library-index, coach, product-owner, architect]
---

# Índice bibliográfico — fundamento de skills SEM-IA

Este índice mapea las fuentes bibliográficas que sustentan las skills core del Coach, del Product Owner y del Architect. **Cada fuente tiene su nota completa en `vault/architect/research/library/`** con conceptos, frameworks, citas y aplicabilidad explícita a SEM-IA. Las skills DEBEN referenciar estas notas en su sección "Fundamento bibliográfico" — no se permite knowledge externo no documentado.

## Convención

- Cada nota en `library/` tiene frontmatter con `applicable-roles: [...]` declarando a qué roles aplica.
- Cada skill (`design.md` dentro de su directorio en `.claude/skills/<rol>/<skill>/`) referencia explícitamente `[[library-<id>]]` en su sección "Fundamento bibliográfico".
- Si una skill se construye sin fundamento en library, la materialización formal de la skill (Fase 5 del WA-003) la rechaza.

## Fuentes infraestructurales (Anthropic / Claude Code)

Definen cómo se materializan agentes y skills en el harness.

| ID | Nota | Aplica a |
|---|---|---|
| `library-anthropic-subagents` | [[library/anthropic-subagents]] | Todos los roles (Coach, PO, Architect, Developer, QA, Security Officer, DevOps, etc.) |
| `library-anthropic-skills` | [[library/anthropic-skills]] | Todos los roles |

## Fuentes para el rol Coach

Custodio de la dimensión `strategy`. Skills relacionadas con visión, goals, capabilities, roadmap, strategy review, vision realignment.

| ID | Nota | Conceptos clave que aporta |
|---|---|---|
| `library-cagan-product-vision` | [[library/cagan-product-vision]] | Vision principles (10 de Cagan), customer-centric, durabilidad 5-10 años, ambitious but feasible. |
| `library-doerr-okrs` | [[library/doerr-okrs]] | Objective + Key Results, fórmula "I will [O] as measured by [KR]", target 70%, KRs cuantitativos. |
| `library-doran-smart` | [[library/doran-smart]] | SMART criteria (Specific, Measurable, Assignable, Realistic, Time-related — original 1981). |
| `library-sinek-start-with-why` | [[library/sinek-start-with-why]] | Golden Circle (Why → How → What), inspiración vs. manipulación. |
| `library-rumelt-good-strategy` | [[library/rumelt-good-strategy]] | Kernel de la estrategia: diagnosis + guiding policy + coherent actions. Hallmarks de bad strategy. |
| `library-torres-continuous-discovery` | [[library/torres-continuous-discovery]] | Opportunity Solution Tree, assumption testing, discovery continuo. |
| `library-christensen-jtbd` | [[library/christensen-jtbd]] | Jobs-to-be-Done, dimensiones funcional/emocional/social, "people hire products". |

## Fuentes para el rol Product Owner

Custodio de la dimensión `product`. Skills relacionadas con specs, AC, stories, backlog, discovery.

| ID | Nota | Conceptos clave que aporta |
|---|---|---|
| `library-cohn-user-stories-invest` | [[library/cohn-user-stories-invest]] | Formato story "Como X quiero Y para Z", criterios INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable). |
| `library-adzic-specification-by-example` | [[library/adzic-specification-by-example]] | 7 patrones de SbE, formato Gherkin (Given/When/Then), living documentation, examples → AC. |
| `library-patton-user-story-mapping` | [[library/patton-user-story-mapping]] | Story map (narrative flow horizontal + priority vertical), thin slices, "prioritize outcomes not features". |
| `library-torres-continuous-discovery` | [[library/torres-continuous-discovery]] | (compartido con Coach) Opportunity Solution Tree, assumption tests, conversación continua con usuarios. |
| `library-christensen-jtbd` | [[library/christensen-jtbd]] | (compartido con Coach) JTBD, articulación de jobs en lenguaje "When X, I want Y, so I can Z". |

## Fuentes para el rol Architect

Custodio de la dimensión `technical`. Skills relacionadas con ADRs, viabilidad arquitectónica, coupling, coherencia técnica.

| ID | Nota | Conceptos clave que aporta |
|---|---|---|
| `library-nygard-adr` | [[library/nygard-adr]] | Plantilla canónica ADR (Title, Status, Context, Decision, Consequences). Estados: proposed/accepted/superseded/deprecated. |
| `library-bass-software-architecture` | [[library/bass-software-architecture]] | ASRs, ADD (Attribute-Driven Design), Quality Attributes, ATAM. Arquitectura como conjunto de decisiones. |
| `library-ford-evolutionary-architecture` | [[library/ford-evolutionary-architecture]] | Fitness functions, Conway's Law, evolutionary architecture, appropriate coupling. |
| `library-ousterhout-philosophy-software-design` | [[library/ousterhout-philosophy-software-design]] | Deep modules, information hiding, complexity management, change amplification, cognitive load. |
| `library-martin-clean-architecture` | [[library/martin-clean-architecture]] | The Dependency Rule, SOLID, component principles, screaming architecture. |

## Mapeo skills ↔ fuentes

Cada skill del catálogo (.claude/skills/_pending-later.md y los design.md por skill) declarará formalmente qué fuentes la sustentan. Mapeo orientativo:

### Skills del Coach

| Skill | Fuentes principales | Fuentes secundarias |
|---|---|---|
| `vision-quality-check` | cagan-product-vision, sinek-start-with-why | rumelt-good-strategy, christensen-jtbd |
| `goal-quality-check` (borrador existente) | doerr-okrs, doran-smart | cagan-product-vision |
| `capability-quality-check` | rumelt-good-strategy, torres-continuous-discovery | cagan-product-vision |
| `inception-orchestration` | cagan-product-vision, sinek-start-with-why, doerr-okrs | rumelt-good-strategy |
| `strategy-review` | rumelt-good-strategy, doerr-okrs | cagan-product-vision |
| `vision-realignment` | cagan-product-vision, rumelt-good-strategy | torres-continuous-discovery |
| `goal-decomposition` | doerr-okrs, doran-smart | cagan-product-vision |
| `capability-derivation` | torres-continuous-discovery, rumelt-good-strategy | christensen-jtbd |
| `capability-prioritization` | rumelt-good-strategy, patton-user-story-mapping | torres-continuous-discovery |
| `cross-link-analysis` | (no requiere bibliografía externa — convenciones internas SEM-IA) | — |

### Skills del Product Owner

| Skill | Fuentes principales | Fuentes secundarias |
|---|---|---|
| `spec-writing` | adzic-specification-by-example | cohn-user-stories-invest |
| `discovery-facilitation` | adzic-specification-by-example, torres-continuous-discovery | christensen-jtbd |
| `example-elicitation` | adzic-specification-by-example | torres-continuous-discovery |
| `acceptance-criteria-definition` | adzic-specification-by-example | doran-smart |
| `feature-decomposition` | patton-user-story-mapping, cohn-user-stories-invest | christensen-jtbd |
| `story-writing` | cohn-user-stories-invest | adzic-specification-by-example |
| `backlog-prioritization` | patton-user-story-mapping | rumelt-good-strategy, doerr-okrs |
| `value-effort-estimation` | cohn-user-stories-invest | christensen-jtbd |
| `dependency-mapping` | (convenciones SEM-IA — modelo grafo) | — |
| `feature-quality-check` | cohn-user-stories-invest (INVEST), adzic-specification-by-example | doran-smart |

### Skills del Architect

| Skill | Fuentes principales | Fuentes secundarias |
|---|---|---|
| `capability-viability-review` | bass-software-architecture (QAs, ASRs) | ford-evolutionary-architecture, martin-clean-architecture |
| `feature-viability-review` | bass-software-architecture, ousterhout-philosophy-software-design | martin-clean-architecture, ford-evolutionary-architecture |
| `coupling-detection` | ousterhout-philosophy-software-design (information hiding/leakage), martin-clean-architecture (Dependency Rule) | ford-evolutionary-architecture (appropriate coupling) |
| `adr-writing` | nygard-adr (plantilla canónica) | bass-software-architecture (architectural decisions) |
| `coherence-evaluation` | nygard-adr (estados, supersession), martin-clean-architecture | ford-evolutionary-architecture (fitness functions) |

## Fuentes citadas pero NO desarrolladas en notas propias

Identificadas durante la investigación pero NO con nota detallada en `library/` por uno de estos motivos: cobertura indirecta vía otras notas, alcance fuera del trabajo actual, o priorización para fases futuras.

- **Andy Grove — *"High Output Management"*** (1983). Origen de OKRs. Cobertura suficiente vía Doerr.
- **Eric Ries — *"The Lean Startup"*** (2011). Validated learning, MVP. Conceptos absorbidos en Torres y mencionados en library notes existentes.
- **Dan Olsen — *"The Lean Product Playbook"*** (2015). Product/market fit pyramid. Pendiente para fase futura si capability-prioritization lo necesita.
- **Marty Cagan — *"Empowered"*** (2020). Team topologies. Pendiente.
- **Liz Keogh** — patrones de AC. Pendiente; cobertura suficiente vía Adzic.
- **Daniel Kahneman — *"Thinking, Fast and Slow"*** (2011). Sesgos cognitivos. Pendiente para skill de facilitation avanzada.
- **Aslak Hellesøy / Cucumber school** — Gherkin standards. Cobertura suficiente vía Adzic.

Estas fuentes pueden añadirse a `library/` cuando se construyan skills que las requieran como base principal.

## URLs externas consultadas (por si hay que volver)

- Anthropic Claude Code Subagents: https://code.claude.com/docs/en/sub-agents
- Anthropic Claude Code Skills: https://code.claude.com/docs/en/skills
- Marty Cagan SVPG Vision FAQ: https://www.svpg.com/product-vision-faq/
- John Doerr / What Matters: https://www.whatmatters.com/okrs-explained/what-are-okrs
- SMART criteria Wikipedia (con citación a Doran 1981): https://en.wikipedia.org/wiki/SMART_criteria
- INVEST criteria Agile Alliance: https://agilealliance.org/glossary/invest/
- Specification by Example (Gojko Adzic): https://gojko.net/books/specification-by-example/
- Teresa Torres Opportunity Solution Trees: https://www.producttalk.org/opportunity-solution-trees/
- Jobs to Be Done HBR: https://hbr.org/2016/09/know-your-customers-jobs-to-be-done
- Good Strategy Bad Strategy (Rumelt): https://www.alexmurrell.co.uk/summaries/richard-rumelt-good-strategy-bad-strategy

## Notas para próximas fases del WA-003

- **Fase 2 (catalogación):** validar el mapeo skills ↔ fuentes con el usuario antes de redactar borradores detallados.
- **Fase 3 (borradores):** cada `design.md` dentro de su directorio en `.claude/skills/<rol>/<skill>/` debe citar las fuentes en `library/` con `[[library-<id>]]`. Si una skill propuesta no tiene base bibliográfica clara, proponer creación de nota nueva en `library/` o reformular la skill.
- **Fase 5 (materialización):** los archivos `SKILL.md` finales en `.claude/skills/<rol>/<skill>/` referencian al borrador correspondiente (que vive en el vault) y, opcionalmente, incluyen extractos breves de la bibliografía relevante. La fuente completa permanece en `library/`.
