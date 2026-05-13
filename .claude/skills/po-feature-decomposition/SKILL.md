---
name: po-feature-decomposition
description: "Descomponer una capability aprobada en features entregables y cada feature en stories, usando User Story Map de Patton (narrative flow + thin slices) e INVEST de Cohn. Use this skill when a capability from the strategic subgraph enters operational decomposition (post-inception), or when an existing feature is too large during implementation and needs breakdown."
allowed-tools: Read Write Edit Glob Grep
materializes-feature: [feature-038-po-modo-1]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): skill operativa invocada por PO Modo 1 cuando outcome-type = feature-design. Aplicada en step-2x del WA-005 actual.
---

# Skill: feature-decomposition (Product Owner)

## Quick reference

Toma una capability aprobada y produce: (a) árbol features/stories, (b) slicing por release (thin slices end-to-end), (c) cross-links declarados.

## When to invoke

- Capability aprobada entra en fase de descomposición operativa (post-inception).
- Feature existente demasiado grande durante implementación.

## Inputs

- Capability padre (frontmatter + descripción + justificación).
- Goal y visión ascendentes.
- Catálogo de roles del proyecto (para tipos de usuario en stories).

## Process — 7 pasos

1. **Identifica outcome JTBD** que la capability habilita. Frase ancla: *"Cuando X, el [usuario] quiere Y, so I can Z"*.
2. **Mapea narrative flow (Patton)**: 3-7 actividades del usuario en orden temporal. Espina dorsal del story map.
3. **Por cada actividad, identifica 1-3 features candidatas**. Cada feature: título + outcome de usuario + dimensiones tentativas + conexión con capability padre.
4. **Por cada feature, descompón en stories** (formato Cohn: *"Como X quiero Y para Z"*). Aplica INVEST. Refactoriza las que fallen.
5. **Slicing por release (Patton)**: thin slice end-to-end como Release 1. Marcar features/stories por release.
6. **Identifica dependencias** vía `graph-cross-link-declaration`: `depends-on`, `also-relates-to`, `related-adrs`, `dimensions-affected`.
7. **Quality-check final** vía `feature-quality-check` antes de formalizar nodos en vault.

## Output format

```
Capability X
├── Feature 1 (Release 1)
│   ├── Story 1.1
│   └── Story 1.2
├── Feature 2 (Release 1)
│   └── Story 2.1
└── Feature 3 (Release 2)
    └── Story 3.1
```

Por cada feature: archivo `vault/product-owner/specs/feature-N.md` con la estructura definida abajo. Por cada story: spec en Gherkin vía `spec-writing` (que define la estructura de story + spec).

## Estructura del nodo feature

```markdown
---
type: feature
id: feature-<N>
title: "<frase corta>"

# JTBD outcome — qué cambia para el usuario cuando esta feature está construida (Cagan principio 1: "solve problems, not features")
# Forma: "Cuando [contexto], el [usuario] quiere [outcome], so I can [beneficio]"
# Obligatorio — sin outcome JTBD claro, la feature es output ciego (feature factory) en lugar de solución a problema.
jtbd-outcome: "<frase JTBD>"

# Espina dorsal jerárquica
parent: cap-<N>-<slug>

# Dimensiones holísticas que toca
dimensions-affected: [<lista>]

# Aristas cross-link
depends-on: []
also-relates-to: []
related-adrs: []

# Estado
status: draft
created: <YYYY-MM-DD>
author: product-owner
---

# <Título>

## Problem

<Qué problema resuelve esta feature para el usuario.>

## Hypothesis

<Qué hipótesis tenemos sobre cómo resolverlo.>

## Expected outcome

<Qué resultado esperamos al entregar esta feature. JTBD outcome.>

## Stories

<Lista de stories candidatas. Se descompone al hacer discovery.>
```

## Bibliographic foundation

- `vault/architect/research/library/patton-user-story-mapping.md` — narrative flow + thin slices + outcomes > features.
- `vault/architect/research/library/cohn-user-stories-invest.md` — formato story + INVEST.
- `vault/architect/research/library/christensen-jtbd.md` — articulación de outcomes.

## Full design

`./design.md` — incluye ejemplo aplicado a CAP-1 custodios homólogos.

## Limitations

- Para capabilities muy técnicas (ej: "memoria compartida en grafo"), narrative flow puede ser artificial. Adaptar a "flujo del developer interactuando".
- Slicing por release puede ser difícil si Release 1 requiere mínimo grande. Ser honesto y aceptarlo.

## Status lifecycle

**Esta skill produce features con `status: draft`.** **NO** setees el status final desde aquí. La transición a `ready-for-implementation` la aplica recepción al ejecutar `/verify` del WA, leyendo el campo `on-close` del frontmatter del WA. Las stories y specs derivadas se gobiernan por `spec-writing` con su mismo lifecycle.

## WA mapping

Esta skill se invoca dentro del template **`feature-design`** (fase `design`, ver `vault/shared/governance/workflows.md`). Step típico: `product-owner` como step 1.

**Aclaración sobre nombres**: la skill se llama `feature-decomposition` (proceso ejecutable del PO), el template del WA se llama `feature-design` (metadato del workflow). Conceptos relacionados pero distintos — el template orquesta el WA, la skill ejecuta el procedimiento dentro del step.
