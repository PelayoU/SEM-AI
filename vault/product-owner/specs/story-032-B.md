---
type: story
id: story-032-B
title: "Operador ve WAs activos agrupados por track Dual"
parent: feature-032-slash-status
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-032-B — WAs activos agrupados por track Dual

## Narrativa

**Como** operador humano que monitoriza el Dual Track del proyecto (Cagan/Patton),
**quiero** que `/status` agrupe los WAs activos por track (Discovery/Delivery/Operations/Meta) derivado del `outcome-type` del WA y de su fase SDLC,
**para** distinguir mentalmente qué bloques de trabajo descubren (Discovery), construyen (Delivery), operan (Operations) o cambian meta-procesos (Meta) — sin tener que abrir cada WA para clasificarlo.

## Examples (discovery)

1. **WA `vision-creation` activo**: agrupado en track **Discovery** (fase SDLC = discovery).
2. **WA `feature-design` activo**: agrupado en **Discovery** (fase = design).
3. **WA `feature-build` activo**: agrupado en **Delivery** (fase = implementation).
4. **WA `bugfix` activo**: agrupado en **Delivery** (fase = implementation).
5. **WA `pipeline-change` activo**: agrupado en **Operations** (fase = operations).
6. **WA `doc-edit` activo**: agrupado en **Meta** (fase = meta).
7. **Múltiples WAs simultáneos**: proyecto maduro con WAs en Discovery (WA-N+1 feature-design en discovery) + Delivery (WA-N feature-build activo) simultáneos = Dual Track materializado. `/status` los muestra en sus tracks respectivos.
8. **Ratio Discovery / Delivery**: opcional output adicional ratio (ej. "3 Discovery / 1 Delivery") como indicador de salud del Dual Track. Sin forzar ratio — anti-patrón Cagan: "solo Delivery" (waterfall disfrazado) o "solo Discovery" (parálisis por análisis).

## Acceptance Criteria

- **AC-B1**: Sección WAs activos agrupa por **4 tracks**: Discovery / Delivery / Operations / Meta. Mapping derivado de la fase SDLC del template del WA según `vault/shared/governance/workflows.md`.
- **AC-B2**: Por cada WA activo muestra: ID + outcome-type + current-role + steps done/total (lista compacta una línea por WA). Visualiza Dual Track Cagan/Patton (absorbe feature-037 Nivel 5 reclasificada).
- **AC-B3**: Si NO hay WAs activos, sección reporta "Sin WAs activos" (formato consistente).

## Cross-links

- **depends-on**: feature-013 (catálogo workflows.md Nivel 4) — mapping `outcome-type → fase SDLC` se lee de workflows.md.

## Test mecánico Adzic SbE

✅ 8 examples concretos.
✅ 3 AC SMART verificables.
✅ Spec Gherkin descendible.

Test mecánico **PASA**.
