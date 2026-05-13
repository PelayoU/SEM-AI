---
type: story
id: story-039-A
title: "PO detecta gaps upstream durante scope-scan"
parent: feature-039-cadena-was-greenfield
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-039-A — Gaps upstream detectados

## Narrativa

**Como** PO durante scope-scan multi-rol (Modo 1 paso 5),
**quiero** que los advisors flag-en gaps upstream (no hay capability padre, no hay goal padre, no hay visión) si la propuesta los requiere,
**para** detectar la necesidad de cadena de WAs antes de comprometer scope.

## Examples (discovery)

1. **Greenfield vault vacío**: humano propone feature. Advisors (PO + 5) detectan: no hay visión, no hay goals, no hay capability padre. Gaps en 3 niveles.
2. **Proyecto maduro sin capability**: vault tiene visión + goals pero falta capability que cubra la feature propuesta. Gap en 1 nivel.
3. **Proyecto maduro con visión-realignment**: propuesta cuestiona visión vigente. Gap meta (no es upstream técnico — es modificación lateral).
4. **Sin gaps**: propuesta encaja con capability existente. Cadena de 0 WAs upstream — directo a feature-design.
5. **Flags coordinados**: cada advisor flag-ea independientemente. PO consolida con Filtro PO.

## AC

- **AC-A1**: Cada advisor (PO + 5) durante scope-scan inspecciona si el WA necesita padre upstream que no existe.
- **AC-A2**: PO consolida flags upstream aplicando Filtro PO regla 12.
- **AC-A3**: Si hay gaps consolidados, PO presenta resumen al humano antes de proponer cadena.

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
