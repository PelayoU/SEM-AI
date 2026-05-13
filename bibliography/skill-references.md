---
category: skill-references
id: skill-references
status: active
created: 2026-05-13
updated: 2026-05-13
---

# Skill references — trazabilidad académica

Por cada skill SEM-IA, las fuentes bibliográficas concretas que sustentan sus criterios. Para AUDITORÍA académica + para refinar skills en el futuro (saber dónde profundizar).

Los agentes IA al ejecutar las skills NO leen este archivo — las skills son autosuficientes. Este documento es para el constructor humano (Pelayo) + auditoría externa (defensa TFM, paper, etc.).

**Convención**: cita con `<archivo-pdf>` (en `sources/`) + slide/página + sección del PDF.

---

## po-vision

**Skill**: crear/refinar/validar la visión del proyecto.

**Definición canónica de visión usada por la skill**:
- ★ `gisf-life-cycle.pdf` slide 54 — *"Vision: the statement that provides a high-level guiding direction for the product."*

**Horizonte 2-10 años + "Science Fiction"**:
- ★ `gisf-discovery.pdf` slides 82-83 — Product Vision Future / Science Fiction.

**10 Principios de Product Vision (atribución Cagan literal)**:
- ★ `gisf-discovery.pdf` slide 89 — los 10 principios listados literales en los apuntes UC3M:
  1. Start with why
  2. Fall in love with the problem, not the solution
  3. Don't be afraid to think big, with vision
  4. Don't be afraid to disrupt yourself
  5. Product vision needs to inspire
  6. Determine and adopt relevant and significant trends
  7. Skate where the puck is going, not where it was
  8. Be stubborn in vision, but flexible in details
  9. Keep in mind that any product vision is an act of faith
  10. Evangelize continuously and relentlessly

**Vision positioning template (For/Who/The/That/Unlike/Our product)**:
- ★ `gisf-discovery.pdf` slide 84.

**5 steps "How to do it"**:
- ★ `gisf-discovery.pdf` slide 86.

---

## po-goal

**Skill**: crear/refinar/validar goals bajo la visión.

**Definición canónica**:
- ★ `gisf-life-cycle.pdf` slide 54 — *"Goals: High level concepts for achieve with the product (value to users, value to business o whatever)."*

**Horizonte temporal (Roadmap/Release/Iteration)**:
- ★ `gisf-delivery-planning.pdf` slide 150 — Multilevel Hierarchical planning: Roadmap (1-2 años) / Release (2-9 meses) / Iteration (1-4 semanas).

**Planning principles aplicables**:
- ★ `gisf-delivery-planning.pdf` slide 152 — 7 planning principles.

**Nota crítica**: los criterios "SMART" (Doran 1981) y "OKR" (Doerr) **NO aparecen en los apuntes GISF auditados**. La skill `po-goal` previa los citaba — drift respecto al material bibliográfico actual. Versión refactorizada usa los 6 criterios anclados en la definición canónica SEM-IA + horizonte GISF + lógica deductiva (un goal debe ser específico, medible, etc. — pero esto es convención SEM-IA, no atribución a Doran/Doerr salvo que se añada esa bibliografía a `sources/`).

---

## po-capability

**Skill**: derivar/refinar/validar capabilities bajo un goal.

**Definición canónica literal**:
- ★ `gisf-life-cycle.pdf` slide 54 — *"Capability: Gives stakeholders the ability to achieve some goal or fulfill some task, regardless of implementation. Don't imply a particular implementation."*

**Capability filtering en Delivery (Capability List → MVP)**:
- ★ `gisf-life-cycle.pdf` slide 69.
- `gisf-agile-teams-and-roles.pdf` slide 161.

**Pirámide jerárquica (Vision → Goals → Capabilities → Features → Stories...)**:
- ★ `gisf-life-cycle.pdf` slide 53 (top-down + bottom-up loop).
- `gisf-delivery-backlog-management.pdf` slide 121 (mismas definiciones reiteradas).
- `gisf-delivery-control-and-monitoring.pdf` slide 200 (idem).

**Nota crítica**: la skill previa citaba "Torres Opportunity Solution Tree", "Rumelt coherent action", "Christensen JTBD" — **ninguna de estas fuentes aparece en los apuntes GISF auditados**. Era drift LLM. Versión refactorizada usa exclusivamente la definición canónica SEM-IA + 6 criterios deducidos honestamente (habilidad/no-feature/parent claro/sirve a goal/no solapa/decomponible/coherente).

---

## po-feature

**Skill**: descomponer capability en features + features en stories.

**Definición canónica (features y stories al mismo nivel)**:
- ★ `gisf-life-cycle.pdf` slide 54 — *"Features/stories: What is designed and implemented to deliver capabilities. Are pieces of deliverable product functionality."*

**Story format Cohn (As/I want/So that)**:
- ★ `gisf-delivery-backlog-management.pdf` slide 124.
- ★ `agile-story-essentials.pdf` p.1 (Patton/Comakers 2013).

**INVEST criteria literal**:
- ★ `gisf-delivery-backlog-management.pdf` slide 128 — los 6 criterios listados literales (Independent, Negotiable, Valuable, Estimable, Small sized appropriately, Testable).
- ★ `agile-story-essentials.pdf` p.1 (referencia tangencial).

**Stories are for telling (Kent Beck origen)**:
- ★ `agile-story-essentials.pdf` p.1 — origen late 1990s, "A story is a token for a conversation".

**Shared Understanding ≠ Shared Documents**:
- ★ `agile-story-essentials.pdf` p.1.

**5 Cs Cycle (Card/Conversation/Confirmation/Construction/Consequences)**:
- ★ `gisf-life-cycle.pdf` slide 56 (cita Antonio Machado).
- ★ `agile-story-essentials.pdf` p.1 (expanded).

**User Story Mapping (Patton)**:
- ★ `gisf-delivery-backlog-management.pdf` slide 132 (Epic/Theme/Story estructura).
- ★ `user-story-mapping.pdf` p.2 (Story Map Concepts y Process — 5 pasos: Frame/Map Big Picture/Explore/Slice Viable Releases/Slice Dev Strategy).
- ★ `user-story-mapping.pdf` p.1 (Concept to Delivery pipeline).

**Splitting heuristics ("think cake", "da Vinci opening/mid/end game")**:
- ★ `user-story-mapping.pdf` p.1.

**Cita "The secret to prioritization is to prioritize outcomes and not features"**:
- ★ `user-story-mapping.pdf` p.2.

**Nota**: la skill previa citaba "Christensen JTBD" — **NO está en bibliografía auditada**. Drift LLM. Versión refactorizada lo omite.

---

## po-spec

**Skill**: producir spec Gherkin de una feature.

**Definición canónica de Examples → AC**:
- ★ `gisf-life-cycle.pdf` slide 54 — *"Examples: What is needed to build up an understanding of the features/stories, concrete examples of what the system should do in different situations. These examples can form the basis for the Acceptance criteria of a feature. Examples illustrate how a feature works."*

**Specification by Example (estructura Given/And/When/Then)**:
- ★ `gisf-delivery-backlog-management.pdf` slide 126 — ejemplo "Feature: Transferring money between accounts" con Scenarios completos.
- Referencia GISF al sitio oficial: `cucumber.io/docs/gherkin/reference`.

**Gherkin canónico (Cucumber oficial)**:
- ★ `gherkin-reference.pdf` pp.1-9 — documentación oficial Cucumber:
  - Keywords primary: Feature/Rule/Example/Scenario/Given/When/Then/And/But (p.1-4).
  - Keywords secondary: `"""` Doc Strings / `|` Data Tables / `@` Tags / `#` Comments (p.1, 8).
  - Background (p.5-6) — tips: max 4 líneas, vivid names.
  - Scenario Outline + Examples (p.7).
  - Spoken Languages `# language: <code>` (p.9).
  - Then debe ser observable (p.4).
  - 3-5 steps recommended per Scenario (p.3).

**Conditions of Satisfaction (back of card)**:
- `gisf-delivery-backlog-management.pdf` slide 125.

**"Before you build, agree on what test confirms done"**:
- `agile-story-essentials.pdf` p.1.

**Nota**: la skill previa citaba "Adzic *Specification by Example*" como fuente principal — Adzic **no tiene ficha dedicada en bibliografía auditada**, pero el concepto SbE SÍ aparece en GISF slide 126 y la implementación canónica (Gherkin) está en `gherkin-reference.pdf` (Cucumber oficial). La versión refactorizada cita estas fuentes verificables, NO Adzic libro completo.

---

## shared-cross-link

**Skill**: declarar cross-links del grafo en frontmatter (also-relates-to, depends-on, dimensions-affected).

**Fuentes**: convención SEM-IA pura. No requiere bibliografía externa.

La estructura jerárquica del grafo (parent relationships) está canonizada en:
- ★ `gisf-life-cycle.pdf` slide 53 (pirámide Vision → Goals → Capabilities → Features → Stories → AC → Examples → Artifacts).

El resto (also-relates-to / depends-on / dimensions-affected) es convención propia de SEM-IA para mantener el grafo navegable en Obsidian.

---

## Resumen — fuentes NO usadas (drift previo eliminado)

Las siguientes fuentes aparecían en las skills previas pero **NO tienen ficha en `sources/`** y por tanto NO se citan en las skills refactorizadas:

- **Cagan, *Inspired/Empowered*** — el libro NO está en sources. Solo los 10 principios literales aparecen en `gisf-discovery.pdf` slide 89. Las skills citan los apuntes GISF como fuente de los 10 principios.
- **Sinek, *Start with Why*** — no en sources. El "WHY" aparece en `gisf-discovery.pdf` slide 89 (Principio 1 Cagan: "Start with why") pero no como framework Golden Circle propio.
- **Rumelt, *Good Strategy***— no en sources. Drift LLM completo.
- **Doerr, *Measure What Matters* (OKR)** — no en sources. Drift LLM.
- **Doran 1981 (SMART)** — no en sources. Drift LLM.
- **Torres, *Continuous Discovery* (OST)** — no en sources. Drift LLM.
- **Christensen JTBD** — no en sources. Drift LLM.
- **Adzic, *Specification by Example* (libro)** — no en sources. El concepto SbE aparece en GISF slide 126; el contrato Gherkin en `gherkin-reference.pdf`. Las skills citan estas fuentes verificables.

Si en el futuro se añaden estas fuentes a `sources/`, se actualizan las skills correspondientes y se documenta aquí.

---

## Sources adicionales en biblioteca (referenciadas pero NO citadas en skills actuales)

- `se-best-practices.pdf` — Capers Jones, McGraw-Hill 2010. Solo TOC indexado en INDEX.md. Profundizar cuando una skill futura lo requiera (especialmente Cap 5 multi-rol, Cap 7 architecture, Cap 9 quality).
- `gisf-delivery-control-and-monitoring.pdf` — Three Ways DevOps, daily stand-up, Release Kanban. Relevante a futuras skills de delivery control (QA / DevOps).
- `gisf-delivery-review-and-retrospectives.pdf` — Product Review activities + Retrospective 5 activities + Inspect and Adapt. Relevante a futuras skills de retros (PO o Coach).
- `gisf-pipeline-devops.pdf` — Conducto de Despliegue (Humble & Farley), Integración Continua, Entrega Continua, Agile testing quadrants. Relevante a futuras skills DevOps.
- `gisf-agile-teams-and-roles.pdf` — CRACK criteria PO, Coacher responsibilities, Agile Team Values. Relevante cuando se construya skill de role definition o se añadan roles (Architect, etc.).
