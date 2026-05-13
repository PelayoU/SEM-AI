---
type: research
id: borrador-skill-po-spec-writing
title: "Borrador de skill: product-owner.spec-writing"
status: draft
created: 2026-04-30
author: pelayo
tags: [skill-borrador, product-owner, spec, gherkin, happy-path]
dimensions-affected: [product]
---

# Borrador de skill: product-owner.spec-writing

> **Estado: borrador.** Materialización en `.claude/skills/product-owner/spec-writing/SKILL.md` durante Fase 5.

## Propósito

Escribir la spec de una story en formato **Gherkin** (Given-When-Then), con frontmatter SEM-IA completo, AC formalizados como Scenarios, y cada AC trazable a un test futuro vía comentario `@ac-coverage`. La spec es contrato ejecutable de comportamiento (Adzic — Specification by Example).

## Cuándo se invoca

- **Trigger principal:** una story está aprobada (post-decomposition + INVEST OK + discovery completado) y necesita su contrato formal.
- **Trigger secundario:** revisión de una spec existente que ha quedado desactualizada.

## Inputs

- La story formalizada (formato Cohn): *"Como X, quiero Y para Z"*.
- Outputs de `discovery-facilitation` y `example-elicitation` (skills later) — la conversación de discovery con sus examples generados.
- Outputs de `acceptance-criteria-definition` — los examples filtrados a AC formales.
- Estructura del nodo definida en `./SKILL.md` (sección "Estructura del nodo").
- ADRs aplicables (referenciados como cross-links).
- Library: [[library-adzic-specification-by-example]], [[library-cohn-user-stories-invest]].

## Proceso

### Paso 1 — Lectura del contexto
Leer la story padre, la feature padre, la capability ascendente, y los ADRs relevantes para no contradecir decisiones técnicas existentes.

### Paso 2 — Frontmatter
Construir frontmatter de la spec siguiendo `node-base` + reglas específicas de spec:
```yaml
---
type: spec
id: spec-NNN-X
title: "Título descriptivo"
parent: feature-NNN              # espina dorsal jerárquica
also-relates-to: []              # cross-links
depends-on: []
related-adrs: []
dimensions-affected: [product, ux, technical, ...]
status: draft
created: YYYY-MM-DD
author: product-owner
---
```

### Paso 3 — Header narrativo
Escribir el bloque de identidad del feature en formato Gherkin:
```gherkin
Feature: STORY-NNN-X — Título descriptivo
  Como [tipo de usuario]
  Quiero [acción / capacidad]
  Para [beneficio que conecta con la capability]
```

### Paso 4 — Background
Si hay contexto común a todos los scenarios (estado inicial de la app, datos precondicionados, etc.), articularlo como `Background:`. Mantener corto — todo lo que no es estrictamente común va en el Given del Scenario.

### Paso 5 — Scenarios
Un **Scenario por cada AC** identificado en `acceptance-criteria-definition`. Cada Scenario:
- Identificador del AC en el título: `Scenario: AC-NX — descripción corta`
- `Given` — precondiciones
- `When` — acción que dispara el comportamiento
- `Then` — resultado esperado
- Opcional `And` para encadenar precondiciones / consecuencias

Forma estricta — no mezclar narrativa libre dentro de los pasos.

### Paso 6 — Validación
Antes de cerrar la spec, autoverificar:
- Cada AC de la story tiene exactamente un Scenario.
- Ningún Scenario refiere a estado fuera del Background o de su propio Given.
- Los identificadores `AC-NX` son consistentes.
- El frontmatter declara `dimensions-affected` con todas las dimensiones que la story toca.

### Paso 7 — Anotación para tests (cobertura)
La spec no se convierte en tests directamente (SEM-IA no usa Cucumber como runtime ejecutable). Pero la spec **debe ser referenciable** por tests futuros vía:
```typescript
// tests/<file>.test.ts
// @sem-ia: spec-NNN-X
// @ac-coverage: AC-N1, AC-N2
```

`vault check coverage` (vault-cli) verificará que cada AC declarado tiene al menos un test que lo cubre.

## Outputs

- Archivo `vault/product-owner/specs/<spec-name>.feature` (extensión `.feature` por convención Gherkin) o `vault/product-owner/specs/<spec-name>.md` con bloque Gherkin embebido — decidir convención y mantenerla consistente.
- Frontmatter SEM-IA completo y validable contra schema.
- Scenarios numerados con AC ids trazables.

## Fundamento bibliográfico

- [[library-adzic-specification-by-example]] — Specification by Example, los 7 patrones, formato Gherkin canónico, living documentation.
- [[library-cohn-user-stories-invest]] — formato de la story padre que la spec materializa.

## Ejemplo

**Story:** *"Como humano arrancando inception, quiero que el PO evalúe cada goal candidato con `goal-quality-check`, para que las decisiones estratégicas no descansen en intuición improvisada."*

**Spec resultante** (extracto):

```gherkin
---
type: spec
id: spec-001-A
title: "PO evalúa goal candidato con goal-quality-check"
parent: feature-001
related-adrs: []
dimensions-affected: [product]
status: draft
created: 2026-05-15
author: product-owner
---

Feature: STORY-001-A — PO evalúa goal con goal-quality-check
  Como humano arrancando inception
  Quiero que el PO evalúe cada goal candidato
  Para que las decisiones estratégicas tengan auditoría bibliográfica

  Background:
    Given la inception está en paso 3 (definición de goals)
    And el PO ha cargado la skill goal-quality-check

  Scenario: AC-A1 — Goal con métricas claras pasa los 6 tests
    Given un goal candidato con resultado medible y conexión con la visión
    When el PO invoca goal-quality-check sobre el goal
    Then el output reporta los 6 tests con veredicto pass
    And la recomendación final es "Mantener tal cual"

  Scenario: AC-A2 — Goal sin métrica falla Test 2
    Given un goal candidato que carece de métrica explícita
    When el PO invoca goal-quality-check sobre el goal
    Then el output marca Test 2 como ❌ fail
    And la recomendación incluye "añadir métricas o reformular"
```

## Limitaciones

- Gherkin es verboso. Para scopes muy pequeños (un AC trivial), el overhead es alto. La regla SEM-IA "una story = una spec" es por defecto, no absoluta — agrupar stories pequeñas en una sola spec si el equipo lo ve útil.
- La spec describe comportamiento esperado, no implementación. Si emerge implementación al escribir, refactorizar para mantener la spec como "what" no "how".
