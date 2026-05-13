---
type: story
id: story-035-A
title: "PO lee 5 directorios del vault al arrancar"
parent: feature-035-ritual-inicio-po
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-035-A — PO lee 5 directorios al arrancar

## Narrativa

**Como** operador agente PO al arrancar sesión via `npm run sem`,
**quiero** leer 5 directorios canónicos del vault (`vault/product-owner/strategy/`, `vault/shared/sessions/active/`, `vault/product-owner/specs/`, `vault/architect/adrs/`, `vault/shared/governance/`),
**para** construir mapa mental del estado del proyecto antes del primer prompt del humano.

## Examples (discovery)

1. **Greenfield**: 4/5 directorios vacíos (solo .gitkeep). PO lee gracefully, detecta vault vacío.
2. **Maduro**: directorios con contenido. PO lee counts + IDs por categoría (no contenido completo).
3. **Mid-WA**: hay WA activo en `vault/shared/sessions/active/`. PO lo identifica y prioriza Modo 2 (continúa step) sobre Modo 1 (nuevo input).
4. **Lectura selectiva**: PO lee frontmatter de archivos para counts + IDs. Contenido completo solo si el humano lo solicita o aplica skill que lo requiere.
5. **Errors silenciosos**: si algún directorio falta, PO lo nota pero continúa (no falla — el vault puede estar incompleto en greenfield).

## AC

- **AC-A1**: PO lee `vault/product-owner/strategy/` (visión + goals + capabilities counts + IDs).
- **AC-A2**: PO lee `vault/shared/sessions/active/` (WAs activos identificados).
- **AC-A3**: PO lee `vault/product-owner/specs/` + `vault/architect/adrs/` + `vault/shared/governance/` (counts por status, paths conocidos).

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
