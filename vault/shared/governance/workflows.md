---
type: governance
id: workflows-catalog
title: "Catálogo de workflows por fase SDLC"
status: active
created: 2026-05-07
author: human
materializes-feature: [feature-018-slash-scope-scan, feature-019-slash-verify, feature-038-po-modo-1, feature-039-cadena-was-greenfield]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): catálogo de 14 workflow templates consumido por:
# - feature-018 /scope-scan (mapping outcome-type → fase SDLC)
# - feature-019 /verify (algoritmo on-close declarado por template)
# - feature-038 PO Modo 1 (carga template del outcome-type clasificado)
# - feature-039 cadena WAs greenfield (consume templates existentes para proponer cadena)
---

# Catálogo de workflows por fase SDLC

**Este archivo es la fuente de verdad de los workflows que SEM-IA orquesta.** Los templates están **indexados por fase del SDLC enterprise** (`discovery | design | implementation | operations | meta`). Cada template tiene un `outcome-type` único, declara qué `produces` (qué output deja en el vault) y opcionalmente qué `consumes` (qué nodo del vault necesita como input). Recepción usa este catálogo al crear un WA: clasifica el outcome-type del request, identifica la fase, carga el template, verifica precondiciones (`consumes`), y adapta los steps según el output del scope-scan.

**Encoded enterprise workflows = la contribución central de SEM-IA.** Las empresas YA tienen workflows con fases discretas y un backlog persistente entre ellas; aquí los declaramos en formato AI-ejecutable.

## Modelo conceptual

- **El WA es uniforme** (un solo shape: `outcome-type` + `steps[]` + sessions + handoffs + verify). No hay categoría `node | impl` como campo de primera clase.
- **La fase la dicta el template**, no el WA. Recepción la deriva al cargar el template.
- **Los templates de fase `design` setean transición de status** vía el campo `on-close` del WA: el nodo de output pasa de `status: draft` (estado inicial que las skills producen) a `status: ready-for-implementation` al cerrar el WA. Ese nodo entra en el **backlog**.
- **Los templates de fase `implementation` consumen un nodo del backlog** (su step 1 referencia el nodo y verifica que existe con el status correcto antes de empezar). Al cerrar transicionan el nodo a `status: implemented`.
- **El backlog emerge gratis** como query sobre nodos del vault con `status: ready-for-implementation`. No hay estructura persistente nueva — solo un campo en el frontmatter.

## Separación de responsabilidades para `status`

- **Skills** producen el nodo con `status: draft` (o `proposed` para ADRs según convención Nygard) — estado neutro, sin asunciones de lifecycle.
- **Templates** declaran en su `on-close` qué transición de status ocurre al cerrar el WA.
- **WAs** heredan el `on-close` del template (recepción lo escribe en el frontmatter al draftear).
- **Recepción al `/verify`** aplica las transiciones de `on-close` después de que los verificadores aprueben.

Lifecycle por tipo de nodo:

| Nodo | Inicial (skill) | Tras /verify de su WA design | Tras /verify de WA implementation |
|---|---|---|---|
| spec / feature | `draft` | `ready-for-implementation` | `implemented` |
| ADR | `proposed` | `accepted` | n/a (ADR no tiene fase implementation) |
| threat-model | `draft` | `active` | n/a |
| visión / goal / capability | `draft` | `active` | n/a |
| review / research / audit | `draft` | `active` | n/a |

## Cómo recepción usa este catálogo

```
1. Humano: "<request>"
2. Recepción clasifica outcome-type (heurística keywords, ver tabla abajo).
3. Recepción identifica la fase del template y verifica precondiciones:
   - Si fase es `implementation`: comprueba que el nodo referenciado por `consumes`
     existe en el vault con `status: ready-for-implementation`.
     Si NO existe: propone primero un WA de fase `design` para producirlo.
4. Recepción ejecuta scope-scan flat parallel (6 asesores en paralelo: product-owner, architect, designer, business-analyst, security-officer, qa).
5. Recepción adapta template:
   - Mantiene steps "siempre".
   - Mantiene steps "optional" si su `condition` matchea con scope-scan output.
   - Omite steps "optional" cuya condition no aplica.
6. Recepción copia el `on-close` del template al frontmatter del WA.
7. Recepción presenta WA con steps al humano.
8. Tras ejecución de todos los steps, recepción al `/verify` aplica las transiciones
   declaradas en `on-close` después de que verificadores aprueben.
```

## Cadena de WAs por gaps detectados (única vía de entrada)

El camino habitual del día a día. Cualquier estado del vault (vacío, parcial, maduro). Mecánica:

1. Humano pide algo (ej. *"implementar feature X"*).
2. Recepción dispara scope-scan flat parallel.
3. Asesores navegan su parte del grafo y flagean **gaps upstream** si los detectan (ej. PO: "no hay capability padre", "no hay goal padre"; Architect: "ADR aplicable falta"; etc.).
4. Recepción consolida flags y, si hay gaps, **propone una cadena de WAs** ordenada top-down (visión → goal → capability → feature) usando los templates existentes (no hay template "cadena" — es comportamiento de recepción).
5. Humano aprueba la cadena. Recepción drafta SOLO el primer WA de la cadena. Tras /verify, drafta el siguiente. Cada WA es independiente con su closure-criteria + on-close.

**Tres formas que toma este patrón:**

- **Cadena directa** (greenfield + feature): humano pide feature en vault vacío → scope-scan flagea visión + goals + capability faltantes → cadena de 4 WAs (`vision-creation` → `goal-definition` → `capability-creation` → `feature-design`).
- **Cadena corta** (proyecto maduro + gap): humano pide feature en vault con visión/goals/capabilities pero sin capability que cubra esta feature → cadena de 2 WAs (`capability-creation` → `feature-design`).
- **Modo arbitraje** (feature cuestiona visión / cross-cutting): la feature contradice visión vigente o toca múltiples capabilities. Recepción NO propone cadena automática — presenta 3 opciones al humano:
  1. **Descartar el cambio.** Visión/grafo prevalece.
  2. **Modificar nivel superior y propagar.** WA de `vision-realignment` (skill later) o re-diseño de capabilities afectadas.
  3. **Documentar excepción consciente.** Cross-cutting feature documentada explícitamente con `coherence-exception` declarado en frontmatter + ADR breve.

## Protocolo de pivot de un WA mid-flight

**Cuándo aplica.** Durante la ejecución de un WA emerge insight que invalida el approach actual: el humano (o el orquestador en su filtro propio) detecta que el plan está mal planteado y conviene refactorizarlo en lugar de continuar (Cagan principio give-and-take aplicado al meta-nivel: cambiar de approach mid-flight es señal de equipo fuerte, no de fracaso).

Pivot ≠ abandono. Pivot = decisión consciente de cambiar el contenedor de trabajo, preservando la trazabilidad de lo aprendido durante el approach descartado.

**Cómo detectarlo (orquestador típicamente PO).** Señales recurrentes:

- Un step se atasca porque el template asumido no encaja con el contexto real (síntoma: necesidad de improvisar campos del frontmatter de forma sistemática).
- El humano explicita el pivot (*"esto no, mejor de otra forma"*).
- Un asesor levanta flag en scope-scan post-step que invalida la `objective` del WA.
- Drift acumulado entre lo planeado y lo producido — los steps ya completados no soportan los pendientes.

Si emerge una de estas señales: pausa, declara la decisión al humano, ejecuta el protocolo.

**Los 7 pasos canónicos del pivot.**

1. **Anuncia el pivot al humano y captura la razón.** El orquestador escribe en el chat: *"Detecto que el approach actual del WA-NNN no encaja porque [razón concreta]. Propongo pivotar a [nuevo approach] vía WA-MMM. Razón: [resumen]. ¿Procedo?"*. Espera confirmación humana antes de continuar.

2. **Marca el WA actual como `aborted`.** Edita el frontmatter:
   - `status: active` → `status: aborted`.
   - Añade `aborted-at: <ISO datetime>`.
   - Añade `aborted-reason: "<razón del pivot capturada en paso 1>"`.
   - Opcionalmente añade `superseded-by: wa-MMM` (rellenar tras crear el successor en paso 6).

3. **Marca los steps con trabajo parcial como `aborted` y preserva su output.** Para cada step con trabajo iniciado pero no completado:
   - `status: in-progress` → `status: aborted`.
   - Añade `aborted-at: <ISO datetime>`.
   - Añade `partial-output: "<descripción del trabajo parcial + paths>"` para preservar lo producido. El trabajo parcial no se borra del vault — queda accesible para el WA successor.

4. **Marca los nodos huérfanos producidos en steps parciales como `aborted-reference`.** Si un step parcial produjo discovery docs, drafts de spec, research notes o cualquier nodo del vault con `status: draft` que el WA contenedor iba a transicionar a `active` (o equivalente) al `/verify`, transicionalos manualmente a `status: aborted-reference`. Documenta brevemente en el cuerpo del archivo el contexto del pivot. Estos nodos NO entran en queries de nodos `active` ni en el backlog — son referencia auditable, no operativos.

5. **Mueve el WA al `archive/`.** Desde `vault/shared/sessions/active/wa-NNN.md` a `vault/shared/sessions/archive/wa-NNN.md`. Esto saca el WA del `/status` activo. El archive preserva la trazabilidad histórica del approach abortado — qué se intentó, por qué no funcionó, qué se aprendió.

6. **Crea el WA successor con `supersedes: wa-NNN`.** Drafta el WA nuevo siguiendo el protocolo normal (Modo 1 paso 8 del PO). Añade al frontmatter:
   - `supersedes: wa-NNN` (referencia al WA abortado).
   - `supersede-reason: "<razón del pivot, alineada con `aborted-reason` del WA original>"`.
   - Opcionalmente `scope-scan-heritage: true` si los flags del scope-scan del WA original siguen aplicando (evita re-invocar 5 asesores para confirmar flags ya consolidados — decisión PO con criterio Gap 6).
   - El cuerpo del WA successor debe ser **autocontenido** (regla de autocontención de `CLAUDE.md` raíz): reproduce in extenso el contexto relevante del WA abortado, no solo lo referencia.
   - Vuelve al frontmatter del WA abortado y rellena `superseded-by: wa-MMM` (cierra el grafo bidireccional).

7. **Handoff verbal al humano.** *"Pivot completado. WA-NNN archivado en `vault/shared/sessions/archive/wa-NNN.md` con `status: aborted`, razón documentada, trabajo parcial preservado. WA-MMM activo en `vault/shared/sessions/active/wa-MMM.md`, supersedes WA-NNN, listo para arrancar step-1."*

**Anti-patrón a evitar.** Iniciar el WA successor antes de cerrar el WA abortado, o continuar el WA abortado en paralelo al successor. Los dos WAs deben tener relación `supersedes`/`superseded-by` y solo el successor debe estar `active`. Mezclar ambos rompe el `/status` y la auditabilidad.

**Cuándo NO procede pivot.** Si la duda es un detalle resoluble dentro de un step (Cagan give-and-take normal: invocar a un asesor mid-step), no pivotes el WA. El pivot es para refactorizar el contenedor entero del trabajo, no para resolver dudas operativas. Si dudas, opta por NO pivotar y resuelve dentro del WA.

**Fundamento bibliográfico.** Cagan, *Inspired* — *"strong product teams change their approach when evidence demands it; weak teams march on with the original plan and call it 'discipline'"*. Pivotar es disciplina aplicada al meta-nivel del proceso. Nygard, *Documenting Architecture Decisions* — trazabilidad de decisiones tomadas (también las decisiones de proceso, no solo las arquitectónicas): el WA abortado en `archive/` con `aborted-reason` es el ADR informal del pivot.

## Patrón colaborativo dentro del WA (Cagan principio 2)

El modelo de **Cagan en *Inspired*** (principio 2 — *"Products are defined and designed collaboratively, rather than sequentially"*) materializa en SEM-IA via tres mecanismos:

1. **Scope-scan flat parallel multi-rol al crear WA** — los 6 asesores miran la propuesta en paralelo desde su ángulo. Discovery colaborativa antes de comprometer scope.
2. **Subagente vía Task tool durante step active-role** — el rol que conduce su step puede invocar a otros roles mid-trabajo. **Esto es el "give and take" puro de Cagan: encouraged, no excepcional.**
3. **Post-step scope-scan flat parallel** — los 5 asesores restantes auditan output recién producido. Captura drift bottom-up dentro de un step de delay.

**Ejemplos canónicos de give-and-take mid-step:**
- **PO durante decomposition** invoca a Designer (sanity check de usabilidad del flow propuesto), Architect (coupling check temprano), Security (early flag), Business-analyst (compliance flag).
- **Architect escribiendo ADR** invoca a Security (decisión toca cripto/auth), Business-analyst (decisión toca pricing/contratos/licensing).
- **Designer haciendo usability review** invoca a PO (validar story / persona target), Business-analyst (compliance accessibility — WCAG legal).
- **PO derivando capability** (lado estratégico) invoca a Architect (viability preview), Business-analyst (modelo de negocio implícito), Designer (usability implícita).

**Esto evita el waterfall**: cada custodio toca el WA en múltiples checkpoints (creation + mid-step + post-step + verify), no espera su turno secuencial. Los steps formales del WA son la **producción** (cada artefacto tiene custodio claro), pero la **discovery** es siempre paralela y colaborativa.

**Cuándo invocar subagente mid-step**: cuando durante tu step emerge una pregunta relevante a otro dominio. Mejor descubrir gaps temprano (mid-step de PO) que tarde (post-step de Architect, requeriría rework).

**Coste**: invocar a 1-2 subagents por step suma ~$0.30-0.50 al WA. Despreciable vs el coste de rework por gap detectado tarde.

## Dual Track — Discovery + Delivery en paralelo (Cagan/Patton)

SEM-IA materializa el modelo **Dual Track Agile** canónico: dos tracks paralelos donde Discovery valida QUÉ construir y Delivery construye CÓMO.

- **Discovery track** = WAs de fases `discovery` (vision, goals, capabilities) + `design` (feature-design, adr, threat-model). Aborda los 4 risks de Cagan: value, usability, viability technical, business viability.
- **Delivery track** = WAs de fase `implementation` (feature-build, bugfix, refactor). Aborda QAs de Bass: functionality, scalability, reliability, performance, maintainability.
- **Backlog** = nodos del vault con `status: ready-for-implementation`. Puente persistente entre tracks.

**Los dos tracks corren en paralelo en proyectos maduros**: mientras el equipo construye `feature-N` (WA `feature-build` activo en Delivery), Discovery puede estar validando `feature-N+1` (WA `feature-design` activo simultáneamente). El motor permite múltiples WAs activos sin restricción — el humano abre las sesiones dedicadas correspondientes (ej. `npm run dev` para feature-N + `npm run po` para feature-N+1 en otra terminal).

**Antipatrón a evitar** (Cagan): solo Delivery (waterfall disfrazado de agile) o solo Discovery (parálisis por análisis). El equipo fuerte mantiene ambos tracks corriendo. SEM-IA no fuerza el ratio entre tracks pero lo **hace visible y auditable** vía `/status`: cuántos WAs en cada fase, tamaño del backlog, gaps emergentes.

## Campo `derived-from` (opcional, futuro)

Campo opcional en frontmatter de nodos cuando se quiere declarar manualmente que un nodo se derivó de artefactos pre-existentes (ej. paths de código). Hoy no se usa activamente; es un placeholder para una capability futura **"Adopción de proyecto pre-existente"** (ver "Pendientes" en README) que automatizará la derivación retroactiva del grafo desde código + docs.

```yaml
derived-from:
  - src/auth/google-oauth.ts
  - src/auth/__tests__/google-oauth.test.ts
  - README.md (sección "Auth providers")
```

Auditabilidad: si los artefactos referenciados cambian significativamente, el nodo es candidato a re-derivación. Nodos creados en modo conversacional (Vía 1) NO tienen `derived-from`.

## Heurística de clasificación outcome-type

| Keywords del humano | outcome-type | Fase |
|---|---|---|
| "review de usabilidad", "audit accessibility", "audit WCAG" | (trigger Designer en scope-scan; sin template dedicado hoy — se invoca como step de feature-design o ad-hoc) | design |
| "review de compliance", "GDPR / PCI / HIPAA review", "impact comercial", "review pricing" | (trigger Business-analyst en scope-scan; sin template dedicado hoy — se invoca como step de feature-design o ad-hoc) | design |
| "definir visión", "crear vision statement", "redefinir visión" | `vision-creation` | discovery |
| "definir capability", "añadir habilidad de", "crear cap-N" | `capability-creation` (`mode: single`, default) | discovery |
| "crear el catálogo de capabilities", "varias capabilities a la vez", "definir el conjunto de habilidades para el dominio X" | `capability-creation` (`mode: batch`) | discovery |
| "extraer capabilities del bootstrap", "mapear el código existente a capabilities", "reverse-engineering del catálogo", "adoptar proyecto pre-existente" | `capability-creation` (`mode: reverse-engineering`) | discovery |
| "definir goal", "OKR para", "objetivo de" | `goal-definition` | discovery |
| "diseñar feature de Y", "decomponer capability X", "spec para feature Z", "definir AC" | `feature-design` (`mode: single`, default) | design |
| "diseñar features de dominio cross-cutting", "decomponer varias capabilities a la vez en features", "spec batch del dominio X" | `feature-design` (`mode: batch`) | design |
| "extraer features del bootstrap", "mapear el código existente a features", "reverse-engineering del catálogo de features", "adoptar features de proyecto pre-existente" | `feature-design` (`mode: reverse-engineering`) | design |
| "decidir entre A y B", "elegir tecnología", "ADR para X" | `adr` | design |
| "threat-model de", "review de seguridad de feature" | `threat-model` | design |
| "implementar feature-N", "construir feature ya specificada", "build feature-N del backlog" | `feature-build` | implementation |
| "arreglar bug en X", "fix de Y", "corrige error" | `bugfix` | implementation |
| "refactorizar X", "reorganizar Y", "limpiar deuda en Z" | `refactor` | implementation |
| "cambiar pipeline CI", "modificar workflow GitHub Actions" | `pipeline-change` | operations |
| "decidir infra para", "elegir cloud provider", "rediseñar deployment" | `infra-decision` | operations |
| "instrumentar métricas", "añadir alerta", "dashboard para" | `observability-instrument` | operations |
| "actualizar doc", "modificar README", "ajustar texto" | `doc-edit` | meta |
| "fix typo", "cambio de copy", "ajuste de config menor" | `trivial` | meta |
| "implementar X end-to-end" (sin spec previa) | **AMBIGUO** → recepción propone partir en `feature-design` + `feature-build` | — |
| Caso ambiguo | Recepción **pregunta al humano** cuál aplica | — |

**Nota sobre pivots mid-WA**: si durante un WA activo el humano expresa *"esto no, mejor de otra forma"* (o equivalente — *"esto es un petardo"*, *"esto no escala"*), esto **NO es un nuevo outcome-type a clasificar**. Es disparador de la sección "Protocolo de pivot de un WA mid-flight" (arriba en este mismo archivo). El orquestador del WA en curso pausa, declara el pivot al humano, y ejecuta los 7 pasos canónicos del protocolo. No se abre un WA `doc-edit` ni `refactor` para gestionar el pivot — el pivot se ejecuta sobre el WA mismo. Solo cuando el WA successor está creado se vuelve a la clasificación normal de outcome-types.

## Templates por fase

```yaml
phases:

  # =========================================================================
  # DISCOVERY — Descubrir qué construir y por qué
  # =========================================================================
  discovery:
    description: "Descubrir qué construir y por qué"
    produces: "nodos estratégicos (visión, goals, capabilities)"
    templates:

      vision-creation:
        description: "Crear o redefinir la visión del producto (post-inception)"
        produces: "vault/product-owner/strategy/vision.md"
        skill-invoked: "vision-quality-check (validación)"
        default-steps:
          - id: step-1
            role: product-owner
            phase: discovery
            purpose: "Facilitar definición de visión (Sinek + Cagan + Rumelt + JTBD)"
            expected-output: "vault/product-owner/strategy/vision.md"
        on-close:
          - "vault/product-owner/strategy/vision.md: draft → active"

      capability-creation:
        description: "Crear capability(es) en el subgrafo estratégico. Soporta tres modos: `single` (default, una capability nueva top-down desde goal), `batch` (varias capabilities nuevas en un mismo WA, ej. discovery cross-cutting de un dominio), `reverse-engineering` (bottom-up: extraer N capabilities desde piezas pre-existentes — bootstrap construido, código legacy, etc.)."
        produces: "vault/product-owner/strategy/<capability-id>.md (uno o varios según `mode`)"
        skill-invoked: "capability-derivation + capability-quality-check"
        collaborative-pattern: "Patrón Cagan (give-and-take): durante step-1, el PO debería invocar a Architect/Designer/Business-analyst como subagentes mid-step si la(s) capability(es) sugieren implicaciones técnicas/usabilidad/business significativas."
        mode-flag:
          field: "mode"
          values: ["single", "batch", "reverse-engineering"]
          default: "single"
          rationale: |
            El template original asumía `single`. Pero SEM-IA es self-hosting y casos reales emergen:
            - `batch`: el humano arranca una capability nueva y mid-discovery emergen 2-3 más en el mismo dominio. Mejor procesarlas en un WA cohesivo que multiplicar WAs.
            - `reverse-engineering`: caso bootstrap o adopción de proyecto pre-existente. El catálogo no se deriva top-down desde goals — se extrae bottom-up desde código, docs y discovery previos, mapeando después a goals.
            Un único template con flag `mode` evita duplicar workflows casi-idénticos (Ousterhout: deep modules — interfaz simple con variantes internas). El PO declara el `mode` al draftear el WA basándose en el contexto del scope-scan.
        default-steps:
          # Steps base (aplican a los 3 modos con adaptaciones)
          - id: step-1
            role: product-owner
            phase: discovery
            purpose: "(mode: single) Definir capability + alineación con goals + cita bibliográfica. (mode: batch) Inventario de capabilities candidatas en el dominio + criterio de inclusión. (mode: reverse-engineering) Inventario de piezas pre-existentes a mapear + criterio de extracción."
            expected-output: "(single) vault/product-owner/strategy/cap-N-slug.md. (batch/reverse-engineering) vault/product-owner/discovery/cap-batch-inventory-<topic>.md con lista cerrada de N capabilities a crear."
          - id: step-2
            role: product-owner
            phase: discovery
            purpose: "(mode: single) Identificar features candidatas (preview, no decomposition completa). (mode: batch/reverse-engineering) Escribir los N capability files siguiendo el template del capability file de la skill capability-derivation."
            expected-output: "(single) Sección 'features candidatas' actualizada en cap-N. (batch/reverse-engineering) N archivos en vault/product-owner/strategy/cap-N-slug.md, uno por capability del inventario."
          - id: step-3
            role: architect
            phase: design
            purpose: "Viability técnica preview (capability-viability-review: Bass QAs + tactics). En mode batch/reverse-engineering: review consolidado de las N capabilities producidas, no N reviews separados."
            expected-output: "(single) vault/architect/research/cap-N-viability.md. (batch/reverse-engineering) vault/architect/research/cap-batch-<topic>-viability.md consolidado."
            optional: true
            condition: "technical en dimensions-affected"
          - id: step-4
            role: designer
            phase: design
            purpose: "Usability preview (Cagan usability-risk): patrones de interacción que la(s) capability(es) sugieren. En mode batch/reverse-engineering: review consolidado."
            expected-output: "(single) vault/designer/audits/cap-N-usability-preview.md. (batch/reverse-engineering) vault/designer/audits/cap-batch-<topic>-usability-preview.md consolidado."
            optional: true
            condition: "usability en dimensions-affected"
          - id: step-5
            role: business-analyst
            phase: design
            purpose: "Business viability preview (Cagan business-viability-risk): impact en pricing/billing/compliance/GTM. En mode batch/reverse-engineering: review consolidado."
            expected-output: "(single) vault/business-analyst/audits/cap-N-business-preview.md. (batch/reverse-engineering) vault/business-analyst/audits/cap-batch-<topic>-business-preview.md consolidado."
            optional: true
            condition: "business en dimensions-affected"
          - id: step-6
            role: qa
            phase: design
            purpose: "(mode: batch/reverse-engineering solo) Verificabilidad-review consolidada de las N capabilities: ¿cada una tiene criterio observable para futuros /verify? ¿el catálogo es internamente consistente (no solapamientos no declarados)?"
            expected-output: "vault/qa/reports/cap-batch-<topic>-verifiability.md"
            optional: true
            condition: "mode == batch o mode == reverse-engineering"
        on-close:
          # Modo single
          - "(mode: single) vault/product-owner/strategy/cap-N-slug.md: draft → active"
          - "(mode: single) vault/architect/research/cap-N-viability.md: draft → active (si existe)"
          - "(mode: single) vault/designer/audits/cap-N-usability-preview.md: draft → active (si existe)"
          - "(mode: single) vault/business-analyst/audits/cap-N-business-preview.md: draft → active (si existe)"
          # Modo batch / reverse-engineering
          - "(mode: batch o reverse-engineering) vault/product-owner/strategy/cap-N-slug.md × N: draft → active"
          - "(mode: batch o reverse-engineering) vault/product-owner/discovery/cap-batch-inventory-<topic>.md: draft → active"
          - "(mode: batch o reverse-engineering) vault/architect/research/cap-batch-<topic>-viability.md: draft → active (si existe)"
          - "(mode: batch o reverse-engineering) vault/designer/audits/cap-batch-<topic>-usability-preview.md: draft → active (si existe)"
          - "(mode: batch o reverse-engineering) vault/business-analyst/audits/cap-batch-<topic>-business-preview.md: draft → active (si existe)"
          - "(mode: batch o reverse-engineering) vault/qa/reports/cap-batch-<topic>-verifiability.md: draft → active (si existe)"

      goal-definition:
        description: "Definir goal nuevo bajo la visión"
        produces: "vault/product-owner/strategy/<goal-id>.md"
        skill-invoked: "goal-quality-check"
        default-steps:
          - id: step-1
            role: product-owner
            phase: discovery
            purpose: "Definir goal + tests Doerr/Doran + alineación con visión"
            expected-output: "vault/product-owner/strategy/goal-N-slug.md"
        on-close:
          - "vault/product-owner/strategy/goal-N-slug.md: draft → active"

  # =========================================================================
  # DESIGN — Definir cómo se construye lo descubierto
  # =========================================================================
  design:
    description: "Definir cómo se construye lo descubierto"
    produces: "nodos con status: ready-for-implementation (entran en backlog)"
    templates:

      feature-design:
        description: "Decomponer capability(es) en feature(s) + stories + examples + AC + spec Gherkin (entra al backlog). Soporta tres modos: `single` (default, una capability → varias features), `batch` (varias capabilities cross-cutting → features de un dominio en un mismo WA), `reverse-engineering` (bottom-up: extraer N features desde piezas pre-existentes — bootstrap construido, código legacy). Cubre los 4 risks de Cagan: value (PO), usability (Designer opt), viability technical (Architect opt), business viability (Business-analyst opt) + security (transversal opt) + quality (QA en mode batch/reverse-engineering)."
        consumes: "(mode: single) una capability del vault con status: active. (mode: batch) N capabilities cross-cutting con status: active. (mode: reverse-engineering) N capabilities con piezas reverse-engineerables del bootstrap."
        produces: "vault/product-owner/specs/<feature-id>.md + <story-id>.md + <spec-id>.md (specs Gherkin formales → status: ready-for-implementation al cierre)"
        skills-invoked: "feature-decomposition + spec-writing (que absorbe AC definition) + feature-quality-check"
        collaborative-pattern: "Patrón Cagan (give-and-take): durante step-1, el PO debería invocar a Designer/Architect/Security/Business-analyst como subagentes mid-step para sanity checks tempranos antes de cerrar la spec. Mejor descubrir gaps de usabilidad/viabilidad/compliance durante decomposition que después."
        mode-flag:
          field: "mode"
          values: ["single", "batch", "reverse-engineering"]
          default: "single"
          rationale: |
            El template original asumía `single` (paralelo a capability-creation antes de su Gap 3). Casos reales que motivan el mode-flag:
            - `batch`: varias capabilities cross-cutting cuyos features se descomponen en un WA cohesivo (ej. dominio "autenticación" con caps OAuth + Sessions + Password — features cruzadas).
            - `reverse-engineering`: caso bootstrap o adopción de proyecto pre-existente. El catálogo de features se extrae bottom-up desde bootstrap/código, mapeando después a capabilities operant.
            Mismos 3 valores que capability-creation = **uniformidad mode-flag entre templates batch-capables** (Ford fitness function del catálogo de workflows; Ousterhout deep modules — interfaz simple con variantes internas). NO se introduce un cuarto valor "reverse-engineering-batch" (lingüísticamente redundante — reverse-engineering ya implica batch al extraer N piezas).
            Incidentes formativos del patrón: WA-2026-05-12-004 (aborted, improvisó mode reverse-engineering-batch y produjo confusión de 5 niveles arquitectónicos por stop-too-early en espina dorsal) + WA-2026-05-13-005 (successor exitoso que aplicó el patrón con test mecánico Adzic SbE y produjo 14 features + 36 stories + 36 specs Gherkin formales).
            Pendiente: ADR meta-1 Nygard formal sobre la decisión de uniformidad mode-flag (Lote B Architect).
        default-steps:
          # Steps base (aplican a los 3 modos con adaptaciones)
          - id: step-1
            role: product-owner
            phase: design
            purpose: "(mode: single) Decomposition de 1 capability en features + stories + spec Gherkin formal aplicando feature-decomposition + spec-writing. (mode: batch) Inventario de features candidatas cross-cutting + criterio de granularidad declarado. (mode: reverse-engineering) Discovery doc bottom-up con reclasificación de piezas-bootstrap en 5 niveles arquitectónicos (features genuinas / ADRs latentes / protocolos / docs / artefactos) + test mecánico Adzic SbE como criterio anti stop-too-early."
            expected-output: "(single) vault/product-owner/specs/feature-N-slug.md + stories + specs Gherkin. (batch/reverse-engineering) vault/product-owner/discovery/<topic>-extraction-<date>.md con lista cerrada de features genuinas + tabla cobertura piezas × nivel arquitectónico."
          - id: step-2
            role: product-owner
            phase: design
            purpose: "(mode: single) — step-2 no aplica como bloque separado; integrado en step-1. (mode: batch/reverse-engineering) Escribir los N feature files + N stories + N specs Gherkin formales en vault/product-owner/specs/ aplicando feature-decomposition + spec-writing + feature-quality-check por feature. Recomendado sub-dividir en sub-pasos (step-2a..2N) por capability para auditoría granular y prevenir output bias (regla 13 PO)."
            expected-output: "(batch/reverse-engineering) N feature files + ~3-5 story files por feature + ~3-5 spec Gherkin files por feature, todos en vault/product-owner/specs/ con status: draft."
            optional: true
            condition: "mode == batch o mode == reverse-engineering"
          - id: step-3
            role: architect
            phase: design
            purpose: "Viability review + ADR si emerge decisión técnica significativa. (single) Per-feature review. (batch/reverse-engineering) Coupling-review consolidado cross-features + ADRs latentes confirmados + viability technical preview consolidado."
            expected-output: "(single) vault/architect/research/feature-N-architect-review.md (+ ADR opcional). (batch/reverse-engineering) vault/architect/research/<topic>-coupling-review.md consolidado."
            optional: true
            condition: "technical en dimensions-affected o flag de ADR del scope-scan"
          - id: step-4
            role: designer
            phase: design
            purpose: "Usability review (Nielsen + Cooper + Norman). (single) Per-feature. (batch/reverse-engineering) Review consolidado cross-features con dimension usability."
            expected-output: "(single) vault/designer/audits/feature-N-usability-review.md. (batch/reverse-engineering) vault/designer/audits/<topic>-usability-review.md consolidado."
            optional: true
            condition: "usability en dimensions-affected"
          - id: step-5
            role: security-officer
            phase: design
            purpose: "Threat-model + AC-S* trazables. (single) Per-feature. (batch/reverse-engineering) Threat-modeling preview consolidado cross-features con superficie security load-bearing (criterio honest-agent assumption — NO checkbox security)."
            expected-output: "(single) vault/security-officer/audits/feature-N-threat-model.md. (batch/reverse-engineering) vault/security-officer/audits/<topic>-security-preview.md consolidado."
            optional: true
            condition: "security en dimensions-affected"
          - id: step-6
            role: business-analyst
            phase: design
            purpose: "Business viability review (Moore + Osterwalder + compliance). (single) Per-feature. (batch/reverse-engineering) Review consolidado cross-features con dimension business."
            expected-output: "(single) vault/business-analyst/audits/feature-N-business-review.md. (batch/reverse-engineering) vault/business-analyst/audits/<topic>-business-review.md consolidado."
            optional: true
            condition: "business en dimensions-affected"
          - id: step-7
            role: qa
            phase: design
            purpose: "(mode: batch/reverse-engineering solo) Verificabilidad-review consolidada cross-features: ¿cada AC tiene identificador único + 'verificable vía'? ¿cobertura piezas × nivel arquitectónico sin gaps? ¿coherencia interna del catálogo sin solapamientos no declarados? ¿cero anti-patrón features-as-output-blind? ¿granularidad INVEST `S` uniforme?"
            expected-output: "vault/qa/reports/<topic>-verifiability.md"
            optional: true
            condition: "mode == batch o mode == reverse-engineering"
        on-close:
          # Modo single
          - "(mode: single) vault/product-owner/specs/feature-N-slug.md: draft → ready-for-implementation"
          - "(mode: single) vault/product-owner/specs/story-N-X.md: draft → active (si existen como nodos separados)"
          - "(mode: single) vault/product-owner/specs/spec-N-X.md: draft → ready-for-implementation"
          - "(mode: single) vault/architect/research/feature-N-architect-review.md: draft → active (si existe)"
          - "(mode: single) vault/architect/adrs/adr-NNN.md: proposed → accepted (si emergió ADR)"
          - "(mode: single) vault/designer/audits/feature-N-usability-review.md: draft → active (si existe)"
          - "(mode: single) vault/security-officer/audits/feature-N-threat-model.md: draft → active (si existe)"
          - "(mode: single) vault/business-analyst/audits/feature-N-business-review.md: draft → active (si existe)"
          # Modo batch / reverse-engineering
          - "(mode: batch o reverse-engineering) vault/product-owner/discovery/<topic>-extraction-<date>.md: draft → active"
          - "(mode: batch o reverse-engineering) vault/product-owner/specs/feature-*.md × N: draft → active"
          - "(mode: batch o reverse-engineering) vault/product-owner/specs/story-*.md × N: draft → active"
          - "(mode: batch o reverse-engineering) vault/product-owner/specs/spec-*.md × N (Gherkin formales): draft → ready-for-implementation"
          - "(mode: batch o reverse-engineering) vault/architect/research/<topic>-coupling-review.md: draft → active (si existe)"
          - "(mode: batch o reverse-engineering) vault/designer/audits/<topic>-usability-review.md: draft → active (si existe)"
          - "(mode: batch o reverse-engineering) vault/security-officer/audits/<topic>-security-preview.md: draft → active (si existe)"
          - "(mode: batch o reverse-engineering) vault/business-analyst/audits/<topic>-business-review.md: draft → active (si existe)"
          - "(mode: batch o reverse-engineering) vault/qa/reports/<topic>-verifiability.md: draft → active (si existe)"

      adr:
        description: "Decisión arquitectónica que requiere ADR formal"
        produces: "vault/architect/adrs/<adr-id>.md (status: accepted al cierre)"
        skill-invoked: "adr-writing"
        default-steps:
          - id: step-1
            role: architect
            phase: design
            purpose: "Research técnico + alternativas + tradeoffs"
            expected-output: "vault/architect/research/<topic>-research.md"
          - id: step-2
            role: architect
            phase: design
            purpose: "Escribir ADR (formato Nygard: Context + Decision + Consequences + Alternatives Considered)"
            expected-output: "vault/architect/adrs/adr-NNN-slug.md"
          - id: step-3
            role: security-officer
            phase: design
            purpose: "Review de seguridad de la decisión"
            expected-output: "vault/security-officer/audits/<adr-id>-review.md"
            optional: true
            condition: "security en dimensions-affected"
        on-close:
          - "vault/architect/adrs/adr-NNN-slug.md: proposed → accepted"
          - "vault/architect/research/<topic>-research.md: draft → active"
          - "vault/security-officer/audits/<adr-id>-review.md: draft → active (si existe)"

      threat-model:
        description: "Threat-model formal de feature sensible"
        consumes: "spec o feature del vault"
        produces: "vault/security-officer/audits/<id>-threat-model.md"
        default-steps:
          - id: step-1
            role: security-officer
            phase: design
            purpose: "Threat modeling completo + AC de seguridad (AC-S*) añadidos a la spec consumida"
            expected-output: "vault/security-officer/audits/<id>-threat-model.md"
        on-close:
          - "vault/security-officer/audits/<id>-threat-model.md: draft → active"

  # =========================================================================
  # IMPLEMENTATION — Construir lo diseñado (consume del backlog)
  # =========================================================================
  implementation:
    description: "Construir lo diseñado (consume nodos del backlog)"
    consumes: "nodos del vault con status: ready-for-implementation"
    produces: "código + tests"
    templates:

      feature-build:
        description: "Implementar spec del backlog"
        consumes: "vault/product-owner/specs/<feature-id>.md con status: ready-for-implementation"
        produces: "src/ + tests/ (referenciados vía // @sem-ia: <feature-id>)"
        precondition: "El nodo referenciado debe existir y tener status: ready-for-implementation"
        default-steps:
          - id: step-1
            role: developer
            phase: implementation
            purpose: "Implementación según spec + ADRs aplicables + threat-model si hay"
            expected-output: "Código en src/ + tests unitarios (@sem-ia + @ac-coverage)"
          - id: step-2
            role: qa
            phase: implementation
            purpose: "Cobertura E2E + edge cases + AC trazables (incluyendo AC-S* de threat-model)"
            expected-output: "Tests E2E + report en vault/qa/reports/feature-N-coverage.md"
        on-close:
          - "vault/product-owner/specs/<feature-id>.md: ready-for-implementation → implemented"
          - "vault/qa/reports/feature-N-coverage.md: draft → active"

      bugfix:
        description: "Reparar comportamiento incorrecto de una feature existente"
        produces: "src/ + tests + learnings"
        default-steps:
          - id: step-1
            role: developer
            phase: discovery
            purpose: "Reproducir + diagnose + identificar root cause"
            expected-output: "Issue analysis (puede ser comentario en código o nota en gotchas)"
          - id: step-2
            role: developer
            phase: implementation
            purpose: "Fix + tests que cubren el bug"
            expected-output: "Cambios en src/ + tests adicionales"
          - id: step-3
            role: qa
            phase: verification
            purpose: "Regression test + verificar que el fix no rompe AC existentes"
            expected-output: "Tests de no-regresión + report en vault/qa/reports/"
        on-close:
          - "vault/qa/reports/<bugfix-id>.md: draft → active (si existe report)"

      refactor:
        description: "Reorganización de código sin cambio funcional"
        produces: "src/ refactorizado (+ ADR si cross-cutting)"
        default-steps:
          - id: step-1
            role: architect
            phase: discovery
            purpose: "Proposal + impact assessment + identificar acoplamientos a romper"
            expected-output: "vault/architect/research/<topic>-refactor-proposal.md"
          - id: step-2
            role: architect
            phase: design
            purpose: "ADR si el refactor es cross-cutting o redefine boundaries"
            expected-output: "vault/architect/adrs/adr-NNN.md"
            optional: true
            condition: "cross-cutting o redefine boundaries entre módulos"
          - id: step-3
            role: developer
            phase: implementation
            purpose: "Implementar refactor preservando comportamiento"
            expected-output: "Cambios en src/"
          - id: step-4
            role: qa
            phase: implementation
            purpose: "Tests no-regresión (asegurar comportamiento idéntico)"
            expected-output: "Tests + report en vault/qa/reports/"
        on-close:
          - "vault/architect/research/<topic>-refactor-proposal.md: draft → active"
          - "vault/architect/adrs/adr-NNN.md: proposed → accepted (si existe)"
          - "vault/qa/reports/<refactor-id>.md: draft → active"

  # =========================================================================
  # OPERATIONS — Desplegar y operar
  # =========================================================================
  operations:
    description: "Desplegar y operar"
    produces: "configs + ADRs operativos"
    templates:

      pipeline-change:
        description: "Cambio significativo de CI/CD pipeline"
        produces: "configs CI (.github/workflows/, etc.) + ADR operativo si cross-cutting"
        default-steps:
          - id: step-1
            role: devops
            phase: design
            purpose: "Diseño del cambio + estrategia (blue/green, canary, etc.) + rollback plan"
            expected-output: "vault/architect/research/pipeline-N-design.md"
          - id: step-2
            role: devops
            phase: implementation
            purpose: "Implementar pipeline + métricas + alertas"
            expected-output: "Cambios en .github/workflows/ o equivalente"
          - id: step-3
            role: security-officer
            phase: design
            purpose: "Review de seguridad del pipeline (secrets, permisos, supply chain)"
            expected-output: "vault/security-officer/audits/pipeline-N-review.md"
            optional: true
            condition: "security en dimensions-affected o el pipeline maneja credenciales"
        on-close:
          - "vault/architect/research/pipeline-N-design.md: draft → active"
          - "vault/security-officer/audits/pipeline-N-review.md: draft → active (si existe)"

      infra-decision:
        description: "Decisión de infraestructura significativa (cloud provider, arquitectura de deployment, etc.)"
        produces: "ADR operativo + configs de infra"
        default-steps:
          - id: step-1
            role: devops
            phase: discovery
            purpose: "Research + alternativas + análisis de coste/SLO"
            expected-output: "vault/architect/research/<topic>-infra-research.md"
          - id: step-2
            role: architect
            phase: design
            purpose: "Escribir ADR conjunto (devops + architect)"
            expected-output: "vault/architect/adrs/adr-NNN-infra.md"
        on-close:
          - "vault/architect/research/<topic>-infra-research.md: draft → active"
          - "vault/architect/adrs/adr-NNN-infra.md: proposed → accepted"

      observability-instrument:
        description: "Añadir métricas/alertas/trazas a una feature implementada"
        consumes: "feature implementada (status: implemented)"
        produces: "configs de observabilidad + dashboard"
        default-steps:
          - id: step-1
            role: devops
            phase: implementation
            purpose: "Instrumentar + dashboard + alertas oncall"
            expected-output: "Configs de instrumentación + dashboard"
        # Sin on-close específico — los configs no son nodos del grafo con lifecycle.

  # =========================================================================
  # META — Cambios fuera del SDLC nuclear
  # =========================================================================
  meta:
    description: "Cambios fuera del SDLC nuclear (docs, triviales)"
    templates:

      doc-edit:
        description: "Edición de documento existente (clarificación, actualización)"
        default-steps:
          - id: step-1
            role: <inferred-from-path>
            phase: implementation
            purpose: "Edit"
            expected-output: "Cambios en el documento"
        notes: |
          El `active-role` se infiere por la ubicación del documento:
          - vault/product-owner/strategy/** → product-owner
          - vault/product-owner/** → product-owner
          - vault/architect/** → architect
          - vault/shared/governance/** → varía según el archivo (ver role-catalog.md)
          - README.md, CLAUDE.md → recepción puede editarlos directamente
        # Sin on-close específico — no transiciona status del documento (los docs no tienen lifecycle estandarizado).

      trivial:
        description: "Cambio trivial (typo, copy fix, config menor)"
        default-steps: []
        notes: |
          Para cambios triviales, recepción lo edita directamente sin crear WA formal.
          Si no estás seguro de si es trivial, opta por crear el WA con el outcome-type apropiado.
```

## Backlog — emergente, no estructural

El "backlog" en SEM-IA **no es una entidad persistente**. Es una **query sobre el vault**:

```
backlog = nodos con frontmatter `status: ready-for-implementation`
```

Estos nodos son output de WAs cerrados de fase `design` (típicamente specs producidas por `feature-design`). El comando `/status` muestra una sección "Backlog" derivada de esta query.

**Estados canónicos del nodo durante el lifecycle:**

| Status | Significado | Quién lo setea |
|---|---|---|
| `draft` | Nodo en construcción durante un WA activo (estado inicial que las skills producen) | Skill al crear el nodo |
| `proposed` | ADR en construcción (convención Nygard) | `adr-writing` skill |
| `active` | Nodo completado y verificado (visión, goal, capability, review, audit, etc.) | Recepción al `/verify` vía `on-close` |
| `accepted` | ADR aprobado | Recepción al `/verify` vía `on-close` |
| `ready-for-implementation` | Spec/feature en backlog esperando WA de implementation | Recepción al `/verify` del WA `feature-design` vía `on-close` |
| `in-implementation` | Hay un WA `feature-build` activo consumiéndolo | Step 1 del WA `feature-build` (developer) lo marca al consumir |
| `implemented` | Feature implementada y verificada | Recepción al `/verify` del WA `feature-build` vía `on-close` |
| `superseded` | ADR reemplazado por otro ADR | Modificación manual + `superseded-by` |
| `deprecated` | Nodo ya no aplica por decisión consciente del producto | Decisión consciente vía WA apropiado |
| `aborted` | WA (o step de WA) terminado antes de `/verify` por pivot consciente del approach. Preserva `aborted-at` + `aborted-reason`; opcionalmente `superseded-by` apuntando al WA successor. Aplicable a WA completo y a steps con trabajo parcial (preservados vía `partial-output`). | PO/orquestador al ejecutar Protocolo de pivot mid-flight |
| `aborted-reference` | Nodo producido en step parcial de un WA `aborted`; preservado como referencia auditable pero no operativo (no entra en backlog ni en queries de nodos `active`). Distinto de `deprecated`: aquí la causa es el pivot del WA contenedor, no obsolescencia semántica del nodo. | PO/orquestador al ejecutar Protocolo de pivot mid-flight |

**Sobre `aborted` / `aborted-reference`**: ver sección "Protocolo de pivot de un WA mid-flight" arriba. Estos estados modelan el caso en que el approach del WA se demuestra incorrecto mid-flight y se decide refactorizar el plan (Cagan principio give-and-take aplicado al meta-nivel). La distinción semántica respecto a `deprecated` preserva trazabilidad auditable: `deprecated` = decisión de producto sobre obsolescencia del nodo; `aborted*` = decisión de proceso sobre refactorización del contenedor de trabajo.

## Extensión por adopters

Cada proyecto añade templates según su dominio. La estructura es siempre la misma: `phase` + `outcome-type` + `produces` + opcionalmente `consumes` + `default-steps` + `on-close`. Adopters pueden también **redefinir las fases** si su SDLC tiene fases diferentes (ej. equipos SAFe con `program-increment`, equipos lean con `experiment`).

### Ejemplos de templates de proyectos custom

**Proyecto DeFi (fase `design`, outcome-type `tokenomics-change`):**

```yaml
tokenomics-change:
  description: "Modificación de mecanismo de incentivos del protocolo"
  produces: "vault/architect/adrs/<adr-id>-tokenomics.md (status: accepted al cierre)"
  default-steps:
    - {role: tokenomics-designer, phase: discovery, purpose: "Análisis económico + game theory"}
    - {role: quant,               phase: design,    purpose: "Simulación + risk model"}
    - {role: security-officer,    phase: design,    purpose: "Auditoría de exploits potenciales"}
  on-close:
    - "vault/architect/adrs/<adr-id>-tokenomics.md: proposed → accepted"
```

**Proyecto con database (fase `operations`, outcome-type `database-migration`):**

```yaml
database-migration:
  description: "Migración de schema o datos en producción"
  produces: "scripts SQL + ADR operativo"
  default-steps:
    - {role: dba,                 phase: discovery,      purpose: "Plan de migración + rollback"}
    - {role: architect,           phase: design,         purpose: "ADR si afecta a otros sistemas", optional: true}
    - {role: security-officer,    phase: design,         purpose: "Review de exposición de datos"}
    - {role: developer,           phase: implementation, purpose: "Migration scripts"}
    - {role: qa,                  phase: verification,   purpose: "Test rollback + integridad de datos"}
  on-close:
    - "vault/architect/adrs/<adr-id>-migration.md: proposed → accepted (si existe)"
```

## Reglas de extensión

1. Cada nuevo template añade keywords a la heurística de clasificación.
2. Los `optional` steps deben tener `condition` clara y evaluable contra scope-scan output.
3. Los roles referenciados deben existir en `role-catalog.md`.
4. Las `phase` siguen las 5 estándar: `discovery | design | implementation | operations | meta`. Adopters pueden añadir más si su SDLC lo requiere (documentándolas).
5. Templates de fase `design` setean transición de status apropiada en su `on-close` (típicamente `draft → ready-for-implementation` para nodos que entran al backlog, o `draft → active` para nodos que no se "implementan" después como vision/goal/capability/review).
6. Templates de fase `implementation` declaran `consumes` y verifican precondición (nodo existe con status correcto) antes de empezar. Su `on-close` típicamente transiciona el nodo consumido a `implemented`.

## Diferencia con `verification-matrix.md`

- **`workflows.md`** (este archivo): templates de **steps a ejecutar** durante el WA, indexados por fase. Forward-looking.
- **`verification-matrix.md`**: guía orientativa de **dimensiones típicas** por tipo de operación, usada al hacer scope-scan. Backward-looking ayuda mnemotécnica.

Ambos se complementan. `workflows.md` define el flujo de trabajo; `verification-matrix.md` ayuda a recordar qué dimensiones suelen tocarse.
