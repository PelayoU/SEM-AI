---
type: research
id: library-patton-user-story-mapping
title: "Jeff Patton — User Story Mapping"
status: draft
created: 2026-04-30
author: pelayo
tags: [library, story-mapping, prioritization, product-owner]
applicable-roles: [product-owner]
---

# Jeff Patton — User Story Mapping

## Datos bibliográficos

- **Autor:** Jeff Patton (jpattonassociates.com)
- **Obra:** *"User Story Mapping: Discover the Whole Story, Build the Right Product"* (O'Reilly, 2014). Forewords: Martin Fowler, Alan Cooper, Marty Cagan.
- **Aplicabilidad SEM-IA:** dimensión `product` — Product Owner al planificar releases y priorizar el backlog.

## Tesis central

> *"User-story maps help Agile teams define what to build and maintain visibility for how it all fits together, enabling user-centered conversations, collaboration, and feature prioritization to align and guide iterative product development."*

El backlog plano es **inadecuado** para entender un producto. Una lista de stories pierde:
- El flujo narrativo del usuario.
- Las relaciones entre stories.
- La visión del producto entero.
- El plan de releases.

El **story map** es una representación bidimensional que recupera todo eso.

## Estructura del Story Map

```
                    NARRATIVE FLOW (left → right)
   Activity 1   Activity 2    Activity 3    Activity 4
   ─────────   ─────────    ─────────    ─────────
   Step 1.1    Step 2.1     Step 3.1     Step 4.1     ← Backbone
   ─────────────────────────────────────────────
                                                       ↑
                                                  Release 1
   Story 1.1   Story 2.1    Story 3.1    Story 4.1
   Story 1.2   Story 2.2    Story 3.2
                                                       ↑
                                                  Release 2
   Story 1.3   Story 2.3                  Story 4.2
```

### Eje horizontal — Narrative flow
- Las **actividades del usuario** y los **pasos** que sigue.
- Forman la "espina dorsal" (backbone) del map.
- Lectura izquierda → derecha = camino del usuario en el tiempo.

### Eje vertical — Priority / Detail
- Para cada paso, **stack de stories de mayor a menor prioridad**.
- Las stories de arriba son las críticas; las de abajo son enrichments.

### Líneas de release
- **Cortes horizontales** que definen qué se entrega cuándo.
- Release 1 = mínimo viable end-to-end del flujo entero (no una sola actividad completa).
- Cada release sigue siendo "thin slice" del producto entero.

## Insights clave de Patton

### 1. Build the whole story before slicing
Antes de priorizar, mapea el flujo entero. Solo entonces decides qué cortar y qué dejar para después.

### 2. Focus on outcomes, not features
> *"The secret to prioritization is to prioritize outcomes and not features."*

Pregunta: ¿qué outcome del usuario quieres habilitar al final del release? Las features se incluyen si contribuyen a ese outcome.

### 3. Different teams need different views
- El PO ve el map completo.
- Devs ven el slice de implementación.
- Ejecutivos ven la backbone + releases.
- Mismo artefacto, lecturas distintas.

### 4. Discovery vs. Delivery
- **Discovery:** usar el map para descubrir qué construir y por qué.
- **Delivery:** usar el map para coordinar implementación y releases.
- Patton enfatiza que el discovery es trabajo continuo, no fase única (alineado con Torres).

## Discovery process según Patton

1. **Frame the problem** — qué problema se está resolviendo, para quién.
2. **Understand customers and users** — entender contexto real.
3. **Envision solutions** — generar opciones múltiples.
4. **Plan releases** — slice horizontal del map.

## Aplicabilidad a SEM-IA

**Skill `product-owner.feature-decomposition`:** el story map es el formato canónico para descomponer una capability en features → stories y verlo como flujo.

**Skill `product-owner.backlog-prioritization`:** el corte horizontal de releases (release 1 = thin slice end-to-end) es la heurística de priorización canónica de Patton.

**Skill `coach.capability-prioritization`:** el equivalente al nivel capability — cuál se construye primero. La heurística "thin slice" aplica: la primera tanda de capabilities debería ya entregar valor end-to-end (aunque mínimo), no una capability "perfecta" sin las demás.

## Citas que anclan decisiones

> *"The secret to prioritization is to prioritize outcomes and not features."*

Aplicable a `coach.capability-prioritization` y `po.backlog-prioritization`: pregunta qué outcome del usuario habilitas, no qué features tachas.

> *"Build the whole story before slicing."*

Aplicable durante inception: tener visión y goals (whole story) antes de empezar capabilities concretas (slicing). Esto es exactamente lo que hicimos en WA-001.

## Limitaciones del framework

- El story mapping es muy visual. Adaptarlo a un grafo declarativo en markdown requiere convención: por ejemplo, releases como tags en frontmatter de capabilities/features.
- Patton orientado a productos consumer/B2B con flujo de usuario claro. SEM-IA es framework — el "usuario" es el equipo que adopta SEM-IA, y su "flujo" es el ciclo de desarrollo bajo el framework. Adaptación posible pero requiere traducción.
