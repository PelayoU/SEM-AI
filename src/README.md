# `src/` — Framework distribuible (`@sem-ia/cli`)

Aquí vivirá el paquete que un adopter instala vía `npm install -D @sem-ia/cli`. Hoy es **esqueleto vacío** — su construcción es una feature post-inception del propio framework.

## Estructura

```
src/
├── adapters/                ← un adapter por harness soportado
│   ├── claude-code/         ← bundled .claude/ + CLAUDE.md raíz formato Claude Code
│   ├── opencode/            ← futuro: bundled .opencode/ formato OpenCode
│   └── pi/                  ← futuro: bundled formato Pi
├── universal/               ← lo que NO depende de harness:
│                            │   - vault skeleton (estructura vacía + governance defaults)
│                            │   - schemas JSON para validación determinística
│                            │   - plantillas si finalmente se necesitan
├── cli/                     ← código del CLI:
│                            │   - sem-ia init       (bootstrap en repo del adopter)
│                            │   - sem-ia validate   (valida frontmatter contra schemas)
│                            │   - sem-ia check      (valida links del grafo)
│                            │   - sem-ia check coverage  (cobertura AC ↔ tests)
└── package.json             ← se publica a npm como @sem-ia/cli
```

## Por qué adapters multi-harness desde el principio

SEM-IA es **harness-agnostic conceptualmente**: la identidad de los roles, las skills, las plantillas y las dimensiones no dependen del runner. Pero **cada harness tiene su propia sintaxis** para descubrir agentes, skills, comandos.

- Claude Code → lee `.claude/agents/*.md`, `.claude/skills/<rol>/<skill>/SKILL.md`, `CLAUDE.md` jerárquico, `.claude/commands/*.md`.
- OpenCode (futuro) → formato propio.
- Pi (futuro) → formato propio.

El adapter hace el "render" del contenido universal al formato del harness destino. El usuario corre `npx sem-ia init --harness=claude-code` y recibe `.claude/` formato Claude Code. Si en el futuro corre `--harness=opencode`, recibe `.opencode/` formato OpenCode con el mismo contenido conceptual.

## Cómo se sincroniza con el dogfooding

Este repo (SEM-IA-the-project) tiene `.claude/` en raíz como **dogfooding** (SEM-IA usándose a sí mismo). Cuando `src/` exista, esa instancia se generará automáticamente desde `src/adapters/claude-code/` mediante un build step. Sin duplicación.

Decisión del mecanismo concreto (build script, symlinks, fuente única) → ADR pendiente: "Mecanismo de distribución del framework" (ver `vault/architect/research/bootstrap-summary.md`).

## Estado actual

`src/` está vacío. Los subdirectorios existen como placeholders arquitectónicos. Cuando se construya el paquete como feature formal:

1. Inception del framework decide el manifest exacto de qué bundle.
2. ADR cubre la estrategia de distribución y de sync con el dogfooding.
3. Se materializa el contenido en cada subdirectorio.
4. Se publica `@sem-ia/cli@0.1.0`.
