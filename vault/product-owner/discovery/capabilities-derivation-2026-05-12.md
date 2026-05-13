---
type: discovery
id: capabilities-derivation-2026-05-12
title: "Derivación top-down goal-1 (parcial) · WA wa-2026-05-12-001 (aborted)"
status: aborted-reference
created: 2026-05-12
aborted-at: 2026-05-12T01:15:00+02:00
aborted-reason: "WA-001 abortado por pivot a bottom-up. Este documento solo procesó goal-1. Se preserva como referencia para cross-check con WA-002 (bottom-up): las 4 candidatas g1-A/B/C/D anticipan capabilities que probablemente ya operan en el bootstrap."
author: product-owner
related-wa: wa-2026-05-12-001
superseding-wa: wa-2026-05-12-002
related-vision: vision
related-goals: [goal-1-auto-sostenibilidad, goal-2-output-auditable-multirol, goal-3-absorcion-coste-revision, goal-4-rigor-multirol-individual, goal-5-portabilidad, goal-6-articulacion-publica, goal-7-ciclo-vida-producto]
skills-applied: [capability-derivation]
bibliography:
  - Torres — Continuous Discovery Habits (OST)
  - Rumelt — Good Strategy/Bad Strategy (guiding policy filter)
  - Christensen — Jobs-To-Be-Done (formulación de oportunidades)
---

# Derivación de capabilities · 2026-05-12

Este documento es el output del **step-1** del WA `wa-2026-05-12-001`. Aplica la skill `capability-derivation` iterativamente sobre los 7 goals aprobados. Produce capabilities candidatas brutas + filtradas, con razones de descarte documentadas para auditoría (Rumelt).

## Guiding policy de SEM-IA (extraída del enunciado de la visión)

> *"IA como infraestructura, humano como autor — sin sustituir roles. Construir contexto persistente versionado + agentes IA multi-rol que se revisan cruzadamente cada decisión antes de cerrarla. Para productos reales con ciclo de vida completo."*

**Filtro Rumelt operativo** — una solución candidata sobrevive si:
1. **Contribuye al kernel estratégico** (diagnosis: deficiencias estructurales de la IA; guiding policy: infraestructura externa que las absorbe; coherent action: agentes multi-rol con grafo declarativo).
2. **No introduce policía** sobre el humano (la IA es infraestructura, no enforcer).
3. **No requiere sustituir** rol humano por agente (los agentes son custodios, el humano firma).
4. **Acumulable** — no es atajo puntual sino propiedad sostenible.

---

## Goal-1 · Auto-sostenibilidad operativa

### Paso 1 — Outcome OST

> **Movemos a SEM-IA de marco-conceptual-aún-no-self-hosting (bootstrap manual con atajos pre-protocolo permitidos en construcción inicial) a marco operativamente self-hosting**:
> - ≥ 90 % del desarrollo pasando por sus propios WAs + verificación multi-rol,
> - inception desde vault vacío sin intervención manual al protocolo,
> - cero atajos pre-bootstrap tras la fecha de inception formal.

### Paso 2 — Oportunidades

Usuarios relevantes: **(a) humano-autor construyendo SEM-IA con SEM-IA** (Pelayo en dogfooding); **(b) adopter futuro que arranca proyecto greenfield con SEM-IA** (cross con goal-5 pero contribuye también a goal-1: si SEM-IA no es greenfield-incepcible, no es self-hosting).

- **O1.1** — El humano-autor **no puede arrancar trabajo de construcción del framework usando los propios protocolos** si el framework aún no está construido (paradoja del bootstrap). Necesita una vía de entrada desde vault vacío conforme al protocolo, no ad-hoc.
- **O1.2** — El humano-autor sufre la **tentación de atajos pre-bootstrap** porque introducir el protocolo en mitad del trabajo es costoso operativamente. Necesita que el protocolo esté disponible desde el momento más temprano posible y que su uso tenga coste marginal bajo.
- **O1.3** — El humano-autor **no puede demostrar a terceros** (académicos, adopters, comunidad) que SEM-IA funciona si no hay evidencia auditable de que el desarrollo del propio SEM-IA pasa por sus protocolos. Necesita trazabilidad pública del dogfooding.
- **O1.4** — El humano-autor **no puede detectar cuándo se está saltando el protocolo** (drift silencioso de auto-sostenibilidad). Necesita visibilidad operativa: % de trabajo dentro de WAs vs ad-hoc, edad de WAs activos, gaps.
- **O1.5** — Un adopter externo (greenfield) **no puede arrancar SEM-IA** si no existe mecanismo de inception desde vault vacío. Si SEM-IA exige "primero construye 8 agents + 7 skills + 14 templates antes de tu primer WA", deja de ser self-hosting.
- **O1.6** — El humano-autor y adopter futuro necesitan que **inception + dogfooding + mantenimiento usen los mismos protocolos** — no tres sets distintos. Es el corazón de la promesa "auto-sostenible".

6 oportunidades. Dentro del rango 3-7 que la skill admite.

### Paso 3 — Soluciones candidatas (2-3 por oportunidad)

**O1.1 — Bootstrap conforme al protocolo desde vault vacío**

- `S1.1.a` — *"El sistema tiene la habilidad de declarar un modo bootstrap manual mínimo auditado"*: pieza mínima indispensable construida pre-protocolo (8 agents core + slash commands `/status` `/wa` `/verify` `/scope-scan` `/sessions` + governance defaults + skills mínimas del PO) con línea explícita de transición a self-hosting.
- `S1.1.b` — *"El sistema tiene la habilidad de inception greenfield-from-empty-vault con un solo comando"*: `npm run sem` arranca PO, PO detecta vault vacío, propone cadena `vision-creation → goal-definition → capability-creation → feature-design`.
- `S1.1.c` — *"El sistema tiene la habilidad de documentar trazablemente el bootstrap manual"*: archivo audit-trail de qué se construyó pre-protocolo, justificación, y línea de transición a strict self-hosting.

**O1.2 — Coste marginal bajo del protocolo**

- `S1.2.a` — *"El sistema tiene la habilidad de automatizar setup de WA"*: slash commands + skills + scope-scan en una sola invocación paralela; humano no construye WA frontmatter a mano.
- `S1.2.b` — *"El sistema tiene la habilidad de scope-scan multi-rol automático al draftear WA"*: el rol orquestador no decide manualmente a quién invocar — el sistema convoca a los 5 asesores restantes en paralelo por defecto.
- `S1.2.c` — *"El sistema tiene la habilidad de degradación gradual del protocolo"*: para outcome-types `trivial` (typos, copy fix), NO hay WA; para `doc-edit` menor, WA mínimo; para el resto, WA completo.

**O1.3 — Trazabilidad pública del dogfooding**

- `S1.3.a` — *"El sistema tiene la habilidad de exponer públicamente los WAs activos y archivados"*: `vault/shared/sessions/active/` + `archive/` versionados en git, auditables por terceros leyendo el repo.
- `S1.3.b` — *"El sistema tiene la habilidad de generar reportes periódicos de auto-sostenibilidad"*: strategy-review periódico con % commits asociados a WAs, ratio WAs por fase, antigüedad media de WAs activos.
- `S1.3.c` — *"El sistema tiene la habilidad de presentar al humano el subgrafo estratégico y el backlog en tiempo real"*: slash `/status` muestra panorámica para auditoría inmediata.

**O1.4 — Detección de drift de auto-sostenibilidad**

- `S1.4.a` — *"El sistema tiene la habilidad de panorámica operativa por sesión y por slash"*: `/status` + `/wa` permiten al humano ver qué está activo, bloqueado, edad media.
- `S1.4.b` — *"El sistema tiene la habilidad de bloquear commits sin WA asociado vía git hooks"*: rigor por enforcement.
- `S1.4.c` — *"El sistema tiene la habilidad de detectar drift retroactivo"*: comparar commits del repo con WAs archivados; reportar commits "sin WA" como atajos.

**O1.5 — Inception greenfield para adopters**

- `S1.5.a` — *"El sistema tiene la habilidad de proveer vault skeleton + governance defaults distribuibles"*: adopter clona y arranca con setup mínimo. (Primariamente goal-5; cross-link.)
- `S1.5.b` — *"El sistema tiene la habilidad de inception interactiva conducida por el PO"*: PO con vault vacío presenta opciones (vision desde cero / importar / template), guía paso a paso.
- `S1.5.c` — *"El sistema tiene la habilidad de generar proyecto SEM-IA-conforme desde plantilla CLI"*: `npx @sem-ia/cli init`. (Primariamente goal-5.)

**O1.6 — Convergencia inception ↔ dogfooding ↔ mantenimiento**

- `S1.6.a` — *"El sistema tiene la habilidad de unificar mecanismos vía templates indexados por fase SDLC"*: los mismos workflows (`workflows.md`) sirven greenfield + maturo. Sin protocolos paralelos.
- `S1.6.b` — *"El sistema tiene la habilidad de distinguir fases de madurez del proyecto sin cambio de protocolo"*: `/status` reporta "fase inception" vs "fase mature" pero usa los mismos WAs/scope-scan/verify.

Total bruto goal-1: **17 candidatas**.

### Paso 4 — Filtro Rumelt (coherencia con guiding policy)

| Sol | Veredicto | Razón |
|---|---|---|
| S1.1.a | ✅ | Explicita la línea bootstrap/self-hosting que goal-1 pide. Acumulable (queda documentado). |
| S1.1.b | ✅ | Habilita arrancar el sistema entero sin ad-hoc. Crítica para self-hosting. |
| S1.1.c | ✅ | Apoya auditabilidad (cross-goal con goal-2). Acumulable. |
| S1.2.a | ✅ | Sin coste bajo el dogfooding total es infactible. Pivotal (Rumelt). |
| S1.2.b | ✅ | Refuerza coste bajo. Coherente con give-and-take Cagan multi-rol. |
| S1.2.c | ✅ | Pragmatismo necesario. Sin esto, el protocolo se aplica a triviales con coste absurdo → genera atajos. |
| S1.3.a | ✅ | Auditabilidad pública vía git. Coste cero (los archivos viven en repo). |
| S1.3.b | ✅ | Apoya auditabilidad sostenida en tiempo (cross-goal con goal-7). |
| S1.3.c | ✅ | Habilita al humano operar conscientemente. |
| S1.4.a | ⚠️ overlap | Solapa con S1.3.c. Unificar — son la misma capability operativa. |
| **S1.4.b** | **❌ descartar** | **Incoherente con guiding policy "IA como infraestructura, no policía". Rigor por incentivo (coste bajo + visibilidad) no por enforcement.** |
| S1.4.c | ⚠️ overlap | Solapa con S1.3.b (strategy-review periódico ya cubre detección retroactiva). Unificar. |
| S1.5.a | ✅ cross-goal | Primariamente goal-5 (portabilidad). Cross-link a goal-1. |
| S1.5.b | ✅ | Habilita conducir adopter greenfield. Esto ya está implícito en el agent file del PO Modo 1 — aquí lo formalizo como capability. |
| **S1.5.c** | **❌ descartar para goal-1** | Primariamente goal-5 territorio puro. No aporta a auto-sostenibilidad de SEM-IA mismo. |
| S1.6.a | ✅ | Pivotal. Sin templates unificados, inception/dogfooding/mantenimiento divergen. |
| S1.6.b | ⚠️ overlap | Es propiedad emergente de S1.6.a, no capability separada. Absorber. |

**Supervivientes consolidados: 11 soluciones** repartidas en **clusters naturales**.

### Paso 5 — Consolidación en capabilities candidatas

**Cluster A · "Inception greenfield protocol-compliant desde vault vacío"**
- Absorbe: S1.1.b, S1.5.b, S1.6.a, S1.6.b
- Enunciado: *El sistema tiene la habilidad de arrancar un proyecto SEM-IA conforme al protocolo desde vault vacío — el PO conduce inception greenfield (vision → goals → capabilities → feature-design) usando los mismos workflows que en fase mature, sin protocolos paralelos ni atajos ad-hoc.*
- Cross-goal candidatos: goal-5 (portabilidad), goal-7 (ciclo de vida, inception es la primera fase).
- Dimensiones tentativas: `product`, `technical` (workflows/templates como mecanismo arquitectónico), `usability` (DX del PO conduciendo inception).

**Cluster B · "Bootstrap manual auditado con línea de transición a self-hosting"**
- Absorbe: S1.1.a, S1.1.c
- Enunciado: *El sistema tiene la habilidad de declarar y documentar trazablemente un bootstrap manual mínimo auditado — pieza indispensable construida pre-protocolo (8 agents, slash commands, governance defaults, skills mínimas del PO) con línea explícita desde la cual todo trabajo subsiguiente pasa por WAs.*
- Cross-goal candidatos: goal-2 (auditabilidad del propio bootstrap), goal-7 (ciclo de vida documentado desde fase 0).
- Dimensiones tentativas: `product`, `technical` (la pieza mínima es decisión arquitectónica), `quality` (auditabilidad del bootstrap).

**Cluster C · "Operación del protocolo con coste marginal bajo"**
- Absorbe: S1.2.a, S1.2.b, S1.2.c
- Enunciado: *El sistema tiene la habilidad de operar bajo su protocolo (WAs + scope-scan multi-rol + verify) con coste marginal bajo — slash commands automatizan setup, scope-scan flat parallel es default automático, degradación gradual permite saltarse WA en outcome-types `trivial`. El rigor se sostiene por incentivo operativo, no por enforcement.*
- Cross-goal candidatos: goal-3 (absorción coste revisión — si crear WA es caro, el coste se traslada al humano en vez de absorberse), goal-4 (rigor individual — sin coste bajo, un humano individual no sostiene el rigor).
- Dimensiones tentativas: `product`, `technical` (slash commands + scope-scan flat parallel son mecanismo técnico), `usability` (DX del operador).

**Cluster D · "Visibilidad operativa del estado y cumplimiento de auto-sostenibilidad"**
- Absorbe: S1.3.a, S1.3.b, S1.3.c, S1.4.a (unificado), S1.4.c (unificado)
- Enunciado: *El sistema tiene la habilidad de exponer al humano y a terceros el estado operativo del proyecto (WAs activos, fase, backlog, subgrafo estratégico vía `/status` `/wa`) + el cumplimiento sostenido de auto-sostenibilidad (strategy-review periódico que mide % desarrollo bajo WA, drift retroactivo, antigüedad de WAs). Los WAs viven en git versionados como evidencia pública.*
- Cross-goal candidatos: goal-2 (auditabilidad), goal-3 (absorción coste revisión), goal-4 (rigor individual — el humano necesita visibilidad para no perderse).
- Dimensiones tentativas: `product`, `quality` (métricas de cumplimiento), `usability` (panorámica operativa), `technical` (mecanismo de query sobre vault).

**Cross-link declarado (no nueva capability)**
- S1.5.a (vault skeleton distribuible): se materializará en una capability primariamente derivada de goal-5. Aquí queda **anotado** como `cross-link futuro: cap-de-goal-5 also-relates-to: [goal-1]`.

### Paso 6 — Descartes documentados (auditoría Rumelt)

| Solución | Razón |
|---|---|
| `S1.4.b` "bloquear commits sin WA asociado vía git hooks" | **Incoherente con guiding policy** *"IA como infraestructura, no policía"*. Genera friction operativa alta y contradice el principio de rigor-por-incentivo. La trayectoria sostenible es bajar coste de usar el protocolo (Cluster C) + dar visibilidad (Cluster D), no bloquear al humano. |
| `S1.5.c` "generar proyecto SEM-IA-conforme desde plantilla CLI (`npx @sem-ia/cli init`)" | **Primariamente goal-5 (portabilidad)** — no aporta a auto-sostenibilidad de SEM-IA mismo (que ya opera vía `npm run sem`). Se derivará desde goal-5 directamente. Cross-link inverso. |
| `S1.4.a` / `S1.4.c` originales | Absorbidas en Cluster D (overlap interno; no descarte real). |
| `S1.6.b` original | Absorbida en Cluster A (propiedad emergente, no capability separada). |

### Output goal-1

**4 capabilities candidatas** + **2 descartadas con razón** + **1 cross-link a capability futura de goal-5**.

| ID temporal | Enunciado breve | Cross-goals candidatos | Dimensiones tentativas |
|---|---|---|---|
| `g1-cluster-A` | Inception greenfield protocol-compliant desde vault vacío | goal-5, goal-7 | product, technical, usability |
| `g1-cluster-B` | Bootstrap manual auditado con línea de transición a self-hosting | goal-2, goal-7 | product, technical, quality |
| `g1-cluster-C` | Operación del protocolo con coste marginal bajo | goal-3, goal-4 | product, technical, usability |
| `g1-cluster-D` | Visibilidad operativa del estado y cumplimiento de auto-sostenibilidad | goal-2, goal-3, goal-4 | product, quality, usability, technical |

IDs definitivos (`cap-NN-<slug>`) se asignan en la consolidación final cross-goal — antes hay que cruzar con goal-2..7 por si emergen overlaps que consoliden clusters entre goals (probable: Cluster D solapa fuerte con candidatas de goal-2; Cluster C solapa con goal-3).

---

_(Iteración goal-2 pendiente)_
