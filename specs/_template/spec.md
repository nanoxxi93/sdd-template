# [Título de la Funcionalidad / Subfase]

> **Subfase del Roadmap:** [Subfase X.Y: Nombre en `specs/roadmap.md`]
> **Regla de Alcance:** Esta especificación cubre únicamente una subfase o módulo acotado. Si el alcance crece o supera 250 líneas, debe particionarse creando nuevas subfases en el roadmap.

## Resumen
<!-- Descripción concisa de la funcionalidad desde la perspectiva del usuario final. Responde a "¿Qué hace?" en 1 o 2 oraciones. -->

## Casos de usuario
<!-- Narraciones de interacción: Como [rol], quiero [acción] para [beneficio]. Agrupar por flujos si son varios. -->
- **CU-1**: Como [rol], quiero [acción] para [beneficio].
- **CU-2**: Como [rol], quiero [acción] para [beneficio].

## Criterios de aceptación
<!-- Condiciones específicas y medibles requeridas para dar por concluida la funcionalidad. Lista de comprobación [ ] -->
- [ ] **CA-1**: [Criterio verificable 1 - flujo principal]
- [ ] **CA-2**: [Criterio verificable 2 - feedback visual / carga con Skeletons]
- [ ] **CA-3**: [Criterio verificable 3 - persistencia / protección de datos]

## Requisitos funcionales
<!-- Comportamiento detallado del sistema, flujos de datos y validaciones. Sin dictar código. -->
- **RF-1**: [Comportamiento funcional principal]
- **RF-2**: [Reglas de negocio y transformaciones de datos]
- **RF-3**: [Validaciones de campos y entradas]

## Requisitos no funcionales y Estándares de Calidad
<!-- Atributos obligatorios alineados con specs/constitution.md -->
- **RNF-Conectividad (Resiliencia de Red):** Tolerancia a pérdida de conexión; peticiones no críticas con reintentos pasivos (backoff exponencial y jitter) sin bloquear la interfaz.
- **RNF-UX (Feedback de Carga):** Carga asíncrona respaldada por Skeletons con la estructura visual del contenido esperado; spinners o barras contextuales para acciones puntuales; empty states descriptivos.
- **RNF-Formularios (Protección de Datos):** Advertencia de confirmación al intentar salir o recargar si existen cambios sin guardar (*dirty state*); persistencia de borrador temporal (*draft auto-save*) recuperable.
- **RNF-Seguridad y Abuso:** Validación estricta mediante esquemas en cliente y servicios; debounce/deshabilitación inmediata en botones de envío para evitar doble submit; rate-limiting en operaciones sensibles.
- **RNF-Dependencias:** Las librerías involucradas deben emplear versiones `latest stable` compatibles comprobadas sin peer-dependency conflicts.

## Casos extremos y Escenarios "¿Qué pasaría si...?"
<!-- Evaluación sistemática de eventos imprevistos, fallas y condiciones de estrés. -->
- **CE-1 (¿Qué pasaría si se corta la red a mitad de operación?):** Pérdida de conectividad o latencia extrema durante el flujo. El sistema no crashea, reintenta pasivamente en background o informa limpiamente con opción de reintentar sin perder el estado actual.
- **CE-2 (¿Qué pasaría si el usuario sale o recarga con datos sin guardar?):** El usuario cierra pestaña, recarga (F5) o navega hacia atrás. Se activa advertencia preventiva de formulario sucio (*dirty state*) y el borrador persiste en almacenamiento local/sesión.
- **CE-3 (¿Qué pasaría si el usuario hace clics repetitivos rápidos?):** Clics masivos o accidentales en el botón de envío. Se mitiga con debounce y deshabilitación visual inmediata, garantizando una única ejecución.
- **CE-4 (¿Qué pasaría si expira el token o sesión en pleno proceso?):** Se preserva el borrador o estado actual, se renueva el token en background o se solicita re-autenticación sin perder el trabajo del usuario.
- **CE-5 (¿Qué pasaría si el servicio externo/backend demora 30s+ o falla con 500/503?):** La interfaz muestra estado degradado amigable tras el timeout con botón para reintentar; jamás queda congelada en un spinner infinito.
- **CE-6 (¿Qué pasaría si entran datos atípicos o malformados?):** Payloads gigantes, scripts, caracteres especiales o valores numéricos extremos son rechazados limpiamente por los esquemas de validación con mensajes claros.

## Changelog de la Especificación
<!-- Registro de modificaciones y evolución de requisitos durante el desarrollo -->
- **YYYY-MM-DD**: Creación inicial de la especificación para la subfase.
