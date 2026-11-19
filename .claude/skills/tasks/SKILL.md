---
name: tasks
description: Convierte las decisiones de spec.md y plan.md en una lista de tareas de implementación (tasks.md). Organiza las tareas en fases y grupos lógicos pequeños para facilitar la revisión de código y permitir commits parciales e incrementales.
---

# Generar Tareas de Implementación (tasks.md)

En la metodología Spec-Driven Development, los planes técnicos (`plan.md`) proporcionan la dirección arquitectónica, pero la implementación requiere pasos concretos. Esta skill toma `spec.md` y `plan.md` y genera el archivo `tasks.md` (la hoja de ruta de ejecución).

**REGLA CARDINAL: PROHIBIDO VOLCAR TAREAS MONOLÍTICAS DE GOLPE.**
Las tareas deben estar rigurosamente organizadas en **Fases** y subdivididas en **Grupos Lógicos Pequeños (2 a 4 tareas por grupo)**. Cada grupo representa una unidad de entrega funcional con su propio punto de revisión y sugerencia de commit parcial, facilitando la auditoría de código incremental.

---

## 1. Criterios para cada Tarea y Grupo Lógico

Toda tarea debe ser:
- **Accionable y Específica**: Indica claramente qué archivo o componente se crea/modifica y qué comportamiento se agrega.
- **Verificable (Testable)**: Se comprueba mediante un test unitario, de integración o validación manual inmediata.
- **Granularidad Acotada**: Una tarea atómica no debe tomar más de 1-2 horas de trabajo.

Cada **Grupo Lógico (Lote de Revisión)** debe contener:
- **Máximo 2 a 4 tareas atómicas relacionadas**.
- **Criterios de Aceptación / Requisitos vinculados**.
- **Punto de Revisión**: Instrucción concreta para que el usuario o la IA valide el código antes de continuar (ej. tests que deben pasar, pantalla a inspeccionar).
- **Sugerencia de Commit Parcial**: Mensaje semántico (`feat(scope): ...`, `fix(scope): ...`) para asentar el progreso incremental en git.

---

## 2. Cobertura Obligatoria de Pilares Transversales

El desglose en `tasks.md` debe incluir tareas explícitas para:
1. **Auditoría de Dependencias (Fase 1 / Setup):** Instalar y verificar versiones `latest stable` compatibles (consultando el gestor de paquetes y asegurando que no rompan el proyecto).
2. **Resiliencia de Red (Fase 2 / Servicios):** Cliente HTTP con reintentos pasivos en segundo plano (exponential backoff + jitter) y tolerancia offline/fallback.
3. **UX y Skeletons (Fase 3 / UI):** Componentes Skeleton estructurales para cargas asíncronas y empty states descriptivos.
4. **Protección de Formularios (Fase 3 / UI):** Detección de formulario sucio (*dirty state* con confirmación de salida) y persistencia de borradores (*draft auto-save*).
5. **Seguridad y Abuso (Fase 4 / Seguridad):** Debounce en disparadores para prevenir doble submit, esquemas de validación estricta y rate-limiting.

---

## 3. Estructura Obligatoria de `tasks.md`

Genera el archivo siguiendo la plantilla de `specs/_template/tasks.md`:

```markdown
# Lista de Tareas: <Nombre de la Funcionalidad / Subfase>

> **Organización por Grupos de Revisión y Commits Parciales:**
> Las tareas están agrupadas en bloques cohesivos pequeños (2 a 4 tareas por grupo). Al finalizar cada grupo, se realiza una pausa para revisión del código generado, ejecución de tests y commit parcial independiente.

## Fase 1: Setup, Modelos y Contratos de Datos

### Grupo 1.1: Scaffolding, Dependencias y Esquemas Base
- [ ] 1.1.1 Auditar e instalar dependencias requeridas en sus versiones latest stable compatibles
- [ ] 1.1.2 Definir modelos de datos y esquemas de validación estricta (Zod/Pydantic/tipos)
- [ ] 1.1.3 Escribir tests unitarios para validación de esquemas y transformaciones
*Punto de Revisión:* Builds y tests unitarios de esquemas en verde; dependencias sin conflictos.
*Commit Parcial sugerido:* `feat(core): dependencias latest y modelos base para <funcionalidad>`

## Fase 2: Servicios, Conectividad y Resiliencia

### Grupo 2.1: Lógica de Servicios y Reintentos Pasivos
- [ ] 2.1.1 Implementar servicios con reintentos pasivos en background (backoff + jitter)
- [ ] 2.1.2 Implementar manejo de desconexión / offline fallback y persistencia
- [ ] 2.1.3 Escribir pruebas unitarias simulando cortes de red y timeouts
*Punto de Revisión:* Validar resiliencia ante red inestable y degradación elegante.
*Commit Parcial sugerido:* `feat(services): servicios con reintentos pasivos y tolerancia offline`

## Fase 3: Interfaz de Usuario y Experiencia (UX)

### Grupo 3.1: Vistas Base, Estados de Carga y Skeletons
- [ ] 3.1.1 Construir estructura de vistas y navegación
- [ ] 3.1.2 Implementar componentes Skeleton estructurales para cargas asíncronas
- [ ] 3.1.3 Implementar estados vacíos (empty states) y feedback contextual
*Punto de Revisión:* Transición fluida de Skeletons a contenido real sin parpadeos.
*Commit Parcial sugerido:* `feat(ui): vistas con skeletons estructurales y empty states`

### Grupo 3.2: Formularios Protegidos y Prevención de Pérdida de Datos
- [ ] 3.2.1 Construir campos de formulario conectados a los esquemas
- [ ] 3.2.2 Implementar persistencia de borrador temporal (draft auto-save)
- [ ] 3.2.3 Implementar confirmación de salida ante formulario sucio (dirty state)
*Punto de Revisión:* Probar recargar y salir del formulario; verificar que no se pierden datos.
*Commit Parcial sugerido:* `feat(ui): formularios con auto-guardado y protección dirty state`

## Fase 4: Seguridad, Prevención de Abusos y Casos Extremos

### Grupo 4.1: Mitigación de Abusos y Validaciones Perimetrales
- [ ] 4.1.1 Implementar debounce y deshabilitación inmediata en botones de envío
- [ ] 4.1.2 Configurar rate-limiting en operaciones críticas
- [ ] 4.1.3 Implementar cobertura de Casos Extremos (CE-1 a CE-4)
*Punto de Revisión:* Probar clics repetidos rápidos en submit y verificar un único envío.
*Commit Parcial sugerido:* `feat(security): debounce de envíos, rate-limiting y casos extremos`

## Fase 5: QA Integral, Checklist y Documentación

### Grupo 5.1: Validación de Checklist y Cierre de Subfase
- [ ] 5.1.1 Ejecutar suite completa de tests automatizados
- [ ] 5.1.2 Ejecutar y verificar todos los escenarios de checklist.md
- [ ] 5.1.3 Actualizar specs/roadmap.md marcando la subfase concluida
*Punto de Revisión:* Todos los checks de lint y tests en verde; checklist.md marcado.
*Commit Parcial sugerido:* `test(qa): validación de checklist y cierre de subfase <funcionalidad>`
```

---

## 4. Revisión Crítica (Auditoría Interna)

Antes de entregar `tasks.md`:
1. **Cobertura del Plan y Spec**: Cada Criterio de Aceptación y decisión del plan debe estar contemplado en al menos un grupo de tareas.
2. **Tamaño de Grupos**: Ningún grupo debe contener más de 4 tareas para no sobrecargar las revisiones.
3. **Puntos de Commit**: Cada grupo debe tener su recomendación de commit semántico parcial.
4. **Presentación**: Explica al usuario cómo se estructuraron los grupos y cómo podrá ir revisando y comiteando por partes durante la fase `implement`.
