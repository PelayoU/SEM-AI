---
type: capability
id: cap-01-grafo-declarativo-persistente
title: "Grafo declarativo persistente del proyecto"

# Espina dorsal jerárquica
parent: goal-2-output-auditable-multirol

# Cross-links (Cagan principio: nodes are not isolated)
also-relates-to:
  - goal-7-ciclo-vida-producto
  - goal-1-auto-sostenibilidad
  - goal-4-rigor-multirol-individual
depends-on: []
dimensions-affected: [product, technical]
related-adrs: []  # vacío hoy. Latentes aflorables en step-3 del WA: ADR-latente-002 (vault role-first), ADR-latente-003 (frontmatter+wiki-links), ADR-latente-004 (estados canónicos), ADR-latente-008 (backlog-como-query)

# Lifecycle del nodo
status: active  # transición aplicada por /verify del WA wa-2026-05-12-002 el 2026-05-12T05:30+02:00

# Madurez operativa del producto (campo improvisado declarado en gap 2 del anexo WA-002)
operational-status: operant

# Bibliografía base
fundamento-bibliografico:
  - Bass — Software Architecture in Practice (QAs + tactics + tradeoffs)
  - Ford et al. — Building Evolutionary Architectures (fitness functions, architectural drift detection)
  - Nygard — ADRs (cross-links explícitos)
  - Cagan — Inspired (memoria persistente del producto como ventaja estratégica)

# Quality attributes Bass implicados
qas-bass:
  - modifiability    # añadir nodos sin romper otros; cross-links declarativos
  - auditability     # cada decisión trazable a sus parents y cross-links
  - analyzability    # query estructural posible (backlog emerge como query, no estructura nueva)
  - portability      # vault role-first es portable; frontmatter es agnóstico de herramienta

# Tactics arquitectónicos (Bass)
tactics:
  - "Information hiding: frontmatter (estructura) separado de contenido del nodo"
  - "Use an intermediary: cross-links declarativos (parent/also-relates-to/depends-on/dimensions-affected/related-adrs), no implícitos en código"
  - "Maintain semantic coherence: convención frontmatter uniforme por tipo de nodo declarada inline en la skill que lo crea"
  - "Standard data formats: YAML + Markdown + wiki-links [[id]] — todo legible sin tooling especial"

# Tradeoffs conscientes
tradeoffs:
  - "Estructura declarativa requiere disciplina del autor — sin validación automatizada hoy (pendiente: skill `sem-ia check` de CAP-H planned)"
  - "Cross-links manuales pueden quedar obsoletos al renombrar/borrar nodos sin tool detection"
  - "Query del backlog es O(N) sobre archivos del vault: aceptable hasta cientos de nodos, degrada con miles (Ford fitness function a vigilar)"
  - "Grafo emergente desde frontmatter es más flexible que schema rígido pero menos contractual — adopters podrían querer schema JSON formal en el futuro (CAP-H universal/ contempla schemas)"

# JTBD outcome (Christensen — formulación del job real del usuario)
jtbd-outcome:
  quien: "Humano operador del proyecto (autor + colaboradores futuros + evaluadores externos + adopters del framework)"
  job: "Recordar y trazar el contexto completo de un proyecto a lo largo de meses o años sin perder coherencia entre decisiones tomadas en momentos distintos"
  outcome-esperado: "Cualquier decisión, artefacto o cambio es trazable a sus parents y cross-links sin depender de la memoria del autor; el grafo es la memoria viva del proyecto"
---

# CAP-01 · Grafo declarativo persistente del proyecto

## Enunciado

El sistema mantiene todo el contexto del proyecto (visión, goals, capabilities, features, stories, specs, ADRs, audits, learnings, sessions) como **grafo dirigido versionado en git**, con espina dorsal jerárquica `vision → goals → capabilities → features → stories → specs` y cross-links explícitos (`parent`, `also-relates-to`, `depends-on`, `dimensions-affected`, `related-adrs`) declarados en frontmatter YAML de cada nodo, más wiki-links `[[id]]` en contenido para referencias internas.

## Por qué es capability fuerte (4 criterios)

1. **Habilidad diferenciada del sistema**: el grafo declarativo es propiedad observable e infraestructura sobre la que todo lo demás opera. Sin él, no hay memoria persistente del proyecto entre sesiones.
2. **Sirve a goals con métrica clara**: goal-2 declara *"100 % de nodos del grafo con cross-links coherentes"* — métrica directa de CAP-A. También goal-7 (estados canónicos cubren ciclo de vida completo).
3. **Cohesión interna**: las 7 piezas que la materializan (vault role-first, frontmatter, wiki-links, dimensions, estados canónicos, skill graph-cross-link-declaration, governance del modelo) comparten el job común *"persistir y relacionar nodos del proyecto"*.
4. **No es trivialmente subcapability de otra**: el grafo no es feature de CAP-C (WAs) ni de CAP-B (multi-rol). Es la **infraestructura de contexto** sobre la que ambas operan. CAP-C consume el grafo (WAs viven en él), CAP-B opera sobre él (cada rol custodia parte del grafo).

## Piezas del bootstrap que la materializan

| Pieza | Path | Rol en la capability |
|---|---|---|
| Vault role-first (8 directorios + shared) | `vault/` | Organización física del grafo por custodio |
| Modelo conceptual del repo | `vault/shared/governance/repo-structure.md` | Declara la estructura y separación `.claude/` vs `vault/` vs `src/` |
| Catálogo de 7 dimensiones + custodios | `vault/shared/governance/dimensions.md` | Dimensiones referenciables desde frontmatter (`dimensions-affected`) |
| Frontmatter YAML obligatorio en todo nodo | declarado en `CLAUDE.md` raíz | Mecanismo declarativo de aristas + metadata |
| Wiki-links `[[id]]` en contenido | convención del proyecto | Referencias internas legibles para humano y máquina |
| Estados canónicos del nodo + transiciones | declarado en `CLAUDE.md` raíz y `workflows.md` | Lifecycle observable (`draft → ready-for-implementation → in-implementation → implemented + superseded + deprecated`) |
| Skill compartida `graph-cross-link-declaration` | `.claude/skills/shared/graph-cross-link-declaration/SKILL.md` | Operación de declarar/actualizar aristas |

## Relación con goals

- **Goal-2 (output auditable, coherente y verificado multi-rol)** — parent primario. Métrica directa: *"100 % de nodos con cross-links coherentes"*. El grafo es la condición de auditabilidad.
- **Goal-7 (ciclo de vida producto completo)** — los estados canónicos del nodo cubren el lifecycle desde `draft` hasta `deprecated`/`superseded`, citado literalmente como métrica de cumplimiento de goal-7.
- **Goal-1 (auto-sostenibilidad)** — el grafo ES la memoria persistente que permite a SEM-IA operar bajo sus propios protocolos. Sin él, dogfooding sería imposible.
- **Goal-4 (rigor multi-rol con humano individual)** — el grafo permite al humano alternar entre roles sin perder coherencia (cross-links son la pista navegable).

## Criterio observable para futuros `/verify`

Una feature descompuesta de CAP-A es verificable si cumple:
- Cada nodo nuevo en el vault tiene frontmatter YAML válido y parseable.
- Cross-links declarados (parent + also-relates-to + depends-on + related-adrs) apuntan a nodos existentes (no rotos).
- Estados del nodo respetan las transiciones canónicas (no se salta de `draft` a `implemented` sin pasar por `ready-for-implementation` en el caso de specs).
- Wiki-links `[[id]]` en contenido referencian IDs reales del vault.

## Features candidatas (preview — decomposition completa en WA `feature-design` posterior)

No es decomposition formal (no se aplica `feature-decomposition` aquí). Solo preview de los bloques naturales:

1. **Estructura inline del frontmatter por tipo de nodo** — definir frontmatter canónico para vision, goal, capability, feature, story, spec, ADR, audit, learning, session, etc. Pendiente para varios tipos (gap 2 del WA-002 lo expone).
2. **Validación de cross-links del grafo** — mecanismo que detecta cross-links rotos al añadir/renombrar/borrar nodos. Pendiente (parte de CAP-H feature `sem-ia check`).
3. **Convención wiki-links + parser** — formato `[[id]]`, alias permitidos, parser opcional para tooling futuro.
4. **Estados canónicos + transiciones validables** — algoritmo del lifecycle declarado y verificable. Hoy declarado en docs, no enforced.
5. **Vault role-first como organización física + governance docs como ground truth** — convención de estructura y su contrato con adopters extensibles.

## Notas / gaps operativos conocidos

- Validación automatizada de cross-links pendiente (parte de CAP-H feature `sem-ia check`). Hoy se confía en la disciplina del autor.
- Estructura inline del frontmatter NO está definida en la skill que crea cada tipo de nodo en varios casos (gap 2 del anexo del WA-002). `capability-derivation` no define el frontmatter de capability; al escribir este capability file el PO improvisó la estructura (declarado en gap 2). Pendiente: formalizar inline.
- Performance del backlog-como-query degrada con miles de nodos. Aceptable a escala actual; vigilar como fitness function (Ford).
