---
category: bibliography-source
id: library-anthropic-subagents
title: "Anthropic — Subagents en Claude Code"
status: draft
created: 2026-04-30
author: pelayo
tags: [library, anthropic, claude-code, subagents, infrastructure]
applicable-roles: [all]
---

# Anthropic — Subagents en Claude Code

## Datos bibliográficos

- **Fuente:** Documentación oficial de Anthropic / Claude Code.
- **URL canónica:** https://code.claude.com/docs/en/sub-agents (redirección desde docs.claude.com)
- **Fecha de consulta:** 2026-04-30
- **Aplicabilidad SEM-IA:** infraestructura — define cómo se materializan los agentes homólogos del modelo SEM-IA en Claude Code.

## Concepto

> *"Subagents are specialized AI assistants that handle specific types of tasks. Use one when a side task would flood your main conversation with search results, logs, or file contents you won't reference again: the subagent does that work in its own context and returns only the summary."*

Cada subagent corre en su **propio context window**, con **system prompt custom**, **acceso específico a tools**, e **permisos independientes**. Cuando Claude detecta una tarea que matchea la `description` de un subagent, delega a ese subagent, que trabaja independientemente y devuelve resultados.

Los subagents permiten:
- **Preservar contexto** — el trabajo de exploración no contamina la conversación principal.
- **Reforzar restricciones** — limitar qué tools puede usar cada subagent.
- **Reusar configuraciones** — definidos a nivel proyecto o usuario.
- **Especializar comportamiento** — system prompts focalizados por dominio.
- **Controlar coste** — derivar tareas a modelos más rápidos / baratos (Haiku).

## Formato del archivo

Subagents se definen como archivos Markdown con **frontmatter YAML** + **system prompt en el cuerpo**.

### Ubicación

| Tipo | Ruta | Aplica a |
|---|---|---|
| Proyecto | `.claude/agents/<name>.md` | Solo este proyecto |
| Usuario | `~/.claude/agents/<name>.md` | Todos los proyectos del usuario |
| Plugin | `<plugin>/agents/<name>.md` | Donde el plugin esté habilitado |

Si hay conflicto de nombres, **proyecto sobreescribe a usuario, usuario sobreescribe a plugin**.

### Frontmatter — campos

```yaml
---
name: <nombre-del-subagent>           # REQUERIDO
description: <cuándo usar el subagent> # REQUERIDO
tools: [Read, Grep, Glob]              # opcional — lista de tools accesibles
model: opus                            # opcional — sonnet, opus, haiku, o ID completo
---
```

- **`name`:** identificador del subagent. Lowercase, hyphens.
- **`description`:** Claude usa esta cadena para decidir cuándo invocar el subagent. **Crítico: debe contener keywords que matcheen lo que el usuario diría naturalmente.**
- **`tools`:** lista explícita de tools que el subagent puede usar. Si se omite, hereda los tools del agente padre.
- **`model`:** override del modelo. Útil para usar Haiku para tareas baratas o forzar Opus para razonamiento profundo.

### Cuerpo del archivo

Todo lo que sigue al frontmatter es el **system prompt** del subagent. Define:
- Identidad del subagent
- Dominio de trabajo
- Protocolo de operación
- Reglas y excepciones
- Lo que NO debe hacer

## Cómo se invocan

1. **Delegación automática:** Claude lee la `description` de los subagents disponibles y delega cuando una tarea matchea.
2. **Invocación explícita:** desde el agente padre, vía la herramienta Agent (Task tool), pasando `subagent_type` con el nombre del subagent.

## Best practices para subagent prompts

Inferidas de la documentación + ejemplos canónicos:

1. **Description focalizada:** una sola frase que diga exactamente cuándo usar el subagent. Front-load keywords.
2. **System prompt con identidad clara:** "Eres el X del proyecto. Tu función es..."
3. **Vault scope explícito** (en SEM-IA): qué archivos lee, qué archivos escribe.
4. **Protocolo numerado:** pasos concretos que el subagent sigue al ser invocado.
5. **"Lo que NO haces":** reglas de exclusión explícitas para evitar overreach.
6. **Tools restringidas:** si el subagent es lectura-solo, no darle tools de escritura.
7. **Modelo apropiado:** Opus para razonamiento estratégico, Sonnet para implementación, Haiku para clasificación o tareas mecánicas.

## Skills preloaded en subagents

Los subagents pueden cargar skills al iniciarse vía el campo `skills` (cuando se define el subagent en frontmatter del prompt). El contenido completo de la skill se inyecta al inicio del subagent, no se carga bajo demanda.

> *"With `context: fork` (skill), you write the task in your skill and pick an agent type to execute it. For the inverse (defining a custom subagent that uses skills as reference material), see Subagents > preload skills into subagents."*

## Aplicabilidad a SEM-IA

**Crítica para todos los roles.** Cada agente homólogo de SEM-IA (Coach, PO, Architect, etc.) se materializa como un subagent en `.claude/agents/<nombre>.md`. La calidad del system prompt determina la calidad de la operación del rol.

Implicaciones:

1. **Los archivos `.claude/agents/<rol>.md` actuales son la materialización**, no documentación. Su redacción importa operativamente.
2. **`description` debe contener keywords del flujo SEM-IA** (inception, strategy, spec, ADR, etc.) para que recepción los detecte.
3. **`tools` debe restringirse** según la dimensión custodiada — el Coach no necesita Bash de escritura, el Security Officer probablemente sí.
4. **`model` se elige según rol** — Opus para Coach/Architect/Security/Quant; Sonnet para Developer/QA/DBA.
5. **Skills del rol se referencian desde el cuerpo del prompt** y/o se preload mediante el campo skills cuando se invoca.
