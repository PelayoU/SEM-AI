---
type: research
id: library-martin-clean-architecture
title: "Robert C. Martin — Clean Architecture"
status: draft
created: 2026-04-30
author: pelayo
tags: [library, clean-architecture, dependency-rule, solid, architect]
applicable-roles: [architect, developer]
---

# Robert C. Martin — Clean Architecture

## Datos bibliográficos

- **Autor:** Robert C. Martin ("Uncle Bob").
- **Obra:** *"Clean Architecture: A Craftsman's Guide to Software Structure and Design"* (Prentice Hall, 2017).
- **Blog post original que la introduce:** "The Clean Architecture" (Cleancoder, 2012).
- **URL:** https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html
- **Aplicabilidad SEM-IA:** dimensión `technical` — Architect al definir boundaries del sistema, al revisar dependencias.

## Tesis central

> *"The architecture of a software system is the shape given to that system by those who build it. The form of that shape is in the division of that system into components, the arrangement of those components, and the ways in which those components communicate with each other."*

La arquitectura existe para **hacer el sistema fácil de cambiar**. Una "buena" arquitectura es la que minimiza el coste de cambio en cada fase del ciclo de vida.

## La Regla de Dependencia (The Dependency Rule)

**El principio fundamental** de Clean Architecture:

> *"Source code dependencies can only point inwards. Nothing in an inner circle can know anything at all about something in an outer circle."*

Capas concéntricas. Las flechas de dependencia siempre apuntan hacia el centro. Lo central depende de NADA externo; lo externo depende de lo central.

Capas (del centro hacia afuera):
1. **Entities** — reglas de negocio core, independientes de aplicaciones específicas.
2. **Use Cases** — reglas de negocio específicas de la aplicación.
3. **Interface Adapters** — controladores, presenters, gateways.
4. **Frameworks & Drivers** — UI, DB, web, dispositivos.

### Implicación de la Regla

Las **decisiones tardías son baratas**. Si las dependencias apuntan hacia adentro:
- Cambiar la base de datos (capa externa) es local y barato.
- Cambiar el web framework (capa externa) es local y barato.
- Cambiar la UI (capa externa) es local y barato.

Las **decisiones tempranas son las críticas** (entities, use cases). Esas casi nunca cambian.

## Dependency Inversion Principle (DIP) — el pilar

> *"High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions."*

DIP es la herramienta operativa de la Regla de Dependencia. Cuando una clase de alto nivel necesita usar una de bajo nivel, el flujo control va hacia el bajo nivel pero la **dependencia de código** va a una **abstracción** que ambos implementan.

Resultado: el código de alto nivel no conoce el bajo nivel directamente — solo conoce la abstracción.

## SOLID Principles (recapitulados en Clean Architecture)

| Principio | Nombre completo | Esencia |
|---|---|---|
| **S** | Single Responsibility | Una clase tiene una y solo una razón para cambiar. |
| **O** | Open / Closed | Abierto a extensión, cerrado a modificación. |
| **L** | Liskov Substitution | Subtipos deben ser sustituibles por sus tipos base. |
| **I** | Interface Segregation | Mejor muchas interfaces específicas que una grande. |
| **D** | Dependency Inversion | Depender de abstracciones, no de concreciones. |

> *"If the SOLID principles tell us how to arrange the bricks into walls and rooms, then the component principles tell us how to arrange the rooms into buildings."*

## Component Principles

Para componentes (módulos cohesivos):

- **REP — Reuse/Release Equivalence Principle:** la unidad de release es la unidad de reuse.
- **CCP — Common Closure Principle:** clases que cambian juntas, juntas.
- **CRP — Common Reuse Principle:** clases que se usan juntas, juntas.

Para acoplamiento entre componentes:

- **ADP — Acyclic Dependencies:** sin ciclos de dependencia entre componentes.
- **SDP — Stable Dependencies:** depender de cosas más estables que tú.
- **SAP — Stable Abstractions:** los componentes estables deben ser abstractos.

## Screaming Architecture

> *"Your architecture should scream the intent of your system."*

Cuando alguien abre el repo, debería ver **el dominio del sistema**, no su framework.

- ✅ Carpetas: `payroll/`, `employees/`, `tax/` — esto es payroll.
- ❌ Carpetas: `controllers/`, `models/`, `views/` — esto podría ser cualquier app web.

## Aplicabilidad a SEM-IA

**Skill `architect.coupling-detection`:** la Regla de Dependencia y los principios SOLID son los lentes principales para detectar acoplamientos problemáticos.

Aplicable a:
- Una feature que importa código de capa más externa que ella → violación de la Regla.
- Un módulo de alto nivel que depende directamente de implementación → violación de DIP.
- Una clase que cambia por múltiples razones → violación de SRP.

**Skill `architect.feature-viability-review`:** evaluar si la feature respeta boundaries arquitectónicas. Si introduce acoplamiento entre capas, marcar.

**Skill `architect.coherence-evaluation`:** los ADRs aceptados pueden incluir Regla de Dependencia explícita ("la capa X no depende de la capa Y"). Cualquier cambio que viola eso requiere arbitraje.

## Citas que anclan decisiones

> *"The Dependency Rule: Source code dependencies can only point inwards."*

Aplicable a `coupling-detection` directamente.

> *"Your architecture should scream the intent of your system."*

Aplicable a la organización del repo y de los agentes / skills / commands. Marcar como red flag cuando algo "huele a framework genérico" en lugar de "huele a SEM-IA".

> *"Both [high and low level] should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions."*

Aplicable al diseño de skills compartidas (`graph-cross-link-declaration`): la skill es la abstracción; los nodos concretos del grafo son los detalles que dependen de ella.

## Limitaciones

- Clean Architecture es opinionada — algunos critican que produce overengineering en proyectos pequeños.
- "Capas concéntricas" puede ser difícil de mapear en sistemas que no son aplicaciones tradicionales (ej. SEM-IA, que es framework de coordinación).
- SOLID se aplica a OOP. Para programación funcional o sistemas declarativos hay traducción necesaria.
- Algunas críticas modernas (DDD strategic patterns, hexagonal architecture) son refinamientos sobre las mismas ideas — Martin reconoce esto en el libro.
