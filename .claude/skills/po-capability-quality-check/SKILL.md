---
name: po-capability-quality-check
description: "Evaluar una capability candidata contra criterios bibliográficos (Rumelt kernel estratégico, Torres OST, Cagan visión): es habilidad (no feature ni actividad), parent claro, alineada con guiding policy, no solapa con otras capabilities, cross-links explícitos, decomponible en features. Use this skill when the Product Owner proposes a capability during inception, when reviewing capabilities during strategy-review, or when a new capability is added post-inception (Product Owner — strategic side)."
allowed-tools: Read Glob Grep
materializes-feature: [feature-038-po-modo-1]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): skill estratégica invocada por PO Modo 1 cuando outcome-type = capability-creation, antes de cerrar capability.
---

# Skill: capability-quality-check (Product Owner — lado estratégico)

## Quick reference

Aplica 6 tests con base bibliográfica a la capability. Devuelve veredicto por test + recomendación final entre 6 opciones.

## When to invoke

- Durante WA `capability-creation` (caso normal), sobre cada capability candidata.

- Durante `strategy-review` (later).
- Cuando se propone capability nueva post-inception.

## Inputs

- Capability candidata (frontmatter + descripción + justificación).
- `vault/product-owner/strategy/vision.md` (para guiding policy).
- `vault/product-owner/strategy/goal-N.md` (parent y posibles cross-links).
- Otras capabilities ya existentes (overlap detection).

## Process — 6 tests

| # | Test | Fuente | Pregunta |
|---|---|---|---|
| 1 | ¿Habilidad o feature/actividad? | (modelo SEM-IA) | "El sistema puede X" vs. "Construir X" |
| 2 | ¿Parent claro? | (jerarquía) | Si goal padre desapareciera, ¿seguiría siendo necesaria? |
| 3 | ¿Sirve a guiding policy? | Rumelt | ¿Coherent action o idea desconectada? |
| 4 | ¿Distinta? | (no overlap) | ¿Hay otra capability que cubra el mismo terreno? |
| 5 | ¿Cross-links explícitos? | (modelo grafo) | `also-relates-to`, `dimensions-affected` declarados? |
| 6 | ¿Decomponible en features? | Torres OST | ¿2-5 features tangibles imaginables? |

## Output format

Para cada test: ✅ / ⚠️ / ❌ + diagnóstico.

**Recomendación final** — una de:
1. **Aprobar tal cual.**
2. **Reformular el enunciado.**
3. **Mover a feature** (era feature, no capability).
4. **Mover a goal** (subió de altitud).
5. **Fundir con capability X.**
6. **Eliminar.**

## Bibliographic foundation

- `vault/architect/research/library/rumelt-good-strategy.md` — capability como coherent action del kernel.
- `vault/architect/research/library/torres-continuous-discovery.md` — capability como solución a oportunidad.
- `vault/architect/research/library/cagan-product-vision.md` — alineación con visión durable.

## Full design

`./design.md` — incluye ejemplos positivo (CAP-1 custodios homólogos) y negativo ("Implementar vault-cli").

## Limitations

- La distinción capability / feature es la más resbaladiza del modelo. Usar test "decomponible en 2-5 features" para resolver dudas.
- Detectar overlap requiere lectura comparativa con TODAS las capabilities — usar lectura focalizada por dimensiones.

## Status lifecycle

Esta skill no produce nodos nuevos — valida una capability candidata. NO modifica el `status`; emite veredicto. La transición de `draft` a `active` la aplica recepción al `/verify` del WA vía `on-close`.

## WA mapping

Esta skill se invoca dentro de:

- **`capability-creation`** — caso normal.
- **`capability-creation`** (template estándar post-inception).
- **`strategy-review`** (skill later).
