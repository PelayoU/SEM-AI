---
type: story
id: story-039-B
title: "PO propone cadena ordenada (3 formas)"
parent: feature-039-cadena-was-greenfield
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-039-B — PO propone cadena en 3 formas

## Narrativa

**Como** PO tras detectar gaps upstream,
**quiero** proponer cadena ordenada de WAs al humano en una de **3 formas canónicas** (directa greenfield / corta proyecto-maduro / modo arbitraje cross-cutting),
**para** que el humano vea el plan completo antes de comprometer.

## Examples (discovery)

1. **Cadena directa (greenfield)**: humano pidió feature en vault vacío. Cadena de 4 WAs: `vision-creation` → `goal-definition × N` → `capability-creation × M` → `feature-design × K`.
2. **Cadena corta (proyecto maduro)**: vault con visión + goals + capabilities pero sin capability que cubra la feature. Cadena de 2 WAs: `capability-creation` → `feature-design`.
3. **Modo arbitraje (cross-cutting)**: feature contradice visión vigente o toca múltiples capabilities. NO cadena automática. PO presenta 3 opciones al humano: (a) descartar el cambio, (b) modificar nivel superior y propagar (WA `vision-realignment` skill later), (c) documentar excepción consciente.
4. **N variable**: número de goals/capabilities/features no es fijo. PO propone basado en propuesta inicial; humano puede ajustar.
5. **Cada WA independiente**: cada WA tiene closure-criteria + on-close propios. Tras /verify de WA-N, PO drafta WA-N+1 (NO drafttea toda la cadena por adelantado).

## AC

- **AC-B1**: PO consulta `vault/shared/governance/workflows.md` sección "Cadena de WAs por gaps detectados" y propone una de 3 formas según contexto.
- **AC-B2**: Si forma = "modo arbitraje", PO presenta 3 opciones al humano explícitamente (descartar / modificar nivel / documentar excepción).
- **AC-B3**: PO drafta SOLO el primer WA de la cadena (no toda la cadena). Cada WA es independiente.

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
