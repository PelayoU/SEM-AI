---
type: research
id: borrador-skill-po-feature-decomposition
title: "Borrador de skill: product-owner.feature-decomposition"
status: draft
created: 2026-04-30
author: pelayo
tags: [skill-borrador, product-owner, feature, decomposition, happy-path]
---

# Borrador de skill: product-owner.feature-decomposition

> **Estado: borrador.** Materialización en `.claude/skills/product-owner/feature-decomposition/SKILL.md` durante Fase 5.

## Propósito

Descomponer una capability aprobada en un conjunto de features entregables, y cada feature en stories. Aplica lentes de **User Story Mapping (Patton)** para mapear narrative flow y priorizar thin slices end-to-end, e **INVEST (Cohn)** para validar las stories resultantes.

## Cuándo se invoca

- **Trigger principal:** una capability del subgrafo estratégico está aprobada y entra en fase de descomposición operativa (post-inception).
- **Trigger secundario:** una feature existente resulta demasiado grande durante implementación y necesita desglose.

## Inputs

- Capability padre con frontmatter completo (parent goal, descripción, justificación).
- Goal y visión ascendentes (para alineación top-down).
- Catálogo de roles del proyecto (para identificar qué tipos de usuario aparecen en las stories).
- Library: [[library-patton-user-story-mapping]], [[library-cohn-user-stories-invest]], [[library-christensen-jtbd]].

## Proceso

### Paso 1 — Identificar el outcome de usuario que la capability habilita
Reformular la capability en lenguaje JTBD: *"Cuando [situación], el [usuario] quiere [progreso], so I can [resultado]"*. Esta es la frase ancla.

### Paso 2 — Mapear el narrative flow (Patton)
Identificar las **actividades del usuario** que la capability cubre, en orden temporal de uso. Estas forman la **espina dorsal** del story map. Típicamente 3-7 actividades.

Forma:

```
Actividad 1 → Actividad 2 → Actividad 3 → Actividad 4
```

### Paso 3 — Por cada actividad, identificar features candidatas
Una **feature** materializa una pieza concreta de funcionalidad dentro de una actividad. Generar 1-3 features por actividad. Cada feature debe tener:
- Título tentativo
- Outcome de usuario que entrega
- Dimensiones afectadas tentativas
- Conexión con la capability padre

### Paso 4 — Identificar stories por feature
Por cada feature, descomponer en **stories** (formato Cohn: *"Como X, quiero Y para Z"*). Aplicar criterios INVEST a cada story:
- **Independent** — puede construirse independientemente
- **Negotiable** — no es contrato cerrado
- **Valuable** — entrega valor a un stakeholder
- **Estimable** — el equipo puede estimar tamaño
- **Small** — cabe en un Working Agreement de implementación
- **Testable** — se pueden formular AC en Gherkin

Si una story falla INVEST, refactorizar (descomponer si grande, fundir si dependiente, especificar si vaga).

### Paso 5 — Slicing por release (Patton)
Identificar el **thin slice end-to-end** que constituye Release 1: stories mínimas de cada actividad que juntas entregan valor de usuario completo. Marcar features / stories como pertenecientes a Release 1, 2, etc.

Antipatrón a evitar: completar una actividad al 100% antes de tocar las demás. Slicing horizontal de Patton es lo correcto.

### Paso 6 — Identificar dependencias
Aplicar `graph-cross-link-declaration` (skill compartida) sobre cada feature: identificar `depends-on`, `also-relates-to`, `related-adrs`, `dimensions-affected`.

### Paso 7 — Quality-check final
Cada story candidata pasa por `feature-quality-check` (que aplica INVEST + cobertura de AC) antes de formalizarse como nodo del vault.

## Outputs

- Estructura de descomposición:
  ```
  Capability X
  ├── Feature 1 (Release 1)
  │   ├── Story 1.1
  │   ├── Story 1.2
  │   └── Story 1.3
  ├── Feature 2 (Release 1)
  │   └── Story 2.1
  └── Feature 3 (Release 2)
      └── Story 3.1
  ```
- Por cada feature: archivo `vault/product-owner/specs/feature-N.md` con frontmatter completo y referencias.
- Por cada story: spec en Gherkin (vía `spec-writing`).
- Lista de cross-links a declarar.
- Slicing de releases documentado.

## Fundamento bibliográfico

- [[library-patton-user-story-mapping]] — narrative flow + thin slices + outcomes > features.
- [[library-cohn-user-stories-invest]] — formato story + criterios INVEST.
- [[library-christensen-jtbd]] — articulación de outcomes en lenguaje JTBD.

## Ejemplo aplicado a una capability futura de SEM-IA

> **`[FUTURE]` — Este ejemplo describe la decomposición de una capability hipotética del propio framework SEM-IA, no funcionalidad operativa hoy.** Las features F2.1, F2.2, etc. ilustran *cómo se descompondría* una capability "custodios homólogos" si SEM-IA fuera el proyecto adopter. NO son features de SEM-IA implementadas. En particular, *"Recepción identifica dimensiones del nodo"* y *"Recepción invoca subagent del custodio"* describen automatizaciones planeadas (recepción haciendo trabajo derivado), pero en el modelo enterprise actual recepción es PM puro y NO ejecuta — esas features serían post-inception del propio SEM-IA.

**Capability:** `cap-1-custodios-homologos`

**Outcome JTBD:** *"Cuando un proyecto adopta SEM-IA, el equipo quiere que cada dimensión del producto holístico tenga su agente custodio, so I can absorber estructuralmente el coste de revisión multiplicada al trabajar con IA."*

**Narrative flow (actividades):**
1. Configurar catálogo de roles del proyecto
2. Invocar custodio según dimensión
3. Recibir review del custodio
4. Coordinar múltiples custodios

**Features por actividad (selección):**

Actividad 1 (Configurar catálogo):
- F1.1: "Catálogo de roles core distribuido con SEM-IA" (Release 1)
- F1.2: "Mecanismo de extensión por proyecto" (Release 1)
- F1.3: "Validación de catálogo en CI" (Release 2)

Actividad 2 (Invocar custodio):
- F2.1: "Recepción identifica dimensiones del nodo" (Release 1)
- F2.2: "Recepción invoca subagent del custodio" (Release 1)

(... etc.)

**Stories de F1.1 (catálogo de roles core):**
- "Como humano que adopta SEM-IA, quiero que el framework venga con 7 roles core ya definidos, para que pueda empezar sin tener que crear roles desde cero" → INVEST ✅
- "Como humano que mantiene un proyecto SEM-IA, quiero que `vault/shared/governance/role-catalog.md` declare los roles activos, para que la coordinación sea predecible" → INVEST ✅

## Limitaciones

- Patton orientado a productos consumer / B2B con flujo de usuario claro. Para capabilities muy técnicas (ej: "memoria compartida en grafo declarativo"), el "narrative flow" puede ser artificial — adaptar a "flujo del developer interactuando con la capability".
- Slicing por release puede ser difícil si la capability requiere mínimo crítico grande. Ser honesto: si Release 1 no puede ser thin, marcarlo y aceptar que el primer slice es grande.
