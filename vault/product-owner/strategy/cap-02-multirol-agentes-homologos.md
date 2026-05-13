---
type: capability
id: cap-02-multirol-agentes-homologos
title: "Operación multi-rol vía agentes IA homólogos especializados"

parent: goal-4-rigor-multirol-individual

also-relates-to:
  - goal-1-auto-sostenibilidad
  - goal-2-output-auditable-multirol
  - goal-3-absorcion-coste-revision
depends-on: []
dimensions-affected: [product, technical, usability]
related-adrs: []  # vacío hoy. Latentes aplicables (step-3): ADR-latente-001 (Claude Code harness primario), ADR-latente-002 (vault role-first)

status: active   # transición aplicada por /verify del WA wa-2026-05-12-002 el 2026-05-12T05:30+02:00
operational-status: operant

fundamento-bibliografico:
  - Cagan — Inspired + Empowered (strong product team multi-rol; 4 risks abordados por custodios)
  - Bass — Software Architecture in Practice (QAs aplicados al ecosistema de agentes)
  - Ousterhout — A Philosophy of Software Design (deep modules: cada rol cohesivo con scope claro)
  - Norman — Design of Everyday Things (modelo conceptual del operador al alternar roles)
  - Nielsen — 10 heurísticas (#6 recognition over recall al elegir rol)
  - Anthropic — Claude Code Agent Skills + subagents (mecanismo nativo)

qas-bass:
  - modifiability    # añadir/redefinir roles sin tocar otros
  - modularity       # 8 agent files independientes
  - portability      # agent files YAML+MD agnósticos del harness (renderizables a otros con adapters)
  - learnability     # operador identifica rol apropiado por nombre + identidad declarada

tactics:
  - "Deep modules (Ousterhout): cada rol con interfaz simple (agent file declarativo + atajo npm) y implementación profunda (identidad + skills + protocolo de modos)"
  - "Abstraction: 8 roles core = 6 asesores custodios de dimensión (PO+Architect+Designer+Business+Security+QA) + 2 ejecutores (Developer+DevOps)"
  - "Naming conventions: nombres de rol estables, mapping 1:1 a dimensión custodiada"
  - "Use intermediary: Task tool como mecanismo unificado de invocación subagent (capacidad técnica de CAP-02; USADA por CAP-04 en checkpoints)"

tradeoffs:
  - "8 roles = más cognitive load del humano al alternar — mitigado por agente especializado conduciendo cada sesión, pero el flag de Designer (Nielsen #6) se mantiene como concern operativo"
  - "Identidades verbose en agent files (varios KB cada uno) — coste de tokens al cargar wrapper en sesión; mitigado por prompt caching de Anthropic"
  - "Cohesión de cada rol depende del agent file — si un agent file está mal especificado, su sesión opera inconsistentemente (gap 5 del WA-002 expone esto)"
  - "vault/developer/CLAUDE.md NO existe hoy — gap operativo conocido; construir cuando exista src/"

jtbd-outcome:
  quien: "Humano operador del proyecto (autor primario + colaboradores futuros + adopter)"
  job: "Sostener desarrollo de producto con cobertura multi-rol especializada sin necesitar equipo humano numeroso, alternando entre roles sin perder coherencia entre ellos"
  outcome-esperado: "Cada decisión y artefacto tiene custodio especializado responsable (anclado bibliográficamente), el humano alterna roles vía atajos npm con bajo cognitive load, y los roles se invocan mutuamente como subagentes cuando emerge necesidad cross-dominio"
---

# CAP-02 · Operación multi-rol vía agentes IA homólogos especializados

## Enunciado

El sistema provee **8 roles core** como agentes IA con identidad bibliográfica anclada y vault scope declarado: 6 asesores custodios de dimensión (product-owner, architect, designer, business-analyst, security-officer, qa) + 2 ejecutores (developer, devops). El humano alterna sesiones por rol vía atajos npm (`npm run sem|arch|des|biz|sec|qa|dev|ops`). Cada rol es también invocable como **subagente** vía Task tool para meetings, scope-scans, checkpoints y give-and-take mid-step (Cagan principio 2).

## Por qué es capability fuerte (4 criterios)

1. **Habilidad diferenciada**: tener un equipo de roles especializados con identidad y skills cargadas es propiedad observable del sistema que un humano individual no puede sostener solo. Sin CAP-02, SEM-IA es teoría sin operadores.
2. **Sirve a goals con métrica clara**: goal-4 declara *"cobertura dimensional ≥ 100 % en features producidas — todos los custodios necesarios participan vía agentes IA"*. Métrica directa.
3. **Cohesión interna**: 8 agent files + 7 wrappers (developer pendiente) + role-catalog + atajos npm + Task tool subagent — comparten el job *"materializar roles humanos especializados como agentes IA"*.
4. **No es trivialmente subcapability**: no es feature de CAP-01 (el grafo existiría sin agentes específicos), ni de CAP-03 (los WAs pueden ejecutarse manualmente sin agentes). Es la **infraestructura de operadores** sobre la que las otras descansan.

## Piezas del bootstrap que la materializan

| Pieza | Path | Rol en la capability |
|---|---|---|
| 8 agent files con identidad bibliográfica | `.claude/agents/*.md` | Identidades de los 8 roles core |
| Catálogo formal de roles | `vault/shared/governance/role-catalog.md` | Mapping rol ↔ dimensión ↔ skills ↔ atajo npm |
| 7 wrappers de sesión dedicada | `vault/<rol>/CLAUDE.md` (developer pendiente) | Entry point multi-turn por rol cuando se invoca con `npm run <rol>` |
| Atajos npm | `package.json` (scripts `sem`, `po`, `arch`, `des`, `biz`, `sec`, `qa`, `dev`, `ops`) | Affordance ergonómico para alternar sesiones |
| CLAUDE.md raíz como entry point | `CLAUDE.md` | Guía estática + tabla de roles + atajos |
| Mecanismo subagent vía Task tool | nativo Claude Code | Capacidad técnica que permite invocar cualquier rol focalizado one-shot (USADA por CAP-04 en checkpoints) |

## Relación con goals

- **Goal-4 (rigor multi-rol con humano individual)** — parent primario. Es la condición de viabilidad de goal-4: sin agentes especializados, un humano individual no puede ejercer 8 roles.
- **Goal-1 (auto-sostenibilidad)** — los agentes propios del framework conducen el dogfooding.
- **Goal-2 (verificación multi-rol)** — los roles especializados son los custodios que verifican (mecanismo materializado en CAP-04, pero los roles existen aquí).
- **Goal-3 (absorción coste revisión)** — la cobertura cross-rol del scope-scan + verify (CAP-04) descansa sobre la existencia de roles distintos custodiando dimensiones distintas.

## Criterio observable para futuros `/verify`

Una feature descompuesta de CAP-02 es verificable si cumple:
- Existe agent file conformante para cada rol declarado en `role-catalog.md`.
- El atajo npm correspondiente arranca sesión que carga el wrapper del rol y, transitivamente, el agent file.
- El rol es invocable como subagente vía Task tool (test: invocación retorna output estructurado en formato declarado).
- La identidad declarada en el agent file cita bibliografía verificable en `vault/architect/research/library/`.

## Features candidatas (preview)

1. **Estructura inline del agent file** — qué secciones canónicas tiene un agent file (identidad, dimensión custodiada, skills cargadas, modos de trabajo, vault scope, lo que NO hace, bibliografía base). Hoy declarado por convención emergente, no formalmente.
2. **Atajos npm scripts** — mapping rol ↔ comando.
3. **Wrappers `vault/<rol>/CLAUDE.md`** — entry point por sesión.
4. **Mecanismo de invocación subagente** — Task tool nativo de Claude Code (no construido por SEM-IA, sí declarado como dependencia y usado).
5. **Catálogo de roles extensible** — `role-catalog.md` con regla para añadir roles custom (adopters DeFi añaden `tokenomics-designer`, etc.).

## Notas / gaps operativos conocidos

- **`vault/developer/CLAUDE.md` no existe**. Gap conocido (verificado por Explore). README lo señala como pendiente "cuando exista código implementado en src/ bajo SEM-IA real". NO bloquea `operational-status: operant` — Developer es invocable como subagente; la sesión dedicada se construye cuando emerja necesidad real.
- Designer flagea (post-step scope-scan WA-002): la alternancia entre 8 roles tiene **cognitive load** sin mecanismo de orientación más allá de `/sessions`. Materializa Nielsen #6 (recognition over recall). Concern aparcado como feature futura de CAP-02; cuando se descomponga, Designer participa como verificador (de ahí `usability` en dimensions-affected).
- Skills de Designer y Business-analyst aún sin formalizar (operan con guía bibliográfica directa). Pendiente cuando emerjan necesidades B2C/consumer + business reales.
