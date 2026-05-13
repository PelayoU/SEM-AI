---
type: story
id: story-039-C
title: "PO drafta primer WA + iteración cadena"
parent: feature-039-cadena-was-greenfield
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-039-C — Iteración cadena (drafta uno por uno)

## Narrativa

**Como** PO tras humano confirmar cadena,
**quiero** draftear solo el primer WA + esperar /verify + draftear el siguiente al cierre,
**para** que cada WA sea independiente con su closure-criteria + on-close propios + el grafo emerja orgánicamente sin batch-up de WAs por adelantado.

## Examples (discovery)

1. **Greenfield cadena 4 WAs**: PO drafta WA-1 vision-creation. Humano + PO ejecutan WA-1. /verify aprueba. on-close: vision.md `draft → active`. PO drafta WA-2 goal-definition consumiendo visión activa.
2. **Iteración sucesiva**: tras /verify de WA-N, PO consulta cadena propuesta + drafta WA-N+1 con el nodo padre del WA-N como `consumes`.
3. **Pivot mid-cadena**: durante WA-2 (goal-definition) humano pivota visión. Aplica Protocolo Gap 4 sobre WA-2 → aborted. Vuelve a WA-1 (vision-realignment) o WA-2 con approach distinto. La cadena adapta.
4. **N WAs no fijo**: vision-creation puede generar N goals (humano decide en step-1). Cada goal genera M capabilities. Cada capability M features. La cadena se materializa iterativamente.
5. **Cierre de cadena**: tras /verify del último WA (feature-design o feature-build según scope), cadena completa. Backlog poblado.

## AC

- **AC-C1**: PO drafta solo primer WA de la cadena (no toda).
- **AC-C2**: Tras /verify de WA-N, PO consulta plan original + drafta WA-N+1 con `consumes` del nodo producido por WA-N.
- **AC-C3**: Cada WA de la cadena es independiente con closure-criteria + on-close propios. Pivots intra-cadena aplican Protocolo Gap 4 (feature-016 Nivel 3 protocolo).

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
