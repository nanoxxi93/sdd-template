# Constitución del Proyecto

Este archivo captura los principios, restricciones y estándares no negociables que rigen el proyecto **{{PROJECT_NAME}}**. Sirve como barandilla para el desarrollo asistido por IA (Spec-Driven Development) y es la única fuente de la verdad para estas reglas. Las decisiones técnicas puntuales viven en `tech-stack.md` y la motivación en `mission.md`.

## Estándares Tecnológicos y Dependencias
- **Plataforma Única:** {{DEFINIR_PLATAFORMA}}
- **Lenguaje y UI:** {{DEFINIR_LENGUAJE_Y_UI}}
- **Arquitectura:** {{DEFINIR_ARQUITECTURA}}
- **Sin Backend Propio / Backend Serverless:** {{DEFINIR_REGLA_BACKEND}}
- **Dependencias y Scaffolding Vigentes (Latest Stable Compatibles):** Toda propuesta de paquetes o inicialización de scaffolding debe auditar y fijar versiones estables recientes (`latest stable` o LTS activo del ecosistema). Queda terminantemente prohibido utilizar paquetes deprecados o versiones obsoletas por inercia del modelo de lenguaje sin antes verificar su compatibilidad cruzada (sin romper dependencias del proyecto).

## Resiliencia, Conectividad y Previsión del "¿Qué pasaría si...?"
- **Tolerancia a Desconexiones:** El sistema debe operar de forma resiliente ante pérdida súbita de conectividad. Si es una aplicación con almacenamiento local o cliente rico, debe permitir operación offline o degradación elegante, informando con honestidad el estado de red y sincronizando automáticamente al recuperar la conexión sin perder estado.
- **Fluidez y Reintentos Pasivos:** Las peticiones a red no deben congelar la interfaz ni interrumpir el flujo del usuario con diálogos modales molestos para errores transitorios. Se implementarán reintentos pasivos en segundo plano con retroceso exponencial (*exponential backoff* y *jitter*), alertando al usuario únicamente cuando el fallo sea definitivo y requiera una acción consciente.
- **Previsión Sistemática del "¿Qué pasaría si...?":** Toda funcionalidad debe someterse a evaluación preventiva de contingencias antes de codificar: interrupciones súbitas del usuario (atrás/recarga), timeouts largos o errores 500 del servidor, expiración de tokens durante un flujo, concurrencia/race conditions y almacenamiento local no disponible.

## Principios de Experiencia de Usuario (UX) y Frontend
- **Nunca Estorbar:** {{DEFINIR_REGLA_UX}}
- **Fluidez y Percepción de Rendimiento:** {{DEFINIR_REGLA_PERFORMANCE}}
- **Indicadores de Carga y Skeletons:** Prohibidas las pantallas en blanco, pantallas congeladas o bloqueos de UI sin retroalimentación. En cargas asíncronas de vistas o listas se deben usar *Skeletons* estructurales que reflejen la forma del contenido entrante. Las acciones puntuales deben usar indicadores de progreso contextuales (spinners o barras sutiles) y estados vacíos (*empty states*) descriptivos.
- **Protección contra Pérdida de Datos en Formularios:** Todo formulario con entrada manual del usuario debe incorporar protección activa:
  1. Detección de formulario sucio (*dirty state*) con advertencia de confirmación antes de navegar fuera o recargar la página si hay cambios sin guardar.
  2. Persistencia temporal de borrador (*draft auto-save* en almacenamiento local/sesión) para restaurar el contenido en caso de recarga accidental, caída de red o cierre fortuito.
- **Fallar en Silencio y Honestidad:** {{DEFINIR_MANEJO_ERRORES}}

## Seguridad y Control de Abusos
- **Validación Estricta de Entradas:** Todas las entradas deben validarse y sanitizarse mediante esquemas estrictos tanto en cliente (UX inmediata) como en servidor/servicios (integridad innegociable).
- **Protección contra Abusos y Envíos Duplicados:** Todo botón o disparador de acción asíncrona debe implementar *debounce* o deshabilitación inmediata durante el procesamiento para evitar doble clic o envíos duplicados. Los endpoints y acciones críticas deben contar con límites de tasa (*rate-limiting*) y control de concurrencia.
- **Aislamiento Seguro de Credenciales:** {{DEFINIR_ALMACENAMIENTO_CREDENCIALES}}
- **Minimización de Datos Extrema:** {{DEFINIR_REGLAS_PRIVACIDAD}}
- **Comportamiento Pasivo:** {{DEFINIR_COMPORTAMIENTO_SISTEMA}}

## Estándares de Codificación
- **Test-Driven Development (TDD):** Sin un test que falle primero, no se escribe código de producto.
- **Aislamiento del Motor/Librería Principal:** {{DEFINIR_ENCAPSULAMIENTO_CORE}}
- **Compatibilidad y Versionado:** Commits semánticos (`feat:`, `fix:`, `docs:`, `chore:`). Todo el código está en español para la documentación e inglés para variables y funciones.
- **Implementación por Lotes / Commits Parciales:** Las tareas deben ejecutarse y revisarse en grupos cohesivos y pequeños para facilitar la auditoría de código antes de integrar.

## Gobernanza y Manejo de Riesgos
- **Consentimiento de Riesgo:** {{DEFINIR_REGLAS_CONSENTIMIENTO}}
- **Control Antiveto:** {{DEFINIR_REGLAS_TELEMETRIA_O_KILLSWITCH}}
