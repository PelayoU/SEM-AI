---
type: research
id: library-bass-software-architecture
title: "Bass, Clements, Kazman — Software Architecture in Practice"
status: draft
created: 2026-04-30
author: pelayo
tags: [library, architecture, asr, add, quality-attributes, architect]
applicable-roles: [architect]
---

# Bass, Clements, Kazman — Software Architecture in Practice

## Datos bibliográficos

- **Autores:** Len Bass, Paul Clements, Rick Kazman (Software Engineering Institute, Carnegie Mellon University).
- **Obra:** *"Software Architecture in Practice"*. SEI Series in Software Engineering. Addison-Wesley.
  - 1ª ed. 1998
  - 2ª ed. 2003
  - 3ª ed. 2012
  - **4ª ed. 2021** (más reciente)
- **Aplicabilidad SEM-IA:** dimensión `technical` — Architect al evaluar viabilidad de capabilities y features con implicaciones técnicas, al definir quality attributes del proyecto.

## Tesis central

> *"Architecture is the set of structures needed to reason about the system, comprising software elements, relations among them, and properties of both."*

La arquitectura emerge de las **decisiones tempranas** sobre estructura, no de las decisiones detalladas de implementación. Es **lo más caro de cambiar después**.

## Conceptos clave aplicables al Architect

### Architecturally Significant Requirements (ASRs)

Capítulo 19 (4ª ed.). Los ASRs son los requisitos que **afectan la arquitectura** — los que, si los ignoras al diseñar, te obligan a re-arquitecturar después.

Métodos para identificar ASRs:
- **Gathering ASRs from requirements documents** — extraer de documentos existentes.
- **Interviewing stakeholders** — preguntas dirigidas a quien tiene contexto.
- **Understanding business goals** — los goals del negocio constriñen la arquitectura.
- **Capturing ASRs in a utility tree** — estructura jerárquica que mapea ASRs a quality attributes.

### Attribute-Driven Design (ADD)

Capítulo 20 (4ª ed.). Método sistemático de diseño arquitectónico que parte de los **quality attributes** (no de las features funcionales).

Pasos generales:
1. Recolectar inputs (ASRs, restricciones, contexto).
2. Establecer iteration goal (qué se diseña en esta iteración).
3. Elegir uno o varios elementos del sistema a refinar.
4. Elegir design concepts (patrones, tactics, frameworks).
5. Producir structures (descomposición en elementos).
6. Crear documentación inicial (vistas, ADRs).
7. Performar análisis del diseño actual (ATAM, etc.).

ADD itera estos pasos hasta que la arquitectura es suficientemente detallada para asignar trabajo a equipos de implementación.

### Quality Attributes (QAs)

Las **propiedades emergentes** del sistema que la arquitectura habilita o impide. La 4ª ed. cubre:

- **Availability** — disponibilidad / tolerancia a fallos.
- **Deployability** — facilidad de desplegar.
- **Energy efficiency** — consumo energético.
- **Integrability** — capacidad de integrar componentes externos.
- **Modifiability** — coste de cambio.
- **Performance** — latencia, throughput.
- **Safety** — comportamiento seguro ante fallos.
- **Security** — protección contra amenazas.
- **Testability** — facilidad de probar.
- **Usability** — facilidad de usar.

Cada QA tiene **tactics** asociadas — patrones arquitectónicos para alcanzarla.

### Architecture as Decisions

> *"Architecture is the set of decisions about the system that, if changed, would force you to throw away significant amounts of work."*

Los Architectural Decisions (ADs) son lo que las ADRs documentan. La arquitectura **es** el conjunto de decisiones tomadas, no un diagrama.

## Métodos de evaluación arquitectónica

Bass, Clements y Kazman introdujeron varios métodos de evaluación que llevan acrónimos del SEI:

- **SAAM** (Software Architecture Analysis Method) — primer método (1995). Análisis basado en escenarios.
- **ATAM** (Architecture Tradeoff Analysis Method) — extensión de SAAM. Identifica tradeoffs entre QAs.
- **CBAM** (Cost Benefit Analysis Method) — combina QAs con coste.

ATAM es el más usado. Estructura:
1. Presentar ATAM.
2. Presentar drivers de negocio.
3. Presentar arquitectura.
4. Identificar architectural approaches.
5. Generar utility tree.
6. Analizar architectural approaches.
7. Brainstorming + priorización de scenarios.
8. Re-analizar.

## Aplicabilidad a SEM-IA

**Skill `architect.capability-viability-review`:** los conceptos de ASR y QA aplican directamente — al revisar una capability, identificar:
- ¿Qué quality attributes implica?
- ¿Qué tactics arquitectónicas se requieren?
- ¿Hay tradeoffs entre QAs (ej. más security ↔ menos performance)?

**Skill `architect.feature-viability-review`:** mismo razonamiento al nivel de feature — pero más concreto. La feature implica decisiones a nivel de modulación, datos, etc.

**Skill `architect.coherence-evaluation`:** los ADRs ya aceptados constriñen lo que es coherente. Cualquier propuesta nueva se evalúa contra ese conjunto.

## Citas que anclan decisiones

> *"Quality attributes are qualifications of functional requirements or of the overall product, such as how fast a function must be."*

Aplicable a `feature-viability-review`: para cada feature, preguntar qué QAs aplican. Si nadie lo identifica, falta análisis.

> *"You don't get qualities by accident. You get them by deliberate design."*

Aplicable a `capability-viability-review`: si una capability tiene QAs implícitos (ej. "memoria compartida" implica modifiability + testability), el Architect debe explicitarlos.

## Limitaciones

- El libro está orientado a sistemas industriales grandes. Para proyectos pequeños, ATAM completo es overhead. Aplicar simplificado.
- 4ª ed. es muy reciente (2021); algunos QAs (energy efficiency) son nuevos. Versiones anteriores tienen variaciones.
- No cubre arquitecturas de IA específicamente — para SEM-IA hay que adaptar QAs a la realidad de agentes y prompts.
