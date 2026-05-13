---
type: story
id: story-001-A
title: "Navegación humana al directorio del rol"
parent: feature-001-vault-role-first
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-001-A — Navegación humana al directorio del rol

## Narrativa

**Como** operador humano (ingeniero adoptador o autor del proyecto),
**quiero** navegar al directorio del rol custodio que necesito vía `vault/<rol>/` con paths predecibles,
**para** localizar artefactos del rol sin inspeccionar otros directorios ni recordar convenciones de tipo técnico.

## Examples (discovery)

Situaciones concretas exploradas durante elicitation Adzic SbE:

1. **El humano busca un ADR**: navega a `vault/architect/adrs/` y encuentra los ADRs ahí (no en `vault/adrs/` ni en otros directorios).
2. **El humano busca una capability**: navega a `vault/product-owner/strategy/` y encuentra `cap-01..cap-10.md`.
3. **El humano busca una sesión activa (WA)**: navega a `vault/shared/sessions/active/` y encuentra los WAs en curso.
4. **El humano busca un threat-model**: navega a `vault/security-officer/audits/` y encuentra los threat-models (no en `vault/threat-models/`).
5. **El humano busca un wrapper CLAUDE.md de rol**: navega a `vault/<rol>/CLAUDE.md` y encuentra el wrapper (no en `vault/wrappers/` ni en `.claude/`).
6. **El humano intenta path desconocido**: ejecuta `ls vault/foo/` (rol inexistente) y recibe error filesystem standard (no hay magia recovery — el operador aplica convención role-first o falla).

## Acceptance Criteria (filtrados de examples, SMART)

Se formalizan en `spec-001-A.md` (Gherkin):

- **AC-A1**: Para cada rol custodio declarado en `role-catalog.md` (8 roles: product-owner, architect, designer, business-analyst, security-officer, qa, developer, devops), existe `vault/<rol>/` como directorio.
- **AC-A2**: Cada `vault/<rol>/` contiene sub-directorios convencionales según el dominio del rol (ej. `architect/adrs/` + `architect/research/`; `product-owner/strategy/` + `product-owner/specs/` + `product-owner/discovery/`).
- **AC-A3**: La convención role-first está documentada en `vault/shared/governance/repo-structure.md` con tabla rol × sub-directorios.

## Cross-links

- **also-relates-to**: feature-009 (catálogo formal de roles) — el listado de roles que custodian directorios proviene de role-catalog.md.

## Test mecánico Adzic SbE aplicado

✅ Story descompone feature-001 en incremento funcional menor (Cohn `S = Small` — pocas stories).
✅ 6 examples concretos elicitados (Adzic SbE).
✅ 3 AC filtrados como SMART con identificadores únicos (AC-A1/A2/A3).
✅ Spec Gherkin descendible con Given/When/Then concretos (ver spec-001-A.md).

Test mecánico **PASA**. Confirma feature-001 como Nivel 1 (feature genuina).
