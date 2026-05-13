---
name: po-spec
description: "Producir el spec Gherkin de una feature: contrato formal con Scenarios (AC) numerados con prefijo de letra de la story origen (AC-A1, AC-A2, AC-B1...) para trazabilidad bidireccional con tests vía @ac-coverage. Sigue la convención Gherkin oficial de Cucumber + Specification by Example (Adzic) tal como aparece en GISF. Use this skill when a feature has all stories ready and needs its formal contract Gherkin, or when an existing spec is outdated."
when_to_use: "El humano tiene una feature con stories ready y quiere materializar el contrato Gherkin formal, o quiere refinar una spec existente."
---

# po-spec

## Propósito

Producir el **contrato formal Gherkin** de una feature: un archivo `.md` con bloque Feature + Scenarios numerados que agregan los AC de todas las stories de esa feature. Documento que los tests cubren con `@ac-coverage`.

## Estructura del nodo

Estructura del archivo en `_obsidian/templates/spec.md`. Léelo antes de crear o editar.

## Definición de Examples y AC (canónica SEM-IA literal)

> *"Examples: What is needed to build up an understanding of the features/stories, concrete examples of what the system should do in different situations. These examples can form the basis for the Acceptance criteria of a feature. Examples illustrate how a feature works."*

Flujo:

```
Examples (situaciones concretas) → Acceptance Criteria (formalizados) → Gherkin Scenarios (testeables)
```

## Specification by Example

Estructura canónica que GISF presenta:

```
Feature: <descripción de la feature>
In order to <business value>
As a <user role>
I want to <action>

Scenario: <título del AC>
  Given <precondición>
  And <precondición adicional>
  When <acción>
  Then <outcome esperado>
  And <outcome adicional>
```

## Gherkin: keywords canónicos (Cucumber official)

**Primary keywords**:

- **Feature**: high-level description de la feature, agrupa scenarios relacionados. Primer keyword obligatorio.
- **Rule** (Gherkin v6+): representa una business rule. Agrupa scenarios que pertenecen a esa regla.
- **Example / Scenario** (sinónimos): ejemplo concreto que ilustra business rule. **Recomendado 3-5 steps por scenario**.
- **Given**: contexto inicial — algo que pasó en el pasado.
- **When**: evento o acción — persona interactuando con sistema o evento triggered.
- **Then**: outcome esperado — assertion comparando actual vs expected. **Debe ser observable**.
- **And, But**: encadenar Given/When/Then.
- **`*` (asterisco)**: en lugar de keyword normal, para steps que son list-of-things.
- **Background**: Given steps repetidos en todos los scenarios de una Feature. Run before EACH scenario.
- **Scenario Outline / Scenario Template**: run mismo scenario múltiples veces con `<>`-delimited parameters.
- **Examples / Scenarios**: tabla de filas que parametrizan el Scenario Outline.

**Secondary keywords**:

- **`"""`** (Doc Strings): pasar texto largo a un step. Optionally annotate content type.
- **`|`** (Data Tables): pasar lista de valores. Pipe-delimited. Escape: `\n`, `\|`, `\\`.
- **`@`** (Tags): agrupar features independiente de file/directory structure.
- **`#`** (Comments): solo al inicio de línea. NO block comments.

**Otros**:

- **Indentación**: 2 espacios recomendado.
- **Spoken Languages**: `# language: <code>` en primera línea para usar otro idioma (default English).

## Tips Gherkin (canónicos)

- **Then debe describir outcome observable** — algo que sale del sistema (UI, mensaje, archivo). NO algo dentro de la BD.
- **Background corto**: máximo 4 líneas. Si es más largo, mover detalles a higher-level steps.
- **Background vivid**: nombres con personalidad, contar historia.
- **Scenarios cortos**: 3-5 steps. Más → pierde poder expresivo como specification.

## Convención SEM-IA: trazabilidad story ↔ AC

Para cada story bajo una feature, los AC se numeran con prefijo de letra de la story:

- `story-NNN-A-<slug>` → AC-A1, AC-A2, AC-A3...
- `story-NNN-B-<slug>` → AC-B1, AC-B2...
- `story-NNN-C-<slug>` → AC-C1...

Los tests referencian con `// @ac-coverage: AC-A1, AC-A2`. Trazabilidad bidireccional: dado un AC, puedo encontrar la story y los tests; dado un test, sé qué AC cubre.

## Cómo procedes

1. **Carga el contexto.** Lees `nodes/<feature>.md` y todas las stories hijas (`nodes/story-NNN-*.md`).
2. **Extrae los examples** de cada story (sección "Examples" del template).
3. **Convierte cada example en Scenario Gherkin** numerando con prefijo de letra de la story origen: AC-A1 viene del primer example de story A, AC-B1 del primer example de story B, etc.
4. **Construye el bloque Gherkin**:
   - Un único `Feature:` para toda la feature.
   - Opcional: `Background:` con preconditions comunes a todos los scenarios.
   - Scenarios agrupados con comentarios separadores `# Scenarios de story-NNN-X`.
   - Cada `Scenario:` lleva su identificador `AC-XN` + nombre + comentario `(story-NNN-X)` para trazabilidad inline.
5. **Verifica cobertura**: cada story contribuye al menos un AC. Si una story no produce AC, está incompleta — vuelves a `po-feature` para refinarla.
6. **Propones al humano** path + contenido leyendo `_obsidian/templates/spec.md` como base.

Aplicas `shared-cross-link` para cross-links adicionales (depends-on de specs hermanas, related-adrs si aplican).

Tras consenso humano, actualizas el `status:` de la feature padre a `ready-for-implementation`.

## Trampas a evitar

- **Then no observable**: *"El backend devuelve 200"* — internal, no observable por usuario. ✅ *"El usuario ve confirmación del pago en pantalla"*.
- **AC sin Given**: cada Scenario debe ser standalone, no asumir contexto implícito.
- **AC duplicados entre stories**: indica drift en descomposición de feature → vuelve a `po-feature`.
- **Spec sin trazabilidad de letras**: AC-1, AC-2 sin prefijo → rompe trazabilidad story↔Scenario.
- **Gherkin verbose**: el spec es contrato, no narrative literario. Mantén Given/When/Then concretos y cortos.
- **Más de 5 steps por scenario** (Cucumber recommendation): pierde poder expresivo como specification.
- **Background largo** (>4 líneas): mueve detalles a higher-level steps.

## Después de aplicar

Registra en documento-sesión:

```markdown
- Creado `nodes/spec-NNN-<slug>.md` aplicando `po-spec`. Cita: Specification by Example + Gherkin canónico (Cucumber). Cobertura: N AC derivados de M stories.
```
