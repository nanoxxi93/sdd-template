---
name: clarify
description: Audita y refina exhaustivamente una especificación (spec.md) en una sola pasada de 360°, evaluando ambigüedades, suposiciones, lagunas y escenarios "¿Qué pasaría si...?", entregando un reporte explicativo y fundamentado para la toma de decisiones, evitando ciclos interminables de preguntas.
---

# Clarificar y Refinar una Especificación (Refinamiento Exhaustivo SDD)

Esta skill se usa en el desarrollo controlado por especificaciones (SDD) para auditar y refinar una especificación (`spec.md`) **antes** de que comience el diseño técnico (`plan.md`) y la implementación. El objetivo es detectar problemas de forma temprana, actuando como un analista de producto/sistemas experimentado.

**OBJETIVOS CLAVE:**
1. **CERO RONDAS INFINITAS (Auditoría Exhaustiva en 1 Sola Pasada):** Escaneo integral de todas las lagunas y ambigüedades de una sola vez.
2. **REPORTE EXPLICATIVO Y FUNDAMENTADO:** Cada hallazgo explica el *por qué* importa, los riesgos, las opciones consideradas y el motivo de la recomendación para que el usuario tome decisiones informadas con criterio.
3. **EVALUACIÓN SISTEMÁTICA DEL "¿QUÉ PASARÍA SÍ...?":** Detección proactiva de escenarios de contingencia, estrés y fallos antes de que lleguen a código.

---

## 0. Paso Previo: Control de Dimensionalidad y Desglose de Roadmap

La causa principal de especificaciones interminables o lagunas infinitas es el tamaño excesivo de la spec.
Antes de auditar detalles:
1. Evalúa el alcance de `spec.md`:
   - ¿Abarca múltiples subsistemas o capas a la vez (ej. Modelos + Servicios + Vistas + Integraciones)?
   - ¿Supera o superará las ~250 líneas al añadir casos extremos y contingencias?
2. **Si la spec es demasiado amplia:**
   - **Detente y propón de inmediato el Desglose de Spec y Roadmap**:
   - Sugiere dividir la fase en `specs/roadmap.md` en **Subfases consistentes** (por módulo o por capa: ej. Subfase 1.1: Núcleo/Dominio, Subfase 1.2: Servicios/Red, Subfase 1.3: UI/Skeletons, Subfase 1.4: Seguridad/Abusos).
   - Con la aprobación del usuario, actualiza `specs/roadmap.md` con las nuevas subfases y acota la spec actual **estrictamente a la primera subfase atómica**, delegando el resto.
   - Si la spec ya está correctamente acotada a una subfase, procede directamente a la auditoría.

---

## 1. Análisis Exhaustivo de la Especificación

Al invocar esta skill, debes leer la especificación objetivo y evaluarla rigurosamente contra los criterios clásicos del analista y la matriz de contingencias:

### Criterios Clásicos de Análisis
- **Ambigüedades**: Busca palabras vagas o imprecisas (ej. *"rápido"*, *"a veces"*, *"muchos"*, *"adecuado"*, *"seguro"*) y señala que necesitan ser reemplazadas por valores exactos y medibles.
- **Lagunas (Gaps) y Detalles Faltantes**: Identifica estados no manejados. Por ejemplo: estados vacíos (*empty states*), estados de carga (*skeletons/spinners*), paginación, límites de caracteres, respuestas de error específicas.
- **Suposiciones**: Detecta decisiones implícitas que no están escritas pero que el desarrollador tendría que tomar por su cuenta (ej. *"el sistema envía un email"*... ¿con qué plantilla?, ¿desde qué dirección?).
- **Incoherencias de Terminología**: Verifica que los términos se usen de manera consistente a lo largo de todo el documento sin sinónimos confusos.
- **Alineación Estratégica**: Asegúrate de que no haya conflictos ocultos con las reglas de `specs/constitution.md` o la visión de `specs/mission.md`.

### Matriz de Pilares Transversales 360°
1. **Contratos y Datos:** Tipos exactos, nulos/opcionales, límites de longitud (min/max), rangos numéricos y formatos.
2. **Estados de UI y Skeletons:** Skeletons estructurales para cargas asíncronas, empty states descriptivos y feedback contextual.
3. **Formularios y Pérdida de Datos:** Advertencia ante salida con cambios (*dirty state*) y persistencia de borradores (*draft auto-save*).
4. **Red y Resiliencia:** Tolerancia a desconexión, modo offline o caché local, reintentos pasivos en background (backoff con jitter).
5. **Seguridad y Control de Abusos:** Debounce en botones de envío (contra doble clic), rate-limiting y validación estricta de esquemas.
6. **Dependencias:** Verificación de versiones `latest stable` compatibles evitando paquetes obsoletos.

### Evaluación de Escenarios "¿Qué pasaría sí...?" (What-If Stress Testing)
Formula y audita rigurosamente las siguientes preguntas de contingencia:
- **¿Qué pasaría si la red se corta o degrada justo durante la operación?** (¿Queda la transacción a medias? ¿Se duplica? ¿Se informa al usuario con opción de reintentar?).
- **¿Qué pasaría si el usuario interrumpe abruptamente?** (¿Presiona 'Atrás', recarga F5 o cierra la pestaña con un formulario o proceso en curso?).
- **¿Qué pasaría si expira la sesión o token de autenticación durante el flujo?** (¿Se pierde el trabajo hecho o se renueva en background / se guarda el borrador antes de redirigir a login?).
- **¿Qué pasaría si hay concurrencia o doble clic rápido?** (¿Dos solicitudes simultáneas pueden desincronizar el estado o crear registros duplicados? ¿Hay riesgo de *race condition*?).
- **¿Qué pasaría si el backend o servicio de terceros tarda 30s+ o responde con error 500/503?** (¿La UI queda congelada con un spinner infinito o degrada limpiamente informando con honestidad?).
- **¿Qué pasaría si el almacenamiento local falla o está deshabilitado?** (¿El modo incógnito o cuota excedida de localStorage crashea la app o se usa un fallback en memoria?).
- **¿Qué pasaría si ingresan datos atípicos, malformados o extremos?** (Strings gigantes, caracteres especiales, números negativos en cantidades, fechas imposibles).

---

## 2. Presentación del Reporte Explicativo (Fundamentado para Decidir)

No presentes una lista escueta ni hagas preguntas abiertas a cuentagotas. Como analista experimentado, estructura el reporte de forma **didáctica, explicativa y fundamentada**, agrupado por hallazgos:

```markdown
### 📋 Hallazgo [ID]: [Título descriptivo]
- **Eje / Tipo:** [Ambigüedad / Laguna / Suposición / ¿Qué pasaría si...? / Pilar transversal]
- **Qué se detectó (Hallazgo):** [Descripción clara del vacío o ambigüedad en spec.md]
- **Por qué importa / Riesgo e Impacto:** [Explicación del riesgo real si no se define: pérdida de datos, cobros duplicados, congelamiento de UI, confusión del usuario, etc.]
- **Alternativas consideradas:**
  - *Opción A:* [Descripción de alternativa 1 y sus pros/contras]
  - *Opción B:* [Descripción de alternativa 2 y sus pros/contras]
- **Recomendación fundamentada:** [Por qué el analista recomienda la opción seleccionada (balance entre valor, UX y complejidad técnica)]
- **Texto propuesto para `spec.md`:**
  > [Redacción exacta lista para insertar en Criterios de Aceptación, RNF o Casos Extremos]
```

*(Acompaña opcionalmente los hallazgos con una tabla resumen que sintetice ID, Eje, Recomendación y Sección afectada).*

---

## 3. Opciones de Decisión para el Usuario (Zero-Friction)

Al final del reporte explicativo, presenta claramente estas dos opciones de cierre:
- **Opción A (Aprobación Rápida en Bloque - Recomendada):** Si tras leer las justificaciones estás de acuerdo con el criterio del analista, responde simplemente: *"Acepto todas las recomendaciones"*. Todas las soluciones se aplicarán automáticamente a `spec.md`.
- **Opción B (Decisión Selectiva / Ajustes):** Si prefieres una alternativa distinta para algún punto concreto, solo menciona el ID y tu elección (ej. *"Para H-02 prefiero la Opción A en vez de la B, el resto aprobado"*).

---

## 4. Actualización y Blindaje de `spec.md`

Una vez que el usuario responda y aclare las dudas (generalmente en un único mensaje de resolución):
1. **Reescribe y actualiza directamente el archivo `spec.md`**:
   - Reemplaza términos imprecisos por valores exactos y medibles.
   - Inserta las soluciones acordadas en los **Criterios de Aceptación** (`CA-X`).
   - Completa los **Requisitos No Funcionales** (Conectividad, Skeletons, Formularios, Seguridad).
   - Traslada los escenarios complejos y contingencias a la sección de **Casos extremos y Escenarios "¿Qué pasaría si...?"** (`CE-X`).
2. **Actualiza el Changelog**: Añade una entrada en `## Changelog de la Especificación` resumiendo el refinamiento explicativo.
3. **Cierre de la Skill**: Notifica al usuario que la especificación ha sido refinada, blindada contra lagunas arquitectónicas y está lista para el diseño técnico (`plan.md`) y la construcción sin requerir más rondas.
