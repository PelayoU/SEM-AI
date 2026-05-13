---
type: story
id: story-019-C
title: "PO invoca verificadores en paralelo y consolida hallazgos"
parent: feature-019-slash-verify
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-019-C — PO invoca verificadores en paralelo y consolida

## Narrativa

**Como** PO con lista de verifiers derivada,
**quiero** invocarlos en paralelo (un único mensaje con N Task tool calls) y consolidar sus hallazgos en `aprobado | objeción menor | objeción bloqueante`,
**para** que el sign-off sea rápido + auditable + decisión cross-rol simultánea.

## Examples (discovery)

1. **5 verifiers aprueban**: PO invoca a los 5 en paralelo. Cada uno devuelve `aprobado`. PO procede a aplicar on-close (story-019-D).
2. **1 verifier con objeción bloqueante**: PO invoca paralelo. Security devuelve objeción bloqueante (ej. "AC-S2 no cubre vector X identificado"). PO presenta al humano: "WA NO cerrable hasta resolver objeción Security. Volver al WA activo." NO aplica on-close.
3. **1 verifier con objeción menor**: PO invoca paralelo. QA devuelve "AC-A2 falta `verificable vía`". PO presenta 3 opciones al humano: resolver / aparcar / aceptar conscientemente. Humano decide.
4. **Subagentes con autoridad de edición (raro en /verify)**: típicamente verifiers son read-only en /verify (auditoría, no producción). Si producen artefacto (ej. report final QA), deben declarar `filesystem-changes` Gap 9.
5. **Filtro PO sobre objeciones**: similar a Filtro PO de scope-scan (feature-018 story-018-C), PO aplica regla 12 sobre objeciones recibidas — distingue las que son load-bearing vs noise.

## Acceptance Criteria

- **AC-C1**: PO invoca a todos los verifiers en **único mensaje** con N tool_use blocks Task (flat parallel, mismo patrón que feature-018 story-018-A).
- **AC-C2**: Cada verifier recibe prompt focal: WA completo + paths a leer + tarea de verificación específica + output esperado (aprobado | objeción menor | objeción bloqueante con razón).
- **AC-C3**: PO consolida hallazgos clasificándolos: aprobados (procede on-close), objeciones bloqueantes (WA vuelve a activo + indica humano), objeciones menores (presenta humano con 3 opciones).

## Cross-links

- **depends-on**: feature-018 (slash /scope-scan paralelización) — mismo mecanismo Task tool flat parallel.

## Test mecánico Adzic SbE

✅ 5 examples concretos.
✅ 3 AC SMART verificables.
✅ Spec Gherkin descendible.

Test mecánico **PASA**.
