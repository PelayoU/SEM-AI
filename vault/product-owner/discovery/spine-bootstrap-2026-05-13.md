---
type: discovery
id: spine-bootstrap-2026-05-13
title: "Extracción bottom-up completa de la espina dorsal descendente desde el bootstrap"
status: active
created: 2026-05-13
author: product-owner
related-wa: wa-2026-05-13-005
supersedes-discovery: features-bootstrap-batch-extraction-2026-05-12  # WA-004 aborted-reference
related-vision: vision
related-goals: [goal-1-auto-sostenibilidad, goal-2-output-auditable-multirol, goal-3-absorcion-coste-revision, goal-4-rigor-multirol-individual, goal-5-portabilidad, goal-6-articulacion-publica, goal-7-ciclo-vida-producto]
related-capabilities:
  - cap-01-grafo-declarativo-persistente
  - cap-02-multirol-agentes-homologos
  - cap-03-working-agreements-sdlc
  - cap-04-verificacion-multirol-cruzada
  - cap-05-anclaje-bibliografico-skills
  - cap-06-visibilidad-operativa
  - cap-07-inception-greenfield
  - cap-10-articulacion-publica
references:
  - vault/product-owner/discovery/features-bootstrap-batch-extraction-2026-05-12.md  # aborted-reference, Bloques 1-2 heredados
  - vault/product-owner/discovery/capabilities-bootstrap-extraction-2026-05-12.md  # ground truth Job × Pieza × Capability
  - vault/shared/sessions/archive/wa-2026-05-12-004.md  # WA abortado, lección stop-too-early
  - vault/shared/sessions/archive/wa-2026-05-12-003.md  # gaps del sistema procesados (Gap 4 pivot + Gap 6 Filtro PO + Gap 8 modality + Gap 9 filesystem-changes + Gap 10 briefing)
  - vault/shared/sessions/archive/wa-2026-05-12-002.md  # WA capability-creation que produjo las 10 capabilities
  - vault/developer/learnings/2026-05-12-filtro-po-contaminado-anti-patron.md
  - CLAUDE.md  # ground truth del framework
bibliography:
  - Cagan — Inspired (principio 1 solve problems not features, strong PM)
  - Cohn — User Stories Applied (INVEST + formato story)
  - Patton — User Story Mapping (narrative flow + task-level granularity + thin slices)
  - Christensen — Jobs-To-Be-Done (outcome del operador)
  - Adzic — Specification by Example (examples → AC → Gherkin como test mecánico de granularidad)
  - Doran — SMART (1981) criterios AC
  - Ford — Building Evolutionary Architectures (fitness functions, appropriate coupling)
  - Nygard — Documenting Architecture Decisions (ADRs latentes)
  - Ousterhout — A Philosophy of Software Design (deep modules, simple interfaces)
---

# Extracción bottom-up completa de la espina dorsal descendente desde el bootstrap

## Contexto

Este documento es el **output del step-1 del WA-2026-05-13-005** que corrige el approach fallido del WA-2026-05-12-004 (abortado por fiasco stop-too-early en la espina dorsal).

**Diferencia clave con discovery doc del WA-004**: el WA-005 desciende **completamente** desde Features hasta Specs Gherkin formales por feature. El test mecánico Adzic SbE actúa como anti stop-too-early — si una pieza candidata a feature no permite descender a Given/When/Then concreto, NO es feature genuina y se reclasifica a su nivel arquitectónico correcto.

**Heredados del discovery doc del WA-004 aborted-reference**:
- **Bloque 1** (Criterios y convenciones) reutilizado con ajuste mínimo: añadido **1.6 Test mecánico Adzic SbE** como criterio adicional de granularidad.
- **Bloque 2** (Flujo del operador end-to-end en 6 fases con 6 insights cross-cap) reutilizado tal cual.

**Reclasificado en este documento**:
- **Bloque 3** (Reclasificación de piezas-bootstrap en 5 niveles arquitectónicos correctos): donde antes el WA-004 mezcló 46 "features" sin distinguir niveles, aquí cada pieza del bootstrap se mapea a su nivel arquitectónico: Feature genuina | ADR latente | Protocolo operativo | Doc/governance/artefacto curado | Convención técnica.

**Anexo nuevo**: lista cerrada de features genuinas por capability con stories candidatas preview, input directo a step-2a..2h.

---

## Bloque 1 — Criterios y convenciones aplicados

> Heredados del Bloque 1 del WA-004 aborted-reference (criterios bibliográficamente sólidos validados con humano) con **adición de 1.6 Test mecánico Adzic SbE** como criterio adicional anti stop-too-early.

### 1.1 — Granularidad de feature (Cohn INVEST + Patton)

Una feature SEM-IA = **habilidad observable cohesiva descomponible en 2-7 stories** (Cohn `S = Small` + Patton task-level).

- ✅ **Es feature** si: cubre job concreto del operador, contornos observables, materializa capability operant, razonablemente independiente.
- 🔧 **Sub-dividir** si: > 7 stories estimables, jobs heterogéneos, decisiones técnicas ortogonales separables.
- 🔗 **Agrupar** si: < 2 stories estimables y otra pieza hermana cubre el mismo job.

**Anti-patrón**: feature = 1 archivo del bootstrap (sintáctico) o feature = todo un Job (gruesa). Ambos rotos.

### 1.2 — JTBD del operador (anti features-as-output-blind)

Cada feature enuncia el **outcome del operador** (qué consigue + por qué le importa), NO la pieza técnica.

**Operador DOBLE**: humano (ingeniero adoptador) + agente (PO, Architect, etc.). Ambos legítimos.

**Template**: *"El [operador] puede [acción + contexto] de modo que [outcome observable + por qué importa]."*

**Anti-patrón rechazado**: *"Feature: archivo X con identidad Y"* (describe pieza). **Reformulación correcta**: *"El operador agente Y puede arrancar con identidad bibliográfica anclada de modo que opera coherente entre sesiones"*.

Anclaje: Cagan *Inspired* principio 1.

### 1.3 — Distinción features-construidas-por-SEM-IA vs dependencias-del-harness

**Es feature de SEM-IA**: agent files, SKILL.md content, slash commands, governance docs, vault role-first, CLAUDE.md, frontmatter+wikilinks, estados canónicos, workflow templates, estructura WA, library bibliográfica curada.

**NO es feature** (dependencia del harness): Task tool, carga perezosa nativa, prompt cache, Read/Write/Edit/Bash tools, mecanismo CLAUDE.md jerárquico de Claude Code, parser YAML, git, MCP servers.

Las dependencias del harness se declaran como `depends-on-harness:` en frontmatter (campo opcional). Al activarse CAP-H portabilidad, serán absorbidas por adapters (`src/adapters/<harness>/`).

### 1.4 — Convención AC: identificadores únicos + "verificable vía:"

Cada AC enumerado con identificador único (AC-A1, AC-A2, ...) **y** anotación `verificable vía: <mecanismo>`.

Mecanismos válidos: inspección vault | ejecución slash | sesión rol | comportamiento agente observable | inspección archivo | cobertura piezas | comparación pre/post | ejecución subagente focal.

**En specs Gherkin formales** (WA-005): cada AC es un Scenario con Given/When/Then. El identificador (AC-X1) precede al título del Scenario.

Anclaje: Adzic *Specification by Example*.

### 1.5 — Cross-links y parent único en solapamientos

**Reglas**:
1. `parent` único (no lista). En solapamientos cross-cap, decisión PO por **JTBD primario**, no por mecanismo.
2. `also-relates-to`: cross-links cross-cap o cross-feature **explícitos**.
3. `depends-on`: features predecesoras o piezas-del-harness (en campo `depends-on-harness:` separado).
4. `related-adrs`: ADRs latentes apuntados per-feature (lista de candidatos).

Mapping decisión de ownership en los 3 solapamientos detectados:
- Estados canónicos: parent CAP-A (espina dorsal del grafo). CAP-C hereda.
- Skills empaquetadas: parent CAP-E (catálogo). CAP-D declara `depends-on`.
- /wa + Progreso entries: /wa parent CAP-F (mecanismo visibilidad), Progreso parent CAP-C (estructura WA).

### 1.6 — **NUEVO** Test mecánico Adzic SbE como criterio anti stop-too-early

> **Bibliografía**: Adzic (*Specification by Example*) — *"specifications crystallize through concrete examples; if you cannot describe an example, the specification is incomplete"*. Aplicado a granularidad de feature: si una pieza candidata no permite descender a stories → examples → Given/When/Then concretos, no es feature genuina.

**Procedimiento (aplicar en step-2x intra-capability)**:

Para cada pieza candidata a feature:

1. **Intentar `feature-decomposition`**: ¿se puede descomponer en 2-7 stories Cohn INVEST? Si NO → reclasificar.
2. **Por cada story candidata, intentar `spec-writing`**: ¿se puede elicit 3-10 examples concretos del comportamiento esperado? Si NO → reclasificar.
3. **Por cada example, intentar Given/When/Then**: ¿se puede formalizar como Scenario Gherkin con precondición + acción + resultado observable? Si NO → reclasificar.

**Si en cualquiera de los 3 pasos NO se puede descender**: la pieza candidata NO es feature genuina. Reclasificar a su nivel arquitectónico correcto en Bloque 3:
- **Nivel 2 ADR latente** si es decisión arquitectónica con alternatives.
- **Nivel 3 Protocolo operativo** si es comportamiento de un rol declarado en agent file.
- **Nivel 4 Doc/governance/artefacto** si es contenido documental cerrado.
- **Nivel 5 Convención técnica** si es estándar declarativo sin alternatives consideradas.

**El test es MECÁNICO**: el PO NO juzga "¿es feature?" por intuición. Aplica el procedimiento. Si descenso falla, reclasifica. Si descenso funciona, escribe la spec Gherkin formal.

Esto es lo que faltó al WA-004 (stop-too-early). Sin Gherkin formal como test, el PO mezcló 5 niveles bajo "feature". Con Gherkin formal como test, la granularidad es auto-correctiva.

**Anclaje del aprendizaje**: WA-004 aborted-reason (`vault/shared/sessions/archive/wa-2026-05-12-004.md`).

---

## Bloque 2 — Flujo del operador end-to-end

> Heredado del Bloque 2 del WA-004 aborted-reference. Secuencia experiencial canónica desde el primer encuentro del operador humano con SEM-IA hasta el cierre del primer ciclo completo Discovery → Delivery. Sirve de criterio para asignar `also-relates-to` cross-cap a features que cubren momentos adyacentes del flujo.

Iconografía: 🧑 humano · 🤖 agente · ⚡ conjunto.

### Fase 1 — Onboarding (newcomer descubre el framework)

| # | Momento | Capability(s) |
|---|---|---|
| 1.1 | 🧑 Encuentra repo SEM-IA por enlace externo | CAP-J |
| 1.2 | 🧑 Lee README.md raíz (modelo conceptual + reglas operativas) | CAP-J · Nielsen #10 |
| 1.3 | 🧑 Inspecciona estructura del repo (vault role-first) | CAP-A + CAP-J |
| 1.4 | 🧑 Lee CLAUDE.md raíz como entry-point | CAP-J + CAP-G |
| 1.5 | 🧑 `npm install` | (operación runtime) |

### Fase 2 — Inception greenfield (arranque del sistema con vault vacío)

| # | Momento | Capability(s) |
|---|---|---|
| 2.1 | 🧑 `npm run sem` | CAP-B + CAP-G |
| 2.2 | 🤖 PO sesión arranca con identidad cargada | CAP-B + CAP-E |
| 2.3 | 🤖 PO ritual de inicio (Modo 1 paso 1) | CAP-F + CAP-A |
| 2.4 | ⚡ PO presenta panorámica al humano (vacío) | CAP-F · Nielsen #1 |
| 2.5 | 🧑 Humano trae propuesta | CAP-G |
| 2.6 | 🤖 PO clasifica outcome-type | CAP-G + CAP-C |
| 2.7 | 🤖 PO propone cadena de WAs por gaps | CAP-G + CAP-C |

### Fase 3 — Scope-scan multi-rol (reunión flat parallel)

| # | Momento | Capability(s) |
|---|---|---|
| 3.1 | 🤖 PO convoca 5 advisors | CAP-D + CAP-B |
| 3.2 | 🤖 5 advisors en paralelo via Task tool | CAP-D + CAP-E |
| 3.3 | 🤖 PO consolida + aplica Filtro PO (Gap 6) | CAP-D + CAP-E |
| 3.4 | ⚡ PO presenta DECISIONES + preguntas cat-4 | CAP-F + CAP-D |
| 3.5 | 🤖 PO carga template + adapta + escribe WA | CAP-C + CAP-A |
| 3.6 | ⚡ PO presenta WA + humano confirma | CAP-F |

### Fase 4 — Step active de la cadena

| # | Momento | Capability(s) |
|---|---|---|
| 4.1 | 🤖 Rol activo arranca Modo 2 + marca step in-progress | CAP-C + CAP-B |
| 4.2 | 🤖 Conduce step aplicando skills bibliográficas | CAP-E + carga perezosa harness |
| 4.3 | 🤖 Give-and-take mid-step via subagentes | CAP-D + CAP-B |
| 4.4 | 🤖 Produce artefacto en vault | CAP-A + CAP-E |
| 4.5 | 🤖 Marca step done + Progreso + post-step scope-scan | CAP-C + CAP-D + CAP-F |
| 4.6 | 🤖 PO consolida + Filtro PO + decisiones | CAP-D + CAP-F |
| 4.7 | ⚡ Handoff verbal al humano (siguiente rol) | CAP-B |
| 4.8 | 🧑 Humano cambia sesión (`npm run <rol>`) | CAP-B (cognitive load latente) |
| 4.9 | 🤖 Nuevo rol arranca + lee WA + /wa + Progreso | CAP-B + CAP-C + CAP-E + CAP-D (filesystem-changes Gap 9) |
| 4.10 | 🔁 Ciclo repite por cada step | CAP-C |

### Fase 5 — Sign-off `/verify` (cierre del WA)

| # | Momento | Capability(s) |
|---|---|---|
| 5.1 | 🧑 `/verify` | CAP-D + CAP-F |
| 5.2 | 🤖 PO comprueba closure-criteria mecánico | CAP-D |
| 5.3 | 🤖 PO deriva verifiers = {custodian(d)} | CAP-D + CAP-A |
| 5.4 | 🤖 Invoca verificadores en paralelo | CAP-D + CAP-B |
| 5.5 | 🤖 Consolida hallazgos | CAP-D |
| 5.6 | 🤖 Aplica on-close transitions | CAP-D + CAP-A |
| 5.7 | 🤖 Archiva WA | CAP-C + CAP-A |
| 5.8 | ⚡ Confirma al humano | CAP-F |

### Fase 6 — Backlog → Delivery (primera spec implementada)

| # | Momento | Capability(s) |
|---|---|---|
| 6.1 | 🧑 `/status` muestra backlog | CAP-F + CAP-A |
| 6.2 | 🧑 Decide siguiente feature + `npm run sem` | CAP-G + CAP-F |
| 6.3 | 🤖 PO clasifica `feature-build` + verifica precondición | CAP-C |
| 6.4 | 🤖 PO drafta WA `feature-build` | CAP-C |
| 6.5 | ⚡ Humano confirma + handoff a Developer | CAP-B |
| 6.6 | 🤖 Developer implementa con `// @sem-ia:` + `// @ac-coverage:` | CAP-A |
| 6.7 | 🤖 QA cobertura E2E + AC-S* | CAP-D + CAP-A |
| 6.8 | ⚡ `/verify` cierra. on-close: feature ready-for-implementation → implemented | CAP-D + CAP-A |
| 6.9 | 🧑 `/status` ve Dual Track materializado | CAP-F + Cagan/Patton |

### Insights del flujo del operador (criterios cross-cap)

1. **Onboarding (Fase 1) y CAP-J son indistinguibles** desde el operador. Features de README + glosario + ruta lectura cubren el momento newcomer.
2. **Inception (Fase 2) y CAP-F son co-emergentes**: ritual de inicio del PO + panorámica son simultáneamente procedimiento (parent CAP-G) y output visible (parent CAP-F). Ownership por enunciado JTBD.
3. **Scope-scan (Fase 3) y CAP-D vistos desde dos lentes**: 3 checkpoints uniformes de CAP-D + Filtro PO cruzan a CAP-F (visibilidad al humano).
4. **Step active (Fase 4) cruza CAP-B (rol) + CAP-C (WA) + CAP-E (skills) + CAP-A (artefactos)**: features de Fase 4 típicamente 2-3 `also-relates-to` cross-cap.
5. **Sign-off (Fase 5) es CAP-D + CAP-A (lifecycle)**: algoritmo verifiers + on-close transitions tocan estados canónicos del nodo.
6. **Dual Track (Fase 6) emerge de CAP-C + CAP-F + CAP-A**: propiedad arquitectónica emergente, materializada en `/status` + backlog query.

---

## Bloque 3 — Reclasificación de piezas-bootstrap en 5 niveles arquitectónicos

> Donde el WA-004 mezcló 46 piezas bajo "feature" sin distinguir niveles, aquí cada pieza se mapea a su nivel arquitectónico correcto aplicando el test mecánico Adzic SbE de 1.6.

### Definición operativa de los 5 niveles

| # | Nivel | Define | Vive en | Test mecánico |
|---|---|---|---|---|
| 1 | **Feature genuina** | Capacidad/comportamiento entregable al operador, descomponible en 2-7 stories Cohn INVEST | `vault/product-owner/specs/feature-*.md` → stories → specs Gherkin | Pasa test 1.6 — descenso a Given/When/Then concreto |
| 2 | **ADR latente** | Decisión arquitectónica con alternatives consideradas y consecuencias auditables | `vault/architect/adrs/adr-*.md` (cuando se materialice en Lote B) | Falla test 1.6 al intentar stories — emerge razón Nygard |
| 3 | **Protocolo operativo** | Comportamiento canónico de un rol declarado en su agent file (no descomponible en stories de delivery) | `.claude/agents/<rol>.md` (ya formalizado) | Falla test 1.6 — vive como regla declarativa |
| 4 | **Doc/governance/artefacto curado** | Contenido documental cerrado del bootstrap (governance, library, README, LICENSE, etc.) | `vault/shared/governance/`, `vault/architect/research/library/`, README raíz, LICENSE | Falla test 1.6 — es contenido, no comportamiento |
| 5 | **Convención técnica** | Estándar declarativo sin alternatives consideradas (típicamente: formato de campo, sintaxis de comentario) | Documentado en CLAUDE.md o en SKILL.md del nodo que la usa | Subset de Nivel 2 (sin alternatives = no ADR Nygard formal); típicamente como AC adicional de feature relacionada |

### Aplicación a las 46 piezas del WA-004 aborted-reference

> Las 46 piezas fueron identificadas correctamente en el WA-004 (reverse-engineering físico correcto). Lo erróneo fue clasificarlas todas como "features". Aquí re-asignamos cada una a su nivel correcto.

#### Piezas reclasificadas a **Nivel 1 — Features genuinas** (~12-15 piezas)

Las piezas que pasan test mecánico 1.6 (descenso a Given/When/Then concreto):

| Pieza original WA-004 | Capability | Por qué es feature genuina |
|---|---|---|
| feature-018 Slash `/scope-scan` | CAP-D | Slash command con stories: convoca 5 advisors, espera outputs, consolida, presenta. Given/When/Then concretos. |
| feature-019 Slash `/verify` + algoritmo verifiers | CAP-D | Slash con stories: comprueba closure-criteria, deriva verifiers, invoca, aplica on-close, archiva. Given/When/Then concretos. |
| feature-032 Slash `/status` | CAP-F | Slash con stories: agrega subgrafo, WAs por track, backlog, ADRs. Given/When/Then concretos. |
| feature-033 Slash `/wa` | CAP-F | Slash con stories: identifica WA activo, lee frontmatter+Progreso, presenta. Given/When/Then concretos. |
| feature-034 Slash `/sessions` | CAP-F | Slash con stories: lista 8 modos de trabajo + atajos. Given/When/Then concretos. |
| feature-010 Entry-point npm scripts + wrappers CLAUDE.md | CAP-B | Comandos: 9 atajos npm. Cada uno arranca sesión con identidad. Given/When/Then concretos. |
| feature-035 Ritual de inicio del PO | CAP-F + CAP-G | Comportamiento observable: detecta vault state, lee directorios, presenta panorámica. Given/When/Then concretos (aunque sea procedimiento de agente). |
| feature-038 PO Modo 1 (10 pasos) | CAP-G | El protocolo en sí tiene 10 sub-momentos = stories. Cada paso con Given/When/Then. **Borderline**: muy grande, candidata a sub-dividir en step-2g. |
| feature-039 Cadena WAs por gaps | CAP-G | Comportamiento del PO: detecta gaps upstream, propone cadena ordenada, confirma humano, drafta primer WA. Given/When/Then concretos. |
| feature-041 README.md raíz | CAP-J | Documento + JTBD del newcomer. Stories: "newcomer lee tesis", "newcomer ve modelo conceptual", etc. Given/When/Then concretos sobre legibilidad. |
| feature-044 Glosario público | CAP-J | Feature de doc futura: stories con AC verificables (cobertura ≥20 términos canónicos, ≥4 categorías). Given/When/Then concretos. |
| feature-045 Ruta lectura por audiencia | CAP-J | Feature de doc futura: stories por audiencia (técnica/académica/adoptante), AC verificables. Given/When/Then concretos. |
| feature-036 Orientación qué rol abrir | CAP-F | Feature de comportamiento del PO: detecta ambigüedad, presenta criterio. Given/When/Then. Borderline pero descomponible. |
| feature-005 Backlog query emergente | CAP-A | Query computada: stories ("el operador ejecuta grep sobre vault", "el operador ve listado"). Given/When/Then. Borderline. |

**Total Nivel 1 estimado**: ~14 features genuinas reales. Step-2a..2h confirma con test mecánico.

#### Piezas reclasificadas a **Nivel 2 — ADRs latentes** (~9 piezas, candidatos a Lote B WAs `adr`)

| Pieza original WA-004 | Reclasificada como ADR | Razón |
|---|---|---|
| feature-002 Frontmatter YAML | ADR-latente-003a Frontmatter YAML como mecanismo declarativo | Decisión arquitectónica con alternatives (JSON, TOML, custom). No es feature — no se "implementa" como behavior. Es estándar. |
| feature-003 Wikilinks `[[id]]` | ADR-latente-003b Wikilinks como mecanismo navegación interna | Idem. Convención de markup, decisión con alternatives. |
| feature-004 Estados canónicos + transiciones | ADR-latente-004 Estados canónicos del nodo + lifecycle | Decisión arquitectónica del lifecycle. Alternatives consideradas (estados libres, lifecycle implícito). |
| feature-007 Trazabilidad `// @sem-ia:` + `// @ac-coverage:` | ADR-latente-008b Trazabilidad código↔grafo via comentarios | Convención de comentarios + decisión arquitectónica. |
| feature-014 Estructura inline del WA | ADR-latente-WA-structure Estructura del WA como contrato declarativo | Decisión arquitectónica del contrato. Alternatives (estructura libre, sub-WAs, etc.). |
| feature-017 Closure-criteria + on-close transitions | ADR-latente-010b Algoritmo declarativo on-close | Decisión arquitectónica del cierre. |
| feature-020 Tres checkpoints uniformes WA lifecycle | ADR-latente-009 Tres checkpoints uniformes | Decisión arquitectónica del proceso. |
| feature-040 Templates uniformes greenfield/maduro | ADR-latente-007 Templates uniformes (no protocolos paralelos) | Decisión arquitectónica + ADR meta-1 (uniformidad mode-flag). |
| feature-043 LICENSE Apache 2.0 | ADR-latente-license Apache 2.0 elegida | Decisión de licensing con alternatives (MIT, GPL, BSD). |

**Total Nivel 2 estimado**: ~9 ADRs latentes ya identificados + ADR-meta-1 (uniformidad mode-flag) + ADR-security-trans (threat surface) = 11 candidatos para Lote B.

#### Piezas reclasificadas a **Nivel 3 — Protocolos operativos** (~8 piezas, ya formalizadas en agent files / governance)

| Pieza original WA-004 | Vive como protocolo en | Estado |
|---|---|---|
| feature-012 Subagente vs sesión-dedicada (Gap 8) | CLAUDE.md raíz "Tres mecanismos de invocación" + agent file PO Modo 1 paso 8 | Ya formalizado en WA-003 |
| feature-015 Progreso entries + handoff explícito | Cada agent file sección "Al completar tu step" | Ya formalizado |
| feature-016 Protocolo pivot WA mid-flight (Gap 4) | `vault/shared/governance/workflows.md` sección "Protocolo de pivot..." | Ya formalizado en WA-003 |
| feature-022 Give-and-take mid-step (Cagan principio 2) | CLAUDE.md raíz "Patrón colaborativo dentro del WA" + cada agent file | Ya formalizado |
| feature-023 Filtro PO 4 categorías + test load-bearing + auto-audit + artefacto declarativo (Gap 6 + regla 12) | agent file PO Modo 1 paso 6b + regla operativa 12 | Ya formalizado (regla 12 hoy 2026-05-12T23:55) |
| feature-024 Contrato `filesystem-changes` para subagentes (Gap 9) | CLAUDE.md raíz "Contrato de trazabilidad" + agent file PO Modo 2 paso 4a | Ya formalizado en WA-003 |
| feature-026 SKILL.md + design.md como unidad de empaquetado bibliográfico | Convención SEM-IA, en cada SKILL.md construida | Ya formalizado |
| feature-006 Skill compartida `graph-cross-link-declaration` | `.claude/skills/shared/` (existe) | Ya construida (artefacto curado, ver Nivel 4) |

**Total Nivel 3**: ~8 protocolos ya formalizados. NO se featurizan (Cagan principio 1 — no son entregables, son comportamiento). El WA-005 NO los duplica.

#### Piezas reclasificadas a **Nivel 4 — Docs/governance/artefactos curados** (~13 piezas)

| Pieza original WA-004 | Vive como artefacto en |
|---|---|
| feature-001 Vault role-first (organización física) | Estructura física del repo + documentado en `repo-structure.md` |
| feature-008 Identidad por rol via agent files | 8 agent files en `.claude/agents/*.md` (artefactos curados) |
| feature-009 Catálogo formal de roles | `vault/shared/governance/role-catalog.md` (doc) |
| feature-011 CLAUDE.md raíz | Documento + ya cubre stories (newcomer comprende framework) → **REASIGNAR**: parte de Nivel 4 como doc, parte de Nivel 1 como feature (cobertura del JTBD del operador newcomer). Voy a tratar feature-011 como Nivel 1 feature genuina + el archivo CLAUDE.md como artefacto del bootstrap. |
| feature-013 Catálogo 14 workflow templates SDLC | `vault/shared/governance/workflows.md` (doc) |
| feature-021 verification-matrix.md | `vault/shared/governance/verification-matrix.md` (doc) |
| feature-025 Library 18 notas bibliográficas + INDEX | `vault/architect/research/library/` (corpus) |
| feature-027 Catálogo skills PO estratégicas | `.claude/skills/product-owner/strategy/` (4 SKILL.md construidas) |
| feature-028 Catálogo skills PO operativas | `.claude/skills/product-owner/` (3 SKILL.md construidas) |
| feature-029 Catálogo skills Architect | `.claude/skills/architect/` (5 SKILL.md construidas) |
| feature-030 Skill Security threat-modeling | `.claude/skills/security-officer/` (1 SKILL.md construida) |
| feature-031 `_pending-later.md` | `.claude/skills/_pending-later.md` (roadmap) |
| feature-042 Artefactos históricos (bootstrap-summary + propuesta-prefacio.pdf) | `vault/architect/research/bootstrap-summary.md` + raíz repo |
| feature-046 Atribución bibliográfica en docs públicos | AC adicional de feature-041 (README) + feature-042 (bootstrap-summary). NO feature propia. |

**Total Nivel 4**: ~13 docs/artefactos curados. NO se featurizan. Aparecen en specs Gherkin SI feature-011 / feature-041 los referencia como pre-requisitos (Given), pero como artefacto inerte, no comportamiento.

#### Piezas reclasificadas a **Nivel 5 — Convenciones técnicas** (sub-set como AC adicionales)

| Pieza original WA-004 | Vive como AC adicional en feature(s) | 
|---|---|
| feature-037 Dual Track visible en /status | AC adicional de feature-032 Slash `/status` |
| (otras convenciones inline emergerán en step-2x al escribir specs) | Como AC de la feature que las usa |

**Total Nivel 5**: pocas piezas que merecen propio nivel. La mayoría son AC inline.

### Síntesis: distribución final

- **Nivel 1 (Features genuinas)**: ~14 piezas (objetivo step-2a..2h: producir feature files + stories + specs Gherkin)
- **Nivel 2 (ADRs latentes)**: ~9-11 candidatos para Lote B
- **Nivel 3 (Protocolos operativos)**: ~8 ya formalizados (NO duplicar)
- **Nivel 4 (Docs/governance/artefactos)**: ~13 artefactos curados existentes (NO featurizar)
- **Nivel 5 (Convenciones técnicas)**: AC inline de features relacionadas

**Total piezas mapeadas: 46** (WA-004 inventario físico preservado). **Cero piezas sin nivel**.

---

## Tabla cobertura — Pieza-bootstrap × Nivel arquitectónico

| Pieza del bootstrap | Nivel | Owner/Materialización |
|---|---|---|
| vault/ organización role-first | 4 | Estructura repo + repo-structure.md |
| repo-structure.md | 4 | doc governance |
| dimensions.md | 4 | doc governance + AC de feature-009 |
| role-catalog.md | 4 | doc governance (feature-009 reclasificada) |
| Frontmatter YAML | 2 | ADR-latente-003a |
| Wiki-links `[[id]]` | 2 | ADR-latente-003b |
| Estados canónicos | 2 | ADR-latente-004 |
| Skill graph-cross-link-declaration | 4 | artefacto curado en .claude/skills/shared/ |
| `// @sem-ia:` + `// @ac-coverage:` | 2 | ADR-latente-008b |
| 8 agent files | 4 | artefactos curados (feature-008 → identidad por rol como Nivel 4) |
| Catálogo roles | 4 | doc governance |
| 7 wrappers CLAUDE.md | **Feature 1** | feature `entry-point por rol` (incluye atajos npm) |
| package.json npm scripts | **Feature 1** | parte de feature anterior |
| CLAUDE.md raíz | **Feature 1** | feature `CLAUDE.md raíz como guía + entry PO` (incluye el artefacto + el JTBD del operador) |
| Mecanismo Task tool | n/a | depends-on-harness |
| Criterio modality (Gap 8) | 3 | protocolo en CLAUDE.md raíz + agent files |
| 14 workflow templates | 4 | doc governance (workflows.md) |
| Estructura inline WA | 2 | ADR-latente-WA-structure |
| Regla autocontención (Gap 7) | 3 | protocolo en CLAUDE.md raíz + agent file PO |
| Briefing por step (Gap 10) | 3 | protocolo en CLAUDE.md raíz + agent file PO |
| Progreso entries + handoff | 3 | protocolo en cada agent file |
| Protocolo pivot mid-flight (Gap 4) | 3 | protocolo en workflows.md |
| Estados WA (active/archived/aborted) | 2 | extensión de ADR-latente-004 |
| Closure-criteria + on-close | 2 | ADR-latente-010b |
| Slash `/scope-scan` | **Feature 1** | feature `/scope-scan` |
| Slash `/verify` + algoritmo verifiers | **Feature 1** | feature `/verify` |
| Tres checkpoints uniformes | 2 | ADR-latente-009 |
| verification-matrix.md | 4 | doc governance |
| Give-and-take Cagan principio 2 | 3 | protocolo en CLAUDE.md raíz + agent files |
| Filtro PO 4 categorías (Gap 6) + regla 12 | 3 | protocolo en agent file PO regla 12 |
| Contrato filesystem-changes (Gap 9) | 3 | protocolo en CLAUDE.md raíz + agent file PO |
| Backlog query emergente | **Feature 1** | feature `backlog query` (borderline; ver step-2a) |
| 18 notas library + INDEX | 4 | corpus bibliográfico curado |
| SKILL.md + design.md unidad de empaquetado | 4 | convención (artefactos curados) |
| 4 skills PO estratégicas | 4 | artefactos curados (.claude/skills/product-owner/strategy/) |
| 3 skills PO operativas | 4 | artefactos curados |
| 5 skills Architect | 4 | artefactos curados |
| 1 skill Security | 4 | artefacto curado |
| _pending-later.md | 4 | doc roadmap |
| Slash `/status` | **Feature 1** | feature `/status` |
| Slash `/wa` | **Feature 1** | feature `/wa` |
| Slash `/sessions` | **Feature 1** | feature `/sessions` |
| Ritual inicio PO | **Feature 1** | feature `ritual inicio PO` |
| Dual Track visible | 5 | AC adicional de feature `/status` |
| Orientación qué rol abrir | **Feature 1** | feature `orientación qué rol abrir` |
| PO Modo 1 (10 pasos) | **Feature 1** | feature `PO Modo 1` (borderline grande; sub-dividir si necesario en step-2g) |
| Cadena WAs por gaps | **Feature 1** | feature `cadena WAs greenfield` |
| Templates uniformes greenfield/maduro | 2 | ADR-latente-007 |
| README.md raíz | **Feature 1** | feature `README onboarding` |
| bootstrap-summary.md + propuesta-prefacio.pdf | 4 | docs históricos curados |
| LICENSE Apache 2.0 | 2 | ADR-latente-license |
| Glosario público | **Feature 1** | feature `glosario público` |
| Ruta lectura por audiencia | **Feature 1** | feature `ruta lectura por audiencia` |
| Atribución bibliográfica explícita | 5 | AC adicional de feature `README onboarding` + feature `bootstrap-summary` (no feature propia) |

**Cobertura final**: 100% de piezas del bootstrap mapeadas a 1 de los 5 niveles. Cero gaps.

---

## Anexo — Lista cerrada features genuinas por capability (input directo a step-2a..2h)

> Lista cerrada de features de Nivel 1 (las que SÍ pasan test mecánico Adzic SbE). Cada feature con stories candidatas preview (a confirmar/expandir en step-2x al aplicar `feature-decomposition`).

### CAP-A · Grafo declarativo persistente — **1 feature genuina + 1 reclasificada**

> **Ajuste post step-2a (2026-05-13T01:50)**: feature-005 (backlog-query) sometida a test mecánico Adzic en step-2a — NO pasa. Reclasificada a Nivel 2 (ADR-latente-008 ya existe) + AC adicional de feature-032 /status (visibilidad backlog) + AC adicional de feature-019 /verify (transición a ready-for-implementation). CAP-A queda con 1 feature genuina (feature-001).

#### feature-001-vault-role-first
- **JTBD**: *"El operador (humano + agente) puede localizar artefactos del proyecto por rol custodio (no por tipo técnico), de modo que la navegación refleja la dimensión responsable."*
- **Stories candidatas preview**:
  - Story-001-A: "Como operador humano, navego al directorio del rol que necesito vía `vault/<rol>/`"
  - Story-001-B: "Como operador agente, escribo artefactos en `vault/<mi-rol>/<subcategoría>/` siguiendo convención role-first"
  - Story-001-C: "Como operador, encuentro artefactos cross-rol en `vault/shared/`"
- **ADRs latentes apuntados**: ADR-latente-002 (Vault role-first)

#### ~~feature-005-backlog-query~~ [RECLASIFICADA — NO ES FEATURE]

**Resultado del test mecánico Adzic en step-2a**: feature-005 NO pasa test 1.6.

Las 3 stories candidatas se reclasifican honestamente:
- Story-005-A "operador humano ejecuta /status y ve Backlog" → **AC adicional de feature-032 /status** (procesar en step-2f cuando se escriba feature-032).
- Story-005-B "operador agente ejecuta query find/grep" → **ADR-latente-008 Backlog query emergente** (ya identificado, propiedad arquitectónica con alternatives — estructura persistente vs emergente).
- Story-005-C "backlog se actualiza tras /verify" → **AC adicional de feature-019 /verify** (procesar en step-2d cuando se escriba feature-019).

**Veredicto**: backlog-query es **invariante arquitectónica + AC inline de features hermanas**, no feature genuina con stories propias. El operador interactúa con el backlog VÍA /status y VÍA /verify (que lo alimenta vía on-close). El backlog en sí mismo no tiene JTBD del operador independiente.

**Acción**: feature-005 eliminada del catálogo Nivel 1. ADR-latente-008 permanece en lista de candidatos para Lote B. Stories que iban a feature-005 se absorben en specs de feature-032 y feature-019.

### CAP-B · Operación multi-rol — **1 feature genuina**

#### feature-010-entry-point-por-rol
- **JTBD**: *"El operador humano puede arrancar una sesión de cualquier rol con un comando único (`npm run sem|arch|des|biz|sec|qa|dev|ops`) que carga identidad + zona de trabajo + skills, de modo que el cambio entre roles es operativamente barato."*
- **Stories candidatas preview**:
  - Story-010-A: "Como operador humano, ejecuto `npm run sem` y arranca sesión PO con identidad cargada"
  - Story-010-B: "Como operador humano, ejecuto `npm run arch` y arranca sesión Architect"
  - Story-010-C: "Como operador humano newcomer, leo `package.json` y veo los 9 scripts disponibles"
  - Story-010-D: "Como operador agente al arrancar, leo mi wrapper CLAUDE.md + mi agent file y cargo identidad"
- **ADRs latentes**: ADR-latente-001 (Claude Code harness), ADR-latente-002 (vault role-first)
- **Nota**: feature-008 (identidad por rol vía agent files) NO es feature separada — los 8 agent files son **artefactos curados de Nivel 4** que `feature-010` consume. La identidad cargada al arrancar es comportamiento de **feature-010**.

### CAP-C · Working Agreements + SDLC — **0 features genuinas en step-2c**

Sorprendentemente: CAP-C es **casi pura Nivel 2-4**. Sus piezas son:
- Estructura inline WA → ADR latente
- 14 templates → doc governance
- Progreso + handoff → protocolo
- Pivot mid-flight → protocolo
- Closure + on-close → ADR latente

**No hay features genuinas que pasen test 1.6 dentro de CAP-C**: las "capacidades" de CAP-C son comportamiento del proceso (declarativo), no entregables del operador. Su materialización vive en CAP-D (slashes que operan sobre WAs) y CAP-F (visibilidad de WAs).

**Decisión PO en step-2c**: documentar honestamente que CAP-C tiene 0 features Nivel 1 directas. Sus piezas viven en Niveles 2-4. Su cobertura al operador se da vía features de CAP-D + CAP-F que **operan sobre** los WAs.

Esto es ejemplo del test mecánico funcionando: si no hay Given/When/Then del operador interactuando con CAP-C directamente, no hay feature genuina — es capability arquitectónica pura.

### CAP-D · Verificación multi-rol cruzada — **2 features genuinas**

#### feature-018-slash-scope-scan
- **JTBD**: *"El operador agente orquestador puede convocar reunión flat parallel multi-rol on-demand (5 advisors en paralelo desde sus ángulos dimensionales) sobre cualquier propuesta, de modo que el scope-scan multi-rol es herramienta disponible, no ritual ceremonioso."*
- **Stories candidatas preview**:
  - Story-018-A: "Como PO al draftear WA, ejecuto `/scope-scan` y convoco 5 advisors"
  - Story-018-B: "Como advisor invocado, recibo prompt + propuesta + paths, leo, devuelvo `scope-scan-output`"
  - Story-018-C: "Como PO orquestador, consolido los 5 outputs aplicando Filtro PO regla 12"
- **ADRs latentes**: ADR-latente-009 (3 checkpoints), ADR-latente-001 (harness Task tool)

#### feature-019-slash-verify
- **JTBD**: *"El humano puede ejecutar `/verify` al cierre de cualquier WA y el PO deriva mecánicamente verificadores aplicando algoritmo `verifiers = {custodian(d) : d ∈ dimensions-affected}`, invoca en paralelo, aplica on-close, archiva. De modo que el sign-off es algoritmo declarativo, no juicio caso-a-caso."*
- **Stories candidatas preview**:
  - Story-019-A: "Como humano, ejecuto `/verify` y el PO comprueba closure-criteria mecánicamente"
  - Story-019-B: "Como PO al verify, derivo verifiers desde dimensions-affected"
  - Story-019-C: "Como PO al verify, invoco verificadores en paralelo via Task tool"
  - Story-019-D: "Como PO al verify, aplico on-close transitions y archivo el WA"
- **ADRs latentes**: ADR-latente-010 (algoritmo verifiers)

### CAP-E · Anclaje bibliográfico + skills empaquetadas — **0 features genuinas directas en step-2e**

Similar a CAP-C: las piezas de CAP-E son **catálogo de artefactos curados** (Nivel 4) + convenciones (Nivel 2/5). La library + 14 skills son artefactos del bootstrap, no features descomponibles en stories.

**Decisión PO en step-2e**: documentar 0 features Nivel 1. CAP-E es capability transversal a todas las demás — su valor se realiza vía **citas bibliográficas en specs Gherkin** producidas por otras features (CAP-J atribución académica, etc.) y vía **invocación perezosa de skills** dentro de WAs.

Si emerge necesidad de feature de "validación de integridad de library" (vector seguridad load-bearing detectado en pelea fuerte WA-004), considerar en step-2e — sería feature operativa derivada (validar bibliografía citada existe), pero borderline.

### CAP-F · Visibilidad operativa — **5 features genuinas**

#### feature-032-slash-status
- **JTBD**: *"El operador humano puede ejecutar `/status` desde cualquier sesión y recibir snapshot del estado del proyecto entero (WAs por track Dual, backlog emergente, subgrafo estratégico, features por status, ADRs), de modo que valida estado conocido en vez de re-explorar el vault."*
- **Stories candidatas preview**:
  - Story-032-A: "Como operador, ejecuto `/status` y veo subgrafo estratégico"
  - Story-032-B: "Como operador, ejecuto `/status` y veo WAs activos agrupados por track Dual"
  - Story-032-C: "Como operador, ejecuto `/status` y veo backlog query emergente"
  - Story-032-D: "Como operador, ejecuto `/status` y veo ADRs por status"
- **AC adicional Nivel 5**: Dual Track Discovery/Delivery visible en /status (heredado de feature-037)
- **ADRs latentes**: ADR-latente-008 (backlog query)

#### feature-033-slash-wa
- **JTBD**: *"El operador humano puede ejecutar `/wa` desde una sesión y recibir detalle del WA activo en el contexto (steps con status, Progreso, scope, closure-criteria, próximo step pending), de modo que comprende dónde está en el ciclo actual."*
- **Stories candidatas preview**:
  - Story-033-A: "Como operador, ejecuto `/wa` y veo steps con status"
  - Story-033-B: "Como operador, ejecuto `/wa` y veo entrada Progreso resumida"
  - Story-033-C: "Como operador, ejecuto `/wa` y veo próximo step pending"

#### feature-034-slash-sessions
- **JTBD**: *"El operador humano puede ejecutar `/sessions` y recibir catálogo legible de los modos de trabajo disponibles (8 roles × atajos npm + cuándo abrir cada uno), de modo que reduce recall cognitive y acelera cambio entre roles."*
- **Stories candidatas preview**:
  - Story-034-A: "Como operador humano newcomer, ejecuto `/sessions` y veo los 8 modos"
  - Story-034-B: "Como operador, ejecuto `/sessions` y veo cuándo invocar cada rol"

#### feature-035-ritual-inicio-po
- **JTBD**: *"El operador agente PO, al arrancar sesión (Modo 1 paso 1), lee strategy/sessions/specs/adrs/governance y presenta panorámica al humano antes de pedir propuesta, de modo que la conversación arranca con contexto compartido."*
- **Stories candidatas preview**:
  - Story-035-A: "Como PO al arrancar `npm run sem`, leo vault y construyo panorámica"
  - Story-035-B: "Como PO, presento panorámica al humano con formato canónico"
  - Story-035-C: "Como PO en vault greenfield, detecto vacío y propongo inception"

#### feature-036-orientacion-rol
- **JTBD**: *"El operador humano que duda qué sesión abrir puede consultar criterio expresado en lenguaje de decisión del operador (CLAUDE.md + tabla delegación PO + `/sessions`), de modo que sabe qué sesión abrir sin leer páginas de docs."*
- **Stories candidatas preview**:
  - Story-036-A: "Como operador humano nuevo, consulto CLAUDE.md sección 'Cómo arrancar' y veo criterio"
  - Story-036-B: "Como operador en sesión equivocada, recibo mensaje recovery del rol activo"
  - Story-036-C: "Como operador, ejecuto `/sessions` y veo descripción cuándo invocar cada rol"

### CAP-G · Inception greenfield — **2 features genuinas**

#### feature-038-po-modo-1
- **JTBD**: *"El operador agente PO, al recibir propuesta humana al arrancar sesión, puede conducir el flujo completo de entrada al sistema aplicando protocolo declarativo de 10 pasos, de modo que la entrada por defecto al sistema es uniforme + auditable + bibliográficamente anclada."*
- **Stories candidatas preview** (10 stories una por paso, agrupables):
  - Story-038-A: "Como PO Modo 1 paso 1, ejecuto ritual de inicio" (cubierto por feature-035 — `also-relates-to`)
  - Story-038-B: "Como PO Modo 1 paso 2-3, escucho propuesta humano + clasifico outcome-type"
  - Story-038-C: "Como PO Modo 1 paso 4, decido conduzco o delego"
  - Story-038-D: "Como PO Modo 1 paso 5, convoco scope-scan" (cubierto por feature-018 — `also-relates-to`)
  - Story-038-E: "Como PO Modo 1 paso 6+6b, consolido + aplico Filtro PO regla 12"
  - Story-038-F: "Como PO Modo 1 paso 7-8, cargo template + drafteo WA con briefings"
  - Story-038-G: "Como PO Modo 1 paso 9-10, presento WA + confirmo + handoff"
- **Borderline grande**: 7 stories agrupadas. Cohn `S` admite hasta 7 stories. OK pero límite. Considerar sub-dividir si emergen sub-features autónomos.

#### feature-039-cadena-was-greenfield
- **JTBD**: *"El operador agente PO, al detectar gaps upstream durante scope-scan (no hay capability padre, no hay goal padre, no hay visión), puede proponer cadena ordenada top-down de WAs (vision-creation → goal-definition × N → capability-creation × M → feature-design × K), de modo que el grafo emerge orgánicamente desde gap detection."*
- **Stories candidatas preview**:
  - Story-039-A: "Como PO scope-scan, detecto gaps upstream"
  - Story-039-B: "Como PO, propongo cadena al humano + 3 formas (directa/corta/arbitraje)"
  - Story-039-C: "Como PO post-confirmación, drafto solo primer WA de la cadena"
  - Story-039-D: "Como PO al cierre de WA-N de la cadena, drafto WA-N+1 si aplica"

### CAP-J · Articulación pública — **3 features genuinas**

#### feature-041-readme-onboarding
- **JTBD**: *"El operador humano newcomer (ingeniero adoptador, evaluador académico, comunidad técnica) puede comprender el framework SEM-IA completo leyendo `README.md` raíz: tesis, modelo conceptual, cómo arrancar, capabilities, dual track, anclaje bibliográfico, posicionamiento Apache 2.0, de modo que decide informado si adoptar/evaluar/contribuir sin invocar al autor."*
- **Stories candidatas preview**:
  - Story-041-A: "Como newcomer, leo README y entiendo la tesis filosófica"
  - Story-041-B: "Como newcomer, leo README y entiendo modelo conceptual (8 roles × 7 dim × 14 templates)"
  - Story-041-C: "Como newcomer, leo README y sé cómo arrancar (npm run sem)"
  - Story-041-D: "Como evaluador académico, leo README y veo atribución bibliográfica explícita"
  - Story-041-E: "Como adopter, leo README y entiendo cautelas de privacidad del vault público"
- **AC adicional Nivel 5**: atribución bibliográfica explícita (heredado de feature-046)

#### feature-044-glosario-publico
- **JTBD**: *"El operador humano newcomer (especialmente evaluador académico) puede resolver la jerga interna del framework (WA, scope-scan, vault, etc.) consultando un glosario navegable referenciado desde README, de modo que la barrera de entrada baja significativamente."*
- **Stories candidatas preview**:
  - Story-044-A: "Como newcomer, encuentro término `WA` en README y voy al glosario"
  - Story-044-B: "Como evaluador académico, consulto glosario y veo ≥20 términos canónicos en ≥4 categorías"
  - Story-044-C: "Como newcomer, cada término en glosario tiene definición + ejemplo + cross-link al doc canónico"

#### feature-045-ruta-lectura-audiencia
- **JTBD**: *"El operador humano newcomer puede identificar su ruta de lectura óptima según audiencia (técnica/académica/adoptante) en sección 'Cómo leer este repo' del README, de modo que no necesita leer 65 KB linealmente — progressive disclosure."*
- **Stories candidatas preview**:
  - Story-045-A: "Como ingeniero adoptante, veo ruta de lectura adoptante con archivos en orden"
  - Story-045-B: "Como evaluador académico, veo ruta académica con tesis + bibliografía + dogfooding"
  - Story-045-C: "Como contribuyente, veo ruta arquitectura + governance"

---

## Totales del catálogo

| Capability | Features genuinas Nivel 1 |
|---|---|
| CAP-A | 1 (feature-001 vault-role-first; feature-005 reclasificada a ADR-latente-008 + AC inline) |
| CAP-B | 1 (feature-010 entry-point-por-rol) |
| CAP-C | 0 (todas las piezas son Nivel 2-4) |
| CAP-D | 2 (feature-018 /scope-scan + feature-019 /verify) |
| CAP-E | 0 (todas las piezas son artefactos curados Nivel 4) |
| CAP-F | 5 (features 032/033/034/035/036) |
| CAP-G | 2 (features 038/039) |
| CAP-J | 3 (features 041/044/045) |
| **TOTAL** | **14 features genuinas** (post step-2a, feature-005 reclasificada) |

**Estimación stories totales**: ~15 features × ~3-5 stories = **~45-75 stories**.
**Estimación specs Gherkin totales**: 1 spec por story = **~45-75 specs Gherkin**.

**Reducción vs WA-004**: el WA-004 mezcló 46 piezas como "features"; el WA-005 honestamente identifica **15 features genuinas** + **9-11 ADRs latentes** + **8 protocolos ya formalizados** + **13 docs/artefactos curados** + AC adicionales.

**Cobertura preservada**: 100% piezas del bootstrap mapeadas a su nivel correcto.

---

## Cierre del step-1

**Status**: lista cerrada de 15 features genuinas Nivel 1 por capability + tabla cobertura 46 piezas × 5 niveles + Bloques 1-2 heredados + ajuste 1.6 Adzic SbE.

**Próximo step**: step-2a (CAP-A) — aplicar `feature-decomposition` + `spec-writing` + `feature-quality-check` sobre las 2 features de CAP-A (feature-001 vault-role-first + feature-005 backlog-query) produciendo feature files + story files + spec Gherkin files con AC formales.
