---
type: story
id: story-038-C
title: "PO carga template + adapta + drafta WA autocontenido con briefings"
parent: feature-038-po-modo-1
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-038-C — PO drafta WA autocontenido con briefings

## Narrativa

**Como** PO tras consolidar scope-scan + aplicar Filtro PO,
**quiero** cargar template del outcome-type desde `workflows.md`, adaptar steps según scope-scan output, y draftear WA autocontenido (Gap 7) con briefings por step para steps no-PO (Gap 10),
**para** que el WA sea contrato legible standalone + cada rol receptor arranque con contexto curado.

## Examples (discovery)

1. **Template adaptado**: outcome-type = `feature-design`. PO carga template. Mantiene steps "siempre" + steps `optional` cuya `condition` matchea scope-scan. Omite los que no aplican.
2. **WA autocontenido (Gap 7)**: cuerpo del WA reproduce contenido necesario in extenso, NO solo referencia. Si consume del WA archivado anterior, reproduce el contexto.
3. **Briefing por step (Gap 10)**: para cada step no-PO, escribe 4 bloques canónicos: Mapa del grafo curado + Contexto conversacional + Razonamiento PO + Output esperado complementario.
4. **Filesystem-changes obligatorio (Gap 9)**: steps `modality: subagente` con autoridad de edición → purpose del step incluye requisito de declarar bloque `filesystem-changes`.
5. **Frontmatter completo**: `outcome-type`, `phase`, `objective`, `dimensions-affected`, `participants`, `steps[]`, `scope-allowed/forbidden`, `verifiers-required`, `closure-criteria`, `on-close`.

## AC

- **AC-C1**: PO carga template desde `workflows.md` y adapta steps según `condition` del scope-scan output.
- **AC-C2**: Cuerpo del WA es autocontenido (Gap 7) — reproduce contenido referenciado in extenso.
- **AC-C3**: Para cada step no-PO, PO escribe Briefing con 4 bloques canónicos (Gap 10). Si step es subagente con autoridad de edición, declara requisito filesystem-changes en purpose (Gap 9).

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
