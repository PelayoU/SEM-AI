---
type: governance
id: repo-structure
title: "Estructura del repositorio SEM-IA"
status: active
created: 2026-04-30
updated: 2026-05-03
author: human
materializes-feature: [feature-001-vault-role-first]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): doc que documenta la convención `vault/<rol>/` materializada por feature-001.
---

# Estructura del repositorio SEM-IA

Este documento es la **fuente única de verdad** de la arquitectura del repo: dónde vive cada cosa, qué se distribuye y qué no, y la regla de no-duplicación.

## Modelo conceptual — dos cosas coexisten

Este repo contiene **dos cosas distintas que conviven**:

1. **El framework SEM-IA** — el paquete distribuible que un adopter instalará en su proyecto. Vive en `src/`.
2. **El proyecto SEM-IA usándose a sí mismo (dogfooding)** — SEM-IA aplicando SEM-IA para construirse. Recursión. Ocupa `.claude/`, `vault/` y `CLAUDE.md` raíz.

| Concepto | Vive en | ¿Viaja al adopter? |
|---|---|---|
| Framework distribuible | `src/` | Sí (publicado a npm como `@sem-ia/cli`) |
| Dogfooding: artifacts Claude Code | `.claude/` | Sí, generado en el adopter al ejecutar `npx sem-ia init` |
| Dogfooding: contenido del proyecto SEM-IA | `vault/product-owner/`, `vault/architect/`, etc. | No |
| Recepción del dogfooding | `CLAUDE.md` raíz | Sí (default del framework) |

## Las tres carpetas reales

```
.claude/      ← Claude Code lee de aquí (agents, skills, commands, settings)
vault/        ← Contenido del proyecto SEM-IA, organizado por rol custodio
src/          ← Framework distribuible (paquete @sem-ia/cli, esqueleto hoy)
```

Más archivos sueltos en raíz: `CLAUDE.md`, `README.md`, `package.json` (cuando exista), `LICENSE`, `.gitignore`.

## `vault/` — organización role-first

Cada rol custodio tiene **su propia carpeta** en el vault. Dentro, sus artefactos. Los wrappers `CLAUDE.md` viven al nivel del rol — al hacer `cd vault/<rol> && claude`, se carga la identidad del rol vía wrapper.

```
vault/
├── product-owner/                      ← Product Owner extendido (dimensión: product — strategy + operativo)
│   ├── CLAUDE.md                       ← entry point PO
│   ├── strategy/                       ← visión, goals, capabilities, roadmap (lado estratégico)
│   ├── strategy-reviews/               ← reviews periódicos del subgrafo estratégico
│   ├── specs/                          ← features, stories, specs Gherkin (lado operativo)
│   └── discovery/                      ← examples, JTBD, AC filtering
│
├── architect/                          ← Architect (dimensión: technical)
│   ├── CLAUDE.md                       ← entry point Architect
│   ├── adrs/                           ← Architecture Decision Records
│   └── research/                       ← reviews técnicos + bibliografía
│       ├── library/                    ← bibliografía citada por skills
│       └── bootstrap-summary.md        ← historia del bootstrap manual
│
├── designer/                           ← Designer (dimensión: usability)
│   ├── CLAUDE.md                       ← entry point Designer
│   └── audits/                         ← usability reviews, accessibility audits
│
├── business-analyst/                   ← Business Analyst (dimensión: business)
│   ├── CLAUDE.md                       ← entry point Business Analyst
│   └── audits/                         ← business-viability reviews, compliance maps
│
├── developer/                          ← Developer (sin dimensión, implementa)
│   ├── learnings/                      ← aprendizajes técnicos
│   └── gotchas/                        ← cosas frágiles
│
├── qa/                                 ← QA (dimensión: quality)
│   └── reports/                        ← qa-reports
│
├── security-officer/                   ← Security Officer (dimensión: security)
│   └── audits/                         ← security-audits
│
├── devops/                             ← DevOps (dimensión: operations)
│
└── shared/                             ← Cross-role / infraestructura
    ├── sessions/active|archive/        ← Working Agreements
    ├── governance/                     ← defaults del framework
    │   ├── dimensions.md
    │   ├── role-catalog.md
    │   ├── verification-matrix.md
    │   └── repo-structure.md (este)
    ├── plans/active|archive/           ← plans operativos
    ├── retros/                         ← retrospectivas
    └── reviews/                        ← reviews automáticas cross-role
```

### Por qué role-first

1. **Auto-explicativo:** el nombre del directorio = nombre del rol. PO se conecta → ve `vault/product-owner/`. Su scope es obvio.
2. **Extensible:** un proyecto adopter que añada un rol custom (Quant, ML Engineer, DBA, Designer) crea `mkdir vault/<rol-custom>/` + wrapper. Patrón limpio.
3. **Refleja la filosofía SEM-IA:** roles homólogos por persona. El vault refleja el organigrama del proyecto.
4. **Conventions internas conservadas:** `vault/architect/adrs/adr-001.md`, `vault/product-owner/specs/feature-1.md`. Cualquier dev encuentra lo que busca con grep `/adrs/` o `/specs/`.

### Reglas de los wrappers de sesión dedicada

- **Un entry point por rol.** El wrapper vive al nivel `vault/<rol>/CLAUDE.md`, no más profundo.
- **El wrapper es thin.** No duplica identidad del agent file — solo dice "lee `.claude/agents/<rol>.md`".
- **El modo de trabajo lo dicta el WA.** No el subdirectorio. Un PO en `vault/product-owner/` puede hacer estrategia (visión/goals/capabilities), discovery o specs según `outcome-type` del WA activo.
- **Los outputs van al subdirectorio correcto** según el artefacto, aunque la sesión arranque en otro path.

## `.claude/` — artifacts que Claude Code descubre nativamente

```
.claude/
├── agents/                  # Identidad de cada rol como subagent (8 roles)
│   ├── product-owner.md     # extendido — custodia product (strategy + operativo)
│   ├── architect.md
│   ├── designer.md
│   ├── business-analyst.md
│   ├── security-officer.md
│   ├── qa.md
│   ├── developer.md
│   └── devops.md
├── skills/                  # Skills materializadas
│   ├── product-owner/strategy/<skill>/SKILL.md  # estratégicas (4)
│   ├── product-owner/<skill>/SKILL.md           # operativas (3)
│   ├── architect/<skill>/...                    # (5)
│   ├── security-officer/<skill>/...             # (1)
│   ├── shared/<skill>/...                       # graph-cross-link-declaration
│   └── _pending-later.md                        # catálogo pendientes
├── commands/                # Slash commands
│   ├── status.md            # /status
│   ├── wa.md                # /wa
│   ├── scope-scan.md        # /scope-scan
│   ├── verify.md            # /verify
│   └── sessions.md          # /sessions
└── settings.json
```

Claude Code lee de aquí. Punto. Si Claude Code no lo descubre nativamente, no va aquí.

## `src/` — framework distribuible (esqueleto)

```
src/
├── adapters/                # Un adapter por harness soportado
│   ├── claude-code/
│   ├── opencode/            # futuro
│   └── pi/                  # futuro
├── universal/               # No depende de harness:
│                            #   - vault skeleton
│                            #   - schemas JSON
│                            #   - governance defaults
├── cli/                     # sem-ia init / validate / check / coverage
└── package.json             # se publica como @sem-ia/cli
```

`src/` está vacío hoy. Su construcción es feature post-inception.

## Por qué los artifacts viven en sitios distintos

Cada tool dicta dónde mira:
- **Claude Code** → `.claude/agents/`, `.claude/skills/`, `.claude/commands/`, `CLAUDE.md`.
- **vault-cli (futuro)** → `src/universal/schemas/`.
- **Node / npm** → `src/`.

Si todos los artifacts pudieran vivir en una sola carpeta, ahí estarían. No pueden por convención de tooling.

## Regla de no-duplicación — un concepto = un archivo

| Concepto | Único archivo fuente |
|---|---|
| Identidad del Product Owner (extendido) | `.claude/agents/product-owner.md` |
| Identidad del Architect | `.claude/agents/architect.md` |
| Skill X del PO (estratégica u operativa) | `.claude/skills/po-X/SKILL.md` (estructura plana con prefijo de rol) |
| Skill X de otro rol | `.claude/skills/<prefijo>-X/SKILL.md` (`arch-`, `sec-`, `qa-`, `des-`, `biz-`, `dev-`, `ops-`, `shared-`) |
| Skill X (diseño detallado) | `.claude/skills/<prefijo>-X/design.md` |
| Estructura del nodo X (vision/goal/capability/feature/story/spec/ADR) | Inline en el SKILL.md de la skill que crea ese nodo |
| Estructura del Working Agreement | `CLAUDE.md` raíz, sección "Estructura de un Working Agreement" |
| Fuente bibliográfica X | `vault/architect/research/library/<fuente>.md` |
| Índice bibliográfico | `vault/architect/research/library/INDEX.md` |
| Estructura del repo | `vault/shared/governance/repo-structure.md` (este archivo) |
| Catálogo de roles | `vault/shared/governance/role-catalog.md` |
| Catálogo de dimensiones | `vault/shared/governance/dimensions.md` |
| Matriz de verificación | `vault/shared/governance/verification-matrix.md` |
| Catálogo de workflows | `vault/shared/governance/workflows.md` |
| Recepción (root) | `CLAUDE.md` |
| Slash command `/sessions` | `.claude/commands/sessions.md` |
| Wrapper de sesión rol X | `vault/<rol>/CLAUDE.md` (thin — no duplica identidad) |
| Resumen del bootstrap | `vault/architect/research/bootstrap-summary.md` |
| Visión del proyecto SEM-IA | `vault/product-owner/strategy/vision.md` |

## Distribución — qué viaja al adopter

### Canal único — npm package `@sem-ia/cli` (cuando `src/` exista)

```bash
npm install -D @sem-ia/cli
npx sem-ia init --harness=claude-code
```

El CLI lee de `src/adapters/claude-code/` + `src/universal/` y escribe en el repo del adopter:

- `.claude/` (agents, skills, commands, settings.json)
- `vault/` skeleton (estructura role-first vacía + governance defaults + wrappers)
- `CLAUDE.md` raíz
- `package.json` con `@sem-ia/cli` como devDependency

### Lo que NUNCA viaja al adopter

- `vault/product-owner/strategy/<files>` (excepto wrapper CLAUDE.md): contenido estratégico del proyecto SEM-IA.
- `vault/product-owner/specs/<files>`, `vault/architect/adrs/<files>`: contenido del proyecto.
- `vault/architect/research/library/`: bibliografía del proyecto SEM-IA. Las skills citan rutas; cuando viajan al adopter, quedan como información de origen pero el adopter no necesita leerlas para operar.
- `vault/architect/research/bootstrap-summary.md`: historia específica.

### Adopter recibe

```
mi-proyecto/
├── .claude/
├── vault/
│   ├── product-owner/CLAUDE.md
│   ├── product-owner/strategy/.gitkeep
│   ├── product-owner/specs/.gitkeep
│   ├── architect/CLAUDE.md
│   ├── designer/CLAUDE.md
│   ├── business-analyst/CLAUDE.md
│   ├── security-officer/CLAUDE.md
│   ├── qa/CLAUDE.md
│   └── shared/governance/
├── CLAUDE.md
├── package.json
└── node_modules/@sem-ia/cli/
```

El adopter ejecuta `claude` en raíz → recepción detecta `vault/product-owner/strategy/` vacío → propone WA con `outcome-type: vision-creation` (primer paso de la cadena por gaps). Recepción ejecuta scope-scan flat parallel + adapta template + crea WA con steps. Indica al humano: *"Step 1 pending para product-owner. Abre: `npm run po`"*. Toda la conducción de steps ocurre en sesiones dedicadas de cada rol.

## Reglas para contribuidores

### Dónde editar según el tipo de cambio

| Quiere mejorar... | Edita... |
|---|---|
| Identidad de un agente core | `.claude/agents/<rol>.md` |
| Una skill estratégica u operativa del PO | `.claude/skills/po-<skill>/SKILL.md` |
| Una skill de otro rol | `.claude/skills/<prefijo>-<skill>/SKILL.md` (`arch-`, `sec-`, etc.) |
| Diseño detallado de una skill | `.claude/skills/<prefijo>-<skill>/design.md` |
| Estructura del frontmatter de un nodo | Sección "Estructura del nodo" del SKILL.md que crea ese nodo |
| Una nota bibliográfica | `vault/architect/research/library/<fuente>.md` |
| Defaults de governance | `vault/shared/governance/<file>.md` |
| Wrapper de sesión de un rol | `vault/<rol>/CLAUDE.md` (thin — no duplicar identidad) |
| Un slash command | `.claude/commands/<name>.md` |
| Recepción | `CLAUDE.md` (root) |
| El framework distribuible | `src/<adapter\|universal\|cli>/...` |

### Lo que NUNCA se toca en PR

- `vault/product-owner/strategy/<files>` (excepto wrapper): contenido estratégico de SEM-IA-the-project. Cambios pasan por WAs `vision-creation`/`goal-definition`/`capability-creation`.
- `vault/product-owner/specs/<files>`, `vault/architect/adrs/<files>`: igual (cambios por WAs).
- `vault/architect/research/bootstrap-summary.md`: historia inmutable.

## Por qué este modelo es óptimo

- **Universal:** SEM-IA-the-project y cualquier adopter tienen estructura idéntica.
- **Role-first:** el vault refleja directamente el modelo SEM-IA. Auto-explicativo y extensible.
- **Recursivo limpio:** SEM-IA-the-project usa SEM-IA-the-framework para construirse.
- **Sin duplicación:** un concepto = un archivo. Otros archivos referencian.
- **Claude Code-native:** los artifacts viven donde Claude Code los descubre.
- **Multi-harness ready:** `src/adapters/` anticipa OpenCode, Pi, etc.
- **Distribución limpia:** un solo canal (npm + CLI).
- **Contribuciones predecibles.**
