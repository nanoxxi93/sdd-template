# Lista de Tareas: [Nombre de la Funcionalidad / Subfase]

> **Organización por Grupos de Revisión y Commits Parciales:**
> Las tareas están agrupadas en bloques cohesivos pequeños (2 a 4 tareas por grupo). Al finalizar cada grupo, se realiza una pausa para revisión del código generado, ejecución de tests y commit parcial independiente antes de pasar al siguiente bloque.

## Fase 1: Setup, Modelos y Contratos de Datos

### Grupo 1.1: Scaffolding, Dependencias y Esquemas Base
- [ ] 1.1.1 Auditar e instalar dependencias requeridas en sus versiones `latest stable` compatibles (sin romper librerías existentes)
- [ ] 1.1.2 Definir modelos de datos y esquemas de validación estricta (Zod/Pydantic/esquemas tipados)
- [ ] 1.1.3 Escribir tests unitarios para validación de esquemas y transformaciones
*Punto de Revisión:* Verificar que las versiones instaladas no tengan vulnerabilidades ni rompan el build. Tests de modelos en verde.
*Commit Parcial sugerido:* `feat(core): setup de dependencias latest y esquemas base para [funcionalidad]`

---

## Fase 2: Servicios, Conectividad y Resiliencia

### Grupo 2.1: Lógica de Servicios y Reintentos Pasivos
- [ ] 2.1.1 Implementar cliente de servicio/red con tolerancia a fallos y reintentos pasivos en background (exponential backoff + jitter)
- [ ] 2.1.2 Implementar manejo de estado de desconexión / offline fallback y persistencia local
- [ ] 2.1.3 Escribir pruebas unitarias simulando cortes de red, timeouts y recuperación pasiva
*Punto de Revisión:* Validar que las llamadas fallidas transitorias no crashean y reintentan limpiamente sin bloquear el hilo.
*Commit Parcial sugerido:* `feat(services): cliente de servicio con reintentos pasivos y tolerancia offline`

---

## Fase 3: Interfaz de Usuario y Experiencia (UX)

### Grupo 3.1: Vistas Base, Estados de Carga y Skeletons
- [ ] 3.1.1 Construir estructura de componentes de vista y navegación
- [ ] 3.1.2 Implementar componentes Skeleton estructurales que coincidan con la forma del contenido para cargas asíncronas
- [ ] 3.1.3 Implementar estados vacíos (*empty states*) descriptivos y feedback de error contextual
*Punto de Revisión:* Inspeccionar visualmente que la transición de Skeleton a contenido real sea fluida y sin saltos de layout (CLS).
*Commit Parcial sugerido:* `feat(ui): componentes de vista con skeletons estructurales y empty states`

### Grupo 3.2: Formularios Protegidos y Prevención de Pérdida de Datos
- [ ] 3.2.1 Construir campos de formulario con validación visual en tiempo real vinculada a los esquemas
- [ ] 3.2.2 Implementar persistencia de borrador temporal (*draft auto-save*) en almacenamiento local/sesión
- [ ] 3.2.3 Implementar guardia de navegación / confirmación de salida ante formulario con cambios sin guardar (*dirty state*)
*Punto de Revisión:* Probar recargar o salir del formulario con datos a medio llenar y confirmar que no se pierden y aparece la advertencia.
*Commit Parcial sugerido:* `feat(ui): formulario con auto-guardado de borradores y protección contra salida`

---

## Fase 4: Seguridad, Prevención de Abusos y Casos Extremos

### Grupo 4.1: Mitigación de Abusos y Validaciones Perimetrales
- [ ] 4.1.1 Implementar debounce y deshabilitación inmediata en botones de envío para evitar doble clic
- [ ] 4.1.2 Configurar rate-limiting / control de frecuencia en llamadas y acciones críticas
- [ ] 4.1.3 Implementar cobertura de Casos Extremos (CE-1 a CE-4: entradas malformadas, cortes de red súbitos)
*Punto de Revisión:* Probar clics repetidos rápidos en submit y confirmar que solo se emite una solicitud. Validar rechazo de payloads inválidos.
*Commit Parcial sugerido:* `feat(security): debounce de envíos, rate-limiting y manejo de casos extremos`

---

## Fase 5: QA Integral, Checklist y Documentación

### Grupo 5.1: Validación de Checklist y Cierre de Subfase
- [ ] 5.1.1 Ejecutar suite completa de tests automatizados (unitarios y de integración)
- [ ] 5.1.2 Ejecutar y verificar todos los escenarios de `checklist.md` (QA manual de desconexión, skeletons y formularios)
- [ ] 5.1.3 Actualizar `specs/roadmap.md` marcando la subfase concluida
*Punto de Revisión:* Todos los checks de lint, typecheck y tests en verde; checklist.md marcado íntegramente.
*Commit Parcial sugerido:* `test(qa): validación de checklist de QA y cierre de subfase [funcionalidad]`

---

## Bloqueos y Dependencias Externas
<!-- Si una tarea se bloquea por factores externos, regístrala aquí: -->
<!-- - [ ] BLOQUEADO: esperando <razón> - <ticket/referencia> -->
- Ninguno actualmente.
