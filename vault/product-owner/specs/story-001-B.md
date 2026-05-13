---
type: story
id: story-001-B
title: "Escritura agente en vault/<mi-rol>/"
parent: feature-001-vault-role-first
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-001-B — Escritura agente en vault/<mi-rol>/

## Narrativa

**Como** operador agente (cualquier rol custodio activo durante un step de WA),
**quiero** escribir mis artefactos producidos en `vault/<mi-rol>/<subcategoría>/` siguiendo la convención role-first,
**para** que mis outputs queden en el directorio responsable y otros operadores los encuentren predecibilmente.

## Examples (discovery)

1. **Architect escribe ADR**: lo guarda en `vault/architect/adrs/adr-NNN-slug.md` (no en `vault/adrs/` ni en `vault/architect-adrs/`).
2. **PO escribe capability**: la guarda en `vault/product-owner/strategy/cap-NN-slug.md`.
3. **Security escribe threat-model**: lo guarda en `vault/security-officer/audits/feature-N-threat-model.md`.
4. **Designer escribe usability review**: lo guarda en `vault/designer/audits/feature-N-usability-review.md`.
5. **Developer escribe gotcha**: lo guarda en `vault/developer/gotchas/<topic>.md`.
6. **Agente intenta escribir fuera de su rol**: ej. PO intenta escribir en `vault/architect/adrs/`. El `scope-allowed` del WA debe declararlo explícitamente; si no, viola scope-forbidden (ver feature-024 contrato filesystem-changes).
7. **Agente escribe artefacto cross-rol**: usa `vault/shared/<sub>/` deliberadamente (ej. WA es shared porque coordina múltiples roles → `vault/shared/sessions/active/`).

## Acceptance Criteria

- **AC-B1**: Cada rol custodio escribe sus artefactos en `vault/<su-rol>/<subcategoría>/` por defecto.
- **AC-B2**: La escritura en `vault/<otro-rol>/` por un agente activo requiere autorización explícita vía `scope-allowed` del WA contenedor.
- **AC-B3**: Artefactos cross-rol viven en `vault/shared/<sub>/` y la decisión de cross-rol es consciente (no por accidente).

## Cross-links

- **depends-on**: feature-024 (contrato `filesystem-changes` Gap 9) — la trazabilidad de qué rol escribió qué exige declaración explícita.
- **also-relates-to**: feature-009 (catálogo roles).

## Test mecánico Adzic SbE aplicado

✅ Story descompone feature-001 en incremento funcional.
✅ 7 examples concretos elicitados.
✅ 3 AC filtrados como SMART.
✅ Spec Gherkin descendible (ver spec-001-B.md).

Test mecánico **PASA**.
