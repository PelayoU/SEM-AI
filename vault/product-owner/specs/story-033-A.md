---
type: story
id: story-033-A
title: "Humano ve detalle del WA activo con /wa"
parent: feature-033-slash-wa
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-033-A — Humano ve detalle del WA activo

## Narrativa

**Como** operador humano en sesión durante un WA activo,
**quiero** ejecutar `/wa` y ver detalle del WA en contexto (steps + status + Progreso resumido + próximo step pending),
**para** ubicarme en el ciclo del WA sin abrir el archivo manualmente.

## Examples (discovery)

1. **Un solo WA activo**: `/wa` identifica el WA en `vault/shared/sessions/active/` automáticamente y muestra detalle.
2. **Múltiples WAs activos**: `/wa` pregunta al operador cuál (lista de IDs disponibles).
3. **Step in-progress**: marca el step actual con indicador visible.
4. **Próximo step pending**: muestra cuál es el próximo step + active-role esperado.
5. **Progreso entries**: muestra resumen 1-3 líneas por entrada (no contenido completo).
6. **Sin WA activo**: `/wa` reporta "Sin WAs activos. Para arrancar, ejecuta `npm run sem`."

## AC

- **AC-A1**: Identifica WA activo automáticamente si hay solo uno. Pregunta si múltiples.
- **AC-A2**: Output incluye: ID del WA + outcome-type + steps[] con status (pending/in-progress/done/aborted) + active-role por step + entrada Progreso resumida si done + próximo step pending destacado.
- **AC-A3**: Si NO hay WA activo, mensaje informativo con sugerencia de acción.

## Test mecánico

✅ 6 examples · ✅ 3 AC SMART · ✅ Gherkin descendible. **PASA**.
