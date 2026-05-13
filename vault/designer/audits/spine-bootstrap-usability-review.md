---
type: audit
id: spine-bootstrap-usability-review
title: "Usability review consolidado — espina dorsal bootstrap WA-005"
status: active
created: 2026-05-13
author: designer
related-wa: wa-2026-05-13-005
dimensions-affected: [usability]
citas-bibliograficas: [Nielsen, Cooper, Norman]
features-auditadas:
  - feature-010-entry-point-por-rol
  - feature-032-slash-status
  - feature-033-slash-wa
  - feature-034-slash-sessions
  - feature-035-ritual-inicio-po
  - feature-036-orientacion-rol
  - feature-038-po-modo-1
  - feature-041-readme-onboarding
  - feature-044-glosario-publico
  - feature-045-ruta-lectura-audiencia
---

# Usability review consolidado — espina dorsal bootstrap WA-005

> Aplicado como subagente step-4 del WA-2026-05-13-005. Base bibliográfica: Nielsen 10 heurísticas (1994), Cooper *About Face* waypoints, Norman *The Design of Everyday Things* (conceptual model, affordances, feedback).
> Operador DOBLE: humano (ingeniero adoptante) + agente (PO, Architect, etc.). Ambos evaluados.

---

## 1. Checklist Nielsen/Cooper/Norman por feature relevante

### feature-010 — Entry-point por rol (Nielsen #7)

| Heurística | Aplicación | Veredicto |
|---|---|---|
| #7 Flexibility + efficiency of use | 9 atajos npm como aceleradores expertos. El experto usa `npm run arch`; el newcomer descubre en README/CLAUDE.md (AC-B2, AC-B3). Gradiente novato→experto cubierto. | PASA |
| #6 Recognition over recall | Los nombres (`sem`, `po`, `arch`, `des`, etc.) son nemotécnicos directos del rol. Verificable: AC-A1. | PASA |
| #4 Consistency | 9 atajos en pattern uniforme `npm run <abreviatura>`. Pattern consistente. | PASA |
| Cooper waypoints | El operador siempre sabe cómo arrancar (entrada por npm run). **Gap menor**: wrapper `vault/developer/CLAUDE.md` ausente — declarado explícitamente en AC-C1 como "gap menor declarado". Gap conocido y honesto. | PASA con nota |

**Severidad**: ningún hallazgo bloqueante. Gap developer wrapper reconocido en la spec.

---

### feature-032 — Slash `/status` (Nielsen #1)

| Heurística | Aplicación | Veredicto |
|---|---|---|
| #1 Visibility of system status | 6 secciones canónicas siempre presentes (AC-A1). Operador nunca ve output vacío sin explicación (AC-B3 cubre "sin WAs activos"). Dual Track visible (AC-B2). | PASA |
| #2 Match with real world | Terminología `track`, `backlog`, `Dual Track` mapea al modelo mental Cagan/Patton que el operador adoptó. Evaluar si newcomer necesita glosario — remitido a feature-044. | PASA condicional a feature-044 |
| #6 Recognition over recall | `/status` produce estado snapshot sin que el operador recuerde qué hay en el vault. Fundamento Nielsen correcto y bien materializado en AC. | PASA |

**Severidad**: ningún hallazgo bloqueante. Dependencia correctamente declarada en `also-relates-to` (feature-044 glosario).

---

### feature-033 — Slash `/wa` (Nielsen #1 + #9)

| Heurística | Aplicación | Veredicto |
|---|---|---|
| #1 Visibility of system status | AC-A2 detalla output estructurado (steps con status, Progreso entries, próximo step). Operador sabe exactamente dónde está en el WA. | PASA |
| #9 Help users recognize, diagnose, recover from errors | AC-A3 cubre "sin WA activo" con mensaje consistente. Recovery documentado. | PASA |
| Norman feedback | El slash devuelve estado del sistema (no silencio). Patrón de feedback correcto para agente que lee el output. | PASA |
| **Flag medio**: `also-relates-to: []` en frontmatter | feature-033 no declara ningún cross-link, pero las specs (spec-033-B AC-B1/B2/B3) revelan dependencia funcional con: (a) feature-035 ritual inicio PO — el ritual lee WA vía `/wa`-like; (b) feature-018 /scope-scan — el PO consulta WA antes de convocar scope-scan; (c) feature-019 /verify — el verify lee WA para aplicar closure-criteria. La ausencia de `also-relates-to` no rompe la spec (AC son verificables) pero degrada trazabilidad del grafo. | FLAG MEDIO |

**Severidad**: 1 flag medio (cross-links ausentes en frontmatter — no bloquea usability pero afecta coherencia del grafo).

---

### feature-034 — Slash `/sessions` (Nielsen #6)

| Heurística | Aplicación | Veredicto |
|---|---|---|
| #6 Recognition over recall | AC-A3 verifica que cada rol tiene descripción "cuándo invocar". Reduce recall del operador alternando entre sesiones. | PASA |
| #7 Flexibility + efficiency | Un solo slash presenta el catálogo completo de 8 roles. Experto ya sabe (no lo usa); novato lo necesita (lo encuentra). | PASA |
| Cooper waypoints | story-034-B (filtrar por dominio) declarada como extensión futura. El MVP actual (8 roles en plano) es suficiente para el cognitive load actual. Decisión conservadora correcta — Cohn `S = Small` preservado. | PASA |
| #4 Consistency | También declarado `also-relates-to: cap-02-multirol-agentes-homologos` en body. Correcto: los 8 roles existen en CAP-B. | PASA |

**Severidad**: ningún hallazgo.

---

### feature-035 — Ritual de inicio PO (Nielsen #1 + Norman)

| Heurística | Aplicación | Veredicto |
|---|---|---|
| #1 Visibility of system status | El ritual produce panorámica en 6 secciones canónicas (AC-B1) antes de pedir input al humano. El sistema informa su estado antes de esperar acción. | PASA |
| Norman conceptual model transfer | Panorámica materializa el modelo mental del framework para el humano: visión → goals → capabilities → WAs → backlog. El operador humano puede leer el estado del sistema en términos del modelo conceptual aprendido. | PASA |
| Norman feedback | AC-B2 requiere que el PO termine con pregunta abierta ("Qué quieres hacer?"). Feedback + señal de espera explícita. | PASA |
| Norman error prevention | AC-B3 cubre vault vacío con mensaje orientador ("Sin WAs activos · Sin Backlog"). Previene que el agente improvise sobre vacío sin señalarlo. | PASA |
| `also-relates-to` en body vs frontmatter | Body declara cross-links con feature-038 y feature-039 en texto narrativo, pero el frontmatter YAML `also-relates-to` está vacío (verificado). | FLAG MEDIO |

**Severidad**: 1 flag medio (mismo patrón que feature-033 — cross-links narrativos sin formalizar en frontmatter YAML).

---

### feature-036 — Orientación qué rol abrir (Nielsen #6 + #7 + #9)

| Heurística | Aplicación | Veredicto |
|---|---|---|
| #6 Recognition over recall | AC-A1 verifica criterio "si dudas" en CLAUDE.md raíz. Operador reconoce sin recordar. | PASA |
| #7 Flexibility | story-036-A (consulta previa) + story-036-B (recovery si ya en sesión equivocada) cubre novato que pregunta antes + experto que corrige sobre la marcha. | PASA |
| #9 Help users recognize, diagnose, recover from errors | story-036-B es la materialización directa de Nielsen #9 como AC verificable. AC-B1/B2/B3 establecen: rol detecta scope ajeno → comunica recovery → no ejecuta dominio ajeno. Heurística bien cubierta. | PASA — hallazgo positivo |
| Cooper waypoints | En cada punto de ambigüedad el operador recibe orientación concreta (tabla conduzco/delego en PO agent file). | PASA |

**Severidad**: ningún hallazgo bloqueante. Esta feature es la más completa en cobertura Nielsen — AC-B3 (no ejecutar dominio ajeno) previene un error silencioso grave.

---

### feature-038 — PO Modo 1 (Norman conceptual model transfer)

| Heurística | Aplicación | Veredicto |
|---|---|---|
| Norman conceptual model | PO Modo 1 es la primera interacción del agente con el sistema. El protocolo de 10 pasos materializa el conceptual model: la "imagen" del sistema que el PO construye y proyecta al humano. Paso 1 = ritual (feature-035); pasos 2-3 = escucha + clasifica; pasos 4-7 = decide + scope-scan + filtro + drafta WA; paso 8-9 = presenta + confirma; paso 10 = handoff. | PASA |
| #1 Visibility of system status | AC-A2 fuerza clasificación explícita vía `workflows.md` (no intuición). Operador/agente conoce el estado del sistema antes de actuar. | PASA |
| #5 Error prevention | AC-A1 fuerza clarificación de ambigüedades antes de proceder. El PO NO drafta WA con propuesta ambigua sin clarificar. | PASA |
| Norman affordances | El protocolo declarativo de 10 pasos es la affordance del rol: le dice qué puede hacer y en qué orden. Sin él, el PO improvisa (anti-patrón explícito). | PASA |
| **Flag bajo**: cognitive load del protocolo | 10 pasos declarados. Para el operador agente es carga mínima (lee el protocolo). Para el operador humano que lee el agent file: 10 pasos es denso pero está justificado (complejidad inherente del sistema). No es reducible sin perder precisión. | FLAG BAJO — informativo |

**Severidad**: 1 flag bajo informativo (10 pasos densos — no reducibles sin pérdida semántica; recomendación: mantener pero con formato visual claro en el agent file).

---

### feature-041 — README onboarding (Nielsen #10)

| Heurística | Aplicación | Veredicto |
|---|---|---|
| #10 Help and documentation | AC-A1 verifica tesis en primeras 50 líneas. AC-A3 verifica "Cómo arrancar". El newcomer encuentra orientación sin leer linealmente. | PASA |
| #2 Match with real world | AC-B1/B2 verifican citas bibliográficas en formato legible `(Autor, Año, Obra)`. Evaluador académico no-practicante puede validar fuentes. | PASA |
| Cooper progressive disclosure | feature-045 (ruta lectura) es la materialización de progressive disclosure — el README no es lineal. **Dependencia bien declarada**: `also-relates-to: [feature-044, feature-045]` en frontmatter. | PASA |
| **Flag bajo**: README no existe aún | feature-041 especifica el JTBD del README pero el artefacto físico se construye en un WA `feature-build` posterior (scope-forbidden en este WA). Los AC son verificables post-implementación. La spec es correcta (especifica comportamiento observable, no implementación). | FLAG BAJO — scope intencional |

**Severidad**: 1 flag bajo por scope intencional (no bloqueante; reconocido en WA frontmatter).

---

### feature-044 — Glosario público (Nielsen #2 + #4 + #10)

| Heurística | Aplicación | Veredicto |
|---|---|---|
| #2 Match between system and real world | Glosario reduce brecha entre jerga SEM-IA y lenguaje del operador newcomer. AC-A3 requiere cada entrada con definición + ejemplo + cross-link. Ejemplo concreto es key para Nielsen #2. | PASA |
| #4 Consistency and standards | AC-A2 requiere ≥4 categorías consistentes. Estructuración sistemática del vocabulario. | PASA |
| #10 Help and documentation | AC-B1/B2/B3 especifican mecanismo de acceso desde README (primera aparición + sección "Términos"). El glosario es accesible desde el punto de entrada. | PASA |
| Cooper waypoints | En cada punto de confusión terminológica el operador tiene ruta a la definición. `also-relates-to` con feature-013 y feature-009 (Nivel 4) declara que el glosario cubre términos de esos artefactos. | PASA |
| **Flag bajo**: glosario futuro | Igual que feature-041: el glosario físico se construye en WA `feature-build` posterior. Los AC de spec-044-A/B son verificables post-build. Scope intencional del WA-005. | FLAG BAJO — scope intencional |

**Severidad**: 1 flag bajo por scope intencional.

---

### feature-045 — Ruta lectura por audiencia (Nielsen #10 + Cooper)

| Heurística | Aplicación | Veredicto |
|---|---|---|
| #10 Help and documentation | AC-A1/A2/A3 verifican sección "Cómo leer este repo" con ≥3 rutas y archivos en orden. Progressive disclosure materializado. | PASA |
| Cooper *About Face* progressive disclosure | AC-B3 establece que cada ruta cubre ~60-70% del valor para esa audiencia (no exhaustiva). Decisión de diseño correcta — progressive disclosure no es completitud, es orientación óptima por audiencia. | PASA |
| #7 Flexibility | 3 rutas distintas (técnica/académica/adoptante) para 3 perfiles de operador. Cada ruta tiene acción siguiente concreta (AC-B2). | PASA |
| `also-relates-to: [feature-044]` | Dependencia correctamente declarada. Ruta lectura y glosario se complementan en el flujo newcomer. | PASA |

**Severidad**: ningún hallazgo bloqueante.

---

## 2. Validación coherencia del flujo del operador

El Bloque 2 del discovery doc `spine-bootstrap-2026-05-13.md` define 6 fases + 6 insights cross-cap. Valido que los `also-relates-to` declarados en features relevantes reflejan esos insights:

| Insight Bloque 2 | Feature(s) esperada(s) | Cross-link declarado | Estado |
|---|---|---|---|
| Insight 1: Onboarding y CAP-J indistinguibles | feature-041 + 044 + 045 con parent CAP-J | feature-041: `also-relates-to: [feature-044, feature-045]`. feature-044: cross-links a feature-009 y feature-013. feature-045: cross-link a feature-044. | CORRECTO |
| Insight 2: Inception y CAP-F co-emergentes | feature-035 (ritual, parent CAP-F) + feature-038 (Modo 1, parent CAP-G) deben cruzarse | feature-035 body declara `also-relates-to: feature-038` (narrativo). Frontmatter YAML de feature-035 vacío. feature-038: `also-relates-to: [feature-039]` — no declara feature-035. | GAP: cross-link bidireccional no formalizado en YAML |
| Insight 3: Scope-scan y CAP-D desde dos lentes | feature-018/019 (CAP-D) con cross-link a CAP-F | Fuera del scope de usability audit directo (features sin dimensión usability). Observado en WA Progreso: feature-032 `also-relates-to: cap-06` declarado. | OK para este audit |
| Insight 4: Step active cruza 4 caps | feature-033 /wa (CAP-F) debería cruzar CAP-C + CAP-B | feature-033 `also-relates-to: []` — vacío. Debería incluir al menos `cap-03-working-agreements-sdlc`. | GAP: cross-link ausente |
| Insight 5: Sign-off es CAP-D + CAP-A | feature-019 /verify (sin dimensión usability) — fuera de scope directo | No auditado por este rol. | Fuera de scope |
| Insight 6: Dual Track emerge de CAP-C + CAP-F + CAP-A | feature-032 /status (CAP-F) con AC-B2 Dual Track visible | AC-B2 cubre visibilidad Dual Track. `also-relates-to` vacío en YAML — el link a CAP-A no está declarado. | GAP MENOR |

**Resumen coherencia del flujo**: 3 gaps de cross-link identificados. Ninguno rompe verificabilidad de AC (los Scenarios son autocontenidos). Sí degradan trazabilidad del grafo.

---

## 3. Cognitive load del operador multi-rol

El operador humano en SEM-IA alterna entre hasta 8 sesiones por WA (hasta 4-6 en un WA típico). Evaluación de feature-036 como feature custodio del cognitive load:

**Mecanismos de reducción de cognitive load detectados y verificados:**

1. **Atajos npm nemotécnicos** (feature-010 AC-A1): `sem`, `arch`, `des` etc. reducen recall a primera sílaba del rol. Carga mínima.
2. **`/sessions` como referencia** (feature-034): operador reconoce, no recuerda. Slash siempre disponible.
3. **CLAUDE.md raíz con criterio "si dudas"** (feature-036 AC-A1): tabla rol → cuándo. Decisión externalizada a la tabla, no al cerebro.
4. **Ritual de inicio contextualiza** (feature-035): el PO presenta panorámica antes de pedir input. Operador no necesita recordar estado — el agente lo construye.
5. **`/wa` posiciona** (feature-033): el agente activo sabe dónde está en el WA sin leer manualmente 25KB de archivo.

**Evaluación feature-036 suficiencia**: feature-036 cubre adecuadamente el problema de orientación inter-sesión. Las 2 stories (consulta previa + recovery si equivocado) cubren los 2 momentos críticos del error de elección de rol. Nielsen #9 materializado en AC verificables (AC-B1/B2/B3).

**Flag medio — cognitive load residual**: el handoff verbal entre sesiones (momento 4.8 del Bloque 2: "humano cambia sesión `npm run <rol>`") no tiene feature dedicada. El operador humano recibe instrucción verbal ("sal de esta sesión y abre `npm run arch`") pero no hay mecanismo que lo recuerde o lo asista si se equivoca de comando. Feature-036 cubre el recovery dentro de una sesión pero no el error de escribir `npm run arch` cuando era `npm run des`. **Severidad baja**: el problema es de UX terminal, no de diseño del framework. El operador que domina 2 atajos resuelve. Aparcar a iteración posterior.

---

## 4. Flags consolidados

| ID | Feature | Heurística | Descripción | Severidad |
|---|---|---|---|---|
| DES-001 | feature-033 /wa | Grafo | `also-relates-to: []` en frontmatter YAML. Debería declarar cross-links con feature-035, feature-018, feature-019. | Medio |
| DES-002 | feature-035 ritual inicio PO | Grafo | Body narrativo declara cross-links con feature-038 y feature-039 pero frontmatter YAML `also-relates-to` vacío. | Medio |
| DES-003 | feature-038 PO Modo 1 | Grafo | No declara `also-relates-to: feature-035` pese a que feature-035 es el paso 1 de Modo 1. Bidireccional roto. | Medio |
| DES-004 | feature-038 PO Modo 1 | Cognitive load | 10 pasos declarados — denso para lectura humana del agent file. No reducible sin pérdida semántica. Recomendación: formato visual (tabla/bullets numerados) en agent file. | Bajo — informativo |
| DES-005 | feature-041 + 044 + 045 | Scope | Artefactos físicos (README, glosario, ruta lectura) se construyen en WA feature-build posterior. Specs correctas; gap de entregable real al GISF deadline 2026-05-25. | Bajo — scope intencional del WA |
| DES-006 | feature-032 /status | Grafo | `also-relates-to` en YAML vacío. Debería incluir al menos CAP-A (lifecycle nodos que /status agrega). | Bajo |
| DES-007 | Flujo operador — Insight 4 | Coherencia flujo | feature-033 /wa debería cruzar `cap-03-working-agreements-sdlc` (el /wa lee el WA, cuyo contrato vive en CAP-C). | Medio |

**Sin hallazgos críticos.** Sin hallazgos altos. Todos los AC de usabilidad existentes son verificables vía los mecanismos declarados.

---

## 5. Veredicto consolidado

**`apto-con-correcciones`**

Los 10 features auditadas cubren adecuadamente las heurísticas Nielsen relevantes. Los AC de usabilidad existentes son verificables y bibliográficamente anclados. La cobertura es correcta.

Los 3 flags medios (DES-001, DES-002, DES-003, DES-007) son todos del mismo tipo: cross-links narrativos en el cuerpo del artefacto no formalizados en el frontmatter YAML. No rompen la verificabilidad de los AC (los Scenarios Gherkin son autocontenidos) pero degradan la trazabilidad del grafo (propiedad custodiada por CAP-A, no por usabilidad).

**Recomendación al PO** (post-/verify, no bloquea este WA):
- Añadir en frontmatter YAML de feature-033: `also-relates-to: [cap-03-working-agreements-sdlc, feature-035-ritual-inicio-po, feature-018-slash-scope-scan, feature-019-slash-verify]`
- Añadir en frontmatter YAML de feature-035: `also-relates-to: [cap-07-inception-greenfield, feature-038-po-modo-1, feature-039-cadena-was-greenfield]`
- Añadir en frontmatter YAML de feature-038: `also-relates-to: [feature-035-ritual-inicio-po, feature-039-cadena-was-greenfield]`
- Añadir en frontmatter YAML de feature-032: `also-relates-to: [cap-01-grafo-declarativo-persistente]`

Estas correcciones son ediciones de frontmatter YAML — no requieren nuevo WA, pero sí autorización explícita del PO (scope-forbidden en este WA: "NO modifiques feature/story/spec files").

---

```yaml
filesystem-changes:
  - path: /Users/pelayo/Developer/SEM-AI/vault/designer/audits/spine-bootstrap-usability-review.md
    operation: created
    locations:
      - lines: "1-end"
        change-summary: "Audit completo usability review: checklist Nielsen/Cooper/Norman por feature relevante, validación coherencia flujo operador (6 insights Bloque 2), evaluación cognitive load multi-rol, 7 flags clasificados, veredicto consolidado apto-con-correcciones."
    rationale: "Step-4 del WA-2026-05-13-005. Output declarado en scope-allowed del WA. Autoridad de escritura del Designer acotada a vault/designer/audits/."
```
