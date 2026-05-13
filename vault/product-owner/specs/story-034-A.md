---
type: story
id: story-034-A
title: "Operador ve catálogo de roles + atajos con /sessions"
parent: feature-034-slash-sessions
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-034-A — Catálogo de roles + atajos visible con /sessions

## Narrativa

**Como** operador humano (newcomer o experimentado),
**quiero** ejecutar `/sessions` y ver tabla compacta de los 8 roles con sus atajos npm + descripción 1-línea "cuándo invocar cada uno",
**para** elegir la sesión correcta sin abrir README ni package.json.

## Examples (discovery)

1. **Newcomer**: clonó el repo, lee CLAUDE.md raíz, ejecuta `/sessions` desde la sesión inicial. Output: tabla con 8 roles + atajos + "para qué".
2. **Mid-WA, handoff**: el operador termina su step PO (ejecuta /verify de un step) y necesita arrancar Architect. Ejecuta `/sessions` para confirmar atajo. Confirma `npm run arch`.
3. **Sesión architect ya abierta**: ejecuta `/sessions` desde architect. Mismo output (slash es transversal).
4. **Catálogo coherente con role-catalog.md**: la tabla del output coincide con `vault/shared/governance/role-catalog.md` + scripts de `package.json`. Sin duplicación de fuente de verdad.
5. **Dimensión custodiada visible**: cada fila incluye qué dimensión custodia (product/technical/usability/business/security/quality/operations) — refuerza recognition Nielsen #6.

## AC

- **AC-A1**: `/sessions` output incluye tabla con columnas: Rol | Atajo npm | Dimensión custodiada | Para qué (1 línea).
- **AC-A2**: La tabla incluye los 8 roles custodios + el alias `sem` (entry-point principal PO).
- **AC-A3**: El contenido es coherente con `vault/shared/governance/role-catalog.md` (sin contradicción ni duplicación de fuente de verdad).

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
