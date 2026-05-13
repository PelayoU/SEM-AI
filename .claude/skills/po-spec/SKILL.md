---
name: po-spec
description: "Producir spec Gherkin por feature siguiendo Specification by Example de Gojko Adzic: agregar AC de todas las stories de la feature en un único archivo, formato Feature/Scenario, AC numerados (AC-A1, AC-A2, AC-B1...) con prefijo de letra correspondiente a la story origen para trazabilidad bidireccional con tests (@ac-coverage). Use this skill when a feature has all stories ready and needs its formal contract Gherkin, or when an existing spec is outdated."
when_to_use: "El humano tiene una feature con stories ready y quiere materializar el contrato Gherkin formal, o quiere refinar una spec existente."
---

# po-spec

## Propósito

Producir el **contrato formal Gherkin** de una feature: un archivo `.md` con bloque Feature/Scenarios numerados, agregando los AC de todas las stories de esa feature. Es el documento que los tests cubren con `@ac-coverage`.

## Bibliografía aplicada

- `bibliography/adzic-specification-by-example.md` — Gojko Adzic, *Specification by Example*. Examples → AC → Living documentation. Un único contrato auditable por feature.

## Principios Adzic

1. **Examples elicit understanding.** Antes de escribir AC abstracto, capturas ejemplos concretos (ya hechos en `po-feature` por story).
2. **Single source of truth.** Un único documento por feature con todos los AC. No diseminado en N archivos.
3. **Living documentation.** El spec es el contrato vigente. Cuando cambia la feature, cambia el spec.
4. **Test-traceable.** Cada AC numerado y citable desde código de test: `@ac-coverage: AC-A1, AC-A2`.

## Estructura del nodo `spec`

```yaml
---
category: spec
id: spec-NNN-<slug>   # mismo NNN que la feature padre
parent: feature-NNN-<slug>
status: draft  # draft | active
created: <ISO date>
updated: <ISO date>
also-relates-to: []
dimensions-affected: []
---

# Spec NNN — <Título de la feature>

## Stories cubiertas
- `[[story-NNN-A-<slug>]]` — AC-A1, AC-A2, AC-A3
- `[[story-NNN-B-<slug>]]` — AC-B1, AC-B2
- `[[story-NNN-C-<slug>]]` — AC-C1, AC-C2, AC-C3

## Spec Gherkin

```gherkin
Feature: <Título de la feature en lenguaje natural>
  As <role>
  I want <action>
  So that <benefit>

  # Story A — <título story>
  Scenario: AC-A1 — <título corto del AC>
    Given <contexto>
    When <acción>
    Then <outcome esperado>

  Scenario: AC-A2 — <título corto>
    Given ...
    When ...
    Then ...

  # Story B — <título story>
  Scenario: AC-B1 — <título corto>
    Given ...
    When ...
    Then ...

  # ... continúa con todos los AC numerados con prefijo de letra de story
```

## Notas
<Decisiones tomadas durante la escritura del spec, edge cases discutidos, AC descartados con razón.>
```

## Cómo procedes

1. **Carga el contexto.** Lees `nodes/<feature>.md` y todas las stories hijas (`nodes/story-NNN-*.md`).
2. **Extrae los examples** de cada story (sección "Examples" del story).
3. **Convierte cada example en AC Gherkin.** Numeras con prefijo de letra de story: AC-A1 viene de la primera example de story A, AC-B1 de story B, etc.
4. **Agregas todos los Scenarios** en un único bloque Gherkin dentro del spec.
5. **Verificas cobertura**: cada story debe contribuir al menos un AC. Si una story no tiene AC derivable de sus examples, está incompleta — vuelves a `po-feature`.
6. **Propones el archivo** al humano: path + contenido.

## Output esperado

Propuesta al humano:
- Path del nodo: `nodes/spec-NNN-<slug>.md`.
- `parent: feature-NNN-<slug>` declarado.
- Bloque Gherkin completo con todos los AC numerados.
- Lista de cobertura: qué story alimenta qué AC.
- Cross-links: la spec se enlaza con la feature padre y, vía wikilinks, con las stories cubiertas.

Aplicas `shared-cross-link` para cross-links adicionales (depends-on de specs hermanas, related-adrs si hay ADRs aplicables).

## Trampas a evitar

- **AC implementation-centric**: *"El backend devuelve 200"* — habla de implementación. ✅ *"El usuario ve el producto en su carrito"*.
- **AC sin Given**: AC que asume contexto implícito. Cada Scenario debe ser standalone (Adzic single-source).
- **AC duplicados entre stories**: si dos stories llevan al mismo AC, hay drift en la descomposición de feature. Vuelve a `po-feature`.
- **Spec sin trazabilidad letras**: AC-1, AC-2, AC-3 sin prefijo de story → rompe trazabilidad bidireccional. Siempre AC-{letra}{número}.
- **Gherkin verbose**: Given/When/Then de 10 líneas. Gherkin es contrato, no documentación literaria. Concreto y corto.

## Después de aplicar la skill

Registra en documento-sesión:
```markdown
- Creado `nodes/spec-NNN-<slug>.md` aplicando `po-spec`. Cita: Adzic Specification by Example. Cobertura: N AC derivados de M stories.
```

Y actualizas el `status:` de la feature padre a `ready-for-implementation` si todas las stories están ready y el spec está active.
