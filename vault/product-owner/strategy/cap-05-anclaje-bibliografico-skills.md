---
type: capability
id: cap-05-anclaje-bibliografico-skills
title: "Anclaje bibliográfico auditable mediante skills empaquetadas y biblioteca canónica"

parent: goal-2-output-auditable-multirol

also-relates-to:
  - goal-4-rigor-multirol-individual
  - goal-6-articulacion-publica
depends-on: []
dimensions-affected: [product, quality]
related-adrs: []  # vacío hoy. Latente aplicable (step-3): ADR-latente-005 (skills como unidad de empaquetado bibliográfico)

status: active   # transición aplicada por /verify del WA wa-2026-05-12-002 el 2026-05-12T05:30+02:00
operational-status: operant

fundamento-bibliografico:
  - Cagan — Inspired + Empowered (anclaje en autoridad establecida vs improvisación)
  - Nygard — ADRs (auditabilidad bibliográfica de decisiones)
  - Bass — Software Architecture in Practice (maintainability + reusability como QAs)
  - Anthropic — Claude Code Agent Skills (mecanismo nativo de carga perezosa)
  - 18 notas canónicas en `vault/architect/research/library/` (Cagan, Sinek, Rumelt, Doerr, Doran, Torres, Christensen, Patton, Cohn, Adzic, Bass, Ford, Nygard, Martin, Ousterhout, Norman/Nielsen/Cooper/WCAG, Moore, Osterwalder)

qas-bass:
  - maintainability  # skills y library mantenibles cuando emergen nuevas fuentes
  - reusability      # skills empaquetadas reusables entre WAs
  - auditability     # cada veredicto cita su fuente con autor + año
  - learnability     # carga perezosa expone skill cuando contexto matchea

tactics:
  - "Each skill cites its source: SKILL.md frontmatter incluye sección `bibliographic foundation` con paths a library/"
  - "Skills as packaged happy-paths: SKILL.md (operativo: quick-reference + when-to-invoke + inputs + process + output) + design.md (referencia: diseño + ejemplos + fundamento + limitaciones)"
  - "Library indexed: `INDEX.md` cataloga las 18 notas; cada nota tiene formato canónico (autor, año, propuesta core, citas literales relevantes, aplicabilidad a SEM-IA)"
  - "Lazy loading: Claude Code Agent Skills cargan SKILL.md cuando el contexto matchea la `description` — sin coste de tokens si no aplica"

tradeoffs:
  - "18 notas requieren mantenimiento — primary sources puede tener ediciones superseded; vigilar con fitness function (Ford) de antigüedad"
  - "Skills lazy-load tiene latencia: el harness debe decidir si invocar — depende del matching de description (probabilístico, no determinístico)"
  - "Bibliografía como autoridad puede ser percibida como dogmática — mitigado por explicitar que es anclaje verificable, no canon obligatorio"
  - "design.md es opcional y duplicado de docs externos — coste vs valor de tener la versión interna parsed con citas literales relevantes para SEM-IA"

jtbd-outcome:
  quien: "Humano operador + agentes ejecutando skills + auditores externos (académicos, comunidad técnica)"
  job: "Tomar decisiones significativas (de producto, arquitectura, usabilidad, business, security, quality) anclando en autoridad bibliográfica verificable, no en improvisación heurística del agente o del humano"
  outcome-esperado: "Cada decisión significativa cita autor + año + obra; cada skill SE PUEDE leer como referencia auditable de cómo se opera el dominio; la biblioteca es accesible al evaluador externo para verificar el anclaje"
---

# CAP-05 · Anclaje bibliográfico auditable mediante skills empaquetadas y biblioteca canónica

## Enunciado

Cada decisión significativa del sistema (identidad de rol, skill aplicada, template de workflow, veredicto de verificación) **cita su fuente bibliográfica auditable**. **18 notas canónicas** en `vault/architect/research/library/` (Cagan, Sinek, Rumelt, Doerr, Doran, Torres, Christensen, Patton, Cohn, Adzic, Bass, Ford, Nygard, Martin, Ousterhout, Anthropic) + **INDEX.md** como catálogo navegable. **14 skills construidas** en `.claude/skills/<rol>/<skill>/SKILL.md` + `design.md` empaquetan happy-paths bibliográficos auditables. **Carga perezosa nativa** de Claude Code: la skill se invoca cuando el contexto matchea su `description`. **10+ skills documentadas como pendientes** en `_pending-later.md` con su bibliografía ya identificada.

## Por qué es capability fuerte (4 criterios)

1. **Habilidad diferenciada**: rigor por anclaje bibliográfico es propiedad cultural y operativa del sistema. Sin CAP-05, las skills son procedimientos sin autoridad — los veredictos no son auditables más allá de "lo dice el agente".
2. **Sirve a goals con métrica clara**: goal-2 (auditabilidad: cada decisión trazable a autor + año), goal-4 (rigor multi-rol vía conocimiento bibliográfico anclado).
3. **Cohesión interna**: library + skills + INDEX + carga perezosa + agentes que citan bibliografía en sus modos de trabajo — comparten el job *"rigor por anclaje, no improvisación"*.
4. **No es trivialmente subcapability**: no es feature de CAP-02 (los agentes podrían existir sin bibliografía citada — serían menos auditables pero existirían), ni de CAP-04 (verificación podría hacerse sin anclaje — sería más débil pero existiría). Es la **capa de autoridad** transversal.

## Piezas del bootstrap que la materializan

| Pieza | Path | Rol en la capability |
|---|---|---|
| 18 notas bibliográficas canónicas | `vault/architect/research/library/*.md` | Anclaje auditable de cada decisión |
| INDEX.md de la biblioteca | `vault/architect/research/library/INDEX.md` | Catálogo navegable |
| 14 skills construidas en `.claude/skills/` | 7 PO + 5 Architect + 1 Security + 1 Shared | Happy-paths bibliográficos empaquetados |
| Estructura SKILL.md + design.md por skill | convención del proyecto | Operativo + referencia con citas literales |
| `_pending-later.md` | `.claude/skills/_pending-later.md` | 10+ skills documentadas como pendientes con bibliografía identificada |
| Citas bibliográficas en cada agent file | `.claude/agents/*.md` sección "Bibliografía base" | Cada identidad de rol ancla en autores |
| Carga perezosa nativa Claude Code | mecanismo del harness | Skills invocables cuando description matchea contexto |

## Relación con goals

- **Goal-2 (output auditable, coherente y verificado multi-rol)** — parent primario. *"Cada decisión trazable a su origen"* requiere anclaje bibliográfico.
- **Goal-4 (rigor multi-rol con humano individual)** — el rigor descansa en bibliografía, no en experiencia de un equipo numeroso.
- **Goal-6 (articulación pública y validación académica)** — la validación académica refuerza con anclaje bibliográfico explícito (evaluador puede verificar fuentes citadas).

## Criterio observable para futuros `/verify`

Una feature descompuesta de CAP-05 es verificable si cumple:
- Cada skill nueva incluye en su SKILL.md sección `bibliographic foundation` con paths a `library/`.
- Cada decisión significativa (en agent file, capability, ADR, audit) cita autor + obra + año.
- Las 18 notas de `library/` están actualizadas (sin contradicciones internas + sin links rotos).
- INDEX.md está sincronizado con el contenido real de `library/`.
- `_pending-later.md` se mantiene como roadmap de skills futuras con bibliografía ya identificada.

## Features candidatas (preview)

1. **Estructura inline de SKILL.md** — secciones canónicas (quick-reference, when-to-invoke, inputs, process, output, bibliographic-foundation, WA mapping, limitations, status lifecycle).
2. **Estructura inline de design.md** — referencia detallada con ejemplos aplicados.
3. **Formato canónico de las notas bibliográficas** — autor, año, obra, propuesta core, citas literales relevantes, aplicabilidad a SEM-IA.
4. **INDEX.md como catálogo navegable** — formato y mantenimiento.
5. **Mecanismo de descubrimiento de skills** — carga perezosa nativa Claude Code (no construido por SEM-IA, sí declarado como dependencia y usado).
6. **Roadmap `_pending-later.md`** — skills pendientes con bibliografía pre-identificada.

## Notas / gaps operativos conocidos

- **Library puede tener primary sources superseded** — algunas obras tienen ediciones nuevas no incorporadas. Vigilar como fitness function (Ford).
- **Carga perezosa es probabilística** — depende del matching de la `description` de la skill con el contexto. No garantiza invocación. Mitigación: descripciones bien escritas + monitoring de cuándo NO se invocó cuando aplicaba.
- **Skills Designer + Business-analyst aún sin formalizar** (operan con guía bibliográfica directa). Pendiente cuando emerjan necesidades B2C/consumer + business.
- **Algunas skills no tienen design.md** — opcional, no bloquea operatividad pero reduce profundidad de referencia.
