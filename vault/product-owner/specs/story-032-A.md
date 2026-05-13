---
type: story
id: story-032-A
title: "Operador ve panorámica completa con /status"
parent: feature-032-slash-status
status: active
created: 2026-05-13
author: product-owner
parent-wa: wa-2026-05-13-005
---

# story-032-A — Operador ve panorámica completa con /status

## Narrativa

**Como** operador humano (o agente al arrancar sesión),
**quiero** ejecutar `/status` desde cualquier sesión y recibir snapshot agregado en 6 secciones canónicas (Estrategia + Producto + Arquitectura + WAs activos + Backlog + Audits),
**para** validar estado conocido del proyecto sin re-explorar el vault manualmente.

## Examples (discovery)

1. **Proyecto greenfield**: operador ejecuta `/status` con vault vacío. Output: Estrategia (visión: ausente · Goals: 0 · Capabilities: 0); Producto (features: 0); Arquitectura (ADRs: 0); WAs (sin WAs activos); Backlog (vacío); Audits (vacío).
2. **Proyecto maduro**: operador ejecuta `/status`. Output muestra subgrafo estratégico (visión active + 7 goals + 10 capabilities), WAs activos agrupados por track, backlog con N specs, features por status, ADRs por status, counts audits.
3. **Proyecto con backlog**: Backlog query computado en tiempo real: `find vault/ -name "*.md" | xargs grep -l "status: ready-for-implementation"`. Output incluye N nodos + sus IDs.
4. **Proyecto con audits**: secciones audits muestran counts por tipo (threat-models, usability reviews, business reviews, QA reports) sin entrar al contenido.
5. **Operador en sesión architect**: ejecuta `/status` desde sesión architect. Mismo output (slash es transversal — el formato no cambia por rol).
6. **Performance**: `/status` ejecuta queries sobre filesystem en O(N) donde N = nodos del vault. Aceptable para proyectos pequeños/medios. Para vault muy grande (1000+ nodos), considerar caching futuro (ADR latente potencial).

## Acceptance Criteria

- **AC-A1**: `/status` produce output con 6 secciones canónicas siempre presentes (vacías si no hay contenido): Estrategia · Producto · Arquitectura · WAs activos · Backlog · Audits.
- **AC-A2**: Sección Estrategia incluye: visión (active/draft/ausente), Goals (count + IDs), Capabilities (count + status).
- **AC-A3**: Sección Producto incluye: Features agrupadas por status (draft/active/ready-for-implementation/in-implementation/implemented/deprecated).
- **AC-A4**: Sección Backlog ejecuta query emergente sobre nodos con `status: ready-for-implementation` y reporta count + IDs (absorbe story-005-A reclasificada — backlog query como AC, no feature aparte).

## Cross-links

- **also-relates-to**: feature-035 (ritual inicio PO) — el ritual replica el formato canónico de `/status` al arrancar.
- **also-relates-to**: feature-005 reclasificada → ADR-latente-008 Backlog query (apuntada en AC-A4).

## Test mecánico Adzic SbE

✅ 6 examples concretos.
✅ 4 AC SMART verificables.
✅ Spec Gherkin descendible.

Test mecánico **PASA**.
