# Plan de Implementación Técnico: [Título de la Funcionalidad / Subfase]

## Información general sobre la arquitectura
<!-- Vista general del flujo de componentes, datos y control entre capas sin entrar en código granular. -->
- **Flujo de datos y capas:** [Descripción de la interacción entre Dominio, Servicios y UI]
- **Estrategia de Resiliencia y Red:** [Mecanismo de reintentos pasivos con backoff exponencial, detección de desconexión y caché/offline fallback]
- **Estrategia de UI y Feedback de Carga:** [Uso de Skeletons estructurales, spinners contextuales y empty states]
- **Estrategia de Protección de Formularios:** [Detección de cambios sin guardar (dirty state) y persistencia de borradores en almacenamiento local/sesión]
- **Estrategia de Seguridad y Mitigación de Abusos:** [Validación con esquemas en tiempo de ejecución, debounce en botones de acción y rate-limiting]
- **Estrategia ante Escenarios "¿Qué pasaría si...?":** [Mitigación arquitectónica para timeouts largos de backend (500/503), expiración de sesión/token en vuelo, concurrencia/race conditions y fallback ante almacenamiento local no disponible]

## Pila tecnológica y auditoría de dependencias
<!-- Justificación técnica explícita y coherencia con specs/tech-stack.md -->

### Auditoría de Versiones (Latest Stable Coexistentes)
<!-- Regla: Las librerías propuestas deben auditarse contra la versión estable más reciente sin romper dependencias mutuas -->
| Librería / Paquete | Versión Verificada (`latest stable`) | Justificación | Compatibilidad con el Stack |
|---|---|---|---|
| `[paquete-1]` | `x.y.z` | [Para qué se usa] | Compatible con [runtime/otras librerías] |
| `[paquete-2]` | `x.y.z` | [Para qué se usa] | Sin conflictos de peer-dependencies |

### Decisiones de Diseño Clave
- **[Decisión 1]**: [Descripción]
  - **Por qué:** [Razón técnica detrás de la elección]
  - **Alternativas consideradas:** [Qué se evaluó y por qué se descartó]
  - **RNF cubiertos:** [Cómo atiende rendimiento, resiliencia, seguridad, etc.]

## Secuencia de implementación (Organizada por Lotes / Grupos Lógicos)
<!-- Progresión lógica en grupos pequeños para permitir revisión incremental y commits parciales -->
1. **Lote 1 (Setup y Modelos):** Tipos, esquemas de validación y modelos de datos.
2. **Lote 2 (Servicios y Resiliencia):** Lógica de negocio, cliente HTTP con reintentos pasivos y persistencia.
3. **Lote 3 (UI, Skeletons y Formularios):** Componentes visuales, Skeletons de carga, persistencia de borradores y debounce.
4. **Lote 4 (Seguridad, QA y Casos Extremos):** Pruebas automatizadas, manejo de desconexión, mitigación del "¿Qué pasaría si...?" y validaciones perimetrales.

## Comprobación de la Constitución
<!-- Punto de control explícito contra specs/constitution.md. Si algo entra en conflicto, detén el diseño. -->
- [ ] **Dependencias Vigentes:** Paquetes auditados en su versión `latest stable` compatible sin romper librerías del proyecto.
- [ ] **Resiliencia de Red:** Tolerancia a desconexión y reintentos pasivos con backoff sin bloquear la interfaz.
- [ ] **UX y Feedback de Carga:** Skeletons estructurales definidos para cargas asíncronas y estados vacíos claros.
- [ ] **Protección de Formularios:** Guardado temporal de borradores y confirmación ante salida con formulario sucio.
- [ ] **Seguridad y Abuso:** Validación de esquemas estricta, debounce en acciones y rate-limiting en operaciones críticas.
- [ ] **Mitigación "¿Qué pasaría si...?":** Escenarios de contingencia (timeout, sesión expirada, fallos 500) abordados.
- [ ] **Codificación y TDD:** Estrategia de pruebas previa al código y desglose en tareas comiteables por partes.

## Suposiciones y preguntas abiertas
<!-- Suposiciones sobre infraestructura, librerías, latencia o integraciones externas. -->
- **Suposición 1**: [Detalle de la suposición]
- **Pregunta abierta 1**: [Punto a validar si surgen bloqueos]
