---
type: feature
id: feature-044-glosario-publico
title: "Glosario público de términos SEM-IA"

jtbd-outcome: "Cuando el operador humano newcomer (especialmente evaluador académico no-practicante) encuentra términos del framework (WA, scope-scan, vault, capability, outcome-type, etc.), quiere consultar glosario navegable referenciado desde README en primera aparición de cada término, so I can resolver jerga interna sin leer páginas de documentación + reducir barrera de entrada (Nielsen #2 match between system and real world + #4 consistency)."

parent: cap-10-articulacion-publica

dimensions-affected: [product, usability, business]  # Nielsen #2+#4 + GTM Moore

depends-on:
  - feature-041-readme-onboarding  # README referencia glosario en primera aparición
also-relates-to:
  - feature-009-catalogo-roles  # NO Nivel 1; nivel 4 — pero glosario incluye términos de roles
  - feature-013-catalogo-workflow-templates  # NO Nivel 1; nivel 4 — glosario incluye términos del WA
related-adrs: []

status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# feature-044 · Glosario público

## Problem

Jerga interna de SEM-IA (WA, scope-scan, capability, outcome-type, dimensions-affected, on-close, modality, custodian, etc.) tiene alta barrera de entrada para newcomers + evaluadores académicos no-practicantes.

## Hypothesis

Glosario público navegable cubriendo ≥20 términos canónicos en ≥4 categorías (frontmatter / WA lifecycle / roles+dimensiones / slash commands), referenciado desde README en primera aparición de cada término.

## Stories

2 stories:

- **story-044-A**: Glosario existe con ≥20 términos en ≥4 categorías, cada término con definición + ejemplo + cross-link al doc canónico
- **story-044-B**: README referencia glosario en primera aparición de cada término jerga

## Notas

- **Pendiente físico**: glosario NO existe aún al cierre de WA-005 (decisión humana: aceptar conscientemente que GISF deadline 2026-05-25 verá README sin glosario materializado). Spec describe estado objetivo. Materialización en WA `feature-build` posterior.
