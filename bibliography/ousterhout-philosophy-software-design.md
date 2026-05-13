---
category: bibliography-source
id: library-ousterhout-philosophy-software-design
title: "John Ousterhout — A Philosophy of Software Design"
status: draft
created: 2026-04-30
author: pelayo
tags: [library, modularity, complexity, information-hiding, architect]
applicable-roles: [architect, developer]
---

# John Ousterhout — A Philosophy of Software Design

## Datos bibliográficos

- **Autor:** John Ousterhout (Stanford University; creador de Tcl/Tk).
- **Obra:** *"A Philosophy of Software Design"* (Yaknyam Press, 1ª ed. 2018; 2ª ed. 2021).
- **Aplicabilidad SEM-IA:** dimensión `technical` — Architect al diseñar módulos, interfaces, abstracciones; Developer al implementar siguiendo principios de modularidad.

## Tesis central

> *"The greatest limitation in writing software is our ability to understand the systems we are creating."*

El enemigo del diseño de software es la **complejidad**. La complejidad no se puede eliminar pero **se puede gestionar** mediante decisiones disciplinadas de diseño.

## Cómo se manifiesta la complejidad

Ousterhout identifica tres síntomas:

### 1. Change amplification
Un cambio aparentemente simple requiere modificaciones en muchos lugares.

> *"A seemingly simple change requires code modifications in many different places."*

### 2. Cognitive load
El programador necesita conocer demasiadas cosas para hacer un cambio.

> *"A programmer needs to know too many things to make changes."*

### 3. Unknown unknowns
Hay cosas que el programador necesita saber pero no sabe que necesita saberlas.

> *"It's not obvious which pieces of code must be modified to complete a task, or what information a developer must have to carry out the task successfully."*

Ousterhout considera **unknown unknowns el peor de los tres** — al menos los otros dos son visibles.

## Estrategias de gestión de complejidad

### Eliminar complejidad
Hacer el código tan obvio como sea posible. Convenciones consistentes, nombres descriptivos, simplicidad de interfaz.

### Encapsular complejidad
Esconder la complejidad detrás de interfaces simples. **Esta es la estrategia central del libro.**

## Concepto central: Deep Modules

> *"The best modules are deep: they have a lot of functionality hidden behind a simple interface."*

Un módulo profundo tiene:
- **Interfaz pequeña** — pocas funciones públicas, pocos parámetros, contratos claros.
- **Implementación grande** — muchísima funcionalidad oculta tras la interfaz.

Ratio interfaz/implementación es lo que mide profundidad.

### Ejemplo canónico (Ousterhout)
**Linux file I/O.** Solo 5 funciones públicas (`open`, `close`, `read`, `write`, `lseek`) que ocultan:
- Representación en HDDs, SSDs, CDs, DVDs.
- Mapping de paths jerárquicos a directorios.
- Permisos de acceso.
- Acceso concurrente.
- Caching.
- Y mucho más.

**Esto es módulo profundo.**

### Antipatron: Shallow Modules

> *"A shallow module is a module with a large or complex interface but not so much depth."*

Módulos shallow proliferan en la práctica. Cada llamada a un módulo shallow tiene **alta complejidad cognitiva** porque la interfaz expone tanta cosa que el llamador tiene que entenderla casi tanto como la implementación.

## Information Hiding

> *"Information hiding is key to producing deep modules. You hide design decisions in the implementation, and ensure they don't appear in the modules interface."*

Información que NO debe estar en la interfaz:
- Cómo se almacenan los datos internamente.
- Algoritmos específicos usados.
- Decisiones de optimización.
- Detalles de comunicación con sistemas externos.

### Information Leakage (antipatron)

> *"Information leakage occurs when the same knowledge is used in multiple places."*

Si dos partes del sistema necesitan saber el mismo detalle de implementación, hay leakage. La solución: encapsular ese detalle en un módulo común que ambos usen.

## Otros principios destacados

- **Different layer, different abstraction** — cada capa debe operar a un nivel de abstracción distinto. Si dos capas hablan el mismo lenguaje, una está de más.
- **Comments should describe things that aren't obvious from the code** — no comentarios redundantes; sí comentarios sobre intent y rationale.
- **Define errors out of existence** — preferir diseño que no produzca errores, en lugar de diseño que produce errores y luego los maneja.
- **Pull complexity downwards** — la complejidad debe vivir en los módulos profundos (que la encapsulan), no en el código llamador.
- **Strategic vs. tactical programming** — invertir tiempo en diseño correcto al principio reduce coste futuro.

## Aplicabilidad a SEM-IA

**Skill `architect.feature-viability-review`:** evaluar si una feature mantiene módulos profundos. Si una feature requiere exponer muchos detalles de implementación al llamador, falla este principio.

**Skill `architect.coupling-detection`:** information leakage es una forma de acoplamiento problemático. Detectar leakage = detectar acoplamiento mal hecho.

**Skill `architect.coherence-evaluation`:** un cambio que aplana módulos (los hace más shallow) viola el principio. Marcarlo y proponer alternativa.

## Citas que anclan decisiones

> *"The best modules are deep: they have a lot of functionality hidden behind a simple interface."*

Aplicable a `feature-viability-review`: si una feature propone módulo con interfaz grande, marcar y proponer simplificación de interfaz.

> *"Information leakage occurs when the same knowledge is used in multiple places."*

Aplicable a `coupling-detection`: detectar conocimiento duplicado entre módulos / skills / plantillas. Es la forma más insidiosa de acoplamiento.

> *"Pull complexity downwards. Complexity is more easily tolerated in low-level modules than in high-level ones."*

Aplicable al diseño del framework: la complejidad de razonamiento (LLM) está en los agentes (low-level del framework, alto nivel de abstracción cognitiva); el código mismo (vault-cli) es simple.

## Limitaciones

- Las heurísticas son cualitativas. "Suficientemente profundo" no es métrica numérica.
- Ousterhout es opinionado — algunas posiciones (ej. evitar getters/setters, comentarios extensos) son discutibles.
- No cubre arquitectura distribuida; está enfocado en diseño de módulos dentro de un sistema.
