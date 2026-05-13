---
type: story
id: story-044-A
title: "Glosario con ≥20 términos en ≥4 categorías"
parent: feature-044-glosario-publico
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-044-A — Glosario con cobertura mínima

## Narrativa

**Como** operador humano newcomer,
**quiero** consultar glosario público con ≥20 términos canónicos del framework agrupados en ≥4 categorías,
**para** resolver jerga sin leer todos los docs.

## Examples

1. Término "WA" → definición + ejemplo + cross-link a CLAUDE.md raíz sección "Estructura de un Working Agreement".
2. Término "scope-scan" → definición + ejemplo + cross-link a feature-018 spec.
3. Término "outcome-type" → definición + cross-link a workflows.md.
4. Término "dimensions-affected" → definición + cross-link a dimensions.md.
5. Término "custodian" → definición + cross-link a role-catalog.md.

## AC

- **AC-A1**: Glosario cubre ≥20 términos canónicos.
- **AC-A2**: Glosario agrupa términos en ≥4 categorías:
  - (a) términos del frontmatter (type, parent, also-relates-to, dimensions-affected, status, modality)
  - (b) términos del WA lifecycle (outcome-type, on-close, closure-criteria, scope-allowed, aborted, ready-for-implementation)
  - (c) términos de roles/dimensiones (custodian, Cagan-risk, role-catalog, scope-scan, /verify)
  - (d) términos de slash commands (/status, /wa, /scope-scan, /verify, /sessions)
- **AC-A3**: Cada entrada incluye: definición concisa + ejemplo + cross-link al doc canónico.

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
