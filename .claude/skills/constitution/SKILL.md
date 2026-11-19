---
name: constitution
description: Aplica los principios, restricciones y estándares no negociables definidos en /specs/constitution.md para el Spec-Driven Development. Úsala para validar especificaciones, planes, tareas o código.
---

# Desarrollo Guiado por Especificaciones: Constitución

Esta skill instruye al agente a aplicar y respetar la constitución del proyecto en el desarrollo asistido por IA (Spec-Driven Development), usando el archivo `/specs/constitution.md`.

## El archivo de constitución

Un archivo de constitución captura principios, restricciones y estándares no negociables que rigen el proyecto. Sirve como barandilla inquebrantable para el desarrollo asistido por IA. 

Cuando el agente genera especificaciones, planes, tareas o código, **debe hacer referencia a la constitución** para comprobar que las propuestas cumplen con sus estándares.

---

## Principios y Estándares Innegociables

Las directivas obligatorias contenidas en `/specs/constitution.md` abarcan:

1. **Estándares Tecnológicos y Dependencias:**
   - Auditoría obligatoria de versiones estables más recientes (`latest stable` o LTS vigente) antes de proponer paquetes o scaffolding. Prohibido usar librerías desactualizadas o incompatibles.
2. **Resiliencia y Conectividad:**
   - Tolerancia a desconexión, degradación elegante y reintentos pasivos en background con backoff exponencial y jitter (sin congelar la UI).
3. **Experiencia de Usuario (UX) y Frontend:**
   - Pantallas y componentes con *Skeletons* estructurales para cargas asíncronas y *empty states* descriptivos.
   - Protección activa contra pérdida de datos en formularios: detección de cambios sin guardar (*dirty state*) con advertencia al salir y auto-guardado de borradores temporales.
4. **Seguridad y Control de Abusos:**
   - Validación estricta con esquemas en cliente y servicios.
   - Prevención de doble clic mediante debounce/deshabilitación en botones de envío.
   - Límites de tasa (*rate-limiting*) en llamadas críticas y aislamiento seguro de credenciales.
5. **Estándares de Codificación:**
   - Test-Driven Development (TDD): pruebas primero.
   - Desglose de tareas en grupos pequeños para permitir revisión incremental y commits parciales.

---

## Instrucciones para el Agente

1. **Validación:** Antes de proponer una nueva arquitectura, escribir especificaciones o generar código, lee `/specs/constitution.md` y verifica que la propuesta cumple con las reglas descritas.
2. **Defensa de los estándares:** Si se propone algo que entra en conflicto con la constitución (ej. componentes sin skeleton, peticiones sin reintentos o paquetes desactualizados), señala la violación de inmediato y propón la solución alineada.
3. **Mantenimiento:** Si se acuerdan nuevas reglas o restricciones innegociables durante el proyecto, agrégalas a `/specs/constitution.md`.
