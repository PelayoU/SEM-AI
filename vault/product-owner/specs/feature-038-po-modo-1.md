---
type: feature
id: feature-038-po-modo-1
title: "PO Modo 1 (Entrada al sistema) con protocolo declarativo de 10 pasos"

jtbd-outcome: "Cuando el operador agente PO recibe propuesta humana al arrancar sesión (vault no vacío o vacío), quiere conducir el flujo completo de entrada al sistema aplicando protocolo declarativo de 10 pasos (ritual inicio → escucha → clasifica outcome-type → decide conduzco/delego → convoca scope-scan → consolida + Filtro PO → carga template → drafta WA → presenta + confirma → indica próximo paso), so I can la entrada por defecto al sistema SEM-IA es uniforme + auditable + bibliográficamente anclada (no improvisación caso-a-caso)."

parent: cap-07-inception-greenfield

dimensions-affected: [product, technical, usability]  # Norman conceptual model transfer

depends-on:
  - feature-035-ritual-inicio-po  # paso 1 cubierto por feature-035
  - feature-018-slash-scope-scan  # paso 5 cubierto por feature-018
also-relates-to:
  - feature-039-cadena-was-greenfield  # paso 7 cuando gaps detected
related-adrs: []

status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005

fundamento-bibliografico:
  - Cagan — Inspired (PO classifica + decide con criterio bibliográfico)
  - Anthropic Claude Code docs (mecanismo Task tool subagentes)
---

# feature-038 · PO Modo 1 con protocolo de 10 pasos

## Problem

Sin un protocolo declarativo del Modo 1, el PO al recibir propuesta humana operaría caso-a-caso: a veces clasificaría primero, a veces convocaría scope-scan antes, a veces draftearía WA sin Filtro PO. Resultado: entrada al sistema heterogénea + no auditable.

## Hypothesis

Protocolo de 10 pasos canónicos en agent file PO (sección "Protocolo del Modo 1"):
1. Ritual de inicio (panorámica)
2. Escucha + clarifica
3. Clasifica outcome-type
4. Decide conduzco/delego
5. Convoca scope-scan multi-rol
6+6b. Consolida outputs + Filtro PO regla 12
7. Carga template + adapta
8. Drafta WA autocontenido + briefings
9. Presenta al humano + confirma
10. Indica próximo paso (Modo 2 si PO, handoff a otro rol si no)

## Stories

4 stories (agrupando pasos cubiertos por features hermanas):

- **story-038-A**: PO escucha propuesta humano + clarifica si ambigua + clasifica outcome-type (pasos 2-3)
- **story-038-B**: PO decide conduzco o delego (paso 4)
- **story-038-C**: PO carga template + adapta + drafta WA autocontenido con briefings por step (pasos 7-8)
- **story-038-D**: PO presenta WA al humano + confirma + indica próximo paso (pasos 9-10)

Pasos 1 (ritual inicio) y 5-6 (scope-scan + Filtro PO) cubiertos por feature-035 + feature-018 + protocolo Nivel 3 regla 12 (ya formalizado en agent file).

## Piezas del bootstrap

- Agent file PO `.claude/agents/product-owner.md` sección "Protocolo del Modo 1 — Entrada al sistema" con 10 pasos declarados.
- Aplicado en práctica: WA-001 (aborted), WA-002, WA-003, WA-004 (aborted), WA-005 (este).
