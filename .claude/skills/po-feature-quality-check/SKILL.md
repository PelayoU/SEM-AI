---
name: po-feature-quality-check
description: "Validar que una feature está completa y consistente antes de cerrarla para implementación: INVEST en stories (Cohn), cobertura de AC (Adzic), coherencia con capability padre, cross-links declarados, trazabilidad operativa, tamaño razonable. Use this skill when the PO is about to close a discovery/spec WA and needs final validation, or when retrospectively reviewing a feature before implementation starts."
allowed-tools: Read Glob Grep
materializes-feature: [feature-038-po-modo-1, feature-019-slash-verify]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): skill operativa invocada por PO Modo 1 antes de cerrar feature. También invocable por /verify (feature-019) durante sign-off de WAs feature-design.
---

# Skill: feature-quality-check (Product Owner)

## Quick reference

Aplica 7 tests a una feature para validar antes de cierre. Devuelve veredicto por test + recomendación final entre 5 opciones.

## When to invoke

- PO va a cerrar WA de discovery / spec-writing.
- Revisión retrospectiva antes de empezar implementación.
- Parcialmente automatizable en CI vía vault-cli (frontmatter, links, AC con Scenario).

## Inputs

- Feature node: `vault/product-owner/specs/feature-N.md`.
- Spec(s) de Gherkin asociadas.
- Stories embebidas o referenciadas.
- Capability padre y goals ascendentes.

## Process — 7 tests

| # | Test | Pregunta |
|---|---|---|
| 1 | ¿Frontmatter completo y válido? | Pasa schema. Cross-links declarados (pueden estar vacíos pero existir). |
| 2 | ¿Stories cumplen INVEST? | I-N-V-E-S-T por cada story. |
| 3 | ¿Cobertura de AC? | Cada story tiene spec; cada AC tiene Scenario; identificadores consistentes. |
| 4 | ¿Coherencia con capability? | Materializa pieza concreta de la capability; no contradice guiding policy. |
| 5 | ¿Cross-links coherentes? | `depends-on`, `related-adrs` apuntan a nodos existentes; `dimensions-affected` completo. |
| 6 | ¿Trazabilidad operativa? | Código a modificar identificado; ADR nuevo si requiere. |
| 7 | ¿Tamaño razonable? | Cabe en 1-3 sprints / WAs. Si mayor → descomponer. Si trivial → fundir con feature hermana. |

## Output format

Para cada test: ✅ / ⚠️ / ❌ + diagnóstico.

**Recomendación final** — una de:
1. **Aprobar para implementación.**
2. **Refinar puntos específicos.**
3. **Volver a discovery** (faltan AC críticos).
4. **Descomponer** (demasiado grande).
5. **Fundir / eliminar** (overlap o sin valor).

## Bibliographic foundation

- `vault/architect/research/library/cohn-user-stories-invest.md` — INVEST aplicado a stories.
- `vault/architect/research/library/adzic-specification-by-example.md` — cobertura de AC, living documentation.
- `vault/architect/research/library/doran-smart.md` — AC individuales pasan SMART.

## Full design

`./design.md` — incluye ejemplo aplicado a feature `feature-skills-po-goal-quality-check`.

## Limitations

- Tests 1, 5, 6 son automatizables vía vault-cli; 2, 3, 4, 7 requieren juicio.
- "Tamaño razonable" depende del equipo.
- La skill rechaza pero no completa el trabajo — devuelve a discovery / decomposition / etc.

## Status lifecycle

Esta skill no produce nodos nuevos — valida features existentes producidas por `feature-decomposition`. NO modifica el `status` del feature directamente; emite veredicto. La transición a `ready-for-implementation` la aplica recepción al `/verify` del WA vía `on-close`, **siempre y cuando** este quality-check pase como uno de los closure-criteria del WA.

## WA mapping

Esta skill se invoca como **último step** dentro del template **`feature-design`** (fase `design`), justo antes de cerrar el WA. Si el veredicto es "Aprobar para implementación", el WA puede pasar a /verify. Si emite cualquier otra recomendación, el step queda abierto hasta resolver.
