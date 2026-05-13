---
type: story
id: story-041-A
title: "Newcomer comprende tesis + modelo conceptual"
parent: feature-041-readme-onboarding
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-041-A — Newcomer comprende tesis + modelo

## Narrativa

**Como** operador humano newcomer leyendo README.md raíz por primera vez,
**quiero** comprender en orden: (a) tesis filosófica del framework, (b) modelo conceptual (espina dorsal + 8 roles + 7 dimensiones + 14 templates), (c) cómo arrancar (`npm run sem`),
**para** decidir informado si invertir tiempo en adoptar/evaluar/contribuir.

## Examples

1. **Tesis primero**: README abre con "El trabajo con IA requiere su propia infraestructura de gestión..." (Goal-1 + visión).
2. **Modelo conceptual visual**: README incluye diagrama o tabla del flujo espina dorsal Visión → Goals → Capabilities → Features → Stories → Examples → AC → Specs Gherkin → Artifacts.
3. **8 roles + 7 dimensiones**: README declara los 8 roles custodios y las 7 dimensiones (product/technical/usability/business/security/quality/operations).
4. **Cómo arrancar**: sección "Cómo arrancar trabajo" con tabla rol → atajo + `npm run sem` como default.
5. **5 reglas para el humano**: README declara las 5 reglas operativas + criterio de delegación.

## AC

- **AC-A1**: README incluye sección "Visión" o equivalente con tesis filosófica en primeras 50 líneas.
- **AC-A2**: README incluye sección "Modelo conceptual" con diagrama/tabla del flujo espina dorsal + 8 roles + 7 dimensiones.
- **AC-A3**: README incluye sección "Cómo arrancar trabajo" con tabla rol → atajo + ejemplo de uso.

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
