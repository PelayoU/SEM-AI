---
type: capability
id: cap-10-articulacion-publica
title: "Articulación pública del framework para audiencias externas (técnicas y académicas)"

parent: goal-6-articulacion-publica

also-relates-to:
  - goal-5-portabilidad
  - goal-1-auto-sostenibilidad
  - goal-2-output-auditable-multirol
depends-on: []
dimensions-affected: [product, business, usability]
related-adrs: []  # vacío hoy

status: active   # transición aplicada por /verify del WA wa-2026-05-12-002 el 2026-05-12T05:30+02:00
operational-status: operant

fundamento-bibliografico:
  - Cagan — Inspired (visión articulable como pre-condición de adopción)
  - Moore — Crossing the Chasm (comunicación a comunidad técnica como pre-condición de adopción más allá del autor)
  - Sinek — Start With Why (narrativa del por qué accesible al lector externo)
  - Nielsen — 10 heurísticas (#10 help/documentation legible y navegable)
  - Norman — Design of Everyday Things (modelo conceptual del framework para newcomer)

qas-bass:
  - usability        # legibilidad estándar de docs públicos (no WCAG formal — el repo es markdown en GitHub)
  - learnability     # newcomer puede entender SEM-IA sin contexto previo del autor
  - comprehensibility # narrativa coherente del framework para audiencias técnicas + académicas
  - maintainability  # docs actualizables sin breaking changes al concepto del framework

tactics:
  - "Progressive disclosure (Nielsen heuristic): README de alto nivel → CLAUDE.md raíz como guía estática → governance docs (5) para profundidad → library bibliográfica (18 notas) para anclaje teórico"
  - "Narrative coherence (Sinek why-how-what aplicado a docs): bootstrap-summary.md contextualiza la historia + decisiones clave; README explica QUÉ es SEM-IA y POR QUÉ"
  - "Licensing claro: LICENSE Apache 2.0 + namespace `@sem-ia` reservado para distribución futura"
  - "Multi-audiencia documentación: técnica (ingenieros adopters, comunidad open source) + académica (evaluadores TFM/GISF, investigación)"
  - "Repo público versionado: git como evidencia auditable del proceso completo (commits + WAs archivados + decisiones)"

tradeoffs:
  - "Docs verbose (README 65 KB) vs concision — adopter técnico puede sentirse abrumado; mitigado por progressive disclosure pero coste real"
  - "Jerga interna ('WA', 'scope-scan', 'vault', 'capability', 'dimensions-affected') difícil para externos sin glosario — pendiente glosario navegable"
  - "LICENSE Apache 2.0 permite forks comerciales — coherente con OSS pero deja la decisión de monetización futura abierta (sin tiers declarados)"
  - "Docs en markdown en GitHub no son web site con UX dedicada — aceptable hoy, limitante si el framework escala a comunidad amplia"

jtbd-outcome:
  quien: "Adopter externo técnico (ingenieros descubriendo el framework) + evaluador académico (TFM/GISF/investigación) + comunidad técnica open source (potencial contributor)"
  job: "Entender QUÉ es SEM-IA, POR QUÉ existe, CÓMO funciona conceptualmente, y SI/CÓMO podría aplicarlo a mi propio contexto — sin necesitar conversación con el autor"
  outcome-esperado: "El lector externo puede leer el repo y construir modelo conceptual del framework sin contexto previo; puede evaluar si SEM-IA aplica a su contexto; puede citar la propuesta en evaluación académica con anclaje bibliográfico verificable"
---

# CAP-10 · Articulación pública del framework para audiencias externas (técnicas y académicas)

## Enunciado

El framework está **articulado y publicado** para audiencias externas: comunidad técnica + evaluadores académicos. Documentación completa versionada en repo público: **README.md raíz** (onboarding completo del framework), **CLAUDE.md raíz** (guía estática + entry point), **bootstrap-summary.md** (historia + 16 decisiones clave + 8 lecciones), **governance docs** (5 archivos canónicos: dimensions, role-catalog, workflows, verification-matrix, repo-structure), **library bibliográfica** (18 notas + INDEX), **LICENSE Apache 2.0** (sin riesgo viral; permite fork comercial + distribución comunitaria). Soporta validación académica + adopción por comunidad técnica.

## Por qué es capability fuerte (4 criterios)

1. **Habilidad diferenciada**: articulación a audiencias externas es habilidad distinta de operar el framework. Sin CAP-10, SEM-IA es experimento privado; con CAP-10, entra en discurso técnico/académico compartible.
2. **Sirve a goals con métrica clara**: goal-6 declara métricas controlables *"README + bootstrap-summary + governance docs públicos y completos en el repositorio"* + *"trabajos académicos entregados a tiempo"*. CAP-10 las materializa.
3. **Cohesión interna**: README + CLAUDE.md raíz + bootstrap-summary + governance docs + library + LICENSE — comparten el job *"hacer el framework articulable a terceros"*.
4. **No es trivialmente subcapability**: no es feature de CAP-05 (anclaje bibliográfico interno) ni de CAP-08 (distribución técnica). Es habilidad de **comunicación pública**.

## Piezas del bootstrap que la materializan

| Pieza | Path | Rol en la capability |
|---|---|---|
| README.md raíz (65 KB) | `README.md` | Onboarding completo del framework + pendientes documentados |
| CLAUDE.md raíz | `CLAUDE.md` | Guía estática + tabla de roles + atajos + estructura conceptual |
| bootstrap-summary.md | `vault/architect/research/bootstrap-summary.md` | Historia del bootstrap + 16 decisiones clave + 8 lecciones aprendidas |
| Governance docs (5) | `vault/shared/governance/dimensions.md`, `role-catalog.md`, `workflows.md`, `verification-matrix.md`, `repo-structure.md` | 5 documentos canónicos que cualquier adopter consulta |
| Biblioteca canónica (18 notas + INDEX) | `vault/architect/research/library/*.md` | Anclaje bibliográfico accesible al evaluador externo |
| LICENSE | `LICENSE` | Apache 2.0 — sin riesgo viral, permite redistribución y forks |

## Relación con goals

- **Goal-6 (articulación pública y validación académica)** — parent primario. Métricas controlables explícitas: docs públicos + entregables académicos.
- **Goal-5 (portabilidad)** — adopters externos descubren el framework via documentación pública antes de adoptarlo técnicamente (CAP-08).
- **Goal-1 (auto-sostenibilidad)** — transparencia del dogfooding refuerza la tesis (terceros pueden ver el repo en operación).
- **Goal-2 (output auditable)** — docs son evidencia auditable de auditabilidad propia.

## Criterio observable para futuros `/verify`

Una feature descompuesta de CAP-10 es verificable si cumple:
- README.md raíz cubre: visión + propuesta + estructura + onboarding + pendientes.
- Governance docs (5) están sincronizados con el bootstrap actual (sin contradicciones internas).
- bootstrap-summary.md está actualizado con decisiones tomadas hasta la fecha de revisión.
- INDEX.md de library refleja las notas reales presentes.
- LICENSE Apache 2.0 sin riesgo viral, compatible con distribución.
- Docs son legibles a evaluador no-practicante (legibilidad estándar, no WCAG AA formal).
- Jerga interna explicada o glosada cuando aparece por primera vez en docs públicos.

## Features candidatas (preview)

1. **README.md raíz** — onboarding completo + secciones canónicas (visión, estructura, slash commands, agentes, governance, pendientes).
2. **CLAUDE.md raíz** — guía estática + entry point.
3. **bootstrap-summary.md** — historia + decisiones + lecciones; mantenido como histórico vivo.
4. **5 governance docs** — actualizados sincronizadamente.
5. **Biblioteca bibliográfica + INDEX** — 18 notas + catálogo navegable.
6. **Glosario público de términos SEM-IA** (planned futuro) — para audiencia externa que entra por primera vez (mitigación de jerga interna).
7. **Índice navegable del repo para newcomer** (planned futuro) — ruta sugerida de lectura para distintas audiencias (técnica vs académica).

## Notas / gaps operativos conocidos

- **README es verbose** (65 KB) — mitigado por progressive disclosure (high-level → detalle), pero adopter técnico puede sentirse abrumado al primer acceso. Glosario + índice navegable mejorarían UX externa.
- **Jerga interna sin glosario formal** — términos como "WA", "scope-scan", "vault", "capability", "dimensions-affected", "outcome-type" requieren contexto. Pendiente: glosario público.
- **No hay web site dedicado** — docs viven en markdown en GitHub. Aceptable hoy. Si SEM-IA escala a comunidad amplia, GitHub Pages o similar mejoraría discoverability.
- **Designer Q sobre WCAG formal**: descartado por PO — el repo es markdown en GitHub público, no web site con audiencia con discapacidades. Si en el futuro hay site académico/de publicación, reconsiderar WCAG AA.
- **Validación académica** (TFM/GISF) depende de evaluadores externos — métrica `signal` aspiracional, no controlable. CAP-10 provee la base (docs articuladas, bibliografía citable), no garantiza calificación.
- **Decisión consciente**: deadlines y roadmap quedan fuera de scope del catálogo de capabilities — el humano los gestiona (decisión cerrada con humano durante WA-002).
