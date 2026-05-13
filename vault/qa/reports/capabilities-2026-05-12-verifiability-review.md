---
type: report
id: capabilities-2026-05-12-verifiability-review
title: "Verificabilidad-review consolidado del catálogo de 10 capabilities · WA wa-2026-05-12-002"
status: active   # transición aplicada por /verify del WA wa-2026-05-12-002 el 2026-05-12T05:30+02:00
created: 2026-05-12
author: qa
related-wa: wa-2026-05-12-002
references:
  - vault/product-owner/discovery/capabilities-bootstrap-extraction-2026-05-12.md
  - vault/architect/research/capabilities-2026-05-12-viability-review.md
  - vault/product-owner/strategy/cap-01-grafo-declarativo-persistente.md
  - vault/product-owner/strategy/cap-02-multirol-agentes-homologos.md
  - vault/product-owner/strategy/cap-03-working-agreements-sdlc.md
  - vault/product-owner/strategy/cap-04-verificacion-multirol-cruzada.md
  - vault/product-owner/strategy/cap-05-anclaje-bibliografico-skills.md
  - vault/product-owner/strategy/cap-06-visibilidad-operativa.md
  - vault/product-owner/strategy/cap-07-inception-greenfield.md
  - vault/product-owner/strategy/cap-08-portabilidad-multi-harness.md
  - vault/product-owner/strategy/cap-09-adopcion-retroactiva.md
  - vault/product-owner/strategy/cap-10-articulacion-publica.md
bibliography:
  - "Adzic — Specification by Example (AC trazables, criterios observables no aspiracionales)"
  - "Cohn — User Stories Applied (INVEST: testability como condicion de un buen criterio de aceptacion)"
  - "Bass — Software Architecture in Practice (testability como QA; verificabilidad de QAs en implementations)"
  - "Ford et al. — Building Evolutionary Architectures (fitness functions como criterios ejecutables)"
---

# Verificabilidad-review consolidado del catálogo de 10 capabilities

## Contexto

Step-4 del WA `wa-2026-05-12-002` (capability-creation bottom-up). El PO ha formalizado 10 capabilities (step-2) y el Architect ha validado su viability técnica (step-3). Este documento es el output del QA: verificabilidad-review de los criterios observables declarados en las 10 capabilities, con foco exclusivo en la pregunta *"¿puede este criterio guiar un test objetivo en futuros `/verify` de features descompuestas?"* No se cuestiona el contenido de las capabilities ni las decisiones arquitectónicas.

**Aplicación de heurísticas:**
- **Adzic (SbE):** un criterio observable válido es concreto, inequívoco, y puede formularse como escenario Given-When-Then aunque no se escriba en Cucumber. Si solo puede formularse como afirmación subjetiva, es vago.
- **Cohn (INVEST testability):** un criterio es testable si un tester puede diseñar un caso de prueba concreto sin preguntar aclaraciones adicionales al PO.
- **Bass (testability como QA):** los QAs arquitectónicos deben tener umbrales o condiciones de satisfacción precisos para ser verificables en implementaciones.
- **Ford (fitness functions):** los tradeoffs declarados solo son gobernables si tienen umbral ejecutable; sin él, degradan silenciosamente.

## Veredicto global

**Aprueba con condiciones menores.**

Las 10 capabilities tienen criterios observables que, en conjunto, son auditables. Ningún criterio es tautológico. Los 6 criterios de capabilities `operant` (CAP-01 a CAP-07, CAP-10) son testables con tests manuales o automáticos convencionales. Los 2 criterios de capabilities `planned` (CAP-08, CAP-09) son verificables en sus términos pero requieren condición explícita de pre-activación antes de aplicarlos.

Hay **4 condiciones menores** que el QA eleva al PO antes del `/verify` (ninguna bloqueante):

1. CAP-01: criterio omite validación de transiciones de estados — añadir caso negativo.
2. CAP-04: el criterio más rico del catálogo, pero trazabilidad `// @ac-coverage:` queda incompleta sin tool de verificación (dependencia de CAP-08).
3. CAP-05: matching de skills lazy-load es probabilístico — reconocer esto explícitamente en el criterio.
4. CAP-06: umbral `< 2s` para `/status` es el único criterio con threshold concreto en el catálogo; recomendación de añadir umbral análogo a CAP-03 y CAP-07.

---

## Verificabilidad por capability

### CAP-01 · Grafo declarativo persistente

**Criterio observable declarado** (literal): *"Cada nodo nuevo en el vault tiene frontmatter YAML válido y parseable. Cross-links declarados apuntan a nodos existentes (no rotos). Estados del nodo respetan las transiciones canónicas. Wiki-links `[[id]]` en contenido referencian IDs reales del vault."*

**Testabilidad:** testable. Los 4 sub-criterios son discretos y evaluables individualmente. Un test puede abrir cualquier archivo del vault, parsear su frontmatter (falla si YAML inválido), resolver cada ID referenciado (falla si no existe), y trazar las transiciones de estado (falla si hay salto ilegal). CAP-08 automatizará esto vía `sem-ia validate` + `sem-ia check` — hasta entonces, auditoría manual es suficiente.

**Cobertura del job:** cubre. El job declarado es *"persistir y relacionar nodos sin perder coherencia"*; el criterio verifica exactamente las 4 condiciones que hacen ese job sostenible.

**Criterios faltantes sugeridos:**
- Añadir criterio negativo explícito: *"Frontmatter con campo `status` no canónico produce error auditable (no se acepta silenciosamente)."* Actualmente el criterio solo valida el camino feliz; sin caso negativo no se detecta corrupción silenciosa de estados.
- Considerar criterio sobre `operational-status` (campo improvisado, gap 2): ¿qué valores son válidos? El criterio actual no lo cubre.

**Veredicto:** aprueba con condición menor (añadir caso negativo de estados canónicos).

---

### CAP-02 · Operación multi-rol vía agentes IA homólogos

**Criterio observable declarado** (literal): *"Existe agent file conformante para cada rol declarado en `role-catalog.md`. El atajo npm correspondiente arranca sesión que carga el wrapper del rol. El rol es invocable como subagente vía Task tool (test: invocación retorna output estructurado en formato declarado). La identidad declarada en el agent file cita bibliografía verificable en `vault/architect/research/library/`."*

**Testabilidad:** testable. Sub-criterio 1 (existencia de archivos): verificable por `ls` + diff contra role-catalog. Sub-criterio 2 (atajo npm arranca sesión correcta): verificable manualmente. Sub-criterio 3 (invocación subagente retorna output estructurado): verificable con invocación real y validación de estructura YAML/Markdown del output. Sub-criterio 4 (bibliografía en library/): verificable por búsqueda de paths en agent file + existencia de los archivos library.

**Cobertura del job:** cubre el job estructural (roles existen, son invocables, tienen autoridad bibliográfica). El criterio **no cubre** el caso del gap conocido (`vault/developer/CLAUDE.md` pendiente). Esto es correcto y consciente, pero debe documentarse como excepción explícita en el criterio de verificación: *"El criterio aplica a 7 de los 8 roles (developer excluido por gap conocido declarado en notas operativas de CAP-02)."*

**Criterios faltantes sugeridos:**
- Añadir: *"Ningún agent file referencia rol o dimensión que no esté declarado en `role-catalog.md`."* (Valida bidireccionalidad: no solo que existen los archivos, sino que el catálogo y los archivos son consistentes entre sí.)

**Veredicto:** aprueba con ajuste editorial menor (documentar la excepción del Developer en el criterio).

---

### CAP-03 · Coordinación de trabajo vía Working Agreements

**Criterio observable declarado** (literal): *"Cada WA del vault tiene `outcome-type` clasificado del catálogo de `workflows.md`. `steps` declaran `active-role` válido del role-catalog. `closure-criteria` son evaluables objetivamente al `/verify`. `on-close` transitions referencian paths existentes y status válidos. Al cerrar el WA, las transiciones declaradas se aplican y el WA se archiva."*

**Testabilidad:** testable. Sub-criterios 1-4 son estructurales y verificables leyendo frontmatter de WAs del vault + cruzando contra workflows.md y role-catalog.md. Sub-criterio 5 (transiciones aplicadas al cerrar) es verificable a posteriori consultando el archivo archivado y comprobando que los nodos referenciados en `on-close` tienen el status declarado.

**Cobertura del job:** cubre parcialmente. El job es *"coordinar bloques de trabajo multi-rol con scope autorizado, criterios de cierre observables y transiciones declarativas"*. El criterio valida la estructura del WA pero **no valida el scope-allowed/scope-forbidden**: debería añadir criterio *"ningún artefacto escrito en el WA cae fuera de `scope-allowed`"*.

**Criterios faltantes sugeridos:**
- *"Los paths en `scope-allowed` y `scope-forbidden` del WA son verificables (no vacíos, no contradictorios entre sí)."*
- Criterio de performance análogo al de CAP-06: considerar añadir *"backlog-query retorna resultado en tiempo aceptable (< X s) sobre el vault actual"* — para que el tradeoff O(N) tenga umbral concreto antes de degradar silenciosamente.

**Veredicto:** aprueba con condición menor (añadir criterio de scope + umbral de backlog-query).

---

### CAP-04 · Verificación multi-rol cruzada en checkpoints uniformes

**Criterio observable declarado** (literal): *"Todo WA del vault tiene `verifiers-required` derivable del algoritmo `{custodian(d) : d ∈ dimensions-affected}`. Cada step completado tiene post-step scope-scan output registrado en Progreso del WA. `/verify` aplica `on-close` transitions solo si todos los verificadores aprueban. Skills `*-quality-check` y `*-viability-review` se invocan en el contexto que su `description` declara. AC trazables a tests vía `// @ac-coverage:` cuando hay tests."*

**Testabilidad:** testable con matices. Sub-criterios 1, 3 son testables mecánicamente (derivar verifiers desde dimensions-affected y comparar con verifiers-required declarado; verificar que /verify solo avanza con todos los aprobados). Sub-criterio 2 es testable por presencia de entrada de Progreso en cada step con `status: done`. Sub-criterio 4 (matching de skills por description) es probabilístico — ver zona gris Architect #3. Sub-criterio 5 (`// @ac-coverage:`) es testable cuando existen tests, pero sin tool de verificación (feature `sem-ia check coverage` de CAP-08) es revisión manual.

**Cobertura del job:** cubre bien el job de verificación cruzada. El criterio es el más completo del catálogo. Observación: el criterio debería declarar explícitamente que el sub-criterio de `// @ac-coverage:` es **condicional** (*"cuando hay tests"*) para que no parezca incumplido en WAs de fases discovery/design donde no hay tests.

**Criterios faltantes sugeridos:**
- *"El algoritmo `verifiers-required` se aplica sin override manual que contradiga las dimensions-affected declaradas."* (Valida que no se añaden ni eliminan verifiers ad-hoc sin actualizar dimensions-affected correspondientes.)

**Veredicto:** aprueba. El criterio es suficiente y bien formulado. La condicionalidad del AC-coverage se puede aclarar editorialmente.

---

### CAP-05 · Anclaje bibliográfico auditable mediante skills empaquetadas

**Criterio observable declarado** (literal): *"Cada skill nueva incluye en su SKILL.md sección `bibliographic foundation` con paths a `library/`. Cada decisión significativa (en agent file, capability, ADR, audit) cita autor + obra + año. Las 18 notas de `library/` están actualizadas (sin contradicciones internas + sin links rotos). INDEX.md está sincronizado con el contenido real de `library/`. `_pending-later.md` se mantiene como roadmap de skills futuras con bibliografía ya identificada."*

**Testabilidad:** parcial. Sub-criterios 1 (sección en SKILL.md), 3 (notas sin links rotos), 4 (INDEX sincronizado) son testables mecánicamente. Sub-criterio 2 ("cada decisión significativa cita autor + obra + año") es el más difícil: *"decisión significativa"* no está definida operativamente — ¿qué distingue una decisión significativa de una menor? Sin esta definición, dos auditores distintos pueden discrepar sobre qué debe citarse. Sub-criterio 5 (`_pending-later.md` mantenido) es verificable por lectura del archivo.

**Cobertura del job:** cubre el job de auditabilidad bibliográfica. El gap es la definición de "decisión significativa".

**Criterios faltantes sugeridos:**
- *"Cada campo de frontmatter de un agent file, capability file, o ADR que introduce un concepto bibliográfico (QA Bass, tactic, heurística Nielsen, principio Cagan, etc.) tiene la obra citada en `fundamento-bibliografico` del mismo archivo."* Esto es más concreto que "decisión significativa" y testable.
- Añadir reconocimiento explícito de que el matching de lazy-load es probabilístico: *"El criterio de 'skills se invocan cuando el contexto matchea su description' se verifica por análisis de casos manuales representativos, no por garantía determinística del harness."* Esto evita que un futuro auditor marque como incumplimiento el hecho de que una skill no se invocó en un caso edge.

**Veredicto:** aprueba con condición menor (precisar "decisión significativa" + reconocer probabilismo del lazy-load en el criterio).

---

### CAP-06 · Visibilidad operativa del estado y progreso

**Criterio observable declarado** (literal): *"`/status` retorna en tiempo aceptable (esperable < 2s) panorámica completa (subgrafo + WAs + backlog + features + ADRs por status). `/wa` retorna detalle del WA activo aplicable al contexto del rol. `/sessions` lista modos de trabajo + atajos disponibles. Cada WA activo tiene Progreso entries para cada step completado. Ritual de inicio del PO ejecuta lecturas declaradas en agent file y presenta panorámica antes de procesar propuesta humana."*

**Testabilidad:** testable. Este es el criterio con el umbral más concreto del catálogo (`< 2s`), lo que lo hace el más robusto desde la perspectiva de Ford fitness function. Los demás sub-criterios son verificables por inspección del output de cada slash command y del agent file del PO.

**Cobertura del job:** cubre bien el job. El criterio valida visibilidad del proyecto (sub-criterios 1-4) y visibilidad de la sesión (sub-criterio 5 — ritual PO). El criterio de ritual es verificable porque el agent file PO declara las lecturas exactas que deben ocurrir.

**Criterios faltantes sugeridos:**
- *"`/status` diferencia explícitamente WAs en track Discovery de WAs en track Delivery en su output."* El criterio actual valida que retorna información pero no que la organiza según la vista Dual Track declarada en el enunciado.

**Veredicto:** aprueba. El criterio es el más maduro del catálogo — tiene umbral concreto, cubre el job, no es tautológico.

---

### CAP-07 · Inception greenfield protocol-compliant

**Criterio observable declarado** (literal): *"`npm run sem` sobre vault vacío arranca sesión PO en Modo 1. El PO detecta el vault vacío y propone cadena de WAs (no asume contexto previo). La cadena propuesta es ordenada top-down (vision → goals → capabilities → features). Cada WA de la cadena usa template de `workflows.md` (no protocolo paralelo). Al cerrar la inception, el vault tiene grafo estructuralmente sano (visión active, goals active, capabilities active iniciales)."*

**Testabilidad:** testable. Sub-criterios 1-4 son testables con un escenario de prueba manual (arrancar sobre vault vacío y observar comportamiento del PO). Sub-criterio 5 es testable a posteriori comparando el vault resultante contra la estructura esperada. El escenario completo es costoso en tiempo (requiere ejecutar toda la cadena de inception), pero es un test de aceptación legítimo.

**Cobertura del job:** cubre bien el job. El criterio valida exactamente la propiedad diferenciadora de CAP-07: que la inception usa los mismos templates que el mantenimiento, y que al cerrar el grafo está estructuralmente sano.

**Criterios faltantes sugeridos:**
- *"El PO no propone protocolo ad-hoc fuera de `workflows.md` (verificable por ausencia de steps sin `outcome-type` en el catálogo)."* Este es el contraejemplo negativo del sub-criterio 4 que lo hace más robusto.
- Considerar umbral: *"La cadena inception para proyecto simple (visión + 3 goals + 3 capabilities) cierra en N sesiones"* — para detectar si el protocolo se ha vuelto operativamente prohibitivo. No obligatorio hoy, candidato a fitness function futura.

**Veredicto:** aprueba.

---

### CAP-08 · Portabilidad multi-harness y distribución como `@sem-ia/cli` [PLANNED]

**Criterio observable declarado** (literal): *"`npx @sem-ia/cli init --harness=claude-code` sobre directorio vacío produce estructura conforme. `sem-ia validate <path-frontmatter>` retorna OK/FAIL según schema JSON. `sem-ia check` detecta cross-links rotos en el vault del adopter. `sem-ia check coverage` calcula cobertura AC ↔ tests cuando existen archivos `// @ac-coverage:`. El paquete publicado tiene LICENSE Apache 2.0 + `package.json` con author/license/repository declarados. Tests de integridad del paquete pasan en CI antes de publish."*

**Testabilidad:** testable — cuando la capability sea `operant`. Los 6 sub-criterios son concretos y ejecutables automáticamente mediante tests de integración estándar (npm install, CLI invocations, schema validation assertions, CI pass/fail).

**Cobertura del job:** cubre bien el job de distribución y herramientas de auditoría. El criterio es correcto y suficientemente concreto para guiar feature-design posterior.

**Caso especial `planned`:** el criterio tiene condición implícita de pre-activación ("cuando sea operant"). QA recomienda hacerla explícita: añadir prefacio *"Cuando `operational-status` pase a `operant` (tras ADR(s) + threat-model formal): ..."* Esto evita que un auditor futuro marque el criterio como incumplido mientras la capability es `planned`.

**Criterios faltantes sugeridos:**
- *"Adapter de Claude Code pasa de `src/adapters/claude-code/` al dogfooding `.claude/` sin discrepancias (build step o equivalente)."* Este criterio valida el tradeoff de no-duplicación declarado en ADR-latente-006 — es testable y cubre el riesgo de drift entre src/ y el dogfooding.
- *"Ningún archivo en `src/universal/` importa de `src/adapters/<harness>/`."* Fitness function del Dependency Rule de Martin — ejecutable con linting estático.

**Veredicto:** aprueba con recomendación de hacer explícita la condición de pre-activación `planned → operant`.

---

### CAP-09 · Adopción retroactiva desde proyecto pre-existente [PLANNED]

**Criterio observable declarado** (literal): *"`/adopt <path>` arranca archeology walk del directorio destino sin tocar nada fuera de él. Walk respeta denylist por defecto (no lee `.env`, `*.pem`, credenciales, `.aws/`, `.ssh/`, `secrets/`). Walk escanea patrones sensibles (AKIA, ghp_, sk-, PRIVATE KEY) antes de citar fragmento. Frontmatter de cualquier nodo derivado incluye `derived-from` con path+versión. Contenidos citados desde código del adopter están redactados por defecto. Threat-model formal del walk existe y AC-S* derivados están en spec."*

**Testabilidad:** testable — cuando la capability sea `operant`. Los 6 sub-criterios son concretos. Sub-criterio 1 (aislamiento del walk) es testable con directorio de prueba y verificación de que ningún archivo fuera del path fue modificado. Sub-criterio 2 (denylist) es testable creando archivos trampa en los paths listados y verificando que no son leídos. Sub-criterio 3 (pattern scanning) es testable con fixtures que contienen patrones conocidos. Sub-criterios 4-6 son verificables en el output del walk.

**Cobertura del job:** cubre el job de seguridad del walk (aspectos más críticos: aislamiento, denylist, pattern scanning, trazabilidad `derived-from`). Sub-criterio 6 (threat-model formal + AC-S*) es el más importante y correcto — declara que el criterio completo requiere que exista un threat-model previo del que derivar AC-S*, lo cual es la dependencia correcta de ordering.

**Caso especial `planned`:** igual que CAP-08, la condición de pre-activación debe ser explícita.

**Criterios faltantes sugeridos:**
- *"Walk es idempotente: ejecutar `/adopt <path>` dos veces sobre el mismo directorio sin cambios produce el mismo vault que ejecutarlo una vez."* Valida el tradeoff de idempotencia declarado en el capability file — es testable con fixture fijo.
- Flag Architect sobre `business` dimension (licensing del adopter): cuando se descomponga en features, añadir criterio *"Walk de código con licencia incompatible (GPL) no introduce en el vault fragmentos que hereden esa licencia."* No obligatorio hoy (planned), pero debe ser AC-B* cuando el threat-model se formalice.

**Veredicto:** aprueba con recomendación de hacer explícita la condición `planned → operant` y añadir criterio de idempotencia.

---

### CAP-10 · Articulación pública del framework

**Criterio observable declarado** (literal): *"README.md raíz cubre: visión + propuesta + estructura + onboarding + pendientes. Governance docs (5) están sincronizados con el bootstrap actual (sin contradicciones internas). bootstrap-summary.md está actualizado con decisiones tomadas hasta la fecha de revisión. INDEX.md de library refleja las notas reales presentes. LICENSE Apache 2.0 sin riesgo viral, compatible con distribución. Docs son legibles a evaluador no-practicante (legibilidad estándar, no WCAG AA formal). Jerga interna explicada o glosada cuando aparece por primera vez en docs públicos."*

**Testabilidad:** parcial. Sub-criterios 1 (README cubre secciones), 4 (INDEX sincronizado), 5 (LICENSE) son testables mecánicamente — checklist o grep. Sub-criterio 2 ("governance docs sincronizados sin contradicciones") es testable pero costoso: requiere revisión cross-document manual o semi-automática. Sub-criterio 7 ("jerga explicada cuando aparece por primera vez") es el más difícil de testear objetivamente — *"por primera vez"* en docs públicos depende del orden de lectura del lector, que no es predecible.

**Cobertura del job:** cubre bien el job de articulación pública. El criterio captura tanto la estructura (qué docs existen) como la calidad mínima de legibilidad.

**Criterios faltantes sugeridos:**
- *"Governance docs (5) no contradicen entre sí en ninguna definición clave (roles, fases SDLC, estados canónicos, dimensiones)."* Esta es la versión más testable del sub-criterio 2 — acota qué significa "sincronizados".
- *"Cambios en el bootstrap (nuevas capabilities, ADRs aprobados, fases SDLC añadidas) se reflejan en al menos uno de los docs públicos de CAP-10 dentro del mismo WA de /verify."* Esto añade un criterio de mantenibilidad temporal que cierra el bucle con el tradeoff "docs verbose con coste de mantenimiento".

**Veredicto:** aprueba con condición menor (precisar sub-criterio de "sincronizados" y añadir criterio de mantenibilidad temporal).

---

## Zonas grises identificadas

### Zona gris 1 (Architect) — CAP-06: umbral `< 2s` para `/status`

**Descripción:** el criterio declara *"tiempo aceptable (esperable < 2s)"* para la respuesta de `/status`. El `esperable` introduce ambigüedad — ¿es objetivo o aspiracional?

**Propuesta de resolución:** reemplazar *"esperable < 2s"* por *"< 2s en el 95% de invocaciones sobre un vault de hasta 200 nodos"*. Esto es una fitness function ejecutable (Ford) con condición de contexto explícita. Sin condición de contexto, el umbral degrada silenciosamente cuando el vault crece.

---

### Zona gris 2 (Architect) — CAP-08/CAP-09 son `planned`; criterios "cuando sea operant"

**Descripción:** los criterios de CAP-08 y CAP-09 asumen que la capability ya es `operant`. Si un auditor ejecuta `/verify` sobre un WA que toca CAP-08 o CAP-09 mientras siguen siendo `planned`, el criterio es inaplicable y podría interpretarse como incumplido.

**Propuesta de resolución:** añadir prefacio estándar a los criterios observables de capabilities `planned`: *"Criterio pre-condicionado: aplica cuando `operational-status` pase a `operant` (requiere ADR(s) + threat-model formal previos). Hasta entonces, el criterio observable es: 'La capability declara `operational-status: planned` y el WA asociado documenta en su Progreso qué falta para pasar a `operant`'."* Esto hace que el criterio tenga valor auditable incluso en estado `planned`.

---

### Zona gris 3 (Architect) — CAP-05: matching de skill lazy-load es probabilístico

**Descripción:** el sub-criterio *"skills se invocan en el contexto que su `description` declara"* de CAP-04 (y la explicación en CAP-05) admite que el matching es probabilístico. Si en un futuro `/verify` una skill no se invocó cuando debería haberlo hecho, ¿es incumplimiento del criterio?

**Propuesta de resolución:** añadir al criterio de CAP-05 y CAP-04 la aclaración: *"El matching es probabilístico por naturaleza del harness; el criterio se verifica mediante revisión de N casos representativos (mínimo 3 por skill) donde el contexto triggering esté bien construido, no por cobertura exhaustiva de todos los contextos posibles."* Esto convierte el criterio de aspiracional a testable con casos concretos.

---

### Zona gris 4 (Architect) — AC traceability `// @ac-coverage:` sin tool de verificación hasta CAP-08

**Descripción:** CAP-04 declara `// @ac-coverage:` como tactic de AC traceability, con el criterio observable de que es verificable vía `sem-ia check coverage` de CAP-08. Pero CAP-08 es `planned`. Hasta que exista la tool, la verificación es manual y puede ser inconsistente.

**Propuesta de resolución:** para el periodo hasta que CAP-08 sea `operant`, definir criterio provisional: *"En cada WA de `feature-build` o `bugfix`, el QA verifica manualmente que cada AC declarado en specs tiene al menos un archivo de test con `// @ac-coverage: AC-X` correspondiente. Esta verificación queda registrada en `vault/qa/reports/<feature-id>-coverage.md`."* Esto hace la verificación auditable sin depender de la tool automatizada.

---

### Zona gris 5 (Architect) — `vault/developer/CLAUDE.md` pendiente y verificabilidad de CAP-02

**Descripción:** CAP-02 declara como criterio *"existe agent file conformante para cada rol declarado en `role-catalog.md`"*. `role-catalog.md` incluye el Developer. Pero `vault/developer/CLAUDE.md` no existe. ¿Cómo se audita esto en `/verify` sin que falle el criterio?

**Propuesta de resolución QA (confirmando recomendación Architect de aparcar):** el criterio de CAP-02 debe tener excepción explícita documentada: *"Aplica a 7 de los 8 roles. El Developer (`vault/developer/CLAUDE.md`) está en lista de excepciones conocidas (gap declarado en notas operativas de CAP-02) hasta que exista `src/` con código implementado bajo SEM-IA real. Este gap se cierra en WA dedicado; no bloquea `operational-status: operant`."* Con esta excepción documentada en el criterio observable, el auditor puede verificar sin ambigüedad.

---

### Zona gris 6 (QA — nueva) — Criterios de capabilities `operant` no distinguen entre verificación en WA `feature-design` vs `feature-build`

**Descripción:** los criterios observables de las 10 capabilities dicen *"una feature descompuesta de CAP-XX es verificable si cumple..."*, pero no especifican en qué fase del ciclo se verifica cada sub-criterio. Por ejemplo, en `feature-design` no hay tests aún, pero el criterio de CAP-04 incluye `// @ac-coverage:`. En `feature-build`, el criterio de CAP-07 sobre "grafo estructuralmente sano al cerrar inception" ya está consumado hace tiempo.

**Propuesta de resolución:** el PO, al descomponer cada capability en features (en el WA `feature-design` correspondiente), debería mapear qué sub-criterios del criterio observable se verifican en `feature-design` (estructura, presencia de artefactos, AC declarados) y cuáles se verifican en `feature-build` (funcionalidad implementada, tests con `@ac-coverage:`). Este mapping puede vivir en la sección `verifiers-required` del WA o en el closure-criteria del feature-design. No requiere modificar los criterios observables de las capabilities — es trabajo del WA que los consuma.

---

## AC traceability transversal

El catálogo de 10 capabilities, en conjunto, **habilita trazabilidad AC ↔ tests** cuando se descompongan en features con specs Gherkin, bajo las siguientes condiciones:

**Lo que funciona hoy:**
- La convención `// @ac-coverage: AC-X` está declarada en CAP-04 como tactic operativa. No es capability propia — es protocolo transversal que aplica a todos los WAs `feature-build`.
- Los criterios observables de las 10 capabilities son suficientemente concretos para generar AC Gherkin en futuros `feature-design`. Por ejemplo, el criterio de CAP-01 genera naturalmente ACs como: *"Given un vault con nodo X, When el frontmatter tiene campo status no canónico, Then `sem-ia validate` retorna FAIL."*

**Lo que es deuda consciente:**
- La verificación de que los `// @ac-coverage:` existen para cada AC es manual hasta que CAP-08 sea `operant` (zona gris 4).
- Los criterios de capabilities no distinguen fase de verificación (zona gris 6) — esto se resuelve en el WA de `feature-design`, no en los capability files.

**Observación cross-cutting:** las capabilities con `dimensions-affected: [product, quality]` (CAP-05) y `[product, quality, technical]` (CAP-04) son las que más directamente habilitan la trazabilidad AC en el sistema. CAP-04 declara el protocolo; CAP-05 garantiza que los criterios están anclados bibliográficamente (Adzic SbE). El resto de capabilities son sujetos de verificación, no mecanismos de ella.

---

## Flags emergentes (para `/verify` del WA-002)

| # | Flag | Severity | Blocking |
|---|---|---|---|
| F-QA-1 | CAP-01: ausencia de caso negativo en criterio de estados canónicos | minor | No |
| F-QA-2 | CAP-02: excepción del Developer debe quedar explícita en el criterio observable | minor | No |
| F-QA-3 | CAP-03: criterio omite verificación de scope-allowed/forbidden + umbral backlog-query | minor | No |
| F-QA-4 | CAP-05: "decisión significativa" no operativamente definida; lazy-load probabilismo no reconocido en criterio | minor | No |
| F-QA-5 | CAP-08 + CAP-09: condición de pre-activación `planned → operant` debe ser explícita en criterio | minor | No |
| F-QA-6 | AC traceability `// @ac-coverage:` es manual sin tool hasta CAP-08 `operant` — definir procedimiento provisional | minor | No |
| F-QA-7 | Zona gris 6 (nueva): criterios no especifican fase de verificación — resolver en WA `feature-design`, no en capability files | informational | No |

Ningún flag es bloqueante para el `/verify` del WA-002. Los criterios declarados son suficientes para guiar feature-design futuro. Los flags son ajustes editoriales o procedimientos provisionales que el PO puede aparcar o incorporar en el WA de mejoras del sistema (los 6 gaps del anexo).

---

## Recomendación al PO

El catálogo de 10 capabilities tiene criterios observables que cumplen las condiciones mínimas de verificabilidad para un catálogo en fase discovery: son concretos, no-tautológicos, alineados con el job JTBD de cada capability, y suficientes para guiar la decomposición en features con specs Gherkin. Desde la perspectiva del QA, el `/verify` del WA-002 puede proceder sin bloqueantes.

La recomendación principal es incorporar en el WA de gaps del sistema (el que procesará los 6 gaps del anexo) los ajustes editoriales señalados en este review: hacer explícita la condición `planned → operant` en CAP-08 y CAP-09, documentar la excepción del Developer en CAP-02, y precisar "decisión significativa" en CAP-05. Son cambios de bajo coste (edición de criterios observables en los capability files correspondientes) que reducen ambigüedad para auditores futuros.

La zona gris más relevante operativamente es la 4 (AC traceability manual hasta CAP-08 `operant`). La recomendación es definir el procedimiento provisional de verificación manual en el agent file del QA o en un documento de procedimientos de calidad, de modo que los WAs `feature-build` futuros tengan protocolo claro antes de que exista la tool automatizada. Esto no requiere WA dedicado — puede hacerse como ajuste al protocolo del QA en el mismo WA de gaps.

La decisión de no añadir "framework-regression-detection" como capability `planned` se confirma desde el ángulo QA: es un concern válido pero no cumple los 4 criterios de capability fuerte en este momento (no tiene cohesión interna suficiente, solaparía con features de CAP-04 sobre enforcement de protocolo). Procede como nota en el backlog de gaps para evaluar cuando el sistema madure.
