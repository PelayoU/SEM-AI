---
type: story
id: story-044-B
title: "README referencia glosario en primera aparición de cada término"
parent: feature-044-glosario-publico
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-044-B — README enlaza glosario en primera aparición

## Narrativa

**Como** newcomer leyendo README,
**quiero** que la primera aparición de cada término jerga incluya enlace al glosario,
**para** resolver el término sin perder el contexto de lectura.

## Examples

1. README menciona "WA" por primera vez → link `[WA](glossary.md#wa)` o equivalente.
2. README menciona "scope-scan" → link al glosario.
3. README menciona "outcome-type" → link.
4. Apariciones subsecuentes del mismo término → NO requieren link (solo primera).
5. README incluye sección "Términos" al final como índice rápido al glosario completo.

## AC

- **AC-B1**: Primera aparición de cada término canónico del framework incluye link al glosario.
- **AC-B2**: Apariciones subsecuentes del mismo término NO requieren link (evita ruido visual).
- **AC-B3**: README incluye sección "Términos" o "Glosario" al final con link al glosario completo.

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
