---
type: story
id: story-035-B
title: "PO presenta panorámica al humano con formato canónico"
parent: feature-035-ritual-inicio-po
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-035-B — PO presenta panorámica al humano con formato canónico

## Narrativa

**Como** operador agente PO tras leer 5 directorios (story-035-A),
**quiero** presentar panorámica al humano con formato canónico (6 secciones: Estrategia + Producto + Arquitectura + WAs activos + Backlog + Audits) antes de pedir propuesta,
**para** que la conversación arranque con contexto compartido y el humano vea estado conocido.

## Examples (discovery)

1. **Greenfield**: panorámica muestra "Visión: ausente · Goals: 0 · Capabilities: 0 · ... · WAs activos: 0 · Backlog: vacío". PO termina con "Qué quieres hacer?".
2. **Maduro**: panorámica detallada con counts + IDs cortos por sección. PO termina con "Qué quieres hacer?".
3. **Coherente con `/status`**: formato similar al output del slash `/status` (feature-032). El ritual de inicio del PO ES funcionalmente un `/status` automático al arrancar sesión.
4. **Newcomer humano**: tras leer panorámica greenfield, humano comprende "el sistema espera mi propuesta para arrancar". Aplica Norman conceptual model transfer.

## AC

- **AC-B1**: Panorámica usa formato canónico de 6 secciones (Estrategia + Producto + Arquitectura + WAs activos + Backlog + Audits) — coherente con `/status` (feature-032).
- **AC-B2**: Tras panorámica, PO termina con "Qué quieres hacer?" (pregunta abierta al humano).
- **AC-B3**: Si vault vacío (greenfield), PO indica explícitamente "Sin WAs activos" + "Sin Backlog" + sugiere acciones de inception (cadena de WAs).

## Test mecánico

✅ 4 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
