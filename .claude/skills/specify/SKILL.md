---
name: specify
description: Especifica una nueva funcionalidad siguiendo el Spec-Driven Development (SDD). Define el resumen, casos de usuario, criterios de aceptación, requisitos, pilares transversales y escenarios "¿Qué pasaría si...?", preguntando siempre antes de asumir.
---

# Especificar una funcionalidad (Spec-Driven Development)

En el desarrollo controlado por especificaciones, la especificación define **exactamente** lo que debe hacer el software y cada decisión de implementación realiza un seguimiento hacia él. 

La skill **termina cuando la spec está escrita y el usuario la ha validado**. 

**REGLA DE ORO**: Para generar una especificación, **es preferible preguntar antes de suponer**. No asumas comportamientos, UI, ni alcances sin validar con el usuario.

---

## 0. Antes de escribir: Verificación de Dimensionalidad y Roadmap

1. Lee `specs/constitution.md` para tener claras las reglas innegociables (seguridad, testing, versiones latest stable, resiliencia, UX y skeletons, protección de formularios, previsión de contingencias).
2. Lee `specs/mission.md` para alinear la funcionalidad con la visión del producto y sus principios de experiencia de usuario.
3. Lee `specs/tech-stack.md` para conocer las herramientas, arquitectura y dependencias aprobadas.
4. **Verificación de Dimensionalidad en `specs/roadmap.md`**:
   - Revisa en qué fase se encuentra la funcionalidad.
   - **Regla de 1 Spec = 1 Subfase o Módulo Acotado**: Si la funcionalidad solicitada cubre una fase amplia o abarca múltiples subsistemas/capas (ej. Modelo + API + UI + Integraciones complejas), **NO crees una spec monolítica**.
   - **Desglose Preventivo**: Actualiza `specs/roadmap.md` descomponiendo la fase en **subfases consistentes** (por módulo o por capa: Dominio/Modelos, Servicios/Red, UI/Vistas, Seguridad/QA).
   - Acota este `spec.md` **únicamente a la primera subfase atómica**, dejando las siguientes agendadas en el roadmap.
   - **Límite de tamaño**: Si la característica va a requerir más de 250 líneas para ser especificada, detente y sugiere al usuario dividirla en especificaciones más pequeñas e incrementales.

---

## 1. Lo que decide el usuario (Entrevista de Alcance y Pilares Transversales)

Pregunta todo lo que no esté claro, ofreciendo tu recomendación primero:
- **Alcance exacto**: Lo que entra en esta subfase y lo que se delega a las siguientes subfases del roadmap.
- **UI/UX y flujos de navegación**: Pantallas, componentes con Skeletons estructurales y empty states descriptivos.
- **Formularios (si aplica)**: Advertencia ante salida con cambios sin guardar (*dirty state*) y auto-guardado de borrador temporal.
- **Resiliencia de Red**: Comportamiento ante caída de conexión, caché local y reintentos pasivos en background (backoff con jitter).
- **Seguridad y Abuso**: Validación de esquemas, debounce en botones para evitar doble clic y límites de tasa (*rate-limiting*).
- **Indagación "¿Qué pasaría si...?":** ¿Qué ocurre si la red se corta a mitad del envío? ¿Si el usuario recarga la página o pulsa atrás? ¿Si el servicio tarda más de 30s o falla con 500? ¿Si el token expira?
- **Dependencias**: Si introduce paquetes nuevos, verificar que se utilicen versiones `latest stable` compatibles sin romper librerías del proyecto.

---

## 2. Reglas de redacción de la especificación

Al redactar la especificación, aplica estrictamente estas reglas:
- **Específico y medible**: Reemplaza términos imprecisos por valores precisos (ej. *"rápido"* por *"inferior a 200ms"*, *"varios"* por un límite exacto).
- **Vocabulario consistente**: Define los términos una vez y reutilízalos a lo largo del documento. No uses sinónimos para el mismo concepto (ej. si usas *"boletas"*, no cambies a *"recibos"* después).
- **El Qué, no el Cómo**: Las especificaciones definen requisitos, no implementaciones. Indica lo que debe hacer el sistema, sus flujos y validaciones, no cómo codificarlo (las decisiones de código pertenecen al `plan.md`).
- **Inclusión obligatoria de Pilares Transversales**: Ninguna spec de interfaz o servicio puede omitir el comportamiento ante desconexión, carga asíncrona, seguridad de formularios o doble clic.

---

## 3. La carpeta y el archivo

Crea la carpeta `specs/AAAA-MM-DD-nombre-subfase/` con la fecha en que empieza el trabajo y un nombre descriptivo en kebab-case. 
Allí escribirás el archivo principal de la especificación: `spec.md` (y su respectivo `plan.md` técnico posterior).

---

## 4. Estructura de `spec.md`

El archivo de especificación DEBE contener exactamente estas secciones, en este orden:

```markdown
# <Título de la funcionalidad / Subfase>

> **Subfase del Roadmap:** [Subfase X.Y: Nombre en specs/roadmap.md]

## Resumen
<Descripción concisa de la aplicación o nueva característica desde una perspectiva del usuario final. Responde a "¿Qué hace esta característica?" en una o dos oraciones.>

## Casos de usuario
<Breves narraciones sobre cómo interactúan los usuarios con la característica. Capturan la intención y el valor en lugar de la implementación técnica. (Como [rol], quiero [acción] para [beneficio]).>
- **CU-1**: Como [rol], quiero [acción] para [beneficio].

## Criterios de aceptación
<Condiciones específicas y medibles que deben ser verdaderas para que la característica se considere completa. Forman una lista de comprobación [ ] para comprobar la implementación.>
- [ ] **CA-1**: [Criterio verificable 1]
- [ ] **CA-2**: [Criterio verificable 2]

## Requisitos funcionales
<Descripciones detalladas del comportamiento del sistema. Indica QUÉ debe hacer el sistema, sus flujos y validaciones, sin dictar la implementación del código.>
- **RF-1**: [Requisito funcional detallado]

## Requisitos no funcionales y Estándares de Calidad
<Atributos de calidad, como el rendimiento, la seguridad, la resiliencia y el cumplimiento. Estos requisitos deben hacer referencia directa a las reglas de specs/constitution.md.>
- **RNF-Conectividad:** Tolerancia a pérdida de conexión y reintentos pasivos con backoff exponencial sin bloquear la interfaz.
- **RNF-UX:** Cargas asíncronas con Skeletons estructurales; feedback contextual y empty states.
- **RNF-Formularios:** Detección de dirty state con advertencia al salir y persistencia de borradores.
- **RNF-Seguridad:** Validación estricta con esquemas, debounce contra doble submit y rate-limiting.
- **RNF-Dependencias:** Versiones latest stable compatibles comprobadas.

## Casos extremos y Escenarios "¿Qué pasaría si...?"
<Escenarios inusuales, condiciones de error y comportamientos de límite (ej. pérdida de red a mitad del proceso, inputs maliciosos, abandono de usuario, timeouts largos). La documentación explícita de casos perimetrales impide hacer suposiciones.>
- **CE-1 (¿Qué pasaría si se corta la red?):** Comportamiento ante caída de conexión durante la operación.
- **CE-2 (¿Qué pasaría si se abandona el formulario?):** Recarga o salida con datos no guardados.
- **CE-3 (¿Qué pasaría si hay clics masivos?):** Clics repetitivos rápidos mitigados por debounce.
- **CE-4 (¿Qué pasaría si expira el token?):** Preservación de estado y renovación limpia.
- **CE-5 (¿Qué pasaría si el backend tarda 30s o devuelve 500?):** Estado degradado amigable y reintento.
- **CE-6 (¿Qué pasaría si entran datos atípicos?):** Payloads gigantes o malformados rechazados limpiamente.

## Changelog de la Especificación
<Registro de modificaciones y evolución de requisitos durante el desarrollo>
- **YYYY-MM-DD**: Creación inicial de la especificación.
```

*(Nota: Los archivos técnicos subsecuentes como `plan.md`, `tasks.md` y `checklist.md` serán generados posteriormente por sus respectivas skills. `specify` solo debe enfocarse en generar un `spec.md` perfecto).*

---

## 5. Actualizar la hoja de ruta

En `specs/roadmap.md`, vincula la funcionalidad a la sección «En curso»:
`- [Subfase X.Y: <Título>](AAAA-MM-DD-nombre-subfase/) — <una frase con lo que entrega>.`

---

## 6. Revisión Final

Antes de dar por terminada la skill:
1. **Verificación contra principios**: Comprueba exhaustivamente que la especificación recién escrita no entra en conflicto con la constitución (`constitution.md`) ni los principios del proyecto (`mission.md`).
2. Al presentar el resultado al usuario, muéstrale:
   - El enlace a la especificación generada (`spec.md`).
   - Las decisiones sobre los pilares de resiliencia, skeletons, formularios y seguridad.
   - Lo que quedó definido en los Casos Extremos y escenarios "¿Qué pasaría si...?".
   - Si se desglosó el roadmap en subfases, muéstrale cómo quedó la estructura.
   - Pregúntale explícitamente si está conforme con la especificación para dar por concluida la tarea y continuar con la skill `clarify`.
