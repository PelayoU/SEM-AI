<!--
type: readme-raiz
materializes-feature: [feature-041-readme-onboarding, feature-044-glosario-publico, feature-045-ruta-lectura-audiencia, feature-010-entry-point-por-rol]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): README como onboarding completo del framework.
# - feature-041 (README como onboarding — tesis + modelo conceptual + atribución bibliográfica + cautelas privacy)
# - feature-044 (referencia al glosario público — pendiente artefacto físico)
# - feature-045 (sección "Cómo leer este repo" con ≥3 rutas por audiencia — pendiente artefacto físico)
# - feature-010 (tabla rol → atajo npm)
-->

# SEM-IA

> **Software Engineering Management framework para desarrollo asistido por IA.** Codifica los workflows que las empresas ya practican (SDLC, governance, approval matrices) en formato AI-ejecutable, con disciplina de roles, scope auditable y verificación cruzada.

Este README es el **onboarding** del repo: si entras por primera vez, léelo de arriba abajo para entender qué hay y cómo funciona todo.

---

## Tabla de contenidos

1. [Qué es SEM-IA](#qué-es-sem-ia)
2. [Quick start](#quick-start)
3. [Estructura del repo](#estructura-del-repo)
4. [Conceptos clave](#conceptos-clave)
5. [`.claude/` — runtime de Claude Code](#claude--runtime-de-claude-code)
6. [`vault/` — grafo declarativo del proyecto](#vault--grafo-declarativo-del-proyecto)
7. [`src/` — framework distribuible](#src--framework-distribuible)
8. [Working Agreement (WA) — anatomía completa](#working-agreement-wa--anatomía-completa)
9. [Workflow templates](#workflow-templates)
10. [Slash commands](#slash-commands)
11. [Cómo extender SEM-IA (para adopters)](#cómo-extender-sem-ia-para-adopters)
12. [`CLAUDE.md` raíz](#claudemd-raíz)
13. [Otros archivos en raíz](#otros-archivos-en-raíz)
14. [Estado del proyecto](#estado-del-proyecto)

---

## Qué es SEM-IA

SEM-IA es un framework para gestionar proyectos de software construidos con IA. Provee la **infraestructura de gobernanza** para que la IA opere bajo las reglas que tu empresa ya practica.

**Insight central:** las empresas ya tienen workflows (qué pasa cuando se añade una feature, qué pasa cuando se cambia auth, qué pasa cuando se hace un refactor). SEM-IA no inventa esos workflows — los codifica en formato declarativo que la IA puede ejecutar con disciplina de roles + verificación auditable.

**Lo que las empresas YA tienen:**
- Roles + responsabilidades.
- Procedimientos del rol (SOPs).
- Workflows por tipo de cambio.
- Matriz de aprobaciones.
- Project management coordinando flow.
- Tickets / charters de trabajo.
- Outputs documentales.

**Lo que SEM-IA aporta:**
- Roles → **agent files** (`.claude/agents/<rol>.md`).
- SOPs → **skills** (`.claude/skills/<rol>/<skill>/`).
- Workflows → **templates** (`vault/shared/governance/workflows.md`).
- Matriz de aprobaciones → **dimensions** + **verification matrix** + algoritmo formal.
- PM → **PO extendido en modo recepción** (sesión `npm run sem` o `npm run po`). El `CLAUDE.md` raíz es guía estática del proyecto, no carga identidad.
- Tickets / charters → **Working Agreements (WAs)** declarativos.
- Outputs → **nodos del vault** (markdown con frontmatter).

---

## Quick start

### Arrancar
```bash
cd /path/to/SEM-AI
npm run sem        # alias de `cd vault/product-owner && claude` — abre sesión PO en modalidad recepción
```
Eso carga la **sesión Product Owner extendido en modalidad recepción** (Modo 1 — Entrada al sistema): el PO ejecuta ritual de inicio (lee el vault: visión, goals, capabilities, WAs activos, backlog), te presenta panorámica del proyecto, y procesa tu propuesta clasificando outcome-type, convocando reunión de discovery (scope-scan multi-rol) y drafteando el WA.

### Atajos npm para sesiones dedicadas

Desde la raíz del repo, en lugar de hacer `cd vault/<rol> && claude` cada vez:

| Comando | Equivalente | Para qué |
|---|---|---|
| `npm run sem` | `cd vault/product-owner && claude` | PO en modalidad recepción (Entrada al sistema — alias literal de `npm run po`) |
| `npm run po` | `cd vault/product-owner && claude` | Sesión Product Owner extendido (estrategia + producto) |
| `npm run arch` | `cd vault/architect && claude` | Sesión Architect |
| `npm run des` | `cd vault/designer && claude` | Sesión Designer |
| `npm run biz` | `cd vault/business-analyst && claude` | Sesión Business Analyst |
| `npm run sec` | `cd vault/security-officer && claude` | Sesión Security Officer |
| `npm run qa` | `cd vault/qa && claude` | Sesión QA |
| `npm run dev` | `cd src && claude` | Sesión Developer |
| `npm run ops` | `cd vault/devops && claude` | Sesión DevOps |

Sin dependencias — solo Node (que ya tienes para Claude Code). `npm run` (sin argumento) lista los scripts disponibles. Si quieres un atajo más corto: `alias n='npm run'` y queda en `n po`, `n arch`, etc.

### Cómo entras al sistema

**Bootstrap orgánico**: cualquier estado del vault (vacío, parcial, maduro). Pides una feature/cambio. Recepción dispara scope-scan multi-rol; si hay gaps upstream (no hay capability, no hay goal, no hay visión), propone una cadena de WAs ordenada top-down. El grafo emerge orgánicamente conforme trabajas. Funciona igual para greenfield (cadena larga: visión → goals → capability → feature) que para proyecto maduro (cadena corta o WA único).

> **Nota**: una capability futura — *"Adopción retroactiva desde código pre-existente"* — automatizará el bootstrap del grafo desde un proyecto que ya tiene código sustancial. Hoy está pendiente (ver "Pendientes" al final).

### Pedir algo
> "Quiero diseñar feature de login con Google"

Recepción:
1. Clasifica `outcome-type: feature-design` (fase `design`).
2. Ejecuta scope-scan flat parallel (6 roles asesores en paralelo: po, architect, designer, business-analyst, security-officer, qa).
3. Carga workflow template de `feature-design`.
4. Adapta steps según scope-scan (mantiene/quita opcionales).
5. Te propone WA con steps. Confirmas.
6. Crea WA en `vault/shared/sessions/active/`.
7. Te indica: *"Step 1 pending para product-owner. Abre: `npm run po`"*.

### Ejecutar steps
Sigues el handoff de step en step:
- `npm run po` → PO conduce step 1 (decomposition + spec), te indica siguiente.
- `npm run arch` → Architect (si aplica) conduce viability + ADR opcional.
- `npm run sec` → Security (si aplica) conduce threat-model.
- ... hasta el último step.

### Cerrar el WA de design
Vuelves a raíz, ejecutas `/verify`. Recepción invoca verificadores en paralelo. Si aprueban, archiva el WA. La spec queda en `vault/product-owner/specs/feature-007.md` con `status: ready-for-implementation` — **entra al backlog**.

### Después: implementar
Cuando lo prioricemos (puede ser días o semanas después), abrimos un nuevo WA:
> "Implementar feature-007"

Recepción clasifica `outcome-type: feature-build` (fase `implementation`), verifica que `feature-007` existe con status correcto, drafta WA `developer → qa`, y ejecutamos. Al cerrar, la spec pasa a `status: implemented`.

---

## Estructura del repo

```
SEM-AI/
├── .claude/                 ← runtime de Claude Code (agents, skills, commands, settings)
├── vault/                   ← contenido del proyecto, organizado por rol custodio
├── src/                     ← framework distribuible (esqueleto hoy, futuro @sem-ia/cli)
├── CLAUDE.md                ← guía estática del proyecto (cargada al arrancar Claude Code al root — no define identidad de agente)
├── .gitignore
├── LICENSE
└── README.md                ← este archivo
```

**Tres carpetas reales** + archivos sueltos. Cada carpeta con un propósito claro:
- `.claude/` → lo que Claude Code descubre nativamente.
- `vault/` → contenido del proyecto SEM-IA (grafo declarativo + governance + research).
- `src/` → futuro paquete distribuible para que adopters lo instalen en sus propios proyectos.

---

## Conceptos clave

| Concepto | Qué es | Vive en |
|---|---|---|
| **Rol** | Identidad de un agente IA homólogo a un puesto en la empresa (PO extendido, Architect, Designer, Business Analyst, etc.) | `.claude/agents/<rol>.md` |
| **Skill** | Procedimiento auditable que un rol sabe ejecutar (escribir ADR, decomposition, etc.) | `.claude/skills/<rol>/<skill>/` |
| **Slash command** | Macro invocable desde el chat (`/wa`, `/status`, etc.) | `.claude/commands/<name>.md` |
| **Working Agreement (WA)** | Contrato declarativo de un bloque de trabajo, con outcome, dimensiones, steps, verificadores | `vault/shared/sessions/active/wa-N.md` |
| **Workflow template** | Plantilla de steps por outcome-type, indexada por fase SDLC, que recepción usa al draftar WAs | `vault/shared/governance/workflows.md` |
| **Fase SDLC** | Etapa del lifecycle (`discovery | design | implementation | operations | meta`) bajo la que vive un template | `vault/shared/governance/workflows.md` |
| **Nodo del vault** | Cualquier markdown con frontmatter del proyecto: vision, goal, capability, feature, story, spec, ADR, etc. | `vault/<rol>/<subdir>/<id>.md` |
| **Backlog** | Query emergente sobre nodos con `status: ready-for-implementation`. No es entidad persistente. | Derivado del vault, mostrado en `/status` |
| **Dimensión** | Eje del producto holístico (product, technical, usability, business, security, quality, operations — 7 dimensiones que mapean a los 4 risks de Cagan; `product` cubre el continuum estratégico + operativo) | `vault/shared/governance/dimensions.md` |
| **Custodio** | El rol responsable de una dimensión (ej. product-owner custodia product (strategy + operativo)) | `vault/shared/governance/role-catalog.md` |
| **Scope-scan** | Análisis multi-rol en paralelo, aplicado en 3 checkpoints uniformes (creation + post-step + verify) para descubrir/auditar dimensiones | Mecanismo en `CLAUDE.md` raíz |
| **Verifier** | Rol que audita una dimensión al cierre del WA | Derivado: `verifiers = { custodian(d) : d ∈ dimensions-affected }` |

---

## `.claude/` — runtime de Claude Code

Lo que Claude Code descubre nativamente al arrancar una sesión. Si Claude Code no lo descubre, no debe vivir aquí.

```
.claude/
├── agents/             ← identidad de cada rol (subagent files)
├── skills/             ← skills materializadas, organizadas por rol
├── commands/           ← slash commands invocables desde el chat
└── settings.json       ← permisos de tooling en este repo
```

### `.claude/agents/`

Cada archivo `.md` define la **identidad de un rol**: quién es, qué dimensión custodia, qué scope tiene en el vault, qué skills usa, qué subagentes puede invocar, qué hace y qué NO hace, la sección **"Al arrancar tu step"** (qué leer en orden estricto al iniciar un step), y la regla de **handoff** al completar steps (incluyendo post-step scope-scan flat parallel + entrada en Progreso downstream-ready + audit-ready).

Hay 8 agent files (uno por rol core). 6 son **asesores** (custodios de dimensiones, participan en scope-scan multi-rol). 2 son **ejecutores** (developer, devops — implementan; sin dimensión propia).

| Agent file | Rol | Dimensión | Cagan risk | Para qué |
|---|---|---|---|---|
| `product-owner.md` | Product Owner | product | value-risk (parcial) | Features, stories, specs Gherkin, discovery |
| `architect.md` | Architect | technical | viability-risk (technical) | ADRs, viability reviews, coupling detection, architecture archeology |
| `designer.md` | Designer | usability | usability-risk | Usability reviews, accessibility audits, interaction flows |
| `business-analyst.md` | Business Analyst | business | business-viability-risk | Business reviews, compliance mapping, GTM impact, pricing analysis |
| `security-officer.md` | Security Officer | security | (transversal) | Threat-models, vulnerability audits, compliance technical |
| `qa.md` | QA | quality | (transversal) | Test strategy, coverage, regression |
| `developer.md` | Developer | (sin dimensión, ejecutor) | — | Implementación de código |
| `devops.md` | DevOps | operations | (transversal) | Pipelines, infra, deployment |

Los **4 risks de Cagan** (*Inspired*) están cubiertos por los custodios: value (Product Owner extendido), usability (Designer), viability technical (Architect), business viability (Business Analyst). Ver sección [Mapeo a 4 risks de Cagan](#mapeo-a-4-risks-de-cagan).

Cada agent file se carga **solo cuando se invoca como subagente** (vía Task tool con `subagent_type: <rol>`) o cuando una sesión dedicada lo invoca (vía wrapper en `vault/<rol>/CLAUDE.md`).

### `.claude/skills/`

Skills son **procedimientos auditables del dominio del rol**. Cada skill tiene:
- `SKILL.md` (operativo): description en frontmatter + procedimiento paso a paso + estructura de nodos producidos + bibliografía + bloque "WA mapping" + sección "Status lifecycle".
- `design.md` (referencia): diseño detallado de la skill (proceso, ejemplos, fundamento bibliográfico, limitaciones).

Las skills se cargan **perezosamente**: Claude Code lee descriptions al iniciar sesión, y carga el cuerpo solo cuando el contexto matchea.

**Principio de separación**: las skills producen nodos con `status` inicial neutro (`draft` o `proposed`). **NO** setean el status final. Las transiciones de status las aplica recepción al `/verify` del WA, leyendo el campo `on-close` del frontmatter del WA. Esto mantiene las skills agnósticas al lifecycle del WA.

#### Skills por agente (14 totales — distribuidas en 8 agentes)

##### Product Owner — lado estratégico (4 skills) — fase `discovery`

| Skill | Qué hace | Output (status inicial) | Templates donde se invoca |
|---|---|---|---|
| `vision-quality-check` | Valida enunciado de visión con 4 lentes (Cagan, Sinek, Rumelt, JTBD) | Veredicto pass/fail con citas | `vision-creation`, `vision-realignment` (later) |
| `goal-quality-check` | Valida goal candidato con 6 tests (Doerr, Doran, Cagan) | Veredicto pass/fail | `goal-definition`, `strategy-review` (later) |
| `capability-quality-check` | Valida capability candidata con 6 tests (Rumelt, Torres, Cagan) | Veredicto pass/fail | `capability-creation` |
| `capability-derivation` | Deriva capabilities desde un goal aplicando OST (Torres) + kernel (Rumelt) + JTBD | Lista priorizada de capabilities candidatas con cross-links (`status: draft`) | `capability-creation` |

##### Product Owner (3 skills) — fase `design`

| Skill | Qué hace | Output (status inicial) | Templates donde se invoca |
|---|---|---|---|
| `feature-decomposition` | Capability → features → stories aplicando Patton story map + Cohn INVEST + JTBD | Árbol de features con cross-links (`status: draft`) | `feature-design` |
| `spec-writing` | Story + examples → AC formales (SMART) → spec Gherkin con frontmatter SEM-IA (Adzic SbE). Absorbe la antigua `acceptance-criteria-definition` | `vault/product-owner/specs/<feature>.md` (`status: draft`) | `feature-design` |
| `feature-quality-check` | Valida feature antes de cerrar el WA: INVEST + cobertura AC + cross-links + tamaño | Veredicto entre 5 opciones (aprobar / refinar / volver a discovery / descomponer / fundir) | `feature-design` (último step) |

##### Architect (5 skills) — fase `design`

| Skill | Qué hace | Output (status inicial) | Templates donde se invoca |
|---|---|---|---|
| `adr-writing` | Escribe ADR formal con plantilla Nygard extendida (Context + Decision + Consequences + Alternatives) | `vault/architect/adrs/<adr-id>.md` (`status: proposed`) | `adr`, opcionalmente en `feature-design`, `refactor`, `infra-decision` |
| `coherence-evaluation` | Evalúa si un cambio propuesto rompe coherencia con ADRs existentes; si sí, presenta 3 opciones (modo arbitraje) | Reporte estructurado + recomendación entre 4 opciones | `feature-design`, `capability-creation`, modo arbitraje SEM-IA |
| `feature-viability-review` | Review técnico de feature: archivos a tocar, ADRs aplicables/nuevos, modularidad, boundaries, coupling | `vault/architect/research/feature-N-architect-review.md` (`status: draft`) | `feature-design` (step Architect opcional) |
| `capability-viability-review` | Review técnico de capability: QAs implícitos, tactics, tradeoffs, fitness functions | `vault/architect/research/cap-N-viability.md` (`status: draft`) | `capability-creation` |
| `coupling-detection` | Inventaria y categoriza acoplamientos (apropiado declarado / no declarado, problemático declarado / no declarado) | Reporte estructurado + recomendación entre 4 opciones | Sub-skill de `feature-viability-review`, también en `refactor` |

##### Security Officer (1 skill) — fase `design`

| Skill | Qué hace | Output (status inicial) | Templates donde se invoca |
|---|---|---|---|
| `threat-modeling` | Threat-model formal con STRIDE simplificado + priorización (likelihood × impact) + mitigaciones + AC de seguridad (AC-S*) trazables a tests | `vault/security-officer/audits/<id>-threat-model.md` (`status: draft`) | `threat-model`, sub-skill en `feature-design` y `adr` cuando dimension `security` activa |

##### Designer (0 skills materializadas — opera con guía bibliográfica)

Designer custodia dimensión `usability` (Cagan usability-risk). **Hoy opera con guía bibliográfica directa** del agent file: Norman *Design of Everyday Things*, Nielsen 10 heurísticas, Cooper *About Face*, Cagan *Inspired*, WCAG 2.1 AA / ADA. Skills formales pendientes (later): `usability-heuristic-evaluation`, `interaction-flow-design`, `accessibility-audit`, `cognitive-load-assessment`. Se construirán cuando emerjan necesidades concretas en proyectos consumer/B2C.

Output típico: `vault/designer/audits/<feature>-usability-review.md` (`status: draft`).

##### Business Analyst (0 skills materializadas — opera con guía bibliográfica)

Business Analyst custodia dimensión `business` (Cagan business-viability-risk). **Hoy opera con guía bibliográfica directa** del agent file: Cagan *Inspired*/*Empowered*, Moore *Crossing the Chasm*, Christensen JTBD, Osterwalder *Business Model Generation*, reglamentos canónicos (GDPR, PCI-DSS, HIPAA, SOC 2, CCPA). Skills formales pendientes (later): `business-viability-review`, `compliance-mapping`, `pricing-impact-analysis`, `gtm-readiness-check`, `licensing-audit`.

Output típico: `vault/business-analyst/audits/<feature>-business-review.md` (`status: draft`).

##### Compartida (1 skill) — invocable desde cualquier agente

| Skill | Qué hace | Output | Templates donde se invoca |
|---|---|---|---|
| `graph-cross-link-declaration` | Identifica y declara aristas cross-link del grafo (`also-relates-to`, `depends-on`, `dimensions-affected`, `related-adrs`) en el frontmatter de cualquier nodo | Frontmatter del nodo con cross-links completos | Cualquier template que cree o modifique nodos del grafo |

##### Roles ejecutores (Developer, QA, DevOps) — sin skills materializadas hoy

Los agent files de los 3 roles ejecutores existen, pero **sus skills están pendientes** — se construirán como features formales bajo SEM-IA real cuando se ejecute el primer `feature-build` post-inception. Hoy estos roles operan con guía bibliográfica directa de su agent file (ej. Developer aplica patrones de TDD/Clean Code; QA aplica `// @ac-coverage:` para trazabilidad de AC).

Skills pendientes (~10 documentadas como later):
- **PO (lado estratégico)**: `strategy-review`, `vision-realignment`, `goal-decomposition`, `capability-prioritization`.
- **PO**: `discovery-facilitation`, `example-elicitation`, `story-writing`, `backlog-prioritization`, `value-effort-estimation`.
- **Architect**: `architectural-pattern-application`, `technical-debt-tracking`, `infrastructure-design`.
- **Security**: `access-control-review`, `vulnerability-scanning`.

### `.claude/commands/`

Slash commands invocables desde el chat. **El nombre del archivo es el nombre del comando**: `wa.md` → `/wa`. **El contenido del archivo es el prompt que se inyecta** cuando se invoca.

5 commands actuales:

| Comando | Para qué |
|---|---|
| `/status` | Snapshot del proyecto: WAs activos, subgrafo, features, ADRs |
| `/wa` | Detalle del WA aplicable a la sesión, con steps y status |
| `/scope-scan "<propuesta>"` | Scope-scan flat parallel multi-rol on-demand |
| `/verify` | Dispara matriz de verificación al cierre del WA |
| `/sessions` | Tabla de modos de trabajo y sesiones dedicadas |

### `.claude/settings.json`

Configuración del comportamiento de Claude Code en este repo: permisos (`allow`/`ask`/`deny`), modelos por defecto, hooks. Hoy declara permisos de Read/Write/Edit en `vault/**` y Read en `src/**`.

---

## `vault/` — grafo declarativo del proyecto

**Organizado por rol custodio (role-first).** Cada rol tiene su propia carpeta con sus artefactos. Los wrappers `CLAUDE.md` de subdirectorio cargan la identidad del rol cuando arrancas Claude Code en esa carpeta.

```
vault/
├── product-owner/                      ← Product Owner extendido (dimensión: product — strategy + operativo)
│   ├── CLAUDE.md                       ← entry point PO (wrapper thin)
│   ├── strategy/                       ← visión, goals, capabilities, roadmap
│   ├── strategy-reviews/               ← reviews periódicos del subgrafo
│   └── value-tracking/                 ← outputs → outcomes → value
│
├── product-owner/                      ← PO (dimensión: product)
│   ├── CLAUDE.md
│   ├── specs/                          ← features, stories, specs Gherkin
│   └── discovery/                      ← examples, JTBD, AC filtering
│
├── architect/                          ← Architect (dimensión: technical)
│   ├── CLAUDE.md
│   ├── adrs/                           ← Architecture Decision Records
│   └── research/                       ← reviews técnicos + bibliografía
│       ├── library/                    ← bibliografía citada por skills
│       └── bootstrap-summary.md        ← historia del bootstrap manual
│
├── developer/                          ← Developer (sin dimensión, ejecutor)
│   ├── learnings/                      ← aprendizajes técnicos
│   └── gotchas/                        ← cosas frágiles
│
├── qa/                                 ← QA (dimensión: quality)
│   └── reports/                        ← qa-reports
│
├── security-officer/                   ← Security Officer (dimensión: security)
│   └── audits/                         ← security-audits
│
├── devops/                             ← DevOps (futuro, dimensión: operations)
│
└── shared/                             ← Cross-role / infraestructura
    ├── sessions/active|archive/        ← Working Agreements (WAs)
    ├── governance/                     ← catálogos canónicos del proyecto
    │   ├── dimensions.md
    │   ├── role-catalog.md
    │   ├── verification-matrix.md
    │   ├── workflows.md
    │   └── repo-structure.md
    ├── plans/active|archive/           ← plans operativos
    ├── retros/                         ← retrospectivas
    └── reviews/                        ← reviews automáticas cross-role
```

### Por qué role-first

- **Auto-explicativo:** el nombre del directorio = el rol. PO se conecta → ve `vault/product-owner/`. Su scope es obvio.
- **Extensible:** un proyecto adopter que añade un rol custom (Quant, ML Engineer, DBA, Designer) crea `mkdir vault/<rol-custom>/`. Patrón limpio.
- **Refleja la filosofía SEM-IA:** roles homólogos por persona; el vault refleja el organigrama.
- **Convenciones internas conservadas:** `vault/architect/adrs/adr-001.md`, `vault/product-owner/specs/feature-1.md`. Cualquier dev encuentra lo que busca con grep `/adrs/` o `/specs/`.

### El grafo dentro del vault

Cada **nodo del vault** es un archivo markdown con:
- **Frontmatter YAML** declarando: `type`, `id`, `title`, `parent` (espina dorsal jerárquica), cross-links (`also-relates-to`, `depends-on`, `dimensions-affected`, `related-adrs`), `status`, etc.
- **Cuerpo markdown** con secciones específicas según el tipo de nodo. La estructura del frontmatter + secciones para cada tipo vive **inline en la skill que crea ese nodo** (no hay plantillas separadas).

**Modelo:** grafo dirigido con espina dorsal jerárquica + aristas cross-link. NO pirámide, NO árbol estricto. Un nodo válido declara explícitamente sus cross-links o el grafo queda incompleto.

### Working Agreements en `vault/shared/sessions/`

WAs son la unidad de trabajo. Mientras están activos, viven en `vault/shared/sessions/active/`. Al cerrarse (post-`/verify` aprobado), se mueven a `vault/shared/sessions/archive/`.

Anatomía completa del WA: ver sección [Working Agreement (WA) — anatomía completa](#working-agreement-wa--anatomía-completa) más abajo.

### Governance defaults (`vault/shared/governance/`)

5 catálogos canónicos:

| Archivo | Para qué |
|---|---|
| `dimensions.md` | Mapeo dimensión → custodio (ej. `product → product-owner`). **Fuente de verdad** del algoritmo de verificación. |
| `role-catalog.md` | Tabla de roles SEM-IA: dimensión custodiada, agent file, sesión dedicada, modelo. |
| `verification-matrix.md` | **Guía orientativa** de dimensiones típicas por tipo de operación. Mnemotécnica, no algoritmo. |
| `workflows.md` | **Templates de workflows indexados por fase SDLC** (`discovery | design | implementation | operations | meta`). Cada template define `produces`, opcionalmente `consumes`, y `default-steps` con role + phase + purpose. Backlog emerge gratis vía nodos con `status: ready-for-implementation`. |
| `repo-structure.md` | Fuente de verdad arquitectónica del repo (este README es onboarding; repo-structure.md es spec formal). |

---

## `src/` — framework distribuible

Esqueleto del paquete `@sem-ia/cli` que un adopter instalará vía `npm install -D @sem-ia/cli`. Hoy es esqueleto vacío — su construcción es feature post-inception del propio framework.

```
src/
├── adapters/                # Un adapter por harness soportado
│   ├── claude-code/         # bundled .claude/ + CLAUDE.md formato Claude Code
│   ├── opencode/            # futuro
│   └── pi/                  # futuro
├── universal/               # No depende de harness:
│                            #   - vault skeleton
│                            #   - schemas JSON para validación
│                            #   - governance defaults
└── cli/                     # sem-ia init / validate / check / coverage
```

Cuando exista, el adopter ejecuta:
```bash
npm install -D @sem-ia/cli
npx sem-ia init --harness=claude-code
```
Y recibe estructura idéntica a este repo: `.claude/` + `vault/` skeleton + `CLAUDE.md`.

---

## Working Agreement (WA) — anatomía completa

Un **Working Agreement (WA)** es un contrato declarativo que captura un bloque coherente de trabajo. Vive en `vault/shared/sessions/active/wa-YYYY-MM-DD-NNN.md` mientras está activo.

### Frontmatter

**Ejemplo: WA de fase `design` (feature-design)**

```yaml
---
type: working-agreement
id: wa-2026-05-07-001
created: 2026-05-07T10:00:00Z
status: active

# Tipo de outcome — selecciona workflow template
outcome-type: feature-design

# Fase SDLC — heredada del template
phase: design

# Qué se va a hacer
objective: "Diseñar feature de login con Google (spec + ADRs aplicables)"

# Referencias a nodos relacionados
related-feature: null
related-capability: cap-3-user-authentication
related-spec: null
related-adr: null

# Nodo consumido (templates de implementation lo usan; aquí null porque es design)
consumes:
  node-id: null
  required-status: null
  verified-at: null

# Output del scope-scan flat parallel
dimensions-affected: [product, technical, security, quality]
participants: [product-owner, architect, security-officer, qa]

# Steps ordenados — derivados del template feature-design, adaptados según scope-scan
steps:
  - id: step-1
    active-role: product-owner
    phase: design
    purpose: "Decomposition + spec Gherkin con AC formales"
    expected-output: "vault/product-owner/specs/feature-7-google-login.md (status: ready-for-implementation)"
    status: pending
    completed-at: null
    completed-by: null
  - id: step-2
    active-role: architect
    phase: design
    purpose: "Viability review + ADR para OAuth flow"
    expected-output: "vault/architect/adrs/adr-005-oauth.md"
    status: pending
    completed-at: null
    completed-by: null
  - id: step-3
    active-role: security-officer
    phase: design
    purpose: "Threat-model"
    expected-output: "vault/security-officer/audits/feature-7-threat-model.md"
    status: pending
    completed-at: null
    completed-by: null

# Scope autorizado / prohibido (paths del repo)
scope-allowed:
  - vault/product-owner/specs/
  - vault/architect/adrs/
  - vault/security-officer/audits/
scope-forbidden:
  - src/   # esto es WA de design; implementación viene en otro WA

# Verificadores al cierre — DERIVADO al ejecutar /verify
verifiers-required: [product-owner, architect, security-officer, qa]

# Criterios de cierre
closure-criteria:
  - Todos los steps en status: done
  - /verify aprobado por todos los verificadores

# Efectos al cerrar el WA — el output entra en el backlog
# Recepción aplica estas transiciones al /verify después de que verificadores aprueben
on-close:
  - "vault/product-owner/specs/feature-7-google-login.md: draft → ready-for-implementation"
  - "vault/architect/adrs/adr-005-oauth.md: proposed → accepted"
  - "vault/security-officer/audits/feature-7-threat-model.md: draft → active"
---
```

> **Status lifecycle separation of concerns.** Las skills (`spec-writing`, `adr-writing`, etc.) producen los nodos con status inicial neutro (`draft` o `proposed` para ADRs). El `on-close` del WA declara las transiciones. Recepción al `/verify` las aplica después de que los verificadores aprueben. Esto mantiene las skills agnósticas al lifecycle del WA: la misma skill puede invocarse en distintos templates con distintas transiciones.

**Ejemplo: WA de fase `implementation` (feature-build)** que consume el nodo del backlog producido arriba:

```yaml
---
type: working-agreement
id: wa-2026-06-12-002
created: 2026-06-12T09:00:00Z   # semanas después del WA de design
status: active
outcome-type: feature-build
phase: implementation

objective: "Implementar feature-7-google-login según spec del backlog"

related-spec: feature-7-google-login

# Nodo consumido del backlog — recepción verifica precondición antes de draftear
consumes:
  node-id: feature-7-google-login
  required-status: ready-for-implementation
  verified-at: 2026-06-12T09:00:00Z

dimensions-affected: [technical, security, quality]
participants: [architect, security-officer, qa, developer]

steps:
  - {id: step-1, active-role: developer, phase: implementation, purpose: "Implementar según spec + ADR-005", status: pending}
  - {id: step-2, active-role: qa, phase: implementation, purpose: "Cobertura E2E + AC + AC-S* del threat-model", status: pending}

scope-allowed: [src/, tests/]
scope-forbidden: [vault/]   # WA de implementation no toca el grafo

verifiers-required: [architect, security-officer, qa]

closure-criteria:
  - Todos los steps en status: done
  - /verify aprobado

on-close:
  - vault/product-owner/specs/feature-7-google-login.md → status: implemented
---
```

### Ciclo de vida

El WA pasa por **tres checkpoints multi-rol uniformes** — el mismo mecanismo (scope-scan flat parallel) en tres puntos del lifecycle:

| Checkpoint | Cuándo | Quién dispara | A quién invoca | Para qué |
|---|---|---|---|---|
| **Creation scope-scan** | Al draftear el WA | Recepción | 6 asesores en paralelo (po, architect, designer, business-analyst, security, qa) | Descubrir dimensiones top-down antes de comprometer scope, abordando los 4 risks de Cagan |
| **Post-step scope-scan** | Al completar cada step | Active-role del step | 6 asesores en paralelo (los 7 menos el active-role) | Capturar drift bottom-up dentro de un step de delay |
| **Verify** | Al cerrar el WA | Recepción (vía `/verify`) | Custodios de `dimensions-affected` | Validación final auditada |

**Flujo end-to-end:**

```
1. Sesión PO (modalidad recepción, Modo 1) recibe propuesta del humano.
   ↓
2. Recepción clasifica outcome-type (identifica fase SDLC del template).
   Si el template declara `consumes`, verifica que el nodo existe en el vault
   con el status correcto. Si NO existe: propone primero un WA de fase `design`.
   ↓
3. Recepción ejecuta scope-scan flat parallel (6 asesores en paralelo),
   carga template, drafta WA con steps, presenta al humano.
   ↓
4. Humano confirma. Recepción escribe WA en vault/shared/sessions/active/.
   ↓
5. Recepción al humano: "Step 1 pending para <rol>. Abre: cd vault/<rol> && claude".
   ↓
6. Humano cd → rol carga contexto upstream (WA + Progreso + artefactos previos),
   marca step in-progress, lo conduce, marca done.
   Rol añade entrada en "Progreso" (downstream-ready + audit-ready) con
   "Para el siguiente step" explícito.
   Rol ejecuta post-step scope-scan flat parallel (6 asesores en paralelo)
   auditando el output recién producido. Si emergen flags, presenta 3
   opciones al humano (aparcar / detener / extender).
   Rol indica handoff: "Step N done. Post-step scope-scan: <resumen>.
   Step N+1 pending para <rol>. Abre: cd ../<rol>".
   ↓
7. (Se repite hasta agotar steps).
   ↓
8. Último rol al humano: "Todos los steps done. Vuelve a recepción para /verify".
   ↓
9. Humano cd ../.. && claude. Ejecuta /verify.
   ↓
10. Recepción aplica algoritmo: verifiers = { custodian(d) : d ∈ dimensions-affected }.
    Invoca verificadores en paralelo. Consolida.
    ↓
11. Si aprobado: ejecuta efectos `on-close` (transiciones de status sobre nodos
    del grafo — ej. spec → status: ready-for-implementation o → status: implemented).
    Archiva WA en vault/shared/sessions/archive/.
    Si objeciones bloqueantes: WA vuelve a activo.
```

**Adicionalmente**, `/scope-scan` está disponible como comando on-demand para que el humano dispare un scope-scan extra entre checkpoints automáticos cuando lo juzgue necesario (mid-step, pre-WA, etc.).

---

## Workflow templates — indexados por fase SDLC

Vive en `vault/shared/governance/workflows.md`. **Es la fuente de verdad de los workflows que SEM-IA orquesta.** Los templates están organizados por **fase del SDLC enterprise**: `discovery | design | implementation | operations | meta`. Cada template tiene un `outcome-type` único, declara qué `produces` (output que deja en el vault) y opcionalmente qué `consumes` (nodo del vault que necesita como input).

**Insight central:** SEM-IA modela el SDLC tal como funciona en empresas reales — fases discretas con un **backlog persistente entre design y implementation**. Diseño e implementación viven en tempos distintos, a menudo separados por días o semanas. SEM-IA captura esa separación de forma natural.

**Dos vías de entrada al sistema:**
**Bootstrap orgánico**: humano pide algo, recepción dispara scope-scan multi-rol, si los asesores flagean nodos upstream faltantes recepción **propone una cadena de WAs** ordenada top-down usando los templates existentes. Cubre greenfield (cadena larga visión → goals → capability → feature), proyecto maduro con gap (cadena corta), y proyecto maduro sin gap (un solo WA). El grafo emerge feature a feature.

**Templates iniciales por fase:**

| Fase | outcome-type | Para qué | Steps típicos | Produces / Consumes |
|---|---|---|---|---|
| **discovery** | `vision-creation` | Definir/redefinir visión del producto | product-owner | → vision.md |
| | `capability-creation` | Crear capability nueva en subgrafo estratégico | product-owner → architect (opt) → designer (opt) → business-analyst (opt) | → capability.md |
| | `goal-definition` | Definir goal nuevo bajo la visión | product-owner | → goal.md |
| **design** | `feature-design` | Decomponer capability en feature(s) con spec Gherkin | po → architect (opt) → security (opt) | consumes capability → spec con `status: ready-for-implementation` |
| | `adr` | Decisión arquitectónica formal | architect → architect (ADR) → security (opt) | → ADR.md |
| | `threat-model` | Threat-model formal de feature sensible | security-officer | consumes spec → threat-model.md |
| **implementation** | `feature-build` | Implementar spec del backlog | developer → qa | consumes spec ready-for-implementation → código + tests; spec pasa a `implemented` |
| | `bugfix` | Reparar comportamiento incorrecto | developer (diagnose) → developer (fix) → qa (regression) | → src/ + tests |
| | `refactor` | Reorganización sin cambio funcional | architect → architect (ADR opt) → developer → qa | → src/ refactorizado |
| **operations** | `pipeline-change` | Cambio de CI/CD pipeline | devops → devops → security (opt) | → configs CI |
| | `infra-decision` | Decisión de infraestructura significativa | devops → architect (ADR) | → ADR operativo |
| | `observability-instrument` | Métricas/alertas/trazas para feature | devops | consumes feature implementada → instrumentación |
| **meta** | `doc-edit` | Edición de documento existente | rol-inferred-by-path | → doc editado |
| | `trivial` | Typo, copy fix, config menor | (sin steps, recepción lo edita directo) | — |

### Modo arbitraje — cuando NO hay cadena automática

La cadena de WAs por gaps cubre el caso normal: el humano pide algo, scope-scan detecta nodos upstream faltantes, recepción propone una cadena ordenada. Pero hay dos situaciones donde **recepción NO propone cadena automática** y eleva la decisión al humano:

**Variante C — Feature cuestiona la visión vigente.** Ejemplo: producto declarativamente "tool simple sin web3", humano propone "añadir blockchain". PO detecta contradicción con visión actual en el scope-scan inicial.

**Variante D — Feature es cross-cutting entre múltiples capabilities.** Toca capabilities X + Y + Z simultáneamente y rompe boundaries declarados.

En ambos casos, recepción presenta al humano **3 opciones** (sec. 11 del modelo SEM-IA):

1. **Descartar el cambio** — la visión / arquitectura actual prevalece.
2. **Modificar nivel superior y propagar** — abrir WA `vision-realignment` (skill later) o re-diseño de capabilities afectadas. La visión se ajusta conscientemente.
3. **Documentar excepción consciente** — feature cross-cutting documentada explícitamente con `coherence-exception` declarado en frontmatter + ADR breve explicando.

El mismo modo arbitraje se activa durante post-step scope-scan si emergen flags significativos (output contradice ADR, dimensión nueva no contemplada, upstream change requerido). Este patrón está soportado por el skill `coherence-evaluation` del Architect.

**`/scope-scan` on-demand** también puede activar arbitraje si los asesores reportan contradicciones graves al evaluar una propuesta antes de crear WA.

### El backlog emerge gratis

El **backlog no es una entidad persistente** en SEM-IA. Es una **query sobre el vault**:

```
backlog = nodos del vault con frontmatter `status: ready-for-implementation`
```

Estos nodos son output de WAs cerrados de fase `design` (specs producidas por el template `feature-design`, ADRs, threat-models). Cuando humano dice *"implementar feature-007"*, recepción clasifica `outcome-type: feature-build` y verifica que `feature-007` existe con ese status antes de draftear el WA. El comando `/status` muestra una sección "Backlog" derivada de esta query.

**Estados canónicos del nodo:** `draft` → `ready-for-implementation` → `in-implementation` → `implemented` (o `deprecated`).

### Caso de uso end-to-end: "implementar login con Google"

1. **Primera invocación a recepción**: humano dice *"quiero diseñar login con Google"* → recepción clasifica `outcome-type: feature-design` (fase `design`) → ejecuta scope-scan flat parallel → drafta WA con `on-close: spec → ready-for-implementation` y steps `po → architect → security` → humano confirma → cada step en sesión dedicada (PO invoca skills `feature-decomposition` + `spec-writing` que producen la spec con `status: draft`) → /verify aprueba y **aplica `on-close`** → `vault/product-owner/specs/feature-007.md` transiciona de `draft` a `ready-for-implementation`. WA se archiva. **Nodo en backlog.**

2. *(Tiempo pasa — días, semanas. El nodo vive en el vault. Aparece en `/status` → Backlog.)*

3. **Segunda invocación a recepción**: humano dice *"vamos a implementar feature-007"* → recepción clasifica `outcome-type: feature-build` (fase `implementation`) → verifica que `feature-007` existe con status correcto (precondición del template) → drafta WA con steps `developer → qa` referenciando `feature-007` como `consumes` → ejecución → al cierre, `feature-007` pasa a `status: implemented`.

Cada invocación es un WA cerrado, sin estado pendiente entre medias. Los post-step scope-scan se mantienen razonables porque cada WA es enfocado en su fase.

**Adopters extienden** con templates de su dominio (ej. `tokenomics-change`, `oracle-update`, `database-migration`) y pueden incluso **redefinir las fases** si su SDLC no es el clásico (ej. SAFe, lean startup). Patrón limpio: añadir entrada a `workflows.md`, sin tocar código.

---

## Mapeo a 4 risks de Cagan

SEM-IA materializa los **3 principios de Modern Product Development** de Marty Cagan (*Inspired*, *Empowered*) en su mecánica operativa:

### Principio 1 — Solve problems, not implement features

> *"Strong teams know that it's not just about implementing a solution. They must ensure that the solution solves the underlying problem. It's about business results."*

Cubierto por:
- **JTBD outcome** como Paso 1 de `feature-decomposition` (skill PO): toda feature empieza articulando *"Cuando X, el [usuario] quiere Y, so I can Z"*. Si no se puede articular el problema, retorno al humano.
- **`goal-quality-check` test 1** (skill PO lado estratégico): distingue "resultado o actividad" — outcomes vs outputs.
- **`capability-quality-check` test 1**: distingue "habilidad vs feature/actividad".

### Principio 2 — Collaborative, not sequential

> *"In strong teams, product, design and engineering work hand in hand, on a 'give and take' path, to come up with solutions based on the technology that our customers love and that work for our business."*

Cubierto por **tres mecanismos**:
- **Scope-scan flat parallel multi-rol al crear WA** — los 6 asesores miran la propuesta en paralelo (discovery colaborativa).
- **Subagente vía Task tool (give-and-take mid-step, Cagan principio 2) durante step active-role** (give-and-take puro de Cagan, **encouraged, no excepcional**). Ejemplos: PO durante decomposition invoca a Designer para sanity check de UX, a Architect para coupling check, a Business para compliance flag.
- **Post-step scope-scan flat parallel** — los 6 asesores restantes auditan el output recién producido (drift detection).

Esto evita el waterfall: cada custodio toca el WA en múltiples checkpoints, no espera su turno secuencial.

### Principio 3 — Risks addressed in advance, not at the end

> *"The risks are addressed before deciding to build anything. These risks include value risk, usability risk, viability risk, and business viability risk."*

**Los 4 risks tienen custodio explícito en SEM-IA:**

| Cagan risk | Pregunta que aborda | Dimensión SEM-IA | Custodio |
|---|---|---|---|
| **Value risk** | ¿Lo van a comprar/usar? | product (íntegro) | Product Owner extendido |
| **Usability risk** | ¿Pueden entender cómo usarlo? | usability | **Designer** |
| **Viability technical** | ¿Podemos construirlo con la tecnología/skills/tiempo? | technical | Architect |
| **Business viability** | ¿Funciona para sales, marketing, finance, legal? | business | **Business Analyst** |

Adicionales (transversales): **security** (Security Officer) cubre threats que solapan con compliance regulatoria; **quality** (QA) cubre coverage de los AC derivados de cada risk; **operations** (DevOps) cubre operational risk de despliegue.

### Por qué value risk no tiene custodio único — riesgos atómicos vs holísticos

A diferencia de los otros 3 risks de Cagan que son **atómicos** (auditables desde un solo ángulo), **value risk es emergente** — requiere síntesis de múltiples dimensiones desde la perspectiva del usuario:

| Risk | Tipo | Pregunta auditable | Auditable desde |
|---|---|---|---|
| Usability | atómico | ¿Pueden usar esto? | Designer (UX/flow/accessibility) |
| Viability technical | atómico | ¿Podemos construirlo? | Architect (code/team/tech) |
| Business viability | atómico | ¿Funciona para nuestro negocio? | Business Analyst (pricing/legal/GTM) |
| **Value** | **emergente** | ¿Querrá el usuario pagar/usar esto? | **Múltiples** (síntesis) |

**Value = benefits / cost**. Y ambas partes se descomponen naturalmente en custodios distintos:

```
BENEFITS                                    COST (al usuario)
────────                                    ─────────────────
¿Resuelve un problema real?                 ¿Vale el precio?
  → Product Owner (strategy alignment)                → Business Analyst (financial)
¿Es el job que el usuario necesita?         ¿Es comprensible?
  → Product Owner (JTBD fit)                  → Designer (cognitive cost)
                                            ¿Confío en compartir mis datos?
                                              → Security (trust cost)
                                            ¿Cuánto esfuerzo de integración?
                                              → Architect (technical friction)
                                              → Designer (UX friction)
```

**Implicación**: NO añadir un "value-officer" agent sería:
- **Anti-Cagan** (strong product team no tiene value officer — el PM es primary owner del outcome de validación pero compose inputs de otros custodios).
- **Anti-modelo** (custodios atómicos 1:1 por dimensión; lo holístico emerge del scope-scan multi-rol).
- **Worse than specialists** (un generalista superficial vs especialistas colaborando).

El "agente que evalúa value risk" en SEM-IA **es literalmente el scope-scan multi-rol consolidado por recepción**. Esa consolidación es la síntesis holística que Cagan describe.

### Generalización — otros riesgos holísticos

El patrón aplica a otros risks emergentes que pueden detectarse durante scope-scan:

| Riesgo holístico | Emerge de |
|---|---|
| **Value** | strategy + product + usability + business + security + technical |
| **Coherence** (¿se siente consistente?) | product + usability + brand |
| **Trustworthiness** | security + business + usability |
| **Adoption** (¿lo adoptarán realmente?) | value + usability + business + operations |
| **Resilience** | technical + operations + quality |

Ninguno tiene custodio dedicado. Todos emergen del scope-scan multi-rol cuando un WA toca múltiples dimensiones simultáneamente.

### Por qué Designer y Business Analyst son core

Sin custodios explícitos para usability y business viability, esos risks se difieren a producción y se descubren cuando los usuarios fallan o cuando legal/finance/sales descubren incompatibilidades. Para que los 4 risks de Cagan sean ABORDADOS antes de construir, los custodios deben existir en el catálogo core, no como roles custom opcionales del adopter.

**Coste**: scope-scan multi-rol pasa de 5 → 6 asesores (~$2.10 vs ~$1.50 con prompt caching). Negligible vs el coste de rework por gap detectado en producción.

---

## Dual Track — Discovery + Delivery (Cagan/Patton)

SEM-IA materializa el **Dual Track Agile** canónico (Cagan, *Inspired*; Patton, *User Story Mapping*): dos tracks paralelos donde la **Discovery** valida QUÉ construir y la **Delivery** construye CÓMO.

```
┌─ DISCOVERY TRACK ────────── "Build the right product" ──────────┐
│ Stakeholder viewpoint · Fast learning + validation               │
│                                                                  │
│  Risks abordados:        →  Custodios SEM-IA:                    │
│   • Value                   Product Owner extendido              │
│   • Usability               Designer                             │
│   • Feasibility (technical) Architect                            │
│   • Viability (business)    Business Analyst                     │
│                                                                  │
│  Fases SEM-IA:           →  discovery + design                   │
│  Templates:                 vision-creation, capability-creation,│
│                             goal-definition, feature-design,     │
│                             adr, threat-model                    │
│  Output:                    spec status: ready-for-implementation│
└──────────────────────────────────────────────────────────────────┘
                       ↓
                BACKLOG (puente persistente entre tracks)
                       ↓
┌─ DELIVERY TRACK ─────────── "Build the product right" ──────────┐
│ Engineering viewpoint · Predictability + quality                 │
│                                                                  │
│  QAs abordados (Bass):   →  Custodios SEM-IA:                    │
│   • Functionality           Product Owner + QA                   │
│   • Scalability             Architect + DevOps                   │
│   • Reliability             Architect + DevOps + QA              │
│   • Performance             Architect + DevOps                   │
│   • Maintainability         Architect (ADRs, coupling-detection) │
│                                                                  │
│  Fase SEM-IA:            →  implementation                       │
│  Templates:                 feature-build, bugfix, refactor      │
│  Output:                    código + tests, spec → implemented   │
└──────────────────────────────────────────────────────────────────┘
```

### Paralelismo real

**Los dos tracks corren en paralelo** en proyectos maduros: mientras el equipo construye `feature-N` en Delivery (`feature-build` WA activo), Discovery puede estar validando `feature-N+1` (`feature-design` WA activo simultáneamente). El motor de SEM-IA permite múltiples WAs activos a la vez sin restricción — humano puede tener varias sesiones abiertas con distintos roles trabajando en distintos tracks.

El **backlog** (nodos con `status: ready-for-implementation`) es el puente persistente: items validados en Discovery esperan ahí hasta que el equipo de Delivery los pull. `/status` muestra el estado de ambos tracks + backlog en una vista única.

### Por qué importa

Cagan describe el antipatrón opuesto: equipos que solo hacen Delivery (waterfall disfrazado de agile — recibir requirements y construir sin validar) o solo Discovery (parálisis por análisis — validar sin entregar). El equipo fuerte mantiene **ambos tracks corriendo en paralelo continuamente**.

SEM-IA no fuerza el ratio entre tracks (es decisión del equipo según contexto), pero **lo hace visible y auditable**: `/status` muestra cuántos WAs en cada fase, el backlog visible te dice si Discovery está alimentando Delivery o si hay cuello de botella en uno de los lados.

---

## Slash commands

Todos invocables desde cualquier sesión.

### `/status`
Snapshot rápido del proyecto: WAs activos (con outcome-type, step actual, progreso), estado del subgrafo estratégico, features ready/blocked, ADRs por status.

### `/wa`
Detalle del WA aplicable al contexto de la sesión actual. Muestra steps con status, scope, criteria, próxima acción.

### `/scope-scan "<propuesta>"`
Scope-scan flat parallel on-demand. Invoca a los 7 roles asesores en paralelo. Útil mid-WA para validar candidatas, detectar drift, o explorar antes de proponer un WA. **Forward-looking** (descubrimiento) — simétrico con `/verify` (audit hacia atrás).

### `/verify`
Dispara matriz de verificación al cierre del WA. Aplica algoritmo: `verifiers = { custodian(d) : d ∈ dimensions-affected }`. Invoca verificadores en paralelo. Consolida veredictos. Tras aprobación, **aplica las transiciones declaradas en `on-close`** del WA (ej. spec: `draft → ready-for-implementation`). Nunca archiva sin confirmación humana.

### `/sessions`
Imprime tabla de modos de trabajo (sesión PO con modalidad recepción + sesiones dedicadas por rol) con sus comandos y para qué sirve cada uno.

---

## Cómo extender SEM-IA (para adopters)

SEM-IA está diseñado para que cada proyecto lo personalice según su organización.

### Añadir un rol custom

Ejemplo: añadir `business-analyst`.

1. Crear `.claude/agents/business-analyst.md` con identidad, dimensión custodiada, scope, skills, protocolo en scope-scan, regla de handoff.
2. Crear `vault/business-analyst/CLAUDE.md` (wrapper thin que apunta al agent file).
3. Añadir entrada a `vault/shared/governance/role-catalog.md`.
4. Si introduce dimensión nueva (`business-metrics`), añadirla a `vault/shared/governance/dimensions.md` con `custodian: business-analyst`.
5. Crear skills en `.claude/skills/business-analyst/`.

A partir de eso, recepción incluye `business-analyst` en scope-scan flat parallel automáticamente, y los workflows pueden referenciarlo.

### Añadir una dimensión custom

1. Editar `vault/shared/governance/dimensions.md`: añadir entrada con `id`, `description`, `custodian`.
2. Si la dimensión tiene custodio sin agent file, crear el agent file.
3. Opcional: actualizar `vault/shared/governance/verification-matrix.md` (guía orientativa) si hay patrones recurrentes que toquen esa dimensión.

### Añadir un workflow template custom

1. Editar `vault/shared/governance/workflows.md`.
2. Añadir entrada bajo la fase apropiada (`discovery | design | implementation | operations | meta`) con `description` + `produces` + opcionalmente `consumes` + `default-steps`. Si la fase no encaja en las estándar, el adopter puede añadir una nueva fase.
3. Cada step define `role`, `phase`, `purpose`, opcional `optional` + `condition`.
4. Actualizar la heurística de clasificación si el outcome-type tiene keywords distintivas.
5. Si el template es de fase `design` que produce un nodo del backlog, asegurar que el último step setea `status: ready-for-implementation` en el frontmatter del nodo.
6. Si el template es de fase `implementation` que consume del backlog, declarar `consumes` con `node-id` + `required-status` para que recepción verifique la precondición.

---

## `CLAUDE.md` raíz

`CLAUDE.md` es el archivo que **Claude Code carga automáticamente al arrancar una sesión** en este repo. Es **guía estática del proyecto** — no define identidad de agente. La identidad de "recepción" la carga el PO extendido cuando se abre `npm run sem` o `npm run po` (sesión `vault/product-owner/`); el PO en su Modo 1 (Entrada al sistema) **ES** lo que en docs operativos se llama "recepción".

### Cuándo se carga

**Solo al arrancar la sesión.** Cuando ejecutas `claude` en un directorio:
1. Claude Code busca y lee `CLAUDE.md` una vez (lectura del disco).
2. Lo añade al contexto de la sesión (system prompt).
3. A partir de ahí, está disponible toda la conversación.

En cada turno posterior, el contenido de `CLAUDE.md` se envía al modelo como parte del system prompt, pero gracias al **prompt caching** de Anthropic se procesa una sola vez por ventana de 5 minutos (re-uso barato del prefix cacheado).

### Carga jerárquica

Cuando arrancas Claude Code en un subdirectorio del repo, **se cargan todos los CLAUDE.md de la cadena**:

```
cd vault/product-owner && claude
```
Carga:
- `/CLAUDE.md` (raíz, guía estática) — siempre.
- `vault/product-owner/CLAUDE.md` (PO extendido, sesión dedicada).

El wrapper de subdirectorio dice al modelo "operas como [rol] en sesión dedicada, lee `.claude/agents/<rol>.md`" y carga la identidad del rol. Para wrappers de roles asesores (architect, designer, etc.) se aclara que NO son "recepción" — esa modalidad es exclusiva del PO en su Modo 1.

En SEM-IA hay **4 archivos CLAUDE.md**:

| Path | Rol cargado | Cuándo |
|---|---|---|
| `/CLAUDE.md` | Recepción | Siempre, en cualquier sesión del repo |
| `vault/product-owner/CLAUDE.md` | PO extendido | Sesión iniciada en `vault/product-owner/` |
| `vault/product-owner/CLAUDE.md` | Product Owner | Sesión iniciada en `vault/product-owner/` |
| `vault/architect/CLAUDE.md` | Architect | Sesión iniciada en `vault/architect/` |

Cada wrapper es **thin** (~30 líneas): apunta al agent file y describe cuándo se usa la sesión.

---

## Otros archivos en raíz

- **`.gitignore`** — qué se excluye del repo (`node_modules/`, `.DS_Store`, etc.).
- **`LICENSE`** — Apache 2.0.

---

## Estado del proyecto

**Pre-inception.** El framework SEM-IA está estructuralmente completo (todos los conceptos descritos en este README están implementados como infraestructura), pero el contenido del proyecto SEM-IA mismo (visión, goals, capabilities, features) aún no se ha generado vía inception real.

### Lo que está listo

- ✅ Estructura del repo (3 carpetas + governance + agents + skills + commands).
- ✅ 8 agent files (PO extendido, Architect, Designer, Business Analyst, Security Officer, QA, Developer, DevOps).
- ✅ 7 dimensions mapeadas a custodios (alineadas con los 4 risks de Cagan).
- ✅ 15 skills materializadas con base bibliográfica + 2 roles operando con guía bibliográfica directa (Designer, Business Analyst).
- ✅ 5 slash commands (`/status`, `/wa`, `/scope-scan`, `/verify`, `/sessions`).
- ✅ Workflow templates en `workflows.md`.
- ✅ Dimensions, role-catalog, verification-matrix, repo-structure (governance).
- ✅ Wrappers de sesión dedicada para los 3 roles asesores con skills implementadas.
- ✅ Vault skeleton role-first.

### Lo que falta

- ⏳ **Bootstrap manual del propio SEM-IA**: arrancar `npm run sem` y construir vision + goals + capabilities + features de SEM-IA paso a paso usando los templates normales (vision-creation → goal-definition → capability-creation → feature-design). Será el primer test del modelo en producción.
- ⏳ **`@sem-ia/cli`** (paquete distribuible en `src/`): bin scripts ergonómicos, init, validate, check.
- ⏳ **Wrappers para roles ejecutores** (Developer, QA, DevOps) cuando exista código en `src/`.
- ⏳ **Skills "later"** (~10 skills documentadas) — se construirán como features formales post-adopción.

### Próximos pasos

1. **Bootstrap manual de SEM-IA**: humano arranca `npm run sem` → request "definir visión de SEM-IA" → cadena de WAs `vision-creation` → `goal-definition` × N → `capability-creation` × M → `feature-design` × K (para features ya implementadas como skills/templates). Vault de SEM-IA queda poblado con su propio grafo via flujo normal del framework (dogfooding).
2. **Construcción de `@sem-ia/cli`** como primera feature formal del framework usándolo a sí mismo (recursión).
3. **Caso de portabilidad** (proyecto adopter de prueba) cuando el framework esté estabilizado.

---

## Recursos adicionales

- `vault/shared/governance/repo-structure.md` — fuente de verdad arquitectónica completa.
- `vault/shared/governance/workflows.md` — todos los workflow templates.
- `vault/architect/research/bootstrap-summary.md` — historia del bootstrap manual del proyecto.
- `vault/architect/research/library/` — bibliografía citada por skills.

---

## Pendientes — capability "Adopción retroactiva desde código pre-existente"

**Caso de uso**: alguien con un proyecto a medias (ej. app de recetas con 30k LOC ya escritos por su cuenta) quiere llevarlo a SEM-IA y que el framework lo entienda derivando el grafo retroactivamente desde el código + docs existentes. En lugar de articular manualmente vision + goals + capabilities + features (que ya están implícitos en el código), el framework los extrae bottom-up.

**Estado**: diseñado conceptualmente durante la fase pre-inception del framework, **no implementado** en v1. La decisión: arrancar SEM-IA con bootstrap orgánico (cadena de WAs por gaps) que cubre todos los casos donde el grafo se construye conforme se trabaja. La adopción retroactiva es optimización para casos específicos (proyectos maduros con código sustancial pre-existente) que se construirá como feature formal cuando emerja la necesidad real.

**Arquitectura prevista** (cuando se implemente):
- Slash command `/adopt <ruta>` como entry point.
- Template `adopt` en fase nueva `adoption` cruzando múltiples fases SDLC en un único WA.
- Skill nueva `architecture-archeology` (Architect): walk del código + inventario de módulos + boundaries + acoplamientos + decisiones técnicas implícitas (candidatas a ADR retroactivo).
- Skills existentes (`spec-writing`, `feature-decomposition`, `capability-derivation`) ganan modo "lectura" (leen artefactos en lugar de conversar).
- Campo `derived-from` en frontmatter de nodos derivados (paths de artefactos origen) para auditabilidad.
- Steps típicos: Architect inventario → PO specs retroactivas (modo lectura) → Architect ADRs retroactivos opt → Designer usability audit opt → Business compliance audit opt → PO capabilities/goals/visión inferida (modo lectura, humano valida fuerte).

Esta capability se construirá vía SEM-IA (recursivo) cuando un adopter real con código sustancial la necesite. Hasta entonces, todos los proyectos arrancan via bootstrap orgánico.

---

## Pendientes — hooks de Claude Code para determinismo

El modelo actual es **probabilístico**: Claude sigue las reglas declaradas en CLAUDE.md, agent files y skills ~99% del tiempo, pero no garantizado al 100%. Los **hooks de Claude Code** son la siguiente capa de hardening — corren en el harness (no en Claude) y permiten validación determinística antes/después de tool calls, inyección de contexto, y bloqueos de operaciones que violen reglas.

**Lo que hooks pueden hacer**: ejecutar bash deterministically, bloquear writes a paths prohibidos, validar frontmatter contra schema, inyectar contexto al inicio de sesión, recordar handoffs olvidados.

**Lo que NO pueden**: invocar a Claude / subagents (no pueden ejecutar scope-scan multi-rol por sí mismos), tomar decisiones cognitivas. Solo flanquean a Claude, no lo sustituyen.

### Quick wins (alto valor, ~2h totales) — pendientes

1. **`SessionStart` hook al root**: ejecutar `/status` y pegar output al prompt antes de la primera respuesta. Garantiza el ritual de inicio sin depender de que Claude lo recuerde. **Riesgo principal que mitiga**: empezar sesión sin leer el WA activo.

2. **`PreToolUse Bash` safety hook**: bloquear comandos peligrosos (`rm -rf /`, `git push --force` a main, `chmod 777`). ~30 líneas de bash.

3. **`PreToolUse Write/Edit` validation en `vault/**/*.md`**: validar frontmatter mínimo (campos `type`, `id`, `status` presentes). Si falta, error con mensaje claro. Necesita `yq`.

### Medio valor (~half day cada uno) — pendientes

4. **`PostToolUse Edit` en WAs**: loggear transiciones de step a `status: done` en `vault/shared/sessions/audit.log` para auditoría temporal.

5. **`Stop` hook en sesiones de rol** (po, arch, des, biz, sec, qa, dev, ops): si el WA tiene un step `done` reciente, verificar que la última respuesta del assistant menciona handoff (`npm run <rol>` o "vuelve a recepción"). Si no, recordatorio.

6. **`PreToolUse Bash` block de cd fuera del scope**: si la sesión es de PO, bloquear `cd vault/architect/` (forzar handoff vía npm scripts).

### Alto coste — post-inception

7. **Schema validation completa**: requiere schemas JSON para cada tipo de nodo en `src/universal/schemas/`. Va con la construcción del `@sem-ia/cli` distribuible.

8. **`/verify` semi-automatizado**: hook que verifica determinísticamente que `on-close` se aplicó correctamente al cerrar WA, leyendo cada path declarado. Necesita parsing YAML robusto.

### Por qué se difieren

Los hooks añaden infra complexity (bash scripts + parsing YAML + testing). Para una primera versión donde estamos validando el modelo conceptual, el coste no se justifica. La fiabilidad probabilística (~99%) es suficiente para arrancar inception y exercitar el flujo. Cuando emerjan errores reales en producción, se identifica qué hooks específicos los habrían prevenido y se construyen targeted.

**Donde el sistema HOY depende de Claude siguiendo reglas** (gaps potenciales para hooks futuros):
- Recepción ritual de inicio (lectura de WAs activos al arrancar).
- Post-step scope-scan automático tras handoff.
- Handoff verbal explícito al humano al cerrar step.
- Aplicación de `on-close` al `/verify`.
- Verificación de precondición `consumes` antes de draftear WA de implementation.
- Marcar step `status: in-progress` al arrancar.
- Frontmatter completo en nodos nuevos (incluyendo `derived-from` retroactivos).
- Append a "Progreso" del WA al cerrar step.
