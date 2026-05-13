---
description: "Lista los modos de trabajo y sesiones dedicadas disponibles"
---

Imprime al humano el modelo de invocación de SEM-IA y las sesiones dedicadas disponibles. NO ejecutes ningún comando — solo presenta la información.

## Output format

```
## Modos de trabajo en SEM-IA

### Recepción al root
Para crear Working Agreements, hacer scope-scan, disparar verificación al cierre.
Comando: `npm run sem`  (atajo de `claude` desde la raíz del repo)

Recepción NO conduce trabajo. Solo coordina.

### Sesión dedicada por step
Cada step del WA se ejecuta en la sesión dedicada del rol active del step.
El humano arranca la sesión con un `npm run <rol-short>`; el wrapper de
subdirectorio (cuando existe) carga la identidad del rol nativamente.

| Rol             | Atajo npm        | Equivalente                                | Trabaja en |
|-----------------|------------------|--------------------------------------------|------------|
| Product Owner   | `npm run po`     | cd vault/product-owner && claude           | visión, goals, capabilities, features, specs, discovery |
| Architect       | `npm run arch`   | cd vault/architect && claude               | ADRs, research técnico |
| Designer        | `npm run des`    | cd vault/designer && claude                | usability, accessibility, flows |
| Business Analyst| `npm run biz`    | cd vault/business-analyst && claude        | business-viability, compliance, GTM |
| Security Officer| `npm run sec`    | cd vault/security-officer && claude        | threat-models, audits |
| QA              | `npm run qa`     | cd vault/qa && claude                      | test strategy, coverage |
| Developer       | `npm run dev`    | cd src && claude (cuando exista wrapper)   | implementación de código |
| DevOps          | `npm run ops`    | cd vault/devops && claude                  | infra, CI/CD |
| Recepción       | `npm run sem`    | claude (desde raíz)                        | drafting de WAs, scope-scan, verify |

**Notas:**
- Los atajos `npm run` funcionan desde **cualquier subdirectorio** del repo —
  npm encuentra el `package.json` automáticamente.
- Sin dependencias: `npm run` no requiere `npm install` (no hay `dependencies`).
- El humano sigue el WA step a step. El rol al completar su step indica la
  siguiente sesión a abrir (handoff explícito), p. ej. *"arranca `npm run po`"*.
- Atajo opcional para tu shell: `alias n='npm run'` → queda en `n po`, `n arch`, etc.

### Subagentes vía Task tool (give-and-take mid-step, Cagan principio 2)
Disponibles desde cualquier sesión cuando se necesita juicio puntual de otro rol.
Útil para scope-scan al crear WA, verificación al cierre, consultas mid-step.

### Slash commands relacionados con WAs (disponibles desde cualquier sesión)

| Comando | Para qué |
|---|---|
| `/status` | Snapshot del estado actual (WAs activos, subgrafo, features, ADRs, backlog). |
| `/wa` | Detalle del WA aplicable al contexto, con steps y status. |
| `/scope-scan "<propuesta>"` | Scope-scan flat parallel multi-rol on-demand. |
| `/verify` | Dispara matriz de verificación al cierre del WA + aplica `on-close`. |

**Pendiente post-inception:** los atajos `npm run` se convertirán en
`npx sem-ia <rol>` cuando exista el CLI distribuible. La ergonomía actual
(npm scripts en `package.json` de la raíz) ya cumple para el día a día.
```

## Cuándo es útil

- Olvidaste qué directorio carga qué rol.
- Estás en una sesión y quieres saber a dónde ir para el siguiente step.
- Como referencia rápida sin abrir `vault/shared/governance/repo-structure.md` o `workflows.md`.
