---
type: discovery
id: features-bootstrap-batch-extraction-2026-05-12
title: "Extracción bottom-up de features desde el bootstrap construido [APPROACH ABORTADO]"
status: aborted-reference  # WA contenedor wa-2026-05-12-004 abortado por fiasco de granularidad sistemática
aborted-at: 2026-05-12T23:59:00+02:00
aborted-reason: |
  Approach abortado: el WA-004 contenedor cerró por "stop-too-early" en la espina dorsal de SEM-IA — sin descender a Stories → Examples → AC → Specs Gherkin, el PO no tenía contraste bibliográfico mecánico para discernir si una "pieza del bootstrap" era feature genuina o pertenecía a otro nivel arquitectónico. Las 46 "features" producidas en este documento mezclan 5 niveles: features genuinas (~10), ADRs latentes (~9), protocolos ya formalizados (~8), docs/governance (~13), artefactos curados (resto).

  Preservado como referencia auditable. Los Bloques 1 (criterios) y 2 (flujo del operador) tienen valor reutilizable; el Bloque 3 (inventario) reclasificable por el WA-005 successor en sus 5 niveles correctos.

  No entra en backlog ni en queries de nodos `active`. Es referencia histórica del approach descartado, no nodo operativo.
superseded-by-wa: wa-2026-05-12-005  # placeholder — successor a drafttear en modo plan
created: 2026-05-12
author: product-owner
related-wa: wa-2026-05-12-004
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
  - vault/product-owner/discovery/capabilities-bootstrap-extraction-2026-05-12.md  # ground truth del Job × Pieza × Capability
  - vault/shared/sessions/archive/wa-2026-05-12-002.md  # precedente directo del approach reverse-engineering batch
  - vault/shared/sessions/archive/wa-2026-05-12-003.md  # gaps estructurales procesados
  - vault/shared/sessions/active/wa-2026-05-12-004.md  # este WA contenedor
  - vault/architect/research/bootstrap-summary.md  # historia del bootstrap
  - CLAUDE.md  # ground truth del framework
  - README.md  # entry point externo
bibliography:
  - Cagan — Inspired (principio 1: solve problems, not features; strong product team)
  - Cohn — User Stories Applied (INVEST: Independent, Negotiable, Valuable, Estimable, Small, Testable)
  - Patton — User Story Mapping (narrative flow + thin slices + task-level granularity)
  - Christensen — Jobs-To-Be-Done (JTBD outcome of the operator, not output of the feature)
  - Adzic — Specification by Example (AC trazables, living documentation)
  - Ford — Building Evolutionary Architectures (fitness functions, appropriate coupling)
  - Nygard — Documenting Architecture Decisions (ADRs latentes declarables)
---

# Extracción bottom-up de features desde el bootstrap construido

## Contexto

Este documento es el **output del step-1 del WA `wa-2026-05-12-004`**. Aplica approach **bottom-up reverse-engineering batch** sobre las 8 capabilities operant del proyecto (CAP-A..G + CAP-J). Es **isomorfo al WA-002** un nivel más abajo en la espina dorsal: igual que WA-002 extrajo capabilities desde piezas reales del bootstrap mapeando por Jobs, este WA-004 extrae features desde esas mismas piezas mapeando por capability.

**Decisión clave** (confirmada con humano al draftear el WA-004):
- Scope: 8 capabilities operant. Las 2 planned (CAP-H portabilidad, CAP-I adopción retroactiva) quedan fuera — sus piezas no están construidas.
- Profundidad: features con AC enumerados + anotación "verificable vía:" por AC. NO Gherkin formal en este WA (queda para WAs feature-design single posteriores).
- IDs: `feature-NNN` secuencial global (NNN = 001, 002, ...) coherente con convención `cap-NN`.
- Template-mode: improvisación declarada de `feature-design` mode `reverse-engineering-batch` (mode-flag formal queda para WA doc-edit posterior).

**Cross-reference con WA-002 archivado**: el discovery doc del WA-002 (`vault/product-owner/discovery/capabilities-bootstrap-extraction-2026-05-12.md`) tiene el inventario canónico de **10 Jobs × Piezas reales × Capabilities**. Este documento opera sobre el subconjunto de piezas materializando las 8 capabilities operant, refinándolas como features formales.

---

## Bloque 1 — Criterios y convenciones aplicados

> Este bloque declara CÓMO se va a hacer todo lo demás. Si los criterios están mal definidos, el inventario capability-by-capability queda contaminado. Es por tanto el bloque que se valida primero antes de avanzar al flujo del operador y al inventario.

### 1.1 — Granularidad de feature (anclaje Cohn INVEST + Patton)

**Definición operativa:** una feature SEM-IA = **habilidad observable cohesiva descomponible en 2-7 stories** (Cohn INVEST `S = Small` + Patton task-level del story map).

**Criterio operacional (cuándo una pieza candidata es feature):**

- ✅ **Es feature** si: cubre un job concreto del operador, tiene contornos observables, materializa una capability operant identificable, y es razonablemente independiente (Cohn `I = Independent` — coupling declarado explícitamente con `also-relates-to` / `depends-on` cuando existe).
- 🔧 **Sub-dividir** si: una pieza candidata abarca > 7 stories estimables, o cubre múltiples jobs del operador heterogéneos, o agrupa decisiones técnicas ortogonales que merecen ADRs separados.
- 🔗 **Agrupar** si: una pieza candidata es < 2 stories estimables y otra pieza hermana cubre el mismo job desde un ángulo cercano (anti sub-feature trivial — Cohn `V = Valuable` requiere valor entregable).

**Anti-patrón de granularidad** (a evitar):
- "Feature = 1 archivo del bootstrap" como mapeo sintáctico 1:1. Producirá features con scopes radicalmente desiguales (un archivo pequeño = una feature; un archivo grande = una feature; pero el cognitive y el value entregable son distintos).
- "Feature = todo un Job" como agrupación gruesa. Producirá features no-decomponibles en stories implementables — habría que sub-dividir luego de todos modos.

**Criterio de evaluación posterior** (aplicable por Architect en step-3 + QA en step-7): para cada feature producida, veredicto granularidad ∈ `{ok | sub-dividir | agrupar}`. Si > 30% de features tienen veredicto ≠ `ok`, el criterio aquí declarado está mal calibrado y se ajustará en `/verify` con vuelta a step-1.

### 1.2 — JTBD del operador (anti-patrón features-as-output-blind)

**Definición operativa:** cada feature enuncia el **outcome del operador** (qué consigue + por qué le importa), NO la descripción de la pieza técnica que la materializa.

**El "operador" en SEM-IA es DOBLE:**
- **Operador humano**: ingeniero solitario o equipo adoptador que usa SEM-IA para gestionar trabajo con IA. Outcomes: visibilidad del estado, decisiones auditables, cobertura multi-rol, etc.
- **Operador sistema**: el propio agente IA que arranca su sesión (PO, Architect, etc.) y necesita contexto del proyecto para operar con criterio. Outcomes: identidad cargada, panorámica del vault, skills disponibles, etc.

Una feature puede tener outcome para uno o ambos. **Ambos son legítimos** — la doble operatividad es propiedad de SEM-IA como infraestructura de gestión IA.

**Convención de enunciado** (template):

> *"El [operador humano | operador agente | ambos] puede [acción + contexto] de modo que [outcome observable + por qué importa]."*

**Ejemplos validados:**

- ✅ **JTBD legítimo**: *"El operador humano puede consultar el estado del proyecto entero (WAs activos por track, backlog, subgrafo estratégico) en un solo comando, de modo que valida estado conocido en vez de re-explorar el vault."* (CAP-F · /status)
- ✅ **JTBD legítimo**: *"El operador agente PO puede arrancar su sesión con panorámica del proyecto pre-cargada, de modo que clasifica propuestas del humano con criterio bibliográfico desde el primer turn."* (CAP-F · ritual de inicio)
- ❌ **Anti-patrón features-as-output-blind**: *"Feature: archivo `.claude/agents/product-owner.md` con identidad del PO declarada."* (describe la pieza, no el outcome del operador)
- ✅ **Reformulado correctamente**: *"El operador agente PO puede arrancar con identidad bibliográfica anclada (Cagan + Sinek + Rumelt + Doerr + Christensen) y modos de operación (1-4) declarados, de modo que opera coherente entre sesiones sin re-derivar quién es."*

**Criterio de detección** (aplicable por Architect step-3 + QA step-7): si el enunciado de una feature **describe la pieza** en lugar del outcome del operador → flag features-as-output-blind → reformular antes de /verify.

**Anclaje bibliográfico:** Cagan *Inspired* principio 1 — *"Strong product teams solve problems for customers; weak teams ship features."* En SEM-IA el "customer" es el operador (humano + agente).

### 1.3 — Distinción features-construidas-por-SEM-IA vs dependencias-del-harness

**Problema que resuelve:** las "piezas candidatas" de cada capability incluyen elementos del harness Claude Code (Task tool, carga perezosa, prompt cache) que NO son construidos por SEM-IA — son infraestructura externa que SEM-IA usa. Considerarlos features propias inflaría el catálogo y degradaría auditabilidad (Architect flag A2 del scope-scan).

**Reglas operativas:**

| Es feature de SEM-IA | Es dependencia del harness (NO feature) |
|---|---|
| Agent files `.claude/agents/<rol>.md` (8) — identidad bibliográfica anclada construida por SEM-IA | Mecanismo `Task tool` para invocar subagentes — provisto por Claude Code, SEM-IA lo usa |
| Skills `.claude/skills/<rol>/<skill>/SKILL.md` (14 construidas) — happy-paths bibliográficos construidos por SEM-IA | Carga perezosa nativa de Agent Skills — comportamiento del runtime Claude Code |
| Slash commands `.claude/commands/<cmd>.md` (cuando se construyan) — flujos declarativos construidos por SEM-IA | Prompt cache de Claude Code — mecanismo del runtime |
| Vault role-first (`vault/<rol>/`) — organización física del grafo construida por SEM-IA | Tools `Read/Write/Edit/Glob/Grep/Bash` — provistas por Claude Code |
| CLAUDE.md raíz + wrappers `vault/<rol>/CLAUDE.md` — entry points construidos por SEM-IA | Mecanismo CLAUDE.md jerárquico — provisto por Claude Code |
| Frontmatter YAML + wiki-links `[[id]]` — convención declarativa construida por SEM-IA | Parser YAML — del runtime / harness |
| Estados canónicos del nodo + transiciones — convención del lifecycle del grafo construida por SEM-IA | Filesystem versionado por git — externo |
| Workflow templates `vault/shared/governance/workflows.md` — 14 templates construidos por SEM-IA | Heurística SDLC en abstracto — patrimonio profesional |
| Estructura WA con frontmatter + steps + on-close + closure-criteria — construida por SEM-IA | Mecanismo MCP servers (si aplica futuro) — externos |
| Bibliografía indexada `vault/architect/research/library/` (18 notas) — curada por SEM-IA | Las obras citadas en sí — bibliográficamente externas |

**Tratamiento de las dependencias del harness:**
- **NO se convierten en features propias** del bootstrap actual.
- Las features que las usan declaran `depends-on-harness: [Task-tool, carga-perezosa-skills, prompt-cache, etc.]` en frontmatter (campo opcional improvisado para auditoría).
- Cuando se active CAP-H portabilidad multi-harness (planned), esas dependencias serán **absorbidas por adapters** (`src/adapters/claude-code/` → render para Claude Code; `src/adapters/opencode/` → render para OpenCode; etc.). Hasta entonces, son `depends-on-harness` declarados.

**Excepción operativa:** si una pieza del harness se **extiende** o **especializa** vía SEM-IA (ej. SEM-IA define cuándo invocar Task tool con qué prompt vs no invocarlo), esa **regla de uso** sí es feature de SEM-IA — la regla, no el mecanismo. Ej.: la decisión "subagente vs sesión-dedicada" (Gap 8 ya formalizado) es feature de SEM-IA; el Task tool en sí es dependencia.

### 1.4 — Convención AC: "verificable vía:" por AC enumerado (anti-Gherkin formal en este WA)

**Definición operativa:** cada feature producida tiene `AC enumerados` con identificador único y, **por cada AC, una línea explícita** `verificable vía: <mecanismo>` que declara CÓMO se observa el cumplimiento.

**Formato canónico del bloque AC en cada feature file:**

```markdown
## Acceptance Criteria (preview — Gherkin formal pendiente)

- **AC-X1**: <enunciado del criterio>
  - *verificable vía*: <mecanismo>
- **AC-X2**: <enunciado>
  - *verificable vía*: <mecanismo>
- ...
```

**Mecanismos válidos** (catálogo no-cerrado, ampliable):

| Mecanismo | Ejemplo de uso |
|---|---|
| `inspección vault` | "Verificable vía inspección vault: existe `vault/<path>` con frontmatter `type: capability`." |
| `ejecución de slash command` | "Verificable vía ejecución `/status` en sesión cualquiera: output incluye sección 'Backlog' con N>0 nodos." |
| `sesión de rol` | "Verificable vía sesión `npm run sem` en vault vacío: el PO presenta panorámica antes de pedir propuesta." |
| `comportamiento agente observable` | "Verificable vía comportamiento del PO en Modo 1 step-6b: declara DECISIONES PO + preguntas filtradas, no agregación bruta de scope-scan." |
| `inspección de archivo` | "Verificable vía inspección de `CLAUDE.md`: incluye sección 'Tres mecanismos de invocación' con matriz orientativa." |
| `cobertura piezas en test futuro` | "Verificable vía tabla cobertura del step-7 QA del WA contenedor: la pieza X está mapeada a esta feature como owner único." |
| `comparación pre/post` | "Verificable vía comparación pre/post: antes de aplicar `/verify` el nodo está `draft`; después está `active`." |
| `ejecución de subagente focal` | "Verificable vía Task tool invocando rol Y con prompt Z: output incluye `scope-scan-output` estructurado." |

**Diferencia con Gherkin formal (que NO se aplica en este WA):**

Gherkin formal exige `Feature → Background → Scenarios (Given/When/Then) → AC-S* del threat-model si aplica`. AC enumerados con "verificable vía:" son **preview** — declaran QUÉ se verifica y CÓMO se observa, pero no formalizan el escenario completo. La completitud Gherkin queda para WAs feature-design single posteriores donde se materialice cada feature para delivery.

**Anclaje bibliográfico:** Adzic *Specification by Example* — *"living documentation must be testable; tests must be observable from the example."* La anotación "verificable vía:" es el puente entre el AC declarativo y la observabilidad del ejemplo.

### 1.5 — Cross-links y parent único en solapamientos detectados

**Reglas para cada feature producida:**

1. **`parent`**: una capability **única** (no lista). Si una pieza está en dos capabilities (solapamiento), el PO decide ownership por **criterio de cobertura primaria del JTBD**. Documentado explícitamente en el feature file.
2. **`also-relates-to`**: lista de cross-links cross-cap o cross-feature **declarados explícitamente**. Especialmente obligatorio en los 3 solapamientos identificados (CAP-01↔CAP-03 estados canónicos, CAP-04↔CAP-05 skills, CAP-06↔CAP-03 /wa + Progreso entries).
3. **`depends-on`**: lista de features predecesoras (otra feature que esta requiere) o piezas-del-harness (`depends-on-harness:` campo separado). Declaración de coupling apropiado Ford — explicito, no oculto.
4. **`related-adrs`**: lista de ADRs latentes apuntados per-feature. Lista de 10 candidatos identificados durante scope-scan:
   - ADR-latente-001 (Claude Code v1 harness primario)
   - ADR-latente-002 (Vault role-first organización física)
   - ADR-latente-003 (Frontmatter YAML + wiki-links)
   - ADR-latente-004 (Estados canónicos del nodo + transiciones)
   - ADR-latente-005 (Skills como unidad de empaquetado bibliográfico)
   - ADR-latente-007 (Fases SDLC redefinibles por adopter)
   - ADR-latente-008 (Backlog como query emergente)
   - ADR-latente-009 (Tres checkpoints uniformes del WA)
   - ADR-latente-010 (Algoritmo declarativo verifiers)
   - ADR-meta-1 (Uniformidad mode-flag templates batch-capables)
   - ADR-security-trans (Modelo threat surface del framework — recomendado por security step-6 del WA-004)

**Mapping decisión de ownership en los 3 solapamientos detectados:**

| Solapamiento | Decisión PO ownership | Razón |
|---|---|---|
| Estados canónicos (CAP-01 nodos del grafo ↔ CAP-03 estados del WA) | **CAP-01** parent (espina dorsal del grafo). Feature de "estados canónicos del WA" en CAP-03 declara `also-relates-to: feature-<estados-nodo-grafo-en-CAP-01>` | El WA es UN nodo del grafo (subtipo). Los estados canónicos son convención del grafo entero. CAP-03 hereda + extiende con estados específicos del WA (`aborted`, etc.). |
| Skills empaquetadas (CAP-04 las usa ↔ CAP-05 las empaqueta) | **CAP-05** parent (catálogo de skills construidas como unidad de empaquetado bibliográfico). Feature de "verificación cruzada multi-rol" en CAP-04 declara `also-relates-to: feature-<catalogo-skills-en-CAP-05>` + `depends-on: feature-<skills-architect-en-CAP-05>, feature-<skills-qa-en-CAP-05>` | CAP-05 es el catálogo; CAP-04 lo invoca como mecanismo. Ownership en el catálogo, dependencia en quien invoca. |
| /wa + Progreso entries (CAP-03 los define ↔ CAP-06 los visibiliza) | **CAP-03** parent (estructura del WA + protocolo handoff). Feature de "visibilidad operativa /wa" en CAP-06 declara `also-relates-to: feature-<estructura-WA-CAP-03>, feature-<progreso-entries-CAP-03>` | El WA y el handoff Progreso son ground truth de CAP-03. `/wa` es un slash que **lee** el WA — su visibilidad es CAP-06 pero el contenido es CAP-03. |

---

## Bloque 2 — Flujo del operador end-to-end

> Secuencia experiencial canónica desde el momento en que el operador humano descubre SEM-IA hasta que cierra su primer ciclo completo Discovery→Delivery con `/verify` aprobado. Sirve de **criterio de coherencia** para asignar `also-relates-to` cross-cap a features que cubren momentos adyacentes del flujo (Designer flag D1 del scope-scan).
>
> El flujo recorre las 5 fases del SDLC SEM-IA: **Onboarding → Discovery → Design → Implementation → Verification**, más una fase 6 emergente (**Maintenance / Adapters externos**) que queda fuera de scope del WA-004 pero se documenta para coherencia futura.
>
> Cada momento marcado con 🧑 = operador humano, 🤖 = operador agente, ⚡ = momento conjunto humano+agente.

### Fase 1 — Onboarding (humano newcomer descubre el framework)

| # | Momento del operador | Capability(s) que cubre | Flag de gap residual |
|---|---|---|---|
| 1.1 | 🧑 Encuentra el repo SEM-IA por enlace externo (paper, charla, comunidad). | CAP-J · articulación pública | — |
| 1.2 | 🧑 Lee README.md raíz. Le toma comprender la tesis ("La IA como infraestructura, el humano como autor"), el modelo conceptual (8 roles × 7 dimensiones × 14 templates), y los 5 reglas operativas. | CAP-J · Nielsen #10 help & documentation + Norman conceptual model transfer | **Flag D2 designer**: README ~65 KB sin glosario navegable ni ruta de lectura por audiencia. Features de "glosario público" + "ruta de lectura" entran en este WA (decisión confirmada). |
| 1.3 | 🧑 Inspecciona estructura del repo: encuentra `vault/`, `.claude/`, `src/`, governance docs. Comprende vault organizado role-first. | CAP-A · grafo declarativo (vault como manifestación física) + CAP-J | — |
| 1.4 | 🧑 Lee `CLAUDE.md` raíz para entender el entry point. Aprende que `npm run sem` arranca sesión PO. | CAP-J + CAP-G · inception greenfield (CLAUDE.md raíz como guía estática) | — |
| 1.5 | 🧑 Ejecuta `npm install` para resolver dependencias del repo. | (operación del runtime, NO feature SEM-IA) | — |

### Fase 2 — Inception greenfield (humano arranca el sistema con vault vacío)

| # | Momento del operador | Capability(s) | Flag |
|---|---|---|---|
| 2.1 | 🧑 Ejecuta `npm run sem` en la terminal. | CAP-B · multi-rol (atajos npm como mecanismo de entrada por rol) + CAP-G · inception | — |
| 2.2 | 🤖 PO sesión arranca: carga identidad bibliográfica (`vault/product-owner/CLAUDE.md` → `.claude/agents/product-owner.md`). | CAP-B · agent files + wrappers CLAUDE.md jerárquicos + CAP-E · anclaje bibliográfico (Cagan + Sinek + Rumelt + Doerr + Christensen citados) | — |
| 2.3 | 🤖 PO ejecuta **ritual de inicio** (Modo 1 paso 1): lee `vault/product-owner/strategy/`, `vault/shared/sessions/active/`, `vault/product-owner/specs/`, `vault/architect/adrs/`, `vault/shared/governance/`. Detecta vault vacío (greenfield). | CAP-F · visibilidad operativa (ritual de inicio del PO) + CAP-A · grafo declarativo | — |
| 2.4 | ⚡ PO presenta panorámica al humano: "Visión: ausente · Goals: 0 · Capabilities: 0 · WAs activos: 0 · Backlog: vacío". Pregunta "¿qué quieres hacer?". | CAP-F · panorámica de inicio + Nielsen #1 visibility of system status | — |
| 2.5 | 🧑 Humano trae propuesta inicial (ej. "construir SaaS de gestión de inventarios"). | CAP-G · inception entry-point | — |
| 2.6 | 🤖 PO escucha + clarifica + clasifica `outcome-type` (Modo 1 paso 3). Detecta gaps upstream: visión + goals + capabilities + features faltantes. | CAP-G · clasificación outcome-type + CAP-C · workflow templates indexados por fase SDLC | — |
| 2.7 | 🤖 PO propone **cadena de WAs por gaps** (`vision-creation` → `goal-definition × N` → `capability-creation` → `feature-design`) y la presenta al humano para confirmar. | CAP-G · cadena de WAs greenfield + CAP-C · workflows.md catálogo | — |

### Fase 3 — Scope-scan multi-rol (reunión de discovery flat parallel)

| # | Momento del operador | Capability(s) | Flag |
|---|---|---|---|
| 3.1 | 🤖 PO convoca scope-scan al draftear primer WA de la cadena. Construye 5 prompts (architect, designer, business-analyst, security-officer, qa) con identidad + propuesta + paths a leer. | CAP-D · verificación cruzada (reunión de discovery, primer checkpoint del WA lifecycle) + CAP-B · subagentes via Task tool | **Dependencia harness** declarada: el mecanismo `Task tool` es del harness. La regla de cuándo invocar + cómo construir el prompt es SEM-IA. |
| 3.2 | 🤖 5 asesores en paralelo (`subagent_type: <rol>`, un solo mensaje del PO con 5 tool_use blocks). Cada uno carga su identidad, hace scope-scan focal desde su ángulo, devuelve `scope-scan-output` estructurado. | CAP-D · flat parallel scope-scan + CAP-E · skills bibliográficas aplicadas por cada asesor (Bass, Cagan, Nielsen, Moore, Shostack, Cohn) | — |
| 3.3 | 🤖 PO consolida outputs (unión dimensions-detected + cross-links + flags + questions). Aplica **Filtro PO** (Cagan principio "PM strong decides informed"): clasifica flags en 4 categorías (1: aplico yo · 2: descarto con razón · 3: difiero a WA futuro · 4: requiere decisión humana real). | CAP-D · sign-off interno del PO (anti-mecanización) + CAP-E · Cagan principio aplicado | — |
| 3.4 | ⚡ PO presenta al humano: DECISIONES tomadas (cat 1) + DESCARTES con razón (cat 2) + APARCADOS a futuro (cat 3) + PREGUNTAS reales (cat 4). Humano responde solo las preguntas cat 4. | CAP-F · visibilidad + CAP-D · transparencia del proceso de filtrado | — |
| 3.5 | 🤖 PO carga template del outcome-type (workflows.md) + adapta steps según scope-scan output + escribe el WA en `vault/shared/sessions/active/wa-NNN.md` con frontmatter completo + cuerpo autocontenido (Gap 7) + Briefings por step para steps no-PO (Gap 10) + checkpoint Gap 9 si subagentes con autoridad de edición. | CAP-C · estructura inline WA + workflow templates + CAP-A · frontmatter YAML declarativo | — |
| 3.6 | ⚡ PO presenta WA al humano. Humano confirma o ajusta. | CAP-F · confirmación legible al humano | — |

### Fase 4 — Step active de la cadena (discovery → design)

| # | Momento del operador | Capability(s) | Flag |
|---|---|---|---|
| 4.1 | 🤖 Si step-1 active-role = PO: arranca Modo 2 directamente sin cambio de sesión. Marca step in-progress en WA. | CAP-C · estructura WA + protocolo Modo 2 + CAP-B · operación del PO | — |
| 4.2 | 🤖 PO conduce step aplicando la skill apropiada (`vision-quality-check`, `goal-quality-check`, `capability-derivation`, `feature-decomposition`, etc.). Cita bibliografía. | CAP-E · 7 skills PO empaquetadas con bibliografía + carga perezosa nativa harness (dependencia) | — |
| 4.3 | 🤖 Durante step, give-and-take Cagan: invoca subagentes mid-step (architect/designer/business/security) cuando emerge duda relevante a otro dominio. | CAP-D · give-and-take subagentes + CAP-B · Task tool (dependencia harness) | — |
| 4.4 | 🤖 PO produce el artefacto: nodo en `vault/product-owner/strategy/<file>.md` (o `specs/`) con frontmatter completo + cross-links + status: draft + citas bibliográficas. | CAP-A · grafo declarativo (nodo creado con frontmatter + wikilinks + cross-links) + CAP-E · citas | — |
| 4.5 | 🤖 PO marca step done + entrada Progreso (resumen + artefactos + decisiones + "para siguiente step" + flags) + ejecuta **post-step scope-scan** (5 asesores restantes en paralelo) — segundo checkpoint del WA lifecycle. | CAP-C · Progreso entries + CAP-D · post-step scope-scan + CAP-F · auditabilidad del handoff | — |
| 4.6 | 🤖 PO consolida post-step scope-scan aplicando Filtro PO. Si flags categoría 4 → presenta al humano con 3 opciones (aparcar / detener / extender). | CAP-D · post-step Filtro PO + CAP-F · presentación al humano | — |
| 4.7 | ⚡ Si siguiente step es PO → continúa sin cambio de sesión. Si es otro rol → handoff verbal: *"Step X completado. Step Y pending para [rol]. Abre `npm run [rol-short]`."* | CAP-B · handoff explícito step→step + atajos npm | — |
| 4.8 | 🧑 Humano abre nueva terminal (o cambia de tab), ejecuta `npm run arch` (o el atajo apropiado). | CAP-B · npm scripts como entrada por rol | **Flag B latente** (designer): cognitive load del operador alternando entre N terminales abiertas + 8 roles disponibles. Feature candidata: "Orientación sobre qué rol abrir ante ambigüedad" en CAP-B. |
| 4.9 | 🤖 Architect (o el rol siguiente) arranca: carga identidad, lee WA activo via `/wa`, lee Progreso entries previas para inputs concretos, conduce su step aplicando sus skills (adr-writing, capability-viability-review, coupling-detection, coherence-evaluation, threat-modeling, etc.). Si tiene `modality: subagente` con autoridad de edición → al cerrar declara bloque `filesystem-changes` literal (Gap 9). | CAP-B · identidad por rol + CAP-C · /wa + Progreso entries + CAP-E · skills del rol + CAP-D · contrato filesystem-changes | — |
| 4.10 | 🔁 Ciclo se repite por cada step del WA hasta que todos están done. | CAP-C · steps ordenados con dependencias declaradas | — |

### Fase 5 — Sign-off / `/verify` (cierre del WA)

| # | Momento del operador | Capability(s) | Flag |
|---|---|---|---|
| 5.1 | 🧑 Humano ejecuta `/verify` desde sesión PO. | CAP-D · slash /verify + CAP-F · visibilidad de cierre | — |
| 5.2 | 🤖 PO identifica WA a verificar, comprueba closure-criteria mecánicamente. Si fallan → indica al humano qué falta. | CAP-D · closure-criteria mecánico (auditabilidad) | — |
| 5.3 | 🤖 PO deriva lista de verificadores aplicando algoritmo declarativo `verifiers = {custodian(d) : d ∈ wa.dimensions-affected}` (consulta `dimensions.md`). | CAP-D · algoritmo verifiers + CAP-A · dimensions.md como ground truth | — |
| 5.4 | 🤖 PO invoca verificadores en paralelo via Task tool. Cada uno recibe: WA completo + paths a leer + tarea de verificación focal. Tercer checkpoint del WA lifecycle. | CAP-D · sign-off review flat parallel + CAP-B · subagentes (Task tool dependencia) | — |
| 5.5 | 🤖 PO consolida hallazgos: aprobado / objeción menor / objeción bloqueante. | CAP-D · consolidación + Filtro PO al cierre | — |
| 5.6 | 🤖 Si todos aprueban → PO aplica `on-close` transitions (lee cada entrada, modifica status del archivo correspondiente). Si objeciones bloqueantes → WA vuelve a activo. Si objeciones menores → presenta al humano para decisión. | CAP-D · on-close transitions + CAP-A · status del nodo lifecycle | — |
| 5.7 | 🤖 PO archiva el WA: mueve de `vault/shared/sessions/active/` a `vault/shared/sessions/archive/`. Actualiza `status: archived` en frontmatter. | CAP-C · archivado del WA + CAP-A · lifecycle del nodo WA | — |
| 5.8 | ⚡ PO confirma al humano todas las transiciones aplicadas + dónde quedó archivado el WA. | CAP-F · confirmación de cierre auditable | — |

### Fase 6 — Backlog → Delivery (Dual Track, primera feature implementada)

| # | Momento del operador | Capability(s) | Flag |
|---|---|---|---|
| 6.1 | 🧑 Humano consulta `/status`. Ve el backlog emergente (nodos con `status: ready-for-implementation`). | CAP-F · /status + CAP-A · backlog como query emergente (NO estructura persistente — propiedad arquitectónica) | — |
| 6.2 | 🧑 Humano decide qué feature implementar siguiente. Ejecuta `npm run sem` (o ya está en PO) y trae propuesta "implementar feature-NNN". | CAP-G · entry-point PO + CAP-F · backlog visible | — |
| 6.3 | 🤖 PO clasifica outcome-type = `feature-build`. Verifica precondición `consumes`: nodo `feature-NNN` existe con `status: ready-for-implementation`. | CAP-C · template feature-build + consumes verification | — |
| 6.4 | 🤖 PO drafta WA `feature-build` con steps developer + qa. Presenta al humano. | CAP-C · template implementation | — |
| 6.5 | ⚡ Humano confirma. PO indica: "Step-1 pending para developer. Abre `npm run dev`." | CAP-B · handoff a developer | — |
| 6.6 | 🤖 Developer arranca, lee WA + spec, implementa código en `src/` + tests con `// @sem-ia: <feature-id>` + `// @ac-coverage: AC-X1, AC-X2`. | CAP-A · trazabilidad @sem-ia + @ac-coverage (campo del grafo en código) | — |
| 6.7 | 🤖 QA arranca step-2: cobertura E2E + edge cases + AC-S* (si threat-model existe) + report en `vault/qa/reports/`. | CAP-D · QA verificación + CAP-A · @ac-coverage trazables | — |
| 6.8 | 🧑 + 🤖 `/verify` cierra el WA feature-build. on-close: `feature-NNN: ready-for-implementation → implemented`. | CAP-D · cierre feature + CAP-A · lifecycle | — |
| 6.9 | 🧑 Humano consulta `/status` → ve feature-NNN como implemented. Dual Track materializado: discovery (futuras features en cap-N) + delivery (feature-NNN implementada) coexisten. | CAP-F · visibilidad Dual Track Cagan/Patton | — |

### Fase 6 — Maintenance + adapters externos (futuro, fuera de scope WA-004)

| # | Momento del operador | Capability(s) | Flag |
|---|---|---|---|
| F.1 | 🧑 Adopter externo descubre SEM-IA en npm, ejecuta `npx sem-ia init --harness=claude-code`. Recibe estructura conforme. | CAP-H planned · portabilidad multi-harness | **Fuera de scope** WA-004 (planned). |
| F.2 | 🧑 Equipo con proyecto a medias quiere adoptar SEM-IA. Ejecuta `/adopt <ruta>`. SEM-IA hace archaeology del código, deriva grafo retroactivo. | CAP-I planned · adopción retroactiva | **Fuera de scope** WA-004 (planned). |
| F.3 | 🧑 + 🤖 Mantenimiento: WAs `bugfix`, `refactor`, `pipeline-change`, `infra-decision`, `observability-instrument`, ciclo de vida producto. | CAP-C · cobertura SDLC completa (5 fases) | — |

---

## Insights del flujo del operador (criterios para `also-relates-to` cross-cap)

**1. Onboarding humano (Fase 1) y articulación pública (CAP-J) son indistinguibles desde el operador**. Features de README + glosario + ruta de lectura cubren el momento del newcomer. `also-relates-to: cap-07-inception-greenfield` cuando una feature de CAP-J facilita el primer arranque del newcomer en Fase 2.

**2. Inception (Fase 2) y visibilidad operativa (CAP-F) son co-emergentes**. El ritual de inicio del PO + la panorámica son **simultáneamente** features de CAP-G (procedimiento de inception) y CAP-F (mecanismo de visibilidad). Decisión PO de ownership: cuando la feature describe **el procedimiento del PO** → parent CAP-G. Cuando describe **el output que el humano ve** → parent CAP-F. `also-relates-to` cruza ambas direcciones.

**3. Scope-scan (Fase 3) y verificación cruzada (CAP-D) son la misma capability vista desde dos lentes**. Scope-scan al crear WA + post-step scope-scan + sign-off review son los **3 checkpoints uniformes** de CAP-D. Filtro PO + presentación al humano cruzan CAP-D ↔ CAP-F.

**4. Step active (Fase 4) cruza CAP-B (rol activo) + CAP-C (WA structure) + CAP-E (skills aplicadas) + CAP-A (artefacto producido en el grafo)**. Cada feature de fase 4 tendrá típicamente 2-3 `also-relates-to` cross-cap.

**5. Sign-off (Fase 5) es la materialización mecánica de CAP-D + CAP-A (lifecycle del nodo)**. Algoritmo declarativo verifiers + on-close transitions son features de CAP-D con `also-relates-to: cap-01-grafo-declarativo` (porque tocan estados canónicos del nodo).

**6. Dual Track (Fase 6) emerge de CAP-C (workflows.md declara fases discovery/design/implementation) + CAP-F (/status muestra ambos tracks) + CAP-A (backlog como query emergente)**. Es propiedad **arquitectónica emergente**, no feature aislada — pero hay features que la materializan (`/status` con sección "Backlog" + visualización Dual Track).

---

## Bloque 3 — Inventario capability-by-capability

> Para cada capability operant: piezas reales del bootstrap (ground truth: discovery doc del WA-002) → features candidatas con enunciado JTBD del operador, parent único, cross-links cross-cap, ADRs latentes apuntados y `depends-on-harness` declarado cuando aplique. IDs `feature-NNN` secuenciales globales.

### CAP-A · Grafo declarativo persistente

**Piezas reales del bootstrap (de Job 1, WA-002 discovery doc):**
- `vault/` organización role-first (8 directorios de rol + `shared/`)
- `vault/shared/governance/repo-structure.md` (modelo conceptual del repo)
- `vault/shared/governance/dimensions.md` (7 dimensiones core + custodios)
- Frontmatter YAML obligatorio en todo nodo (campos: `type, id, title, parent, also-relates-to, depends-on, dimensions-affected, related-adrs, status`)
- Wiki-links `[[id]]` en contenido
- Estados canónicos del nodo declarados en CLAUDE.md raíz
- Skill compartida `graph-cross-link-declaration`
- Comentarios de trazabilidad en código: `// @sem-ia: <node-id>` + `// @ac-coverage: AC-X1, AC-X2`

**Features candidatas:**

#### feature-001 · Vault role-first como organización física del grafo
- **JTBD operador**: *"El operador (humano + agente) puede localizar artefactos del proyecto por **rol custodio** (no por tipo técnico), de modo que la navegación refleja la dimensión responsable y se evitan colisiones cross-rol en el sistema de archivos."*
- **Parent**: cap-01-grafo-declarativo-persistente
- **also-relates-to**: cap-02-multirol-agentes-homologos (los roles que custodian existen por CAP-B)
- **depends-on**: —
- **depends-on-harness**: filesystem versionado por git
- **related-adrs**: ADR-latente-002 (Vault role-first como organización física)
- **dimensions-affected**: [product, technical]
- **AC preview**: cobertura `vault/<rol>/` para los 8 roles; `vault/shared/` para cross-rol; `vault/shared/governance/repo-structure.md` documenta el modelo.

#### feature-002 · Estructura inline del frontmatter YAML por tipo de nodo
- **JTBD operador**: *"El operador agente puede leer **metadata declarativa** (type, id, parent, cross-links, status) de cualquier nodo en formato uniforme, de modo que extrae contexto del grafo sin parsear el contenido libre del archivo."*
- **Parent**: cap-01-grafo-declarativo-persistente
- **also-relates-to**: cap-05-anclaje-bibliografico-skills (las skills declaran la estructura del frontmatter del nodo que crean — Gap 2 ya formalizado)
- **depends-on**: —
- **depends-on-harness**: parser YAML del runtime
- **related-adrs**: ADR-latente-003 (Frontmatter YAML + wiki-links como mecanismo declarativo)
- **dimensions-affected**: [product, technical, security]  # path traversal latente en `parent` flagged by security
- **AC preview**: cada tipo de nodo (vision, goal, capability, feature, spec, adr, learning, working-agreement) tiene estructura inline declarada en su SKILL.md creador (Gap 2 aplicado); validación de campos obligatorios verificable vía inspección de archivos.

#### feature-003 · Wiki-links `[[id]]` como navegación interna entre nodos del grafo
- **JTBD operador**: *"El operador humano puede navegar visualmente entre nodos relacionados via referencias `[[id]]` en el contenido, de modo que la lectura del grafo no requiere consultar frontmatter ni paths de filesystem."*
- **Parent**: cap-01-grafo-declarativo-persistente
- **also-relates-to**: —
- **depends-on**: feature-002 (los ids referenciados existen en frontmatter)
- **depends-on-harness**: render Markdown del editor / viewer (no específico del harness)
- **related-adrs**: ADR-latente-003 (Frontmatter YAML + wiki-links)
- **dimensions-affected**: [product, usability]
- **AC preview**: convención `[[id]]` documentada en CLAUDE.md raíz sección "Convenciones"; al menos un nodo del vault demuestra wikilinks resolviendo entre archivos (verificable vía inspección de capability files que se cruzan).

#### feature-004 · Estados canónicos del nodo + transiciones validables del lifecycle
- **JTBD operador**: *"El operador (humano + agente) puede consultar el **estado del lifecycle** de cualquier nodo (draft, active, ready-for-implementation, in-implementation, implemented, superseded, deprecated, aborted, aborted-reference) y predecir las transiciones válidas, de modo que el grafo es navegable temporalmente y las decisiones tomadas son auditables en el tiempo."*
- **Parent**: cap-01-grafo-declarativo-persistente
- **also-relates-to**: cap-03-working-agreements-sdlc (estados del WA + protocolo pivot heredan + extienden los estados del nodo — solapamiento resuelto: ownership CAP-A, herencia CAP-C)
- **depends-on**: feature-002 (campo `status` en frontmatter)
- **depends-on-harness**: —
- **related-adrs**: ADR-latente-004 (Estados canónicos + transiciones)
- **dimensions-affected**: [product, technical]
- **AC preview**: 10 estados canónicos documentados en CLAUDE.md raíz sección "Estados canónicos del nodo"; protocolo de pivot WA-mid-flight declara transiciones para `aborted` + `aborted-reference` en workflows.md.

#### feature-005 · Backlog como query emergente sobre `status`
- **JTBD operador**: *"El operador (humano + agente) puede consultar el backlog como **query computada** sobre nodos con `status: ready-for-implementation`, de modo que no se mantiene estructura persistente paralela y el backlog refleja siempre el estado actual del grafo sin sincronización manual."*
- **Parent**: cap-01-grafo-declarativo-persistente
- **also-relates-to**: cap-03-working-agreements-sdlc (los WAs `feature-design` transitan a `ready-for-implementation` vía on-close, alimentando el backlog) + cap-06-visibilidad-operativa (/status muestra sección Backlog)
- **depends-on**: feature-004 (estados canónicos), feature-002 (campo `status` parseable)
- **depends-on-harness**: —
- **related-adrs**: ADR-latente-008 (Backlog como query emergente, no estructura persistente)
- **dimensions-affected**: [product, technical]
- **AC preview**: query `find vault/ -name "*.md" | xargs grep -l "status: ready-for-implementation"` produce backlog actual sin estructura persistente nueva; documentado en CLAUDE.md raíz sección "Modelo conceptual".

#### feature-006 · Skill compartida `graph-cross-link-declaration`
- **JTBD operador**: *"El operador agente (cualquier rol creando un nodo nuevo) puede declarar las aristas del grafo (`parent`, `also-relates-to`, `depends-on`, `dimensions-affected`, `related-adrs`) aplicando una skill compartida con bibliografía auditable, de modo que la convención cross-link es uniforme entre todos los roles sin que cada uno la re-derive."*
- **Parent**: cap-01-grafo-declarativo-persistente
- **also-relates-to**: cap-05-anclaje-bibliografico-skills (la skill es unidad de empaquetado bibliográfico — pieza compartida)
- **depends-on**: feature-002 (frontmatter), feature-004 (estados que `status` toma)
- **depends-on-harness**: carga perezosa nativa de Agent Skills (Claude Code)
- **related-adrs**: ADR-latente-005 (Skills como unidad de empaquetado bibliográfico)
- **dimensions-affected**: [product, technical, quality]
- **AC preview**: SKILL.md existe en `.claude/skills/shared/graph-cross-link-declaration/`; documenta los 5 tipos de cross-link declarables; carga perezosa nativa al matchear contexto.

#### feature-007 · Trazabilidad código ↔ grafo vía `// @sem-ia: <node-id>` y `// @ac-coverage: AC-X*`
- **JTBD operador**: *"El operador humano (developer) o agente (QA) puede **trazar artefactos del código** (módulos, tests) hacia nodos del grafo (features, ACs) vía comentarios convencionales, de modo que la cobertura AC↔tests es verificable mecánicamente sin estructura paralela."*
- **Parent**: cap-01-grafo-declarativo-persistente
- **also-relates-to**: cap-03-working-agreements-sdlc (el WA `feature-build` consume feature/spec y produce código con estos comentarios)
- **depends-on**: feature-002 (los node-ids referenciados existen)
- **depends-on-harness**: —
- **related-adrs**: ADR-latente-008 (la trazabilidad emerge como propiedad declarativa del grafo)
- **dimensions-affected**: [product, technical, quality]
- **AC preview**: convención `// @sem-ia:` documentada en CLAUDE.md sección "Convenciones"; convención `// @ac-coverage:` documentada; al menos un test futuro demuestra trazabilidad (verificable vía grep sobre src/ cuando exista código).

---

### CAP-B · Operación multi-rol vía agentes IA homólogos especializados

**Piezas reales del bootstrap (de Job 2, WA-002 discovery doc):**
- 8 agent files en `.claude/agents/*.md`: product-owner, architect, designer, business-analyst, security-officer, qa, developer, devops
- `vault/shared/governance/role-catalog.md` (catálogo formal + atajos npm + dimensión custodiada + Cagan risk)
- 7 wrappers `vault/<rol>/CLAUDE.md` (developer pendiente — gap menor)
- `package.json` con npm scripts: `sem`, `po`, `arch`, `des`, `biz`, `sec`, `qa`, `dev`, `ops`
- CLAUDE.md raíz (guía estática + entrypoint de PO via `npm run sem`)
- Mecanismo subagent via Task tool (dependencia harness — NO feature propia)
- Criterio operativo "subagente vs sesión dedicada" (Gap 8 formalizado en WA-003)

**Features candidatas:**

#### feature-008 · Identidad bibliográficamente anclada por rol vía agent files
- **JTBD operador**: *"El operador agente puede arrancar con **identidad de rol auditada bibliográficamente** (autores citados, dimensión custodiada, skills disponibles, modos de operación, reglas operativas, lo que NO hace), de modo que opera coherente entre sesiones sin re-derivar quién es y el humano puede invertir en cuál rol consulta para qué."*
- **Parent**: cap-02-multirol-agentes-homologos
- **also-relates-to**: cap-05-anclaje-bibliografico-skills (la identidad cita bibliografía del library)
- **depends-on**: feature-002 (frontmatter del agent file)
- **depends-on-harness**: mecanismo agent files de Claude Code (subagent_type → `.claude/agents/<rol>.md`)
- **related-adrs**: ADR-latente-001 (Claude Code v1 como harness primario)
- **dimensions-affected**: [product, technical, security]  # spoofing latente vector S
- **AC preview**: 8 agent files existen en `.claude/agents/`; cada uno declara identidad + dimensión + skills + modos + reglas; verificable vía inspección de archivos + ejecución `Task subagent_type: <rol>` que carga la identidad.

#### feature-009 · Catálogo formal de roles + custodios + Cagan risk
- **JTBD operador**: *"El operador humano puede consultar **qué rol custodia qué dimensión y qué risk de Cagan aborda**, de modo que al detectar un trabajo nuevo sabe a qué rol delegarlo y por qué."*
- **Parent**: cap-02-multirol-agentes-homologos
- **also-relates-to**: cap-01-grafo-declarativo-persistente (dimensions.md y role-catalog.md son ground truth conceptual del grafo)
- **depends-on**: —
- **depends-on-harness**: —
- **related-adrs**: ADR-latente-002 (organización del grafo) latente
- **dimensions-affected**: [product]
- **AC preview**: `vault/shared/governance/role-catalog.md` existe; declara 8 roles con (sesión, dimensión, Cagan-risk, cuándo invocar como subagente); coherente con `vault/shared/governance/dimensions.md` (mapping dimensión → custodio único).

#### feature-010 · Entry-point por rol vía atajos npm + wrappers CLAUDE.md jerárquicos
- **JTBD operador**: *"El operador humano puede arrancar una sesión de cualquier rol con un comando único (`npm run sem|arch|des|biz|sec|qa|dev|ops`) que carga **identidad + zona de trabajo + skills** del rol sin teclear paths ni recordar convenciones, de modo que el cambio entre roles es operativamente barato."*
- **Parent**: cap-02-multirol-agentes-homologos
- **also-relates-to**: cap-06-visibilidad-operativa (cada sesión presenta panorámica vía ritual de inicio del rol)
- **depends-on**: feature-008 (identidad del rol existe en agent file), feature-002 (frontmatter del wrapper)
- **depends-on-harness**: mecanismo CLAUDE.md jerárquico de Claude Code (carga `.claude/agents/<rol>.md` cuando se arranca desde `vault/<rol>/`)
- **related-adrs**: ADR-latente-001 (Claude Code v1 harness primario), ADR-latente-002 (vault role-first)
- **dimensions-affected**: [product, usability]  # Nielsen #7 flexibility + efficiency
- **AC preview**: `package.json` declara los 9 scripts (`sem`, `po`, `arch`, `des`, `biz`, `sec`, `qa`, `dev`, `ops`); 7 wrappers `vault/<rol>/CLAUDE.md` existen (developer pendiente — gap menor declarado); cada script ejecutado arranca sesión Claude Code en el directorio del rol con la identidad cargada.

#### feature-011 · CLAUDE.md raíz como guía estática + entry-point del PO
- **JTBD operador**: *"El operador humano puede comprender el **modelo conceptual completo del framework** (visión, grafo, 7 dimensiones, 8 roles, 14 templates, 5 reglas, slash commands) leyendo un único documento de entrada, de modo que opera con criterio sin tener que descubrir el sistema fragmentado en docs dispersos."*
- **Parent**: cap-02-multirol-agentes-homologos
- **also-relates-to**: cap-07-inception-greenfield (CLAUDE.md raíz declara `npm run sem` como entrada por defecto al sistema) + cap-10-articulacion-publica (CLAUDE.md raíz es doc público auditable)
- **depends-on**: feature-009 (role-catalog), feature-004 (estados canónicos)
- **depends-on-harness**: mecanismo CLAUDE.md raíz auto-cargado por Claude Code al arrancar
- **related-adrs**: ADR-latente-001 (harness primario)
- **dimensions-affected**: [product, usability]  # Nielsen #10 help & documentation
- **AC preview**: `/Users/pelayo/Developer/SEM-AI/CLAUDE.md` existe; declara la guía estática del proyecto; documenta los 3 mecanismos de invocación + las 5 reglas para el humano + slash commands disponibles + estados canónicos + estructura de WA + briefing por step.

#### feature-012 · Subagente vs sesión-dedicada como criterio operativo de delegación
- **JTBD operador**: *"El operador agente orquestador (típicamente PO al draftear WA, o cualquier rol mid-step) puede **decidir si invocar a otro rol como subagente focal one-shot o derivar al humano a abrir sesión dedicada multi-turn**, aplicando criterio bibliográfico anclado en Anthropic Claude Code docs + Cagan principio 2 give-and-take, de modo que la modalidad de cada step es decisión explícita auditable y no improvisación."*
- **Parent**: cap-02-multirol-agentes-homologos
- **also-relates-to**: cap-03-working-agreements-sdlc (modality declarado por step en WA)
- **depends-on**: feature-008 (identidad del rol invocado existe)
- **depends-on-harness**: mecanismo Task tool de Claude Code + mecanismo sesión multi-turn
- **related-adrs**: ADR-latente-001 (harness primario que provee Task tool)
- **dimensions-affected**: [product, technical]
- **AC preview**: criterio "participación humana mid-trabajo" declarado en CLAUDE.md raíz sección "Tres mecanismos de invocación"; matriz orientativa de 8 tipos de step con modality preferida; campo `modality` opcional en `default-steps` de workflow templates; verificable vía inspección de WA-003 archivado (cada step declara `modality`).

---

#### Sub-anexo Grupo 1 — Cobertura piezas-bootstrap CAP-A + CAP-B

| Pieza del bootstrap (Job 1 + 2) | Feature owner | Cobertura |
|---|---|---|
| `vault/` organización role-first | feature-001 | Total |
| `vault/shared/governance/repo-structure.md` | feature-001 (AC: documenta el modelo) | Parcial — doc se referencia |
| `vault/shared/governance/dimensions.md` | feature-009 (AC: coherente con role-catalog) | Total |
| Frontmatter YAML obligatorio | feature-002 | Total |
| Wiki-links `[[id]]` | feature-003 | Total |
| Estados canónicos del nodo | feature-004 | Total |
| Skill `graph-cross-link-declaration` | feature-006 | Total |
| Comentarios `// @sem-ia:` + `// @ac-coverage:` | feature-007 | Total |
| 8 agent files | feature-008 | Total |
| `vault/shared/governance/role-catalog.md` | feature-009 | Total |
| 7 wrappers `vault/<rol>/CLAUDE.md` | feature-010 | Total |
| `package.json` npm scripts | feature-010 | Total |
| CLAUDE.md raíz | feature-011 | Total |
| Mecanismo subagente Task tool | **NO es feature propia** (depends-on-harness declarado en feature-008, 012) | n/a |
| Backlog query (Job 1) | feature-005 | Total |
| Criterio modality (Gap 8) | feature-012 | Total |

Grupo 1 total: **12 features** (feature-001..feature-012). 0 piezas sin cobertura.

---

### CAP-C · Coordinación de trabajo vía Working Agreements indexados por fase SDLC

**Piezas reales del bootstrap (de Job 3, WA-002 discovery doc):**
- `vault/shared/governance/workflows.md` (14 templates por fase SDLC: discovery / design / implementation / operations / meta)
- Estructura inline del WA declarada en CLAUDE.md raíz (frontmatter + steps + scope-allowed/forbidden + closure-criteria + on-close)
- Slash `/wa` — detalle del WA activo  (NOTA: el slash en sí pertenece a CAP-F como mecanismo de visibilidad — la estructura del WA que `/wa` lee pertenece a CAP-C)
- Protocolo de handoff explícito step→step + Progreso entries audit-ready (declarado en cada agent file)
- Protocolo de pivot WA mid-flight (Gap 4 formalizado en WA-003) en `workflows.md`
- Regla de autocontención del WA (Gap 7 formalizado en CLAUDE.md raíz + agent file PO)
- Estados canónicos del WA (active, archived, aborted) — heredados de feature-004 CAP-A

**Features candidatas:**

#### feature-013 · Catálogo de 14 workflow templates indexados por fase SDLC
- **JTBD operador**: *"El operador agente orquestador (típicamente PO en Modo 1) puede **clasificar el outcome-type** de cualquier request humano contra un catálogo cerrado de 14 templates (vision-creation, goal-definition, capability-creation, feature-design, adr, threat-model, feature-build, bugfix, refactor, pipeline-change, infra-decision, observability-instrument, doc-edit, trivial), de modo que cada bloque de trabajo arranca con `default-steps + consumes + on-close + collaborative-pattern` preestablecidos auditables bibliográficamente y no improvisación."*
- **Parent**: cap-03-working-agreements-sdlc
- **also-relates-to**: cap-01-grafo-declarativo-persistente (workflows.md es ground truth conceptual)
- **depends-on**: feature-002 (frontmatter del WA materializa los templates)
- **depends-on-harness**: —
- **related-adrs**: ADR-latente-007 (Fases SDLC redefinibles por adopter)
- **dimensions-affected**: [product, technical]
- **AC preview**: `vault/shared/governance/workflows.md` declara 5 fases × 14 outcome-types; cada template declara `default-steps` (con role + phase + purpose + modality + optional + condition) + `on-close` (transiciones de status); heurística keywords→outcome-type documentada; verificable vía inspección + ejecución de PO Modo 1 paso 3 que clasifica.

#### feature-014 · Estructura inline del Working Agreement (frontmatter + cuerpo autocontenido)
- **JTBD operador**: *"El operador humano puede leer cualquier WA standalone (sin abrir archivos referenciados) y comprender qué se va a hacer + por qué + cómo, con frontmatter declarativo (outcome-type, phase, objective, dimensions-affected, participants, steps[], scope-allowed/forbidden, verifiers-required, closure-criteria, on-close) + cuerpo autocontenido (regla Gap 7 / Cohn INVEST 'I = Independent'), de modo que el WA es contrato auditable + trabajo entregable + registro histórico simultáneamente."*
- **Parent**: cap-03-working-agreements-sdlc
- **also-relates-to**: cap-01-grafo-declarativo-persistente (el WA es un nodo del grafo con frontmatter como cualquier otro)
- **depends-on**: feature-002 (frontmatter), feature-013 (template del que hereda)
- **depends-on-harness**: —
- **related-adrs**: ADR-latente-003 (frontmatter YAML), ADR-latente-007 (templates extensibles)
- **dimensions-affected**: [product, technical, quality]
- **AC preview**: estructura inline declarada en CLAUDE.md raíz sección "Estructura de un Working Agreement"; regla de autocontención + briefing por step (4 bloques canónicos) documentadas; verificable vía inspección WA-003 archivado (cuerpo autocontenido) y WA-004 activo.

#### feature-015 · Handoff explícito step→step vía Progreso entries audit-ready
- **JTBD operador**: *"Al completar un step, el operador agente (cualquier rol activo) puede **transmitir contexto curado al rol siguiente** vía una entrada Progreso estructurada (resumen + artefactos + decisiones + 'para el siguiente step' + flags) que sirve como audit-trail + briefing operativo, de modo que el rol siguiente arranca con inputs concretos sin re-descubrir el contexto y el humano puede auditar quién hizo qué cuándo."*
- **Parent**: cap-03-working-agreements-sdlc
- **also-relates-to**: cap-06-visibilidad-operativa (Progreso entries son ground truth de error recovery Nielsen #9; Designer flag mayor)
- **depends-on**: feature-014 (estructura WA contiene sección Progreso)
- **depends-on-harness**: —
- **related-adrs**: ADR-latente-009 (checkpoints uniformes del WA lifecycle latente)
- **dimensions-affected**: [product, quality, usability]
- **AC preview**: protocolo handoff declarado en cada agent file ("Al completar tu step"); Progreso entries demostradas en WA-002 + WA-003 archivados; estructura canónica (resumen + artefactos + decisiones + para-siguiente-step + flags) presente en cada entry; verificable vía inspección de WAs archivados.

#### feature-016 · Protocolo de pivot de un WA mid-flight (Gap 4 formalizado)
- **JTBD operador**: *"Cuando durante un WA emerge insight que invalida el approach actual (4 señales declaradas), el operador (humano o agente orquestador) puede **refactorizar el contenedor de trabajo** vía 7 pasos canónicos (anunciar → marcar aborted → preservar trabajo parcial → mover archive → crear successor con supersedes → handoff), de modo que el pivot es decisión disciplinada Cagan-style en vez de abandono que rompe trazabilidad."*
- **Parent**: cap-03-working-agreements-sdlc
- **also-relates-to**: cap-01-grafo-declarativo-persistente (estados `aborted` y `aborted-reference` aplicados a nodos)
- **depends-on**: feature-004 (estados canónicos extendidos), feature-014 (estructura WA con campos aborted-*)
- **depends-on-harness**: —
- **related-adrs**: ADR-latente apuntado al pivot como decisión Nygard de proceso (a confirmar por Architect step-3)
- **dimensions-affected**: [product, quality]
- **AC preview**: sección "Protocolo de pivot de un WA mid-flight" en `vault/shared/governance/workflows.md` documenta 4 señales + 7 pasos canónicos + anti-patrones; estados `aborted` y `aborted-reference` en estados canónicos; aplicado en WA-001 que fue aborted (verificable vía inspección de su frontmatter en archive).

#### feature-017 · Closure-criteria + on-close transitions como contrato declarativo de cierre
- **JTBD operador**: *"Al ejecutar `/verify`, el operador agente PO puede **comprobar mecánicamente** que el WA cumple closure-criteria + aplicar las transiciones de status declaradas en `on-close` (formato `<path>: <status-inicial> → <status-final>`), de modo que el cierre es auditable + reproducible + no depende de juicio caso-a-caso."*
- **Parent**: cap-03-working-agreements-sdlc
- **also-relates-to**: cap-04-verificacion-multirol-cruzada (`/verify` ejecuta closure-criteria + on-close) + cap-01-grafo-declarativo-persistente (las transiciones tocan estados canónicos del nodo)
- **depends-on**: feature-013 (templates declaran on-close por defecto), feature-004 (estados canónicos)
- **depends-on-harness**: —
- **related-adrs**: ADR-latente-010 (algoritmo declarativo verifiers + on-close)
- **dimensions-affected**: [product, technical, quality]
- **AC preview**: cada template en `workflows.md` declara `on-close`; WA hereda al draftear; /verify aplica mecánicamente verificable vía inspección de WA-002 + WA-003 archivados (transiciones aplicadas registradas en frontmatter de los archivos transitados).

---

### CAP-D · Verificación multi-rol cruzada en checkpoints uniformes

**Piezas reales del bootstrap (de Job 4, WA-002 discovery doc):**
- Slash `/scope-scan "<propuesta>"` — flat parallel multi-rol on-demand (6 asesores en paralelo)
- Slash `/verify` — matriz declarativa `verifiers = {custodian(d) : d ∈ dimensions-affected}`
- Tres checkpoints uniformes del WA lifecycle: (1) discovery review al crear WA, (2) step checkpoint post-step, (3) sign-off al `/verify`
- `vault/shared/governance/verification-matrix.md` — guía orientativa de dimensiones × operaciones
- Skills de verificación (`capability-viability-review`, `feature-viability-review`, `coherence-evaluation`, `coupling-detection`, `threat-modeling`, `*-quality-check`) — pertenecen a CAP-E como catálogo (depends-on para CAP-D)
- Give-and-take mid-step Cagan principio 2 — el rol activo invoca subagentes a otros dominios
- Filtro PO al consolidar scope-scan (Gap 6 formalizado en WA-003) — 4 categorías Cagan
- Contrato `filesystem-changes` para subagentes con autoridad de edición (Gap 9 formalizado en WA-003)
- Briefing por step (4 bloques canónicos: mapa grafo + contexto conversacional + razonamiento PO + output esperado) — Gap 10 formalizado en WA-003

**Features candidatas:**

#### feature-018 · Slash `/scope-scan "<propuesta>"` para reunión multi-rol on-demand
- **JTBD operador**: *"El operador agente orquestador (típicamente PO al draftar WA, o cualquier rol mid-trabajo con duda cross-dominio) puede **convocar reunión flat parallel multi-rol** (6 asesores en paralelo desde su ángulo dimensional) on-demand sobre cualquier propuesta o candidata, de modo que el scope-scan multi-rol no es ritual ceremonioso de checkpoint sino herramienta disponible cuando hace falta — materializa Cagan principio 2 (give-and-take) en formato slash command."*
- **Parent**: cap-04-verificacion-multirol-cruzada
- **also-relates-to**: cap-02-multirol-agentes-homologos (los 6 asesores existen por CAP-B)
- **depends-on**: feature-008 (identidad de cada asesor cargada), feature-012 (modality subagente decidida)
- **depends-on-harness**: Task tool (mecanismo de invocación) + paralelización via múltiples tool_use blocks en un solo mensaje
- **related-adrs**: ADR-latente-009 (tres checkpoints uniformes), ADR-latente-001 (harness primario)
- **dimensions-affected**: [product, technical]
- **AC preview**: slash `/scope-scan` documentado en CLAUDE.md raíz sección "Slash commands"; aplicado en WAs cuando se draftan (WA-002, WA-004); flat parallel = un único mensaje del orquestador con múltiples tool_use; cada asesor devuelve `scope-scan-output` estructurado.

#### feature-019 · Slash `/verify` + algoritmo declarativo `verifiers = {custodian(d)}`
- **JTBD operador**: *"El operador humano puede ejecutar `/verify` al cierre de cualquier WA y el operador agente PO **deriva mecánicamente** la lista de verificadores aplicando el algoritmo `verifiers = {custodian(d) : d ∈ wa.dimensions-affected}`, invoca verificadores en paralelo, consolida hallazgos, aplica `on-close` transitions + archiva el WA, de modo que el sign-off es algoritmo declarativo no juicio caso-a-caso del PO."*
- **Parent**: cap-04-verificacion-multirol-cruzada
- **also-relates-to**: cap-01-grafo-declarativo-persistente (dimensions.md como ground truth del mapping dimensión → custodio) + cap-03-working-agreements-sdlc (consume on-close del WA)
- **depends-on**: feature-009 (catálogo roles + custodios), feature-017 (on-close transitions), feature-018 (mecanismo invocación verificadores en paralelo)
- **depends-on-harness**: Task tool
- **related-adrs**: ADR-latente-010 (algoritmo declarativo verifiers)
- **dimensions-affected**: [product, quality]
- **AC preview**: slash `/verify` documentado; algoritmo `verifiers = {custodian(d)}` declarado en agent file PO Modo 3; closure-criteria comprobado mecánicamente antes de invocar verificadores; verificable vía inspección de WAs archivados (WA-002, WA-003) — sus verified-by listan los custodios derivados del algoritmo.

#### feature-020 · Tres checkpoints uniformes del WA lifecycle (discovery + step + sign-off)
- **JTBD operador**: *"El motor SEM-IA aplica scope-scan flat parallel multi-rol en **tres puntos uniformes** del lifecycle de cualquier WA — (1) discovery review al crear el WA, (2) step checkpoint post-step, (3) sign-off al `/verify` — de modo que el modelo de verificación es predecible (un operador sabe siempre cuándo le toca aportar), uniforme entre tipos de outcome, y no rito caso-a-caso."*
- **Parent**: cap-04-verificacion-multirol-cruzada
- **also-relates-to**: cap-03-working-agreements-sdlc (los checkpoints viven en el WA lifecycle)
- **depends-on**: feature-018 (scope-scan), feature-019 (verify), feature-015 (Progreso entries marcan post-step)
- **depends-on-harness**: —
- **related-adrs**: ADR-latente-009 (tres checkpoints uniformes como mecanismo arquitectónico)
- **dimensions-affected**: [product, quality]
- **AC preview**: tres checkpoints documentados en CLAUDE.md raíz sección "Tres reuniones del lifecycle del WA"; aplicados visibles en WA-002 + WA-003 + WA-004 (cada uno tiene los 3 momentos identificables); verificable vía inspección de las secciones Progreso de WAs archivados.

#### feature-021 · `verification-matrix.md` como guía orientativa de dimensiones × operaciones
- **JTBD operador**: *"El operador agente orquestador, al hacer scope-scan, puede **recordar mnemotécnicamente** qué dimensiones típicamente toca cada tipo de operación consultando una matriz orientativa (no prescriptiva), de modo que detectar dimensiones-detected es ayuda + criterio bibliográfico, no improvisación pura."*
- **Parent**: cap-04-verificacion-multirol-cruzada
- **also-relates-to**: cap-01-grafo-declarativo-persistente (la matriz es ground truth conceptual del grafo)
- **depends-on**: feature-009 (catálogo roles), feature-013 (catálogo outcome-types)
- **depends-on-harness**: —
- **related-adrs**: —
- **dimensions-affected**: [product, quality]
- **AC preview**: `vault/shared/governance/verification-matrix.md` existe; declara matriz dimensiones × operaciones como guía orientativa (no rígida); diferenciada de `workflows.md` (este último es forward-looking de steps; matriz es backward-looking mnemotécnica).

#### feature-022 · Give-and-take mid-step (Cagan principio 2) vía subagentes a otros dominios
- **JTBD operador**: *"El operador agente activo en un step puede **invocar subagentes a otros dominios mid-trabajo** cuando emerge duda relevante a otro dominio, de modo que la discovery es colaborativa-paralela (no waterfall secuencial) y los gaps cross-dominio se detectan temprano dentro del step en vez de tarde en post-step scope-scan o /verify."*
- **Parent**: cap-04-verificacion-multirol-cruzada
- **also-relates-to**: cap-02-multirol-agentes-homologos (subagentes existen por CAP-B)
- **depends-on**: feature-012 (criterio subagente vs sesión-dedicada)
- **depends-on-harness**: Task tool
- **related-adrs**: ADR-latente-001 (harness primario)
- **dimensions-affected**: [product, quality]
- **AC preview**: give-and-take documentado en CLAUDE.md raíz sección "Patrón colaborativo dentro del WA" + en agent files (cada uno indica cuándo invocar a otros mid-step); ejemplos canónicos documentados (PO durante decomposition invoca Designer/Architect/Security/Business; Architect escribiendo ADR invoca Security/Business; etc.).

#### feature-023 · Filtro PO al consolidar scope-scan (4 categorías Cagan) — Gap 6 formalizado
- **JTBD operador**: *"El operador agente PO, al consolidar outputs de scope-scan multi-rol, puede **filtrar cada flag aplicando criterio propio** clasificándolo en 4 categorías Cagan (acepto y aplico yo · descarto con razón · difiero a WA futuro · requiere decisión humana real), de modo que el humano recibe DECISIONES PO + preguntas filtradas (no agregación bruta) y se previene el patrón 'PO contaminado' de operar mecánicamente sin aplicación de criterio."*
- **Parent**: cap-04-verificacion-multirol-cruzada
- **also-relates-to**: cap-02-multirol-agentes-homologos (es comportamiento del rol PO específicamente)
- **depends-on**: feature-018 (scope-scan provee inputs a filtrar), feature-008 (identidad PO con criterio bibliográfico)
- **depends-on-harness**: —
- **related-adrs**: —
- **dimensions-affected**: [product, quality]
- **AC preview**: paso 6b en agent file PO Modo 1 documenta las 4 categorías + anclaje Cagan (*Inspired* — *"strong product manager: opinions are informed by data but decisions are own"*); aplicado en WA-002 + WA-003 + WA-004 visibles en sus secciones de scope-scan consolidado; verificable vía inspección de WAs archivados.

#### feature-024 · Contrato `filesystem-changes` para subagentes con autoridad de edición (Gap 9 formalizado)
- **JTBD operador**: *"Cuando un subagente con autoridad de edición cierra su step, **DEBE incluir en su output un bloque estructurado `filesystem-changes`** (formato canónico: path absoluto + operation + locations con line ranges + rationale por cambio), de modo que el orquestador puede registrarlo en Progreso del WA y el humano puede auditar futuro qué cambió cada subagente en step Y del WA Z con precisión técnica (no solo resumen narrativo)."*
- **Parent**: cap-04-verificacion-multirol-cruzada
- **also-relates-to**: cap-02-multirol-agentes-homologos (subagentes via Task tool) + cap-03-working-agreements-sdlc (Progreso entries registran el filesystem-changes)
- **depends-on**: feature-015 (Progreso entries), feature-022 (subagentes invocados)
- **depends-on-harness**: Task tool
- **related-adrs**: ADR latente "Subagentes con autoridad de edición + trazabilidad" (recomendado afloramiento explícito por Security step-6 del WA-004)
- **dimensions-affected**: [product, technical, quality, security]
- **AC preview**: contrato `filesystem-changes` documentado en CLAUDE.md raíz sección "Contrato de trazabilidad `filesystem-changes`"; protocolo del PO al recibir output en agent file PO Modo 2 "Al completar tu step" paso 4a; aplicado en este WA-004 (steps 3-7 declaran requisito en su `purpose`); verificable vía inspección de Progreso entries que registren bloques YAML literales.

---

#### Sub-anexo Grupo 2 — Cobertura piezas-bootstrap CAP-C + CAP-D

| Pieza del bootstrap (Job 3 + 4) | Feature owner | Cobertura |
|---|---|---|
| `vault/shared/governance/workflows.md` (14 templates) | feature-013 | Total |
| Estructura inline WA (frontmatter + cuerpo) | feature-014 | Total |
| Slash `/wa` (mecanismo lectura) | **CAP-F (Grupo 3)** | Aplazado |
| Progreso entries + protocolo handoff | feature-015 | Total |
| Protocolo de pivot WA mid-flight (Gap 4) | feature-016 | Total |
| Regla de autocontención del WA (Gap 7) | feature-014 (AC: cuerpo autocontenido) | Total |
| Estados canónicos del WA | feature-016 (extensión `aborted` y `aborted-reference`) + heredado de feature-004 CAP-A | Total |
| Closure-criteria + on-close | feature-017 | Total |
| Slash `/scope-scan` | feature-018 | Total |
| Slash `/verify` + algoritmo verifiers | feature-019 | Total |
| Tres checkpoints uniformes del WA lifecycle | feature-020 | Total |
| `vault/shared/governance/verification-matrix.md` | feature-021 | Total |
| Give-and-take mid-step (Cagan principio 2) | feature-022 | Total |
| Filtro PO 4 categorías Cagan (Gap 6) | feature-023 | Total |
| Contrato `filesystem-changes` (Gap 9) | feature-024 | Total |
| Briefing por step (Gap 10, 4 bloques canónicos) | feature-014 (AC: briefing es sección del cuerpo del WA) | Total |
| Skills de verificación (`*-viability-review`, `coherence-evaluation`, `coupling-detection`, `threat-modeling`, `*-quality-check`) | **CAP-E (Grupo 3)** ownership — CAP-D declara `depends-on` | Aplazado |

Grupo 2 total: **12 features** (feature-013..feature-024). 2 piezas aplazadas a Grupo 3 (CAP-E + CAP-F) por decisión de ownership PO. 0 piezas sin cobertura final.

---

### CAP-E · Anclaje bibliográfico auditable mediante skills empaquetadas y biblioteca canónica

**Piezas reales del bootstrap (de Job 5, WA-002 discovery doc):**
- 18 notas bibliográficas en `vault/architect/research/library/` (Cagan, Sinek, Rumelt, Doerr, Doran, Torres, Christensen, Patton, Cohn, Adzic, Bass, Ford, Nygard, Martin, Ousterhout, Anthropic skills+subagents)
- `vault/architect/research/library/INDEX.md` (índice de bibliografía)
- 14 skills construidas en `.claude/skills/<rol>/<skill>/SKILL.md` + `design.md`:
  - **PO estratégicas (4)**: vision-quality-check, goal-quality-check, capability-derivation, capability-quality-check
  - **PO operativas (3)**: feature-decomposition, spec-writing, feature-quality-check
  - **Architect (5)**: adr-writing, capability-viability-review, coherence-evaluation, coupling-detection, feature-viability-review
  - **Security-officer (1)**: threat-modeling
  - **Shared (1)**: graph-cross-link-declaration → **ownership CAP-A** (feature-006), no se duplica aquí
- `.claude/skills/_pending-later.md` (10+ skills documentadas como pendientes con bibliografía identificada)
- Carga perezosa nativa de Agent Skills (Claude Code) — **dependencia harness, NO feature propia**

**Features candidatas:**

#### feature-025 · Biblioteca bibliográfica curada (18 notas + INDEX) en `vault/architect/research/library/`
- **JTBD operador**: *"El operador agente (cualquier rol aplicando una skill) puede **citar fuente bibliográfica auditable** (autor + año + obra + capítulo si aplica) consultando una biblioteca curada de 18 notas con índice navegable, de modo que cada decisión significativa del sistema queda anclada a corpus profesional auditado y no improvisación."*
- **Parent**: cap-05-anclaje-bibliografico-skills
- **also-relates-to**: cap-10-articulacion-publica (la library es doc público auditable; evaluador académico la inspecciona) + cap-04-verificacion-multirol-cruzada (las skills de verificación citan library)
- **depends-on**: feature-002 (frontmatter por nota), feature-003 (wikilinks entre notas + nodos)
- **depends-on-harness**: —
- **related-adrs**: ADR-latente-005 (skills como unidad de empaquetado bibliográfico)
- **dimensions-affected**: [product, quality, business, security]  # business latente: atribución académica para evaluador GISF/TFM. security: vector T+R (Tampering + Repudiation) — citas bibliográficas inventadas/fabricated sin mecanismo de verificación automatizado; integridad académica core (Security flag post-step CAP-05 T+R)
- **AC preview**: `vault/architect/research/library/` contiene 18 archivos con frontmatter `type: research, status: active`; `INDEX.md` indexa los 18 con (autor, año, obra, contextos aplicables); cada nota cita corpus original con páginas si aplica; verificable vía inspección.

#### feature-026 · SKILL.md + design.md como unidad de empaquetado bibliográfico con carga perezosa
- **JTBD operador**: *"El operador agente puede invocar happy-paths bibliográficos auditables (heurísticas auditadas por autor citado) a través de **skills empaquetadas como SKILL.md operativo + design.md referencia**, cargadas perezosamente por Claude Code cuando el contexto matchea su `description`, de modo que las skills son aplicación nativa transparente del operador sin que tenga que invocarlas explícitamente."*
- **Parent**: cap-05-anclaje-bibliografico-skills
- **also-relates-to**: cap-02-multirol-agentes-homologos (las skills viven en `.claude/skills/<rol>/` mapeadas a roles)
- **depends-on**: feature-025 (citas bibliográficas de la library)
- **depends-on-harness**: carga perezosa nativa de Agent Skills (Claude Code)
- **related-adrs**: ADR-latente-005 (Skills como unidad de empaquetado bibliográfico), ADR-latente-001 (harness primario que provee carga perezosa)
- **dimensions-affected**: [product, technical, quality]
- **AC preview**: `.claude/skills/<rol>/<skill>/SKILL.md` existe (14 skills construidas); convención SKILL.md operativo + design.md referencia documentada; carga perezosa nativa verificada via descripción matching contexto; verificable vía inspección de árbol de skills + ejecución.

#### feature-027 · Catálogo de skills PO estratégicas (vision/goal/capability quality + derivation)
- **JTBD operador**: *"El operador agente PO en lado estratégico puede aplicar happy-paths bibliográficos auditados al evaluar visión (7 tests Cagan + Sinek + Rumelt + JTBD), evaluar goal (6 tests Doerr OKR + Doran SMART), derivar capabilities desde goal (Torres OST + Rumelt + JTBD) y evaluar capability (6 tests Rumelt + Torres + Cagan), de modo que las decisiones estratégicas no son improvisación del PO sino aplicación de skills empaquetadas con bibliografía citada."*
- **Parent**: cap-05-anclaje-bibliografico-skills
- **also-relates-to**: cap-02-multirol-agentes-homologos (las skills son del rol PO)
- **depends-on**: feature-026 (SKILL.md como unidad), feature-025 (citas library)
- **depends-on-harness**: carga perezosa nativa Agent Skills
- **related-adrs**: ADR-latente-005
- **dimensions-affected**: [product, quality]
- **AC preview**: 4 SKILL.md en `.claude/skills/product-owner/strategy/`: vision-quality-check, goal-quality-check, capability-derivation, capability-quality-check; cada uno cita autores aplicables; aplicados visibles en WA-001 (abortado), WA-002 (capability-derivation + capability-quality-check) archivados.

#### feature-028 · Catálogo de skills PO operativas (feature-decomposition + spec-writing + feature-quality-check)
- **JTBD operador**: *"El operador agente PO en lado operativo puede aplicar happy-paths bibliográficos auditados al descomponer capability en features (Patton story map + Cohn INVEST + JTBD), escribir spec Gherkin formal (Adzic SbE) y validar feature antes de cerrar (7 tests INVEST + cobertura AC + coherencia capability), de modo que el design de features no es improvisación sino aplicación de skills empaquetadas con bibliografía."*
- **Parent**: cap-05-anclaje-bibliografico-skills
- **also-relates-to**: cap-02-multirol-agentes-homologos (skills del rol PO) + cap-03-working-agreements-sdlc (aplicadas durante WAs `feature-design`)
- **depends-on**: feature-026, feature-025
- **depends-on-harness**: carga perezosa
- **related-adrs**: ADR-latente-005
- **dimensions-affected**: [product, quality]
- **AC preview**: 3 SKILL.md en `.claude/skills/product-owner/`: feature-decomposition, spec-writing, feature-quality-check; cada uno cita autores; documentadas en agent file PO sección "Skills cargadas nativamente — Operativas (lado design)".

#### feature-029 · Catálogo de skills Architect (adr-writing + viability reviews + coherence + coupling)
- **JTBD operador**: *"El operador agente Architect puede aplicar happy-paths bibliográficos auditados al escribir ADR (formato Nygard: Context + Decision + Consequences + Alternatives), revisar viability de capability/feature (Bass QAs + tactics + tradeoffs + Ford fitness functions), evaluar coherencia con grafo existente (Ford + Martin Dependency Rule) y detectar coupling (Ford appropriate coupling vs accidental), de modo que la dimensión technical opera con criterio anclado y no opinión técnica subjetiva."*
- **Parent**: cap-05-anclaje-bibliografico-skills
- **also-relates-to**: cap-04-verificacion-multirol-cruzada (CAP-D `depends-on` estas skills — son su mecanismo de verificación técnica)
- **depends-on**: feature-026, feature-025
- **depends-on-harness**: carga perezosa
- **related-adrs**: ADR-latente-005
- **dimensions-affected**: [product, technical, quality]
- **AC preview**: 5 SKILL.md en `.claude/skills/architect/`: adr-writing, capability-viability-review, coherence-evaluation, coupling-detection, feature-viability-review; cada uno cita autores aplicables; aplicado en WA-004 step-3 (coupling-detection + coherence-evaluation).

#### feature-030 · Catálogo de skill Security (threat-modeling) + pendientes Security identificadas
- **JTBD operador**: *"El operador agente Security puede aplicar happy-path bibliográfico auditado al hacer threat-modeling formal (STRIDE + Shostack) sobre feature consumida, produciendo AC-S* trazables a tests, de modo que la dimensión security no es check ceremonioso sino verificación anclada Shostack + OWASP-LLM-Top-10."*
- **Parent**: cap-05-anclaje-bibliografico-skills
- **also-relates-to**: cap-04-verificacion-multirol-cruzada (CAP-D `depends-on` skill threat-modeling como mecanismo de verificación security)
- **depends-on**: feature-026, feature-025
- **depends-on-harness**: carga perezosa
- **related-adrs**: ADR-latente-005
- **dimensions-affected**: [product, quality, security]
- **AC preview**: 1 SKILL.md en `.claude/skills/security-officer/threat-modeling/`; cita Shostack + OWASP-LLM-Top-10; aplicado en este WA-004 step-6.

#### feature-031 · `.claude/skills/_pending-later.md` — skills pendientes documentadas con bibliografía
- **JTBD operador**: *"El operador (humano + agente) puede consultar **qué skills están planificadas pero no construidas** (≥10 documentadas) con su bibliografía ya identificada, de modo que el roadmap de skills es transparente y futuras adopciones del framework heredan el corpus pendiente con anclaje bibliográfico declarado."*
- **Parent**: cap-05-anclaje-bibliografico-skills
- **also-relates-to**: cap-10-articulacion-publica (visibilidad pública de skills pendientes refuerza articulación del framework)
- **depends-on**: —
- **depends-on-harness**: —
- **related-adrs**: ADR-latente-005
- **dimensions-affected**: [product, quality]
- **AC preview**: `.claude/skills/_pending-later.md` existe con 10+ skills pendientes documentadas con bibliografía identificada (autor + obra) por skill; estructura uniforme verificable vía inspección.

---

### CAP-F · Visibilidad operativa del estado y progreso del proyecto

**Piezas reales del bootstrap (de Job 6, WA-002 discovery doc):**
- Slash `/status` — snapshot del proyecto (WAs por track Dual, backlog, subgrafo, features por status, ADRs)
- Slash `/wa` — detalle del WA activo (aplazado de CAP-C Grupo 2 — ownership decisión PO: parent CAP-F)
- Slash `/sessions` — modos de trabajo + sesiones dedicadas + atajos npm
- Ritual de inicio del PO declarado en agent file PO Modo 1 paso 1 + wrapper `vault/product-owner/CLAUDE.md`
- Progreso entries en cada WA (ya cubierto por feature-015 CAP-C — also-relates-to CAP-F declarado)
- Dual Track Discovery/Delivery explicitado en CLAUDE.md raíz + workflows.md

**Features candidatas:**

#### feature-032 · Slash `/status` con panorámica del proyecto agrupada por track Dual + backlog + ADRs
- **JTBD operador**: *"El operador humano puede ejecutar `/status` desde cualquier sesión y recibir **snapshot del estado del proyecto entero** — WAs activos por track (Discovery/Delivery/Operations/Meta vía Dual Track Cagan/Patton), backlog emergente, subgrafo estratégico (visión + goals + capabilities), features por status, ADRs por status — de modo que valida estado conocido (Nielsen #1 visibility of system status) en vez de re-explorar el vault y absorbe coste de revisión (goal-3)."*
- **Parent**: cap-06-visibilidad-operativa
- **also-relates-to**: cap-01-grafo-declarativo-persistente (el snapshot es query sobre el grafo) + cap-03-working-agreements-sdlc (agrupa WAs por fase SDLC)
- **depends-on**: feature-005 (backlog query), feature-004 (estados canónicos)
- **depends-on-harness**: —
- **related-adrs**: ADR-latente-008 (backlog query emergente)
- **dimensions-affected**: [product, usability, security]  # Nielsen #1. security: vector I (Information disclosure) — /status agrega contenido del vault completo; secrets accidentalmente commitados en frontmatter o Progreso entries quedan expuestos en output agregado (Security flag post-step CAP-06 I)
- **AC preview**: slash `/status` documentado en CLAUDE.md raíz; output incluye secciones (Estrategia, Producto, Arquitectura, WAs activos, Backlog, Audits); verificable vía ejecución `/status` en sesión cualquiera.

#### feature-033 · Slash `/wa` con detalle del WA activo (steps + status + progreso)
- **JTBD operador**: *"El operador humano puede ejecutar `/wa` desde una sesión y recibir **detalle del Working Agreement activo en el contexto** (steps con status, Progreso entries, scope, closure-criteria, próximo step pending), de modo que comprende dónde está en el ciclo actual sin abrir el archivo .md manualmente y minimiza error recovery cognitive (Nielsen #9)."*
- **Parent**: cap-06-visibilidad-operativa
- **also-relates-to**: cap-03-working-agreements-sdlc (lee la estructura del WA — feature-014)
- **depends-on**: feature-014 (estructura del WA), feature-015 (Progreso entries)
- **depends-on-harness**: —
- **related-adrs**: —
- **dimensions-affected**: [product, usability]  # Nielsen #1 + #9
- **AC preview**: slash `/wa` documentado en CLAUDE.md raíz; output incluye steps + status + sección Progreso resumida + próximo step pending; verificable vía ejecución `/wa` desde sesión con WA activo (ej. WA-004 actual).

#### feature-034 · Slash `/sessions` con catálogo de modos de trabajo + sesiones dedicadas + atajos npm
- **JTBD operador**: *"El operador humano puede ejecutar `/sessions` y recibir **catálogo legible de los modos de trabajo disponibles** (8 roles × sus atajos npm + cuándo abrir cada uno + qué se cubre en cada uno), de modo que reduce recall cognitive (Nielsen #6) y acelera el cambio entre roles del flujo multi-rol."*
- **Parent**: cap-06-visibilidad-operativa
- **also-relates-to**: cap-02-multirol-agentes-homologos (los modos existen por CAP-B)
- **depends-on**: feature-009 (catálogo roles), feature-010 (entry-points npm)
- **depends-on-harness**: —
- **related-adrs**: —
- **dimensions-affected**: [product, usability]  # Nielsen #6 recognition over recall
- **AC preview**: slash `/sessions` documentado en CLAUDE.md raíz; output incluye 8 roles × atajos + descripción cuándo abrir cada uno; verificable vía ejecución.

#### feature-035 · Ritual de inicio del PO con panorámica al arrancar sesión
- **JTBD operador**: *"El operador agente PO, al arrancar su sesión (Modo 1 paso 1), ejecuta **ritual de inicio** leyendo strategy/, sessions/active/, specs/, adrs/, governance/, y presenta panorámica al humano (visión + goals + capabilities + WAs activos + backlog + audits) antes de pedir propuesta, de modo que la conversación arranca con contexto compartido (humano sabe qué hay; PO sabe qué hay) y se previene el patrón 'agente improvisa sobre vault vacío en su cabeza'."*
- **Parent**: cap-06-visibilidad-operativa
- **also-relates-to**: cap-07-inception-greenfield (en greenfield el ritual de inicio detecta vault vacío y propone cadena de WAs)
- **depends-on**: feature-008 (identidad PO con Modo 1 declarado), feature-011 (CLAUDE.md raíz)
- **depends-on-harness**: —
- **related-adrs**: —
- **dimensions-affected**: [product, usability]  # Nielsen #1 + Norman conceptual model transfer
- **AC preview**: ritual de inicio documentado en agent file PO Modo 1 paso 1 + en wrapper `vault/product-owner/CLAUDE.md`; presentación canónica de panorámica documentada; verificable vía sesión `npm run sem` con vault no-vacío — el PO presenta panorámica antes de pedir propuesta.

#### feature-036 · Orientación al operador sobre qué rol abrir ante ambigüedad
- **JTBD operador**: *"El operador humano que duda entre `npm run sem` vs `npm run arch` vs otro rol puede **consultar criterio de delegación expresado en lenguaje de decisión del operador** (CLAUDE.md raíz + tabla de delegación del PO Modo 1 paso 4 + /sessions output), de modo que sabe qué sesión abrir sin leer páginas de docs y minimiza ambigüedad cognitive (Nielsen #6 + #7) — concretiza Designer flag latente del scope-scan."*
- **Parent**: cap-06-visibilidad-operativa
- **also-relates-to**: cap-02-multirol-agentes-homologos (los 8 roles existen por CAP-B; este JTBD es del operador sabiendo qué hacer = visibilidad)
- **depends-on**: feature-009 (catálogo roles), feature-034 (slash sessions)
- **depends-on-harness**: —
- **related-adrs**: —
- **dimensions-affected**: [product, usability]  # Nielsen #6 recognition over recall + #7 flexibility + efficiency
- **AC preview**: CLAUDE.md raíz incluye sección "Cómo arrancar trabajo" con criterio "si dudas qué sesión arrancar"; agent file PO Modo 1 paso 4 declara criterio de delegación; /sessions output incluye descripción de cuándo invocar cada rol; **AC error-state**: si el operador ya está en sesión equivocada, el rol activo detecta scope ajeno y comunica "esta no es decisión de mi dominio; sal y abre `npm run <rol-correcto>`" (Nielsen #9 error recovery — Designer flag post-step).

#### feature-037 · Dual Track Discovery/Delivery visible en `/status` (Cagan/Patton)
- **JTBD operador**: *"El operador humano puede ver en `/status` el estado del **Dual Track Discovery/Delivery** (Cagan/Patton): cuántos WAs en cada fase, tamaño del backlog (puente persistente entre tracks), ratio Discovery vs Delivery, de modo que detecta antipatrones (solo Discovery = parálisis por análisis; solo Delivery = waterfall disfrazado) sin forzar ratio."*
- **Parent**: cap-06-visibilidad-operativa
- **also-relates-to**: cap-03-working-agreements-sdlc (los WAs viven por fase SDLC) + cap-01-grafo-declarativo-persistente (backlog como query emergente)
- **depends-on**: feature-032 (slash /status), feature-005 (backlog query)
- **depends-on-harness**: —
- **related-adrs**: —
- **dimensions-affected**: [product, usability]  # Nielsen #1 + Cagan dual track explícito
- **AC preview**: documentación Dual Track en CLAUDE.md raíz sección "Dual Track (Cagan/Patton)" + en `workflows.md` sección "Dual Track"; `/status` agrupa WAs por track (Discovery/Delivery/Operations/Meta); verificable vía ejecución `/status`.

---

#### Sub-anexo Grupo 3 — Cobertura piezas-bootstrap CAP-E + CAP-F

| Pieza del bootstrap (Job 5 + 6) | Feature owner | Cobertura |
|---|---|---|
| 18 notas bibliográficas en library/ | feature-025 | Total |
| INDEX.md de la library | feature-025 (AC explícito) | Total |
| Skill `vision-quality-check` | feature-027 | Total |
| Skill `goal-quality-check` | feature-027 | Total |
| Skill `capability-derivation` | feature-027 | Total |
| Skill `capability-quality-check` | feature-027 | Total |
| Skill `feature-decomposition` | feature-028 | Total |
| Skill `spec-writing` | feature-028 | Total |
| Skill `feature-quality-check` | feature-028 | Total |
| Skill `adr-writing` | feature-029 | Total |
| Skill `capability-viability-review` | feature-029 | Total |
| Skill `coherence-evaluation` | feature-029 | Total |
| Skill `coupling-detection` | feature-029 | Total |
| Skill `feature-viability-review` | feature-029 | Total |
| Skill `threat-modeling` | feature-030 | Total |
| Skill compartida `graph-cross-link-declaration` | feature-006 (CAP-A) + also-relates-to declarado en feature-026 | Total via cross-link |
| Convención SKILL.md + design.md + carga perezosa | feature-026 | Total |
| `_pending-later.md` (10+ skills pendientes) | feature-031 | Total |
| Carga perezosa nativa Claude Code | **NO es feature propia** (depends-on-harness declarado en feature-026..030) | n/a |
| Slash `/status` | feature-032 | Total |
| Slash `/wa` | feature-033 | Total |
| Slash `/sessions` | feature-034 | Total |
| Ritual de inicio del PO | feature-035 | Total |
| Progreso entries (visibilidad) | feature-015 (CAP-C, ownership) + also-relates-to declarado | Total via cross-link |
| Dual Track explicitado | feature-037 | Total |
| Orientación qué rol abrir (Designer flag) | feature-036 | Total |

Grupo 3 total: **13 features** (feature-025..feature-037). 1 pieza heredada de Grupo 1 (feature-006) + 1 pieza heredada de Grupo 2 (feature-015) cubren cross-link. 0 piezas sin cobertura final.

---

### CAP-G · Inception greenfield protocol-compliant desde vault vacío

**Piezas reales del bootstrap (de Job 7, WA-002 discovery doc):**
- PO Modo 1 (Entrada al sistema) declarado en `.claude/agents/product-owner.md` con protocolo de 10 pasos
- Cadena de WAs por gaps detectados declarada en `vault/shared/governance/workflows.md` (`vision-creation → goal-definition × N → capability-creation × M → feature-design × K`)
- Templates uniformes greenfield/maduro — los mismos `workflows.md` sirven en ambas fases
- `vault/<rol>/CLAUDE.md` wrappers + atajos npm — entrada directa por dominio si propuesta no es de PO (ya cubierto por feature-010 + feature-011 en CAP-B, ritual de inicio PO ya cubierto por feature-035 en CAP-F)

**Features candidatas:**

#### feature-038 · PO Modo 1 (Entrada al sistema) con protocolo de 10 pasos
- **JTBD operador**: *"El operador agente PO, al recibir propuesta humana al arrancar sesión, puede **conducir el flujo completo de entrada al sistema** aplicando un protocolo declarativo de 10 pasos (ritual de inicio → escucha → clasifica outcome-type → decide conduzco/delego → convoca scope-scan → consolida + Filtro PO → carga template → drafta WA → presenta + confirma → indica próximo paso), de modo que la entrada por defecto al sistema SEM-IA es uniforme + auditable + bibliográficamente anclada (no improvisación caso-a-caso del PO)."*
- **Parent**: cap-07-inception-greenfield
- **also-relates-to**: cap-03-working-agreements-sdlc (Modo 1 culmina en draft de WA) + cap-04-verificacion-multirol-cruzada (paso 5 convoca scope-scan) + cap-06-visibilidad-operativa (paso 1 ritual inicio presenta panorámica)
- **depends-on**: feature-008 (identidad PO), feature-035 (ritual de inicio), feature-013 (templates), feature-018 (scope-scan), feature-023 (Filtro PO)
- **depends-on-harness**: —
- **related-adrs**: —
- **dimensions-affected**: [product, technical, usability]  # Norman: el procedimiento del PO es modelo conceptual transferible al humano
- **AC preview**: protocolo Modo 1 documentado en `.claude/agents/product-owner.md` sección "Protocolo del Modo 1 — Entrada al sistema" con los 10 pasos declarados; ejecutado visible en WA-001 (aborted), WA-002, WA-003, WA-004 (este — en curso); verificable vía sesión PO con vault no-vacío.

#### feature-039 · Cadena de WAs por gaps detectados (vision → goals → capabilities → features)
- **JTBD operador**: *"El operador agente PO, al detectar gaps upstream durante scope-scan (no hay capability padre, no hay goal padre, no hay visión), puede **proponer al humano una cadena ordenada top-down de WAs** (`vision-creation → goal-definition × N → capability-creation × M → feature-design × K`) usando los templates existentes (no template ad-hoc para 'cadena'), de modo que el grafo emerge orgánicamente desde gap detection y la inception greenfield converge con dogfooding maduro bajo los mismos workflows."*
- **Parent**: cap-07-inception-greenfield
- **also-relates-to**: cap-03-working-agreements-sdlc (la cadena consume templates existentes)
- **depends-on**: feature-013 (templates de discovery), feature-038 (PO Modo 1 detecta gaps en paso 6)
- **depends-on-harness**: —
- **related-adrs**: —
- **dimensions-affected**: [product, technical]
- **AC preview**: sección "Cadena de WAs por gaps detectados (única vía de entrada)" documentada en `workflows.md`; 3 formas del patrón documentadas (cadena directa greenfield · cadena corta proyecto-maduro · modo arbitraje cross-cutting); aplicado en este proyecto (cadena vision → goals × 7 → capabilities × 10 → features × 46 visible en historia de WAs archivados).

#### feature-040 · Templates uniformes greenfield/maduro (convergencia bajo `workflows.md`)
- **JTBD operador**: *"El operador (humano + agente) puede operar la fase inception greenfield con **los mismos workflow templates** que operan dogfooding maduro y mantenimiento, de modo que no hay protocolos paralelos ni atajos ad-hoc ni divergencia greenfield/maduro — propiedad arquitectónica de uniformidad que sostiene CAP-G."*
- **Parent**: cap-07-inception-greenfield
- **also-relates-to**: cap-03-working-agreements-sdlc (los templates son los mismos de la fase SDLC)
- **depends-on**: feature-013 (catálogo templates)
- **depends-on-harness**: —
- **related-adrs**: ADR-latente-007 (fases SDLC redefinibles por adopter, propiedad de uniformidad implícita)
- **dimensions-affected**: [product, technical]
- **AC preview**: declarado en CAP-G capability file ("Convergencia inception ↔ dogfooding ↔ mantenimiento bajo los mismos templates indexados por fase SDLC"); verificable vía comparación: los WAs `capability-creation` mode reverse-engineering (WA-002) usan el mismo template que un WA `capability-creation` mode single futuro en proyecto maduro.

---

### CAP-J · Articulación pública del framework para audiencias externas

**Piezas reales del bootstrap (de Job 10, WA-002 discovery doc):**
- `README.md` raíz (65 KB) — onboarding completo del framework
- `CLAUDE.md` raíz (ya cubierto por feature-011 en CAP-B — guía estática + entry-point)
- `vault/architect/research/bootstrap-summary.md` (historia + 16 decisiones + 8 lecciones del bootstrap)
- `vault/shared/governance/*.md` (5 docs canónicos: dimensions, role-catalog, workflows, verification-matrix, repo-structure — todos ya cubiertos por features individuales en CAP-A/B/C/D)
- `vault/architect/research/library/` (ya cubierto por feature-025 en CAP-E)
- `LICENSE` Apache 2.0
- `propuesta-prefacio.pdf` — propuesta inicial archivada

**Features aplazadas que entran en este Grupo (decisión humana confirmada):**
- Glosario público de términos SEM-IA (Designer flag D2 + Business GTM Moore)
- Ruta de lectura diferenciada por audiencia técnica vs académica vs adoptante (Business GTM)
- Atribución bibliográfica explícita en docs públicos (Business flag latente sobre CAP-E)

**Features candidatas:**

#### feature-041 · README.md raíz como onboarding completo del framework
- **JTBD operador**: *"El operador humano newcomer (ingeniero adoptador, evaluador académico, miembro de comunidad técnica) puede **comprender el framework SEM-IA completo** leyendo `README.md` raíz: tesis filosófica, modelo conceptual (8 roles × 7 dimensiones × 14 templates × 5 fases SDLC), cómo arrancar, ejemplos canónicos, capabilities operant + planned, dual track, anclaje bibliográfico, posicionamiento Apache 2.0, de modo que decide informado si adoptar/evaluar/contribuir sin invocar al autor."*
- **Parent**: cap-10-articulacion-publica
- **also-relates-to**: cap-02-multirol-agentes-homologos (README documenta CLAUDE.md raíz + atajos npm + roles) + cap-01-grafo-declarativo-persistente (README documenta el grafo conceptual)
- **depends-on**: feature-011 (CLAUDE.md raíz como referencia)
- **depends-on-harness**: —
- **related-adrs**: —
- **dimensions-affected**: [product, usability, business, security]  # Nielsen #10 + GTM Moore. security: vector I+R (Information disclosure + Repudiation) — para framework cuyo vault es ground truth público auditable POR DISEÑO, README debe advertir adopters sobre blast radius si aplican SEM-IA en proyecto con datos sensibles (externalidad de la convención) (Security flag post-step CAP-10 I+R)
- **AC preview**: `/Users/pelayo/Developer/SEM-AI/README.md` existe (65 KB); secciones canónicas presentes (tesis, modelo conceptual, onboarding, capabilities, dual track, anclaje bibliográfico, license); verificable vía inspección.
- **Flag asociado**: README sin glosario ni ruta de lectura por audiencia → resuelto via feature-044 + feature-045.

#### feature-042 · Artefactos históricos curados (`bootstrap-summary.md` + `propuesta-prefacio.pdf`)
- **JTBD operador**: *"El operador humano (evaluador académico, contribuyente curioso, futuro mantenedor) puede **trazar la historia del bootstrap** del framework: las 16 decisiones clave + 8 lecciones aprendidas durante el bootstrap manual (`bootstrap-summary.md`) y la propuesta inicial del proyecto pre-bootstrap (`propuesta-prefacio.pdf`), de modo que comprende el porqué de las decisiones arquitectónicas + la trayectoria de razonamiento sin entrevistar al autor."*
- **Parent**: cap-10-articulacion-publica
- **also-relates-to**: cap-05-anclaje-bibliografico-skills (bootstrap-summary cita autores aplicados en cada decisión)
- **depends-on**: feature-025 (library bibliográfica referenciada)
- **depends-on-harness**: —
- **related-adrs**: —
- **dimensions-affected**: [product, business]  # business: corpus auditable para evaluador académico
- **AC preview**: `vault/architect/research/bootstrap-summary.md` existe con 16 decisiones + 8 lecciones; `propuesta-prefacio.pdf` existe archivado en raíz del repo; verificable vía inspección.

#### feature-043 · LICENSE Apache 2.0 como decisión de licenciamiento del framework
- **JTBD operador**: *"El operador humano (adoptante, contribuyente, evaluador) puede **conocer las condiciones de uso, modificación y distribución** del framework via LICENSE Apache 2.0 (permite fork comercial + distribución comunitaria sin riesgo viral), de modo que toma decisiones de adopción sin ambigüedad legal."*
- **Parent**: cap-10-articulacion-publica
- **also-relates-to**: —
- **depends-on**: —
- **depends-on-harness**: —
- **related-adrs**: —
- **dimensions-affected**: [product, business]  # business: compliance licensing
- **AC preview**: `/Users/pelayo/Developer/SEM-AI/LICENSE` existe con texto canónico Apache 2.0; verificable vía inspección.
- **Flag-para-WA-futuro**: NOTICE file requerido solo si se distribuye paquete con modificaciones (CAP-H planned). Aparcado.

#### feature-044 · Glosario público de términos SEM-IA (Designer D2 + Business GTM)
- **JTBD operador**: *"El operador humano newcomer (especialmente evaluador académico no-practicante) puede **resolver la jerga interna** del framework (WA, scope-scan, vault, dimensions-affected, outcome-type, custodian, on-close, modality, etc.) consultando un glosario navegable referenciado desde README en la primera aparición de cada término, de modo que la barrera de entrada a la documentación pública baja significativamente y Nielsen #2 (match between system and real world) + #4 (consistency and standards) se cumplen."*
- **Parent**: cap-10-articulacion-publica
- **also-relates-to**: cap-02-multirol-agentes-homologos (incluye términos de roles + dimensiones) + cap-03-working-agreements-sdlc (incluye términos del WA)
- **depends-on**: feature-041 (README referenciado), feature-009 (catálogo roles), feature-013 (catálogo templates)
- **depends-on-harness**: —
- **related-adrs**: —
- **dimensions-affected**: [product, usability, business]  # Nielsen #2 + #4 + GTM cruzar el chasm Moore
- **AC preview**: glosario público existe (paths a definir en WA siguiente de feature-build); cubre ≥20 términos canónicos del framework con definición concisa + ejemplo + cross-link al doc que lo define; referenciado desde README en primera aparición; verificable vía inspección + grep desde README a glosario; **AC categorías mínimas cubiertas** (Designer flag post-step): glosario cubre ≥4 categorías de términos: (a) términos del frontmatter (type, parent, also-relates-to, dimensions-affected, status), (b) términos del WA lifecycle (outcome-type, on-close, closure-criteria, scope-allowed, modality), (c) términos de roles/dimensiones (custodian, Cagan-risk, role-catalog), (d) términos de slash commands (/status, /wa, /scope-scan, /verify, /sessions).
- **Decisión humana confirmada**: entra como feature formal en este WA (no como nota). **Scheduling confirmado** (Business flag post-step): el evaluador GISF verá README sin glosario materializado físicamente — decisión humana de aceptar conscientemente riesgo de no producir artefactos físicos antes del deadline 2026-05-25; feature queda formalizada para WA `feature-build` posterior.

#### feature-045 · Ruta de lectura diferenciada por audiencia (técnica / académica / adoptante)
- **JTBD operador**: *"El operador humano newcomer puede **identificar su ruta de lectura óptima** según audiencia (ingeniero adoptante quiere ver cómo adoptar; evaluador académico quiere ver tesis + bibliografía + dogfooding; contribuyente quiere ver arquitectura + governance), de modo que no necesita leer 65 KB de README linealmente — progressive disclosure (Nielsen + Cooper) materializado."*
- **Parent**: cap-10-articulacion-publica
- **also-relates-to**: cap-06-visibilidad-operativa (es feature de visibilidad pública del proyecto)
- **depends-on**: feature-041 (README), feature-044 (glosario referenciado en cada ruta)
- **depends-on-harness**: —
- **related-adrs**: —
- **dimensions-affected**: [product, usability, business]  # Nielsen #10 + Cooper + GTM Moore
- **AC preview**: sección "Cómo leer este repo" en README con ≥3 rutas diferenciadas (técnica / académica / adoptante); cada ruta enumera secciones del README + archivos del vault en orden recomendado; verificable vía inspección; **AC criterio "ruta completa"** (Designer flag post-step): cada ruta debe incluir mínimo (i) path de arranque (sección README o archivo del vault), (ii) ≥1 artefacto del vault (capability file, governance doc, library), (iii) ≥1 slash command relevante; sin completitud mínima la ruta no cumple progressive disclosure Nielsen #10 + Cooper.
- **Decisión humana confirmada**: entra como feature formal en este WA. **Scheduling confirmado** (Business flag post-step): mismo razonamiento que feature-044 — feature formalizada en este WA, artefacto físico (sección "Cómo leer este repo" en README) queda para WA `feature-build` posterior con aceptación consciente del riesgo de deadline GISF.

#### feature-046 · Atribución bibliográfica explícita en docs públicos (no solo library interna)
- **JTBD operador**: *"El operador humano (especialmente evaluador académico GISF/TFM) puede **ver atribución bibliográfica explícita en los docs públicos** que lee primero (README, CLAUDE.md, bootstrap-summary), no solo cuando bucea en `vault/architect/research/library/`, de modo que la credibilidad académica del framework es visible desde la primera lectura sin requerir exploración profunda."*
- **Parent**: cap-10-articulacion-publica
- **also-relates-to**: cap-05-anclaje-bibliografico-skills (la library es el corpus citado)
- **depends-on**: feature-025 (library), feature-041 (README), feature-042 (bootstrap-summary)
- **depends-on-harness**: —
- **related-adrs**: —
- **dimensions-affected**: [product, business]  # business: compliance académico para evaluador
- **AC preview**: README + CLAUDE.md + bootstrap-summary citan autores aplicados en formato académico breve (autor, año, obra); cada cita cruza wikilink a la nota correspondiente en library; verificable vía grep de `(autor, año)` patterns en docs públicos.

---

#### Sub-anexo Grupo 4 — Cobertura piezas-bootstrap CAP-G + CAP-J

| Pieza del bootstrap (Job 7 + 10) | Feature owner | Cobertura |
|---|---|---|
| PO Modo 1 (10 pasos) | feature-038 | Total |
| Cadena de WAs por gaps | feature-039 | Total |
| Templates uniformes greenfield/maduro | feature-040 | Total |
| `vault/<rol>/CLAUDE.md` wrappers | feature-010 (CAP-B) | Total via cross-link |
| Atajos npm | feature-010 (CAP-B) | Total via cross-link |
| Ritual de inicio del PO | feature-035 (CAP-F) | Total via cross-link |
| README.md raíz | feature-041 | Total |
| CLAUDE.md raíz | feature-011 (CAP-B) | Total via cross-link |
| `vault/architect/research/bootstrap-summary.md` | feature-042 | Total |
| `propuesta-prefacio.pdf` | feature-042 (agrupado) | Total |
| 5 governance docs (dimensions, role-catalog, workflows, verification-matrix, repo-structure) | Distribuidos: dimensions/role-catalog (feature-009 CAP-B), workflows (feature-013 CAP-C), verification-matrix (feature-021 CAP-D), repo-structure (feature-001 CAP-A) | Total via cross-link |
| `vault/architect/research/library/` | feature-025 (CAP-E) | Total via cross-link |
| LICENSE Apache 2.0 | feature-043 | Total |
| Glosario público (decisión confirmada) | feature-044 | Total |
| Ruta de lectura por audiencia (decisión confirmada) | feature-045 | Total |
| Atribución bibliográfica explícita en docs públicos (Business flag) | feature-046 | Total |

Grupo 4 total: **9 features** (feature-038..feature-046). 7 piezas heredadas de Grupos 1-3 cubren cross-links. 0 piezas sin cobertura final.

---

## Anexo final — Catálogo completo de features y tabla de cobertura piezas × feature-owner

### Lista cerrada de 46 features por capability padre

**Total: 46 features** (feature-001..feature-046) cubriendo las 8 capabilities operant. Cobertura completa de las piezas reales de los 10 Jobs del bootstrap (excluidos Jobs 8 y 9 correspondientes a CAP-H y CAP-I planned, fuera de scope WA-004).

#### CAP-A · Grafo declarativo persistente (7 features)
- feature-001 · Vault role-first como organización física del grafo
- feature-002 · Estructura inline del frontmatter YAML por tipo de nodo
- feature-003 · Wiki-links `[[id]]` como navegación interna entre nodos del grafo
- feature-004 · Estados canónicos del nodo + transiciones validables del lifecycle
- feature-005 · Backlog como query emergente sobre `status`
- feature-006 · Skill compartida `graph-cross-link-declaration`
- feature-007 · Trazabilidad código ↔ grafo vía `// @sem-ia:` y `// @ac-coverage:`

#### CAP-B · Operación multi-rol vía agentes IA homólogos (5 features)
- feature-008 · Identidad bibliográficamente anclada por rol vía agent files
- feature-009 · Catálogo formal de roles + custodios + Cagan risk
- feature-010 · Entry-point por rol vía atajos npm + wrappers CLAUDE.md jerárquicos
- feature-011 · CLAUDE.md raíz como guía estática + entry-point del PO
- feature-012 · Subagente vs sesión-dedicada como criterio operativo de delegación

#### CAP-C · Working Agreements + SDLC (5 features)
- feature-013 · Catálogo de 14 workflow templates indexados por fase SDLC
- feature-014 · Estructura inline del Working Agreement (frontmatter + cuerpo autocontenido)
- feature-015 · Handoff explícito step→step vía Progreso entries audit-ready
- feature-016 · Protocolo de pivot de un WA mid-flight (Gap 4 formalizado)
- feature-017 · Closure-criteria + on-close transitions como contrato declarativo de cierre

#### CAP-D · Verificación multi-rol cruzada (7 features)
- feature-018 · Slash `/scope-scan` para reunión multi-rol on-demand
- feature-019 · Slash `/verify` + algoritmo declarativo `verifiers = {custodian(d)}`
- feature-020 · Tres checkpoints uniformes del WA lifecycle (discovery + step + sign-off)
- feature-021 · `verification-matrix.md` como guía orientativa de dimensiones × operaciones
- feature-022 · Give-and-take mid-step (Cagan principio 2) vía subagentes
- feature-023 · Filtro PO al consolidar scope-scan (4 categorías Cagan) — Gap 6
- feature-024 · Contrato `filesystem-changes` para subagentes con autoridad de edición — Gap 9

#### CAP-E · Anclaje bibliográfico + skills empaquetadas (7 features)
- feature-025 · Biblioteca bibliográfica curada (18 notas + INDEX)
- feature-026 · SKILL.md + design.md como unidad de empaquetado bibliográfico con carga perezosa
- feature-027 · Catálogo de skills PO estratégicas (vision/goal/capability quality + derivation)
- feature-028 · Catálogo de skills PO operativas (feature-decomposition + spec-writing + feature-quality-check)
- feature-029 · Catálogo de skills Architect (adr-writing + viability reviews + coherence + coupling)
- feature-030 · Catálogo de skill Security (threat-modeling) + pendientes Security
- feature-031 · `_pending-later.md` — skills pendientes documentadas con bibliografía

#### CAP-F · Visibilidad operativa (6 features)
- feature-032 · Slash `/status` con panorámica por track Dual + backlog + ADRs
- feature-033 · Slash `/wa` con detalle del WA activo
- feature-034 · Slash `/sessions` con catálogo de modos de trabajo + atajos npm
- feature-035 · Ritual de inicio del PO con panorámica al arrancar sesión
- feature-036 · Orientación al operador sobre qué rol abrir ante ambigüedad
- feature-037 · Dual Track Discovery/Delivery visible en `/status` (Cagan/Patton)

#### CAP-G · Inception greenfield protocol-compliant (3 features)
- feature-038 · PO Modo 1 (Entrada al sistema) con protocolo de 10 pasos
- feature-039 · Cadena de WAs por gaps detectados (vision → goals → capabilities → features)
- feature-040 · Templates uniformes greenfield/maduro (convergencia bajo `workflows.md`)

#### CAP-J · Articulación pública del framework (6 features)
- feature-041 · README.md raíz como onboarding completo del framework
- feature-042 · Artefactos históricos curados (`bootstrap-summary.md` + `propuesta-prefacio.pdf`)
- feature-043 · LICENSE Apache 2.0 como decisión de licenciamiento
- feature-044 · Glosario público de términos SEM-IA (Designer + Business)
- feature-045 · Ruta de lectura diferenciada por audiencia (técnica / académica / adoptante)
- feature-046 · Atribución bibliográfica explícita en docs públicos

### Tabla consolidada — Cobertura pieza-bootstrap × feature-owner

| Pieza del bootstrap | Feature owner (parent único) |
|---|---|
| **Job 1 — Grafo declarativo** | |
| `vault/` organización role-first (8 dirs + shared) | feature-001 (CAP-A) |
| `vault/shared/governance/repo-structure.md` | feature-001 (CAP-A, AC explícito) |
| `vault/shared/governance/dimensions.md` | feature-009 (CAP-B, AC coherencia con role-catalog) |
| Frontmatter YAML obligatorio + campos canónicos | feature-002 (CAP-A) |
| Wiki-links `[[id]]` | feature-003 (CAP-A) |
| Estados canónicos del nodo + transiciones | feature-004 (CAP-A) |
| Skill `graph-cross-link-declaration` | feature-006 (CAP-A, also-relates-to CAP-E) |
| Comentarios `// @sem-ia:` + `// @ac-coverage:` | feature-007 (CAP-A) |
| **Job 2 — Multi-rol agentes** | |
| 8 agent files | feature-008 (CAP-B) |
| `role-catalog.md` | feature-009 (CAP-B) |
| 7 wrappers `vault/<rol>/CLAUDE.md` | feature-010 (CAP-B) |
| `package.json` npm scripts (9) | feature-010 (CAP-B) |
| CLAUDE.md raíz | feature-011 (CAP-B, also-relates-to CAP-G + CAP-J) |
| Mecanismo subagente Task tool | **depends-on-harness** (feature-008, 012, 018, 019, 022, 024) |
| Criterio modality (Gap 8) | feature-012 (CAP-B) |
| **Job 3 — WAs + SDLC** | |
| `workflows.md` 14 templates | feature-013 (CAP-C) |
| Estructura inline del WA | feature-014 (CAP-C) |
| Regla autocontención WA (Gap 7) | feature-014 (CAP-C, AC explícito) |
| Briefing por step (Gap 10) | feature-014 (CAP-C, AC explícito) |
| Progreso entries + handoff explícito | feature-015 (CAP-C, also-relates-to CAP-F) |
| Protocolo pivot WA mid-flight (Gap 4) | feature-016 (CAP-C) |
| Estados WA (active, archived, aborted) | feature-016 + heredado de feature-004 |
| Closure-criteria + on-close | feature-017 (CAP-C) |
| **Job 4 — Verificación cruzada** | |
| Slash `/scope-scan` | feature-018 (CAP-D) |
| Slash `/verify` + algoritmo verifiers | feature-019 (CAP-D) |
| Tres checkpoints uniformes WA lifecycle | feature-020 (CAP-D) |
| `verification-matrix.md` | feature-021 (CAP-D) |
| Give-and-take mid-step (Cagan principio 2) | feature-022 (CAP-D) |
| Filtro PO 4 categorías (Gap 6) | feature-023 (CAP-D) |
| Contrato `filesystem-changes` (Gap 9) | feature-024 (CAP-D) |
| Backlog query emergente | feature-005 (CAP-A) |
| Skills de verificación (5 Architect + 1 Security) | feature-029 + feature-030 (CAP-E), CAP-D `depends-on` |
| **Job 5 — Anclaje bibliográfico** | |
| 18 notas library + INDEX | feature-025 (CAP-E) |
| SKILL.md + design.md unidad empaquetado | feature-026 (CAP-E) |
| Skills PO estratégicas (4) | feature-027 (CAP-E) |
| Skills PO operativas (3) | feature-028 (CAP-E) |
| Skills Architect (5) | feature-029 (CAP-E) |
| Skill Security (1) | feature-030 (CAP-E) |
| `_pending-later.md` skills pendientes (10+) | feature-031 (CAP-E) |
| Carga perezosa nativa Agent Skills | **depends-on-harness** (feature-026..030) |
| **Job 6 — Visibilidad operativa** | |
| Slash `/status` | feature-032 (CAP-F) |
| Slash `/wa` | feature-033 (CAP-F) |
| Slash `/sessions` | feature-034 (CAP-F) |
| Ritual de inicio del PO | feature-035 (CAP-F, also-relates-to CAP-G) |
| Dual Track Discovery/Delivery visible | feature-037 (CAP-F) |
| Orientación qué rol abrir (Designer flag) | feature-036 (CAP-F, also-relates-to CAP-B) |
| **Job 7 — Inception greenfield** | |
| PO Modo 1 (10 pasos) | feature-038 (CAP-G) |
| Cadena de WAs por gaps | feature-039 (CAP-G) |
| Templates uniformes greenfield/maduro | feature-040 (CAP-G) |
| **Job 10 — Articulación pública** | |
| README.md raíz (65 KB) | feature-041 (CAP-J) |
| `bootstrap-summary.md` (16 decisiones + 8 lecciones) | feature-042 (CAP-J) |
| `propuesta-prefacio.pdf` | feature-042 (CAP-J, agrupado) |
| 5 governance docs canónicos | Distribuidos: feature-001/009/013/021 (CAP-A/B/C/D) |
| library bibliográfica | feature-025 (CAP-E) |
| LICENSE Apache 2.0 | feature-043 (CAP-J) |
| Glosario público (decisión confirmada) | feature-044 (CAP-J) |
| Ruta de lectura por audiencia (decisión confirmada) | feature-045 (CAP-J) |
| Atribución bibliográfica en docs públicos (Business flag) | feature-046 (CAP-J) |

**Cobertura final**: 100% piezas reales de Jobs 1-7 + 10 mapeadas a feature owner único. Jobs 8 + 9 fuera de scope (CAP-H + CAP-I planned). Dependencias-del-harness explícitamente declaradas como `depends-on-harness` en features que las usan (NO features propias).

### Metadatos del catálogo

**Features con dimension `security` declarada honestamente** (con anclaje load-bearing, NO checkbox security):
- feature-002 (frontmatter — vector T+I path traversal + YAML unsafe)
- feature-008 (agent files — vector S spoofing)
- feature-024 (contrato `filesystem-changes` — vectores T+R)
- feature-025 (library bibliográfica — integridad académica core del valor del framework: bibliografía inventada destruye el JTBD del producto)
- feature-030 (skill threat-modeling — cubre la dimension misma)
- feature-032 (/status — secret hygiene visible al adopter externo)
- feature-041 (README — advertencia adopter sobre blast radius del vault=público por diseño)

**7 features cubren la dimensión security** con criterio PO: amplía security solo donde el vector es load-bearing para el JTBD del framework o legítimo para adopters externos. NO declara security para vectores que dependen de "agent comprometido" (out-of-scope: SEM-IA opera con honest-agent assumption explícita, no promete autenticación criptográfica entre subagentes).

**Features con dimension `business` declarada honestamente**:
- feature-025 (library — atribución académica para evaluador)
- feature-041 (README — GTM Moore)
- feature-042 (bootstrap-summary — corpus auditable)
- feature-043 (LICENSE)
- feature-044 (glosario — GTM cruzar chasm)
- feature-045 (ruta lectura — GTM Moore)
- feature-046 (atribución bibliográfica explícita)

**Features con dimension `usability` declarada honestamente**:
- feature-003 (wikilinks — navegación interna)
- feature-010 (atajos npm — Nielsen #7)
- feature-011 (CLAUDE.md — Nielsen #10)
- feature-015 (Progreso entries — Nielsen #9)
- feature-032 (/status — Nielsen #1)
- feature-033 (/wa — Nielsen #1+#9)
- feature-034 (/sessions — Nielsen #6)
- feature-035 (ritual inicio — Nielsen #1 + Norman)
- feature-036 (orientación qué rol — Nielsen #6+#7)
- feature-037 (Dual Track visible — Nielsen #1 + Cagan)
- feature-038 (PO Modo 1 — Norman)
- feature-041 (README — Nielsen #10)
- feature-044 (glosario — Nielsen #2+#4)
- feature-045 (ruta lectura — Nielsen #10 + Cooper)

**ADRs latentes apuntados desde features** (lista consolidada — input para Lote B WAs `adr` posteriores):
- ADR-latente-001 (Claude Code v1 harness primario): features 008, 010, 011, 018, 019, 022, 026
- ADR-latente-002 (Vault role-first): features 001, 010
- ADR-latente-003 (Frontmatter YAML + wikilinks): features 002, 003, 014
- ADR-latente-004 (Estados canónicos + transiciones): feature 004
- ADR-latente-005 (Skills como unidad empaquetado): features 006, 025, 026, 027, 028, 029, 030, 031
- ADR-latente-007 (Fases SDLC redefinibles): features 013, 014, 040
- ADR-latente-008 (Backlog query emergente): features 005, 007, 032
- ADR-latente-009 (Tres checkpoints uniformes WA lifecycle): features 015, 020
- ADR-latente-010 (Algoritmo declarativo verifiers): features 017, 019
- ADR-meta-1 (Uniformidad mode-flag templates batch-capables): emergente del WA-004 scope-scan, a confirmar
- ADR-security-trans (Modelo threat surface del framework): recomendado por security step-6 WA-004 — debe enunciar threat model raíz "SEM-IA asume agentes alineados; NO protege contra agente desalineado con write access"

**Dependencias-del-harness declaradas** (input para CAP-H adapters cuando se active):
- Filesystem versionado por git
- Parser YAML del runtime
- Render Markdown de editor/viewer
- Mecanismo agent files de Claude Code (subagent_type)
- Mecanismo CLAUDE.md jerárquico
- Task tool de Claude Code
- Carga perezosa nativa de Agent Skills
- Sesión multi-turn de Claude Code

### Veredictos preliminares de granularidad y JTBD

(Veredictos formales se aplicarán por Architect step-3 + QA step-7 del WA-004. Preliminar PO):

- **Granularidad uniforme**: 46/46 features estimadas en rango 2-7 stories descomponibles. Veredicto preliminar `ok` cross-features.
- **Anti-patrón features-as-output-blind**: 0/46 detectadas. Cada feature enuncia JTBD del operador (humano o agente).
- **Distinción features-propias vs depends-on-harness**: 8 dependencias-harness declaradas explícitamente en features que las usan; 0 features-propias falsamente atribuidas al harness.
- **Solapamientos cross-cap declarados**: 3 detectados al inicio resueltos con parent único + `also-relates-to`: CAP-01↔CAP-03 (estados canónicos → parent CAP-01), CAP-04↔CAP-05 (skills → parent CAP-05), CAP-06↔CAP-03 (/wa+Progreso → /wa parent CAP-F, Progreso parent CAP-C).

Estos veredictos preliminares son los datos del PO. La verificación formal cross-rol pertenece a Architect step-3 + QA step-7.

### Post-step scope-scan multi-rol — registro (2026-05-12T23:00)

Tras cerrar el inventario, se ejecutó **post-step scope-scan flat parallel multi-rol** con los 5 asesores en paralelo (read-only).

**Filtro PO aplicado con criterio fuerte** (Cagan *strong PM* + Ousterhout *deep modules*) — peleado cada flag para distinguir load-bearing vs noise:

**Mantenidos al discovery doc** (6 cambios con valor load-bearing demostrable):
- feature-025 +security: integridad bibliográfica de la library es CORE del valor del framework (anclaje auditable). Bibliografía inventada destruye el JTBD del producto.
- feature-032 +security: /status agrega vault completo; secret hygiene aplicable a adopters externos con datos sensibles.
- feature-041 +security: README debe advertir adopters sobre blast radius (vault=público por diseño).
- feature-036 AC error state: Nielsen #9 legítimo — operador en sesión equivocada necesita recovery comunicado.
- feature-044 AC categorías mínimas: sin categorías el glosario cumple cantidad sin calidad.
- feature-045 AC criterio ruta completa: progressive disclosure necesita completitud mínima por ruta.

**Descartados con razón fuerte** (resto de recomendaciones de advisors):
- Security en features 015/017/019/026/035/046: vectores dependientes de "agent comprometido / tampering". **SEM-IA opera con honest-agent assumption explícita** — declarar security para vectores out-of-scope es anti-patrón "checkbox security" que infla sin proteger. NO load-bearing.
- Cross-links cross-feature en 007/014/024/036: coupling transitivo over-declarado. **Cohn INVEST `I = Independent` requiere coupling mínimo declarado, no máximo**. Architect over-engineered.
- ADRs latentes adicionales 006 (Filtro PO) y 011 (modality): ya formalizados en Gaps 6 y 8 del WA-003 + agent files. **No son decisiones arquitectónicas con alternatives** — son comportamiento operativo. No merecen Nygard.
- Usability en feature-039: el JTBD core es procedimiento PO, no UI al humano. Usability vive en features 035 y 038.
- AC IDs semánticos en feature-003: los IDs los crean las features creadoras, no la feature de navegación.
- AC estructura formal Progreso en feature-015: ya implícito en el cuerpo de la feature.

**Decisiones humanas confirmadas durante consolidación**:
- Orden steps 3-7: **steps 3-6 paralelo + step-7 QA al final** (QA necesita outputs cross-rol).
- Features 044/045 deadline GISF: **aceptar conscientemente** que artefactos físicos NO se materialicen antes del 2026-05-25.

**Diferidos a WA futuro o fuera de scope** (categorías 2-3 del filtro):
- NOTICE Apache 2.0: aplicable solo con distribución (CAP-H planned), diferido.
- CONTRIBUTING.md gobernanza contribuciones: diferido a WA posterior CAP-J/CAP-A.
- depends-on-harness campo improvisado: diferido a WA `doc-edit` posterior que formalice.
- ADR-latente-003 dividir 003a/003b al formalizar: diferido al WA `adr` correspondiente.
- ADR-latente-008 paraguas vs separar: diferido al WA `adr` correspondiente.
- Namespace npm `@sem-ia`: acción operativa fuera del WA, en backlog CAP-H.
- ADR-security-trans confirmación: pertenece al step-6 propio del security officer.

**Veredicto consolidado PO**: discovery doc del step-1 **apto-para-step-2** tras pelea fuerte del Filtro PO. 6 cambios load-bearing mantenidos; resto descartado con criterio bibliográfico explícito. Ningún flag bloqueante residual.

---

## Cierre del step-1

**Status**: lista cerrada de 46 features candidatas con parent único + cross-links cross-cap declarados + dependencias-del-harness identificadas + ADRs latentes apuntados + dimensiones honestas. Ground truth para step-2 (PO escribir N feature files draft).

**Convenciones aplicadas** (input para step-2):
1. Granularidad: Cohn INVEST `S` + Patton task-level
2. JTBD del operador (humano o agente)
3. Distinción features-propias vs depends-on-harness
4. AC enumerados con anotación `verificable vía:` por AC
5. Parent único + cross-links cross-cap explícitos
6. ADRs latentes apuntados per-feature
7. Dimensions-affected honestas (incluyendo security cuando mapping STRIDE lo indique)
8. Estados de feature: `draft` al crearse (transitará a `active` al `/verify` del WA-004)

**Próximo step**: step-2 (PO sesión-dedicada) — escritura de los 46 feature files en `vault/product-owner/specs/feature-001..feature-046.md` siguiendo las convenciones declaradas y los enunciados+cross-links de este discovery doc.
