---
type: research
id: bootstrap-summary
title: "Bootstrap manual de SEM-IA — historia y decisiones clave"
status: active
created: 2026-04-30
updated: 2026-05-10
author: pelayo
tags: [bootstrap, summary, historical, operational-model]
---

# Bootstrap manual de SEM-IA — historia y decisiones clave

## Contexto

Este documento registra el trabajo manual hecho **antes de que SEM-IA pudiera operar bajo sus propios protocolos**. Sin él, en sesiones futuras nadie (ni humano ni agentes) recuerda qué se construyó, qué decisiones se tomaron, ni qué quedó pendiente.

El bootstrap manual fue lo suficiente para que SEM-IA arranque inception real con identidades, skills y governance operativos. **A partir de ahí, el propio SEM-IA construye sus features bajo sus protocolos** (dogfooding total, goal-1).

> **Nota:** detalles operativos del modelo (estructura del repo, agents, skills, workflows, dimensiones, roles) viven en sus archivos canónicos: `vault/shared/governance/{dimensions,role-catalog,workflows,verification-matrix,repo-structure}.md`, `.claude/agents/`, `.claude/skills/`, `CLAUDE.md` raíz, `README.md`. Este documento solo conserva **historia + decisiones clave + lecciones**.

## Decisiones clave tomadas durante el bootstrap

Las siguientes decisiones convergieron en el modelo actual tras múltiples iteraciones. Cada una resuelve una tensión real encontrada durante el bootstrap.

| Decisión | Justificación clave |
|---|---|
| **Agentes en `.claude/agents/`, skills en `.claude/skills/<rol>/<skill>/SKILL.md`** | Convenciones nativas de Claude Code Agent Skills (agentskills.io). Permite organización por rol + descubrimiento nativo. |
| **CLAUDE.md jerárquico** (root + por subdirectorio del vault) | Modelo híbrido: recepción al root, sesiones dedicadas multi-turn por rol. Aprovecha mecanismo nativo de Claude Code sin inventar capa nueva. |
| **Vault organizado por rol custodio** (role-first) | Auto-explicativo + extensible. Adopter custom añade rol = `mkdir vault/<rol>/`. |
| **Modelo grafo dirigido con espina dorsal jerárquica + cross-links** | Sustituye terminología "pirámide" (oculta cross-links reales). `parent` + `also-relates-to` + `depends-on` + `dimensions-affected` + `related-adrs` declarados en frontmatter de cada nodo. |
| **Bibliografía en `vault/architect/research/library/`** (17 notas) | Anclaje auditable de cada skill. Sin esto, las skills descansan en conocimiento externo no auditable. Cada decisión cita su fuente. |
| **Estructura de nodos inline en skills** (no archivos template separados) | La IA crea los nodos; la estructura del frontmatter vive en la skill que produce ese nodo. Skills self-contained. |
| **Recepción es PM puro** | Solo crea WAs (drafting + scope-scan + workflow template) y verifica al cierre. Cada step se ejecuta en sesión dedicada del rol active. Modelo simétrico, sin escape hatch. Aprovecha patrón empresarial estándar: PM coordina, especialistas ejecutan. |
| **Algoritmo único de verificación al cierre del WA** | `verifiers = { custodian(d) : d ∈ dimensions-affected }`. `dimensions.md` es la única fuente de verdad para mapeo dimensión → custodio. `verification-matrix.md` queda como guía orientativa, no algoritmo. |
| **Scope-scan flat parallel en 3 checkpoints uniformes** | Creation + post-step + verify, todos con el mismo mecanismo (asesores en paralelo via Task tool). Captura discovery colaborativa + drift bottom-up + veredicto final. Coste ~$1.50-2 por WA con prompt caching, despreciable vs rework por drift no detectado. |
| **`outcome-type` + `steps[]` en frontmatter del WA + workflow templates por fase SDLC** | Captura la contribución central: **encoded enterprise workflows en formato AI-ejecutable**. Templates por fase (discovery/design/implementation/operations/meta). Backlog emerge gratis como query sobre `status: ready-for-implementation`. |
| **Handoff explícito al completar step** | Cada agent file tiene regla obligatoria: marca step done + Progreso entry + post-step scope-scan + indicación verbal del siguiente step. El humano nunca tiene que pensar qué viene después. |
| **Contrato bidireccional "Al arrancar tu step" + "Para el siguiente step"** | Bracketea el trabajo de cada rol con checklist de lectura inicial + entrada Progreso downstream-ready + audit-ready. Resuelve el problema de "lectura a ciegas" entre steps secuenciales. |
| **Templates indexados por fase SDLC + ruptura `feature` en `feature-design`/`feature-build`** | El template `feature` monolítico arrastra discovery + design + implementation en un único WA gigante; descartado. Modelo final: `feature-design` (fase design, produce spec ready-for-implementation) + `feature-build` (fase implementation, consume spec, produce código). WAs más cortos, post-step scope-scan respeta planos cognitivos, timing realista, backlog persistente sin estructura nueva. |
| **Designer + Business Analyst añadidos al catálogo core** (alineación con 4 risks de Cagan) | Cagan principio 3: 4 risks abordados antes de construir. Sin Designer (usability) y Business-analyst (business viability), 2 de los 4 risks quedan sin custodio. Adopters consumer/B2C tendrían fricción de añadirlos como custom. |
| **Anclaje bibliográfico explícito a los 3 principios de Cagan + Patrón colaborativo encouraged** | El motor ya soportaba el flujo colaborativo (scope-scan multi-rol + subagent invocation mid-step + post-step scope-scan); el refuerzo explicitó la alineación bibliográfica con Cagan, para que adopters reconozcan inmediatamente el modelo y usen activamente el give-and-take entre custodios. |
| **Dual Track Discovery + Delivery (Cagan/Patton) explicitado** | Múltiples WAs activos simultáneamente; backlog persistente entre fases design e implementation. `/status` agrupa WAs por track (Discovery / Delivery / Operations / Meta) con vista de salud Dual Track. |
| **`/adopt` (adopción retroactiva) movido a Pendientes del README** | SEM-IA mismo es mal primer caso de prueba para adopción retroactiva (meta-proyecto declarativo en markdown). El bootstrap orgánico (cadena de WAs por gaps) cubre los casos del día a día. La adopción retroactiva es optimización para proyectos consumer/B2C maduros, se construirá como feature formal cuando emerja necesidad real. |
| **Refactor Coach-out + fusión dimensiones strategy+product (2026-05-10)** | El profesor (validador académico) señala que el Coach es figura Scrum, no Cagan. En Cagan, el Product Manager extendido cubre desde visión hasta features (escalando a Product Leader en empresas grandes). Para ingeniero solitario, el Coach es proxy del humano. **Decisiones combinadas**: (a) eliminar rol Coach (8 roles, no 9); (b) fusionar dimensión `strategy` con `product` (7 dimensiones, no 8) con PO como custodio único de value-risk; (c) simplificar jerga "Patrón A/B/C" → descripciones operativas; (d) reducir bootstrap-summary (este archivo); (e) añadir campo `jtbd-outcome` al frontmatter de feature (Cagan principio 1: *solve problems, not features*). El PO extendido absorbe las 4 skills estratégicas (vision-quality-check, goal-quality-check, capability-quality-check, capability-derivation) movidas a `.claude/skills/product-owner/strategy/`. Visión + 7 goals movidos a `vault/product-owner/strategy/`. Post-step scope-scan se mantiene como motor estructural de colaboración multi-rol (Cagan principio 2). |

## Lecciones aprendidas

1. **Bootstrap mínimo no fue mínimo suficiente.** La intuición original ("plantillas + schemas + AGENTS.md") asumía que las skills emergerían "como features post-inception". En la práctica, sin skills core operativas, la inception se hace improvisando — lo cual contradice el principio de SEM-IA de auditoría.

2. **Agentes y skills son condición operativa, no feature.** Documentar bibliografía y diseño en vault + materializar skills en `.claude/skills/` es trabajo de bootstrap, no trabajo "post-inception".

3. **El modelo grafo necesita ser explícito desde plantillas.** Sin cross-link fields en frontmatter, los nodos se crean estructuralmente correctos pero conceptualmente incompletos (sin aristas).

4. **"Pirámide" es legacy term que confunde.** El modelo real es grafo dirigido con espina dorsal jerárquica. Sustituir terminología es trivial pero importante.

5. **Subagents one-shot no soportan trabajo conversacional multi-turn.** Por eso el modelo híbrido (sesiones dedicadas por rol con CLAUDE.md jerárquico) es necesario para inception y otras tareas multi-turn deep.

6. **La bibliografía debe vivir en el vault**, no como referencias externas. Sin esto, las skills descansan en conocimiento no auditable.

7. **Working Agreements son para post-bootstrap.** Durante el bootstrap manual, los WAs se crearon prematuramente y se eliminaron. Los WAs se activan cuando inception arranca, no antes.

8. **Más roles ≠ más rigor.** Cagan no tiene rol Coach; eliminar el Coach IA (proxy del humano) reduce fricción sin perder capacidad. **Menos jerga + menos abstracciones ≠ menos modelo**: simplificar la nomenclatura (Patrón A/B/C → descripciones operativas) mejora comunicabilidad sin cambiar el motor.

## Próximos pasos previstos

1. **Inception real** del subgrafo estratégico en sesión dedicada del PO extendido (`npm run po`): derivar capabilities desde los 7 goals existentes con `capability-derivation` + `capability-quality-check`.
2. **Construcción de features del framework bajo SEM-IA** — vault-cli como primera feature crítica.
3. **Caso de portabilidad** (stablecoin DeFi u otro proyecto) cuando el framework esté estabilizado.
4. **Documentación pública** y entregables académicos del máster (GISF deadline 25 mayo 2026, TFM).
