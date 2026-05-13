---
type: research
id: borrador-skill-architect-capability-viability-review
title: "Borrador de skill: architect.capability-viability-review"
status: draft
created: 2026-04-30
author: pelayo
tags: [skill-borrador, architect, capability, viability, happy-path]
---

# Borrador de skill: architect.capability-viability-review

> **Estado: borrador.** Materialización en `.claude/skills/architect/capability-viability-review/SKILL.md` durante materialización.

## Propósito

Evaluar la **viabilidad técnica** de una capability candidata: qué quality attributes implica, qué tactics arquitectónicas se requieren, si introduce tradeoffs problemáticos entre QAs, si es coherente con la arquitectura existente del proyecto.

Esta skill se invoca **durante inception**, después de que el PO (lado estratégico) derive una capability con `capability-derivation` y la valide con `capability-quality-check`. El Architect aporta el lente técnico antes de que la capability se cierre.

## Cuándo se invoca

- **Trigger principal:** durante `inception-orchestration` paso 4, cuando una capability candidata declara `dimensions-affected` que incluye `technical` (la mayoría lo hace).
- **Trigger secundario:** capability nueva añadida post-inception que toca dimensión técnica.
- **Trigger asistencial:** revisión de capability existente cuyo coste o complejidad técnica se ha reevaluado.

## Inputs

- Capability candidata (frontmatter + descripción + justificación).
- Visión y goals ascendentes (para QAs implícitos del proyecto).
- ADRs existentes en `vault/architect/adrs/` — la capability NO puede contradecirlos sin disparar `coherence-evaluation`.
- Capabilities hermanas — la nueva no debe imponer QAs incompatibles con las existentes.
- Library: [[library-bass-software-architecture]], [[library-ford-evolutionary-architecture]], [[library-martin-clean-architecture]].

## Proceso — 5 pasos

### Paso 1 — Identificar Quality Attributes implícitos
Para la capability propuesta, identificar qué QAs (Bass et al.) se implican:
- ¿Modifiability? (¿el sistema seguirá siendo modificable después?)
- ¿Performance? (¿impacto en latencia / throughput?)
- ¿Security? (¿abre superficie de ataque?)
- ¿Testability? (¿es testeable end-to-end?)
- ¿Deployability? (¿complica el deploy?)
- ¿Integrability? (¿facilita integración con sistemas externos?)

Listar los 2-3 QAs más afectados (positiva o negativamente).

### Paso 2 — Identificar tactics requeridas
Para cada QA dominante, identificar las **tactics arquitectónicas** que la capability requiere o sugiere. Bass et al. Cap. 4-13 tienen catálogos de tactics por QA.

Ejemplo: si la capability requiere alta modifiability → tactics como "encapsulation", "use intermediary", "maintain semantic coherence".

### Paso 3 — Detectar tradeoffs entre QAs
Algunos QAs están en tensión entre sí. Ejemplos:
- More security ↔ less performance.
- More flexibility ↔ less simplicity.
- More features ↔ more cognitive load (Ousterhout).

Si la capability mejora un QA a costa de degradar otro de forma significativa → marcar como tradeoff crítico para discusión con humano.

### Paso 4 — Verificar coherencia con ADRs y arquitectura existente
- ¿Hay ADR que la capability contradice? Si sí → activar `coherence-evaluation`.
- ¿Encaja con las "capas" existentes (Martin)? Si introduce dependencia entre capas no permitida → red flag.
- ¿Información leakage potencial entre módulos (Ousterhout)? Si la capability requiere que múltiples módulos sepan el mismo detalle → red flag.

### Paso 5 — Evaluar fitness functions necesarias
¿Qué fitness function (Ford et al.) protegería la propiedad arquitectónica que esta capability introduce? Si no se puede formular fitness function clara, la capability puede ser **deriva no detectable** — marcar.

## Output format

Para cada paso: hallazgos + diagnóstico.

**Recomendación final** entre cuatro:

1. **Aprobar — viable y coherente.** La capability puede formalizarse. (Opcional: sugerir ADR para documentar tactics elegidas.)
2. **Aprobar con condiciones.** Viable pero requiere ADR explícito documentando los tradeoffs aceptados, o requiere fitness function nueva, o requiere modificar capability hermana.
3. **Reformular.** El concepto es válido pero la formulación introduce conflicto técnico. Volver al PO con sugerencias.
4. **Rechazar.** No viable con la arquitectura actual. Requiere cambio mayor de la arquitectura o de la visión.

## Fundamento bibliográfico

- [[library-bass-software-architecture]] — QAs, ASRs, ADD.
- [[library-ford-evolutionary-architecture]] — fitness functions, appropriate coupling.
- [[library-martin-clean-architecture]] — Dependency Rule, capas.
- [[library-ousterhout-philosophy-software-design]] — modules, information hiding (para detectar leakage potencial).

## Ejemplo aplicado

**Capability:** "Memoria compartida humano-agentes en grafo declarativo" (CAP-2 si la inception próxima la mantiene).

| Paso | Hallazgo |
|---|---|
| 1. QAs | Modifiability (alta — vault es markdown editable), Testability (alta — vault-cli valida), Performance (variable — lectura de muchos archivos), Integrability (alta — formato estándar). |
| 2. Tactics | Encapsulation (frontmatter como contrato), Maintain semantic coherence (schemas), Reduce computational overhead (lectura focalizada por dimensiones). |
| 3. Tradeoffs | Modifiability ↑ vs. Performance ↓ en proyectos grandes (lectura de cientos de archivos). Tradeoff aceptable hasta cierto tamaño; escalado vía índice SQLite (sec. 23 boceto inicial) si crece. |
| 4. Coherencia | Coherente con ADR (futuro) sobre "single source of truth en markdown". Sin contradicciones detectadas. |
| 5. Fitness functions | `vault validate`, `vault check`, `vault check coverage` cubren modifiability + testability. |

**Recomendación:** Aprobar con condición — escribir ADR explícito sobre el tradeoff modifiability/performance y la estrategia de migración a índice SQLite cuando aplique.

## Limitaciones

- Identificar QAs es subjetivo. Diferentes Architects pueden ver QAs distintos en la misma capability — no hay canónica.
- Tradeoffs entre QAs no siempre son cuantificables. La skill requiere que el humano confirme la severidad.
- Para proyectos en bootstrapping sin arquitectura establecida, "coherencia con arquitectura existente" es delgada — la skill se vuelve más predictiva (¿esta capability sienta precedente coherente?).
