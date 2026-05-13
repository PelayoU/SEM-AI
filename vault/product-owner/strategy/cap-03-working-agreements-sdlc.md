---
type: capability
id: cap-03-working-agreements-sdlc
title: "Coordinación de trabajo vía Working Agreements indexados por fase SDLC"

parent: goal-7-ciclo-vida-producto

also-relates-to:
  - goal-1-auto-sostenibilidad
  - goal-2-output-auditable-multirol
  - goal-3-absorcion-coste-revision
depends-on: []
dimensions-affected: [product, technical, operations]
related-adrs: []  # vacío hoy. Latentes aplicables (step-3): ADR-latente-007 (fases SDLC redefinibles), ADR-latente-008 (backlog-como-query)

status: active   # transición aplicada por /verify del WA wa-2026-05-12-002 el 2026-05-12T05:30+02:00
operational-status: operant

fundamento-bibliografico:
  - Patton — User Story Mapping (narrative flow + thin slices)
  - Cohn — User Stories Applied (INVEST applied to backlog items)
  - Cagan + Patton — Dual Track Discovery + Delivery
  - Ford et al. — Building Evolutionary Architectures (templates como fitness functions del proceso)
  - Bass — Software Architecture in Practice (templates como decisiones arquitectónicas del workflow)

qas-bass:
  - modifiability    # añadir/refinar templates sin tocar workflow existentes
  - deployability    # cada WA es deployable unit de trabajo
  - testability      # WA cierra solo si closure-criteria + verifiers aprueban
  - evolvability     # adopters pueden añadir templates y redefinir fases

tactics:
  - "Separation of concerns: templates indexados por fase SDLC (discovery/design/implementation/operations/meta), cada uno con outcome-type único"
  - "Declarative structure: WA es frontmatter + steps + scope + on-close — sin lógica imperativa"
  - "Emergent state: backlog NO es estructura persistente nueva, emerge como query sobre nodos con `status: ready-for-implementation`"
  - "Standardized handoff: cada agent file declara protocolo de handoff explícito step→step (marca step done + Progreso entry + post-step scope-scan + handoff verbal)"
  - "Configurable framework: adopters pueden añadir outcome-types nuevos y redefinir fases SDLC para SDLCs custom (SAFe, lean, DeFi-specific, etc.)"

tradeoffs:
  - "Workflow templates como YAML pueden ser verbose — coste de mantenimiento si crecen muchos templates; mitigado por extensibilidad"
  - "Backlog-como-query es O(N) sobre archivos del vault — aceptable hasta cientos de nodos; degrada con miles (fitness function a vigilar)"
  - "Estado de WA distribuido en archivos individuales (no UI consolidada) — `/status` slash es el agregador, pero no es ground truth (los archivos sí)"
  - "Protocolo handoff explícito es manual hoy — sin hooks (gap planned: hardening con hooks en P2 del README)"

jtbd-outcome:
  quien: "Humano operador + agentes ejecutando cada step + verificadores al cierre"
  job: "Coordinar bloques de trabajo multi-rol cubriendo el ciclo SDLC completo (discovery → design → implementation → operations) con scope autorizado, criterios de cierre observables y transiciones de status declarativas"
  outcome-esperado: "Cualquier bloque de trabajo se conduce bajo un WA con outcome-type clasificado, steps multi-rol con active-role explícito, scope-allowed/forbidden auditable, closure-criteria evaluable y on-close transitions aplicadas automáticamente al /verify"
---

# CAP-03 · Coordinación de trabajo vía Working Agreements indexados por fase SDLC

## Enunciado

El sistema conduce cada bloque de trabajo bajo un **Working Agreement (WA) declarativo** con `outcome-type`, `phase` SDLC, `steps` multi-rol, `scope-allowed/forbidden`, `closure-criteria` y `on-close` transitions. **14 templates por fase SDLC** (discovery/design/implementation/operations/meta) capturan workflows enterprise en formato AI-ejecutable. El backlog emerge como **query** sobre nodos con `status: ready-for-implementation` (sin estructura persistente nueva). Handoff explícito step→step con entrada de Progreso audit-ready en el WA.

## Por qué es capability fuerte (4 criterios)

1. **Habilidad diferenciada**: encoded enterprise workflows en formato AI-ejecutable es la contribución central de SEM-IA según bootstrap-summary. Sin CAP-03, agentes operan ad-hoc sin coordinación auditable.
2. **Sirve a goals con métrica clara**: goal-7 *"cobertura del ciclo SDLC completo en templates"* + goal-1 *"≥ 90 % del desarrollo de SEM-IA pasa por sus propios WAs"*. Dos métricas directas.
3. **Cohesión interna**: 4 sub-mecanismos (WA structure declarativa + workflow templates SDLC + backlog emergente + handoff explícito) comparten el job *"coordinar trabajo de forma trazable"*. En el límite del test capability-quality-check #6 (decomponible en 2-5 features) pero defendible — los 4 son inseparables del job.
4. **No es trivialmente subcapability**: no es feature de CAP-01 (el grafo existiría sin WAs como nodos en él), ni de CAP-02 (los agentes pueden operar sin WAs aunque caóticamente). Es el **mecanismo de coordinación** propio.

## Piezas del bootstrap que la materializan

| Pieza | Path | Rol en la capability |
|---|---|---|
| Catálogo de 14 templates por fase SDLC | `vault/shared/governance/workflows.md` | Templates de WA por outcome-type |
| Estructura inline del WA | declarada en `CLAUDE.md` raíz sección "Estructura de un Working Agreement" | Frontmatter + steps + scope + closure-criteria + on-close |
| Slash `/wa` | `.claude/commands/wa.md` | Detalle del WA activo en contexto |
| Backlog emergente como query | propiedad emergente del status del nodo | Sin estructura nueva — query sobre `status: ready-for-implementation` |
| Protocolo handoff explícito | declarado en cada agent file (sección "Al completar tu step") | Step done + Progreso entry + post-step scope-scan + handoff verbal |
| Estados canónicos del WA | declarado en `CLAUDE.md` raíz + `workflows.md` | `active` → archivado al `/verify` (+ `aborted` propuesto en gap 1 del WA-002) |

## Relación con goals

- **Goal-7 (ciclo de vida producto completo)** — parent primario. Los 14 templates cubren las 5 fases SDLC más meta. Métrica de cumplimiento citada literalmente: *"cobertura del ciclo SDLC completo en templates"*.
- **Goal-1 (auto-sostenibilidad)** — *"≥ 90 % del desarrollo de SEM-IA pasa por sus propios WAs"* es métrica directa.
- **Goal-2 (output auditable)** — los WAs son la unidad de auditoría: cada bloque de trabajo deja archivo audit-ready.
- **Goal-3 (absorción coste revisión)** — el handoff explícito step→step + Progreso entries reducen el coste de "saber qué viene"; el humano valida en vez de descubrir.

## Criterio observable para futuros `/verify`

Una feature descompuesta de CAP-03 es verificable si cumple:
- Cada WA del vault tiene `outcome-type` clasificado del catálogo de `workflows.md`.
- `steps` declaran `active-role` válido del role-catalog.
- `closure-criteria` son evaluables objetivamente al `/verify`.
- `on-close` transitions referencian paths existentes y status válidos.
- Al cerrar el WA, las transiciones declaradas se aplican y el WA se archiva.

## Features candidatas (preview)

1. **Estructura inline del WA** (frontmatter + secciones) declarada en CLAUDE.md raíz — pendiente formalizar definitivamente y resolver gaps 1/3 del anexo (status `aborted`, campos de pivot).
2. **14 workflow templates** por fase SDLC en `workflows.md` — extensibles por adopters.
3. **Backlog query** mechanism — primitivo hoy, posiblemente skill futura `backlog-query` en pending.
4. **Protocolo handoff explícito** declarado por convención en cada agent file — posiblemente formalizar como skill compartida.
5. **Estados canónicos del WA** + transiciones — incluye propuesta de `aborted` (gap 1 del WA-002).
6. **Catálogo de outcome-types extensible** — adopters añaden templates custom (DeFi: `tokenomics-change`; database: `database-migration`).

## Notas / gaps operativos conocidos

- **Template `capability-creation` está pensado para UNA capability** (gap 3 del WA-002). El WA-002 actual es bottom-up batch — improvisó adaptación del template. Pendiente: añadir variante `capability-batch-extraction` o flag `mode` al template `capability-creation`.
- **No hay protocolo formal para pivotar WA mid-flight** (gap 4 del WA-002). Pendiente.
- **Hardening determinístico via hooks** (P2 del README, planned) reforzaría CAP-03: pre-commit hooks que validan integridad de WA, SessionStart hooks que leen `/status`, etc. Hoy todo es probabilístico (~99% confiabilidad).
