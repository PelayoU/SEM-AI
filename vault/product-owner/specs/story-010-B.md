---
type: story
id: story-010-B
title: "Newcomer descubre scripts disponibles en package.json"
parent: feature-010-entry-point-por-rol
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-010-B — Newcomer descubre scripts disponibles en package.json

## Narrativa

**Como** operador humano newcomer (ingeniero adoptador que acaba de clonar el repo),
**quiero** inspeccionar `package.json` o ejecutar `npm run` (sin argumentos) y ver los 9 scripts disponibles,
**para** descubrir los modos de trabajo del framework sin leer toda la documentación previamente.

## Examples (discovery)

1. **Inspeccionar package.json**: `cat package.json` muestra la sección `scripts` con los 9 atajos + comentarios mínimos por rol.
2. **Listar scripts sin argumentos**: `npm run` (sin args) muestra lista de scripts disponibles ordenada.
3. **Documentación en README**: el README raíz incluye sección "Cómo arrancar trabajo" con tabla rol → atajo.
4. **CLAUDE.md raíz**: el documento incluye sección "Slash commands" y referencia atajos npm.
5. **Operator con `--help` mentality**: el operador busca convención estándar. Encuentra package.json scripts (convención node estándar) sin sorpresas.

## Acceptance Criteria

- **AC-B1**: `package.json` raíz incluye los 9 scripts con nombres convencionales (`sem`, `po`, `arch`, `des`, `biz`, `sec`, `qa`, `dev`, `ops`).
- **AC-B2**: `README.md` raíz incluye tabla rol → atajo npm en sección "Cómo arrancar trabajo".
- **AC-B3**: `CLAUDE.md` raíz incluye tabla rol → atajo npm con descripción "para qué" de cada rol.

## Cross-links

- **also-relates-to**: feature-041 (README onboarding) — el newcomer lee README como entry-point.
- **also-relates-to**: feature-009 (catálogo formal de roles) — role-catalog.md también declara atajos.

## Test mecánico Adzic SbE

✅ 5 examples concretos.
✅ 3 AC SMART verificables.
✅ Spec Gherkin descendible.

Test mecánico **PASA**.
