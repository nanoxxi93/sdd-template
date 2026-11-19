---
name: specify
description: Especifica una nueva funcionalidad siguiendo el Spec-Driven Development (SDD). Define el resumen, casos de usuario, criterios de aceptación, requisitos, pilares transversales y escenarios "¿Qué pasaría si...?", preguntando siempre antes de asumir.
---

# Especificar una funcionalidad (Spec-Driven Development)

En el desarrollo controlado por especificaciones, la especificación define **exactamente** lo que debe hacer el software y cada decisión de implementación realiza un seguimiento hacia él. 

La skill **termina cuando la spec está escrita y el usuario la ha validado**. 

**REGLA DE ORO**: Para generar una especificación, **es preferible preguntar antes de suponer**. No asumas comportamientos, UI, ni alcances sin validar con el usuario.

## 0. Antes de escribir: Verificación de Dimensionalidad y Roadmap

1. Lee `specs/constitution.md` para tener claras las reglas innegociables (seguridad, testing, versiones latest stable, resiliencia, UX y skeletons, protección de formularios, previsión de contingencias).
2. Lee `specs/mission.md` para alinear la funcionalidad con la visión del producto y sus principios de experiencia de usuario.
3. Lee `specs/tech-stack.md` para conocer las herramientas, arquitectura y dependencias aprobadas.
4. **Verificación de Dimensionalidad en `specs/roadmap.md`**:
   - Revisa en qué fase se encuentra la funcionalidad.
   - **Regla de 1 Spec = 1 Subfase o Módulo Acotado**: Si la funcionalidad solicitada cubre una fase amplia o abarca múltiples subsistemas/capas (ej. Modelo + API + UI + Integraciones complejas), **NO crees una spec monolítica**.
   - **Desglose Preventivo**: Actualiza `specs/roadmap.md` descomponiendo la fase en **subfases consistentes** (por módulo o por capa: Dominio/Modelos, Servicios/Red, UI/Vistas, Seguridad/QA).
   - Acota este `spec.md` **únicamente a la primera subfase atómica**, dejando las siguientes agendadas en el roadmap.
   - **Límite de tamaño**: Una especificación no debe superar ~250 líneas. Si proyecta más, fragmenta de inmediato.

## 1. Lo que decide el usuario (Entrevista de Alcance y Pilares Transversales)

Pregunta todo lo que no esté claro, ofreciendo tu recomendación primero:
- **Alcance exacto**: Lo que entra en esta subfase y lo que se delega a las siguientes subfases del roadmap.
- **Flujo y UI/UX**: Navegación, pantallas, Skeletons de carga estructurales y empty states descriptivos.
- **Formularios (si aplica)**: Advertencia ante salida con cambios sin guardar (*dirty state*) y auto-guardado de borrador temporal.
- **Resiliencia de Red**: Comportamiento ante caída de conexión, caché local y reintentos pasivos en background (backoff con jitter).
- **Seguridad y Abuso**: Validación de esquemas, debounce en botones para evitar doble clic y límites de tasa (*rate-limiting*).
- **Indagación "¿Qué pasaría si...?":** ¿Qué ocurre si la red se corta a mitad del envío? ¿Si el usuario recarga la página o pulsa atrás? ¿Si el servicio tarda más de 30s o falla con 500?
- **Dependencias**: Si introduce paquetes nuevos, verificar que se utilicen versiones `latest stable` compatibles sin romper librerías del proyecto.

## 2. Reglas de redacción de la especificación

Al redactar la especificación, aplica estrictamente estas reglas:
- **Específico y medible**: Reemplaza términos imprecisos por valores precisos (ej. "rápido" por "< 200ms", "varios" por un límite exacto).
- **Vocabulario consistente**: Define los términos una vez y reutilízalos a lo largo del documento. No uses sinónimos para el mismo concepto.
- **El Qué, no el Cómo**: Las especificaciones definen requisitos, no implementaciones. Indica lo que debe hacer el sistema, no cómo codificarlo (las decisiones de código pertenecen al `plan.md`).
- **Inclusión obligatoria de Pilares Transversales**: Ninguna spec de interfaz o servicio puede omitir el comportamiento ante desconexión, carga asíncrona, seguridad de formularios o doble clic.

## 3. La carpeta y el archivo

Crea la carpeta `specs/AAAA-MM-DD-nombre-subfase/` con la fecha en que empieza el trabajo y un nombre descriptivo en kebab-case. 
Allí escribirás el archivo principal de la especificación: `spec.md`.

## 4. Estructura de `spec.md`

El archivo de especificación DEBE seguir la plantilla de `specs/_template/spec.md`:

```markdown
# <Título de la Funcionalidad / Subfase>

> **Subfase del Roadmap:** [Subfase X.Y: Nombre en specs/roadmap.md]

## Resumen
<Descripción concisa desde la perspectiva del usuario final. Responde a "¿Qué hace?" en una o dos oraciones.>

## Casos de usuario
- **CU-1**: Como [rol], quiero [acción] para [beneficio].

## Criterios de aceptación
- [ ] **CA-1**: [Criterio verificable 1]
- [ ] **CA-2**: [Criterio verificable 2]

## Requisitos funcionales
- **RF-1**: [Requisito funcional detallado]

## Requisitos no funcionales y Estándares de Calidad
- **RNF-Conectividad:** Tolerancia a pérdida de conexión y reintentos pasivos con backoff exponencial sin bloquear la interfaz.
- **RNF-UX:** Cargas asíncronas con Skeletons estructurales; feedback contextual y empty states.
- **RNF-Formularios:** Detección de dirty state con advertencia al salir y persistencia de borradores.
- **RNF-Seguridad:** Validación estricta con esquemas, debounce contra doble submit y rate-limiting.
- **RNF-Dependencias:** Versiones latest stable compatibles comprobadas.

## Casos extremos y Escenarios "¿Qué pasaría si...?"
- **CE-1 (¿Qué pasaría si se corta la red?):** Comportamiento ante caída de conexión durante la operación.
- **CE-2 (¿Qué pasaría si se abandona el formulario?):** Recarga o salida con datos no guardados.
- **CE-3 (¿Qué pasaría si hay clics masivos?):** Clics repetitivos rápidos mitigados por debounce.
- **CE-4 (¿Qué pasaría si expira el token?):** Preservación de estado y renovación limpia.
- **CE-5 (¿Qué pasaría si el backend tarda 30s o devuelve 500?):** Estado degradado amigable y reintento.
- **CE-6 (¿Qué pasaría si entran datos atípicos?):** Payloads gigantes o malformados rechazados limpiamente.

## Changelog de la Especificación
- **YYYY-MM-DD**: Creación inicial de la especificación.
```

## 5. Actualizar la hoja de ruta

En `specs/roadmap.md`, vincula la funcionalidad a la sección «En curso»:
`- [Subfase X.Y: <Título>](AAAA-MM-DD-nombre-subfase/) — <una frase con lo que entrega>.`

## 6. Revisión Final

Antes de dar por terminada la skill:
1. **Verificación contra principios**: Comprueba exhaustivamente que la especificación no entra en conflicto con `constitution.md` ni `mission.md`.
2. Al presentar el resultado al usuario, muéstrale:
   - El enlace a `spec.md`.
   - Las decisiones sobre resiliencia, skeletons, formularios y seguridad.
   - Si se desglosó el roadmap en subfases, muéstrale cómo quedó la estructura.
   - Pregúntale explícitamente si aprueba la especificación para proceder a la skill `clarify`.
