---
description: "Scope-scan flat parallel multi-rol sobre una propuesta o candidata"
argument-hint: "<propuesta o candidata, en prosa>"
---

Ejecuta scope-scan flat parallel sobre la propuesta indicada. Invoca a los 6 roles asesores (product-owner, architect, designer, business-analyst, security-officer, qa) en paralelo. Cada uno navega su parte del grafo desde su ángulo y reporta `scope-scan-output`. Tú consolidas la unión y presentas al humano.

Útil al crear WA, mid-WA para validar candidatas, o cuando hay duda sobre scope.

## Pasos

1. **Identifica el contexto:**
   - Working directory actual y rol cargado.
   - Si hay WA activo en `vault/shared/sessions/active/`, lee su `dimensions-affected` para comparar al final.

2. **Construye prompt para CADA uno de los 6 roles asesores.** Cada prompt incluye:
   - Contenido de `.claude/agents/<rol>.md` (identidad del rol y su protocolo en scope-scan).
   - La propuesta del humano (el argumento del comando).
   - Si hay WA activo: dimensiones actuales del WA (para que el rol indique si la propuesta extiende esas dimensiones).
   - Si hay `related-spec` aplicable: el contenido de la spec.
   - Instrucción: *"Haz scope-scan sobre esta propuesta. Navega tu parte del grafo desde tu ángulo. Devuelve `scope-scan-output` con dimensions-detected, cross-links, flags, questions. Si no detectas nada relevante desde tu dominio, devuelve listas vacías. NO cascadees a otros roles — recepción los está invocando a todos en paralelo."*

3. **Invoca a los 6 roles EN PARALELO** vía Task tool — un solo mensaje con múltiples tool_use blocks:
   - `subagent_type: product-owner`
   - `subagent_type: architect`
   - `subagent_type: designer`
   - `subagent_type: business-analyst`
   - `subagent_type: security-officer`
   - `subagent_type: qa`

4. **Recibes 6 outputs.** Cada uno con la estructura `scope-scan-output`.

5. **Consolida:**
   - `dimensions-detected` = unión de todas las dimensions reportadas.
   - `cross-links-suggested` = unión de todos los reportados (related-to, depends-on, related-adrs).
   - `flags` = todos agregados, indicando qué rol los emitió.
   - `questions-for-human` = todas agregadas, indicando qué rol pregunta.

6. **Compara con WA activo (si lo hay):**
   - Si el conjunto de dimensiones detectadas es ⊂ del `dimensions-affected` del WA → la propuesta está dentro del scope actual.
   - Si añade dimensiones nuevas → la propuesta extiende el scope. Indica al humano que considere extender el WA o abrir uno nuevo.

7. **Presenta al humano** con el formato de output abajo.

## Output format

```
## Scope-scan · "<propuesta>"

### Dimensiones detectadas (unión)
[<lista>]

### Por rol
**Product Owner:** dimensions=[<lista o []>], flags=<N>, cross-links=<N>
**Architect:** dimensions=[<lista o []>], flags=<N>, cross-links=<N>
**Designer:** dimensions=[<lista o []>], flags=<N>, cross-links=<N>
**Business Analyst:** dimensions=[<lista o []>], flags=<N>, cross-links=<N>
**Security Officer:** dimensions=[<lista o []>], flags=<N>, cross-links=<N>
**QA:** dimensions=[<lista o []>], flags=<N>, cross-links=<N>

### Cross-links sugeridos
- related-to: [<node-ids o vacío>]
- depends-on: [<node-ids o vacío>]
- related-adrs: [<adr-ids o vacío>]

### Flags consolidados
- [<rol>] <flag breve>
- ...

### Questions for human
- [<rol>] <pregunta>
- ...

### Comparación con WA activo
<bloque solo si hay WA activo>
WA `<id>` tiene dimensions-affected: [<actuales>].
Scope-scan detecta: [<detectadas>].
→ <"Dentro de scope actual" | "Extiende scope: añade <nuevas>. Considera extender el WA o abrir uno nuevo.">
```

## Cuándo es útil

`/scope-scan` complementa los **tres checkpoints automáticos** que ya existen en el lifecycle del WA (creation + post-step + verify). Lo usas on-demand cuando el humano juzga necesario un scan extra entre checkpoints automáticos:

- **Mid-step (mid-trabajo, antes del handoff):** el active-role está conduciendo su step y duda con una candidata high-stakes (ej. PO iterando capabilities, una candidata que parece tocar security pero no está claro). En lugar de esperar al post-step scope-scan automático del handoff, ejecuta `/scope-scan` ahora para validar antes de seguir.
- **Pre-WA:** explorar una idea antes de proponer un WA formal. Ver qué roles tendrían algo que decir.
- **Mid-step en sesión Developer:** detectar si una decisión de implementación extiende el scope (ej. "voy a refactorizar X" — `/scope-scan` confirma si está dentro del scope del WA o lo extiende).
- **Manual al crear WA:** alternativa explícita al scope-scan automático que recepción ejecuta. Mismo mecanismo.

**Diferencia con post-step scope-scan automático:**
- Post-step automático lo dispara el active-role al completar su step (parte del handoff obligatorio).
- `/scope-scan` lo dispara el humano on-demand en cualquier momento, sobre cualquier propuesta o candidata, sin esperar al handoff.

## Importante

- NO confundir con `/verify`. `/verify` es backward-looking (valida que un WA cumple su scope al cierre). `/scope-scan` es forward-looking (descubre qué scope tendrá una propuesta).
- NO ejecutes el comando si la propuesta es trivial (typo, copy fix). Para esos casos, decide tú directamente.
- Si la propuesta es muy abstracta o muy concreta, ajusta el prompt enviado a los roles para darles contexto suficiente.
