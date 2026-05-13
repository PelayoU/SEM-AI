---
description: "Dispara la matriz de verificación sobre un Working Agreement listo para cierre"
---

Aplica la matriz de verificación al WA activo aplicable. Invoca verificadores en paralelo y consolida veredicto. Ejecutar **desde la sesión PO (modo recepción)** cuando un WA está listo para cierre — comando: `npm run sem` o `npm run po`. También accesible desde cualquier sesión de rol, pero típicamente lo invoca el rol orquestador del WA (PO para outcome-types product; Architect/DevOps/Security para WAs de su dominio puro).

## Pre-condiciones

- Existe al menos un WA en `vault/shared/sessions/active/`.
- El WA tiene `closure-criteria` declarados.
- Working directory: típicamente `vault/product-owner/` (sesión PO en modo recepción) o `vault/<rol>/` (rol orquestador). El root no aplica — el `CLAUDE.md` raíz es guía estática, no carga sesión.

## Pasos

1. **Identifica el WA a verificar.**
   - Si hay UN solo WA activo: ese es.
   - Si hay varios: pregúntale al humano cuál.

2. **Comprueba pre-condiciones de cierre.**
   - Lee el WA. Evalúa cada `closure-criterion` mecánicamente (lectura del vault).
   - Si algún criterio NO se cumple objetivamente: NO lances verificación. Indica al humano qué falta y termina.
   - Si todos se cumplen: continúa.

3. **Deriva la lista de verificadores desde `dimensions-affected`.**

   Lee del WA: `dimensions-affected`.

   Aplica el algoritmo formal:

   ```
   verifiers_final = { custodian(d) : d ∈ wa.dimensions-affected }
   ```

   Donde `custodian(d)` se obtiene del catálogo `vault/shared/governance/dimensions.md` (cada dimensión declara su custodio).

   Deduplica. Esa es la lista de verificadores a invocar.

   **Override:** si el WA tiene `verifiers-required` con un valor explícito distinto de la lista derivada, respeta el override (el humano lo asignó conscientemente al crear el WA o post-scope-scan). Indícalo al humano antes de invocar: *"WA tiene override de verificadores. Lista derivada: [X, Y, Z]. Lista override: [X]. ¿Procedo con override?"*

   Escribe la lista finalmente usada en `verifiers-required` del WA antes de cerrar (auditoría).

4. **Invoca verificadores en paralelo.**
   - Por cada verificador requerido (ej: `architect`, `qa`, `security-officer`):
     - Lee `.claude/agents/<rol>.md` para conocer su identidad.
     - Construye prompt con: identidad del rol + WA completo + tarea concreta de verificación + paths a leer.
     - Invoca con Task tool, `subagent_type: <rol>`.
   - **Lánzalos todos en paralelo** (un solo mensaje con múltiples tool uses).

5. **Consolida hallazgos.**
   - Recoge output de cada verificador.
   - Clasifica: aprobado / objeción menor / objeción bloqueante.
   - Presenta resumen al humano: matriz de veredictos + objeciones detalladas si las hay.

6. **Decisión.**
   - **Si todos aprueban:** continúa al paso 7 (aplicar `on-close`).
   - **Si hay objeciones bloqueantes:** WA vuelve a estado activo. Resume qué hay que resolver. NO archives, NO apliques `on-close`.
   - **Si hay objeciones menores:** presenta al humano para decisión (resolver ahora, aparcar como gotcha/learning, o aceptar conscientemente). Si humano acepta, procede al paso 7.

7. **Aplica las transiciones declaradas en `on-close` del WA.**

   Lee el campo `on-close` del frontmatter del WA. Cada entrada tiene formato:
   ```
   <path-relativo-al-repo>: <status-inicial> → <status-final>
   ```
   Ejemplo:
   ```yaml
   on-close:
     - "vault/product-owner/specs/feature-7-google-login.md: draft → ready-for-implementation"
     - "vault/architect/adrs/adr-005-oauth.md: proposed → accepted"
   ```

   Para cada entrada:
   - Lee el archivo referenciado.
   - Verifica que el campo `status` actual matchea el `<status-inicial>` declarado. Si no matchea (alguien lo cambió manualmente, o el step previo no lo dejó en draft): para, reporta al humano *"Status inicial inesperado en `<path>`: encontrado `<actual>`, esperado `<inicial>`. ¿Aplico transición a `<final>` igualmente?"* y espera decisión.
   - Si matchea, modifica el campo `status` del frontmatter del archivo a `<status-final>` usando Edit tool. Preserva todo lo demás del archivo intacto.
   - Si el archivo referenciado no existe: para, reporta al humano *"Archivo declarado en on-close no existe: `<path>`. El step que debía producirlo no lo creó o lo movió. ¿Procedo sin esta transición?"* y espera decisión.

   Confirma al humano TODAS las transiciones aplicadas antes de archivar:
   ```
   Transiciones on-close aplicadas:
   - vault/product-owner/specs/feature-7-google-login.md: draft → ready-for-implementation ✓
   - vault/architect/adrs/adr-005-oauth.md: proposed → accepted ✓
   ```

8. **Archiva el WA.**
   - Propón al humano archivar el WA (mover de `vault/shared/sessions/active/` a `vault/shared/sessions/archive/`). Espera confirmación.
   - Tras confirmación, mueve el archivo y actualiza `status: archived` en el frontmatter del WA.

## Output format

```
## Verificación · WA <id>

### Pre-condiciones
- [x|✗] <closure-criterion 1>
- [x|✗] <closure-criterion 2>

### Verificadores invocados
- <rol 1>: <APROBADO | OBJECIÓN MENOR | OBJECIÓN BLOQUEANTE>
- <rol 2>: ...

### Objeciones
<bloque por verificador con detalle, si las hay>

### Veredicto consolidado
<APROBADO PARA CIERRE | RETORNA A ACTIVO | DECISIÓN HUMANA REQUERIDA>

### Transiciones on-close (solo si veredicto aprobado)
- <path 1>: <status-inicial> → <status-final> ✓
- <path 2>: <status-inicial> → <status-final> ✓

### Acción propuesta
<archivar WA + paths de update | resolver objeciones + listado | decisión humana sobre objeciones menores>
```

## Cuándo es útil

- Has terminado el trabajo de un WA y quieres cerrarlo formalmente.
- Quieres auditar mid-trabajo si lo que tienes pasaría verificación (ejecutas y descartas).

## Importante

- NUNCA archives un WA sin confirmación humana, aunque el veredicto sea APROBADO.
- Si la matriz de verificación cambia mid-WA, prevalece la versión vigente al momento del cierre.
- Las objeciones detalladas se guardan en `vault/shared/reviews/wa-<id>-verification.md` para auditoría.
