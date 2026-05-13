---
type: feature
id: feature-032-slash-status
title: "Slash `/status` con panorámica del proyecto por track Dual"

jtbd-outcome: "Cuando el operador humano necesita conocer el estado del proyecto en cualquier momento, quiere ejecutar `/status` desde cualquier sesión y recibir snapshot completo (subgrafo estratégico + WAs activos agrupados por track Dual + backlog query emergente + features por status + ADRs por status), so I can valido estado conocido en vez de re-explorar el vault (Nielsen #1 visibility of system status + goal-3 absorción coste revisión)."

parent: cap-06-visibilidad-operativa

dimensions-affected: [product, usability]  # Nielsen #1

depends-on:
  - feature-001-vault-role-first  # lee desde vault/<rol>/
also-relates-to:
  - cap-01-grafo-declarativo-persistente  # backlog query emergente + estados canónicos consumidos (cat-1 Filtro PO post-step 3-6)
  - cap-03-working-agreements-sdlc  # agrupa WAs por fase SDLC
depends-on-harness: []

related-adrs:
  - ADR-latente-008  # Backlog como query emergente

status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005

fundamento-bibliografico:
  - Nielsen 10 heurísticas (#1 Visibility of system status)
  - Cagan + Patton (Dual Track Discovery/Delivery)
  - Cohn (lifecycle nodos)
---

# feature-032 · Slash `/status` con panorámica del proyecto

## Problem

El operador humano alterna entre múltiples sesiones (PO, Architect, Designer, etc.) durante un proyecto SEM-IA. Sin un mecanismo de visibilidad agregada del estado completo, el operador debería:

1. Inspeccionar manualmente `vault/<rol>/` por rol para ver qué hay.
2. Listar `vault/shared/sessions/active/` para ver WAs activos.
3. Ejecutar query `grep` para derivar backlog.
4. Mantener mentalmente el mapa entre WAs y sus tracks (Discovery/Delivery/Operations/Meta).

Esto rompe Nielsen #1 (visibility of system status) + cargas cognitive load del operador alternando entre sesiones.

## Hypothesis

Si proveemos slash `/status` que agrega panorámica completa en un solo output con secciones canónicas:
- **Estrategia**: visión + goals + capabilities (counts + IDs)
- **WAs activos**: agrupados por track Dual (Discovery/Delivery/Operations/Meta)
- **Backlog**: query emergente sobre `status: ready-for-implementation`
- **Producto**: features por status (draft/active/ready-for-implementation/implemented)
- **Arquitectura**: ADRs por status (proposed/accepted/superseded)
- **Audits/reports**: counts de threat-models, usability reviews, business reviews, QA reports

Entonces el operador valida estado conocido en lugar de re-explorar el vault.

## Expected outcome (JTBD)

*Cuando el operador humano necesita conocer el estado del proyecto, ejecuta `/status` y recibe snapshot agregado. Goal-3 (absorción coste revisión) materializado.*

## Stories

2 stories cohesivas:

- **story-032-A**: Como operador, ejecuto `/status` y veo panorámica completa del estado actual del proyecto agrupada en 6 secciones canónicas (Estrategia + Producto + Arquitectura + WAs activos + Backlog + Audits)
- **story-032-B**: Como operador, ejecuto `/status` y los WAs activos están agrupados por track Dual Discovery/Delivery (Cagan/Patton) — distingo qué WAs están descubriendo vs entregando vs operando vs meta

## Piezas del bootstrap que materializan esta feature

- Documentación de `/status` en CLAUDE.md raíz sección "Slash commands"
- Convención del output canónico (6 secciones) documentada en agent file PO ritual de inicio
- Aplicación práctica: cada sesión PO al arrancar presenta panorámica con formato similar al output de `/status`

## Notas

- **AC adicional absorbido** (story-005-A reclasificada en step-2a + feature-037 Dual Track reclasificada): AC-A4 de spec-032-A declara explícitamente "sección Backlog incluye query emergente sobre nodos `status: ready-for-implementation`". AC-B2 de spec-032-B declara "agrupación por track Dual Discovery/Delivery (Cagan/Patton)".
- **Filtra implementación**: la feature describe COMPORTAMIENTO observable del slash. NO especifica el código exacto. La implementación es responsabilidad del WA `feature-build` posterior cuando se materialice como skill/command construido.
