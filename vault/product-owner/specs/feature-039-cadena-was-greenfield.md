---
type: feature
id: feature-039-cadena-was-greenfield
title: "Cadena de WAs por gaps detectados (vision → goals → capabilities → features)"

jtbd-outcome: "Cuando el PO durante scope-scan detecta gaps upstream (no hay capability padre, no hay goal padre, no hay visión), quiere proponer al humano cadena ordenada top-down de WAs (vision-creation → goal-definition × N → capability-creation × M → feature-design × K) usando templates existentes, so I can el grafo emerge orgánicamente desde gap detection sin protocolos paralelos ni atajos ad-hoc."

parent: cap-07-inception-greenfield

dimensions-affected: [product, technical]

depends-on:
  - feature-013-catalogo-workflow-templates  # NO Nivel 1 — Nivel 4; pero la cadena consume templates existentes
  - feature-038-po-modo-1
also-relates-to: []
related-adrs: []

status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# feature-039 · Cadena WAs greenfield

## Problem

Operador adopter externo arranca `npm run sem` con vault vacío. Trae propuesta como "construir SaaS de inventarios". No hay visión + goals + capabilities + features. Sin un protocolo de cadena, el PO no sabría: ¿drafteo todos los WAs ahora? ¿uno por uno? ¿en qué orden?

## Hypothesis

Cadena ordenada top-down de WAs por gaps:
- `vision-creation` → `goal-definition × N` → `capability-creation × M` → `feature-design × K`

Cada WA al cerrar produce el nodo padre del siguiente. PO propone la cadena, humano confirma, PO drafta el primer WA. Tras `/verify` del primer WA, PO drafta el siguiente. Cada WA independiente con closure-criteria propios.

## Stories

3 stories:

- **story-039-A**: PO durante scope-scan detecta gaps upstream y los enumera al humano
- **story-039-B**: PO propone cadena ordenada de WAs (3 formas: directa greenfield, corta proyecto-maduro, modo arbitraje cross-cutting)
- **story-039-C**: PO drafta SOLO el primer WA de la cadena. Tras /verify, drafta el siguiente. Cada WA independiente.

## Piezas del bootstrap

- `vault/shared/governance/workflows.md` sección "Cadena de WAs por gaps detectados" documenta las 3 formas.
- Agent file PO declara cadena en Modo 1 paso 7.
