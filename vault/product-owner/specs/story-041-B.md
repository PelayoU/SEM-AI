---
type: story
id: story-041-B
title: "Evaluador académico ve atribución bibliográfica + corpus"
parent: feature-041-readme-onboarding
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-041-B — Evaluador académico ve atribución + corpus

## Narrativa

**Como** evaluador académico (TFM / GISF) leyendo README,
**quiero** ver atribución bibliográfica explícita (autores citados con formato académico breve) + referencia al corpus auditable en `vault/architect/research/library/`,
**para** validar el rigor académico del framework sin tener que abrir cada SKILL.md o capability file.

## Examples

1. **Citas en README**: cuando README menciona conceptos clave (Cagan dual track, Patton story map, Cohn INVEST, Adzic SbE), cita autor + obra entre paréntesis (formato académico breve).
2. **Sección "Anclaje bibliográfico"**: README incluye sección dedicada listando las 18 notas en library + referenciando INDEX.md.
3. **bootstrap-summary referenciado**: README enlaza a `vault/architect/research/bootstrap-summary.md` (16 decisiones + 8 lecciones).
4. **GISF context**: si aplica, README menciona deadline académico + contexto TFM.
5. **Apache 2.0**: README declara LICENSE con razón ("Apache 2.0 — sin riesgo viral; permite fork comercial + distribución comunitaria").

## AC

- **AC-B1**: README cita autores aplicados en formato breve `(Autor, Año, Obra)` cuando menciona conceptos bibliográficamente anclados.
- **AC-B2**: README incluye sección "Anclaje bibliográfico" o equivalente que lista corpus library + referencia bootstrap-summary.md.
- **AC-B3**: README declara LICENSE Apache 2.0 con justificación corta.

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
