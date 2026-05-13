---
type: feature
id: feature-034-slash-sessions
title: "Slash `/sessions` con catálogo de modos de trabajo + atajos npm"

jtbd-outcome: "Cuando el operador humano necesita saber qué sesiones de rol existen y cuándo invocar cada una, quiere ejecutar `/sessions` y recibir catálogo legible (8 roles × atajos npm + descripción 'cuándo abrir cada uno'), so I can reducir recall cognitive (Nielsen #6) y acelerar el cambio entre roles."

parent: cap-06-visibilidad-operativa

dimensions-affected: [product, usability]  # Nielsen #6 recognition over recall

depends-on: []
also-relates-to:
  - cap-02-multirol-agentes-homologos  # los 8 roles existen por CAP-B
related-adrs: []

status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005

fundamento-bibliografico:
  - Nielsen #6 Recognition rather than recall
  - Nielsen #7 Flexibility and efficiency of use
---

# feature-034 · Slash `/sessions` con catálogo de modos de trabajo

## Problem

8 roles + 9 atajos npm. Un operador humano newcomer (o intermedio) puede olvidar qué atajo corresponde a qué rol, especialmente bajo presión durante un WA con múltiples handoffs (Architect → Developer → QA). Sin slash dedicado, debe consultar README o `package.json`.

## Hypothesis

Slash `/sessions` que produce tabla compacta rol × atajo × cuándo abrir, accesible desde cualquier sesión.

## Stories

- **story-034-A**: Operador ejecuta `/sessions` y ve los 8 roles + atajos npm + descripción "cuándo invocar cada uno"
- **story-034-B**: Operador filtra `/sessions` por dominio (technical/usability/business/security/quality/operations) y ve solo roles relevantes (extension futura, NO en WA-005)

(Solo story-034-A se implementa en este WA — story-034-B es preview futura).

## Piezas del bootstrap

- Documentación de `/sessions` en CLAUDE.md raíz.
- Información subyacente: `vault/shared/governance/role-catalog.md` + `package.json` scripts.
