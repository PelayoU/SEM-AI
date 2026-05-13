---
type: research
id: spine-bootstrap-coupling-review
title: "Coupling-review consolidado de 14 features bootstrap + ADRs latentes confirmados · WA-2026-05-13-005 step-3"
status: active  # transitado por /verify del WA-2026-05-13-005 el 2026-05-13T08:30+02:00
created: 2026-05-13
author: architect
related-wa: wa-2026-05-13-005
related-discovery: spine-bootstrap-2026-05-13
related-capabilities:
  - cap-01-grafo-declarativo-persistente
  - cap-02-multirol-agentes-homologos
  - cap-04-verificacion-multirol-cruzada
  - cap-06-visibilidad-operativa
  - cap-07-inception-greenfield
  - cap-10-articulacion-publica
related-features:
  - feature-001-vault-role-first
  - feature-010-entry-point-por-rol
  - feature-018-slash-scope-scan
  - feature-019-slash-verify
  - feature-032-slash-status
  - feature-033-slash-wa
  - feature-034-slash-sessions
  - feature-035-ritual-inicio-po
  - feature-036-orientacion-rol
  - feature-038-po-modo-1
  - feature-039-cadena-was-greenfield
  - feature-041-readme-onboarding
  - feature-044-glosario-publico
  - feature-045-ruta-lectura-audiencia
dimensions-affected: [technical]
citas-bibliograficas:
  - "Ford, Parsons, Kua — Building Evolutionary Architectures (appropriate coupling, fitness functions, evolvability)"
  - "Bass, Clements, Kazman — Software Architecture in Practice (Quality Attributes + tactics + tradeoffs)"
  - "Cohn — User Stories Applied (INVEST: Small, Independent)"
  - "Patton — User Story Mapping (narrative coherence, task-level)"
  - "Nygard — Documenting Architecture Decisions (ADR cuando hay alternatives consideradas)"
  - "Ousterhout — A Philosophy of Software Design (deep modules, information hiding)"
  - "Martin — Clean Architecture (Dependency Rule, boundaries)"
---

# Coupling-review consolidado · 14 features bootstrap

## Contexto y scope

Output del step-3 del WA-2026-05-13-005. Cobertura: 14 features Nivel 1 producidas en step-2 (+ ~40 stories + ~40 specs Gherkin). Aplica `coupling-detection` (Ford), `coherence-evaluation` (Ford+Martin), `feature-viability-review` (Bass+Ford) **bibliográficamente disciplinado** con criterio load-bearing — no transitive coupling, no ADR-inflation.

**Veredicto global**: **apto-con-correcciones menores** para `/verify` (ver §6). El conjunto es internamente coherente, granularidad INVEST mayoritariamente correcta (1 caso borderline acotado), coupling estructural declarado limpiamente, ADRs latentes razonables.

---

## 1. Matriz coupling cross-feature (Ford appropriate coupling)

Test load-bearing aplicado: una arista `F1 → F2` SOLO se considera coupling estructural si **el comportamiento de F1 depende operativamente de un mecanismo provisto por F2 en runtime/protocolo**. Coupling narrativo (ambas mencionan al PO) NO cuenta. Coupling transitivo (F1 depende de F2 que depende de F3) NO se duplica en F1.

### 1.1 Coupling declarado y verificado correcto (`depends-on`)

| Origen | Destino | Tipo | Veredicto |
|---|---|---|---|
| feature-019 `/verify` | feature-018 `/scope-scan` | reuso paralelización subagentes (Task tool) | **Correcto, load-bearing.** `/verify` invoca verifiers via mismo patrón flat parallel. Ford appropriate coupling: dependencia explícita en mecanismo, no en implementación. |
| feature-019 | feature-009 catalogo-roles (Nivel 4 artefacto) | lookup `custodian(d)` | **Correcto pero apuntar Nivel 4** — feature-009 NO existe como feature Nivel 1 (reclasificada en discovery doc). El depends-on debe re-anclarse al **artefacto** `vault/shared/governance/role-catalog.md` (campo `depends-on-artifact` o nota inline). Correción cosmética, no estructural. |
| feature-032 `/status` | feature-001 vault-role-first | lectura física de `vault/<rol>/` | **Correcto.** `/status` enumera artefactos por rol — la organización física es la interfaz que consume. |
| feature-035 ritual-inicio | feature-001 | idem | **Correcto.** Ritual lee 5 directorios del vault. |
| feature-038 PO-Modo-1 | feature-035 ritual + feature-018 scope-scan | paso 1 + paso 5 cubiertos por hermanas | **Correcto.** Composición declarada. INVEST `I` preservado (feature-038 no duplica comportamiento). |
| feature-039 cadena-WAs | feature-038 + feature-013 templates (Nivel 4) | paso 7 + uso templates | **Correcto.** Idem corrección cosmética sobre feature-013 (artefacto, no feature). |
| feature-041 README | feature-011 CLAUDE.md (NO Nivel 1) | referencia documental | **Inconsistencia minor**: feature-011 fue reclasificada borderline (Nivel 4 artefacto + JTBD newcomer cubierto por feature-041). Re-anclar a `CLAUDE.md` raíz como artefacto. |
| feature-044 glosario | feature-041 README | referenciado primera-aparición | **Correcto.** |
| feature-045 ruta-lectura | feature-041 + feature-044 | sección embebida en README + glosario | **Correcto.** |

### 1.2 Coupling NO declarado detectado (recomendación añadir)

| Origen | Destino faltante | Razón load-bearing | Severidad |
|---|---|---|---|
| feature-018 `/scope-scan` | feature-010 entry-point | invocación Task tool requiere identidad del rol cargada por wrappers + agent files — feature-010 garantiza identidad cargable | **Media** — añadir `also-relates-to: feature-010` (no `depends-on` directo: feature-018 NO instancia la sesión del advisor; Task tool carga la identidad nativa). Cross-link narrativo correcto. *Ya declarado en spec-018-A inline, NO en feature-018 frontmatter — propagar.* |
| feature-032 `/status` | feature-019 `/verify` | `/status` muestra "features por status" y los status transitan vía on-close de `/verify` | **Baja** — flow indirecto vía estado del nodo, no llamada directa. Ford permite coupling vía data shape sin declarar arista (deep module: el nodo del grafo es la interfaz). Opcional `also-relates-to`. |
| feature-033 `/wa` | feature-018 + feature-019 | `/wa` muestra "próximo step pending" que apunta a workflows que invocan a las dos | **Baja** — coupling narrativo, no estructural. NO declarar (evita inflar). |
| feature-036 orientación-rol | feature-034 `/sessions` | criterio orientación se materializa en /sessions output | **Media** — ya declarado vía `also-relates-to: cap-02`. Faltaría feature-level `also-relates-to: feature-034`. Añadir. |
| feature-038 PO-Modo-1 | feature-019 `/verify` | paso 10 indica handoff al humano + `/verify` al cerrar steps | **Media** — el flujo Modo-1 NO ejecuta /verify directamente; el humano lo ejecuta al cierre. Coupling narrativo solamente. NO declarar arista directa. |
| feature-039 cadena-WAs | feature-019 `/verify` | "Tras /verify del primer WA, drafta el siguiente" | **Media** — feature-039 OBSERVA un /verify completado; no invoca. Trigger event-driven via estado del grafo. Opcional `also-relates-to`. |
| Conjunto features-CAP-J (041/044/045) | feature-001 vault-role-first | README documenta vault role-first | **Baja** — coupling documental no operativo. NO declarar (Ford anti-overengineering). |

### 1.3 Coupling problemático (smell)

**Ninguno detectado** que requiera supersession o rediseño. Patrón global limpio: features de slash commands (CAP-D + CAP-F) componen sobre features de organización (CAP-A) + identidad (CAP-B), respetando Martin Dependency Rule (alto nivel → bajo nivel, no inversa). No hay ciclos. No hay coupling implícito en data shape (cada feature declara su contrato via stories+specs).

**Información leakage (Ousterhout)**: cero detecciones. Las features-slash NO exponen internals de unas a otras — comparten solo el grafo declarativo persistente (interface stable).

---

## 2. Veredicto granularidad per-feature (Cohn INVEST `S`)

| Feature | Stories | Veredicto | Razón |
|---|---|---|---|
| feature-001 vault-role-first | 3 | **ok** | Job concreto, contornos observables. |
| feature-010 entry-point-por-rol | 3 (preview 4) | **ok** | 8 atajos × 1 patrón = familia coherente. |
| feature-018 /scope-scan | 3 | **ok** | Convocatoria + recepción + consolidación = 3 movimientos claros. |
| feature-019 /verify | 4 | **ok** | Closure-check / derive / invoke / on-close+archive. Linde sup. INVEST `S`. |
| feature-032 /status | 4 stories preview, 2 specs (A,B) | **ok-con-nota**: el preview menciona 4 stories pero existen solo specs A,B materializadas. Otras 2 pendientes para WA `feature-build` posterior. INVEST `S` se preserva si stories C,D viven como AC adicionales o specs incrementales. **No bloqueante**. |
| feature-033 /wa | 2 | **ok** |
| feature-034 /sessions | 1 materializada (A; B futura) | **ok** | Granularidad minimal correcta. |
| feature-035 ritual-inicio | 2 specs (A,B; preview menciona 3) | **ok-con-nota** análoga a feature-032. |
| feature-036 orientación-rol | 2 specs (A,B; preview menciona 3) | **ok-con-nota**. |
| feature-038 PO-Modo-1 | 4 specs (A,B,C,D) cubriendo pasos 2-3,4,7-8,9-10 con pasos 1+5+6 cubiertos por hermanas | **ok**: pasó test mecánico Adzic. Decisión PO de agrupar 10 pasos en 4 stories vía composición con feature-035 + feature-018 es correcta. Linde sup. INVEST `S`. **Aviso preventivo**: si emergen sub-features autónomos durante feature-build (paso 4 "decide conduzco/delego" es candidato a extracción), sub-dividir. |
| feature-039 cadena-WAs | 3 | **ok** |
| feature-041 README | 3 | **ok** |
| feature-044 glosario | 2 | **ok** |
| feature-045 ruta-lectura | 2 | **ok** |

**Veredicto granularidad**: **ok global, sin sub-divisiones ni agrupaciones requeridas**. Notas no-bloqueantes: features con stories C,D no materializadas en step-2 son aceptables — el catálogo se cierra en este WA, materialización de stories pendientes en WAs `feature-build` futuros (Cagan principio 1 — entregar `S` que aporta valor; resto incremental).

---

## 3. Coherencia features ↔ QAs Bass de capability padre

Validación: cada feature contribuye a ≥1 QA declarado en su capability padre.

| Feature → Capability padre | QAs Bass del padre relevantes | Coherencia |
|---|---|---|
| feature-001 → CAP-01 grafo declarativo | modifiability, integrability | **OK** — vault role-first materializa separation of concerns (modifiability). |
| feature-010 → CAP-02 multirol | usability, modifiability | **OK** — atajos npm = usability tactic; wrappers CLAUDE.md = modifiability via convention. |
| feature-018, feature-019 → CAP-04 verif multirol | reliability (algoritmo declarativo), modifiability (verifiers extensibles) | **OK** — algoritmo `verifiers = {custodian(d)}` es tactic Bass para reliability + modifiability. |
| feature-032, 033, 034, 035, 036 → CAP-06 visibilidad | usability (Nielsen #1, #6, #7, #9), modifiability | **OK** — todas materializan tactics de visibility/recognition. |
| feature-038, 039 → CAP-07 inception | usability + modifiability (templates uniformes) | **OK**. |
| feature-041, 044, 045 → CAP-10 articulación pública | usability + business viability | **OK** — Moore/Cooper/Nielsen anclados. |

**Sin mismatches detectados.** Coherencia features ↔ QAs padre: 14/14.

**Nota Architect**: feature-038 declara `dimensions-affected: [product, technical, usability]` — la dimensión `technical` aquí es marginal (PO Modo-1 es comportamiento de agente, no decisión arquitectónica). Mantener por trazabilidad scope-scan WA-005, pero al `/verify` el custodio `technical` aprobará con observación "tocado por orquestación del Modo-1, no por decisión arq propia".

---

## 4. Viability technical preview per-feature relevante

Solo features con dimensión `technical` declarada (8/14). Otras 6 son product+usability puro — no viability technical material.

| Feature | Riesgo arq. | Mitigación / fitness function recomendada |
|---|---|---|
| feature-001 vault-role-first | **Bajo**. Convention-over-mechanism. Riesgo: deriva future cuando aparezcan nuevos roles. | Fitness function: `script` que valida que `.claude/agents/*.md` tiene 1:1 con `vault/*/`. Documentar en ADR-latente-002. |
| feature-010 entry-point | **Bajo**. Dependencia harness (Claude Code CLAUDE.md jerárquico + npm). | Documentado en `depends-on-harness` — adapter pattern al activarse CAP-08 portabilidad. |
| feature-018 /scope-scan | **Bajo-Medio**. Paralelización Task tool puede fallar si advisor responde inconsistente (output `scope-scan-output` mal formado). | Schema-validation del output Filtro PO regla 12 actúa como fitness function. Documentar en ADR-latente-009. |
| feature-019 /verify | **Medio**. Algoritmo on-close mutates estado del grafo (transitions). Riesgo: race conditions si dos `/verify` simultáneos. | Mitigation: WA `active` es singleton por humano (no documentado explícitamente — flag para ADR-latente-010). Fitness function: lint que `on-close` paths son únicos cross-WA-activo. |
| feature-032 /status | **Bajo**. Read-only query. | — |
| feature-033 /wa | **Bajo**. Read-only query. | — |
| feature-036 orientación-rol | n/a (no technical declarado) | — |
| feature-038 PO-Modo-1 | **Bajo**. Comportamiento de agente; technical marginal. | — |
| feature-039 cadena-WAs | **Bajo**. Composición de WAs existentes vía templates. | — |
| feature-041 README | n/a (technical no declarado en el frontmatter; sí en su ámbito documental) | — |

**Sin viability blockers.** Dos features con riesgo `Medio` documentados (`/scope-scan` schema-validation, `/verify` race-conditions singleton-assumption).

---

## 5. ADRs latentes confirmados (input Lote B WAs `adr` posteriores)

### 5.1 Confirmados heredados del discovery doc (11 candidatos)

| ADR-latente-ID | Título | Confirmación |
|---|---|---|
| 001 | Claude Code v1 como harness primario | **Confirmar.** Alternatives: Cursor, Cline, custom. Apuntado por feature-010, 018, 019. |
| 002 | Vault role-first como organización física | **Confirmar.** Alternatives: vault/type-first, vault/timeline. Apuntado por feature-001 + propagar a feature-032, 035 (lectores). |
| 003a | Frontmatter YAML como mecanismo declarativo | **Confirmar.** Alternatives: JSON, TOML, custom. |
| 003b | Wikilinks `[[id]]` para referencias internas | **Confirmar.** Alternatives: markdown links, IDs sin link. |
| 004 | Estados canónicos + transiciones del nodo | **Confirmar.** Alternatives: estados libres, lifecycle implícito. Apuntado por spec-019-D. |
| 007 | Templates uniformes greenfield/maduro (mode-flag) | **Confirmar.** ADR meta-1. Alternatives: protocolos paralelos. |
| 008 | Backlog como query emergente | **Confirmar.** Apuntado por feature-032, feature-019. Alternatives: backlog persistente como archivo. |
| 008b | Trazabilidad `// @sem-ia:` + `// @ac-coverage:` | **Confirmar.** Alternatives: trazabilidad externa, ninguna. |
| 009 | Tres checkpoints uniformes WA lifecycle | **Confirmar.** Apuntado por feature-018, 019. |
| 010 | Algoritmo declarativo verifiers / on-close | **Confirmar.** Apuntado por feature-019. **Añadir flag**: singleton-WA-activo (sección 4). |
| WA-structure | Estructura inline del WA como contrato declarativo | **Confirmar.** |
| license | Apache 2.0 elegida | **Confirmar.** Alternatives: MIT, GPL, BSD. Apuntado por feature-041. |

**Total heredados: 12 confirmados** (uno de ellos, WA-structure, no estaba en la enumeración 11 inicial pero está presente en discovery doc Bloque 3 — confirmar).

### 5.2 Emergentes durante este review (3 nuevos candidatos)

| ADR-latente-ID propuesto | Título | Razón de emergencia |
|---|---|---|
| **010-singleton** (o extensión de 010) | Singleton-WA-activo-por-humano: race-conditions de on-close | Emergente sec. 4. Decisión arquitectónica con alternatives (lock-file vs cooperative protocol vs ignore). NO bloqueante WA-005 pero candidato Lote B. |
| **011-cross-link-cardinality** | Reglas de cardinalidad `parent` único vs `also-relates-to` plural | Mencionado inline en feature-005 reclasif. + discovery 1.5. NO está explícito como ADR. Alternatives: parent plural, parent único. |
| **012-scope-forbidden-enforcement** | Cómo se enforcea `scope-forbidden` del WA (advisory vs hard-block) | Latente en estructura WA. Tu prompt mismo dice "scope-forbidden". Alternatives: advisory (auto-audit PO), runtime check (Edit hook), ninguna (confianza). |

### 5.3 Apuntamientos a corregir

- **Specs Gherkin** apuntan ADRs latentes vía `related-adrs` por **ID corto** (`ADR-latente-008`). Cuando Lote B materialice ADRs, mapping ID-corto → ID-canónico debe documentarse en cada ADR como `supersedes-latent: ADR-latente-NNN`. NO hay corrección a aplicar ahora — solo nota para Lote B.
- **feature-009-catalogo-roles** y **feature-013-catalogo-workflow-templates** y **feature-011-claude-md-raiz** aparecen referenciadas como `depends-on` en algunas features (019, 039, 041, 044) PERO no son features Nivel 1 (reclasificadas a Nivel 4 artefactos). **Acción NO-bloqueante**: PO al `/verify` puede re-anclar esas referencias a artefactos del filesystem (`vault/shared/governance/role-catalog.md`, etc.) o dejar como están con nota inline "reclasificada Nivel 4". Decisión de PO, no de Architect.

### 5.4 Total final candidatos Lote B

**12 heredados confirmados + 3 emergentes = 15 ADRs latentes**. (Discovery doc estimó ~9-11; emergen 4 adicionales tras review riguroso — esperado.)

---

## 6. Veredicto consolidado

**APTO-CON-CORRECCIONES MENORES** para `/verify` del WA-2026-05-13-005.

### Sin blockers técnicos:
- Coupling cross-feature: limpio, sin ciclos, sin information leakage (Ford+Ousterhout+Martin).
- Granularidad INVEST: 14/14 OK; 3 features con stories C,D no materializadas — aceptable (entregar `S` ahora, incremental después).
- Coherencia features ↔ QAs Bass de capabilities padre: 14/14.
- Viability technical: 8/8 con dimensión `technical` declarada honestamente. Dos con riesgo Medio documentado (fitness functions recomendadas).

### Correcciones menores recomendadas (NO bloqueantes para /verify, abordables en post-step PO o aparcables para Lote B):
1. **Propagar `also-relates-to: feature-010`** a frontmatter de feature-018 (hoy solo en spec-018-A inline).
2. **Añadir `also-relates-to: feature-034`** a feature-036.
3. **Re-anclar `depends-on: feature-009/011/013`** (Nivel 4 reclasificadas) a artefactos del filesystem, o dejar nota inline. Decisión PO.
4. **Documentar fitness functions** recomendadas en sec. 4 cuando Lote B materialice ADR-002, ADR-009, ADR-010.

### Para Lote B:
- 12 ADRs latentes heredados confirmados.
- 3 ADRs emergentes nuevos: 010-singleton, 011-cross-link-cardinality, 012-scope-forbidden-enforcement.
- Total Lote B: **15 ADRs candidatos**.

### Anclaje bibliográfico citado:
Ford (appropriate coupling §1 + fitness functions §4), Bass (QAs §3 + tactics §4), Cohn INVEST (§2), Patton narrative coherence (§3), Nygard ADR criterion §5 (decisión con alternatives consideradas — sin alternatives no es ADR Nygard), Ousterhout deep modules §1.3 (cero information leakage), Martin Dependency Rule §1.3 (no ciclos).

---

## filesystem-changes

```yaml
filesystem-changes:
  - path: /Users/pelayo/Developer/SEM-AI/vault/architect/research/spine-bootstrap-coupling-review.md
    operation: created
    locations:
      - lines: 1-44
        change-summary: "Frontmatter (type=research, id, related-wa/discovery/capabilities/features, dimensions=[technical], citas-bibliograficas Ford+Bass+Cohn+Patton+Nygard+Ousterhout+Martin)"
      - lines: 46-58
        change-summary: "Contexto y scope + veredicto global (apto-con-correcciones)"
      - lines: 60-100
        change-summary: "§1 Matriz coupling cross-feature: 1.1 declarado correcto (9 aristas), 1.2 no declarado detectado (7 candidatos con severidad), 1.3 problemático (cero)"
      - lines: 102-122
        change-summary: "§2 Veredicto granularidad INVEST per-feature 14/14"
      - lines: 124-141
        change-summary: "§3 Coherencia features ↔ QAs Bass capability padre 14/14"
      - lines: 143-157
        change-summary: "§4 Viability technical preview: 8 features con technical, 2 riesgo Medio (scope-scan schema, verify singleton)"
      - lines: 159-201
        change-summary: "§5 ADRs latentes: 12 heredados confirmados + 3 emergentes (010-singleton, 011-cross-link-cardinality, 012-scope-forbidden-enforcement) + apuntamientos a corregir"
      - lines: 203-228
        change-summary: "§6 Veredicto consolidado: apto-con-correcciones menores + 4 correcciones no bloqueantes + 15 ADRs Lote B"
    rationale: "Output esperado del step-3 del WA-2026-05-13-005 (feature-design reverse-engineering-batch). Consolidar coupling-detection + coherence-evaluation + feature-viability-review sobre 14 features producidas en step-2, confirmar ADRs latentes para Lote B. Aplicar Filtro PO contaminado (regla 12 + learning anti-pattern) anti coupling-inflation y anti ADR-inflation. Anclaje bibliográfico explícito (Ford+Bass+Cohn+Patton+Nygard+Ousterhout+Martin) por requisito del agent file Architect."
```
