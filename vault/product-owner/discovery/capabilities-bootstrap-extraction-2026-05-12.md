---
type: discovery
id: capabilities-bootstrap-extraction-2026-05-12
title: "Extracción bottom-up de capabilities desde el bootstrap construido"
status: active   # transición aplicada por /verify del WA wa-2026-05-12-002 el 2026-05-12T05:30+02:00
created: 2026-05-12
author: product-owner
related-wa: wa-2026-05-12-002
related-vision: vision
related-goals: [goal-1-auto-sostenibilidad, goal-2-output-auditable-multirol, goal-3-absorcion-coste-revision, goal-4-rigor-multirol-individual, goal-5-portabilidad, goal-6-articulacion-publica, goal-7-ciclo-vida-producto]
references:
  - vault/shared/sessions/archive/wa-2026-05-12-001.md
  - vault/product-owner/discovery/capabilities-derivation-2026-05-12.md
  - vault/architect/research/bootstrap-summary.md
  - README.md
  - src/README.md
bibliography:
  - Ford et al. — Building Evolutionary Architectures (architectural drift detection)
  - Christensen — Jobs-To-Be-Done (jobs reales del sistema)
  - Cagan — Inspired + Empowered (4 risks, strong product team)
  - Bass — Software Architecture in Practice (QAs por capability)
  - Nygard — ADRs (latentes detectables sin escribir)
---

# Extracción bottom-up de capabilities desde el bootstrap construido

## Contexto

Este documento es el output del **step-1 del WA `wa-2026-05-12-002`**. Aplica approach **bottom-up reverse-engineering**: leer el bootstrap construido (`.claude/`, `vault/shared/governance/`, CLAUDE.md raíz + wrappers, README.md raíz, `src/README.md`, `bootstrap-summary.md`), agrupar las piezas por jobs/habilidades observables, y declarar las capabilities operantes que emerjan.

**Decisión clave** (cerrada con humano): el catálogo refleja **lo operante + lo planeado con flag** `operational-status: operant | planned`. Las pendientes documentadas en README (architecture-archeology, distribución `@sem-ia/cli`, etc.) entran como capabilities con estado `planned` — la propuesta integral del framework es visible, no solo lo construido.

**Cross-reference con WA-001 abortado:** la derivación top-down sobre goal-1 produjo 4 candidatas (g1-A/B/C/D). Este documento las cruza al final como sanity check.

---

## Inventario del bootstrap agrupado por habilidades/jobs

### Job 1 — Grafo declarativo persistente del proyecto

Piezas que lo materializan:
- **`vault/`** — organización role-first (8 directorios de rol + `shared/`).
- **`vault/shared/governance/repo-structure.md`** — modelo conceptual del repo (vault + .claude + src).
- **`vault/shared/governance/dimensions.md`** — 7 dimensiones core (product, technical, usability, business, security, quality, operations) + custodios.
- **Frontmatter YAML obligatorio** en todo nodo: `type`, `id`, `title`, `parent`, `also-relates-to`, `depends-on`, `dimensions-affected`, `related-adrs`, `status`.
- **Wiki-links `[[id]]`** en contenido para referencias internas.
- **Estados canónicos del nodo** declarados en CLAUDE.md raíz (`draft → ready-for-implementation → in-implementation → implemented + deprecated + superseded`).
- **Skill compartida `graph-cross-link-declaration`** — declara aristas del grafo.

### Job 2 — Operación multi-rol vía agentes IA homólogos

Piezas:
- **8 agent files** en `.claude/agents/*.md`: product-owner, architect, designer, business-analyst, security-officer, qa, developer, devops.
- **`vault/shared/governance/role-catalog.md`** — catálogo formal de roles + atajos npm + dimensión custodiada + Cagan risk.
- **7 wrappers `vault/<rol>/CLAUDE.md`** (developer pendiente).
- **`package.json`** con npm scripts: `sem`, `po`, `arch`, `des`, `biz`, `sec`, `qa`, `dev`, `ops`.
- **CLAUDE.md raíz** — guía estática + entrypoint de PO (`npm run sem`).
- **Mecanismo subagent vía Task tool** — cualquier rol puede invocar a otros para meetings/give-and-take.

### Job 3 — Coordinación de trabajo vía Working Agreements indexados por fase SDLC

Piezas:
- **`vault/shared/governance/workflows.md`** — 14 templates por fase SDLC (discovery/design/implementation/operations/meta) con outcome-type + default-steps + consumes + on-close.
- **Estructura inline de WA** declarada en CLAUDE.md raíz (frontmatter + steps + scope + on-close + closure-criteria).
- **Slash `/wa`** — detalle del WA activo.
- **Backlog emergente** como query sobre `status: ready-for-implementation`.
- **Estados canónicos del WA** (`active` mientras tiene steps pendientes → archivado al `/verify`).
- **Protocolo de handoff explícito step→step** declarado en cada agent file.

### Job 4 — Verificación multi-rol cruzada en checkpoints uniformes

Piezas:
- **Slash `/scope-scan "<propuesta>"`** — flat parallel multi-rol (6 asesores en paralelo).
- **Slash `/verify`** — matriz declarativa `verifiers = {custodian(d) : d ∈ dimensions-affected}`.
- **Tres checkpoints uniformes** del lifecycle del WA: discovery review (al crear) · step checkpoint (post-step) · sign-off (al verify).
- **`vault/shared/governance/verification-matrix.md`** — guía orientativa.
- **Skill `capability-viability-review`** (Architect).
- **Skill `feature-viability-review`** (Architect).
- **Skill `coherence-evaluation`** (Architect).
- **Skill `coupling-detection`** (Architect).
- **Skill `threat-modeling`** (Security Officer).
- **Skills `*-quality-check`** (PO: vision, goal, capability, feature).
- **Give-and-take mid-step** vía Task tool (Cagan principio 2).

### Job 5 — Anclaje bibliográfico auditable mediante skills empaquetadas

Piezas:
- **18 notas bibliográficas** en `vault/architect/research/library/` (Cagan, Sinek, Rumelt, Doerr, Doran, Torres, Christensen, Patton, Cohn, Adzic, Bass, Ford, Nygard, Martin, Ousterhout, Anthropic skills+subagents).
- **`vault/architect/research/library/INDEX.md`** — índice de bibliografía.
- **14 skills construidas** en `.claude/skills/<rol>/<skill>/SKILL.md` + `design.md`:
  - PO estratégicas (4): vision-quality-check, goal-quality-check, capability-derivation, capability-quality-check.
  - PO operativas (3): feature-decomposition, spec-writing, feature-quality-check.
  - Architect (5): adr-writing, capability-viability-review, coherence-evaluation, coupling-detection, feature-viability-review.
  - Security-officer (1): threat-modeling.
  - Shared (1): graph-cross-link-declaration.
- **`.claude/skills/_pending-later.md`** — 10+ skills documentadas como pendientes.
- **Carga perezosa nativa** (Claude Code Agent Skills).

### Job 6 — Visibilidad operativa del estado y progreso del proyecto

Piezas:
- **Slash `/status`** — snapshot del proyecto (WAs por track Dual, backlog, subgrafo, features por status, ADRs).
- **Slash `/wa`** — detalle del WA activo.
- **Slash `/sessions`** — modos de trabajo + atajos.
- **Ritual de inicio del PO** declarado en agent file y wrapper `vault/product-owner/CLAUDE.md` (lee strategy/, sessions/active/, specs/, adrs/, governance/ + presenta panorámica).
- **Progreso entry** en cada WA (handoff explícito + audit-ready).
- **Dual Track Discovery/Delivery** explicitado en CLAUDE.md raíz y workflows.md.

### Job 7 — Inception greenfield protocol-compliant desde vault vacío

Piezas:
- **PO Modo 1 (Entrada al sistema)** declarado en agent file con protocolo de 10 pasos.
- **Cadena de WAs por gaps detectados** declarada en workflows.md (vision-creation → goal-definition × N → capability-creation × M → feature-design × K).
- **Templates uniformes greenfield/maduro** — los mismos workflows.md sirven en ambas fases.
- **`vault/<rol>/CLAUDE.md` wrappers** + atajos npm — entrada directa por dominio si la propuesta no es de PO.

### Job 8 — Portabilidad multi-harness y distribución como `@sem-ia/cli` [PLANNED]

Piezas previstas (esqueleto en `src/`):
- **`src/adapters/claude-code/`** — bundled `.claude/` + CLAUDE.md raíz formato Claude Code (futuro: opencode/, pi/).
- **`src/universal/`** — vault skeleton + schemas JSON + governance defaults independientes de harness.
- **`src/cli/`** — bin scripts (`sem-ia init`, `validate`, `check`, `coverage`).
- **`package.json`** publicable a npm como `@sem-ia/cli`.
- **`src/README.md`** documenta la estructura y el modelo de "build step" desde adapters al dogfooding actual.

Estado actual: esqueleto vacío en `src/`. Documentación operativa en `src/README.md` + `README.md` raíz.

### Job 9 — Adopción retroactiva desde proyecto pre-existente [PLANNED, P1]

Piezas previstas (nada construido):
- **Slash `/adopt <ruta>`** — comando para arrancar adopción retroactiva.
- **Template `adopt`** en nueva fase SDLC `adoption`.
- **Skill `architecture-archeology`** (Architect) — walk de código, inventario módulos, boundaries, acoplamientos, decisiones técnicas implícitas candidatas a ADR retroactivo.
- **Modo "lectura" en skills existentes** (`spec-writing`, `feature-decomposition`, `capability-derivation`) — leen artefactos pre-existentes en lugar de conversar.
- **Campo `derived-from` en frontmatter** (declarado en workflows.md como opcional futuro).

Estado actual: solo documentado en README.md sección "Pendientes — capability 'Adopción retroactiva'".

### Job 10 — Articulación pública del framework para audiencias externas

Piezas:
- **`README.md` raíz** (65 KB) — onboarding completo del framework.
- **`CLAUDE.md` raíz** — guía estática + entry point.
- **`vault/architect/research/bootstrap-summary.md`** — historia + 16 decisiones clave + 8 lecciones del bootstrap.
- **`vault/shared/governance/*.md`** — 5 docs canónicos (dimensions, role-catalog, workflows, verification-matrix, repo-structure).
- **`vault/architect/research/library/`** — 18 notas bibliográficas + INDEX.
- **`LICENSE`** Apache 2.0 (sin riesgo viral; permite distribución comunitaria + fork comercial).
- **`propuesta-prefacio.pdf`** — propuesta inicial archivada.

---

## Las 10 capabilities operantes extraídas

Para cada capability: enunciado JTBD-style + parent + cross-goals + dimensions honestas + operational-status + jobs/piezas que la materializan.

### CAP-A · Grafo declarativo persistente del proyecto

- **Enunciado:** *El sistema mantiene todo el contexto del proyecto (visión, goals, capabilities, features, stories, specs, ADRs, audits, learnings) como grafo dirigido versionado en git, con espina dorsal jerárquica `vision → goals → capabilities → features → stories → specs` y cross-links explícitos (`parent`, `also-relates-to`, `depends-on`, `dimensions-affected`, `related-adrs`) declarados en frontmatter YAML de cada nodo, más wiki-links `[[id]]` en contenido.*
- **Parent goal:** goal-2 (output auditable, coherente y verificado multi-rol — métrica "100% nodos con cross-links coherentes").
- **Cross-goals:** goal-7 (ciclo de vida con estados canónicos), goal-1 (auto-sostenibilidad: el grafo ES la memoria persistente), goal-4 (rigor: cobertura sin perder coherencia).
- **Dimensions honest:** `product`, `technical` (decisión arquitectónica con QAs Bass: modificabilidad + auditabilidad + analyzability).
- **Operational-status:** `operant`.
- **Jobs/piezas que la materializan:** Job 1 entero.

### CAP-B · Operación multi-rol vía agentes IA homólogos especializados

- **Enunciado:** *El sistema provee 8 roles core como agentes IA con identidad bibliográfica anclada y vault scope declarado: 6 asesores custodios de dimensión (product-owner, architect, designer, business-analyst, security-officer, qa) + 2 ejecutores (developer, devops). El humano alterna sesiones por rol vía atajos npm (`npm run sem|arch|des|biz|sec|qa|dev|ops`). Cada rol es también invocable como subagente vía Task tool para meetings, scope-scans, checkpoints y give-and-take mid-step (Cagan principio 2).*
- **Parent goal:** goal-4 (sostener rigor multi-rol con humano individual — métrica "100% cobertura dimensional en features").
- **Cross-goals:** goal-1 (auto-sostenibilidad: dogfooding con roles propios), goal-2 (verificación cruzada), goal-3 (absorción coste: el humano valida en vez de descubrir).
- **Dimensions honest:** `product`, `technical` (mecanismo de agent files + wrappers CLAUDE.md jerárquico + carga prompt cache).
- **Operational-status:** `operant` (7 wrappers construidos; `vault/developer/CLAUDE.md` pendiente — gap menor).
- **Jobs/piezas:** Job 2 entero.

### CAP-C · Coordinación de trabajo vía Working Agreements indexados por fase SDLC

- **Enunciado:** *El sistema conduce cada bloque de trabajo bajo un Working Agreement declarativo con `outcome-type`, `phase` SDLC, `steps` multi-rol, `scope-allowed/forbidden`, `closure-criteria` y `on-close` transitions. 14 templates por fase (discovery/design/implementation/operations/meta) capturan workflows enterprise en formato AI-ejecutable. El backlog emerge como query sobre nodos con `status: ready-for-implementation` (sin estructura persistente nueva). Handoff explícito step→step con entrada Progreso audit-ready.*
- **Parent goal:** goal-7 (sostener productos a escala con ciclo de vida completo — métrica "cobertura SDLC completo en templates").
- **Cross-goals:** goal-1 (≥90% desarrollo bajo WAs), goal-2 (verificación al cierre), goal-3 (handoff explícito absorbe el coste de "saber qué viene").
- **Dimensions honest:** `product`, `technical` (WA structure + workflow templates como mecanismo arquitectónico).
- **Operational-status:** `operant`.
- **Jobs/piezas:** Job 3 entero.

### CAP-D · Verificación multi-rol cruzada en checkpoints uniformes

- **Enunciado:** *El sistema aplica scope-scan flat parallel multi-rol en 3 checkpoints uniformes del lifecycle del WA: (1) discovery review al crear WA, (2) step checkpoint post-step, (3) sign-off al `/verify`. Algoritmo declarativo `verifiers = {custodian(d) : d ∈ dimensions-affected}`. Cubre los 4 risks de Cagan (value, usability, viability technical, business viability) + transversales (security, quality, operations). Soporta give-and-take mid-step vía subagentes — el rol activo invoca a otros cuando emerge duda relevante a otro dominio.*
- **Parent goal:** goal-2 (output auditable + verificado multi-rol — métrica "100% WAs cerrados con verificación multi-rol completa").
- **Cross-goals:** goal-3 (≥80% drift detectado pre-cierre vs post-cierre), goal-4 (cobertura cross-roles que un humano individual no puede dar solo).
- **Dimensions honest:** `product`, `quality` (cobertura cross-roles), `technical` (mecanismo via Task tool + slash commands).
- **Operational-status:** `operant`.
- **Jobs/piezas:** Job 4 entero.

### CAP-E · Anclaje bibliográfico auditable mediante skills empaquetadas y biblioteca canónica

- **Enunciado:** *Cada decisión significativa del sistema (identidad de rol, skill aplicada, template de workflow, veredicto de verificación) cita su fuente bibliográfica auditable. 18 notas en `vault/architect/research/library/` (Cagan, Sinek, Rumelt, Doerr, Doran, Torres, Christensen, Patton, Cohn, Adzic, Bass, Ford, Nygard, Martin, Ousterhout, Anthropic). 14 skills construidas empaquetan happy-paths bibliográficos auditables como `SKILL.md` (operativo) + `design.md` (referencia). Carga perezosa nativa de Claude Code: la skill se invoca cuando el contexto matchea su `description`. 10+ skills documentadas como pendientes en `_pending-later.md` con su bibliografía ya identificada.*
- **Parent goal:** goal-2 (auditabilidad: cada decisión trazable a su autor/año).
- **Cross-goals:** goal-4 (rigor multi-rol descansa en bibliografía, no improvisación), goal-6 (validación académica refuerza con anclaje bibliográfico).
- **Dimensions honest:** `product`, `quality` (rigor por anclaje).
- **Operational-status:** `operant`.
- **Jobs/piezas:** Job 5 entero.

### CAP-F · Visibilidad operativa del estado y progreso del proyecto

- **Enunciado:** *El sistema provee al humano operador panorámica del estado del proyecto: subgrafo estratégico (visión + goals + capabilities), WAs activos agrupados por track (Discovery/Delivery/Operations/Meta vía Dual Track Cagan/Patton), backlog emergente, features por status, ADRs por status. Mecanismo: slash commands (`/status`, `/wa`, `/sessions`) + ritual de inicio del PO al arrancar sesión + entries de Progreso en cada WA. Aplica heurística Nielsen #1 (visibility of system status) y reduce friction de error recovery (Nielsen #9).*
- **Parent goal:** goal-3 (absorción coste revisión: humano valida estado conocido en vez de descubrirlo).
- **Cross-goals:** goal-1 (visibilidad pública del dogfooding), goal-2 (auditabilidad operativa), goal-4 (humano individual no se pierde alternando entre roles).
- **Dimensions honest:** `product`, `usability` (Nielsen #1 + #9), `technical` (mecanismo: slash commands + query sobre vault).
- **Operational-status:** `operant`.
- **Jobs/piezas:** Job 6 entero.

### CAP-G · Inception greenfield protocol-compliant desde vault vacío

- **Enunciado:** *El humano arranca un proyecto SEM-IA desde vault vacío vía `npm run sem`. El PO en Modo 1 (Entrada al sistema) detecta el estado del vault, propone cadena de WAs ordenada top-down (`vision-creation → goal-definition × N → capability-creation × M → feature-design × K`) usando los mismos workflow templates que en fase mature. Sin protocolos paralelos ni atajos ad-hoc. Convergencia inception ↔ dogfooding ↔ mantenimiento bajo los mismos templates indexados por fase SDLC.*
- **Parent goal:** goal-1 (auto-sostenibilidad — métrica "inception desde vault vacío sin intervención manual al protocolo").
- **Cross-goals:** goal-5 (adopters externos greenfield), goal-7 (inception es la primera fase del ciclo de vida).
- **Dimensions honest:** `product`, `technical` (workflows uniformes como mecanismo), `usability` (DX del PO conduciendo inception).
- **Operational-status:** `operant`.
- **Jobs/piezas:** Job 7 entero.

### CAP-H · Portabilidad multi-harness y distribución como `@sem-ia/cli` [PLANNED]

- **Enunciado:** *El framework es portable entre harnesses (Claude Code v1, OpenCode/Pi futuros) y distribuible vía npm como `@sem-ia/cli`. Adopter ejecuta `npx sem-ia init --harness=<X>` y recibe estructura conforme (`.claude/` o equivalente + vault skeleton + governance defaults + CLAUDE.md). CLI provee bin scripts ergonómicos: `init`, `validate` (frontmatter contra schemas JSON), `check` (integridad de cross-links del grafo), `coverage` (AC ↔ tests). Adapters por harness hacen el "render" del contenido universal al formato del harness destino.*
- **Parent goal:** goal-5 (portabilidad entre harnesses y proyectos — métrica controlable "adapter Claude Code funcional y publicado como @sem-ia/cli").
- **Cross-goals:** goal-1 (adopters arrancan greenfield con el mismo protocolo), goal-7 (ciclo vida producto en proyectos externos).
- **Dimensions honest:** `product`, `technical`, `operations` (packaging + distribución + build step).
- **Operational-status:** `planned` (esqueleto vacío en `src/`, documentación en `src/README.md` + sección "Pendientes" del README raíz).
- **Jobs/piezas:** Job 8.

### CAP-I · Adopción retroactiva desde proyecto pre-existente [PLANNED]

- **Enunciado:** *El sistema permite a un equipo con proyecto a medias (código + docs ya existentes, sin vault) llevar el proyecto a SEM-IA derivando el grafo retroactivamente. Mecanismo (pendiente): slash `/adopt <path>` + skill `architecture-archeology` (Architect walk de código → inventario módulos/boundaries/coupling → ADRs retroactivos candidatos) + modo "lectura" en skills existentes (leen artefactos en lugar de conversar) + campo `derived-from` en frontmatter para trazabilidad de derivación retroactiva.*
- **Parent goal:** goal-5 (portabilidad a tipos de proyecto: greenfield + existing — el README explícitamente cita ambos).
- **Cross-goals:** goal-6 (adopters externos refuerzan articulación pública), goal-7 (ciclo de vida producto para proyectos no-greenfield maduros).
- **Dimensions honest:** `product`, `technical` (archaeología de código).
- **Operational-status:** `planned` (P1 del README, nada construido).
- **Jobs/piezas:** Job 9.

### CAP-J · Articulación pública del framework para audiencias externas (técnicas y académicas)

- **Enunciado:** *El framework está articulado y publicado para audiencias externas: comunidad técnica + evaluadores académicos. Documentación completa versionada en repo público: README.md raíz (onboarding completo), CLAUDE.md raíz (guía estática), bootstrap-summary.md (historia + decisiones + lecciones), governance docs (5 archivos canónicos), library bibliográfica (18 notas con INDEX). LICENSE Apache 2.0 (sin riesgo viral; permite fork comercial + distribución comunitaria). Soporta validación académica (deadlines GISF 2026-05-25, TFM) + adopción por comunidad técnica.*
- **Parent goal:** goal-6 (articulación pública y validación académica — métricas controlables "README + bootstrap-summary + governance docs públicos" + "trabajos académicos del máster entregados a tiempo").
- **Cross-goals:** goal-5 (adopters externos requieren articulación pública), goal-1 (transparencia del dogfooding refuerza la tesis), goal-2 (docs son evidencia de auditabilidad).
- **Dimensions honest:** `product`, `business` (compliance académico + LICENSE).
- **Operational-status:** `operant`.
- **Jobs/piezas:** Job 10 entero.

---

## Mapping capability ↔ goal(s) padre

| Capability | Goal padre primario | Cross-goals | Estado |
|---|---|---|---|
| CAP-A · Grafo declarativo persistente | goal-2 | goal-7, goal-1, goal-4 | operant |
| CAP-B · Operación multi-rol via agentes homólogos | goal-4 | goal-1, goal-2, goal-3 | operant |
| CAP-C · Coordinación vía Working Agreements + SDLC | goal-7 | goal-1, goal-2, goal-3 | operant |
| CAP-D · Verificación multi-rol cruzada en checkpoints | goal-2 | goal-3, goal-4 | operant |
| CAP-E · Anclaje bibliográfico via skills + library | goal-2 | goal-4, goal-6 | operant |
| CAP-F · Visibilidad operativa del estado y progreso | goal-3 | goal-1, goal-2, goal-4 | operant |
| CAP-G · Inception greenfield protocol-compliant | goal-1 | goal-5, goal-7 | operant |
| CAP-H · Portabilidad multi-harness y `@sem-ia/cli` | goal-5 | goal-1, goal-7 | planned |
| CAP-I · Adopción retroactiva desde proyecto pre-existente | goal-5 | goal-6, goal-7 | planned |
| CAP-J · Articulación pública del framework | goal-6 | goal-5, goal-1, goal-2 | operant |

### Cobertura de los 7 goals (todos tienen ≥1 capability ancla)

| Goal | Primary | Cross |
|---|---|---|
| goal-1 (auto-sostenibilidad) | CAP-G | CAP-C, CAP-F, CAP-B, CAP-J, CAP-H |
| goal-2 (output auditable multirol) | CAP-A, CAP-D, CAP-E | CAP-F, CAP-J |
| goal-3 (absorción coste revisión) | CAP-F | CAP-D, CAP-C, CAP-B |
| goal-4 (rigor multirol individual) | CAP-B | CAP-E, CAP-D, CAP-F |
| goal-5 (portabilidad) | CAP-H, CAP-I | CAP-G |
| goal-6 (articulación pública) | CAP-J | CAP-E, CAP-I |
| goal-7 (ciclo vida producto) | CAP-C, CAP-A | CAP-H, CAP-I, CAP-G |

---

## Cross-check con candidatas top-down del WA-001 abortado

El WA-001 (top-down) derivó 4 candidatas sobre goal-1 antes del pivot:

| Candidata top-down (WA-001) | Mapping con catálogo bottom-up | Veredicto |
|---|---|---|
| **g1-A** "Inception greenfield protocol-compliant" | **= CAP-G** | ✅ Match exacto. Confirma coherencia top-down ↔ bottom-up. |
| **g1-B** "Bootstrap manual auditado con línea de transición a self-hosting" | **NO es capability del producto** — es metadata histórico ya documentado en `vault/architect/research/bootstrap-summary.md` | ✅ Descartar como capability separada. El bootstrap-summary cubre la trazabilidad histórica. |
| **g1-C** "Operación del protocolo con coste marginal bajo" | **Propiedad transversal emergente** de CAP-C + CAP-F + CAP-D (slash commands + scope-scan automático + degradación gradual en triviales) | ✅ Descartar como capability separada. Es propiedad de calidad/DX, no habilidad diferenciada. |
| **g1-D** "Visibilidad operativa del estado y cumplimiento de auto-sostenibilidad" | **= CAP-F** | ✅ Match exacto. Confirma coherencia. |

**Conclusión cross-check**: 2 de las 4 candidatas top-down se confirman con match exacto en el catálogo bottom-up (CAP-G y CAP-F). Las otras 2 eran metadata histórico (g1-B) o propiedad transversal emergente (g1-C), no capabilities propias. El catálogo bottom-up es **más completo** (10 capabilities cubren los 7 goals) sin contradecir lo derivado top-down sobre goal-1.

---

## Breakdown operational-status

- **8 capabilities operant** (CAP-A, B, C, D, E, F, G, J) — son lo que SEM-IA YA hace observablemente. Materializadas en piezas técnicas construidas (agents + skills + commands + governance + docs públicos).
- **2 capabilities planned** (CAP-H, I) — pendientes documentadas en README. CAP-H tiene esqueleto en `src/` + documentación operativa; CAP-I está solo documentada conceptualmente.

Cobertura goal-by-goal: todos los 7 goals tienen ≥1 capability operante como ancla. CAP-H y CAP-I (planned) extienden la propuesta del framework hacia adopters externos y proyectos no-greenfield.

---

## Notas para step-2 (escritura formal capability files)

Al escribir los 10 capability files `vault/product-owner/strategy/cap-NN-<slug>.md`:

1. **Convención de IDs:** `cap-01-grafo-declarativo`, `cap-02-multirol-agentes`, ..., `cap-10-articulacion-publica`. Mapping letra→número:
   - CAP-A → cap-01-grafo-declarativo-persistente
   - CAP-B → cap-02-multirol-agentes-homologos
   - CAP-C → cap-03-working-agreements-sdlc
   - CAP-D → cap-04-verificacion-multirol-cruzada
   - CAP-E → cap-05-anclaje-bibliografico-skills
   - CAP-F → cap-06-visibilidad-operativa
   - CAP-G → cap-07-inception-greenfield
   - CAP-H → cap-08-portabilidad-multi-harness
   - CAP-I → cap-09-adopcion-retroactiva
   - CAP-J → cap-10-articulacion-publica

2. **Estructura del frontmatter** (gap G2 del anexo del WA — voy a declararla aquí; al procesar gaps después se formalizará en `capability-derivation/SKILL.md`):
   - `type: capability`
   - `id`
   - `title`
   - `parent` (goal-id primario)
   - `also-relates-to` (lista cross-goals)
   - `depends-on` (otras capabilities si aplica)
   - `dimensions-affected` (lista honesta)
   - `related-adrs` (vacío hoy; latentes se afloran en step-3 sin escribir)
   - `status: draft` (la transición a `active` la aplica `/verify` al cierre)
   - `operational-status: operant | planned` (improvisación declarada — gap G2 del anexo)
   - `qas-bass` (quality attributes Bass implicados)
   - `tactics` (Bass)
   - `tradeoffs` (Bass)
   - `jtbd-outcome` (Christensen — outcome del job que cumple)
   - `fundamento-bibliografico` (autores citados)

3. **AC de legibilidad GISF** (heredado del scope-scan business-analyst del WA-001): cada capability file articula su enunciado y QAs/tactics en lenguaje accesible a evaluador no-practicante de SEM-IA.

4. **Aplicar `capability-quality-check`** a cada capability antes de marcarla finalizada (6 tests: habilidad vs feature/actividad · parent claro · sirve a guiding policy · distinta · cross-links · decomponible en 2-5 features).
