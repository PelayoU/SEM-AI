---
name: po-goal-quality-check
description: "Evaluar un goal individual contra criterios bibliográficos (SMART de Doran, OKR de Doerr, alineación con visión de Cagan): si es resultado medible, si materializa la visión, si es controlable, si tiene altitud correcta, si es distinto de los demás goals. Use this skill when the Product Owner proposes a goal during inception, when reviewing existing goals during strategy-review, or when a bottom-up change questions a goal."
allowed-tools: Read Glob Grep
materializes-feature: [feature-038-po-modo-1]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): skill estratégica invocada por PO Modo 1 cuando outcome-type = goal-definition.
---

# Skill: goal-quality-check (Product Owner — lado estratégico)

## Quick reference

Aplica 6 tests con base bibliográfica al goal. Devuelve veredicto por test + recomendación final entre 6 opciones.

## When to invoke

- Durante WA `goal-definition` (caso normal), sobre cada goal candidato.

- Durante `strategy-review` (later) periódico.
- Cuando un descubrimiento bottom-up cuestiona un goal (entrada a `vision-realignment`).

## Inputs

- Nodo del goal: `vault/product-owner/strategy/goal-N.md` (frontmatter + Resultado esperado + Métricas + Conexión con la visión).
- Visión padre.
- Goals hermanos.

## Process — 6 tests

| # | Test | Fuente | Pregunta |
|---|---|---|---|
| 1 | ¿Resultado o actividad? | SMART · Specific | ¿Describe estado del mundo o acciones? |
| 2 | ¿Es medible? | SMART + OKR (KR) | ¿Hay métrica explícita? Binaria preferible. |
| 3 | ¿Materializa la visión? | Cagan | ¿Qué afirmación de la visión se vuelve verificable? |
| 4 | ¿Controlable o aspiracional? | Lean | ¿Depende del producto o de mercado externo? |
| 5 | ¿Altitud correcta? | Pyramid model SEM-IA | ¿Resultado intermedio o feature/visión disfrazada? |
| 6 | ¿Distinto de los demás? | (no overlap) | ¿Solapa con goal hermano? |

## Output format

Para cada test: ✅ / ⚠️ / ❌ + diagnóstico.

**Recomendación final** — una de:
1. **Mantener tal cual.**
2. **Reformular el enunciado.**
3. **Mover a milestone del roadmap** (era actividad).
4. **Mover a capability** (era habilidad).
5. **Fundir con otro goal.**
6. **Eliminar.**

## Bibliographic foundation

- `vault/architect/research/library/doerr-okrs.md` — Objectives + Key Results, 70% target.
- `vault/architect/research/library/doran-smart.md` — SMART original (1981).
- `vault/architect/research/library/cagan-product-vision.md` — alineación con visión durable.

## Full design

`./design.md` — incluye ejemplos positivo (goal-1 reformulado) y negativo ("Tener documentación buena").

## Limitations

- Los tests no son ortogonales.
- La frontera "controlable / aspiracional" puede ser difusa — forzar la decisión.
- La skill rechaza pero no inventa goals. Devuelve la conversación al humano.

## Status lifecycle

Esta skill no produce nodos nuevos — valida un goal existente o candidato. NO modifica el `status` del nodo `goal`; emite veredicto. La transición de `draft` a `active` la aplica recepción al `/verify` del WA vía `on-close`, **siempre que** este quality-check pase como criterio de cierre.

## WA mapping

Esta skill se invoca dentro de:

- **`goal-definition`** — caso normal.
- **`goal-definition`** (cuando se añade un goal nuevo post-inception).
- **`strategy-review`** (skill later — revisión periódica de goals).
