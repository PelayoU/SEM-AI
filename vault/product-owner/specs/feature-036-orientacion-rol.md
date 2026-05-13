---
type: feature
id: feature-036-orientacion-rol
title: "Orientación al operador sobre qué rol abrir ante ambigüedad"

jtbd-outcome: "Cuando el operador humano duda qué sesión de rol abrir ante una propuesta o trabajo ambiguo (¿es product? ¿es technical? ¿es business?), quiere consultar criterio expresado en lenguaje de decisión del operador (CLAUDE.md raíz + tabla delegación PO + `/sessions`), so I can saber qué sesión abrir sin leer páginas de documentación + recovery si ya está en sesión equivocada (Nielsen #6 + #9)."

parent: cap-06-visibilidad-operativa

dimensions-affected: [product, usability]  # Nielsen #6 + #7 + #9

depends-on: []
also-relates-to:
  - cap-02-multirol-agentes-homologos
  - feature-034-slash-sessions  # mecanismo /sessions cubre parte del JTBD orientación (cat-1 Filtro PO post-step 3-6)
related-adrs: []

status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005

fundamento-bibliografico:
  - Nielsen #6 Recognition rather than recall
  - Nielsen #7 Flexibility and efficiency of use
  - Nielsen #9 Help users recognize, diagnose, recover from errors
---

# feature-036 · Orientación qué rol abrir ante ambigüedad

## Problem

8 roles custodios + propuestas del humano que a veces son ambiguas en dominio. Ej.: "diseñar feature de login" toca product (PO) + usability (Designer) + security (Security) + technical (Architect). El operador humano puede:
1. Empezar en sesión equivocada (ej. arch cuando debería ser sem).
2. Hesitar antes de elegir sesión, retrasando arranque.
3. No saber que existe la posibilidad de delegación cross-rol.

## Hypothesis

Si proveemos criterio explícito de orientación:
- En **CLAUDE.md raíz** sección "Cómo arrancar trabajo" con tabla "si dudas qué sesión arrancar".
- En **agent file PO Modo 1 paso 4** tabla "decide conduzco/delego" con criterios.
- En **`/sessions`** output con descripción "cuándo invocar cada rol".

Y un **mecanismo de recovery** cuando el operador ya está en sesión equivocada: el rol activo detecta scope ajeno y comunica al operador "esta no es decisión de mi dominio; sal y abre `npm run <rol-correcto>`".

Entonces el operador sabe orientarse + recupera si se equivocó (Nielsen #9).

## Stories

- **story-036-A**: Operador humano consulta criterio de orientación en CLAUDE.md raíz o `/sessions` antes de arrancar sesión (Nielsen #6)
- **story-036-B**: Operador humano YA en sesión equivocada recibe recovery del rol activo (Nielsen #9 error recovery — absorbe AC adicional Designer flag post-step)

## Piezas del bootstrap

- CLAUDE.md raíz sección "Cómo arrancar trabajo" con criterio.
- Agent file PO Modo 1 paso 4 "decide conduzco/delego" con tabla.
- `/sessions` output con descripción cuándo invocar cada rol.
- Comportamiento de cada rol custodio al detectar scope ajeno (declarado en cada agent file).
