---
type: capability
id: cap-04-verificacion-multirol-cruzada
title: "Verificación multi-rol cruzada en checkpoints uniformes"

parent: goal-2-output-auditable-multirol

also-relates-to:
  - goal-3-absorcion-coste-revision
  - goal-4-rigor-multirol-individual
depends-on:
  - cap-02-multirol-agentes-homologos  # consume la capacidad de invocar subagentes
dimensions-affected: [product, quality, technical]
related-adrs: []  # vacío hoy. Latentes aplicables (step-3): ADR-latente-009 (tres-checkpoints-uniformes), ADR-latente-010 (algoritmo-verifiers)

status: active   # transición aplicada por /verify del WA wa-2026-05-12-002 el 2026-05-12T05:30+02:00
operational-status: operant

fundamento-bibliografico:
  - Cagan — Inspired (4 risks + principio 2 give-and-take)
  - Bass — Software Architecture in Practice (testability como QA, verificación cruzada como tactic)
  - Ford et al. — Building Evolutionary Architectures (fitness functions + verificación continua)
  - Nygard — ADRs (revisión cruzada de decisiones)
  - Shostack — Threat Modeling (verificación security cuando aplica)

qas-bass:
  - testability      # cada WA es verificable al cierre por algoritmo declarativo
  - modifiability    # añadir checkpoints sin tocar otros
  - independence     # custodios independientes operando en paralelo (flat parallel) — terminología Bass estándar (sustituye `separability` ajustado tras viability-review)
  - auditability     # output de cada checkpoint queda como artefacto auditable

tactics:
  - "Three uniform checkpoints: discovery review al crear WA / step checkpoint post-step / sign-off al verify — mismo mecanismo en los 3"
  - "Declarative algorithm: `verifiers = {custodian(d) : d ∈ dimensions-affected}` deriva los verificadores automáticamente de dimensions-affected; sin lógica imperativa"
  - "Flat parallel (no cascade): los asesores se invocan EN PARALELO en un solo mensaje, no en secuencia — discovery colaborativa antes de comprometer scope"
  - "Give-and-take mid-step (Cagan principio 2): subagentes invocables ad-hoc durante un step para sanity checks tempranos"
  - "AC traceability: trazabilidad AC→tests vía `// @ac-coverage: AC-X1, AC-X2` en archivos de test — tactic operativa de la verificación, no capability propia"

tradeoffs:
  - "Scope-scan flat parallel cuesta tokens — ~$1.5-2 por WA con prompt caching, despreciable vs el coste de rework por drift no detectado"
  - "Algoritmo `verifiers = {custodian(d)}` puede infra-cubrir si dimensions-affected está mal declarado (gap 6 del WA-002 + flag Architect: dimensions honestas, no mecánicas)"
  - "Post-step scope-scan es obligatorio por protocolo pero sin enforcement técnico — depende de la disciplina del agente activo (planned: hooks)"
  - "Verificadores en paralelo NO cascadean — no pueden coordinarse entre sí (cada uno escribe independiente); coordinación queda al rol orquestador (recepción/PO) que consolida"

jtbd-outcome:
  quien: "Humano operador + agentes en cada checkpoint + verificadores al cierre del WA"
  job: "Validar cada decisión, artefacto o cambio significativo del proyecto con cobertura cross-rol antes de que se cierre o avance al siguiente step, de forma que el drift se detecte pre-cierre (no post-cierre, no en producción)"
  outcome-esperado: "Cada WA cerrado tiene firma cross-rol de los custodios de sus dimensions-affected; cada step completado tiene scope-scan post-step que captura drift bottom-up; y los 4 risks de Cagan + transversales (security, quality, operations) tienen custodio asignado cuando aplican"
---

# CAP-04 · Verificación multi-rol cruzada en checkpoints uniformes

## Enunciado

El sistema aplica **scope-scan flat parallel multi-rol** en **3 checkpoints uniformes** del lifecycle del WA: (1) **discovery review** al crear WA, (2) **step checkpoint** post-step, (3) **sign-off** al `/verify`. Algoritmo declarativo `verifiers = {custodian(d) : d ∈ dimensions-affected}`. Cubre los 4 risks de Cagan (value, usability, viability technical, business viability) + transversales (security, quality, operations). Soporta **give-and-take mid-step** vía subagentes — el rol activo invoca a otros cuando emerge duda relevante a otro dominio (Cagan principio 2).

## Por qué es capability fuerte (4 criterios)

1. **Habilidad diferenciada**: la verificación multi-rol cruzada NO es propiedad emergente — es mecanismo declarativo con 3 checkpoints uniformes y algoritmo explícito. Sin CAP-04, los WAs cierran solos sin verificación cruzada estructural.
2. **Sirve a goals con métrica clara**: goal-2 declara *"100 % de WAs cerrados con verificación multi-rol completa"* y goal-3 *"≥ 80 % de drift detectado pre-cierre"*. Métricas directas.
3. **Cohesión interna**: 3 checkpoints uniformes + algoritmo verifiers + give-and-take + skills `*-viability-review` + `coherence-evaluation` + `coupling-detection` + `threat-modeling` + skills `*-quality-check` — comparten el job *"verificación cruzada antes de cierre"*.
4. **No es trivialmente subcapability**: no es feature de CAP-03 (los WAs podrían cerrarse sin verificación cruzada — sería opcional). CAP-04 es el **mecanismo de calidad cross-rol** que hace los WAs auditables.

## Piezas del bootstrap que la materializan

| Pieza | Path | Rol en la capability |
|---|---|---|
| Slash `/scope-scan "<propuesta>"` | `.claude/commands/scope-scan.md` | Reunión multi-rol on-demand (6 asesores en paralelo) |
| Slash `/verify` | `.claude/commands/verify.md` | Sign-off al cierre con algoritmo declarativo |
| Tres checkpoints uniformes del WA lifecycle | declarado en CLAUDE.md raíz + cada agent file | Discovery review / step checkpoint / sign-off |
| `verification-matrix.md` | `vault/shared/governance/verification-matrix.md` | Guía orientativa de dimensions típicas por outcome-type (no algoritmo) |
| Skill `capability-viability-review` (Architect) | `.claude/skills/architect/capability-viability-review/` | Verificación de capability post-derivación |
| Skill `feature-viability-review` (Architect) | `.claude/skills/architect/feature-viability-review/` | Verificación de feature pre-implementación |
| Skill `coherence-evaluation` (Architect) | `.claude/skills/architect/coherence-evaluation/` | Detección de contradicciones vs ADRs |
| Skill `coupling-detection` (Architect) | `.claude/skills/architect/coupling-detection/` | Detección de acoplamientos no declarados |
| Skill `threat-modeling` (Security Officer) | `.claude/skills/security-officer/threat-modeling/` | STRIDE + Shostack para features sensibles |
| Skills `vision/goal/capability/feature-quality-check` (PO) | `.claude/skills/product-owner/...quality-check/` | Tests bibliográficos por tipo de nodo |
| Give-and-take mid-step (subagent vía Task tool) | usa la pieza de CAP-02 | Sanity checks tempranos durante un step (Cagan principio 2) |

## Relación con goals

- **Goal-2 (output auditable, coherente y verificado multi-rol)** — parent primario. CAP-04 es la materialización operativa de "verificado multi-rol".
- **Goal-3 (absorción coste revisión)** — *"≥ 80 % de drift detectado pre-cierre"* es métrica de CAP-04. Sin verificación cruzada, el coste se traslada al humano.
- **Goal-4 (rigor multi-rol con humano individual)** — la cobertura cross-rol que un humano individual no puede dar solo, la dan los verificadores derivados de dimensions-affected.

## Criterio observable para futuros `/verify`

Una feature descompuesta de CAP-04 es verificable si cumple:
- Todo WA del vault tiene `verifiers-required` derivable del algoritmo `{custodian(d) : d ∈ dimensions-affected}`.
- Cada step completado tiene post-step scope-scan output registrado en Progreso del WA.
- `/verify` aplica `on-close` transitions solo si todos los verificadores aprueban.
- Skills `*-quality-check` y `*-viability-review` se invocan en el contexto que su `description` declara.
- AC trazables a tests vía `// @ac-coverage:` cuando hay tests (planned: feature `coverage` del CAP-08 CLI).

## Features candidatas (preview)

1. **Slash `/scope-scan`** y **`/verify`** — implementación de slash commands con invocación flat parallel via Task tool.
2. **Algoritmo declarativo `verifiers = {custodian(d)}`** — implementado en `/verify` consultando `dimensions.md`.
3. **Tres checkpoints uniformes del WA** — protocolo declarado en cada agent file; posiblemente skill compartida `checkpoint-protocol` futura.
4. **Skills de viability/coherence/coupling/threat-modeling/quality-check** (10 skills construidas).
5. **Mecanismo AC traceability** `// @ac-coverage:` — convención + futuro check del CAP-08 CLI.
6. **Give-and-take mid-step** — convención + ejemplos en `workflows.md`.

## Notas / gaps operativos conocidos

- **Algoritmo `verifiers = {custodian(d)}` puede infra-cubrir** si dimensions-affected está mal declarado (gap 6 del WA-002 — contaminación + flag Architect: dimensions honestas, no mecánicas). Mitigación: el scope-scan inicial al crear WA detecta dimensions-affected; el filtro PO valida.
- **Post-step scope-scan obligatorio sin enforcement técnico** — depende de disciplina del agente activo. Planned: hooks de Claude Code (P2 del README) lo harán determinístico.
- **AC traceability `// @ac-coverage:` declarado pero sin tool de verificación** — feature `coverage` del CAP-08 CLI (planned) lo automatizará.
- **Framework regression detection** (flag QA): editar un agent file o SKILL.md puede romper protocolo sin detección. Pendiente como WA futuro de gaps (decisión: NO añadir como capability planned ahora — recomendación QA confirmada).
