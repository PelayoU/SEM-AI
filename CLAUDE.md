<!--
type: claude-md-raiz
materializes-feature: [feature-010-entry-point-por-rol, feature-038-po-modo-1, feature-041-readme-onboarding, feature-044-glosario-publico, feature-045-ruta-lectura-audiencia]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): guía estática del proyecto cargada por Claude Code al arrancar al root del repo. Materializa:
# - feature-010 (tabla rol → atajo + criterio de delegación)
# - feature-038 (referencia al PO Modo 1)
# - feature-041 (sección onboarding públicamente accesible cuando se ve el repo)
# - feature-044 (referencia al glosario público — pendiente artefacto físico)
# - feature-045 (sección "Cómo arrancar trabajo" como ruta de lectura inicial)
-->

# SEM-IA · Guía del proyecto

Este archivo carga automáticamente cuando se arranca Claude Code al root del repo. **No define identidad de agente** — es guía estática del proyecto.

SEM-IA es un framework de gestión del desarrollo de software con IA. El motor opera con **agentes IA homólogos por rol** que conducen el trabajo en sus dominios.

> **Nota terminológica sobre "recepción":** *"Recepción"* es la **modalidad del Product Owner extendido cuando arranca con propuesta del humano** (Modo 1 — Entrada al sistema). NO hay sesión separada de "recepción" al root: este `CLAUDE.md` raíz es **guía estática del proyecto**; la sesión de recepción real es `npm run sem` (o `npm run po`), que abre sesión PO con identidad cargada desde `.claude/agents/product-owner.md`. El PO en Modo 1 clasifica outcome-type, convoca reuniones (scope-scan multi-rol), drafta Working Agreements, conduce trabajo product-driven o delega a otros roles custodios cuando corresponde. Otros roles (Architect, DevOps) pueden ser orquestadores de WA cuando el humano arranca trabajo de su dominio puro (`npm run arch`, `npm run ops`) — pero esa modalidad no se llama "recepción", ese término queda reservado para el PO.

Cuando los docs operativos (`workflows.md`, agent files asesores, slash commands) mencionan *"recepción"*, se refieren al PO en su Modo 1.

> Tesis: *"El trabajo con IA requiere su propia infraestructura de gestión: una Ingeniería de Gestión de Software de IA — reformulación de la SEM clásica materializada como capa de agentes de IA que rodea el trabajo del ingeniero, sin sustituir a ninguno de los roles humanos. La IA como infraestructura, el humano como autor."*

---

## Cómo arrancar trabajo

**Entrada por defecto:** sesión Product Owner extendido (PM + Product Leader en Cagan).

```bash
npm run sem    # alias de: cd vault/product-owner && claude
npm run po     # idéntico — sesión PO directa
```

El PO extendido es la entrada al sistema cuando el humano trae una propuesta. Conduce el flujo completo: clasifica `outcome-type`, convoca reunión de discovery (scope-scan flat parallel multi-rol), drafta el plan (Working Agreement), conduce trabajo estratégico/producto, delega trabajo puramente técnico/ops a los roles custodios apropiados, ejecuta `/verify` al cierre.

**Entradas alternativas** para trabajo puramente de otro dominio (sin pasar por PO):

| Comando | Para qué |
|---|---|
| `npm run arch` | Architect — ADRs, refactor sin spec previa, decisiones técnicas puras |
| `npm run des` | Designer — usability audits, accessibility reviews |
| `npm run biz` | Business Analyst — compliance maps, pricing impact, GTM reviews |
| `npm run sec` | Security Officer — threat models, security audits |
| `npm run qa` | QA — test strategy, coverage analysis |
| `npm run dev` | Developer — implementación de specs ready-for-implementation |
| `npm run ops` | DevOps — pipelines CI/CD, infraestructura, observabilidad |

**Si dudas qué sesión arrancar:** abre `npm run sem` (PO). El PO clasifica la propuesta y, si es de otro dominio, te indica explícitamente qué sesión abrir.

---

## Slash commands (disponibles desde cualquier sesión)

| Comando | Para qué |
|---|---|
| `/status` | Snapshot del estado: WAs activos por track (Discovery/Delivery/Operations/Meta), backlog, subgrafo estratégico, features por status, ADRs |
| `/wa` | Detalle del Working Agreement activo en el contexto actual, con steps y status |
| `/scope-scan "<propuesta>"` | Scope-scan flat parallel multi-rol on-demand sobre una propuesta. Invoca a los 6 asesores en paralelo (PO + 5 restantes) |
| `/verify` | Aplica matriz de verificación al WA listo para cierre. Invoca custodios derivados de `dimensions-affected`, consolida, ejecuta `on-close` transitions, archiva |
| `/sessions` | Lista de modos de trabajo y sesiones dedicadas disponibles |

---

## Modelo conceptual

**El proyecto vive como grafo declarativo** con espina dorsal jerárquica + cross-links explícitos:

```
Visión → Goals → Capabilities → Features → Stories → Specs (Gherkin con AC) → Examples → Artifacts (código)
```

Cada nodo es un archivo Markdown con frontmatter YAML que declara `parent` (espina dorsal) + `also-relates-to` / `depends-on` / `dimensions-affected` / `related-adrs` (cross-links).

**Vault organizado role-first** — un directorio por rol custodio. Cada rol custodia una dimensión.

| Dimensión | Custodio | Cagan risk |
|---|---|---|
| `product` (estrategia + operativo) | Product Owner extendido | value-risk íntegro |
| `technical` | Architect | viability-risk technical |
| `usability` | Designer | usability-risk |
| `business` | Business Analyst | business-viability-risk |
| `security` | Security Officer | (transversal) |
| `quality` | QA | (transversal) |
| `operations` | DevOps | (transversal) |

8 roles core: 6 asesores (custodios de dimensiones, participan en reuniones multi-rol) + 2 ejecutores (Developer, DevOps).

---

## Working Agreement (WA) — estructura

Un WA es un **contrato declarativo** que orquesta un bloque de trabajo multi-rol. Vive en `vault/shared/sessions/active/wa-YYYY-MM-DD-NNN.md`. Frontmatter:

```yaml
type: working-agreement
id: wa-YYYY-MM-DD-NNN
created: <ISO datetime>
status: active  # active | aborted (ver Protocolo de pivot mid-flight en workflows.md)

# Clasificación
outcome-type: <discovery|design|implementation|operations|meta outcome>
phase: <SDLC phase, heredada del template>

# Qué se va a hacer
objective: "<frase clara>"

# Referencias a nodos del grafo
related-feature: <feature-id o null>
related-capability: <cap-id o null>
related-spec: <spec-id o null>
related-adr: <adr-id o null>

# Nodo consumido del backlog (si template lo requiere)
consumes:
  node-id: <id o null>
  required-status: <status esperado o null>
  verified-at: <ISO datetime>

# Output del scope-scan flat parallel
dimensions-affected: [<lista>]
participants: [<roles que aportaron en scope-scan>]

# Steps ordenados — derivados del template del outcome-type, adaptados al scope-scan
steps:
  - id: step-1
    active-role: <rol>
    phase: <fase>
    modality: <subagente | sesion-dedicada>  # ver "Tres mecanismos de invocación" abajo
    purpose: "<...>"
    expected-output: "<...>"
    status: pending  # pending | in-progress | done | aborted
    completed-at: null
    completed-by: null
    # Campos opcionales si el step se aborta con trabajo parcial:
    # aborted-at: <ISO datetime>
    # partial-output: "<descripción del trabajo parcial preservado + paths>"

# Alcance autorizado/prohibido (paths del repo)
scope-allowed: [<paths>]
scope-forbidden: [<paths>]

# Verificadores derivados de dimensions-affected (algoritmo: verifiers = { custodian(d) })
verifiers-required: [<lista>]

# Criterios de cierre
closure-criteria:
  - Todos los steps en status: done
  - /verify aprobado por todos los verificadores
  - <criterios adicionales>

# Efectos al cerrar el WA — el /verify aplica estas transiciones
on-close:
  - "<path>: <status-inicial> → <status-final>"

# Campos opcionales — solo presentes si el WA es aborted (pivot mid-flight) o supersede a otro:
# aborted-at: <ISO datetime>           # cuándo se decidió el pivot
# aborted-reason: "<por qué>"          # razón documentada del pivot
# supersedes: wa-YYYY-MM-DD-MMM         # qué WA anterior reemplaza este
# superseded-by: wa-YYYY-MM-DD-NNN      # qué WA successor reemplaza a este (si aborted)
# supersede-reason: "<por qué>"        # razón del supersede
```

### Regla de autocontención (legibilidad standalone)

**El cuerpo del WA debe incluir todo el contexto necesario para que un lector standalone — sin acceder a otros archivos — entienda qué se va a hacer y por qué.**

Si el WA consume contenido de otro archivo (ej. gaps del anexo de un WA archivado, decisiones de un discovery doc, criterios de un research previo), **reproducir ese contenido in extenso en el cuerpo del WA, no solo referenciarlo**. Los campos `related-feature` / `related-capability` / `related-spec` / `related-adr` del frontmatter señalan referencias auxiliares para trazabilidad; el cuerpo del WA es ground truth operativo.

Fundamento (Cohn, *User Stories Applied* — INVEST, criterio "I = Independent"): un Working Agreement, como unidad de trabajo, debe ser inteligible sin documentos externos. Asumir que el lector va a abrir un archivo archivado en otro path rompe la propiedad de independencia y degrada la auditabilidad del registro histórico del proyecto.

Criterio operativo (aplicable al draftear o auditar un WA): *"si alguien que no ha leído otros archivos abre solo este WA, ¿entiende qué se va a hacer y por qué? Si no, expandir el cuerpo del WA incluyendo el contenido referenciado."*

### Briefing por step (sección del cuerpo del WA)

Cuando un WA tiene steps con `active-role` distinto del orquestador (ej. PO drafta un WA donde steps son ejecutados por Architect, Designer, QA, etc.), el cuerpo del WA debe incluir una **sección "Briefing del step-N"** por cada step no-orquestador, escrita por el orquestador al draftear. El briefing transmite al rol receptor **contexto curado + matices conversacionales** que el orquestador ya conoce y que el rol receptor de otro modo tendría que descubrir solo (déficit estructural + conversacional, Gap 10 del sistema).

**Estructura canónica del briefing (4 bloques)**:

**Bloque 1 — Mapa del grafo relevante** (paths curados, NO contenido duplicado): lista de paths del vault que el rol debe leer para este step, con una línea por path explicando por qué es relevante a ESTE step específico. NO se copia el contenido (DRY — ground truth vive en el archivo canónico). Si los archivos cambian, el rol lee la versión actual.

**Bloque 2 — Contexto conversacional del humano**: matices que emergieron de la conversación humano-orquestador y NO viven en ningún archivo del grafo (urgencias mencionadas, preferencias explícitas, experiencia previa relevante, dudas concretas planteadas, decisiones o restricciones implícitas detectadas). Incluir in extenso — no existe en otro sitio.

**Bloque 3 — Razonamiento del orquestador al draftar este step**: por qué este step, qué espera del rol, heurísticas o criterios a aplicar, coherencia esperada con otras features/decisiones, indicación de qué flagear para otros steps si emerge.

**Bloque 4 — Output esperado complementario**: paths específicos a crear, cross-links a declarar, anclaje rico al `expected-output` del frontmatter (descripción narrativa de qué forma debe tener el output, no solo qué path).

**Razón (Gap 10)**: el rol receptor del step arranca con panorámica curada + matices preservados, no con frontmatter desnudo. Anclaje Cagan (*Empowered*) — strong product team transmite contexto explícitamente, NO asume que el especialista lo descubra solo. Bloques opcionales si no aplican (no inventar).

---

## Tres reuniones del lifecycle del WA

El motor aplica scope-scan flat parallel multi-rol en **tres puntos uniformes** del lifecycle de un WA:

| Reunión | Cuándo | Quién dispara | Detecta |
|---|---|---|---|
| **Discovery review** (al crear WA) | Al draftear el WA | PO (entrada al sistema) | Dimensiones, cross-links, flags iniciales. Adapta workflow template. |
| **Step checkpoint** (post-step) | Tras completar cada step | Active-role del step | Drift bottom-up, contradicciones con grafo, dimensiones nuevas surgidas. |
| **Sign-off / approval** (verify) | Al cierre del WA | PO (o quien ejecute `/verify`) | Veredicto final de los custodios de las dimensiones afectadas. |

Adicionalmente:

- **`/scope-scan "<propuesta>"`** — slash on-demand desde cualquier sesión para validar candidatas mid-trabajo.
- **Stakeholder sync mid-step** — el active-role invoca subagentes via Task tool cuando emerge duda relevante a otro dominio (Cagan principio 2: give-and-take, encouraged).

---

## Estados canónicos del nodo

| Status | Significado | Quién lo setea |
|---|---|---|
| `draft` | Nodo en construcción durante un WA activo | Skill al crear el nodo |
| `proposed` | ADR en construcción (convención Nygard) | `adr-writing` skill |
| `active` | Nodo completado y verificado (visión, goal, capability, review, audit) | PO al `/verify` vía `on-close` |
| `accepted` | ADR aprobado | PO al `/verify` vía `on-close` |
| `ready-for-implementation` | Spec/feature en backlog esperando WA de implementation | PO al `/verify` del WA `feature-design` |
| `in-implementation` | WA `feature-build` activo consumiéndolo | Step 1 del `feature-build` |
| `implemented` | Feature implementada y verificada | PO al `/verify` del WA `feature-build` |
| `superseded` | ADR reemplazado por otro ADR | Modificación manual + `superseded-by` |
| `deprecated` | Nodo ya no aplica por decisión consciente del producto | Decisión consciente vía WA apropiado |
| `aborted` | WA (o step de WA) terminado antes de `/verify` por pivot consciente del approach. Preserva `aborted-at` + `aborted-reason`; opcionalmente `superseded-by` apuntando al WA successor. Aplicable a WA completo y a steps con trabajo parcial (preservados vía `partial-output`). | PO/orquestador al ejecutar Protocolo de pivot mid-flight |
| `aborted-reference` | Nodo producido en step parcial de un WA `aborted`; preservado como referencia auditable pero no operativo (no entra en backlog ni en queries de nodos `active`). Distinto de `deprecated`: aquí la causa es el pivot del WA contenedor, no obsolescencia semántica del nodo. | PO/orquestador al ejecutar Protocolo de pivot mid-flight |

**El backlog emerge como query**: nodos del vault con `status: ready-for-implementation`. No es estructura persistente nueva.

**Sobre los estados de pivot (`aborted` / `aborted-reference`)**: ver "Protocolo de pivot de un WA mid-flight" en `vault/shared/governance/workflows.md`. Los estados `aborted` y `aborted-reference` modelan el caso en que el approach del WA se demuestra incorrecto mid-flight y se decide refactorizar el plan (Cagan principio give-and-take aplicado al meta-nivel). NO son sinónimos de `deprecated`: `deprecated` significa "el nodo ya no aplica por decisión de producto"; `aborted*` significa "el contenedor de trabajo fue refactorizado". La distinción preserva trazabilidad auditable.

---

## Workflow templates por fase SDLC

Catálogo en `vault/shared/governance/workflows.md`. Indexado por fase:

| Fase | Outcome-types |
|---|---|
| **discovery** | `vision-creation` · `goal-definition` · `capability-creation` *(modes: single \| batch \| reverse-engineering)* |
| **design** | `feature-design` · `adr` · `threat-model` |
| **implementation** | `feature-build` · `bugfix` · `refactor` |
| **operations** | `pipeline-change` · `infra-decision` · `observability-instrument` |
| **meta** | `doc-edit` · `trivial` |

Cada template declara `default-steps` (con `role` + `phase` + `purpose` + `optional` + `condition`) y `on-close` (transiciones de status al cerrar el WA).

---

## Dual Track (Cagan/Patton)

SEM-IA materializa el modelo dual track canónico:

- **Discovery track** = WAs de fases `discovery` + `design`. Aborda los 4 risks de Cagan (value, usability, viability technical, business viability).
- **Delivery track** = WAs de fase `implementation`. Aborda QAs de Bass (functionality, scalability, reliability, performance, maintainability).
- **Backlog** = query sobre `status: ready-for-implementation`. Puente persistente entre tracks.

Los dos tracks corren en paralelo en proyectos maduros. `/status` muestra salud del Dual Track.

---

## Estructura del vault

```
vault/
├── product-owner/         ← PO extendido (dimensión: product — strategy + operativo)
│   ├── CLAUDE.md          ← entry point sesión PO
│   ├── strategy/          ← visión, goals, capabilities, roadmap
│   ├── strategy-reviews/  ← reviews periódicos
│   ├── specs/             ← features, stories, specs Gherkin
│   └── discovery/         ← examples, JTBD, AC filtering
│
├── architect/             ← Architect (dimensión: technical)
│   ├── CLAUDE.md
│   ├── adrs/              ← Architecture Decision Records (formato Nygard)
│   └── research/          ← reviews técnicos + library/ bibliográfica
│
├── designer/              ← Designer (dimensión: usability)
│   ├── CLAUDE.md
│   └── audits/
│
├── business-analyst/      ← Business Analyst (dimensión: business)
│   ├── CLAUDE.md
│   └── audits/
│
├── security-officer/      ← Security Officer (dimensión: security)
│   └── audits/
│
├── qa/                    ← QA (dimensión: quality)
│   └── reports/
│
├── developer/             ← Developer (sin dimensión, implementa)
│   ├── learnings/
│   └── gotchas/
│
├── devops/                ← DevOps (dimensión: operations)
│
└── shared/                ← Cross-role / infraestructura
    ├── sessions/active|archive/   ← Working Agreements
    ├── governance/                ← defaults del framework
    │   ├── dimensions.md          ← catálogo dimensión → custodio
    │   ├── role-catalog.md        ← catálogo de roles
    │   ├── verification-matrix.md ← guía orientativa de dimensiones por operación
    │   ├── workflows.md           ← catálogo de workflows por fase SDLC
    │   └── repo-structure.md      ← estructura del repo
    ├── plans/active|archive/
    ├── retros/
    └── reviews/
```

---

## Convenciones

- **Frontmatter YAML** obligatorio en todo archivo del vault. La estructura de cada tipo de nodo vive **inline en la skill que lo crea** (`vision-quality-check` define estructura visión, `capability-derivation` define estructura capability, `feature-decomposition` define estructura feature, etc.).
- **Wiki-links `[[id]]`** para referencias internas en el contenido.
- **Comentarios de trazabilidad** `// @sem-ia: <node-id>` en archivos de código.
- **Cobertura de AC** `// @ac-coverage: AC-X1, AC-X2` en archivos de test.
- **Agentes** en `.claude/agents/<rol>.md` (8 roles core).
- **Skills** en `.claude/skills/<rol>/<skill>/SKILL.md` (operativas) y `.claude/skills/<rol>/strategy/<skill>/SKILL.md` (estratégicas del PO).

---

## Tres mecanismos de invocación

| Mecanismo | Cuándo | Cómo |
|---|---|---|
| **Sesión dedicada del rol** | Ejecución multi-turn de un step con participación humana mid-trabajo | `npm run <rol>` carga la identidad del rol vía wrapper `vault/<rol>/CLAUDE.md` |
| **Subagente via Task tool** | Step focal one-shot sin participación humana mid-trabajo (reuniones scope-scan / checkpoint / sign-off + reviews focales + give-and-take mid-step) | El rol activo invoca `subagent_type: <rol>` con prompt focalizado |
| **Skill inline** | Activación nativa de Claude Code cuando el contexto matchea la `description` de un SKILL.md | Transparente — no requiere invocación manual |

### Criterio operativo "subagente vs sesión dedicada"

Al draftear un WA (o al invocar un rol mid-step), el orquestador debe decidir la modalidad de cada step. **El pivot decisorio es: ¿el step requiere participación humana mid-trabajo?**

**Subagente** (one-shot focal) procede cuando el step produce un **artefacto consolidado sin requerir input humano durante su ejecución**. El subagente recibe contexto completo, opera, devuelve resultado. Ejemplos: scope-scans, viability-reviews, coherence-evaluations, verificabilidad-reviews, threat-models pequeños, audits focales.

**Sesión dedicada** (multi-turn) procede cuando el step requiere **conversación profunda con el humano participando**: ida-y-vuelta, decisiones intermedias, exploración de alternativas. Ejemplos: descomposición de capability en features con conversación (PO en feature-design), escritura de ADR completo con research Nygard (Architect), implementación de feature con iteración (Developer), conducción de inception greenfield (PO Modo 1).

**Casos límite**: si un step empieza como subagente pero emerge necesidad de profundizar → el subagente devuelve estado parcial recomendando "esto requiere sesión dedicada", y el orquestador deriva al humano a abrir `npm run <rol>` para continuar.

**Trade-offs operativos a sopesar:**

- **Coste de tokens y context window**: subagente devuelve resumen breve sin inflar el context del orquestador; sesión dedicada arranca cache propio del rol y consume context window separado.
- **UX humano**: subagente es transparente (no requiere cambio de terminal); sesión dedicada requiere `npm run <rol>` con cambio de contexto operativo del humano.
- **Profundidad del trabajo**: subagente NO permite pivotar a multi-turn dentro del mismo invocation; sesión dedicada permite ida-y-vuelta con humano participando.
- **Paralelización**: varios subagentes en paralelo (un solo mensaje del orquestador con múltiples Task tool calls); sesiones dedicadas son serializadas (humano cambia entre terminales).

**Fundamento bibliográfico**: la distinción mapea formalmente la separación de Anthropic Claude Code entre subagents (contexto independiente, one-shot, paralelizables, retornan resumen) y sessions (multi-turn conversational con humano). Cagan principio 2 (give-and-take) refina el criterio: cuando el give-and-take es entre el rol y el humano → sesión dedicada; cuando es entre roles AI sin humano mid-trabajo → subagentes paralelos.

### Matriz orientativa de modalidad por tipo de step

No rígida — el orquestador (PO típicamente) ejerce criterio según contexto del WA concreto.

| Tipo de step | Modalidad preferida | Razón |
|---|---|---|
| Scope-scan (initial al crear WA, post-step, sign-off al `/verify`) | Subagente paralelo | Multi-rol simultáneo, focal por dominio, sin participación humana intermedia |
| Review focal (viability-review, verificabilidad-review, coherence-evaluation) | Subagente | One-shot sobre artefacto existente, producido sin humano mid-trabajo |
| Audit focal (threat-model focal, business review, usability audit) | Subagente típicamente | One-shot focal; puede pivotar a sesión si emerge profundidad |
| Implementación de feature (developer) | Sesión dedicada | Multi-turn iterativo con humano probando |
| Design completo de feature (PO en feature-design) | Sesión dedicada PO | Multi-turn decomposition + spec writing con humano decidiendo |
| Escritura de ADR completo (Architect) | Sesión dedicada Architect | Research + redacción Nygard + alternatives, conversación con humano |
| Edición menor de doc (doc-edit) | Subagente o el orquestador edita directamente | Trivial, sin necesidad de profundidad |
| Inception greenfield (PO Modo 1) | Sesión dedicada PO | Multi-turn de visión → goals → capabilities → features con humano |

Los templates de `workflows.md` pueden declarar opcionalmente `modality: subagente | sesion-dedicada` en cada step de `default-steps` para hacer explícita la decisión recomendada por el template (el orquestador puede override-arlo en el WA concreto si el contexto del scope-scan justifica otra elección).

### Contrato de trazabilidad `filesystem-changes` (subagentes con autoridad de edición)

Todo subagente invocado via Task tool con autoridad de edición sobre archivos del repo, al cerrar su step, **debe incluir en su output al orquestador**, además del resumen ejecutivo narrativo, una sección estructurada `filesystem-changes` con el siguiente formato canónico:

```yaml
filesystem-changes:
  - path: <path absoluto al archivo>
    operation: created | edited | deleted
    locations:
      - lines: <rango ej. 153-161 o "N/A si created/deleted">
        change-summary: "<qué se añadió / modificó / eliminó en este rango, frase corta>"
    rationale: "<por qué se hizo este cambio, anclado al gap u objetivo del WA>"
```

**Razón (Gap 9 del sistema)**: los subagentes mantienen autoridad de edición — la paralelización y eficiencia operativa requieren que puedan tocar archivos sin pasar por sesión dedicada. PERO el orquestador debe tener **registro técnico auditable** de lo aplicado, no solo resumen narrativo. Sin `filesystem-changes`, ni el orquestador ni el humano pueden auditar con precisión en el futuro qué tocó cada subagente.

**Protocolo del orquestador al recibir output del subagente**: (1) leer los paths reportados para verificar coincidencia con `filesystem-changes`; (2) registrar `filesystem-changes` literal en la entrada de Progreso del step en el WA; (3) aplicar Filtro PO (ver agent file PO Modo 1 paso 6b) sobre los cambios.

**Garantía de auditoría humana**: como el `filesystem-changes` queda persistente en el WA (activo o archivado), el humano puede en cualquier momento futuro pedir auditoría — *"enséñame qué cambió el subagente X en step-Y del WA-Z"* — y el orquestador responde con precisión consultando el Progreso del WA + abriendo los paths referenciados, sin reconstrucción de memoria narrativa.

**Anclaje bibliográfico**: Nygard ADRs principio de "registro auditable de decisiones técnicas" extendido a registro auditable de cambios al filesystem. Cohn INVEST "I = independent" extendido — cada step debe ser auditable sin reinvocar al subagente original.

---

## Cinco reglas para el humano

1. Entra al sistema por la sesión del rol custodio del primer trabajo. Para producto / estrategia: `npm run sem` (PO). Para trabajo puramente técnico o de ops: directamente `npm run arch` / `npm run ops` / etc.
2. El rol activo conduce su step. Tu papel es dirigir (juzgar, decidir, firmar), no ejecutar línea por línea.
3. Trabajo bajo Working Agreement. Si no hay WA aún, el rol activo lo drafta primero (con discovery review previo).
4. Al cierre, `/verify` aplica matriz de verificación. Los custodios aprueban o bloquean.
5. Si te desvías de un WA activo, vuelves a la sesión del rol que lo coordina (típicamente PO) y decides: aparcar, detener, o extender.

---

## Más información

- Filosofía y tesis: `vault/product-owner/strategy/vision.md`.
- Goals del proyecto: `vault/product-owner/strategy/goal-*.md`.
- Historia del bootstrap: `vault/architect/research/bootstrap-summary.md`.
- Onboarding completo: `README.md`.
