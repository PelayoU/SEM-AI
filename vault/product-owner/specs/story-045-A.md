---
type: story
id: story-045-A
title: "README incluye 3 rutas de lectura por audiencia"
parent: feature-045-ruta-lectura-audiencia
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-045-A — 3 rutas por audiencia

## Narrativa

**Como** newcomer ante README de 65 KB,
**quiero** ver sección "Cómo leer este repo" con ≥3 rutas según audiencia (técnica / académica / adoptante),
**para** seguir progressive disclosure y NO leer linealmente.

## Examples

1. **Ruta técnica** (contribuyente / arquitecto interesado): leer tesis → modelo conceptual → bootstrap-summary → workflows.md → agent files.
2. **Ruta académica** (evaluador TFM/GISF): leer tesis → visión + goals + capabilities → library bibliográfica → WAs archivados como evidencia.
3. **Ruta adoptante** (ingeniero / equipo): leer tesis → cómo arrancar → primer WA → cautelas de privacidad.
4. **Cada ruta tiene path explícito**: README enumera archivos en orden recomendado.
5. **Rutas no exhaustivas**: cubren ~60-70% del repo (el operador puede ahondar después si quiere).

## AC

- **AC-A1**: README incluye sección "Cómo leer este repo" con encabezado visible.
- **AC-A2**: La sección declara ≥3 rutas (técnica + académica + adoptante) o equivalentes según audiencias relevantes.
- **AC-A3**: Cada ruta enumera archivos/secciones en orden recomendado (no aleatorio).

## Test mecánico

✅ 5 examples · ✅ 3 AC · ✅ Gherkin descendible. **PASA**.
