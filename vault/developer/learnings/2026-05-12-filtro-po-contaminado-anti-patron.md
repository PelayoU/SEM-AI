---
type: learning
id: learning-2026-05-12-filtro-po-contaminado
title: "Anti-patrón: Filtro PO contaminado — clasificar como categoría 1 todo lo razonable que dice un advisor"
status: active
created: 2026-05-12
author: product-owner
related-wa: wa-2026-05-12-004
related-gap-sistema: gap-6  # Filtro PO 4 categorías formalizado en WA-003
dimensions-affected: [product, quality]
bibliography:
  - Cagan — Inspired (strong PM: opinions informed by data but decisions are own)
  - Cagan — Empowered (strong product team: coherent point of view; PM owns decision)
  - Ousterhout — A Philosophy of Software Design (deep modules, simple interfaces — no inflar)
  - Cohn — User Stories Applied (INVEST `I = Independent` — coupling mínimo declarado)
---

# Anti-patrón: Filtro PO contaminado

## Contexto del incidente

Durante el WA-2026-05-12-004 (`feature-design` mode reverse-engineering batch), tras cerrar el step-1 (PO discovery doc con 46 features candidatas), se ejecutó **post-step scope-scan flat parallel multi-rol** con los 5 asesores en paralelo (Architect, Designer, Business-analyst, Security-officer, QA). Cada uno produjo `scope-scan-output` estructurado con flags + sugerencias.

El PO (yo) aplicó el **Filtro PO de 4 categorías Cagan** (Gap 6 ya formalizado en WA-003) sobre los outputs consolidados. **Clasificación inicial**:
- Categoría 1 ("acepto y aplico yo"): **13 cambios** al discovery doc + WA.
- Categoría 2 ("descarto con razón"): 3 cambios (NOTICE Apache, CONTRIBUTING.md, depends-on-harness campo).
- Categoría 3 ("difiero a WA futuro"): 4 cambios (ADRs latentes split, namespace npm, ADR-security-trans).
- Categoría 4 ("requiere decisión humana"): 2 preguntas (orden steps 3-7, deadline GISF features 044/045).

**El humano detectó el patrón inmediatamente al ver el resumen**: *"¿De dónde han salido tantas features? Los subagentes están para darte info, no para contaminarte. Tú eres el que sabe de features."*

## Diagnóstico del fallo

El Filtro PO formal de 4 categorías Cagan **es correcto bibliográficamente pero insuficiente operativamente**. El PO puede operarlo mecánicamente — clasificar como categoría 1 ("acepto y aplico yo") todo lo que un advisor diga si suena académicamente razonable, en lugar de pelearlo con criterio bibliográfico propio.

**El bug operacional**: el PO opera el filtro como **clasificador de "razonable / no razonable"** en lugar de como **decisor de "load-bearing / noise"**.

Cuando un advisor dice "feature X debería declarar dimension Y porque vector STRIDE Z aplica", la pregunta del PO ANTES de "aceptar" no es:
- ❌ *"¿es académicamente correcto este flag?"* (siempre lo suele ser — los advisors son expertos en su dominio)

Sino:
- ✅ *"¿este cambio aporta valor load-bearing al grafo o al JTBD del operador, o es verbosity que infla sin proteger nada?"*

Si el cambio NO es load-bearing → **descartar aunque advisor "tenga razón académicamente"**. El PO sostiene la simplicidad estructural del grafo (Ousterhout *deep modules, simple interfaces*) — más dimensions/cross-links/ADRs/AC no es mejor; es noise si no son load-bearing.

## Ejemplo concreto del incidente

El Security Officer en post-step scope-scan declaró **flag MAYOR**: 9 features deberían añadir dimension `security` porque tienen vectores STRIDE aplicables (CAP-03 R+T, CAP-05 T+S+R, CAP-06 I+D, CAP-10 I+R).

Mi primera pasada (contaminada): clasifiqué como categoría 1 y apliqué `security` a las 9 features.

Mi segunda pasada (con criterio fuerte tras crítica humana):
- **De las 9, solo 3 son load-bearing**:
  - feature-025 (library): integridad bibliográfica = CORE del JTBD del framework. SÍ load-bearing.
  - feature-032 (/status): output visible al humano final agrega vault completo, secret hygiene relevante para adopters externos. SÍ load-bearing.
  - feature-041 (README): debe advertir adopters sobre blast radius del vault=público por diseño. SÍ load-bearing.
- **Las otras 6 son out-of-scope del framework**:
  - feature-015/017/019/026/035: vectores dependientes de "agent comprometido / tampering". **SEM-IA opera con honest-agent assumption explícita** — el framework NO promete autenticación criptográfica entre subagentes, NO promete signing de SKILL.md, NO promete tamper-detection de Progreso entries. Declarar security para vectores out-of-scope es anti-patrón "checkbox security" — infla sin proteger.
  - feature-046: yo mismo lo marqué "debatible — vector R serializable con quality+business". Si el PO marca "debatible" la honestidad indica descartar, no aceptar.

**El insight clave**: el flag de Security Officer ERA académicamente correcto (los vectores STRIDE aplican). Pero **no era load-bearing al JTBD del framework**, porque el framework explícitamente NO promete defender contra esos vectores. Aplicarlo era over-promising auditoría que el producto NO entrega.

Patrón equivalente con otros advisors:
- **Architect** sugirió 4 cross-links cross-feature adicionales: todos eran coupling transitivo válido pero NO load-bearing. Cohn INVEST `I = Independent` requiere coupling **mínimo** declarado, no máximo.
- **Architect** sugirió 2 ADRs latentes adicionales (Filtro PO, modality): ambos ya formalizados en Gaps 6 y 8 del WA-003. NO son decisiones arquitectónicas con alternatives — son comportamiento operativo. Nygard ADRs son para decisiones con alternatives consideradas.

## Bibliografía aplicada al diagnóstico

**Cagan, Inspired** — *"Strong product managers have opinions informed by data but decisions are own. Weak product managers aggregate votes from stakeholders."*

El Filtro PO mecánico es exactamente el patrón "aggregator of votes" — el PO recoge 5 advisor outputs y los suma como si fueran decisiones, en lugar de tomar SU decisión informada por (no determinada por) los advisor outputs.

**Cagan, Empowered** — *"Strong product team has a coherent point of view; collaborates with give-and-take but the PM owns the decision."*

El give-and-take con advisors (subagentes) está bien. La pérdida del coherent point of view es lo que mata. El PO debe llegar al post-step scope-scan con criterio propio sobre QUÉ aporta valor al grafo, y filtrar los advisor outputs CONTRA ese criterio.

**Ousterhout, A Philosophy of Software Design** — *"Modules should be deep, not shallow. Make modules deep by hiding complexity behind simple interfaces."*

Aplicado al grafo SEM-IA: una feature con frontmatter inflado (muchas dimensions, muchos cross-links, muchos ADRs latentes apuntados, muchos AC) NO es feature deep — es feature shallow con verbosidad. Una feature deep tiene JTBD claro, dimensions honestas (las que realmente toca), cross-links mínimos declarados (los load-bearing), y ADRs latentes solo cuando hay decisión arquitectónica real con alternatives.

**Cohn, User Stories Applied** — *INVEST `I = Independent`*: las features deben ser independientes. Coupling apropiado se declara explícitamente; coupling transitivo (B usa A, B también usa C, declaremos B↔C) infla el grafo sin aportar.

## Acción correctiva ejecutada

Tras la crítica del humano, ejecuté pelea fuerte:

1. **Mantuve 6 cambios load-bearing** (de los 13 originales).
2. **Reverté 9 cambios noise from advisor** + 4 metadatos correspondientes.
3. Reescribí la sección "Post-step scope-scan" del discovery doc para reflejar la pelea fuerte (no la versión contaminada).
4. Actualicé entrada Progreso del WA-004 con el registro del incidente + corrección.

Estado final: discovery doc con 7 features declarando security (no 13), 11 ADRs latentes apuntados (no 13), cross-links cross-feature solo donde load-bearing.

## Prevención future

**Heurística adicional al Filtro PO de 4 categorías** (extensión al Gap 6, a aplicar mecánicamente en cada post-step):

> Antes de clasificar un flag de advisor como categoría 1 ("acepto y aplico yo"), aplica el **test de load-bearing**:
>
> 1. ¿El cambio aporta valor que el JTBD del operador (humano o agente) o el grafo no tienen sin él?
> 2. ¿La ausencia del cambio degrada algún criterio observable del framework (anclaje bibliográfico, auditabilidad, navegación del grafo, valor para adopter externo)?
> 3. ¿Está el cambio dentro del scope que el framework realmente promete cubrir? (Anti-anti-patrón: si el framework dice "honest-agent assumption", no declarar security para vectores de agent comprometido — over-promising auditoría inexistente.)
>
> Si los 3 SÍ → categoría 1.
> Si alguno NO → **categoría 2 con razón fuerte** ("descarto porque no es load-bearing, es verbosity") o categoría 3 (diferir si pueda madurar a load-bearing en otro contexto).

**Anclaje del test**: Ousterhout deep modules + Cagan strong PM + Cohn INVEST. **Audita** la honestidad de mi propia pelea — si todas las recomendaciones de advisors caen en categoría 1, el filtro está rompiéndose. Heurística meta: si > 60% de advisor flags caen en categoría 1, sospechar Filtro PO mecánico y volver a pelear con criterio fuerte.

## Referencias

- `vault/shared/sessions/archive/wa-2026-05-12-003.md` — Gap 6 formalizado (Filtro PO 4 categorías base).
- `.claude/agents/product-owner.md` — Modo 1 paso 6b + Modo 2 paso 4 (donde Gap 6 aplica).
- `vault/shared/sessions/active/wa-2026-05-12-004.md` — sección "Step 1 — Post-step scope-scan flat parallel" donde quedó registrado el incidente.

## Aplicabilidad

Este learning aplica a **cualquier rol orquestador ejecutando scope-scan multi-rol** (PO típicamente, Architect cuando orquestra WA `adr` puro, DevOps cuando orquestra WA `pipeline-change`). Cualquier rol que reciba outputs de advisors y los filtre debe aplicar el test de load-bearing, no solo el filtro mecánico de 4 categorías.

**No es learning de implementación de código** (a pesar de vivir en `vault/developer/learnings/`) — es learning de proceso de gestión multi-rol. Considerar futuro: si vault/shared/retros/ se activa, este aprendizaje pertenece allí (cross-rol) o también en `vault/product-owner/discovery/` como nota meta del PO. Mientras tanto vive aquí por decisión humana.
