---
name: arch-capability-viability-review
description: "Evaluar viabilidad técnica de una capability candidata: qué quality attributes implica (Bass), qué tactics arquitectónicas requiere, si introduce tradeoffs problemáticos, si es coherente con la arquitectura existente. Use this skill when the Product Owner (lado estratégico) proposes a capability with technical dimensions during inception, when a new capability is added post-inception, or when reviewing existing capability whose technical cost has been re-evaluated."
allowed-tools: Read Glob Grep
materializes-feature: [feature-018-slash-scope-scan, feature-019-slash-verify]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): skill Architect invocada como advisor en scope-scan multi-rol (feature-018) cuando capability-creation está en discovery. También aplicable durante /verify (feature-019) si la dimensión technical fue declarada en el WA.
---

# Skill: capability-viability-review (Architect)

## Quick reference

Aplica 5 pasos para validar viabilidad técnica de una capability candidata. Output: hallazgos por paso + recomendación final entre 4 opciones.

## When to invoke


- Capability nueva post-inception que toca dimensión técnica.
- Revisión de capability cuyo coste técnico se ha reevaluado.

## Inputs

- Capability candidata (frontmatter + descripción + justificación).
- Visión y goals ascendentes.
- ADRs existentes en `vault/architect/adrs/`.
- Capabilities hermanas.

## Process — 5 pasos

1. **Identificar Quality Attributes implícitos** (Bass): modifiability, performance, security, testability, deployability, integrability. Listar 2-3 dominantes.
2. **Identificar tactics requeridas** por cada QA dominante (catálogos de Bass cap. 4-13).
3. **Detectar tradeoffs entre QAs**: more security ↔ less performance, more flexibility ↔ less simplicity, etc. Marcar tradeoffs críticos.
4. **Verificar coherencia con ADRs y arquitectura existente**. Si contradicción → activar `coherence-evaluation`.
5. **Evaluar fitness functions necesarias** (Ford): ¿qué fitness function protegería la propiedad arquitectónica nueva?

## Output format

Hallazgos por paso + diagnóstico.

**Recomendación final**:
1. **Aprobar** — viable y coherente.
2. **Aprobar con condiciones** — requiere ADR explícito o fitness function nueva.
3. **Reformular** — concepto válido, formulación introduce conflicto técnico.
4. **Rechazar** — no viable con la arquitectura actual.

## Bibliographic foundation

- `vault/architect/research/library/bass-software-architecture.md` — QAs, ASRs, ADD.
- `vault/architect/research/library/ford-evolutionary-architecture.md` — fitness functions, appropriate coupling.
- `vault/architect/research/library/martin-clean-architecture.md` — Dependency Rule, capas.
- `vault/architect/research/library/ousterhout-philosophy-software-design.md` — modules, information hiding.

## Full design

`./design.md` — incluye ejemplo aplicado a CAP-2 (memoria compartida en grafo declarativo).

## Limitations

- Identificar QAs es subjetivo.
- Tradeoffs no siempre cuantificables — requiere confirmación humana.
- En proyectos en bootstrapping, "coherencia con arquitectura existente" es delgada — la skill se vuelve predictiva.

## Modos de input

Esta skill opera en dos modos según el contexto:

| Modo | Contexto | Fuente de input |
|---|---|---|
| **Prospectivo** | WA `capability-creation` step Architect (caso normal) | Capability candidata aún no implementada |
| **Retroactivo** | Audit ad-hoc de capability ya implementada (Architect se incorpora a proyecto maduro o capability legada que requiere review) | Código existente que materializa la capability — review de QAs ya materializados |

**En modo prospectivo**, identifico QAs implícitos y tactics requeridas predictivamente. La capability aún no tiene código.

**En modo retroactivo**, leo el código asociado a las features que la capability agrupa, identifico QAs ya materializados (positiva o negativamente), y emito veredicto sobre coherencia con arquitectura existente.

Mismos 5 pasos, distinta naturaleza temporal.

## Status lifecycle

Si esta skill produce un review en `vault/architect/research/cap-N-viability.md`: `status: draft` inicial. Transición a `active` vía `on-close` del WA al `/verify`. Si emite veredicto sin archivo formal (caso common para review preliminary durante inception), no aplica lifecycle — el output queda en el Progreso del WA.

## WA mapping

Esta skill se invoca dentro del template **`capability-creation`** (fase `discovery`), step `architect` opcional condicional a `technical en dimensions`. También invocable ad-hoc desde sesión Architect cuando se necesita review retroactivo de capability legada.
