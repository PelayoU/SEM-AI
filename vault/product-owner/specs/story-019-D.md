---
type: story
id: story-019-D
title: "PO aplica on-close transitions y archiva el WA"
parent: feature-019-slash-verify
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-019-D — PO aplica on-close transitions y archiva el WA

## Narrativa

**Como** PO tras consolidar aprobaciones de todos los verifiers,
**quiero** aplicar mecánicamente las transiciones declaradas en `on-close` del frontmatter del WA + mover el WA de `active/` a `archive/`,
**para** que el sign-off finalice el lifecycle del WA + alimente el backlog (si aplica) deterministicamente.

## Examples (discovery)

1. **on-close simple**: WA declara `on-close: feature-N.md: draft → active`. PO lee el archivo, verifica `status: draft`, modifica a `status: active`. Confirma transición al humano.
2. **on-close múltiple**: WA `feature-design` mode batch declara N transiciones (feature files, story files, spec files, audits, reports). PO aplica cada una secuencialmente.
3. **on-close de spec Gherkin formal → ready-for-implementation**: para WA `feature-design` con Gherkin formal, on-close transita specs `draft → ready-for-implementation` (entrada al backlog query emergente). **Esto es la materialización de la story-005-C reclasificada — el backlog se alimenta via on-close de specs.**
4. **on-close de feature/story (sin Gherkin formal) → active**: features y stories del WA-005 transitan a `active` (no `ready-for-implementation` — solo specs Gherkin con AC formales entran al backlog).
5. **Status inicial NO matchea esperado**: WA declara `on-close: feature-X: draft → active`. PO lee, descubre `status: in-progress` (no draft). Presenta al humano: "Status inesperado. ¿Aplico la transición de todos modos, o investigamos?" — decisión humana antes de aplicar.
6. **Archivado del WA**: tras todas las on-close aplicadas, PO mueve `vault/shared/sessions/active/wa-NNN.md` a `vault/shared/sessions/archive/wa-NNN.md`. Actualiza frontmatter `status: archived` + `archived-at: <ISO datetime>` + `verified-at: <timestamp>` + `verified-by: [<lista verifiers>]`.
7. **Confirmación al humano**: PO confirma todas las transiciones aplicadas + path del WA archivado + lista de verifiers que aprobaron.

## Acceptance Criteria

- **AC-D1**: PO procesa cada entrada de `on-close` del frontmatter del WA secuencialmente. Para cada `<path>: <status-inicial> → <status-final>`: lee el archivo, verifica status actual matchea esperado, modifica al final via Edit.
- **AC-D2**: Para WAs `feature-design`, specs Gherkin con AC formales transitan `draft → ready-for-implementation` (alimenta backlog query emergente). Features y stories sin Gherkin formal transitan `draft → active` (no entran al backlog).
- **AC-D3**: PO mueve el WA de `active/` a `archive/`, actualiza `status: archived` + metadata de cierre (`archived-at`, `verified-at`, `verified-by`), y confirma al humano todas las transiciones aplicadas.

## Cross-links

- **also-relates-to**: feature-017 closure-criteria + on-close (Nivel 2 ADR latente — el algoritmo de on-close).
- **also-relates-to**: feature-004 estados canónicos del nodo (Nivel 2 ADR latente — las transiciones operan sobre el lifecycle declarado).
- **Absorbe**: story-005-C reclasificada (alimentación del backlog vía on-close de specs feature-design).

## Test mecánico Adzic SbE

✅ 7 examples concretos.
✅ 3 AC SMART verificables.
✅ Spec Gherkin descendible.

Test mecánico **PASA**.
