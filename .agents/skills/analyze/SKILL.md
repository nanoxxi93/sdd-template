---
name: analyze
description: Realiza la comprobación de coherencia cruzada entre todos los artefactos SDD (spec, plan, tasks, checklist) y la constitución. Audita la cobertura de los pilares transversales, dependencias latest stable y el desglose en grupos lógicos antes de codificar.
---

# Análisis de Coherencia de Artefactos (Quality Assurance Integral)

En el Spec-Driven Development (SDD), la integridad documental es la base del éxito. La skill `analyze` actúa como un auditor estricto que evalúa la coherencia cruzada entre `spec.md`, `plan.md`, `tasks.md`, `checklist.md` y `specs/constitution.md` antes de que comience la fase de programación.

---

## 1. Auditorías de Integridad y Coherencia

Carga los artefactos de la subfase y ejecuta sistemáticamente estas 5 comprobaciones:

### A. Cobertura de Requisitos y Pilares Transversales (`spec.md` ➔ `plan.md`)
- Cruza cada Criterio de Aceptación, Requisito y Caso Extremo contra el diseño del plan.
- **Fallo si:** El plan omite cómo se manejará la **tolerancia a desconexión y reintentos pasivos**.
- **Fallo si:** La interfaz carece de diseño de **Skeletons** estructurales para cargas asíncronas.
- **Fallo si:** Hay formularios pero el plan no contempla **protección de pérdida de datos** (borradores y confirmación ante dirty state).
- **Fallo si:** Los botones de acción no definen **debounce** o prevención de doble submit, o las APIs carecen de **rate-limiting**.

### B. Cobertura de Implementación y Grupos Lógicos (`plan.md` ➔ `tasks.md`)
- Verifica que cada decisión técnica y componente del plan tenga tareas explícitas asociadas.
- **Fallo si:** Las tareas están volcadas de golpe en una lista plana monolítica en lugar de estar seccionadas en **Grupos Lógicos pequeños (2 a 4 tareas)** con puntos de revisión y commits parciales.
- **Fallo si:** Falta la tarea de auditoría de dependencias en versiones `latest stable` compatibles en la Fase 1.

### C. Auditoría de Pruebas de QA (`spec.md` ➔ `checklist.md`)
- Verifica que todos los `CA-X`, `CE-X` y las pruebas de desconexión, skeletons y formularios tengan casos de comprobación en `checklist.md`.

### D. Auditoría Constitucional y de Versiones (Todos ➔ `constitution.md`)
- Comprueba que las librerías propuestas sean auditadas contra versiones `latest stable` vigentes y que no existan violaciones de privacidad, secretos o arquitectura.

### E. Dimensionalidad y Consistencia con Roadmap
- Verifica que la especificación corresponda a una subfase atómica de `specs/roadmap.md` y no exceda el límite de ~250 líneas.

---

## 2. Reporte de Análisis y Resolución

Genera un **Reporte de Coherencia**:
1. Si no hay fallos: *"El Análisis ha finalizado con éxito. Los artefactos están 100% alineados, desglosados en grupos lógicos y listos para la implementación."*
2. Si detectas problemas, agrúpalos por categoría (Lagunas de pilares transversales, Tareas no agrupadas, Versiones de dependencias, Violación constitucional).
3. Para cada problema, sé accionable indicando el archivo exacto y la solución redactada.
4. Solicita confirmación al usuario para aplicar automáticamente las correcciones antes de pasar a `implement`.
