---
type: report
id: sistema-gaps-2026-05-12-verifiability-review
title: "Verificabilidad-review consolidado de las 10 mejoras al sistema (WA wa-2026-05-12-003)"
status: active   # transición aplicada por /verify del WA wa-2026-05-12-003 el 2026-05-12T09:05+02:00
created: 2026-05-12
author: qa
related-wa: wa-2026-05-12-003
references:
  - CLAUDE.md
  - vault/shared/governance/workflows.md
  - .claude/agents/product-owner.md
  - .claude/skills/product-owner/strategy/capability-derivation/SKILL.md
bibliography:
  - Adzic — Specification by Example (AC trazables, verificabilidad observable)
  - Cohn — User Stories Applied (INVEST testability, I = independent)
  - Bass — Software Architecture in Practice (testability como QA del sistema mismo)
  - Ford et al. — Building Evolutionary Architectures (fitness functions como mecanismo de detección de regresión)
  - Nygard — Documenting Architecture Decisions (registro auditable de decisiones de proceso)
---

# Verificabilidad-review de las 10 mejoras al sistema

## Contexto

El WA `wa-2026-05-12-003` procesó 10 gaps estructurales detectados durante WA-001 y WA-002 (y durante la escritura del propio WA-003). Los gaps son defectos del framework mismo — templates incompletos, protocolos faltantes, comportamiento no auto-correctivo del agente PO. Los 4 archivos del bootstrap tocados son:

- `CLAUDE.md` (raíz): Gaps 1, 7, 8, 9, 10 + ajuste tabla outcome-types (F-ARCH-1).
- `vault/shared/governance/workflows.md`: Gaps 1 (cross-file), 3, 4 + F-ARCH-2, F-ARCH-3.
- `.claude/agents/product-owner.md`: Gaps 2-PO, 4-PO, 5, 6, 7-PO, 8-PO, 9-PO, 10-PO (+ ajuste coherence step-3).
- `.claude/skills/product-owner/strategy/capability-derivation/SKILL.md`: Gap 2.

Este report evalúa: (a) si cada mejora está aplicada en su path correspondiente, (b) si un futuro WA puede auditar la aplicación correcta de la mejora, y (c) si hay mecanismo de detección de regresión.

---

## Veredicto global

**APRUEBA** — las 10 mejoras están aplicadas. Todos los gaps tienen test de verificación definible. Hay flags menores (ninguno bloqueante) agrupados en la sección final.

---

## Verificabilidad por Gap

### Gap 1 — Estado `aborted` para WA + campos pivot

**Aplicado en**:
- `CLAUDE.md` raíz: tabla "Estados canónicos del nodo" — filas `aborted` y `aborted-reference` presentes con definición completa + párrafo explicativo semántico. Sección "Working Agreement (WA) — estructura": frontmatter extendido con `status: active | aborted`, campo `modality` por step, `status` de step extendido `pending | in-progress | done | aborted`, campos opcionales `aborted-at` / `partial-output` en step, bloque opcional al final con `aborted-at`, `aborted-reason`, `supersedes`, `superseded-by`, `supersede-reason`. Verificado por lectura directa.
- `vault/shared/governance/workflows.md`: tabla de estados al final (sección "Backlog — emergente, no estructural") — filas `aborted` y `aborted-reference` consistentes con CLAUDE.md raíz. Párrafo semántico idéntico en esencia. Verificado.

**Verificación posible**:
- `grep -n "aborted" CLAUDE.md` → espera filas `aborted` y `aborted-reference` en tabla de estados + campos `aborted-at` / `aborted-reason` / `supersedes` en la sección estructura del WA.
- `grep -n "aborted" vault/shared/governance/workflows.md` → espera las mismas dos filas en la tabla del Backlog.
- Consistencia cross-file: comparar wording entre ambas tablas — deben coincidir en esencia (tolerancia: pequeñas diferencias de redacción entre versiones, no de semántica).

**Detección de regresión**:
- Si alguien edita los estados canónicos de CLAUDE.md raíz sin replicar en workflows.md → divergencia entre las dos tablas. Test: `grep -c "aborted-reference" CLAUDE.md` debe ser >= 2 (tabla + párrafo); `grep -c "aborted-reference" vault/shared/governance/workflows.md` debe ser >= 2.
- Si alguien elimina los campos opcionales del frontmatter del WA en CLAUDE.md raíz → WAs reales que usan `aborted-at` quedan sin esquema de referencia. Test: `grep -n "aborted-at" CLAUDE.md` debe aparecer en la sección estructura del WA.

**Veredicto**: aprueba.

---

### Gap 2 — Template del capability file en SKILL.md

**Aplicado en**:
- `.claude/skills/product-owner/strategy/capability-derivation/SKILL.md`: sección nueva `## Template del capability file` presente. Subsecciones verificadas por lectura directa: "Frontmatter — campos esenciales" (type, id, title, parent, also-relates-to, depends-on, dimensions-affected, related-adrs, status), "Frontmatter — profundidad bibliográfica" (operational-status, qas-bass, tactics, tradeoffs, fitness-functions opcional, jtbd-outcome, fundamento-bibliografico), "Cuerpo del archivo — secciones esenciales" (6 secciones en orden), "Cuerpo del archivo — secciones opcionales" (3 secciones opcionales), "Reglas de aplicación" (5 reglas). Filosofía del template ("mínimo con extensiones opcionales") declarada. Fitness functions Ford marcadas como OPCIONAL pero recomendado.

**Verificación posible**:
- `grep -n "## Template del capability file" .claude/skills/product-owner/strategy/capability-derivation/SKILL.md` → debe existir.
- `grep -n "operational-status\|qas-bass\|jtbd-outcome\|fitness-functions" .claude/skills/product-owner/strategy/capability-derivation/SKILL.md` → los 4 campos de profundidad bibliográfica deben estar.
- Contar secciones esenciales del cuerpo: `grep -n "## Enunciado\|## Por qué\|## Piezas\|## Relación con goals\|## Criterio observable" .claude/skills/product-owner/strategy/capability-derivation/SKILL.md` → espera >= 5 líneas.

**Detección de regresión**:
- Un futuro edit que elimine `## Template del capability file` o sus subsecciones → PO vuelve a improvisar frontmatter (Gap 2 regresa). Test rápido: contar líneas del SKILL.md; el template añadió ~90 líneas (hoy > 140 líneas en total; si cae por debajo de 100 → flag).
- Si `operational-status` desaparece del template → capabilities nuevas podrían omitir el campo. Grep como check.

**Veredicto**: aprueba.

---

### Gap 3 — Template `capability-creation` con flag `mode`

**Aplicado en**:
- `vault/shared/governance/workflows.md`: template `capability-creation` — descripción extendida ("Soporta tres modos"), bloque `mode-flag` con `field: mode`, `values: [single, batch, reverse-engineering]`, `default: single`, `rationale`. `default-steps` ampliados con bifurcación de `purpose` y `expected-output` por modo en cada step. Step-6 nuevo (QA verificabilidad, `condition: mode == batch o mode == reverse-engineering`, `optional: true`). `on-close` bifurcado por modo. Verificado.

**Verificación posible**:
- `grep -n "mode-flag\|mode: single\|batch\|reverse-engineering" vault/shared/governance/workflows.md` → espera sección `mode-flag` + 3 values.
- Contar steps en `capability-creation`: `grep -n "id: step-" vault/shared/governance/workflows.md` debe incluir step-6 con `condition: mode == batch`.
- `grep -n "on-close" vault/shared/governance/workflows.md` → `on-close` del template `capability-creation` debe tener entradas con `mode:` bifurcado.

**Detección de regresión**:
- Si el `mode-flag` se elimina y el template vuelve a `single` implícito → los modos batch/reverse-engineering quedan sin soporte formal. Test: `grep -c "mode-flag" vault/shared/governance/workflows.md` debe ser >= 1.
- Si step-6 (QA en batch) se elimina → WAs de tipo batch pierden el step de verificabilidad. Test: `grep -n "mode == batch" vault/shared/governance/workflows.md` debe existir.

**Veredicto**: aprueba.

---

### Gap 4 — Protocolo de pivot de un WA mid-flight

**Aplicado en**:
- `vault/shared/governance/workflows.md`: sección nueva `## Protocolo de pivot de un WA mid-flight`. Estructura completa verificada: "Cuándo aplica", "Cómo detectarlo (4 señales)", "Los 7 pasos canónicos del pivot" (numerados 1-7), "Anti-patrón a evitar", "Cuándo NO procede pivot", "Fundamento bibliográfico".
- `.claude/agents/product-owner.md`: Modo 2 "Conduce el step" — `#### Checkpoint Gap 4 — Detección de pivot mid-flight` presente. Las 4 señales alineadas **literalmente** con las de workflows.md (ajuste correctivo aplicado en step-3). La cita coloquial preservada como ilustración. Referencia explícita a workflows.md como ground truth. Los 7 pasos canónicos reproducidos inline para operar sin abrir otro archivo (con declaración explícita de que el ground truth es workflows.md).

**Verificación posible**:
- `grep -n "## Protocolo de pivot" vault/shared/governance/workflows.md` → debe existir.
- `grep -n "7 pasos canónicos\|Checkpoint Gap 4" .claude/agents/product-owner.md` → ambas líneas deben estar.
- Coherencia 4 señales: `grep -A 6 "Cómo detectarlo" vault/shared/governance/workflows.md` debe producir las mismas 4 señales que `grep -A 8 "Checkpoint Gap 4" .claude/agents/product-owner.md`.

**Detección de regresión**:
- Si las 4 señales en el agent file PO divergen de las de workflows.md → incoherencia que el Architect correctivo de step-3 ya resolvió una vez. Test: revisar manualmente las 4 señales en ambos archivos al hacer cualquier edit a workflows.md.
- Si el paso 7 del protocolo (handoff verbal) desaparece → pivots se ejecutan sin cierre explícito al humano. Test: `grep -n "Handoff verbal" vault/shared/governance/workflows.md` debe aparecer en la sección de pivot.

**Veredicto**: aprueba.

**Nota**: el ajuste correctivo de step-3 (alineación de las 4 señales) es él mismo un caso de test exitoso — el mecanismo de coherence review detectó y corrigió divergencia antes del cierre del WA. Buena señal para la robustez del protocolo.

---

### Gap 5 — Checkpoint anti-improvisación en el agente PO

**Aplicado en**:
- `.claude/agents/product-owner.md`: Modo 2 "Conduce el step" — `#### Checkpoint Gap 5 — Anti-improvisación (declarar campos no documentados en el momento)` presente. Frase canónica verificada: *"Voy a introducir el campo / sección / estructura X porque [razón]. NO está documentado en el sistema. ¿Lo formalizamos al cerrar el WA?"*. Extensión Gap 7 integrada en el mismo checkpoint (caso WA referenciador).

**Verificación posible**:
- `grep -n "Checkpoint Gap 5" .claude/agents/product-owner.md` → debe existir.
- `grep -n "NO está documentado en el sistema" .claude/agents/product-owner.md` → frase canónica must exist.
- `grep -n "caso WA referenciador" .claude/agents/product-owner.md` → extensión Gap 7 debe estar en el mismo checkpoint o inmediatamente después.

**Detección de regresión**:
- Este checkpoint es comportamental — no hay forma de testear automáticamente que el PO lo sigue. La detección de regresión es: si en un futuro WA el PO introduce campos no documentados sin declararlos → el humano lo detecta retroactivamente (mismo patrón que Gap 2 en WA-002). Mitigación: el checkpoint existe como texto declarativo; si el agente lo lee antes de cada step, el comportamiento correcto se activa.
- Test indirecto: en WAs futuros, si el Progreso de un step PO no menciona NINGUNA improvisación declarada, podría indicar que el checkpoint funciona correctamente o que el PO lo salteó. No distinguible desde fuera. Flag aparcado (framework regression detection diferido a WA futuro).

**Veredicto**: aprueba. Cobertura del test de verificabilidad es parcial (comportamental), pero la mejora está correctamente aplicada en el texto del agent file.

---

### Gap 6 — Filtro PO en consolidación de scope-scan

**Aplicado en**:
- `.claude/agents/product-owner.md`: Modo 1 — `### Paso 6b — Filtro PO (CRÍTICO — no saltar)` presente entre paso 6 y paso 7. Las 4 categorías declaradas: (1) acepto y aplico yo, (2) descarto con razón, (3) difiero a WA futuro, (4) requiere decisión humana real. Bibliografía Cagan incluida. Anti-patrón ("PO contaminado") nombrado.
- `.claude/agents/product-owner.md`: Modo 2 "Al completar tu step" — punto 4 con Filtro PO y las 4 categorías replicado (+ opción "Pivotar" si señales del protocolo de pivot aplican).

**Verificación posible**:
- `grep -n "Paso 6b — Filtro PO\|Filtro PO" .claude/agents/product-owner.md` → espera >= 2 ocurrencias (Modo 1 + Modo 2).
- `grep -n "acepto y aplico yo\|descarto con razón\|difiero a WA futuro\|requiere decisión humana real" .claude/agents/product-owner.md` → las 4 categorías deben existir.
- Coherencia Modo 1 vs Modo 2: las 4 categorías deben ser idénticas en ambas secciones (test manual al editar).

**Detección de regresión**:
- Si Paso 6b se elimina o las 4 categorías colapsan → PO vuelve a agregar mecánicamente. Test: `grep -c "Paso 6b" .claude/agents/product-owner.md` >= 1.
- Si las categorías de Modo 2 divergen de las de Modo 1 → inconsistencia de criterio. Test: revisar manualmente al editar cualquiera de las dos secciones.

**Veredicto**: aprueba.

---

### Gap 7 — Regla de autocontención del WA

**Aplicado en**:
- `CLAUDE.md` raíz: sección "Working Agreement (WA) — estructura" — subsección `### Regla de autocontención (legibilidad standalone)` presente. Fundamento Cohn INVEST "I = Independent" citado. Criterio operativo formulado como pregunta de auto-evaluación.
- `.claude/agents/product-owner.md`: Modo 1 paso 8 — `#### Checkpoint Gap 7 — WA legible standalone (regla de autocontención)` presente. Pregunta de auto-evaluación reproducida literalmente. 3 casos de aplicación listados. Referencia explícita a "regla de autocontención de CLAUDE.md raíz" sin redefinirla.
- `.claude/agents/product-owner.md`: Modo 2 Checkpoint Gap 5 — extensión del caso WA referenciador integrada.

**Verificación posible**:
- `grep -n "Regla de autocontención\|legibilidad standalone" CLAUDE.md` → sección must exist.
- `grep -n "Checkpoint Gap 7" .claude/agents/product-owner.md` → must exist.
- Coherencia: la pregunta de auto-evaluación en CLAUDE.md raíz y en el agent file PO deben ser literalmente la misma. Test: extraer ambas frases y comparar.

**Detección de regresión**:
- Si la sección en CLAUDE.md raíz se elimina → el checkpoint del agent file PO referencia algo que ya no existe. Test: `grep -n "Regla de autocontención" CLAUDE.md` >= 1.
- Si el checkpoint del agent file PO se elimina → el PO pierde el punto de control behavioral. Test: `grep -n "Checkpoint Gap 7" .claude/agents/product-owner.md` >= 1.

**Veredicto**: aprueba.

---

### Gap 8 — Criterio operativo "subagente vs sesión dedicada"

**Aplicado en**:
- `CLAUDE.md` raíz: sección "Tres mecanismos de invocación" — tabla reformulada con pivot "participación humana mid-trabajo". Subsecciones `### Criterio operativo "subagente vs sesión dedicada"` y `### Matriz orientativa de modalidad por tipo de step` (8 tipos). Nota final sobre `modality` opcional en templates de workflows.md. Verificado.
- `.claude/agents/product-owner.md`: Modo 1 paso 8 — `#### Checkpoint Gap 8 — Modalidad por step` presente. Referencia explícita a CLAUDE.md raíz + "NO dupliques la matriz aquí — aplícala". Modo 2 "Give-and-take con subagentes" — criterio Gap 8 aplicado mid-step.
- Campo `modality` en la estructura inline del WA en CLAUDE.md raíz (frontmatter de step). Verificado.

**Verificación posible**:
- `grep -n "Criterio operativo.*subagente\|Matriz orientativa de modalidad" CLAUDE.md` → ambas subsecciones must exist.
- `grep -n "Checkpoint Gap 8" .claude/agents/product-owner.md` → must exist.
- `grep -n "modality:" CLAUDE.md` → campo `modality` en la estructura de step must exist.
- Matriz: `grep -c "Sesión dedicada\|Subagente" CLAUDE.md` en la sección matriz → espera >= 8 ocurrencias (8 filas).

**Detección de regresión**:
- Si la matriz de 8 tipos desaparece de CLAUDE.md raíz → el checkpoint del agent file PO referencia "matriz orientativa" que ya no existe. Test: `grep -c "Scope-scan\|Review focal\|Audit focal\|Implementación" CLAUDE.md` en el bloque de la matriz → espera >= 4.
- Si el campo `modality` se elimina de la estructura de step → WAs futuros no declaran modalidad y el criterio Gap 8 no puede aplicarse en auditoría. Test: `grep -n "modality:" CLAUDE.md` >= 1.

**Veredicto**: aprueba.

---

### Gap 9 — Trazabilidad obligatoria (filesystem-changes)

**Aplicado en**:
- `CLAUDE.md` raíz: sección "Tres mecanismos de invocación" — subsección `### Contrato de trazabilidad \`filesystem-changes\` (subagentes con autoridad de edición)` presente. Formato YAML canónico declarado. Protocolo del orquestador (3 pasos: leer paths + registrar literal en Progreso + aplicar Filtro PO). Garantía de auditoría humana. Anclaje Nygard + Cohn.
- `.claude/agents/product-owner.md`: Modo 1 paso 8 — `#### Checkpoint Gap 9 — Trazabilidad obligatoria` presente con frase canónica que el PO debe incluir en el `purpose` del step subagente.
- `.claude/agents/product-owner.md`: Modo 2 "Al completar tu step" — `4a. Si el output viene de un subagente que aplicó edits a archivos` presente ANTES del Filtro PO, con los 3 sub-pasos (verificar paths + registrar filesystem-changes literal + aplicar Filtro PO).

**Verificación posible**:
- `grep -n "Contrato de trazabilidad\|filesystem-changes" CLAUDE.md` → >= 2 (sección + uso en el YAML).
- `grep -n "Checkpoint Gap 9\|filesystem-changes" .claude/agents/product-owner.md` → >= 2 (checkpoint Modo 1 + paso 4a Modo 2).
- Coherencia: el formato YAML canónico en CLAUDE.md raíz debe ser el mismo formato que el agent file PO referencia. Test: comparar estructura YAML en CLAUDE.md con lo que el paso 4a del Modo 2 menciona.

**Test de primer uso**: este mismo report (step-6 del WA-003) es el primer caso real de aplicación del Gap 9 por un subagente (QA invocado vía Task tool). El output del subagente incluye `filesystem-changes` estructurado. Si el PO recibe este output y registra el bloque literal en el Progreso del WA → Gap 9 completamente verificado en práctica.

**Detección de regresión**:
- Si la sección "Contrato de trazabilidad" se elimina de CLAUDE.md raíz → el checkpoint del agent file PO referencia algo inexistente. Test: `grep -n "Contrato de trazabilidad" CLAUDE.md` >= 1.
- Si el paso 4a del Modo 2 desaparece → el PO deja de verificar y registrar filesystem-changes de subagentes. Test: `grep -n "4a\." .claude/agents/product-owner.md` >= 1 en la sección "Al completar tu step".

**Veredicto**: aprueba. Este gap tiene además un primer test de integración real en este mismo WA-003.

---

### Gap 10 — Briefing proactivo por step

**Aplicado en**:
- `CLAUDE.md` raíz: sección "Working Agreement (WA) — estructura" — subsección `### Briefing por step (sección del cuerpo del WA)` presente. Los 4 bloques canónicos definidos (Mapa del grafo relevante, Contexto conversacional del humano, Razonamiento del orquestador, Output esperado complementario). Fundamento Cagan Empowered. Ejemplo de markdown canónico.
- `.claude/agents/product-owner.md`: Modo 1 paso 8 — `#### Checkpoint Gap 10 — Briefing proactivo por step` presente. Los 4 bloques estructurados con ejemplo de markdown completo. Las 6 reglas del Briefing por step declaradas. Coste en tokens estimado (~500-1000 por step).

**Verificación posible**:
- `grep -n "Briefing por step" CLAUDE.md` → must exist en sección estructura del WA.
- `grep -n "Checkpoint Gap 10\|Mapa del grafo relevante\|Contexto conversacional" .claude/agents/product-owner.md` → los 3 must exist.
- `grep -n "4 bloques" CLAUDE.md` o `grep -n "Bloque 1\|Bloque 2\|Bloque 3\|Bloque 4" CLAUDE.md` → los 4 bloques must exist en la subsección.

**Detección de regresión**:
- Si los 4 bloques canónicos se reducen (ej. alguien simplifica a 2 bloques) → los roles receptores vuelven a descubrir contexto solos. Test: `grep -c "Bloque [1-4]" .claude/agents/product-owner.md` debe ser >= 4.
- Si el Checkpoint Gap 10 desaparece del agent file PO → el PO deja de escribir briefings al draftear WAs. Test: `grep -n "Checkpoint Gap 10" .claude/agents/product-owner.md` >= 1.

**Veredicto**: aprueba.

**Nota operacional**: el WA-003 mismo fue draftado ANTES de que Gap 10 estuviera aplicado, por lo que sus steps no tienen Briefings por step. Es el caso esperado — la mejora aplica a WAs futuros. No es incumplimiento, es el bootstrapping cronológico correcto.

---

### F-ARCH-1, F-ARCH-2, F-ARCH-3 — Editoriales aplicadas en step-3

Estos tres flags del Architect se aplicaron en step-3 (coherence review). Por su naturaleza editorial, los verifico juntos.

**F-ARCH-1 aplicado en**: `CLAUDE.md` raíz sección "Workflow templates por fase SDLC" — tabla discovery muestra `capability-creation (modes: single | batch | reverse-engineering)`. Verificado.

**F-ARCH-2 y F-ARCH-3 aplicados en**: `vault/shared/governance/workflows.md` sección "Heurística de clasificación outcome-type" — tabla con 2 filas nuevas para keywords de `mode: batch` y `mode: reverse-engineering`. Nota al final de la heurística sobre el caso de pivot mid-WA (no clasificar como outcome-type nuevo). Verificado.

**Verificación conjunta**:
- `grep -n "modes: single" CLAUDE.md` → F-ARCH-1 must exist.
- `grep -n "crear el catálogo de capabilities\|extraer capabilities del bootstrap" vault/shared/governance/workflows.md` → F-ARCH-2 keywords must exist.
- `grep -n "Nota sobre pivots mid-WA\|esto no, mejor de otra forma" vault/shared/governance/workflows.md` → F-ARCH-3 must exist.

**Veredicto**: aprueba (los 3 flags editoriales están aplicados).

---

## Test de regresión recomendado (matriz consolidada)

| Gap | Path primario | Patrón de regresión a vigilar | Comando de check rápido |
|---|---|---|---|
| Gap 1 | `CLAUDE.md` + `workflows.md` | Desaparición de filas `aborted`/`aborted-reference` de la tabla de estados en uno de los dos archivos (divergencia cross-file) | `grep -c "aborted-reference" CLAUDE.md workflows.md` — espera >= 2 por archivo |
| Gap 2 | `capability-derivation/SKILL.md` | Desaparición de `## Template del capability file` o de cualquiera de sus 4 sub-secciones | `grep -c "Frontmatter\|Cuerpo del archivo\|Reglas de aplicación" .claude/skills/product-owner/strategy/capability-derivation/SKILL.md` — espera >= 3 |
| Gap 3 | `workflows.md` | Desaparición de `mode-flag` o de step-6 con `condition: mode == batch` | `grep -c "mode-flag\|mode == batch" vault/shared/governance/workflows.md` — espera >= 2 |
| Gap 4 | `workflows.md` + `product-owner.md` | Divergencia entre las 4 señales de pivot en ambos archivos | Revisar manualmente las 4 señales en ambos archivos tras cualquier edit a la sección de pivot |
| Gap 5 | `product-owner.md` | Desaparición de `Checkpoint Gap 5` o de la frase *"NO está documentado en el sistema"* | `grep -c "Checkpoint Gap 5\|NO está documentado en el sistema" .claude/agents/product-owner.md` — espera >= 1 cada uno |
| Gap 6 | `product-owner.md` | Desaparición de `Paso 6b` o de cualquiera de las 4 categorías del filtro (en Modo 1 O Modo 2) | `grep -c "acepto y aplico yo\|descarto con razón" .claude/agents/product-owner.md` — espera >= 2 (una ocurrencia por modo) |
| Gap 7 | `CLAUDE.md` + `product-owner.md` | Desaparición de `### Regla de autocontención` o de `Checkpoint Gap 7` | `grep -c "autocontención" CLAUDE.md .claude/agents/product-owner.md` — espera >= 1 por archivo |
| Gap 8 | `CLAUDE.md` + `product-owner.md` | Desaparición de la matriz de 8 tipos de step o de `Checkpoint Gap 8` | `grep -c "Matriz orientativa de modalidad" CLAUDE.md` + `grep -c "Checkpoint Gap 8" .claude/agents/product-owner.md` — espera >= 1 cada uno |
| Gap 9 | `CLAUDE.md` + `product-owner.md` | Desaparición de `Contrato de trazabilidad` o del paso `4a` en Modo 2 | `grep -c "Contrato de trazabilidad" CLAUDE.md` + `grep -c "4a\." .claude/agents/product-owner.md` — espera >= 1 cada uno |
| Gap 10 | `CLAUDE.md` + `product-owner.md` | Desaparición de `Briefing por step` o de `Checkpoint Gap 10` | `grep -c "Briefing por step" CLAUDE.md .claude/agents/product-owner.md` — espera >= 1 por archivo |

---

## Flags emergentes (filtrados por criterio QA)

### FQA-1 — Coherencia entre tabla de estados en CLAUDE.md raíz y en workflows.md (acoplamiento por duplicación)

Gap 1 aplica la tabla de estados en DOS lugares (CLAUDE.md raíz + workflows.md). El acoplamiento es consciente y declarado (Architect step-1: "duplicación controlada con coherencia auditable"). El riesgo es que ediciones futuras a una tabla no se repliquen en la otra.

**Clasificación QA**: flag menor, no bloqueante. El riesgo es real pero el coste de mitigación (revisar ambas tablas al hacer cualquier edit) es bajo. Recomendación: cuando se edite la tabla de estados en cualquiera de los dos archivos, el editor añade una nota explícita "TAMBIÉN actualizar en [otro archivo]" — o, mejor, el WA que produzca ese cambio incluye ambos paths en su `scope-allowed`.

**No aplica a cierre del WA-003**: este flag no bloquea el `/verify` del WA-003. Es input para práctica editorial futura.

### FQA-2 — Gap 5 y Gap 6 son mejoras comportamentales sin test automatizable

Los checkpoints Gap 5 (anti-improvisación) y Gap 6 (filtro PO) están correctamente declarados en el agent file PO, pero su efectividad real depende del comportamiento del agente en runtime. No hay fitness function automatizable para "el agente declara improvisaciones en el momento". La única detección es retroactiva (como en WA-002).

**Clasificación QA**: flag de cobertura parcial, esperado y aceptado. Los tests de verificación definidos en este report son tests de presencia del texto (grep), no tests de comportamiento runtime. Para tests de comportamiento sería necesario un mecanismo de auditoría de conversaciones (CAP-08 CLI, diferido a WA futuro). No bloquea.

### FQA-3 — El WA-003 no tiene Briefings por step (Gap 10 aplicado post-drafting)

Gap 10 se aplicó en step-4 del propio WA-003, DESPUÉS de que el WA ya estaba en ejecución. Los steps 1, 2 y 3 del WA-003 se ejecutaron sin Briefing. El step-6 (este) recibió un briefing completo en el prompt de invocación del PO (compensación ad-hoc).

**Clasificación QA**: nota de contexto, no flag bloqueante. El bootstrapping cronológico explica esta inconsistencia. La mejora aplica a WAs futuros. El step-5 del WA-003 documenta explícitamente este caso en el Progreso. No requiere acción.

---

## Recomendación al PO

El WA-003 puede cerrarse vía `/verify`. Las 10 mejoras están aplicadas en sus paths correspondientes y son verificables mediante tests simples de grep sobre los archivos editados. La verificabilidad es suficiente para que un futuro auditor pueda confirmar la aplicación de cada mejora sin necesidad de reinvocar a los subagentes originales (principio Cohn INVEST "I = Independent" extendido a steps, y Nygard "registro auditable sin reinvocación").

El punto más débil de verificabilidad es el comportamiento runtime de Gaps 5 y 6 (comportamentales), que solo son detectables retroactivamente por el humano. Esto es coherente con el flag preservado de "framework regression detection" diferido a WA futuro (CAP-08 CLI). No es bloqueante para el cierre del WA-003.

La matriz de test de regresión producida en este report sirve como punto de entrada para un futuro WA de "framework health check" si el equipo decide formalizarlo. Los comandos grep están diseñados para ser ejecutables en < 30 segundos sobre cualquier checkout del repo.

Un aspecto que merece atención en el próximo WA de edición del sistema: la duplicación controlada de la tabla de estados canónicos entre CLAUDE.md raíz y workflows.md (FQA-1). Es un acoplamiento consciente y auditado — pero necesita una convención editorial explícita para mantener la coherencia a medida que el catálogo de estados crece.
