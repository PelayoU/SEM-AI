---
type: goal
id: goal-3-absorcion-coste-revision
title: "Absorción estructural del coste de revisar la IA"
parent: vision
also-relates-to: [goal-2-output-auditable-multirol, goal-4-rigor-multirol-individual]
depends-on: []
dimensions-affected: [product]
status: active
created: 2026-05-10
author: pelayo
nature: controlable
---

# Goal-3: Absorción estructural del coste de revisar la IA

## Resultado esperado

El humano que trabaja con SEM-IA no asume el coste multiplicado de revisar el output de la IA. La infraestructura lo absorbe estructuralmente vía contexto persistente (vault), scope-scan multi-rol al crear y al cerrar cada bloque de trabajo, y verificación cruzada previa al cierre.

La revisión humana deja de ser **descubrimiento** ("¿qué se desvió?") y pasa a ser **validación** ("confirmar lo ya registrado como conforme").

## Métricas

- **Cumplimiento:** ≥ 80 % de drift / contradicciones / regresiones detectados **pre-cierre** (no post-cierre, no en producción).
- **Señal:** Tiempo de revisión por feature comparable o inferior al baseline humano-sin-IA en proyectos pilot (benchmark estilo METR).
- **Señal:** Eliminación efectiva del "coste multiplicado en capas" — los roles superiores no vuelven a verificar desde cero, validan trabajo ya pre-revisado por los custodios apropiados.

## Conexión con la visión

Aborda directamente el problema operativo que el contexto de la visión diagnostica: *"revisar lo que produce es caro y ese coste se multiplica en capas"*. SEM-IA invierte el paradigma: la infraestructura absorbe ese coste, no el humano. Sin este goal, la visión sería diagnóstico sin remedio operativo.

## Fundamento bibliográfico

- **Cagan — *Inspired*.** Risks abordados antes de construir, no después.
- **Reportes recientes (citados en prefacio):** METR (2025) 19 % slowdown · Uplevel (2024) 41 % más bugs · Stack Overflow (2025) 66 % frustración. Datos del problema que este goal resuelve.
