---
category: bibliography-source
id: library-anthropic-skills
title: "Anthropic — Skills en Claude Code (SKILL.md)"
status: draft
created: 2026-04-30
author: pelayo
tags: [library, anthropic, claude-code, skills, infrastructure]
applicable-roles: [all]
---

# Anthropic — Skills en Claude Code (SKILL.md)

## Datos bibliográficos

- **Fuente:** Documentación oficial de Anthropic / Claude Code.
- **URL canónica:** https://code.claude.com/docs/en/skills (redirección desde docs.claude.com)
- **Standard:** Agent Skills (https://agentskills.io) — open standard que funciona en múltiples herramientas AI.
- **Fecha de consulta:** 2026-04-30
- **Aplicabilidad SEM-IA:** infraestructura — define cómo se materializan las skills de los agentes homólogos.

## Concepto

> *"Skills extend what Claude can do. Create a SKILL.md file with instructions, and Claude adds it to its toolkit. Claude uses skills when relevant, or you can invoke one directly with /skill-name."*

Una skill es **una unidad de capacidad reutilizable**: instrucciones, playbooks, procedimientos multi-paso, conocimiento de dominio. A diferencia del contenido de CLAUDE.md (que se carga siempre), el contenido de una skill **solo se carga cuando se usa**, así que material de referencia largo cuesta poco hasta que se necesita.

**Crear una skill cuando:**
- Sigues pegando el mismo playbook / checklist / procedimiento en chat
- Una sección de CLAUDE.md ha crecido a procedimiento en lugar de un hecho

> *"Custom commands have been merged into skills. A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way."*

Las skills extienden los commands añadiendo:
- Un directorio para archivos auxiliares
- Frontmatter para controlar quién las invoca
- Capacidad de Claude de cargarlas automáticamente cuando son relevantes

## Formato de archivo

Cada skill es un **directorio** con `SKILL.md` como entrypoint:

```
my-skill/
├── SKILL.md           # REQUERIDO — instrucciones principales
├── reference.md       # opcional — referencia detallada cargada bajo demanda
├── examples.md        # opcional — ejemplos
├── template.md        # opcional — plantilla a rellenar
└── scripts/           # opcional — scripts ejecutables
    └── helper.py
```

`SKILL.md` es REQUERIDO. Otros archivos se referencian DESDE `SKILL.md` para que Claude sepa qué contienen y cuándo cargarlos.

> *"Tip: Keep SKILL.md under 500 lines. Move detailed reference material to separate files."*

## Ubicación

| Nivel | Ruta | Aplica a |
|---|---|---|
| Enterprise | Managed settings | Toda la organización |
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` | Todos los proyectos del usuario |
| Proyecto | `.claude/skills/<skill-name>/SKILL.md` | Este proyecto |
| Plugin | `<plugin>/skills/<skill-name>/SKILL.md` | Donde el plugin está habilitado |

Override: enterprise → personal → proyecto. Plugin skills usan namespace `plugin-name:skill-name` para evitar conflictos.

## Frontmatter — campos

Todos los campos son opcionales. **Solo `description` es recomendado**.

```yaml
---
name: my-skill
description: What this skill does and when to use it
disable-model-invocation: false
user-invocable: true
allowed-tools: Read Grep
model: inherit
---
```

| Campo | Required | Descripción |
|---|---|---|
| `name` | No | Display name. Si se omite, usa el nombre del directorio. Lowercase, hyphens, max 64 chars. |
| `description` | **Recomendado** | Qué hace la skill y cuándo usarla. Claude usa esto para decidir cuándo aplicar. Si se omite, usa el primer párrafo del markdown. **Truncado a 1,536 chars en el listing.** |
| `when_to_use` | No | Contexto adicional sobre cuándo invocar. Se concatena al description. |
| `argument-hint` | No | Hint para autocomplete. Ej.: `[issue-number]`. |
| `arguments` | No | Argumentos posicionales nombrados para `$name` substitution. |
| `disable-model-invocation` | No | `true` = solo el usuario puede invocar (no Claude automático). Útil para `/deploy`, `/commit`. |
| `user-invocable` | No | `false` = oculta del menú `/`. Útil para conocimiento de fondo. |
| `allowed-tools` | No | Tools que Claude puede usar sin pedir permiso cuando la skill está activa. |
| `model` | No | Override del modelo. Solo durante el turno actual. |
| `effort` | No | low / medium / high / xhigh / max. |
| `context` | No | `fork` = ejecuta en subagente forked. |
| `agent` | No | Qué tipo de subagent usar cuando `context: fork`. Default: `general-purpose`. |
| `paths` | No | Glob patterns que limitan cuándo se activa la skill. |
| `hooks` | No | Hooks scoped al lifecycle de la skill. |

## Tipos de contenido

### Reference content
Conocimiento que Claude aplica a tu trabajo actual. Convenciones, patrones, style guides, dominio. Corre **inline** con la conversación.

```yaml
---
name: api-conventions
description: API design patterns for this codebase
---

When writing API endpoints:
- Use RESTful naming conventions
- Return consistent error formats
```

### Task content
Instrucciones step-by-step para una acción específica. Suele invocarse manualmente con `/skill-name`. Recomienda añadir `disable-model-invocation: true`.

```yaml
---
name: deploy
description: Deploy the application to production
context: fork
disable-model-invocation: true
---

Deploy the application:
1. Run the test suite
2. Build the application
3. Push to the deployment target
```

## Substitución de strings

| Variable | Descripción |
|---|---|
| `$ARGUMENTS` | Todos los argumentos pasados al invocar |
| `$ARGUMENTS[N]` | Argumento por índice (0-based) |
| `$N` | Shorthand de `$ARGUMENTS[N]` |
| `$name` | Argumento nombrado declarado en frontmatter `arguments:` |
| `${CLAUDE_SESSION_ID}` | ID de la sesión actual |
| `${CLAUDE_EFFORT}` | low / medium / high / xhigh / max |
| `${CLAUDE_SKILL_DIR}` | Directorio que contiene `SKILL.md` |

## Inyección de contexto dinámico

Sintaxis ``!`<command>`'' ejecuta comandos shell **antes** de que el contenido se envíe a Claude. La salida reemplaza el placeholder.

```yaml
---
name: pr-summary
description: Summarize changes in a pull request
context: fork
agent: Explore
allowed-tools: Bash(gh *)
---

## Pull request context
- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`

## Your task
Summarize this pull request...
```

Esto es **preprocessing**, no algo que Claude ejecute. Claude solo ve el resultado final.

## Skills en subagents

Con `context: fork`, una skill se ejecuta en un subagent forkeado:

| Approach | System prompt | Task | También carga |
|---|---|---|---|
| Skill con `context: fork` | Del agent type (Explore, Plan...) | Contenido de SKILL.md | CLAUDE.md |
| Subagent con campo `skills` | Body del subagent | Mensaje de delegación | Skills preloaded + CLAUDE.md |

## Lifecycle del contenido

> *"When you or Claude invoke a skill, the rendered SKILL.md content enters the conversation as a single message and stays there for the rest of the session. Claude Code does not re-read the skill file on later turns, so write guidance that should apply throughout a task as standing instructions rather than one-time steps."*

Auto-compaction mantiene los primeros 5,000 tokens de cada skill después de un summary. Re-attach skills comparten un budget combinado de 25,000 tokens.

## Best practices

1. **Description front-loaded:** los keywords clave al principio de la frase. La descripción se trunca a 1,536 chars.
2. **Mantener SKILL.md < 500 líneas.** Material extra en archivos referenciados.
3. **Reference supporting files** explícitamente desde SKILL.md para que Claude sepa qué contienen.
4. **Para skills de acción** (deploy, commit, send-message): `disable-model-invocation: true` para que solo el usuario las invoque.
5. **Para skills de conocimiento de fondo** (legacy-system-context): `user-invocable: false`.
6. **Allowed-tools** para autorizar tools sin prompt mientras la skill está activa.
7. **Description debe matchear lenguaje natural del usuario** — "How does this work?" debe disparar `explain-code`.

## Aplicabilidad a SEM-IA

Materialización directa de las skills de cada rol del catálogo SEM-IA.

Implicaciones:

1. **Cada skill del Coach y del PO se materializa como `.claude/skills/<rol>/<skill>/SKILL.md`** (con su carpeta).
2. **Reference material extenso** (ejemplos detallados, frameworks bibliográficos completos) va en archivos auxiliares: `examples.md`, `reference.md`, `patterns.md`, etc.
3. **`description` debe matchear el flujo SEM-IA**: "Use this skill when validating a goal during inception" en lugar de descripción genérica.
4. **Skills de domain knowledge** (sin acción explícita): pueden estar `user-invocable: false` para que solo Claude las cargue cuando es relevante.
5. **Skills con acciones de archivos** (escribir un nodo, mover de active a archive): consideran `disable-model-invocation: true` y los `allowed-tools`.
6. **Para auditabilidad: el contenido bibliográfico de la skill DEBE referenciar `vault/architect/research/library/<fuente>.md`** explícitamente. Esto cierra el loop con la decisión de "documentación EN el vault" — las skills pueden citar pero el contenido vive en el vault.
