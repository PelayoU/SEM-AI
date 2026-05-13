---
name: sec-threat-modeling
description: "Producir threat-model formal de una feature, capability o ADR sensible: identificar activos, threats (STRIDE simplificado), vulnerabilidades, priorizar riesgo (likelihood × impact), proponer mitigaciones, derivar AC de seguridad (AC-S*) que la spec debe cubrir. Use this skill when a feature touches auth/authz/data sensitive/external interfaces, when an ADR has security implications, or when retrospective audit detects un-modeled risk."
allowed-tools: Read Write Edit Glob Grep
materializes-feature: [feature-018-slash-scope-scan, feature-019-slash-verify]
# Trazabilidad bidireccional (WA-2026-05-13-005 step-8): skill Security invocada como advisor en scope-scan (feature-018) y sign-off (feature-019). Aplicada en step-6 del WA-005 actual con criterio honest-agent assumption (preview, no formal — pendiente WAs threat-model dedicados Lote B).
---

# Skill: threat-modeling (Security Officer)

## Quick reference

Aplica 7 pasos (basados en STRIDE simplificado + Shostack) para producir threat-model auditable. Output: archivo formal en `vault/security-officer/audits/<id>-threat-model.md` + AC de seguridad (AC-S1, AC-S2, ...) para añadir a la spec consumida.

## When to invoke

- **Template `threat-model`** (caso principal): WA dedicado a producir threat-model de una feature/capability/ADR sensible.
- **Sub-skill dentro de `feature-design`** (step Security opcional): cuando feature toca security, esta skill se invoca para producir el threat-model como parte del WA.
- **Step opcional dentro de `adr`** (step Security): cuando ADR tiene implicaciones de seguridad significativas.
- **Retrospectivo ad-hoc** (raro): si Architect identifica módulo de auth/data-sensitive sin threat-model documentado durante audit/refactor, Security puede producirlo retroactivamente.

**NO invocar** para features sin superficie de seguridad (UI cosmética, refactor interno sin datos sensibles).

## Inputs

- Spec o feature o ADR a threat-modelar (frontmatter + descripción + AC).
- Código relevante si existe (lectura focalizada por archivos referenciados).
- ADRs aplicables sobre seguridad/cripto/auth.
- Threat-models previos del proyecto (`vault/security-officer/audits/`) para no duplicar.
- Compliance aplicable si hay (GDPR, PCI, SOC 2, etc.) — humano lo aporta.

## Process — 7 pasos

### Paso 1 — Identificar activos
¿Qué se está protegiendo? Lista los activos:
- Datos sensibles (PII, credenciales, secrets, datos financieros, datos de salud).
- Identidades (cuentas, sesiones, tokens).
- Funcionalidad crítica (operaciones que mueven valor, escalan privilegio).
- Disponibilidad (SLOs comprometidos por feature).
- Reputación / compliance.

Cada activo: nombre + dónde vive (path o sistema) + clasificación de sensibilidad (público / interno / confidencial / restringido).

### Paso 2 — Identificar threats (STRIDE simplificado)
Para cada activo, evalúa STRIDE:
- **S**poofing — ¿alguien puede suplantar identidad?
- **T**ampering — ¿pueden modificarse datos sin autorización?
- **R**epudiation — ¿se puede negar haber hecho una acción?
- **I**nformation disclosure — ¿se filtran datos sensibles?
- **D**enial of service — ¿pueden agotar recursos?
- **E**levation of privilege — ¿pueden ganar permisos no autorizados?

Para cada threat detectado: categoría STRIDE + descripción concreta + path/contexto donde aplica.

### Paso 3 — Identificar vulnerabilidades concretas
Para cada threat, ¿qué vulnerabilidad lo materializa? Ejemplos:
- Spoofing: falta de MFA, tokens predecibles, sesiones sin expiración.
- Tampering: input no validado, falta de integridad en data-in-transit.
- Information disclosure: logs con PII, errores que filtran stack-traces, missing redaction.
- DoS: sin rate-limit, sin timeouts, sin circuit-breaker.
- Privilege escalation: roles sin granularidad, missing authz checks en endpoints.

Para cada vulnerabilidad: descripción + path/contexto + threat al que sirve.

### Paso 4 — Priorizar (likelihood × impact)
Cada vulnerabilidad recibe puntuación:
- **Likelihood**: alto / medio / bajo (¿qué tan factible es explotarla?).
- **Impact**: crítico / alto / medio / bajo (¿qué pasa si se explota?).
- **Priority**: matriz likelihood × impact → crítico / alto / medio / bajo / informativo.

Tabla resumen ordenada por priority descendente.

### Paso 5 — Proponer mitigaciones
Para cada vulnerabilidad priority crítico/alto/medio: proponer mitigación concreta. Forma: *"Implementar X en módulo Y para mitigar Z"*. Si la mitigación requiere ADR (decisión arquitectónica), flag para invocar `adr-writing` posterior.

Para priority bajo/informativo: documentar pero no exigir mitigación obligatoria. El humano decide.

### Paso 6 — Derivar AC de seguridad (AC-S*)
Cada mitigación crítico/alto que se traduce en comportamiento testeable se convierte en AC de seguridad para añadir a la spec consumida. Forma:
- `AC-S1: Token de sesión expira tras 30 minutos de inactividad`
- `AC-S2: Endpoint /admin requiere rol admin verificado en cada request`
- `AC-S3: Logs no contienen tokens, contraseñas, ni PII no-redactado`

QA cubrirá estos AC con tests (`@ac-coverage: AC-S1, AC-S2, AC-S3`).

### Paso 7 — Documentar el threat-model
Escribe `vault/security-officer/audits/<id>-threat-model.md` con `status: draft`. Estructura abajo. Ejecuta handoff a recepción / siguiente step del WA.

## Output format

Archivo `vault/security-officer/audits/<id>-threat-model.md`:

```markdown
---
type: threat-model
id: <id>-threat-model
title: "Threat-model — <feature/capability/ADR id>"
related-feature: <feature-id o null>
related-capability: <capability-id o null>
related-adr: <adr-id o null>
status: draft
created: <YYYY-MM-DD>
author: security-officer
findings-critical: <N>
findings-high: <N>
findings-medium: <N>
findings-low: <N>
ac-security-added: [AC-S1, AC-S2, ...]
---

# Threat-model — <id>

## 1. Activos
<lista con nombre + path + sensibilidad>

## 2. Threats (STRIDE)
<por cada activo, threats categorizados>

## 3. Vulnerabilidades
<lista con descripción + path + threat asociado>

## 4. Priorización
<tabla likelihood × impact ordenada por priority>

## 5. Mitigaciones
<por cada vulnerabilidad crítico/alto/medio>

## 6. AC de seguridad añadidos a spec
<lista de AC-S* añadidos a la spec consumida>

## 7. Compliance check (si aplica)
<GDPR / PCI / SOC2 / etc. — solo si humano declaró compliance aplicable>
```

## Bibliographic foundation

- STRIDE (Microsoft Threat Modeling) — categorías canónicas de threats.
- Shostack — *Threat Modeling: Designing for Security* (2014). Procedimiento ordenado.
- OWASP Top 10 — vulnerabilidades web comunes para chequear.
- OWASP ASVS — Application Security Verification Standard, niveles de exigencia.

(Bibliografía documentada en `vault/architect/research/library/` cuando se materialice.)

## Limitations

- STRIDE no es exhaustivo — útil como punto de partida, no garantía de cobertura total.
- Likelihood / impact tienen componente subjetivo. Humano valida priorización.
- Threat-model evoluciona con la feature — no es one-shot. Re-evaluar cuando feature cambia significativamente.
- Compliance específico (GDPR detallado, PCI completo) puede requerir auditoría externa, no solo skill.

## Status lifecycle

**Esta skill produce el threat-model con `status: draft`.** **NO** setees el status final desde aquí. La transición a `status: active` la aplica recepción al `/verify` del WA vía `on-close`. Lifecycle:

| Status | Cuándo |
|---|---|
| `draft` | Output inicial de esta skill (durante el step) |
| `active` | Tras /verify del WA aprobado |
| `deprecated` | Threat-model ya no aplica (feature deprecated o re-modelado) |

## WA mapping

Esta skill se invoca dentro de:
- **`threat-model`** template (caso principal, en su único step).
- **`feature-design`** template (step Security opcional, condicional a `security en dimensions-affected`).
- **`adr`** template (step Security opcional cuando ADR tiene implicaciones de seguridad).
- Audit ad-hoc retroactivo cuando se detecta módulo de auth/data-sensitive sin threat-model documentado (ej. durante refactor o code review).
