---
name: analyze
description: Realiza la comprobación de coherencia cruzada entre todos los artefactos SDD (spec, plan, tasks, checklist) y la constitución. Audita la cobertura de requisitos generales, pilares transversales, dependencias latest stable, secuencias y desglose en grupos lógicos antes de codificar.
---

# Análisis de Coherencia de Artefactos (Quality Assurance Integral)

En el Spec-Driven Development (SDD), la integridad documental es la base del éxito. La skill `analyze` actúa como un auditor de sistemas estricto que evalúa la coherencia cruzada entre `spec.md`, `plan.md`, `tasks.md`, `checklist.md` y `specs/constitution.md`, idealmente justo antes de que comience la fase de programación (construcción). 

Cada incoherencia identificada aquí es un error, un "bug arquitectónico" o una refactorización que de otro modo explotaría durante la implementación o en la revisión de código.

---

## 1. Comprobaciones de Integridad y Coherencia

Al ejecutar esta skill, debes cargar todos los archivos de la subfase (`spec.md`, `plan.md`, `tasks.md`, `checklist.md`) y contrastarlos con las reglas maestras (`specs/constitution.md` y `specs/tech-stack.md`). Realiza estas auditorías:

### A. Cobertura de Requisitos (`spec.md` ➔ `plan.md`)
- Cruza cada Criterio de Aceptación, Requisito y Caso Extremo del `spec.md` contra el `plan.md`.
- **Fallo si:** El `spec.md` exige algo (ej. *"Mostrar un mensaje de error para archivos mayores a 50MB"*) pero el `plan.md` omite explicar *dónde y cómo* se va a manejar esa validación (en el front, en un middleware, etc.).
- **Fallo si:** El plan omite cómo se manejarán los pilares transversales requeridos: la **tolerancia a desconexión y reintentos pasivos**, el diseño de **Skeletons** estructurales para cargas asíncronas, la **protección de pérdida de datos en formularios** (dirty state y borradores), o los mecanismos de seguridad (**debounce** contra doble submit y **rate-limiting**).

### B. Cobertura de Implementación (`plan.md` ➔ `tasks.md`)
- Revisa las decisiones arquitectónicas y la pila tecnológica del `plan.md`.
- Verifica que el `tasks.md` incluya al menos una tarea explícita para cada componente del plan.
- **Fallo si:** El `plan.md` detalla que *"Se usará Amazon S3 para guardar los documentos"*, pero en el `tasks.md` no existe ninguna tarea de configuración de S3 ni de implementación de su SDK.
- **Fallo si:** Las tareas están volcadas de golpe en una lista plana monolítica en lugar de estar seccionadas en **Grupos Lógicos pequeños (2 a 4 tareas)** con puntos de revisión y commits parciales sugeridos.
- **Fallo si:** Falta la tarea explícita de auditoría de dependencias en versiones `latest stable` compatibles en la Fase 1.

### C. Auditoría de Constitución (Todos ➔ `constitution.md`)
- Contrapón las propuestas contra las reglas innegociables de `specs/constitution.md`, así como las herramientas de `specs/tech-stack.md`.
- **Fallo si:** Las tareas proponen almacenar un token en un lugar inseguro, o se propone una librería externa no listada en el stack sin justificación, o se rompe la arquitectura Local-First.
- **Fallo si:** Se proponen paquetes desactualizados sin verificar `latest stable` o se violan los principios de resiliencia, UX y no-intrusión.

### D. Secuencia y Bloqueos (`tasks.md`)
- Analiza la secuencia lógica de fases y grupos de tareas.
- **Fallo si:** Hay tareas de frontend planificadas antes de que se haya listado la creación de las tablas de base de datos o los endpoints que ese frontend va a consumir.
- **Fallo si:** Tareas con dependencias externas bloqueadas no están marcadas explícitamente como `BLOQUEADO`.

### E. Auditoría de Pruebas de QA (`spec.md` ➔ `checklist.md`)
- Verifica que todos los `CA-X`, `CE-X` y las pruebas de desconexión, skeletons, formularios y escenarios "¿Qué pasaría si...?" tengan casos de comprobación en `checklist.md`.
- **Fallo si:** Existen Criterios de Aceptación o Casos Extremos en `spec.md` sin cobertura en la tabla de QA.

### F. Dimensionalidad y Consistencia con Roadmap
- Verifica que la especificación corresponda a una subfase atómica de `specs/roadmap.md` y no exceda el límite de ~250 líneas.

---

## 2. Reporte de Análisis

Tras el escrutinio, genera un **Reporte de Coherencia**:

1. Si no hay fallos: *"El Análisis ha finalizado con éxito. Los artefactos están 100% alineados, desglosados en grupos lógicos y listos para la implementación."*
2. Si detectas problemas, agrúpalos por tipo (Laguna de especificación, Falta de tarea, Violación de constitución, Error de secuencia).
3. Para cada problema, sé estrictamente accionable:
   - Menciona el documento que está incompleto o erróneo (`spec.md`, `plan.md`, `tasks.md`, `checklist.md`).
   - **Explica el motivo de la inconsistencia:** Detalla exactamente por qué es un problema y el impacto que tendría durante el desarrollo.
   - **Propón la solución exacta:** Redacta el texto exacto a insertar o modificar (ej. *"Sugiero agregar la Tarea 4.2 en tasks.md para el manejo de logs de auditoría estipulado en el plan"*).

---

## 3. Resolución Interactiva

Pregunta al usuario si da luz verde para que apliques las correcciones sugeridas en los archivos correspondientes. Si acepta, actualiza los documentos para blindar el paquete antes de la fase de código.
