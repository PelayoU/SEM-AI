---
type: research
id: library-adzic-specification-by-example
title: "Gojko Adzic — Specification by Example (BDD)"
status: draft
created: 2026-04-30
author: pelayo
tags: [library, bdd, specifications, gherkin, product-owner]
applicable-roles: [product-owner, qa]
---

# Gojko Adzic — Specification by Example (BDD)

## Datos bibliográficos

- **Autor:** Gojko Adzic
- **Obras principales:**
  - *"Specification by Example: How Successful Teams Deliver the Right Software"* (Manning, 2011)
  - *"Bridging the Communication Gap: Specification by Example and Agile Acceptance Testing"* (2009)
- **Aplicabilidad SEM-IA:** dimensión `product` y `quality` — Product Owner al escribir specs en Gherkin; QA al verificar coverage de AC.

## Tesis central

> *"Specification by Example is a collaborative method for specifying requirements and tests... a set of process patterns that facilitate change in software products to ensure that the right product is delivered efficiently."*

Objetivo declarado:
> *"To specify, develop, and deliver the right software, without defects, in very short cycles."*

## Los 7 patrones

Adzic organiza Specification by Example en 7 patrones de proceso:

1. **Deriving scope from goals** — los specs nacen de objetivos de negocio, no de soluciones predefinidas.
2. **Specifying collaboratively** — el equipo (PO + dev + QA + UX) crea specs juntos en workshops.
3. **Illustrating using examples** — los ejemplos concretos reemplazan abstracciones ambiguas.
4. **Refining the specification** — los ejemplos se filtran y formalizan en AC.
5. **Automating validation without changing specs** — los AC se ejecutan como tests sin reescribir el spec.
6. **Validating frequently** — la validación es continua, no batch al final.
7. **Evolving a documentation system** — los specs vivos son la documentación canónica del producto.

## Beneficios documentados

> *"It produces living, reliable documentation; it defines expectations clearly and makes validation efficient; it reduces rework; and, above all, it assures delivery teams and business stakeholders that the software that's built is right for its purpose."*

## Discovery → Specification

Adzic recomienda este flujo:

1. **Business users propose key examples** — los stakeholders empiezan poniendo ejemplos importantes.
2. **Developers and testers comment** — añaden condiciones, casos límite, casos no cubiertos.
3. **Workshop builds shared understanding** — la conversación produce comprensión compartida.
4. **Examples filtered to AC** — solo los críticos se formalizan; otros se descartan con justificación.
5. **AC become spec in Gherkin** — Given-When-Then formal.
6. **Spec becomes test** — automatización referencia los AC.

## Living Documentation

> *"Use examples as a source of truth about the system, as documentation to support product evolution, for onboarding new team members and for evaluating proposed changes."*

El documento se mantiene vivo porque:
- Los ejemplos son AC formales.
- Los AC son tests automatizados.
- Los tests fallan si el sistema diverge del spec.
- Por tanto, spec ↔ comportamiento real están sincronizados estructuralmente.

## Aplicabilidad a SEM-IA

**Crítica para el flujo del Product Owner**, alineado directamente con el modelo SEM-IA descrito en el boceto inicial sección 8 ("De la story a los artifacts").

Citas del boceto inicial alineadas:

> *"Para cada story, el equipo (PO + dev + QA + designer) tiene una conversación de discovery donde explora examples..."*

> *"El PO filtra los examples. Los críticos se formalizan como acceptance criteria, los demás se descartan con justificación."*

**Corrección bibliográfica importante**: En Adzic literal y BDD/Cucumber canónico, un archivo `.feature` Gherkin (con su bloque `Feature:`) corresponde a **una funcionalidad/feature cohesiva** — NO a una user story individual. Una `Feature:` Gherkin típicamente **agrupa los Scenarios (AC) de varias stories relacionadas** que cubren juntas una unidad de comportamiento entregable. Esto se debe a que en BDD el nivel "story" es organizacional (Cohn), mientras que Gherkin organiza por funcionalidad observable (Adzic).

Por tanto:
- **1 archivo `.feature` Gherkin = 1 feature en sentido Cohn/Patton/Adzic** (funcionalidad cohesiva entregable).
- **N Scenarios dentro = N AC de N stories** que pertenecen a esa feature.
- Cada Scenario se identifica con el AC + opcionalmente con la story de origen para trazabilidad (ej. `Scenario: AC-A1 — Story X: <título del AC>`).

Esto difiere de la convención previamente declarada en versiones tempranas de esta nota ("una story = una spec"), que era **interpretación SEM-IA estricta** no canónica Adzic.

**Skill `product-owner.discovery-facilitation`:** estructura del workshop de Adzic.

**Skill `product-owner.example-elicitation`:** las técnicas para provocar examples (qué pasa si X, y si Y, y sin conexión...).

**Skill `product-owner.acceptance-criteria-definition`:** filtrar examples a AC formales.

**Skill `product-owner.spec-writing`:** escribir el archivo Gherkin con frontmatter SEM-IA.

**Skill (compartida con QA): coverage validation** — cada AC debe tener al menos un test asociado vía `@ac-coverage:`.

## Formato Gherkin canónico (Adzic literal)

```gherkin
Feature: feature-007-crear-receta — Crear receta con título y atributos

  Como usuario que documenta una receta
  Quiero crear receta con sus atributos básicos (título, ingredientes, pasos)
  Para identificar y consultar mis recetas

  Background:
    Given la app está abierta
    And me encuentro en "Nueva receta"

  # Scenarios de story-007-A: validación del título
  Scenario: AC-A1 — Título obligatorio (story-007-A)
    Given el campo título está vacío
    When pulso "Guardar"
    Then aparece el mensaje "El título es obligatorio"
    And la receta no se guarda

  Scenario: AC-A2 — Título con longitud máxima (story-007-A)
    Given el campo título excede 100 caracteres
    When pulso "Guardar"
    Then aparece el mensaje "Título demasiado largo"

  # Scenarios de story-007-B: validación de ingredientes
  Scenario: AC-B1 — Al menos un ingrediente (story-007-B)
    Given el campo ingredientes está vacío
    When pulso "Guardar"
    Then aparece el mensaje "Añade al menos un ingrediente"
```

Características:
- **Feature:** id de la **feature SEM-IA** (no de la story). Agrupa AC de todas las stories de esa feature.
- **Background:** contexto común a TODOS los Scenarios (todas las stories de la feature).
- **Scenarios agrupados por story origen** dentro del archivo con comentarios separadores `# Scenarios de story-NNN-X`.
- **Scenario:** uno por AC. Numeración (AC-A1, AC-A2, AC-B1, etc.) — el prefijo letra (A, B, C, D) corresponde a la story de origen, lo cual preserva trazabilidad story↔AC.
- **Given/When/Then:** stricto. No mezclar lenguaje narrativo en Gherkin.

**Trazabilidad story↔Scenario**: el comentario `(story-NNN-X)` al final de cada `Scenario:` permite ubicar de qué story proviene cada AC sin necesidad de archivos `.feature` separados por story.

## Sin Cucumber obligatorio

SEM-IA (sec. 23 boceto inicial + Adzic mismo) **no requiere Cucumber** como runtime ejecutable. Los AC en Gherkin son **contrato legible**; los tests se escriben en el runner nativo del lenguaje (Vitest, pytest, Foundry) y referencian el AC con `// @ac-coverage: AC-A1, AC-A2`. El vault-cli verifica que cada AC tiene un test que lo cubre.

## Citas que anclan decisiones

> *"Examples are bridges that connect business and technical perspectives."* — espíritu de SbE

Aplicable a `discovery-facilitation`: los examples son el formato común al que humanos (negocio/PO) y agentes (dev/QA) pueden llegar.

> *"The biggest mistake is to specify too much upfront."* — Adzic

Aplicable a `acceptance-criteria-definition`: filtrar examples implica descartar muchos. No todo lo discutido se formaliza.

## Limitaciones del framework

- Adzic asume equipo humano colaborativo. En SEM-IA, parte del workshop la facilitan agentes — adaptación necesaria.
- Specs en Gherkin son verbosos. Para features pequeñas, puede ser overhead.

## Convención canónica SEM-IA (post-corrección 2026-05-13)

Tras detectar inconsistencia bibliográfica entre versiones tempranas de esta nota y Adzic literal, la convención canónica SEM-IA es:

- **1 archivo `.md`/`.feature` por feature SEM-IA** (no por story).
- El bloque `Feature:` Gherkin nombra la feature SEM-IA (ej. `Feature: feature-019-slash-verify — ...`).
- Los `Scenarios` dentro agrupan AC de **todas las stories** de la feature, con comentarios separadores `# Scenarios de story-NNN-X` para trazabilidad.
- Cada Scenario lleva su identificador AC único (`AC-A1, AC-A2, AC-B1, ...`) donde la letra corresponde a la story origen.

Esto es **fiel Adzic literal** y reduce verbosidad (1 spec por feature en vez de 1 por story).
