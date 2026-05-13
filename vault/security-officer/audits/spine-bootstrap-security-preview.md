---
type: audit
id: spine-bootstrap-security-preview
title: "Threat-modeling preview consolidado sobre la espina dorsal bootstrap (14 features)"
status: active  # transitado por /verify del WA-005 el 2026-05-13T08:30+02:00
created: 2026-05-13
author: security-officer
parent-wa: wa-2026-05-13-005
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
dimensions-affected: [security]
citas-bibliograficas:
  - Shostack — Threat Modeling (STRIDE + honest-agent assumption + declarar threat surface)
  - OWASP LLM Top 10 — vectores específicos a agentes LLM con write access
  - Nygard — ADRs como registro auditable de decisiones de seguridad
verificadores-aplicables: [security-officer]
alcance: preview  # AC-S* enumerables; threat-models formales completos vienen en WAs `threat-model` posteriores
---

# Threat-modeling preview consolidado · Espina dorsal bootstrap WA-005

## 1. Marco metodológico y honest-agent assumption explícita

**Criterio Shostack aplicado** (heredado de la pelea fuerte WA-004): SEM-IA opera bajo **honest-agent assumption explícita** — el framework asume que los agentes IA invocados (PO, Architect, Designer, etc.) están alineados con el operador humano. NO protege contra agente desalineado con write access al vault. Esta asunción es **load-bearing** y debe declararse honestamente (Shostack: *"declarar lo que NO proteges es tan importante como declarar lo que sí proteges"*).

**Implicaciones operativas:**

- Vectores STRIDE que requieren "agente desalineado" como precondición son **out-of-scope** del framework → NO se declara `security` en la feature.
- Vectores que el framework promete cubrir (path traversal del filesystem, vault público por diseño, integridad bibliográfica auditable) son **load-bearing** → SÍ se declara `security`.
- NO checkbox security: declarar `security` en una feature obliga a producir AC-S* verificables. Sin AC-S* → no declarar.

## 2. Mapping STRIDE per-feature load-bearing

### 2.1 Features que declaran `security` honestamente (load-bearing real)

| Feature | Vectores STRIDE | Load-bearing | Justificación |
|---|---|---|---|
| **feature-041 (README onboarding)** | I (Information Disclosure), R (Repudiation) | SÍ | spec-041-C declara cautelas explícitas: vault público por diseño + qué NO commitear + Progreso entries sin trazabilidad criptográfica. Mitigación = adopter education honesta, no protección técnica. Vector mitigado por la feature misma. |

**Confirmación**: feature-041 declara `dimensions-affected: [product, usability, business, security]`. spec-041-C ya implementa el threat surface declarativo (AC-C1/C2/C3 cubren visibilidad de sección + lista qué NO commitear + honestidad Shostack). **No requiere AC-S* adicional** — los AC-C1/C2/C3 ya son los AC-S* implícitos de feature-041.

### 2.2 Features con security latente NO declarada (criterio honest-agent assumption — correcto NO declarar)

Las siguientes features tienen vectores STRIDE teóricos, pero los vectores **dependen de precondiciones out-of-scope** (agente desalineado, harness comprometido, filesystem comprometido). Confirmación de que NO declarar `security` es honesto bibliográficamente:

| Feature | Vector teórico | Razón NO declarar (honest-agent assumption) |
|---|---|---|
| feature-001 (vault role-first) | T (Tampering) path traversal en `vault/<rol>/`; YAML unsafe en frontmatter | Path traversal requiere agente desalineado escribiendo fuera de su `vault/<mi-rol>/`. YAML unsafe requiere parser inseguro en el harness. Ambos out-of-scope del framework. La convención role-first es protección **organizacional**, no técnica. **Honesto NO declarar security.** |
| feature-010 (entry-point por rol) | S (Spoofing) suplantación de identidad via agent files | Requiere agente desalineado cargando agent file de otro rol. Out-of-scope: el harness Claude Code carga la identidad declarada en frontmatter, no hay autenticación criptográfica. **Honesto NO declarar.** |
| feature-018 (/scope-scan) | T integridad de outputs cross-rol | Subagentes invocados via Task tool con autoridad de edición operan bajo honest-agent assumption. Gap 9 (filesystem-changes) provee auditabilidad declarativa, NO defensa contra subagente desalineado. **Honesto NO declarar.** |
| feature-019 (/verify) | E (Elevation of Privilege) verificador no autenticado aprueba indebidamente | Out-of-scope: verificadores son subagentes alineados invocados por algoritmo declarativo `verifiers = {custodian(d)}`. Sin auth criptográfica entre roles AI. **Honesto NO declarar.** |
| feature-032 (/status) | I secret hygiene (vault completo agregado en output) | **Vector REAL pero mitigado vía feature-041 spec-041-C AC-C3** (advertencia adopter declarativa). /status NO promete redaction — es agregador honesto del vault público por diseño. **Mitigación delegada correctamente a feature-041 (adopter education).** Honesto NO declarar en feature-032. |
| feature-033 (/wa) | T+R subagentes con autoridad de edición sin trazabilidad criptográfica | spec-033-B AC-B3 ya declara que subagentes registran `filesystem-changes` (Gap 9 protocolo declarativo). Mitigación auditable, no criptográfica. **Honesto NO declarar security** — Gap 9 vive bajo dimensión `product` + `usability` (transparencia operativa), no `security` formal. |
| feature-034 (/sessions), feature-035 (ritual PO), feature-036 (orientación rol), feature-038 (PO Modo 1), feature-039 (cadena WAs greenfield), feature-044 (glosario), feature-045 (ruta lectura) | n/a | Sin superficie security significativa. Lectura del vault es operación honest-agent. Out-of-scope explícito. **Honesto NO declarar.** |

### 2.3 Veredicto sobre features con `security` declarada

**Conclusión**: la única feature con `security` declarada en frontmatter (**feature-041**) lo hace **load-bearing real** vía spec-041-C. NO hay over-declaration. NO hay under-declaration crítica.

**Decisión arquitectónica honesta confirmada**: SEM-IA tiene **threat surface mínima por diseño** porque el vault es público por construcción + agentes alineados + sin auth criptográfica entre roles. Toda la "security" del framework se materializa como **adopter education declarativa** (feature-041 spec-041-C), no como controles técnicos.

## 3. AC-S* preview enumerables

Solo feature-041 requiere AC-S* explícitos. spec-041-C AC-C1/C2/C3 ya los implementa como AC del scenario regular (no requieren renombrado a AC-S*). Para trazabilidad downstream (QA step-7 + future WAs `threat-model`), declaro mapping:

| AC actual (spec-041-C) | AC-S* equivalente | Verificable vía |
|---|---|---|
| AC-C1 (sección cautelas visible en README) | AC-S1 | Inspección README + grep encabezado |
| AC-C2 (blast radius + lista NO commitear) | AC-S2 | Inspección sección README + tabla canónica presente |
| AC-C3 (vectores STRIDE I+R declarados honestamente) | AC-S3 | Inspección README + comparación con threat-model preview (este doc) |

**Decisión**: NO modifico spec-041-C (forbidden scope security-officer + autoridad de edición acotada a `vault/security-officer/audits/`). El mapping AC-C* ↔ AC-S* queda registrado aquí para QA step-7 + Lote B WAs `threat-model`.

**Para features sin `security` declarada**: cero AC-S* adicionales (criterio honest-agent assumption). Añadir AC-S* a features out-of-scope sería checkbox security — exactamente el anti-patrón que se rechaza.

## 4. ADRs latentes security recomendados para Lote B

### 4.1 ADR-security-trans · "Modelo threat surface del framework SEM-IA" (PRIORIDAD ALTA)

**Decisión declarativa**: SEM-IA opera bajo **honest-agent assumption explícita**:

- (a) Los agentes IA invocados (PO, Architect, Designer, Business-analyst, Security-officer, QA, Developer, DevOps) son **alineados** con el operador humano.
- (b) El framework **NO protege** contra agente desalineado con write access al vault.
- (c) El vault es **público por diseño** (versionado por git, ground truth visible).
- (d) NO hay **autenticación criptográfica** entre roles AI ni en handoffs WA.
- (e) NO hay **redacción automática de secrets**; la responsabilidad es del adopter (spec-041-C AC-C2).

**Alternatives consideradas a declarar en Nygard**: (1) auth criptográfica inter-rol (rechazada: complejidad sin beneficio — operamos en un solo harness Claude Code); (2) vault privado por defecto (rechazada: contradice goal-2 output auditable); (3) redaction layer automática (rechazada: false sense of security).

**Trazabilidad downstream**: feature-041 spec-041-C es la materialización de este ADR (cautelas declarativas para adopter).

### 4.2 ADR-secret-hygiene · "Convención de qué NO commitear al vault" (PRIORIDAD MEDIA)

**Decisión declarativa**: lista canónica de qué NO commitear (vector I), declarada como convención del framework:

| Categoría | Ejemplos | Razón |
|---|---|---|
| Credenciales | API keys, tokens, passwords en frontmatter | Vault público |
| Tokens | OAuth tokens en Progreso entries, session tokens | Vault público |
| Datos clientes/PII | Emails reales en specs, nombres en discovery | Privacy |
| Información comercial sensible | Precios, contratos NDA, deal terms | Confidentiality |
| Secretos de operación | URLs internas, IPs privadas, hostnames internos | Operational security |

**Relación con feature-041**: spec-041-C AC-C2 ya cita una versión de esta lista para README adopter education. El ADR canoniza la lista como convención del framework + provee `gitignore`/pre-commit hook recommendation para futuras CAP-H portabilidad implementations.

### 4.3 ADR-filesystem-changes-audit · "Contrato Gap 9 como protocolo declarativo de auditabilidad, NO criptográfico" (PRIORIDAD BAJA)

**Decisión declarativa**: Gap 9 (`filesystem-changes` literal en output de subagentes) opera bajo honest-agent assumption — provee **registro auditable declarativo** (el subagente reporta qué tocó) pero NO firma criptográfica. Si el subagente miente sobre `filesystem-changes`, el orquestador detecta vía verificación de paths reportados vs paths reales modificados (spec-033-B AC-B3 + protocolo PO Modo 1 paso 6b).

**Trazabilidad downstream**: spec-033-B + protocolo Filtro PO (regla 12 agent file PO).

### 4.4 NO recomendados (descartados conscientemente)

- ADR sobre auth inter-rol AI: descartado, contradice asunción honest-agent.
- ADR sobre redacción automática de secrets en /status: descartado, contradice transparencia + delega correctamente a adopter education.
- ADR sobre encrypted vault: descartado, contradice vault público por diseño (goal-2).

## 5. Veredicto consolidado

**APROBADO**: el catálogo de 14 features producido en step-2a..2h pasa el filtro security honest-agent assumption.

- **0 over-declarations** detectadas (cero features con `security` declarada sin AC-S* materializable).
- **0 under-declarations críticas** (la única feature load-bearing real, feature-041, declara security correctamente y materializa cautelas en spec-041-C).
- **1 mitigación delegada correctamente**: vector I de feature-032 /status → mitigado vía feature-041 spec-041-C adopter education. Anclaje cross-feature honesto (no se infla feature-032 con redaction prometida-no-cumplida).
- **3 ADRs latentes** recomendados para Lote B (ADR-security-trans ALTA, ADR-secret-hygiene MEDIA, ADR-filesystem-changes-audit BAJA).
- **0 hallazgos críticos o altos** que bloqueen `/verify` del WA-005.

**Hallazgos informativos** (no bloqueantes):

- Recomendación: tras Lote B WAs `adr` (especialmente ADR-security-trans), considerar **WA `threat-model`** específico sobre CAP-H portabilidad multi-harness cuando se active — escenarios multi-harness traen vectores nuevos (cada adapter tiene threat surface propia).
- Recomendación: si emerge CAP-I (adopción retroactiva), threat-modelar el slash `/adopt` específicamente — leer codebase ajeno tiene vectores de I+T no presentes en greenfield.

## 6. filesystem-changes

```yaml
filesystem-changes:
  - path: /Users/pelayo/Developer/SEM-AI/vault/security-officer/audits/spine-bootstrap-security-preview.md
    operation: created
    locations:
      - lines: 1-end
        change-summary: "Threat-modeling preview consolidado sobre 14 features del bootstrap. Confirma feature-041 como única load-bearing security (vía spec-041-C). Confirma honest-agent assumption explícita como decisión arquitectónica honesta. Recomienda 3 ADRs latentes para Lote B (ADR-security-trans ALTA + ADR-secret-hygiene MEDIA + ADR-filesystem-changes-audit BAJA). Cero hallazgos críticos/altos."
    rationale: "Step-6 del WA-2026-05-13-005 requiere audit security preview con mapping STRIDE per-feature load-bearing + AC-S* enumerables + ADRs latentes. Output del subagente declara bloque filesystem-changes literal según Gap 9 protocolo (CLAUDE.md raíz)."
  - path: /Users/pelayo/Developer/SEM-AI/vault/shared/sessions/active/wa-2026-05-13-005.md
    operation: edited
    locations:
      - lines: 222-225
        change-summary: "Step-6 marcado status: in-progress con started-at timestamp."
    rationale: "Protocolo arranque de step del security-officer (agent file sección 'Al arrancar tu step' paso 5)."
```
