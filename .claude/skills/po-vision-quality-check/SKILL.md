---
name: po-vision-quality-check
description: "Evaluar si un enunciado de visión cumple criterios bibliográficos (Cagan, Sinek, Rumelt, JTBD): customer-centric, durable 5-10 años, articula propósito (Why), ambiciosa pero anclada. Use this skill when the Product Owner proposes a vision statement during inception, when reviewing existing vision after bottom-up changes, or when the user asks to revise the project vision."
allowed-tools: Read Glob Grep
materializes-feature: [feature-038-po-modo-1]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): skill estratégica invocada por PO Modo 1 cuando outcome-type = vision-creation.
---

# Skill: vision-quality-check (Product Owner — lado estratégico)

## Quick reference

Aplica 7 tests con base bibliográfica al enunciado de la visión. Devuelve veredicto por test + recomendación final entre 5 opciones.

## When to invoke

- Durante WA `vision-creation` (caso normal).

- Durante `vision-realignment` (later) cuando un cambio bottom-up cuestiona la visión.
- Cuando el usuario pide "revisa la visión".

## Inputs

- Enunciado a evaluar (string).
- Opcional: `vault/product-owner/strategy/vision.md` completo.

## Process — 7 tests

| # | Test | Fuente | Pregunta operativa |
|---|---|---|---|
| 1 | Customer-centricity | Cagan | ¿Describe cambio en la vida del usuario o el producto? |
| 2 | Magnitud | Cagan | ¿Es lo suficientemente grande para importar? |
| 3 | Inspiracional / emocional | Sinek + Cagan | ¿Conecta con propósito (Why)? ¿Toca lo emocional? |
| 4 | Durabilidad | Cagan | ¿Horizonte 5-10 años? |
| 5 | Ambición anclada | Cagan | ¿Stretch pero no fantasía? |
| 6 | Why ≠ What | Sinek | ¿Articula propósito o solo producto? |
| 7 | Job articulado | JTBD (opcional) | ¿Identifica el job del cliente? |

## Output format

Para cada test: ✅ pass / ⚠️ frontera / ❌ fail + diagnóstico de una línea.

**Recomendación final** — una de:
1. **Aprobar.**
2. **Reformular** (cambia redacción, mantiene espíritu).
3. **Profundizar contexto** (visión OK, contexto necesita articular WHY).
4. **Rehacer** (no captura propósito).
5. **Subir altitud** (lo ofrecido es goal, no visión).

## Bibliographic foundation

- `vault/architect/research/library/cagan-product-vision.md` — 10 principios + 6 características.
- `vault/architect/research/library/sinek-start-with-why.md` — Golden Circle.
- `vault/architect/research/library/rumelt-good-strategy.md` — visión como diagnosis.
- `vault/architect/research/library/christensen-jtbd.md` — opcional.

## Full design

`./design.md` — incluye ejemplos positivos y negativos detallados.

## Limitations

- Los 7 tests no son ortogonales — fallar uno suele implicar fallar otros.
- "Inspiracional" tiene componente subjetivo. El humano del proyecto es juez último.
- La skill no inventa visiones. Solo evalúa.

## Status lifecycle

Esta skill no produce nodos nuevos del grafo — valida un enunciado de visión existente o candidato. NO modifica el `status` del nodo `vision`; emite veredicto. La transición de `draft` a `active` la aplica recepción al `/verify` del WA vía `on-close`, **siempre que** este quality-check pase como criterio de cierre.

## WA mapping

Esta skill se invoca dentro de:

- **`vision-creation`** — caso normal.
- **`vision-creation`** (cuando se redefine la visión post-inception).
- **`vision-realignment`** (skill later — bottom-up driven cuestionamiento de visión).
