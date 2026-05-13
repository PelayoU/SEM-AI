---
type: feature
id: feature-033-slash-wa
title: "Slash `/wa` con detalle del WA activo en contexto"

jtbd-outcome: "Cuando el operador (humano o agente) necesita saber dónde está exactamente en el ciclo del WA activo, quiere ejecutar `/wa` y recibir detalle del WA en contexto (steps con status, Progreso entries, próximo step pending, scope), so I can comprender mi ubicación en el lifecycle sin abrir el archivo .md manualmente."

parent: cap-06-visibilidad-operativa

dimensions-affected: [product, usability]  # Nielsen #1 + #9 error recovery

depends-on:
  - feature-014-estructura-wa  # NO Nivel 1 — Nivel 2 ADR latente; feature-033 lee la estructura del WA
also-relates-to: []
depends-on-harness: []

related-adrs: []

status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005

fundamento-bibliografico:
  - Nielsen 10 heurísticas (#1 + #9 help users recognize, diagnose, recover)
---

# feature-033 · Slash `/wa` con detalle del WA activo

## Problem

El operador (humano o agente) durante un WA activo necesita saber: qué step está en curso, qué steps ya están done, qué Progreso entries hay, qué scope-allowed/forbidden, qué viene a continuación. Sin slash dedicado, debe abrir manualmente el archivo `vault/shared/sessions/active/wa-NNN.md` (verboso, ~1500 líneas en WAs grandes).

## Hypothesis

Slash `/wa` que detecta WA activo (o pide al operador identificarlo si hay múltiples) y produce output legible con: ID del WA + outcome-type + steps[] con status + Progreso resumen + próximo step pending + scope compacto.

## Expected outcome (JTBD)

*Cuando operador necesita ubicarse en el ciclo del WA, ejecuta `/wa` y comprende dónde está sin abrir el archivo.*

## Stories

- **story-033-A**: Operador humano ejecuta `/wa` y ve detalle del WA activo (steps + status + próximo step pending)
- **story-033-B**: Agente al continuar un step lee `/wa` para reorientarse + ver inputs del step anterior (Progreso entry resumido)

## Piezas del bootstrap

- Documentación de `/wa` en CLAUDE.md raíz.
- Estructura WA convencional (frontmatter + steps[] + Progreso) que `/wa` parsea.
