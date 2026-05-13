---
type: story
id: story-019-B
title: "PO deriva verifiers aplicando algoritmo declarativo"
parent: feature-019-slash-verify
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-019-B — PO deriva verifiers aplicando algoritmo declarativo

## Narrativa

**Como** PO al ejecutar `/verify` tras pasar closure-criteria,
**quiero** derivar la lista de verificadores aplicando el algoritmo declarativo `verifiers = {custodian(d) : d ∈ wa.dimensions-affected}` con lookup en `dimensions.md`,
**para** que la lista sea reproducible + auditable + no dependa de mi memoria.

## Examples (discovery)

1. **WA con dimensions [product, technical, quality]**: PO aplica algoritmo. Lookup en dimensions.md: product → product-owner, technical → architect, quality → qa. Verifiers = {product-owner, architect, qa}. Lista de 3.
2. **WA con dimensions [product, technical, usability, business, security, quality]** (las 6 cubiertas): verifiers = {product-owner, architect, designer, business-analyst, security-officer, qa}. Lista de 6 (todos los custodios cubiertos).
3. **WA con operations declarada**: lookup → devops. Verifiers incluyen devops.
4. **WA con verifiers-required override explícito**: el WA frontmatter declara `verifiers-required: [...]` con override consciente del PO al draftear. PO respeta override en lugar de aplicar algoritmo (decisión PO consciente al draftar prevale).
5. **Deduplicación**: si dos dimensiones tienen el mismo custodio (no debería pasar por diseño de dimensions.md, pero por robustez), PO deduplica la lista.

## Acceptance Criteria

- **AC-B1**: PO aplica algoritmo `verifiers = {custodian(d) : d ∈ wa.dimensions-affected}` consultando `vault/shared/governance/dimensions.md` para el lookup.
- **AC-B2**: Si el WA tiene `verifiers-required` declarado explícitamente en frontmatter, PO respeta override (decisión consciente del PO al draftar prevalece sobre algoritmo automático).
- **AC-B3**: La lista derivada está deduplicada (sin custodios repetidos).

## Cross-links

- **depends-on**: feature-009 (catálogo roles + custodios) — el mapping vive en dimensions.md + role-catalog.md.

## Test mecánico Adzic SbE

✅ 5 examples concretos.
✅ 3 AC SMART verificables.
✅ Spec Gherkin descendible.

Test mecánico **PASA**.
