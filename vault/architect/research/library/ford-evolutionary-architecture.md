---
type: research
id: library-ford-evolutionary-architecture
title: "Ford, Parsons, Kua — Building Evolutionary Architectures"
status: draft
created: 2026-04-30
author: pelayo
tags: [library, evolutionary-architecture, fitness-functions, conways-law, architect]
applicable-roles: [architect]
---

# Ford, Parsons, Kua — Building Evolutionary Architectures

## Datos bibliográficos

- **Autores:** Neal Ford, Rebecca Parsons, Patrick Kua (con Pramod Sadalage).
- **Obra:** *"Building Evolutionary Architectures: Support Constant Change"* (O'Reilly, 1ª ed. 2017; 2ª ed. 2022 con subtítulo *"Automated Software Governance"*).
- **Recursos:** https://nealford.com/books/buildingevolutionaryarchitectures.html
- **Aplicabilidad SEM-IA:** dimensión `technical` — Architect al diseñar arquitectura que evoluciona, al definir métricas de salud arquitectónica, al considerar Conway's Law en la organización del equipo y agentes.

## Tesis central

> *"Building an evolutionary architecture consists of three primary concerns: fitness functions, incremental change, and appropriate coupling."*

La arquitectura debe ser **diseñada para cambiar** sostenidamente. No "perfecta de partida e inmutable" sino "sólida y modificable continuamente".

Tres pilares:

1. **Fitness functions** — métricas que protegen las características arquitectónicas a lo largo del tiempo.
2. **Incremental change** — capacidad de modificar pieza a pieza sin big bang.
3. **Appropriate coupling** — el acoplamiento correcto para los objetivos del sistema.

## Concepto: Architectural Fitness Functions

> *"An architectural fitness function provides an objective integrity assessment of some architectural characteristic(s), employing a wide variety of implementation mechanisms including tests, metrics, monitoring, logging, and so on, to protect one or more architectural dimensions."*

Una fitness function es una **prueba ejecutable** (en sentido amplio) que verifica que el sistema mantiene una propiedad arquitectónica objetivo. Ejemplos:

- **Test:** test unitario que verifica que una capa no importa de otra capa prohibida.
- **Métrica:** linter que mide ciclomatic complexity y falla si supera umbral.
- **Monitoring:** alarma en producción si latencia P95 supera SLA.
- **Logging:** auditoría que detecta llamadas a APIs deprecadas.

### Categorías de fitness functions

- **Atomic vs. holistic** — afectan a un componente vs. al sistema entero.
- **Triggered vs. continuous** — ejecutan en CI vs. corren siempre en producción.
- **Static vs. dynamic** — analizan código vs. comportamiento en runtime.
- **Automated vs. manual** — la mayoría automatizadas; algunas (ej. UX review) manuales.

Ford et al. recomiendan **automatizar tantas fitness functions como sea posible** y ejecutarlas en CI.

## Conway's Law

> *"Organizations design systems that mirror their own communication structure."* — Melvyn Conway, 1968.

Ford et al. dedican atención significativa a Conway. Implicación: la **estructura del equipo** condiciona la arquitectura emergente. Si tres equipos construyen un sistema, terminará siendo tres componentes.

**Inverse Conway Maneuver:** diseña el equipo según la arquitectura que quieres. No la arquitectura según el equipo que tienes.

## Tipos de cambio arquitectónico

- **Foreseeable** — anticipado, planeado.
- **Unforeseeable** — emerge del uso real.
- **Disruptive** — cambia el game (nuevas tecnologías, nuevos modelos de negocio).

La arquitectura evolutiva está diseñada para los TRES tipos, especialmente el unforeseeable.

## Coupling — appropriate, not minimal

Una idea importante de Ford et al.: **el acoplamiento no es malo per se**. Lo que importa es el acoplamiento APROPIADO.

- Servicios que comparten un dominio de negocio están **bien acoplados**.
- Servicios que no deberían conocerse pero se acoplan son **mal acoplados**.

Las fitness functions ayudan a vigilar el acoplamiento — detectar acoplamientos no deseados y permitir los deseados.

## Aplicabilidad a SEM-IA

**Skill `architect.coupling-detection`:** las fitness functions sobre acoplamiento son aplicables al código del propio framework. Ejemplos para SEM-IA:

- *Fitness function:* "Ningún archivo de plantilla puede importar de archivos de schema". (Conceptualmente — los lados deben ser independientes.)
- *Fitness function:* "Cada `parent` declarado en frontmatter apunta a nodo existente". Esto YA es lo que `vault check` ejecuta en CI.
- *Fitness function:* "Cada AC tiene un test que lo cubre". Esto YA es `vault check coverage`.

El framework SEM-IA YA TIENE fitness functions implícitas (vault validate, vault check, vault check coverage) — lo que falta es **declararlas explícitamente como fitness functions arquitectónicas** en un ADR.

**Skill `architect.feature-viability-review`:** Conway's Law aplicable — si una feature requiere coordinación entre múltiples roles SEM-IA, ¿la organización (catálogo de roles) la soporta?

**Skill `architect.adr-writing`:** una categoría de ADRs típica son las fitness functions adoptadas. Cada fitness function debería tener su ADR documentando **por qué** se adopta y **qué propiedad protege**.

## Citas que anclan decisiones

> *"Building an evolutionary architecture consists of three primary concerns: fitness functions, incremental change, and appropriate coupling."*

Tres preguntas para cualquier capability con implicaciones arquitectónicas:
1. ¿Qué fitness function la protege?
2. ¿Permite cambio incremental?
3. ¿El acoplamiento que introduce es apropiado?

> *"Conway's Law: Organizations design systems that mirror their own communication structure."*

Aplicable a `feature-viability-review`: si una feature cruza varios roles, considerar si la coordinación está soportada por el catálogo.

## Limitaciones

- "Fitness functions" como concepto es abstracto. Los ejemplos concretos son útiles pero no exhaustivos. Cada proyecto tiene que descubrir sus propias.
- Ford et al. asumen sistemas grandes con CI/CD maduro. SEM-IA en bootstrap tiene CI mínimo (vault-cli pendiente).
- "Inverse Conway Maneuver" es ideal — en proyectos reales (especialmente pequeños) no siempre se puede rediseñar la organización.
