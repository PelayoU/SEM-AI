---
type: working-agreement
id: wa-{{DATE}}-{{SLUG}}
created: {{DATETIME}}
status: active
phase: discovery

# Qué se va a hacer
objective: "{{OBJETIVO}}"
related-feature: {{FEATURE_ID}}
related-capability: {{CAPABILITY_ID}}

# Quién está activo
active-role: {{CUSTODIO_PRINCIPAL}}

# Custodios que participarán en construcción
participants: [{{ROLES}}]

# Alcance autorizado
scope-allowed:
  - {{PATHS_PERMITIDOS}}
scope-forbidden:
  - {{PATHS_PROHIBIDOS}}

# Niveles del grafo afectados
pyramid-levels-affected: [{{LEVELS}}]
pyramid-levels-locked: [{{LOCKED_LEVELS}}]

# Dimensiones afectadas
dimensions-affected: [{{DIMENSIONS}}]

# Verificación al cierre
verifiers-required: [{{VERIFICADORES}}]

# Criterio de cierre
closure-criteria:
  - {{CRITERIO_1}}
  - {{CRITERIO_2}}
---

# Plan de pasos

1. {{PASO_1}}
2. {{PASO_2}}
3. {{PASO_3}}

# Progreso

{{Se actualiza conforme avanza el trabajo.}}
