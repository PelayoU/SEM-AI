---
name: arch-feature-viability-review
description: "Evaluar viabilidad técnica de una feature candidata: archivos a crear/modificar, ADRs aplicables, ADRs nuevos requeridos, modularidad (Ousterhout deep modules), boundaries (Martin Clean Architecture), coupling (vía coupling-detection). Output: review formal en vault/architect/research/. Use this skill when PO has decomposed a capability into features and needs technical validation before closure, or when reviewing a feature whose scope has changed."
allowed-tools: Read Write Edit Glob Grep
materializes-feature: [feature-018-slash-scope-scan, feature-019-slash-verify]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): skill Architect invocada como advisor en scope-scan (feature-018) y sign-off (feature-019). Aplicada en step-3 del WA-005 actual para review consolidado de 14 features.
---

# Skill: feature-viability-review (Architect)

## Quick reference

Aplica 6 pasos para validar viabilidad técnica de una feature. Output: archivo formal de review en `vault/architect/research/feature-N-architect-review.md` con recomendación entre 4 opciones.

## When to invoke

- PO ha descompuesto capability en features y necesita validación técnica.
- Revisión de feature cuyo alcance ha cambiado.
- Humano pide "revisión técnica de esta feature".

## Inputs

- Feature candidata (frontmatter + descripción + stories + AC).
- Capability padre.
- ADRs existentes.
- Features hermanas y existentes.
- Estructura de código actual (lectura focalizada).

## Process — 6 pasos

1. **Identificar archivos de código a tocar**: nuevos, modificaciones, tests, migrations.
2. **Identificar ADRs aplicables**: existentes que constriñen + identificar si requiere ADR nuevo.
3. **Evaluar respecto a Clean Architecture (Martin)**: dependencias apuntan hacia adentro? Boundaries respetados? SOLID OK?
4. **Evaluar modularidad (Ousterhout)**: deep modules? Information leakage? Cognitive load?
5. **Detectar coupling problemático**: invocar `coupling-detection` sobre features hermanas.
6. **Producir review estructurada** en `vault/architect/research/feature-N-architect-review.md`.

## Output format

Archivo `vault/architect/research/feature-N-architect-review.md`:

```markdown
---
type: research
id: research-feature-N-architect-review
title: "Architect review — feature-N"
related-feature: feature-N
status: draft
created: YYYY-MM-DD
author: architect
---
```

Cuerpo: Viabilidad, Archivos a crear, Archivos a modificar, ADRs aplicables, ADRs nuevos requeridos, Tactics arquitectónicas, Acoplamientos identificados, Riesgos, Recomendaciones.

**Recomendación final**:
1. **Aprobar.**
2. **Aprobar con condiciones.**
3. **Reformular feature.**
4. **Bloquear** — no viable.

## Bibliographic foundation

- `vault/architect/research/library/bass-software-architecture.md` — análisis arquitectónico de features.
- `vault/architect/research/library/ousterhout-philosophy-software-design.md` — modularidad.
- `vault/architect/research/library/martin-clean-architecture.md` — Dependency Rule, SOLID.
- `vault/architect/research/library/ford-evolutionary-architecture.md` — coupling, fitness functions.

## Full design

`./design.md` — incluye ejemplo aplicado a feature-009 (favoritos) del boceto inicial sec. 19.

## Limitations

- En código legacy, identificar archivos a tocar puede ser exploratorio.
- En proyectos en bootstrap (poco código), la review es predictiva.
- La skill no implementa; solo revisa.

## Modos de input

Esta skill opera en dos modos según el contexto:

| Modo | Contexto | Fuente de input |
|---|---|---|
| **Prospectivo** | WA `feature-design` step Architect (caso normal) | Feature candidata aún no implementada — review predictivo |
| **Retroactivo** | Audit ad-hoc de feature ya implementada (detectar deuda técnica acumulada o validar feature legada) | Código existente que materializa la feature — review post-hoc |

**En modo prospectivo**, los Pasos 1-2 (archivos a tocar + ADRs aplicables) son predictivos: identifico qué archivos hay que tocar y qué ADRs constreñirán. La feature aún no existe.

**En modo retroactivo**, los Pasos 1-2 son descriptivos: la feature ya existe en código, identifico qué archivos la materializan, qué ADRs (existentes o que deberían existir) la constreñirían. Útil para detectar deuda técnica acumulada.

Mismos 6 pasos, distinta naturaleza temporal. Output con `status: draft`.

## Status lifecycle

**Esta skill produce un review con `status: draft`.** **NO** setees el status final desde aquí. La transición a `active` la aplica recepción al `/verify` del WA vía `on-close`. Reviews con `status: active` quedan como referencia para futuros WAs (developer las consulta antes de implementar).

## WA mapping

Esta skill se invoca dentro del template **`feature-design`** (fase `design`), step `architect` (típicamente opcional, condicional a `technical en dimensions-affected`). También puede invocarse on-demand desde sesión Architect cuando humano pide "revisión técnica de feature-N" sin abrir WA formal (caso ad-hoc).
