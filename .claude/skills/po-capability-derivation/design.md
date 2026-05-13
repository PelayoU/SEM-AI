---
type: research
id: borrador-skill-po-strategy-capability-derivation
title: "Borrador de skill: product-owner.strategy.capability-derivation"
status: draft
created: 2026-04-30
author: pelayo
tags: [skill-borrador, product-owner, strategy, capability, derivation, happy-path]
---

# Borrador de skill: product-owner.strategy.capability-derivation

> **Estado: borrador.** Materialización en `.claude/skills/product-owner/strategy/capability-derivation/SKILL.md` durante Fase 5.

## Propósito

Derivar un conjunto de capabilities desde un goal aprobado, usando Opportunity Solution Tree (Torres) + lentes de coherencia estratégica (Rumelt). El output es un mapa goal → oportunidades → capabilities candidatas, que se filtra y formaliza con `capability-quality-check` y `graph-cross-link-declaration`.

## Cuándo se invoca

- **Trigger principal:** durante `inception-orchestration`, paso 4, después de aprobar goals.
- **Trigger secundario:** cuando un goal nuevo se añade post-inception y necesita su tanda de capabilities.
- **Trigger asistencial:** revisión periódica de un goal con capabilities consideradas insuficientes.

## Inputs

- Goal padre (frontmatter + resultado esperado + métricas + conexión con visión).
- Visión completa (para mantener coherencia top-down).
- Capabilities ya existentes (para evitar duplicación; permite detectar capabilities cross-link).
- Library: [[library-torres-continuous-discovery]], [[library-rumelt-good-strategy]], [[library-christensen-jtbd]].

## Proceso

### Paso 1 — Articular el outcome del goal en lenguaje OST
Reformular el goal como **outcome de negocio** según Torres. Forma: *"Movemos [métrica] de [estado actual] a [estado deseado]"*.

### Paso 2 — Identificar oportunidades
Generar lista de **oportunidades** (necesidades / gaps / pains) que, si se cubren, contribuyen al outcome. Una oportunidad es algo que el cliente necesita, no una solución.

Forma típica: *"El [usuario / adopter / equipo] [no puede / sufre / necesita] [X]"*.

Apuntar 3-7 oportunidades por goal. Más de 7 → el goal es demasiado amplio.

### Paso 3 — Generar soluciones (capabilities candidatas) por oportunidad
Para cada oportunidad, generar **2-3 soluciones distintas** (no enamorarse de la primera idea — Torres). Cada solución es un candidato a capability.

Forma típica: *"El sistema tiene la habilidad de [X]"*.

### Paso 4 — Filtrar por coherencia con guiding policy (Rumelt)
Para cada solución candidata: ¿está alineada con la guiding policy de la visión? Eliminar las que no lo estén o reformular.

### Paso 5 — Detectar overlap con capabilities existentes
Para cada candidata superviviente: ¿solapa con capability ya existente?
- Sí → no crear nueva, declarar cross-link en la existente.
- No → candidata para nueva capability.

### Paso 6 — Identificar cross-links a otros goals
Para cada nueva capability candidata: ¿sirve también a otros goals? Marcar `also-relates-to` candidatos para `graph-cross-link-declaration`.

### Paso 7 — Aplicar `capability-quality-check`
Cada candidata final pasa por la skill de quality-check antes de formalizarse en el vault.

## Outputs

- Lista priorizada de capabilities candidatas con:
  - Enunciado (título)
  - Oportunidad que cubre (justificación)
  - Parent (goal del que derivan)
  - Cross-links candidatos (`also-relates-to`)
  - Dimensiones afectadas tentativas
- Lista de cross-links a añadir a capabilities existentes (no crear nuevas).
- Razones explícitas de descarte para soluciones rechazadas (auditoría).

## Fundamento bibliográfico

- [[library-torres-continuous-discovery]] — Opportunity Solution Tree, multiplicidad de soluciones por oportunidad, assumption tests.
- [[library-rumelt-good-strategy]] — coherencia con guiding policy, concentración en aspectos pivotales.
- [[library-christensen-jtbd]] — articulación de oportunidades como "jobs to be done" del usuario / adopter.

## Ejemplos

### Ejemplo aplicado al goal-1 de SEM-IA (auto-sostenibilidad)

**Outcome reformulado:** Mover el desarrollo de SEM-IA del % "fuera del framework" actual a >90% "bajo SEM-IA".

**Oportunidades:**
- O1: el developer del framework no tiene infraestructura de gestión propia para construir el framework
- O2: las decisiones técnicas del framework no se documentan en su propio modelo
- O3: las features del framework no pasan por el flujo de specs / AC / verificación

**Soluciones candidatas (capabilities):**

Para O1:
- "Custodios homólogos por dimensión con catálogo extensible" → CAP-1
- "Sistema de invocación manual por slash command" (rechazada: no estructural)

Para O2:
- "Memoria compartida humano-agentes en grafo declarativo" → CAP-2
- "Documentación externa en wiki" (rechazada: viola single source of truth)

Para O3:
- "Coordinación por Working Agreements" → CAP-3
- "Governance estructural en escritura, commit, PR" → CAP-4
- "Code review manual" (rechazada: no escala)

Total derivadas para goal-1: 4 capabilities (CAP-1, 2, 3, 4).

### Ejemplo de detección de cross-link

Durante derivación para goal-2 (portabilidad), surge oportunidad: *"Otro proyecto que adopta SEM-IA necesita poder definir sus propias dimensiones del dominio"*.

Solución candidata: "Catálogo de dimensiones extensible".

Detección de overlap: esto YA está implícito en CAP-1 ("custodios homólogos con **catálogo extensible**"). En lugar de crear nueva capability, **declarar cross-link de CAP-1 a goal-2** (`also-relates-to: [goal-2]`). Documentar la decisión.

## Limitaciones

- La generación de oportunidades depende de conocer al usuario / cliente. Si la inception es por un humano que no conoce los adopters reales, las oportunidades serán especulativas — marcar como assumption tests pendientes.
- Generar 2-3 soluciones por oportunidad puede producir 15+ candidatas por goal. Filtrar agresivamente.
- La skill no garantiza completitud — puede faltar oportunidades que nadie articula. La revisión humana es la red de seguridad.
