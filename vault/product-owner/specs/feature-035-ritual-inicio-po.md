---
type: feature
id: feature-035-ritual-inicio-po
title: "Ritual de inicio del PO con panorámica al arrancar sesión"

jtbd-outcome: "Cuando el operador agente PO arranca su sesión (Modo 1 paso 1), quiere ejecutar ritual de inicio leyendo strategy/sessions/specs/adrs/governance y presentar panorámica al humano antes de pedir propuesta, so I can la conversación arranca con contexto compartido (humano sabe qué hay; PO sabe qué hay) y se previene el patrón 'agente improvisa sobre vault vacío en su cabeza'."

parent: cap-06-visibilidad-operativa

dimensions-affected: [product, usability]  # Nielsen #1 + Norman conceptual model transfer

depends-on:
  - feature-001-vault-role-first  # lee desde vault/<directorios>
also-relates-to:
  - cap-07-inception-greenfield  # ritual detecta vault vacío y propone inception
  - feature-038-po-modo-1  # bidireccional con feature-038 depends-on (cat-1 Filtro PO post-step 3-6)
related-adrs: []

status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005

fundamento-bibliografico:
  - Nielsen #1 Visibility of system status
  - Norman — Design of Everyday Things (conceptual model transfer)
---

# feature-035 · Ritual de inicio del PO

## Problem

El PO al arrancar sesión Claude Code no tiene contexto del proyecto cargado. Sin un ritual estructurado, el PO podría:
1. Empezar a procesar propuesta del humano sin saber qué hay en el vault.
2. Pedir contexto al humano repetidamente.
3. Operar con asumido en lugar de leído.

## Hypothesis

Ritual de inicio canónico (Modo 1 paso 1 del agent file PO) que lee 5 directorios + presenta panorámica al humano con formato consistente.

## Stories

- **story-035-A**: PO al arrancar lee 5 directorios del vault (strategy/, sessions/active/, specs/, adrs/, governance/) y construye mapa mental
- **story-035-B**: PO presenta panorámica al humano con formato canónico antes de pedir propuesta
- **story-035-C**: PO detecta vault vacío (greenfield) y propone inception (cadena de WAs) en lugar de pedir propuesta arbitraria

## Piezas del bootstrap

- Agent file PO `.claude/agents/product-owner.md` sección "Protocolo del Modo 1 — Paso 1 Ritual de inicio"
- Wrapper `vault/product-owner/CLAUDE.md` referencia el ritual

## Cross-links

- **also-relates-to**: feature-038 PO Modo 1 (10 pasos) — ritual de inicio ES el paso 1 de Modo 1.
- **also-relates-to**: feature-039 Cadena WAs greenfield — si vault vacío, ritual propone cadena.
