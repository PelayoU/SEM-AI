---
type: research
id: borrador-skill-architect-coupling-detection
title: "Borrador de skill: architect.coupling-detection"
status: draft
created: 2026-04-30
author: pelayo
tags: [skill-borrador, architect, coupling, happy-path]
---

# Borrador de skill: architect.coupling-detection

> **Estado: borrador.** Materialización en `.claude/skills/architect/coupling-detection/SKILL.md`.

## Propósito

Identificar **acoplamientos** entre features, capabilities, módulos de código, o nodos del grafo. Distinguir entre **acoplamiento apropiado** (deseado, necesario, alineado con dominio) y **acoplamiento problemático** (no deseado, oculto, fuera de boundaries).

Aplicable tanto a:
- **Acoplamiento entre nodos del grafo** (ej. feature A `depends-on` feature B porque comparten lógica de negocio relacionada).
- **Acoplamiento entre módulos de código** (ej. clase X importa de clase Y de capa más externa).

## Cuándo se invoca

- **Trigger principal:** durante `feature-viability-review` paso 5.
- **Trigger secundario:** revisión periódica del repo cuando se sospecha deuda arquitectónica.
- **Trigger asistencial:** humano pide "ver acoplamientos".

## Inputs

- Feature / capability / módulo a revisar.
- Otras features / módulos del proyecto (lectura focalizada en los que comparten dimensiones).
- ADRs existentes (algunos ADRs declaran explícitamente acoplamientos permitidos / prohibidos).
- Library: [[library-ousterhout-philosophy-software-design]], [[library-martin-clean-architecture]], [[library-ford-evolutionary-architecture]].

## Proceso — 5 pasos

### Paso 1 — Inventariar acoplamientos declarados
- `depends-on` declarados en frontmatter de la feature.
- `also-relates-to` declarados.
- `related-adrs` declarados.

Estos son **acoplamientos visibles**. Empezar aquí.

### Paso 2 — Detectar acoplamientos NO declarados (visibles en código)
Búsqueda de imports / referencias entre módulos:
- ¿Algún archivo de la feature importa de un módulo no declarado en `depends-on`?
- ¿Algún archivo de otra feature importa de la nueva sin que esté en `also-relates-to`?

Estos son **acoplamientos ocultos** — los más problemáticos.

### Paso 3 — Evaluar contra Dependency Rule (Martin)
Para cada acoplamiento detectado:
- ¿La dependencia apunta hacia adentro (capa más interna)? ✅ OK.
- ¿La dependencia apunta hacia afuera (capa más externa)? ❌ Violación de Dependency Rule.

### Paso 4 — Detectar information leakage (Ousterhout)
- ¿Hay conocimiento (de implementación, datos, lógica) que aparece en múltiples lugares?
- Ejemplo: si dos features tienen ambas lógica que asume el formato de fecha "DD/MM/YYYY", hay leakage del conocimiento "formato de fecha".

Solución típica: extraer el conocimiento a un módulo común (utility, schema, helper) que ambas features usan.

### Paso 5 — Categorizar cada acoplamiento

| Categoría | Significado | Acción |
|---|---|---|
| **Apropiado declarado** | Acoplamiento necesario, declarado en frontmatter, alineado con dominio. | Aceptar. |
| **Apropiado no declarado** | Acoplamiento necesario pero no declarado. | Pedir al PO que lo declare en frontmatter. |
| **Problemático declarado** | Acoplamiento no deseado pero existe. | Refactorizar (puede requerir ADR). |
| **Problemático no declarado** | Acoplamiento oculto y no deseado. | Refactorizar urgente. Posible ADR sobre cómo evitar futuros. |

## Output format

Reporte estructurado:

```markdown
## Acoplamientos detectados — feature-N

### Apropiados declarados
- feature-N → feature-M (depends-on declarado, dominio compartido X)

### Apropiados no declarados
- feature-N → feature-K (declaración pendiente: añadir a `depends-on`)

### Problemáticos declarados
- feature-N → feature-J (información leakage de schema de datos. Refactorizar a módulo común `data-schema`.)

### Problemáticos no declarados
- (ninguno, o lista detallada)
```

**Recomendación final:**
1. **Aprobar** — solo acoplamientos apropiados.
2. **Aprobar con declaraciones pendientes** — añadir cross-links faltantes.
3. **Refactorizar antes de implementar** — acoplamientos problemáticos requieren resolución.
4. **Escalar a ADR** — el patrón de acoplamiento es decisión arquitectónica significativa.

## Fundamento bibliográfico

- [[library-ousterhout-philosophy-software-design]] — information leakage como acoplamiento insidioso.
- [[library-martin-clean-architecture]] — Dependency Rule.
- [[library-ford-evolutionary-architecture]] — distinción appropriate vs. inappropriate coupling.

## Ejemplo aplicado

**Feature:** `feature-009` (favoritos) en repo de recetas.

| Acoplamiento | Categoría | Acción |
|---|---|---|
| feature-009 → feature-001 (formulario, depends-on declarado) | Apropiado declarado | Aceptar |
| feature-009 → feature-002 (guardado SQLite, depends-on declarado) | Apropiado declarado | Aceptar |
| feature-009 → feature-003 (tags, also-relates-to declarado) | Apropiado declarado | Aceptar (patrón visual similar) |
| feature-009 → feature-006 (búsqueda — relación lógica entre filtros) | Apropiado **NO declarado** | Pedir al PO añadir `also-relates-to: feature-006` |

**Recomendación:** Aprobar con declaraciones pendientes — añadir `also-relates-to: feature-006`.

## Limitaciones

- "Apropiado" depende del dominio. Lo que es leakage en un proyecto puede ser legítimo en otro.
- Detección automatizada de acoplamiento de código requiere parsing — vault-cli inicial no lo cubre. La skill se ejecuta semi-manualmente con el Architect agente leyendo código.
- Para proyectos en bootstrapping (poco código), el coupling-detection es más predictivo — sugerir patrones para evitar acoplamiento futuro.
