---
type: research
id: skills-pending-later
title: "Skills pendientes de redactar — fase later"
status: draft
created: 2026-04-30
updated: 2026-05-10
author: pelayo
tags: [skill-borrador, todo, pending, product-owner]
---

# Skills pendientes — fase later

Las skills del happy-path están redactadas. Estas 9 quedan **pendientes** y se redactarán como features bajo SEM-IA real (post-inception), siguiendo el flujo: PO escribe spec → Architect aporta viabilidad técnica → materialización.

**Importante:** estas skills NO se necesitan para que la inception próxima funcione. Las del happy-path son suficientes. Estas se construyen cuando su demanda emerja del uso real.

## Product Owner extendido — 9 skills pendientes

Tras el refactor Coach-out, el Product Owner extendido absorbe todas las skills estratégicas que antes eran del Coach. Las 9 pendientes se dividen en lado estratégico (4) y lado operativo (5).

### Lado estratégico (4)

#### `strategy-review`
Revisión periódica del subgrafo estratégico para detectar derivas, goals sin capabilities asociadas, cross-links faltantes, contradicciones entre niveles.
- **Bibliografía principal:** [[library-rumelt-good-strategy]], [[library-doerr-okrs]] (+Cagan).
- **Trigger:** invocación periódica del humano (ej: cada cierre de release o cada 3-6 meses).
- **Por qué later:** la inception inicial no requiere review periódica. Esta skill se necesita cuando el subgrafo lleva tiempo en uso.

#### `vision-realignment`
Arbitraje cuando un cambio bottom-up cuestiona la visión o los goals. Facilita la conversación de tres opciones (descartar / modificar y propagar / documentar excepción).
- **Bibliografía principal:** [[library-cagan-product-vision]], [[library-rumelt-good-strategy]] (+Torres).
- **Trigger:** modo arbitraje según master doc sec. 11.
- **Por qué later:** se invoca solo cuando hay tensión real. Hasta que SEM-IA opere bajo flujo normal, no hay tensiones bottom-up que arbitrar.

#### `goal-decomposition`
Derivar goals desde una visión usando OKR (Objective + Key Results) y SMART.
- **Bibliografía principal:** [[library-doerr-okrs]], [[library-doran-smart]] (+Cagan).
- **Trigger:** durante WA `goal-definition` (cuando hay visión y se quieren derivar goals candidatos).
- **Por qué later:** en el happy-path inicial, esta skill se ejecuta **manualmente con la guía bibliográfica** (PO lee Doerr y Doran y propone). Cuando se formalice como skill, se automatiza más rigurosamente.

#### `capability-prioritization`
Ordenar capabilities en el roadmap por valor estratégico, dependencias y "concentración en aspectos pivotales" (Rumelt).
- **Bibliografía principal:** [[library-rumelt-good-strategy]], [[library-patton-user-story-mapping]] (+Torres).
- **Trigger:** producción de roadmap tras crear/redefinir capabilities, o priorización de capabilities en backlog.
- **Por qué later:** mismo razonamiento — el roadmap inicial puede hacerse manualmente con guía de Rumelt y Patton. Formalización después.

### Lado operativo (5)

#### `discovery-facilitation`
Conducir el workshop de discovery con el equipo, generando examples y opciones.
- **Bibliografía principal:** [[library-adzic-specification-by-example]], [[library-torres-continuous-discovery]] (+JTBD).
- **Trigger:** inicio de cada feature significativa.
- **Por qué later:** las primeras features del bootstrap del framework las puede facilitar el PO con conocimiento general de SbE/Torres. Skill formalizada cuando aparezca cliente externo del framework.

#### `example-elicitation`
Provocar examples concretos durante discovery (qué pasa si X, y si Y, casos límite).
- **Bibliografía principal:** [[library-adzic-specification-by-example]] (+Torres).
- **Trigger:** durante `discovery-facilitation`.
- **Por qué later:** parte de discovery-facilitation. Formalizar como skill separada después si se demuestra valor.

#### `story-writing`
Escribir story individual en formato Cohn ("Como X, quiero Y para Z") con criterios INVEST.
- **Bibliografía principal:** [[library-cohn-user-stories-invest]] (+Adzic).
- **Trigger:** durante `feature-decomposition`.
- **Por qué later:** el happy-path actual incluye stories embebidas en `spec-writing`. Skill separada útil cuando proyectos crezcan y stories se gestionen como nodos propios.

#### `backlog-prioritization`
Ordenar features por valor / esfuerzo, slicing por release.
- **Bibliografía principal:** [[library-patton-user-story-mapping]] (+Rumelt, Doerr).
- **Trigger:** al planificar release.
- **Por qué later:** en bootstrap inicial, el roadmap del PO (lado estratégico) actúa como priorización. Skill formalizada cuando haya múltiples features candidatas compitiendo.

#### `value-effort-estimation`
Estimar impact (valor) y effort (esfuerzo) relativos de features candidatas.
- **Bibliografía principal:** [[library-cohn-user-stories-invest]] (+JTBD).
- **Trigger:** input de `backlog-prioritization`.
- **Por qué later:** input de la anterior. Mismo razonamiento.

## Cómo se construirán

Estas 9 skills se construirán **bajo SEM-IA real**, una vez la inception haya producido el subgrafo estratégico y el flujo de features esté operativo. Cada skill será una **feature** descompuesta del PO:

1. Capability `cap-skills-po-completas` (cuelga de algún goal de auto-sostenibilidad).
2. Features: `feature-skill-strategy-review`, `feature-skill-vision-realignment`, etc.
3. Cada feature: spec en Gherkin con AC sobre el comportamiento de la skill.
4. Implementación: archivo `SKILL.md` en `.claude/skills/po-<skill>/` (estructura plana con prefijo de rol — Claude Code descubre skills planas en `.claude/skills/`, no soporta nesting profundo).

Esto cierra el bucle: el bootstrap manual produce las skills críticas, y SEM-IA construye las restantes con sus propios protocolos.

## Skills de OTROS roles también pendientes (para rondas siguientes)

Skills de Architect (más allá del happy-path), Security Officer (más allá de threat-modeling), QA, Designer, Business-analyst, DevOps, Developer no se documentan aquí en detalle. Tendrán su propio bootstrap manual mínimo cuando se necesiten para invocar a esos roles. La prioridad actual es el PO extendido porque conduce las primeras fases (inception → features). Architect ya tiene 5 skills; Security tiene 1 + later (access-control-review, vulnerability-scanning); Designer y Business-analyst arrancan con 0 skills materializadas (operan con guía bibliográfica directa); QA y DevOps con skills mencionadas en sus agent files pero no formalizadas en `.claude/skills/`.
