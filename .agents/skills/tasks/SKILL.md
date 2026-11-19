---
name: tasks
description: Convierte las decisiones de spec.md y plan.md en una lista de tareas de implementación (tasks.md). Las organiza por fases lógicas y grupos pequeños para facilitar la revisión de código y permitir commits parciales e incrementales.
---

# Generar Tareas de Implementación (tasks.md)

En la metodología Spec-Driven Development, los planes técnicos (`plan.md`) proporcionan la dirección arquitectónica, pero la implementación requiere pasos concretos. Esta skill toma `spec.md` y `plan.md` y genera el archivo `tasks.md` (la hoja de ruta de ejecución).

**REGLA CARDINAL: PROHIBIDO VOLCAR TAREAS MONOLÍTICAS DE GOLPE.**
Las tareas deben estar rigurosamente organizadas en **Fases** y subdivididas en **Grupos Lógicos Pequeños (2 a 4 tareas por grupo)**. Cada grupo representa una unidad de entrega funcional con su propio punto de revisión y sugerencia de commit parcial, facilitando la auditoría de código incremental.

---

## 1. Características de una Tarea Bien Definida

Toda tarea redactada en `tasks.md` debe cumplir con estos cuatro criterios:
- **Accionable**: Indica claramente qué se va a construir (ej. *"Implementar el endpoint POST /api/documents/upload que acepte X y devuelva Y"*).
- **Verificable (Testable)**: Es evidente cuándo la tarea está terminada y puede probarse de forma aislada mediante un test unitario, de integración o comprobación manual.
- **Independiente**: Se puede completar sin esperar a otro trabajo paralelo (respetando la secuencia lógica).
- **Límite de tiempo (Granularidad correcta)**: Su alcance representa horas o máximo un día de trabajo. No debe ser inmensa (*"Implementar todo el backend"*) ni excesivamente prescriptiva o diminuta (*"Añadir un punto y coma en la línea 42"*).

Cada **Grupo Lógico (Lote de Revisión)** debe contener:
- **Máximo 2 a 4 tareas atómicas relacionadas**.
- **Criterios de Aceptación / Requisitos vinculados**.
- **Punto de Revisión**: Instrucción concreta para que el usuario o la IA valide el código antes de continuar (ej. tests que deben pasar, pantalla a inspeccionar).
- **Sugerencia de Commit Parcial**: Mensaje semántico (`feat(scope): ...`, `fix(scope): ...`) para asentar el progreso incremental en git.

---

## 2. Organización Basada en Fases y Secuenciación

Las funcionalidades complejas deben dividirse en hitos lógicos. El orden de las fases y grupos es crítico para evitar bloqueos. Genera `tasks.md` siguiendo este esquema:

```markdown
# Lista de Tareas: <Nombre de la Funcionalidad / Subfase>

> **Organización por Grupos de Revisión y Commits Parciales:**
> Las tareas están agrupadas en bloques cohesivos pequeños (2 a 4 tareas por grupo). Al finalizar cada grupo, se realiza una pausa para revisión del código generado, ejecución de tests y commit parcial independiente.

## Fase 1: Setup, Modelos y Contratos de Datos
*(No hay dependencias. Desbloquea la Fase 2).*

### Grupo 1.1: Scaffolding, Dependencias y Esquemas Base
- [ ] 1.1.1 Auditar e instalar dependencias requeridas en sus versiones latest stable compatibles (sin romper librerías existentes)
- [ ] 1.1.2 Definir modelos de datos y esquemas de validación estricta (Zod/Pydantic/tipos)
- [ ] 1.1.3 Escribir tests unitarios para validación de esquemas y transformaciones
*Punto de Revisión:* Builds y tests unitarios de esquemas en verde; dependencias sin conflictos.
*Commit Parcial sugerido:* `feat(core): dependencias latest y modelos base para <funcionalidad>`

## Fase 2: Servicios, Conectividad y Resiliencia
*(Depende de la Fase 1. Desbloquea la Fase 3).*

### Grupo 2.1: Lógica de Servicios y Reintentos Pasivos
- [ ] 2.1.1 Implementar servicios con reintentos pasivos en background (backoff exponencial + jitter)
- [ ] 2.1.2 Implementar manejo de desconexión / offline fallback y persistencia
- [ ] 2.1.3 Escribir pruebas unitarias simulando cortes de red, timeouts y recuperación pasiva
*Punto de Revisión:* Validar resiliencia ante red inestable y degradación elegante.
*Commit Parcial sugerido:* `feat(services): servicios con reintentos pasivos y tolerancia offline`

## Fase 3: Interfaz de Usuario y Experiencia (UX)
*(Depende de la Fase 2).*

### Grupo 3.1: Vistas Base, Estados de Carga y Skeletons
- [ ] 3.1.1 Construir estructura de vistas y navegación
- [ ] 3.1.2 Implementar componentes Skeleton estructurales para cargas asíncronas
- [ ] 3.1.3 Implementar estados vacíos (empty states) y feedback contextual
*Punto de Revisión:* Transición fluida de Skeletons a contenido real sin saltos de layout (CLS).
*Commit Parcial sugerido:* `feat(ui): vistas con skeletons estructurales y empty states`

### Grupo 3.2: Formularios Protegidos y Prevención de Pérdida de Datos
- [ ] 3.2.1 Construir campos de formulario conectados a los esquemas
- [ ] 3.2.2 Implementar persistencia de borrador temporal (draft auto-save)
- [ ] 3.2.3 Implementar confirmación de salida ante formulario sucio (dirty state)
*Punto de Revisión:* Probar recargar y salir del formulario; verificar que no se pierden datos.
*Commit Parcial sugerido:* `feat(ui): formularios con auto-guardado y protección dirty state`

## Fase 4: Seguridad, Prevención de Abusos y Casos Extremos
*(Endurece la funcionalidad principal).*

### Grupo 4.1: Mitigación de Abusos y Validaciones Perimetrales
- [ ] 4.1.1 Implementar debounce y deshabilitación inmediata en botones de envío
- [ ] 4.1.2 Configurar rate-limiting en operaciones críticas
- [ ] 4.1.3 Implementar cobertura de Casos Extremos y escenarios "¿Qué pasaría si...?" (CE-1 a CE-6)
*Punto de Revisión:* Probar clics repetidos rápidos en submit y verificar un único envío.
*Commit Parcial sugerido:* `feat(security): debounce de envíos, rate-limiting y casos extremos`

## Fase 5: QA Integral, Checklist y Documentación
*(Depende del código y pruebas concluidas).*

### Grupo 5.1: Validación de Checklist y Cierre de Subfase
- [ ] 5.1.1 Ejecutar suite completa de tests automatizados (unitarios y de integración)
- [ ] 5.1.2 Ejecutar y verificar todos los escenarios de checklist.md
- [ ] 5.1.3 Actualizar specs/roadmap.md marcando la subfase concluida
*Punto de Revisión:* Todos los checks de lint y tests en verde; checklist.md marcado.
*Commit Parcial sugerido:* `test(qa): validación de checklist y cierre de subfase <funcionalidad>`

---

## Bloqueos y Dependencias Externas
<!-- Si una tarea se bloquea por factores externos, regístrala aquí: -->
<!-- - [ ] BLOQUEADO: esperando <razón> - <ticket/referencia> -->
- Ninguno actualmente.
```

---

## 3. Revisión Crítica (Auditoría Interna)

Antes de entregar el `tasks.md`, realiza estas tres comprobaciones de calidad en silencio:
1. **Cobertura del Plan**: Mapea sistemáticamente contra `plan.md` y `spec.md`. Cada decisión arquitectónica (ej. *"auditoría de logs"*, *"persistencia de borradores"*) y cada criterio de aceptación DEBE corresponder a una o más tareas explícitas dentro de un grupo. Si falta algo, añádelo.
2. **Caza de Lagunas (Gaps) lógicas**: Busca vacíos evidentes que el plan omitió pero el código necesitará. ¿Hay tareas para el manejo de errores (ej. caídas de red)? ¿Se contemplan estados de carga (*skeletons/spinners*) o respuestas de éxito para el usuario? ¿Limpieza de datos fallidos o temporales?
3. **Revisión de Dependencias**: Asegúrate de que las tareas de UI no estén listadas antes que los endpoints o modelos de los que dependen.
4. **Tamaño de Grupos y Commits**: Ningún grupo debe tener más de 4 tareas y cada uno debe incluir su sugerencia de commit semántico y punto de revisión.

---

## 4. Paso a Producción

Al presentar el resultado al usuario:
- Confírmale que el documento `tasks.md` se ha generado como hoja de ruta.
- Explícale brevemente las fases y grupos lógicos que definiste.
- Recuérdale que `tasks.md` es un documento vivo: se irán marcando las casillas `[x]` a medida que se implemente con la skill de construcción por grupos, y puede actualizarse si surgen nuevos requerimientos durante el desarrollo.
