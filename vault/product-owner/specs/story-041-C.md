---
type: story
id: story-041-C
title: "Adopter externo ve cautelas de privacidad"
parent: feature-041-readme-onboarding
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-041-C — Cautelas de privacidad para adopters

## Narrativa

**Como** operador humano adopter externo (ingeniero/equipo considerando aplicar SEM-IA en proyecto propio),
**quiero** ver en README sección explícita sobre cautelas de privacidad (vault = ground truth público por diseño + blast radius si repo se abre),
**para** decidir conscientemente cómo proteger información sensible antes de adoptar (no descubrirlo tarde).

## Examples

1. **Adopter con datos sensibles**: equipo aplicando SEM-IA en proyecto comercial con clientes. Lee cautelas, decide aplicar secret hygiene + revisar Progreso entries antes de commit.
2. **Adopter open-source**: proyecto OSS sin datos sensibles. Lee cautelas, confirma que blast radius no aplica.
3. **Adopter privado**: proyecto en repo privado. Lee cautelas, entiende que si el repo se abre o se filtra, vault entero queda público.
4. **Mensaje claro**: cautelas en formato visible (sección dedicada con encabezado tipo "⚠️ Cautelas para adopters" o "Privacy considerations").
5. **Vector I+R declarado**: cautelas explican que `/status` agrega vault completo, Progreso entries son auto-reportadas (vector R).

## AC

- **AC-C1**: README incluye sección "Cautelas de privacidad" o equivalente con encabezado visible.
- **AC-C2**: La sección explica que el vault es ground truth público por diseño + lista qué NO debe commitearse al vault (credenciales en frontmatter, tokens en Progreso entries, datos de clientes en specs).
- **AC-C3**: La sección referencia los vectores STRIDE applicable (vector I `/status` agregando vault; vector R Progreso entries no firmadas) **como honestidad Shostack** — declarar threat surface real, no aparentar protección que el framework no entrega.

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
