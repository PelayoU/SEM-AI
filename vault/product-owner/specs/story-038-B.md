---
type: story
id: story-038-B
title: "PO decide conduzco o delego según dominio"
parent: feature-038-po-modo-1
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-038-B — PO decide conduzco/delego

## Narrativa

**Como** PO tras clasificar outcome-type,
**quiero** decidir si conduzco yo el WA o delego al rol custodio correcto aplicando criterio del Modo 1 paso 4 (tabla "TÚ CONDUCES si..." vs "DELEGAS si..."),
**para** que cada outcome-type vaya al rol orquestador apropiado sin que el PO opere fuera de su dominio.

## Examples (discovery)

1. **outcome-type product (vision-creation, goal-definition, capability-creation, feature-design, feature-build)**: PO conduce.
2. **outcome-type technical puro (adr sin contexto product, refactor sin spec previa)**: PO delega a Architect → "Sal y abre `npm run arch`. Architect conduce ADRs aplicando adr-writing (Nygard)."
3. **outcome-type operations (pipeline-change, infra-decision, observability-instrument)**: PO delega a DevOps → "Sal y abre `npm run ops`."
4. **outcome-type security (threat-model standalone)**: PO delega a Security → "Sal y abre `npm run sec`."
5. **outcome-type cross-cutting (toca product + otro dominio)**: PO conduce y delega steps específicos en el WA (via condition opcional de cada template).

## AC

- **AC-B1**: PO consulta tabla del Modo 1 paso 4 de su agent file para decidir.
- **AC-B2**: Si DELEGA, comunica al humano explícitamente: "Sal de mi sesión, abre `npm run <rol-short>`. Yo no me meto en su dominio. Si emerge implicación de producto, el rol me invocará como subagente."
- **AC-B3**: Si CONDUCE, procede a paso 5 (convocar scope-scan vía feature-018).

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
