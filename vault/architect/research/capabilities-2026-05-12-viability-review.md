---
type: research
id: capabilities-2026-05-12-viability-review
title: "Viability-review consolidado del catálogo de 10 capabilities · WA wa-2026-05-12-002"
status: active   # transición aplicada por /verify del WA wa-2026-05-12-002 el 2026-05-12T05:30+02:00
created: 2026-05-12
author: architect
related-wa: wa-2026-05-12-002
related-vision: vision
related-goals: [goal-1-auto-sostenibilidad, goal-2-output-auditable-multirol, goal-3-absorcion-coste-revision, goal-4-rigor-multirol-individual, goal-5-portabilidad, goal-6-articulacion-publica, goal-7-ciclo-vida-producto]
references:
  - vault/product-owner/discovery/capabilities-bootstrap-extraction-2026-05-12.md
  - vault/product-owner/strategy/cap-01-grafo-declarativo-persistente.md
  - vault/product-owner/strategy/cap-02-multirol-agentes-homologos.md
  - vault/product-owner/strategy/cap-03-working-agreements-sdlc.md
  - vault/product-owner/strategy/cap-04-verificacion-multirol-cruzada.md
  - vault/product-owner/strategy/cap-05-anclaje-bibliografico-skills.md
  - vault/product-owner/strategy/cap-06-visibilidad-operativa.md
  - vault/product-owner/strategy/cap-07-inception-greenfield.md
  - vault/product-owner/strategy/cap-08-portabilidad-multi-harness.md
  - vault/product-owner/strategy/cap-09-adopcion-retroactiva.md
  - vault/product-owner/strategy/cap-10-articulacion-publica.md
  - vault/shared/governance/dimensions.md
  - vault/shared/governance/role-catalog.md
  - vault/shared/governance/workflows.md
  - vault/shared/governance/repo-structure.md
  - vault/shared/governance/verification-matrix.md
bibliography:
  - "Bass, Clements, Kazman — Software Architecture in Practice (QAs + tactics + tradeoffs)"
  - "Ford, Parsons, Kua — Building Evolutionary Architectures (fitness functions, appropriate coupling, evolvability)"
  - "Ousterhout — A Philosophy of Software Design (deep modules, information hiding)"
  - "Martin — Clean Architecture (Dependency Rule, dependency inversion, boundaries)"
  - "Nygard — Documenting Architecture Decisions (ADR format, immutability, supersession)"
  - "Shostack — Threat Modeling (referenciado para CAP-09 secret leakage)"
---

# Viability-review consolidado del catálogo de 10 capabilities

## Contexto

Step-3 del WA `wa-2026-05-12-002` (capability-creation bottom-up). El PO ha extraído 10 capabilities operantes desde el bootstrap construido (step-1) y las ha formalizado como nodos del grafo (step-2). Este documento es el output del Architect: viability-review consolidado por capability, anexo de ADRs latentes aflorados (NO escritos), y coherence-evaluation final.

**Aplicación de skills**:
- `capability-viability-review` por capability (Bass QAs + tactics + tradeoffs + dimensions honest + related-adrs latentes).
- `coherence-evaluation` final del catálogo contra vision + goals + governance + repo-structure.
- `adr-writing` SOLO para identificar candidatos, no para escribir ADRs (decisión cerrada con humano en WA-002).

**Scope explícito**: NO se cuestionan decisiones del PO sobre estructura del catálogo (autoridad de product). El Architect aporta viability técnica con anclaje bibliográfico. Donde detecta inconsistencia técnica real, declara flag.

## Veredicto global

**Aprueba con condiciones menores.**

- Las 10 capabilities tienen viability técnica defendible. QAs Bass declarados son apropiados y coherentes con el bootstrap operante.
- Dimensions-affected están declaradas honestamente (no heredan mecánicamente del goal padre — cumple flag crítico Architect heredado del WA-001).
- Tactics y tradeoffs están explícitamente documentados con anclaje bibliográfico verificable.
- 2 capabilities `planned` (CAP-08, CAP-09) tienen viability flag importante: requieren ADR(s) reales + threat-model formal antes de pasar a feature-design. Documentado.
- 4 condiciones menores listadas en sección "Flags emergentes" (no bloqueantes para `/verify`, pero a procesar en WAs futuros).

El catálogo es **coherente** con vision, goals, governance y repo-structure. Sin contradicciones detectadas. Coupling entre capabilities documentado vía `depends-on` (CAP-04 → CAP-02; CAP-07 → CAP-03; CAP-09 → CAP-08) — pattern Martin Clean Architecture (dependency inversion: capacidades de bajo nivel custodian primitivas; capacidades de alto nivel componen sobre ellas).

---

## Viability por capability

### CAP-01 · Grafo declarativo persistente del proyecto

- **QAs Bass implicados** (validación): `modifiability`, `auditability`, `analyzability`, `portability`. Coherentes — el grafo como infraestructura justifica los 4. Añadiría implícitamente `interoperability` (frontmatter YAML + wiki-links son standard formats, accesibles a tooling externo) — no bloqueante, documentado en tactic "Standard data formats".
- **Tactics** (validación): información hiding (frontmatter vs contenido), intermediary (cross-links declarativos), semantic coherence (convención inline), standard data formats. Correctos y citables a Bass. Faltaría tactic explícita "Configurability" (Ousterhout): el adopter extiende dimensions y tipos de nodo sin romper el schema base — implícito en CAP-08 universal/, no bloqueante.
- **Tradeoffs** (validación): aceptables. El tradeoff "query O(N)" tiene fitness function declarable cuando se construya `sem-ia check` (CAP-08). Tradeoff "cross-links manuales" es real — vigilar como information leakage (Ousterhout) si los renombrados de IDs se vuelven comunes.
- **Dimensions-affected honest**: `[product, technical]` — correcto. Es decisión arquitectónica con QAs Bass, no solo organizacional.
- **ADRs latentes relacionados**: ADR-latente-002, ADR-latente-003, ADR-latente-004, ADR-latente-008.
- **Veredicto**: **aprueba**.
- **Notas**: el grafo es **deep module** (Ousterhout) — interfaz simple (frontmatter + paths) con implementación profunda (semántica de tipos + lifecycle + cross-links). Es columna vertebral arquitectónica; cualquier cambio significativo requerirá ADR.

### CAP-02 · Operación multi-rol vía agentes IA homólogos especializados

- **QAs Bass implicados** (validación): `modifiability`, `modularity`, `portability`, `learnability`. Coherentes. Sugeriría añadir `replaceability` (Ford evolutionary) — un agent file puede reescribirse sin tocar otros gracias al desacoplamiento; el flag de "vault/developer/CLAUDE.md pendiente" sin bloquear `operant` valida esto. No bloqueante, mejora opcional.
- **Tactics** (validación): deep modules (cada rol), abstraction (6 asesores + 2 ejecutores), naming conventions, use intermediary (Task tool). Correctos. La tactic "Deep modules" es la fundamental — cada rol expone interfaz simple (agent file declarativo) e implementación profunda (identidad + skills + protocolos). Justifica la separación de 8 archivos en lugar de un megafile.
- **Tradeoffs** (validación): aceptables. El tradeoff "8 roles = más cognitive load" tiene mitigación documentada (cada sesión carga su rol activo); el flag de Designer (Nielsen #6) está preservado correctamente.
- **Dimensions-affected honest**: `[product, technical, usability]` — correcto. `usability` añadido por Designer (Nielsen #6 al alternar roles) — honesto.
- **ADRs latentes relacionados**: ADR-latente-001, ADR-latente-002.
- **Veredicto**: **aprueba**.
- **Notas**: dependency inversion (Martin) aplicada: Task tool es **intermediary** que permite invocación entre roles sin acoplamiento de implementación. Coupling es **appropriate** (Ford) — los roles se conocen por nombre + dimensión, no por implementación interna. Validar fitness function: ningún agent file debería require knowledge of internal protocols of another agent file (solo de su dimensión custodiada + skills expuestas).

### CAP-03 · Coordinación de trabajo vía Working Agreements indexados por fase SDLC

- **QAs Bass implicados** (validación): `modifiability`, `deployability`, `testability`, `evolvability`. Coherentes. El uso de `evolvability` (Ford) es apropiado — los adopters pueden añadir templates SDLC custom sin tocar el core.
- **Tactics** (validación): separation of concerns (templates por fase), declarative structure, emergent state (backlog), standardized handoff, configurable framework. Excelente set bibliográfico. La tactic "Emergent state" (backlog-como-query) es **information hiding** (Ousterhout) aplicado a estructura del proyecto: el adopter no necesita conocer cómo se construye el backlog, solo que existe la query — minimiza el contracto entre WAs design y WAs implementation.
- **Tradeoffs** (validación): aceptables. El tradeoff "estado distribuido sin UI consolidada" debe vigilarse con fitness function: si el proyecto escala a cientos de WAs, `/status` debe paginarse (declarado en CAP-06 notas).
- **Dimensions-affected honest**: `[product, technical, operations]` — correcto. `operations` justificado porque workflows.md incluye fase SDLC `operations` con templates `pipeline-change` / `infra-decision` / `observability-instrument`.
- **ADRs latentes relacionados**: ADR-latente-007, ADR-latente-008, ADR-latente-009.
- **Veredicto**: **aprueba**.
- **Notas**: CAP-03 tiene **límite alto** del rango Cohn 2-5 features (6+ features candidatas preview). PO justifica como sub-bloques inseparables del job; el Architect valida esa decisión — los sub-bloques (WA structure + workflows + backlog + handoff + estados) están **deeply coupled by semantics** (Ford appropriate coupling), no por implementación. Defendible.

### CAP-04 · Verificación multi-rol cruzada en checkpoints uniformes

- **QAs Bass implicados** (validación): `testability`, `modifiability`, `separability`, `auditability`. Coherentes. `separability` es término poco estándar en Bass; sugiero sustituir por `independence` o explicitar como "verifier independence" (los custodios operan sin acoplarse entre sí). No bloqueante — cosmético, se puede ajustar en `/verify` o aparcar.
- **Tactics** (validación): three uniform checkpoints, declarative algorithm, flat parallel, give-and-take mid-step, AC traceability. **Excelente cobertura**. La tactic "declarative algorithm `verifiers = {custodian(d) : d ∈ dimensions-affected}`" es el corazón arquitectónico — pattern declarative deriving (Martin) que evita lógica imperativa. Es **fitness function explícita** (Ford): cualquier feature de CAP-04 que rompa el algoritmo es regresión detectable.
- **Tradeoffs** (validación): aceptables. El tradeoff "verifiers en paralelo NO cascadean" es **intencional** — flat parallel evita coupling cascade (Ousterhout temporal coupling). Cada verifier opera con vista propia; recepción consolida.
- **Dimensions-affected honest**: `[product, quality, technical]` — correcto. `quality` justifica QA como custodio si surgen features de CAP-04 (ej. coverage tools); `technical` por el mecanismo Task tool + slash commands.
- **Depends-on**: `cap-02-multirol-agentes-homologos`. **Correcto** — Martin Dependency Rule: CAP-04 depende de CAP-02 (capability de bajo nivel: existencia de roles invocables), no al revés. Documenta appropriate coupling.
- **ADRs latentes relacionados**: ADR-latente-009, ADR-latente-010.
- **Veredicto**: **aprueba**.
- **Notas**: el "framework regression detection" (flag QA aparcado en notes) es candidato a feature futura — cuando emerja, threat-model implícito: editar un agent file puede silenciar verificación cross-rol. Mitigación: hooks de Claude Code (P2 README).

### CAP-05 · Anclaje bibliográfico auditable mediante skills empaquetadas y biblioteca canónica

- **QAs Bass implicados** (validación): `maintainability`, `reusability`, `auditability`, `learnability`. Coherentes. Añadiría implícitamente `traceability` (Ford evolutionary) — cada decisión trazable a fuente; ya está cubierto por `auditability`, no es bloqueante.
- **Tactics** (validación): each skill cites source, packaged happy-paths, library indexed, lazy loading. Correctos. La tactic "Lazy loading" depende del harness (Anthropic Claude Code Agent Skills) — riesgo de coupling con harness específico. Mitigación: cuando CAP-08 construya adapters multi-harness, la lazy loading debe replicarse o sustituirse en cada harness target. Documentado en notas operativas.
- **Tradeoffs** (validación): aceptables. El tradeoff "skills lazy-load probabilístico" es real — Ford fitness function candidato: monitorear cuándo NO se invocó la skill cuando aplicaba (detección de coverage gap).
- **Dimensions-affected honest**: `[product, quality]` — correcto. `quality` justifica QA si se construyen tools de validación bibliográfica.
- **ADRs latentes relacionados**: ADR-latente-005.
- **Veredicto**: **aprueba**.
- **Notas**: la separación `SKILL.md` (operativo) + `design.md` (referencia) es **deep module** (Ousterhout) — SKILL.md tiene interfaz reducida (quick-reference + when-to-invoke + process); design.md provee profundidad sin contaminar el contrato operativo. Patrón replicable.

### CAP-06 · Visibilidad operativa del estado y progreso del proyecto

- **QAs Bass implicados** (validación): `usability`, `learnability`, `performance`, `observability`. Coherentes. `observability` es término propio de operations (no Bass original), pero está extendido en Ford evolutionary architectures — aceptable. `performance` (<2s slash) tiene fitness function declarable.
- **Tactics** (validación): visibility heuristic (Nielsen #1), recognition over recall (Nielsen #6), error recovery (Nielsen #9), dual track visualization, distinct perspectives (Cooper). **Excelente cobertura usability**. Los 3 heuristics Nielsen + Cooper en distintos roles aplican.
- **Tradeoffs** (validación): aceptables. El tradeoff "no UI gráfica" es **decisión consciente** documentada — target técnico (ingenieros) acepta CLI; reconsiderar si CAP-08 escala a adopters no-técnicos.
- **Dimensions-affected honest**: `[product, usability, technical]` — correcto. `usability` honesto (no mecánico) por las 3 heuristics Nielsen citadas explícitamente.
- **ADRs latentes relacionados**: ninguno crítico hoy (los slash commands son implementación del harness). Si se materializa "filtros y paginación de /status", podría emerger ADR sobre query strategy.
- **Veredicto**: **aprueba**.
- **Notas**: los slash commands tienen **coupling con harness** (no portables sin adapter — declarado en notas operativas). Es appropriate coupling (Ford) mientras CAP-08 sea `planned`; cuando se construya el adapter OpenCode/Pi, slash commands deben replicarse o sustituirse.

### CAP-07 · Inception greenfield protocol-compliant desde vault vacío

- **QAs Bass implicados** (validación): `learnability`, `predictability`, `modifiability`, `portability`. Coherentes. `predictability` (uniformidad inception ↔ mantenimiento) es key — justifica deep module (Ousterhout): mismo protocolo en ambos contextos.
- **Tactics** (validación): uniform protocol (deep module), conversational guidance, cadena ordenada top-down, affordance ergonómica. Correctos. La tactic "Uniform protocol" es la fundamental — Ousterhout aplicado al meta-nivel: SEM-IA usa los mismos templates en greenfield que en mature, evitando "special case" code que duplicaría complejidad.
- **Tradeoffs** (validación): aceptables. El tradeoff "inception lenta vs script" es **intencional** — el coste estructural compra auditabilidad desde el primer minuto. El tradeoff "gap 3 del WA-002" reconoce que el template `capability-creation` no contemplaba batch ni bottom-up; honestidad apropiada.
- **Dimensions-affected honest**: `[product, technical, usability]` — correcto. `usability` por DX del PO conduciendo inception (Norman: modelo conceptual emergente).
- **Depends-on**: `cap-03-working-agreements-sdlc`. **Correcto** — CAP-07 consume los workflow templates de CAP-03; documenta appropriate coupling (Ford). Sin esta declaración, el coupling sería implícito y rompería fitness function "depends-on declarado".
- **ADRs latentes relacionados**: ninguno crítico hoy. Si se construye skill `inception-orchestration`, podría emerger ADR sobre detección del estado del vault.
- **Veredicto**: **aprueba**.
- **Notas**: el `depends-on cap-03` valida el flag Architect del scope-scan WA-001 (CAP-07 separada de CAP-03 con coupling explícito, no fusión). Architect (yo) confirmo: la inception es habilidad cohesiva propia (detección vault vacío + cadena ordenada + conducción PO Modo 1), no feature de CAP-03 — el job greenfield-from-empty es distinto del job coordinate-work-in-mature-project.

### CAP-08 · Portabilidad multi-harness y distribución como `@sem-ia/cli` [PLANNED]

- **QAs Bass implicados** (validación): `portability` (CRÍTICO), `deployability`, `modifiability`, `security`. Coherentes. `security` honestamente declarado — supply chain + path traversal + YAML parsing son vectores reales.
- **Tactics** (validación): adapter pattern, dependency inversion (Martin), schema-based validation, cross-link integrity check, AC coverage tool, safe defaults en CLI. **Excelente cobertura** — los 6 tactics tienen anclaje bibliográfico explícito (Martin Clean Architecture es el más citable para adapter + dependency inversion).
- **Tradeoffs** (validación): aceptables. El tradeoff "multi-harness multiplica maintenance" es real; mitigación: pin de adapters al subset usado. El tradeoff "supply chain risk" tiene mitigación tactic (scope namespace + pin versiones + tests integridad) — coherente.
- **Dimensions-affected honest**: `[product, technical, operations, business, security]` — **correcto y honesto**. 5 dimensiones es legítimo para CAP-08:
  - `technical` (arquitectura del CLI + adapters)
  - `operations` (packaging + distribución + build step)
  - `business` (LICENSE Apache 2.0 + namespace registry npm)
  - `security` (supply chain + filesystem mutation + YAML safe-load)
- **ADRs latentes relacionados**: ADR-latente-001, ADR-latente-006.
- **Veredicto**: **aprueba con condición — requiere ADR(s) reales antes de feature-design**. Cuando CAP-08 pase de `planned` a `in-implementation`:
  1. ADR sobre **mecanismo de sync** entre `src/adapters/claude-code/` y dogfooding `.claude/` (build step, symlinks, single source).
  2. ADR sobre **CLI surface** (commands, flags, output format).
  3. Threat-model formal del Security Officer sobre los 4 vectores declarados (supply chain, path traversal, YAML parsing, template injection en init).
- **Notas**: la viability técnica está bien razonada por PO. Architect respalda. El **dependency inversion** (Martin) entre `src/universal/` y `src/adapters/<harness>/` es la decisión arquitectónica fundamental — adapters deben depender de universal, no al revés. Fitness function declarable: ningún `src/universal/*` debería importar de `src/adapters/*`.

### CAP-09 · Adopción retroactiva desde proyecto pre-existente [PLANNED]

- **QAs Bass implicados** (validación): `portability`, `testability`, `security` (CRÍTICO), `reliability` (idempotencia). Coherentes. `security` CRÍTICO honestamente declarado — secret leakage es el vector inherente del walk.
- **Tactics** (validación): archeology walk, read-only mode, denylist by default (Ousterhout information hiding aplicado a security), pattern scanning, redacted-by-default, derivación auditable. **Cobertura security-first apropiada** — Shostack threat-modeling implícito en cada tactic.
- **Tradeoffs** (validación): aceptables. El tradeoff "walk de código heterogéneo no-trivial" es **viability flag mayor** — Architect lo reconoce explícitamente. Cuando se descomponga, debe haber estrategia clara de qué lenguajes/AST se soportan en MVP y cuáles vienen después. Tradeoff "ADRs retroactivos especulativos" requiere convención `retroactive-inferred` (declarada) para distinguir de ADRs proposados-en-su-momento.
- **Dimensions-affected honest**: `[product, technical, security]` — correcto. Falta posiblemente `business` si la adopción implica compliance con licencias del adopter (ej. proyecto adopter tiene código GPL — derivación retroactiva no debe contaminar el vault SEM-IA con código bajo licencia incompatible). No bloqueante, **flag menor** a evaluar cuando se descomponga.
- **Depends-on**: `cap-08-portabilidad-multi-harness`. **Correcto** — `/adopt` se invoca desde el CLI distribuible; sin CAP-08, no hay donde implementar `/adopt`.
- **ADRs latentes relacionados**: ninguno crítico hoy. Los ADRs reales emergerán cuando se descomponga (architecture-archeology, walker strategy, security defaults concretos).
- **Veredicto**: **aprueba con condición — requiere ADR(s) + threat-model FORMAL antes de feature-design**. Concretamente:
  1. ADR sobre **estrategia de walker** (lenguajes soportados MVP, profundidad, manejo de archivos binarios).
  2. ADR sobre **idempotencia del walk** (re-derivar produce resultado equivalente).
  3. Threat-model formal completo del Security Officer (no solo defaults declarados — STRIDE aplicado al walk: confidentiality del adopter, integrity del vault SEM-IA derivado, secrets pattern coverage).
- **Notas**: Architect viability flag preservado del scope-scan WA-002 — walk de código heterogéneo es **alto riesgo técnico** (testability + modifiability). El PO ha capturado esto en tradeoffs, correctamente. La feature debe priorizarse cuidadosamente: MVP solo TypeScript/JavaScript (lenguaje del dogfooding inicial) podría reducir scope técnico significativamente.

### CAP-10 · Articulación pública del framework para audiencias externas

- **QAs Bass implicados** (validación): `usability` (legibilidad), `learnability`, `comprehensibility`, `maintainability`. Coherentes. `comprehensibility` no es QA estándar Bass; se puede asimilar a `understandability` (Ford) o `learnability`. No bloqueante — terminología documental, no estructural.
- **Tactics** (validación): progressive disclosure (Nielsen), narrative coherence (Sinek), licensing claro, multi-audiencia, repo público versionado. Correctos. La tactic "Progressive disclosure" es **information hiding aplicado a documentación** (Ousterhout) — README de alto nivel oculta detalles que viven en governance docs y library.
- **Tradeoffs** (validación): aceptables. El tradeoff "docs verbose (65 KB README)" tiene mitigación (progressive disclosure) pero es coste real — feature futura "glosario navegable + índice newcomer" lo absorbería.
- **Dimensions-affected honest**: `[product, business, usability]` — correcto. `business` por LICENSE Apache 2.0 + compliance académico + namespace npm. `usability` por legibilidad estándar de docs.
- **ADRs latentes relacionados**: ninguno crítico hoy. Si se construye web site dedicado o glosario formal, podría emerger ADR sobre hosting/CDN.
- **Veredicto**: **aprueba**.
- **Notas**: CAP-10 tiene cobertura documental fuerte ya construida (README + bootstrap-summary + 5 governance + library). La mantenibilidad de estos docs es la fitness function crítica — Ford recomienda fitness functions automatizables: sugerir feature futura "doc drift detector" que valide que governance docs no contradicen el bootstrap construido. No bloqueante para `/verify`, candidato a backlog futuro.

---

## Anexo — 10 ADRs latentes aflorados (NO escritos)

Cada uno: id-tentativo + título + contexto resumido + decisión que afloraría + consecuencias clave + alternativas evaluadas (breve) + capabilities relacionadas. Estos se escribirán como ADRs reales en WA dedicado posterior orquestado por Architect.

### ADR-latente-001 — Adopción de Claude Code como harness primario para el dogfooding

- **Contexto**: SEM-IA es framework multi-harness por visión (`goal-5-portabilidad`), pero el bootstrap construyó adapter para Claude Code como target inicial. La decisión `Claude Code primario` no está documentada como ADR — es elección implícita.
- **Decisión latente**: adoptar Claude Code como harness primario; otros harnesses (OpenCode, Pi) emergerán como adapters secundarios cuando haya demanda real de adopters.
- **Consecuencias**: dependencias con primitivas de Claude Code (`Task tool`, slash commands, Agent Skills lazy loading). Adapters futuros deben replicar o sustituir esas primitivas.
- **Alternativas evaluadas**: empezar harness-agnóstico (rechazado por coste de adapter pattern desde día 0); OpenCode primario (rechazado por madurez menor del ecosistema en momento del bootstrap).
- **Capabilities relacionadas**: CAP-02 (Task tool subagent), CAP-05 (lazy loading), CAP-06 (slash commands), CAP-08 (portabilidad explícita).

### ADR-latente-002 — Vault role-first (un directorio por rol custodio)

- **Contexto**: La organización física del vault es decisión arquitectónica significativa. Alternativas posibles: type-first (`vault/specs/`, `vault/adrs/`, `vault/audits/`), phase-first (`vault/discovery/`, `vault/design/`).
- **Decisión latente**: role-first — `vault/<rol>/` con sub-directorios por tipo. Justifica auto-explicabilidad + extensibilidad (adopter añade `vault/<rol-custom>/`) + cohesión con la filosofía SEM-IA (roles homólogos).
- **Consecuencias**: cada rol tiene scope claro de escritura (declarado en agent files). Cross-references entre roles vía paths absolutos. Wrapper `vault/<rol>/CLAUDE.md` por rol como entry point.
- **Alternativas evaluadas**: type-first (rechazado por dificultar scope de escritura por rol); phase-first (rechazado por confundir lifecycle del nodo con organización física); flat (rechazado por scalability).
- **Capabilities relacionadas**: CAP-01 (organización del grafo), CAP-02 (wrappers por rol), CAP-08 (adopter clona estructura).

### ADR-latente-003 — Frontmatter YAML + wiki-links `[[id]]` como mecanismo del grafo

- **Contexto**: Cómo declarar la estructura del grafo (nodos + aristas) de forma legible y herramienta-agnóstica.
- **Decisión latente**: frontmatter YAML para metadata estructural (parent, also-relates-to, depends-on, dimensions-affected, related-adrs, status) + wiki-links `[[id]]` en contenido para referencias narrativas.
- **Consecuencias**: legibilidad sin tooling especial. Parseable por scripts simples. Adopters pueden usar editores estándar (Obsidian, VSCode). Limitación: validación de cross-links requiere tool (CAP-08 `sem-ia check`).
- **Alternativas evaluadas**: JSON schemas exclusivamente (rechazado por menos legible humano); base de datos (rechazado por no versionable git-native); RDF/triples (rechazado por overkill para target técnico).
- **Capabilities relacionadas**: CAP-01 (mecanismo central), CAP-08 (validation tool).

### ADR-latente-004 — Estados canónicos del nodo (incluye propuesta `aborted` del Gap 1 del WA-002)

- **Contexto**: Lifecycle declarativo de cada nodo del grafo. Estados deben ser predecibles, no improvisables.
- **Decisión latente**: estados canónicos = `draft | proposed | active | accepted | ready-for-implementation | in-implementation | implemented | superseded | deprecated`. Pendiente formalizar `aborted` para WAs pivotados mid-flight (Gap 1 del anexo WA-002).
- **Consecuencias**: transiciones declaradas en `on-close` del template. Recepción aplica al `/verify`. Cualquier estado fuera del catálogo es bug.
- **Alternativas evaluadas**: estados libres por adopter (rechazado por incoherencia entre proyectos); FSM rígido sin extensibilidad (rechazado por inflexibilidad).
- **Capabilities relacionadas**: CAP-01 (lifecycle), CAP-03 (estados del WA), Gap 1 del WA-002.

### ADR-latente-005 — Skills como unidad de empaquetado bibliográfico (SKILL.md + design.md + carga perezosa)

- **Contexto**: Cómo empaquetar happy-paths bibliográficos auditables que se invoquen automáticamente cuando el contexto matchea.
- **Decisión latente**: skill = directorio `.claude/skills/<rol>/<skill>/` con `SKILL.md` (operativo: quick-reference + when-to-invoke + process + output + bibliographic foundation) + `design.md` opcional (referencia detallada con citas literales). Carga perezosa nativa Claude Code.
- **Consecuencias**: cada decisión auditable cita su fuente. Adopters pueden añadir skills custom siguiendo el mismo formato. Lazy loading depende del harness — adapters futuros deben replicar.
- **Alternativas evaluadas**: single-file skills (rechazado — no separa operativo de referencia); skills imperativas con código (rechazado — incoherente con filosofía declarative); skills sin lazy load (rechazado — coste token de cargar todas).
- **Capabilities relacionadas**: CAP-05 (mecanismo central), CAP-08 (replicar lazy loading en adapters).

### ADR-latente-006 — Separación `src/` (distribuible) vs `.claude/` (harness-specific bundled) vs `vault/` (dogfooding)

- **Contexto**: Tres cosas coexisten en el repo: el framework distribuible, los artifacts harness-specific que Claude Code descubre, y el contenido del proyecto SEM-IA usándose a sí mismo. Decisión arquitectónica de boundaries.
- **Decisión latente**: tres carpetas con responsabilidad clara y regla de no-duplicación. `src/` se publica como `@sem-ia/cli`; `.claude/` es bundled de adapter Claude Code; `vault/` es contenido del dogfooding (no viaja al adopter). Build step (TBD) sincroniza `src/adapters/claude-code/` con `.claude/` del dogfooding.
- **Consecuencias**: separación clara entre framework y proyecto-usándose. Adopter solo recibe `src/` + bundle adapter. Mantenimiento dual: si bootstrap se modifica via WA, hay que decidir si propaga a `src/adapters/claude-code/`.
- **Alternativas evaluadas**: monorepo sin separación (rechazado por contaminar adopter); single source con symlinks (pendiente — viable alternativa al build step); duplicación consciente (rechazado por drift inevitable).
- **Capabilities relacionadas**: CAP-08 (mecanismo central), CAP-10 (articulación de la separación), Martin Clean Architecture (boundaries explícitas).

### ADR-latente-007 — Fases SDLC redefinibles por adopter

- **Contexto**: Las 5 fases SDLC declaradas (`discovery | design | implementation | operations | meta`) son defaults; los adopters pueden tener SDLCs distintos (SAFe, lean, DeFi-specific).
- **Decisión latente**: las fases SDLC son **defaults extensibles** — los adopters pueden añadir fases custom (ej. `experiment` para lean, `program-increment` para SAFe) y mapear workflow templates a ellas. La regla: cada template declara su `phase`, recepción la deriva al cargar.
- **Consecuencias**: framework no impone SDLC rígido. Adopters extienden `workflows.md`. Riesgo: drift entre fases custom del adopter y dimensiones core (resoluble con extensión también de `dimensions.md`).
- **Alternativas evaluadas**: SDLC fijo (rechazado por inflexibilidad — incompatible con goal-5); SDLC totalmente libre (rechazado por incoherencia entre adopters).
- **Capabilities relacionadas**: CAP-03 (templates por fase), CAP-08 (adopters extienden).

### ADR-latente-008 — Backlog emergente como query sobre status, no estructura persistente

- **Contexto**: Cómo modelar el "backlog" entre WAs `design` (output) y WAs `implementation` (input).
- **Decisión latente**: el backlog es **query**, no entidad — nodos del vault con `status: ready-for-implementation` constituyen el backlog. `/status` agrega la query. Sin estructura persistente nueva.
- **Consecuencias**: simplicidad operativa — un solo campo (`status`) gobierna el lifecycle. Limitación: query es O(N) sobre archivos del vault; aceptable hasta cientos de nodos, degrada con miles (Ford fitness function a vigilar). Ousterhout information hiding aplicado: los WAs no necesitan saber cómo se construye el backlog, solo que existe.
- **Alternativas evaluadas**: backlog persistente en archivo único (rechazado por single point of mutation + ground-truth distribuido en archivos); base de datos (rechazado por no git-native); índice cacheado (pendiente — viable optimización futura).
- **Capabilities relacionadas**: CAP-01 (status del grafo), CAP-03 (consumo desde WAs implementation).

### ADR-latente-009 — Tres checkpoints uniformes del WA lifecycle (discovery review / step checkpoint / sign-off)

- **Contexto**: Cómo aplicar verificación multi-rol sin sobrecarga y sin gaps. Necesidad de captura de drift bottom-up y top-down.
- **Decisión latente**: 3 checkpoints uniformes — (1) discovery review al crear WA (top-down: discovery colaborativa antes de comprometer scope), (2) step checkpoint post-step (bottom-up: captura drift dentro de un step de delay), (3) sign-off al `/verify` (cierre: veredicto final). Mismo mecanismo (scope-scan flat parallel) en los 3.
- **Consecuencias**: cobertura predecible. Coste de tokens conocido (~$1.5-2 por WA con prompt caching). Adopters tienen modelo conceptual claro. Limitación: 3 checkpoints son obligatorios; en triviales puede ser overkill (decisión: outcome-type `trivial` los omite).
- **Alternativas evaluadas**: solo sign-off (rechazado por late detection — drift acumulado); checkpoints variables por outcome-type (rechazado por incoherencia + complejidad).
- **Capabilities relacionadas**: CAP-04 (mecanismo central).

### ADR-latente-010 — Algoritmo declarativo `verifiers = {custodian(d) : d ∈ dimensions-affected}`

- **Contexto**: Cómo derivar los verificadores requeridos al cierre de un WA. Necesidad de coherencia con dimensiones declaradas, sin lógica imperativa.
- **Decisión latente**: algoritmo único declarativo — los verificadores son la unión de custodios de las dimensiones afectadas. Resultado: cada WA tiene `verifiers-required` derivable mecánicamente desde `dimensions-affected` + `dimensions.md`.
- **Consecuencias**: simplicidad + auditabilidad. Limitación crítica: si `dimensions-affected` está mal declarado (mecánico, no honesto), el algoritmo infra-cubre verificación. Mitigación: scope-scan flat parallel detecta dimensiones; filtro PO (Cagan strong PM) valida — Gap 6 del WA-002 documenta este mecanismo.
- **Alternativas evaluadas**: lista imperativa por outcome-type (rechazado — duplica conocimiento ya en `dimensions.md`); verificación manual por orchestrator (rechazado — propenso a error).
- **Capabilities relacionadas**: CAP-04 (algoritmo central), CAP-01 (dimensions catalog como ground truth).

**Procesamiento futuro**: estos 10 ADRs latentes deberían procesarse en WA dedicado orquestado por Architect (outcome-type `adr` × 10, posiblemente batch). NO escritos aquí — decisión cerrada con humano en WA-002.

---

## Coherence-evaluation final del grafo

Aplicación de skill `coherence-evaluation` sobre el catálogo de 10 capabilities + 10 ADRs latentes contra los nodos del grafo existentes.

### Comprobaciones realizadas

#### vs. vision (`vault/product-owner/strategy/vision.md`)

La visión declara: *"capa de agentes de IA que rodea el trabajo del ingeniero ... toda la traza viva del proyecto vive como contexto persistente y versionado ... sobre esa memoria operan múltiples agentes IA, uno por cada rol del proceso, custodios de dimensiones distintas, que se revisan cruzadamente cada decisión y cada artefacto antes de cerrarlo ... productos reales con ciclo de vida completo"*.

| Frase de la visión | Capability que la materializa |
|---|---|
| "traza viva del proyecto vive como contexto persistente y versionado" | CAP-01 |
| "múltiples agentes IA, uno por cada rol del proceso" | CAP-02 |
| "custodios de dimensiones distintas, que se revisan cruzadamente cada decisión" | CAP-04 |
| "productos reales con ciclo de vida completo" | CAP-03, CAP-07 |
| "absorbe el coste específico de trabajar con IA" | CAP-04, CAP-06 |
| "habilita el rigor multi-rol que antes requería un equipo de personas especializadas" | CAP-02, CAP-04, CAP-05 |
| (implícito — adopters externos) | CAP-08, CAP-09, CAP-10 |

**Resultado: coherente.** El catálogo cubre todas las frases significativas de la visión. Sin contradicciones detectadas.

#### vs. los 7 goals

Cross-check con tabla del extraction document:

| Goal | Capability ancla primaria | Cross-coverage |
|---|---|---|
| goal-1 (auto-sostenibilidad) | CAP-07 | CAP-03, CAP-06, CAP-02, CAP-08, CAP-10 |
| goal-2 (output auditable multirol) | CAP-01, CAP-04, CAP-05 | CAP-06, CAP-10 |
| goal-3 (absorción coste revisión) | CAP-06 | CAP-04, CAP-03, CAP-02 |
| goal-4 (rigor multirol individual) | CAP-02 | CAP-05, CAP-04, CAP-06 |
| goal-5 (portabilidad) | CAP-08, CAP-09 | CAP-07 |
| goal-6 (articulación pública) | CAP-10 | CAP-05, CAP-09 |
| goal-7 (ciclo vida producto) | CAP-03, CAP-01 | CAP-08, CAP-09, CAP-07 |

**Resultado: coherente.** Todos los goals tienen ≥1 capability ancla primaria + cross-coverage. Métricas controlables de los goals están cubiertas por al menos una capability operante. Goals aspiracionales (goal-5 número de adopters, goal-6 evaluadores externos) tienen base materializada (CAP-08 + CAP-09 + CAP-10).

#### vs. dimensions catalog (`vault/shared/governance/dimensions.md`)

Las 7 dimensiones core están declaradas: `product, technical, usability, business, security, quality, operations`. Cross-check con `dimensions-affected` honestos declarados en las 10 capabilities:

| Dimensión | Capabilities que la declaran |
|---|---|
| product | TODAS (10/10) — coherente: catálogo de producto |
| technical | CAP-01, CAP-02, CAP-03, CAP-04, CAP-06, CAP-07, CAP-08, CAP-09 (8/10) |
| usability | CAP-02, CAP-06, CAP-07, CAP-10 (4/10) |
| business | CAP-08, CAP-10 (2/10) |
| security | CAP-08, CAP-09 (2/10) |
| quality | CAP-04, CAP-05 (2/10) |
| operations | CAP-03, CAP-08 (2/10) |

**Resultado: coherente.** Las 7 dimensiones están representadas en al menos 2 capabilities (la menos cubierta es `business` y `security` con 2 cada una). El flag heredado "dimensions declaradas honestamente, no heredadas mecánicamente del goal padre" se cumple — varias capabilities (CAP-05 con `[product, quality]` no `[product]`; CAP-07 con `[product, technical, usability]`; CAP-08 con 5 dimensiones) reflejan análisis real, no mecánico.

#### vs. role-catalog (`vault/shared/governance/role-catalog.md`)

8 roles core (6 asesores + 2 ejecutores). Cada dimensión tiene custodio asignado. Cross-check:

- Para cada `dimensions-affected` de una capability, existe custodio en `role-catalog.md`: ✅ verificado para las 7 dimensiones.
- El algoritmo `verifiers = {custodian(d)}` aplicado a cada capability produce conjunto válido de verifiers existentes: ✅ verificado.
- CAP-02 referencia explícitamente los 8 roles core + `vault/developer/CLAUDE.md` pendiente (gap operativo declarado, no contradicción).

**Resultado: coherente.** Sin contradicciones con role-catalog.

#### vs. workflows.md (`vault/shared/governance/workflows.md`)

Cross-check con templates SDLC y outcome-types:

- CAP-03 ES el catálogo de workflows; coherente por construcción.
- CAP-07 ES el uso de templates en greenfield; coherente.
- CAP-08 (CLI `sem-ia validate/check/coverage`) extiende el modelo de validation pero no contradice templates.
- CAP-09 (`/adopt`) propone nuevo outcome-type futuro (`adopt` en fase nueva o `discovery` extendido) — declarado en notas operativas como decisión pendiente, no contradicción.
- Estados canónicos del nodo en workflows.md son consistentes con `status: draft` declarado por las skills + transición `draft → active` en `on-close` del WA-002.

**Resultado: coherente.** El catálogo de capabilities respeta la estructura de workflows.md. Las propuestas de extensión (gaps 1, 3, 4 del anexo WA-002) están **alineadas** con la filosofía declarada de extensibilidad del framework.

#### vs. repo-structure.md (`vault/shared/governance/repo-structure.md`)

Cross-check con la separación `vault/` (dogfooding) + `.claude/` (Claude Code) + `src/` (distribuible):

- Las 10 capabilities respetan la separación: capabilities operantes describen artefactos que viven en sus carpetas correctas (`.claude/agents/`, `vault/shared/governance/`, `vault/architect/research/library/`, etc.).
- CAP-08 declara explícitamente `src/adapters/`, `src/universal/`, `src/cli/` — coherente con la regla "framework distribuible vive en `src/`".
- CAP-09 declara que `derived-from` ya existe como campo opcional en workflows.md — coherente.
- La "regla de no-duplicación" de repo-structure.md está respetada: cada capability referencia su única fuente de verdad.

**Resultado: coherente.** Sin contradicciones con repo-structure.md.

#### vs. bootstrap-summary.md (decisiones del bootstrap)

Bootstrap-summary documenta 16 decisiones clave del bootstrap manual. Cross-check selectivo:

- "Adopción de Claude Code como harness primario" → ADR-latente-001 captura esta decisión implícita.
- "Vault role-first" → ADR-latente-002 captura.
- "Skills empaquetadas con SKILL.md + design.md" → ADR-latente-005 captura.
- "Frontmatter YAML + wiki-links" → ADR-latente-003 captura.
- "Separación src/ vs .claude/ vs vault/" → ADR-latente-006 captura.

**Resultado: coherente.** Los ADRs latentes aflorados son **trazables** a decisiones documentadas en bootstrap-summary.md. Hay alineamiento entre lo que el bootstrap construyó y lo que el catálogo declara como capabilities.

### Resultado global de coherence-evaluation

**El catálogo de 10 capabilities + 10 ADRs latentes es COHERENTE con vision, goals, governance docs (5) y repo-structure.**

Sin contradicciones detectadas que requieran arbitraje (3 opciones de la skill `coherence-evaluation`: descartar / modificar nivel superior / documentar excepción). El catálogo extiende el grafo de forma consistente con su filosofía declarada.

---

## Flags emergentes (para `/verify` del WA-002)

Flags que el Architect eleva al PO antes del `/verify` del WA-002. **Ninguno es bloqueante** para cerrar el WA, pero deben aparcarse para WAs futuros.

### Flag 1 (medium) — CAP-09 dimension-affected `business` potencialmente missing

- **Contexto**: Adopción retroactiva implica leer código del adopter, que puede tener licencia incompatible (GPL viral, proprietary). Derivar grafo a `vault/` SEM-IA con `derived-from` apuntando a código GPL puede contaminar el repo SEM-IA con licencia heredada.
- **Recomendación Architect**: añadir `business` a `dimensions-affected` de CAP-09 cuando se descomponga (feature-design dedicado) — Business Analyst custodia licensing del adopter.
- **Severidad**: medium. No bloquea CAP-09 hoy (es `planned`), bloquea cuando se construya. Aparcar.
- **Anclaje bibliográfico**: Bass `business` dimension; Cagan business-viability-risk.

### Flag 2 (medium) — Fitness functions Ford no declaradas formalmente

- **Contexto**: Varias capabilities declaran tradeoffs que son **candidatos a fitness functions** (Ford evolutionary architectures): query O(N) del backlog (CAP-01, CAP-03), cobertura de skills lazy load (CAP-05), drift entre `src/adapters/` y dogfooding (CAP-08), idempotencia del archeology walk (CAP-09), drift de governance docs (CAP-10).
- **Recomendación Architect**: cuando se descomponga cada capability en features, declarar fitness functions explícitas (test ejecutable + threshold). Sin fitness function, el tradeoff degrada silenciosamente.
- **Severidad**: medium. No bloquea WA-002, pero es **deuda técnica consciente** declarable. Aparcar como "gap-7" del anexo del WA-002 o como WA dedicado posterior.
- **Anclaje bibliográfico**: Ford et al. *Building Evolutionary Architectures* — fitness functions como protección contra architectural drift.

### Flag 3 (informational) — Terminología `separability` en CAP-04 no estándar Bass

- **Contexto**: CAP-04 declara QA `separability` para "verifier independence". No es término canónico Bass (Bass usa `independence` o `decoupling`).
- **Recomendación Architect**: en `/verify` o WA futuro de doc-edit, sustituir `separability` por `independence` o `verifier-independence` (term explícito).
- **Severidad**: informational. Cosmético. No impide entender la capability.
- **Anclaje bibliográfico**: Bass *Software Architecture in Practice* — vocabulario canónico de QAs.

### Flag 4 (informational) — ADRs latentes deben procesarse pronto (recomendación de orden)

- **Contexto**: Los 10 ADRs latentes son decisiones arquitectónicas significativas ya tomadas implícitamente. Cuanto más tiempo pasen sin escribirse formalmente, mayor riesgo de drift implícito (alguien refactoriza el bootstrap sin saber que existe decisión).
- **Recomendación Architect**: priorizar el WA dedicado de ADRs (Architect orquestador, outcome-type `adr` × 10 o batch) antes de los WAs de features de CAP-08/CAP-09 — los ADRs latentes son inputs de esas capabilities `planned`.
- **Severidad**: informational. Recomendación de roadmap.
- **Anclaje bibliográfico**: Nygard *Documenting Architecture Decisions* — ADRs deben escribirse cerca del momento de la decisión, no años después.

---

## Notas para QA (step-4)

Step-4 verificará verificabilidad — cada capability debe tener criterio observable auditable en futuros `/verify` de features descompuestas. Notas del Architect para QA:

1. **Sección "Criterio observable para futuros /verify"** está presente en las 10 capability files. QA debe verificar que cada criterio es **auditable** (no aspiracional, no subjetivo). Architect ha revisado y considera que los 10 criterios son testables. Casos a vigilar:
   - CAP-06 declara "tiempo aceptable (esperable < 2s)" para `/status` — verificable con timing test.
   - CAP-08 / CAP-09 son `planned`; criterios observables declaran "cuando sea operant". QA debe validar que el criterio será aplicable al pasar a `operational-status: operant`.
   - CAP-05 menciona "skills se invocan en el contexto que su `description` declara" — QA puede verificar este criterio con casos test de matching de description (probabilístico, no determinístico — Ford fitness function candidata).

2. **AC traceability** (`// @ac-coverage:`) es **cross-cutting** — declarado en CAP-04 como tactic operativa, no como capability propia. QA debe verificar que el criterio observable de CAP-04 incluye AC traceability cuando se descomponga.

3. **Fitness functions** (flag 2 emergente): QA puede recomendar al PO que cada capability futura tenga fitness function declarada al descomponerse en features. Sin esto, los tradeoffs declarados degradan silenciosamente.

4. **`vault/developer/CLAUDE.md`** pendiente (gap de CAP-02): QA debe decidir si esto bloquea verificabilidad de CAP-02 hoy o se aparca. Architect recomienda **aparcar** — CAP-02 declara explícitamente el gap como conocido sin bloquear `operational-status: operant`.

5. **Framework regression detection** (flag QA aparcado en notes de CAP-04): QA debe confirmar que la decisión de no añadirlo como capability planned hoy se mantiene. Si se reabre, sería capability nueva (no feature de CAP-04).

---

## Resumen ejecutivo

- **10 capabilities aprobadas** desde viability técnica. 8 con `operational-status: operant`, 2 con `planned` (CAP-08, CAP-09) — éstas requieren ADRs reales + threat-model formal antes de pasar a feature-design.
- **10 ADRs latentes aflorados** del bootstrap, ninguno escrito. Procesamiento en WA dedicado posterior (Architect orquestador recomendado).
- **Coherence-evaluation: coherente** contra vision, 7 goals, 5 governance docs, repo-structure, bootstrap-summary. Sin contradicciones que requieran arbitraje.
- **4 flags emergentes** para el PO: 2 medium (CAP-09 business dimension, fitness functions Ford), 2 informational (terminología separability, orden de ADRs).
- **Anclaje bibliográfico aplicado**: Bass (QAs + tactics + tradeoffs), Ford (fitness functions + appropriate coupling + evolvability), Ousterhout (deep modules + information hiding), Martin (Dependency Rule + boundaries + adapter pattern), Nygard (ADR format + supersession), Shostack (threat-modeling para CAP-09).

El catálogo está listo para que QA verifique verificabilidad en step-4. `/verify` del WA-002 puede ejecutarse al cierre con los 5 verificadores (PO, Architect, Designer, Business-analyst, QA) sin bloqueantes desde el ángulo Architect.
