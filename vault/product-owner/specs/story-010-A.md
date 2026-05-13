---
type: story
id: story-010-A
title: "Arrancar sesión de rol vía atajo npm"
parent: feature-010-entry-point-por-rol
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-010-A — Arrancar sesión de rol vía atajo npm

## Narrativa

**Como** operador humano (ingeniero adoptador o autor),
**quiero** ejecutar `npm run <atajo>` (sem, arch, des, biz, sec, qa, dev, ops) en la terminal,
**para** arrancar una sesión Claude Code con la identidad del rol cargada sin teclear paths ni recordar convenciones del harness.

## Examples (discovery)

1. **Arrancar PO**: el operador ejecuta `npm run sem` (o el alias `npm run po`). La sesión arranca en `vault/product-owner/` con identidad PO cargada vía `.claude/agents/product-owner.md`.
2. **Arrancar Architect**: el operador ejecuta `npm run arch`. La sesión arranca en `vault/architect/` con identidad Architect cargada.
3. **Arrancar Designer**: `npm run des` → sesión en `vault/designer/` con identidad Designer.
4. **Arrancar Business Analyst**: `npm run biz` → `vault/business-analyst/`.
5. **Arrancar Security Officer**: `npm run sec` → `vault/security-officer/`.
6. **Arrancar QA**: `npm run qa` → `vault/qa/`.
7. **Arrancar Developer**: `npm run dev` → `vault/developer/` (con gap menor declarado: wrapper CLAUDE.md de developer pendiente al cierre del WA-005).
8. **Arrancar DevOps**: `npm run ops` → `vault/devops/`.
9. **Atajo desconocido**: el operador ejecuta `npm run foo` (script inexistente). npm responde con error standard "missing script: foo". El operador consulta `npm run` (sin argumentos) para ver lista de scripts.

## Acceptance Criteria

- **AC-A1**: `package.json` raíz declara los 9 scripts (`sem`, `po`, `arch`, `des`, `biz`, `sec`, `qa`, `dev`, `ops`) en sección `scripts`.
- **AC-A2**: Cada script ejecuta `cd vault/<rol>/ && claude` (o equivalente que arranque Claude Code en el directorio del rol).
- **AC-A3**: La sesión arrancada por cualquier atajo tiene la identidad del rol cargada (verificable vía comportamiento del agente que cita su agent file al primer prompt o ritual de inicio).

## Cross-links

- **also-relates-to**: feature-035 (ritual de inicio del PO) — al arrancar `npm run sem`, el PO ejecuta ritual de inicio y presenta panorámica.

## Test mecánico Adzic SbE

✅ Story descompone feature-010 en incremento funcional (ejecutar atajo → arrancar sesión).
✅ 9 examples concretos (los 9 scripts + error case).
✅ 3 AC SMART verificables vía inspección package.json + ejecución.
✅ Spec Gherkin descendible (Given/When/Then sobre ejecución de script).

Test mecánico **PASA**.
