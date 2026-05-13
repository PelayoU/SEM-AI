---
type: capability
id: cap-06-visibilidad-operativa
title: "Visibilidad operativa del estado y progreso del proyecto"

parent: goal-3-absorcion-coste-revision

also-relates-to:
  - goal-1-auto-sostenibilidad
  - goal-2-output-auditable-multirol
  - goal-4-rigor-multirol-individual
depends-on: []
dimensions-affected: [product, usability, technical]
related-adrs: []  # vacío hoy

status: active   # transición aplicada por /verify del WA wa-2026-05-12-002 el 2026-05-12T05:30+02:00
operational-status: operant

fundamento-bibliografico:
  - Nielsen — 10 heurísticas de usabilidad (#1 visibility of system status, #6 recognition over recall, #9 error recovery)
  - Norman — Design of Everyday Things (modelo conceptual del operador)
  - Cooper — About Face (awareness del contexto de trabajo vs feedback de la acción inmediata)
  - Cagan + Patton — Dual Track Discovery + Delivery (visualización de tracks paralelos)
  - Bass — Software Architecture in Practice (usability como QA)

qas-bass:
  - usability        # operador navega el sistema con bajo cognitive load
  - learnability     # newcomer entiende el estado del proyecto sin training
  - performance      # slash responses esperablemente < 2 segundos
  - observability    # estado del proyecto es legible desde múltiples ángulos

tactics:
  - "Visibility heuristic (Nielsen #1): slash `/status` provee panorámica permanente del subgrafo + WAs + backlog + ADRs"
  - "Recognition over recall (Nielsen #6): `/sessions` lista comandos disponibles para no requerir memoria"
  - "Error recovery (Nielsen #9): Progreso entries en cada WA permiten retomar trabajo sin redescubrir contexto"
  - "Dual track visualization (Cagan/Patton): `/status` agrupa WAs por track (Discovery / Delivery / Operations / Meta) con vista de salud"
  - "Distinct perspectives (Cooper): el sistema diferencia visibilidad del estado del PROYECTO (subgrafo + WAs + backlog) de visibilidad del estado de la SESIÓN del operador (rol activo + step actual + next action)"

tradeoffs:
  - "Slash commands son comando-driven — requieren recall del comando; mitigado por `/sessions` como listado"
  - "Panorámica saturada si proyecto crece — `/status` puede volverse verbose con cientos de WAs/specs; mitigación futura: filtros y paginación"
  - "Progreso entries son texto libre — útiles para audit, costoso parsear automáticamente; tradeoff vs schema rígido"
  - "No hay UI gráfica — solo CLI/terminal; aceptable para target técnico (ingenieros), inaccesible para roles no-técnicos (consciente)"

jtbd-outcome:
  quien: "Humano operador (autor primario alternando entre roles + colaboradores futuros + adopter externo)"
  job: "Saber en cualquier momento qué está activo en el proyecto, en qué fase está cada bloque de trabajo, qué viene a continuación — sin tener que reconstruir el contexto desde cero"
  outcome-esperado: "El operador valida el estado conocido en vez de descubrirlo; al cerrar sesión y volver, retoma con panorámica completa; al alternar entre roles, sabe dónde está y qué viene; el coste de revisar la IA se absorbe vía estado siempre legible"
---

# CAP-06 · Visibilidad operativa del estado y progreso del proyecto

## Enunciado

El sistema provee al humano operador **panorámica del estado del proyecto**: subgrafo estratégico (visión + goals + capabilities), WAs activos agrupados por track (Discovery/Delivery/Operations/Meta vía Dual Track Cagan/Patton), backlog emergente, features por status, ADRs por status. Mecanismo: **slash commands** (`/status`, `/wa`, `/sessions`) + **ritual de inicio del PO** al arrancar sesión + **Progreso entries** en cada WA. Aplica heurística **Nielsen #1** (visibility of system status). Diferencia explícitamente **visibilidad del estado del PROYECTO** (subgrafo + WAs + backlog) de **visibilidad del estado de la SESIÓN del operador** (rol activo + step actual + next action) — Cooper: son modelos conceptuales distintos que requieren superficies distintas.

## Por qué es capability fuerte (4 criterios)

1. **Habilidad diferenciada**: visibilidad operativa es propiedad UX/DX directa del sistema. Sin CAP-06, el humano opera ciego — no sabe qué hay activo, qué viene, qué se ha completado. Es habilidad fuerte específica.
2. **Sirve a goals con métrica clara**: goal-3 (*"la revisión humana es validación, no descubrimiento"*) requiere visibilidad estructural. Sin CAP-06, goal-3 es aspiracional sin mecanismo.
3. **Cohesión interna**: 5 piezas (slash `/status`, `/wa`, `/sessions`, ritual de inicio PO, Progreso entries) comparten el job *"hacer visible el estado del proyecto y de la sesión"*.
4. **No es trivialmente subcapability**: no es feature de CAP-03 (los WAs existirían sin slash de visibilidad), ni de CAP-02 (los agentes operarían sin panorámica). Es la **capa de observabilidad** para el humano.

## Piezas del bootstrap que la materializan

| Pieza | Path | Rol en la capability |
|---|---|---|
| Slash `/status` | `.claude/commands/status.md` | Panorámica del proyecto (subgrafo + WAs + backlog + ADRs por track) |
| Slash `/wa` | `.claude/commands/wa.md` | Detalle del WA activo en contexto |
| Slash `/sessions` | `.claude/commands/sessions.md` | Lista de modos de trabajo + atajos npm |
| Ritual de inicio del PO | declarado en `vault/product-owner/CLAUDE.md` y agent file PO | Panorámica al arrancar sesión, lectura ligera del vault, presentación al humano |
| Progreso entries en WAs | convención del proyecto en cada WA archivado/activo | Audit-ready trail por step completado, handoff hacia el siguiente |
| Dual Track explicitado en `/status` | propiedad emergente | Vista agrupada de WAs por Discovery/Delivery |

## Relación con goals

- **Goal-3 (absorción coste revisión)** — parent primario. *"Revisión es validación, no descubrimiento"* es directamente CAP-06.
- **Goal-1 (auto-sostenibilidad)** — `/status` provee transparencia del propio dogfooding (cuántos WAs cerrados, cuáles activos, salud del Dual Track).
- **Goal-2 (output auditable)** — Progreso entries son evidencia auditable; `/status` y `/wa` exponen el grafo en cualquier momento.
- **Goal-4 (rigor multi-rol con humano individual)** — el humano que alterna entre 8 roles necesita visibilidad para no perderse (Nielsen #1 + Norman: modelo conceptual del estado).

## Criterio observable para futuros `/verify`

Una feature descompuesta de CAP-06 es verificable si cumple:
- `/status` retorna en tiempo aceptable (esperable < 2s) panorámica completa (subgrafo + WAs + backlog + features + ADRs por status).
- `/wa` retorna detalle del WA activo aplicable al contexto del rol.
- `/sessions` lista modos de trabajo + atajos disponibles.
- Cada WA activo tiene Progreso entries para cada step completado.
- Ritual de inicio del PO ejecuta lecturas declaradas en agent file y presenta panorámica antes de procesar propuesta humana.

## Features candidatas (preview)

1. **Slash `/status`** — implementación de query agregadora.
2. **Slash `/wa`** — detección del WA activo aplicable al contexto + presentación.
3. **Slash `/sessions`** — listado fijo de modos + atajos npm.
4. **Ritual de inicio del PO** — protocolo declarado, posiblemente skill futura.
5. **Formato de Progreso entry** — estructura canónica de entradas por step (resumen + artefactos + decisiones + "para el siguiente step" + flags aparcados).
6. **Vista Dual Track** — agrupación de WAs por track (Discovery / Delivery / Operations / Meta) en `/status`.
7. **Filtros y paginación de `/status`** (planned cuando proyecto crezca a cientos de WAs).

## Notas / gaps operativos conocidos

- **`/status`, `/wa`, `/sessions`** son slash de Claude Code — su implementación está en el harness. SEM-IA declara el contrato (qué retornan) pero el comportamiento detallado de la implementación es del harness.
- **Slash commands no son portables a otros harnesses** sin adapter — parte de CAP-08 (planned).
- **Cognitive load del operador con 8 roles** (Designer flag preservado): Nielsen #6 (recognition over recall) requiere que `/sessions` sea consultable rápidamente. Cubierto por `/sessions` pero mejorable con UI visual futura.
- **Consistencia terminológica cross-rol** (Designer flag preservado, Nielsen #4): los 8 roles tienen identidades distintas con jerga propia; CAP-06 muestra estados pero no homologa jerga. Aparcado como gap menor.
