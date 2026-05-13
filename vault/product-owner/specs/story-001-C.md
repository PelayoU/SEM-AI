---
type: story
id: story-001-C
title: "Localización de artefactos cross-rol en vault/shared/"
parent: feature-001-vault-role-first
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-001-C — Localización de artefactos cross-rol en vault/shared/

## Narrativa

**Como** operador (humano o agente),
**quiero** encontrar artefactos compartidos cross-rol en `vault/shared/<sub>/`,
**para** distinguir artefactos transversales del proyecto de artefactos custodiados por un rol único.

## Examples (discovery)

1. **Buscar WA activo**: el operador navega a `vault/shared/sessions/active/` y encuentra los WAs en curso.
2. **Buscar governance doc**: el operador navega a `vault/shared/governance/` y encuentra los 5 docs canónicos (dimensions, role-catalog, workflows, verification-matrix, repo-structure).
3. **Buscar retros del proyecto**: el operador navega a `vault/shared/retros/` (cuando existan).
4. **Buscar plans cross-rol**: el operador navega a `vault/shared/plans/active/` o `vault/shared/plans/archive/`.
5. **Buscar reviews cross-rol**: el operador navega a `vault/shared/reviews/`.
6. **Decisión de ownership ambigua**: un artefacto candidato a cross-rol PERO en realidad de un único rol — el PO decide ownership por JTBD primario (no por mecanismo). Si JTBD es de un rol, va en `vault/<rol>/`; si JTBD requiere múltiples roles, va en `vault/shared/`.

## Acceptance Criteria

- **AC-C1**: Los WAs (coordinadores multi-rol por naturaleza) viven en `vault/shared/sessions/{active|archive}/`.
- **AC-C2**: Los governance docs (5 canónicos: dimensions, role-catalog, workflows, verification-matrix, repo-structure) viven en `vault/shared/governance/`.
- **AC-C3**: Cualquier artefacto cuyo JTBD requiera múltiples roles vive en `vault/shared/<sub>/`. Decisión de ownership por JTBD primario, documentada al draftar el artefacto.

## Cross-links

- **also-relates-to**: feature-013 (catálogo 14 workflow templates) — workflows.md vive en shared/governance porque coordina múltiples roles.
- **also-relates-to**: feature-009 (catálogo roles) — role-catalog.md vive en shared/governance.

## Test mecánico Adzic SbE aplicado

✅ Story descompone feature-001 en incremento funcional cross-rol.
✅ 6 examples concretos.
✅ 3 AC filtrados SMART.
✅ Spec Gherkin descendible.

Test mecánico **PASA**.
