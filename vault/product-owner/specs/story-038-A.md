---
type: story
id: story-038-A
title: "PO escucha + clarifica + clasifica outcome-type"
parent: feature-038-po-modo-1
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-038-A — Escucha + clarifica + clasifica outcome-type

## Narrativa

**Como** PO en Modo 1 tras presentar panorámica al humano (paso 1 cubierto por feature-035),
**quiero** escuchar propuesta humana + clarificar si ambigua + clasificar `outcome-type` consultando `workflows.md`,
**para** determinar qué template aplicar antes de convocar scope-scan.

## Examples (discovery)

1. **Propuesta clara**: humano dice "definir visión". PO clasifica directamente `outcome-type: vision-creation`.
2. **Propuesta ambigua**: humano dice "mejorar la arquitectura". PO clarifica: "¿ADR específico? ¿refactor focal? ¿reorganización mayor?".
3. **Propuesta cross-cutting**: humano dice "implementar login Google end-to-end". PO clarifica: "Sin spec previa. Propongo partir en `feature-design` ahora + `feature-build` después. ¿Aceptas?".
4. **Heurística workflows.md**: PO consulta tabla "Heurística de clasificación outcome-type" + matches por keywords.
5. **Outcome-type desconocido**: humano propone algo que no encaja con los 14 templates. PO indica: "No tengo template específico. ¿Encaja con `doc-edit` (meta)? ¿Necesitamos nuevo outcome-type?".

## AC

- **AC-A1**: PO clarifica con pregunta concreta si propuesta es ambigua (NO procede a clasificar sobre ambigüedad).
- **AC-A2**: PO clasifica outcome-type consultando heurística de `vault/shared/governance/workflows.md`.
- **AC-A3**: Si propuesta es cross-cutting o requiere cadena, PO lo declara explícitamente al humano (no clasifica silenciosamente como UN outcome cuando son varios).

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
