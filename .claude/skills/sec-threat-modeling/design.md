---
type: research
id: design-skill-security-threat-modeling
title: "Design — threat-modeling skill"
status: draft
created: 2026-05-07
author: security-officer
---

# Design — threat-modeling

## Propósito

Skill canónica del Security Officer para producir threat-models auditables de features/capabilities/ADRs sensibles. Aplica STRIDE simplificado (Shostack) extendido con priorización (likelihood × impact) + derivación de AC de seguridad para que QA tenga tests trazables.

## Por qué existe esta skill (vs solo agent file)

Hasta este refactor, Security Officer operaba con guía bibliográfica del agent file solamente (sin skill formal). Para un proyecto que se toma seguridad en serio:
- **Auditabilidad**: el threat-model es un artefacto al que la organización puede volver. Sin procedimiento estandarizado, threat-models inconsistentes entre WAs.
- **Trazabilidad a tests**: AC de seguridad (AC-S*) derivados sistemáticamente conectan threat-modeling con QA coverage.
- **Lifecycle gestionable**: threat-models evolucionan. Skill estandariza cuando re-evaluar.

Misma razón por la que `adr-writing` es skill formal: decisión arquitectónica significativa merece procedimiento auditable.

## Distinción con otras skills

| Skill | Cuándo | Output |
|---|---|---|
| `threat-modeling` | Feature/capability/ADR con superficie de seguridad. **Análisis de threats + mitigaciones.** | `<id>-threat-model.md` + AC-S* en spec |
| `coherence-evaluation` (Architect) | Cambio propuesto vs ADRs existentes. Puede aplicar a ADR de seguridad. | Reporte de coherencia |
| `adr-writing` (Architect) | Decisión arquitectónica, incluyendo de seguridad. | ADR con sección Consequences |

`threat-modeling` es **específicamente** sobre amenazas y mitigaciones, no sobre coherencia general ni decisiones puras.

## Proceso detallado

### Paso 1 — Activos

Pregunta clave: **¿qué se está protegiendo?**

Categorías canónicas:
- **Datos sensibles**: PII (nombres, emails, direcciones), credenciales (passwords, tokens, claves), datos financieros (tarjetas, cuentas), datos de salud (HIPAA-relevant), datos de niños (COPPA-relevant), secrets de la app (DB passwords, API keys, signing keys).
- **Identidades**: cuentas de usuario, sesiones, tokens (JWT, OAuth), API keys de clientes.
- **Funcionalidad crítica**: operaciones que mueven dinero/valor, operaciones que escalan privilegio (cambio de rol, password reset), operaciones administrativas.
- **Disponibilidad**: SLOs comprometidos por la feature (latencia P99, uptime).
- **Reputación / compliance**: si se incumple, multa o impacto reputacional.

Para cada activo: nombre + dónde vive (path o sistema) + clasificación (público / interno / confidencial / restringido).

### Paso 2 — STRIDE

STRIDE es la lente. Para cada activo, evalúa los 6 categorías:

**S**poofing (suplantación de identidad):
- ¿Puede alguien hacerse pasar por otro usuario? Si sí, ¿qué activos accede?
- Vectores: credenciales débiles, sin MFA, phishing, session fixation.

**T**ampering (modificación no autorizada):
- ¿Pueden modificarse datos en tránsito o en reposo sin autorización?
- Vectores: man-in-the-middle, SQL injection, parámetros HTTP modificables sin validación.

**R**epudiation (negación de acción):
- ¿Puede un usuario negar haber hecho una acción crítica?
- Vectores: falta de logs, logs no firmados, falta de audit trail.

**I**nformation disclosure (filtración):
- ¿Se filtran datos sensibles a usuarios no autorizados?
- Vectores: error messages con stack trace, logs con PII, missing field redaction, IDORs (Insecure Direct Object References).

**D**enial of service:
- ¿Pueden agotarse recursos para impedir servicio?
- Vectores: sin rate-limit, queries pesadas no controladas, sin timeouts, sin circuit-breaker.

**E**levation of privilege:
- ¿Puede un usuario ganar permisos no autorizados?
- Vectores: missing authz checks, role-confusion bugs, IDOR a recursos de admin.

Para cada threat detectado: categoría STRIDE + descripción concreta + path/contexto donde aplica.

### Paso 3 — Vulnerabilidades concretas

Cada threat debe materializarse en una vulnerabilidad explotable concreta. Si no la encuentras, el threat es teórico — anótalo como "informativo".

Vulnerabilidades comunes (OWASP Top 10 + específicas SEM-IA):
- A01:2021 Broken Access Control → Privilege escalation
- A02:2021 Cryptographic Failures → Information disclosure
- A03:2021 Injection → Tampering
- A04:2021 Insecure Design → varios
- A05:2021 Security Misconfiguration → varios
- A06:2021 Vulnerable Components → varios
- A07:2021 Auth & Session Management → Spoofing
- A08:2021 Software & Data Integrity → Tampering
- A09:2021 Security Logging & Monitoring → Repudiation
- A10:2021 SSRF → Information disclosure / Tampering

### Paso 4 — Priorizar

Matriz likelihood × impact:

|         | Impact: Bajo | Medio | Alto | Crítico |
|---------|--------------|-------|------|---------|
| **Likelihood Alto** | Medio | Alto | Crítico | Crítico |
| **Likelihood Medio** | Bajo | Medio | Alto | Crítico |
| **Likelihood Bajo** | Informativo | Bajo | Medio | Alto |

Likelihood evalúa:
- ¿Hay public-facing endpoints? (más alto)
- ¿Requiere conocimiento interno del sistema? (más bajo)
- ¿Hay rate-limiting / WAF / monitoring? (más bajo)

Impact evalúa:
- ¿Qué activos se ven afectados? (datos críticos = más alto)
- ¿Cuántos usuarios afectados? (más = más alto)
- ¿Es reversible? (irreversible = más alto)
- ¿Implica compliance breach? (sí = más alto)

### Paso 5 — Mitigaciones

Para cada vulnerabilidad crítico/alto/medio: mitigación concreta y testeable.

Forma:
- *"Implementar [mitigación] en [módulo] para mitigar [vulnerabilidad → threat]."*
- *"Añadir [control] en [endpoint] que verifica [condición]."*

Si la mitigación requiere decisión arquitectónica significativa (ej. cambio de proveedor de auth, nueva criptografía): flag para invocar `adr-writing` separado.

Mitigaciones priority bajo/informativo: documentar como recomendación. Humano decide si las aplica.

### Paso 6 — AC de seguridad

Cada mitigación testeable se traduce en AC-S (AC de Seguridad). Forma Gherkin-friendly:

```
AC-S1: Token de sesión expira tras 30 minutos de inactividad
  Given un usuario con sesión activa
  When pasan 30 minutos sin actividad
  Then la sesión se invalida y requiere re-login
```

QA en su step posterior cubrirá AC-S* con tests (`// @ac-coverage: AC-S1, AC-S2`).

### Paso 7 — Documentar

Estructura del archivo definida en SKILL.md. Énfasis en:
- **Auditabilidad**: cada threat tiene path/contexto que lo ancla.
- **Frontmatter**: counts (findings-critical, findings-high, etc.) para `/status` agregue.
- **Cross-link**: declarar `related-feature`/`related-capability`/`related-adr`.

## Ejemplo aplicado: feature de login con Google

### Paso 1 — Activos:
- Email del usuario (PII, confidencial).
- Token OAuth de Google (credencial, restringido).
- Sesión SEM-IA tras login (identidad, restringido).
- Endpoint de callback (funcionalidad crítica).

### Paso 2 — STRIDE:
- S: spoofing de callback URL → atacante recibe token.
- T: tampering de state parameter → CSRF en flow OAuth.
- I: token leakage en logs.
- E: privilege escalation si el token de Google da acceso a roles internos.

### Paso 3 — Vulnerabilidades:
- V1: redirect_uri whitelist demasiado permisiva → spoofing callback.
- V2: state parameter no validado en callback → CSRF.
- V3: token logged in middleware → information disclosure.
- V4: rol asignado por defecto sin verificación → privilege escalation.

### Paso 4 — Priorización:
- V1: likelihood medio × impact crítico → **Crítico**.
- V2: likelihood medio × impact alto → **Alto**.
- V3: likelihood alto × impact alto → **Crítico**.
- V4: likelihood bajo × impact crítico → **Alto**.

### Paso 5 — Mitigaciones:
- V1: redirect_uri whitelist estricta (solo dominios propios) → ADR sobre policy.
- V2: validar state en callback (UUID per-request, expiración, single-use).
- V3: token redaction en logger middleware (regex match).
- V4: nuevo usuario recibe rol `viewer` por defecto, escalada explícita por admin.

### Paso 6 — AC-S derivados:
- AC-S1: redirect_uri whitelist solo permite dominios del proyecto.
- AC-S2: callback rechaza requests sin state válido.
- AC-S3: logs no contienen tokens (verificable con regex en tests).
- AC-S4: usuario nuevo tiene rol `viewer`, no admin.

### Paso 7 — Documenta en `vault/security-officer/audits/feature-7-google-login-threat-model.md`.

## Limitaciones

- STRIDE útil pero no exhaustivo — agentes con expertise en dominios específicos (cripto, web3) detectan threats que STRIDE no captura.
- Skill semi-manual: análisis depende de juicio del Security Officer + conocimiento del proyecto.
- Threat-model evoluciona — re-evaluar cuando la feature cambia significativamente.
- Compliance específico (GDPR detallado, PCI completo, SOC 2 Type II) puede requerir auditoría externa.
