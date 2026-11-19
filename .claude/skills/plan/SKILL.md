---
name: plan
description: Elabora el documento de diseño técnico (plan.md) que sirve de puente entre los requisitos de spec.md y la implementación. Define la arquitectura, audita versiones latest stable compatibles, diseña la resiliencia, skeletons, protección de datos y seguridad, y secuencia el desarrollo por lotes.
---

# Diseñar el Plan Técnico (plan.md)

En el Spec-Driven Development, esta skill toma los requisitos de alto nivel definidos en `spec.md` (el *qué*) y diseña la estrategia técnica de implementación (el *cómo*). 

La **separación de preocupaciones** es fundamental: la especificación debe permanecer estable definiendo los requisitos, mientras que el plan es un documento vivo que puede evolucionar a medida que se refina el enfoque técnico, la resiliencia y la auditoría de dependencias.

---

## 1. Reglas estrictas para la Planificación Técnica

Al redactar o refinar el `plan.md`, debes aplicar estos criterios rigurosamente:

- **Mapeo Sistemático**: Todo requisito (funcional, no funcional y caso extremo) de `spec.md` debe asignarse a un enfoque de implementación en el plan. Si `spec.md` pide validar el tamaño de un archivo, el plan debe describir exactamente **dónde** (frontend, middleware, backend) y **cómo** se produce esta validación.
- **Cero instrucciones vagas**: Prohibido usar frases como *"implementar manejo de errores adecuado"*. Debes empujar el detalle: ¿Qué errores pueden ocurrir? ¿Cómo se captura cada error? ¿Qué información va a los logs y qué se le muestra al usuario?
- **Auditoría de Versiones y Dependencias (Latest Stable Coexistentes):**
  - *Prohibido asumir versiones viejas de memoria:* Para cualquier paquete propuesto, consulta e investiga activamente la versión estable más reciente (`latest stable` o LTS activo) mediante comandos del gestor de paquetes (`npm view`, `pip index`, etc.).
  - *Matriz de Coexistencia:* Valida que las dependencias propuestas no rompan librerías ya instaladas ni generen conflictos de dependencias entre pares (*peer dependencies*).
- **Diseño Obligatorio de Pilares Transversales:**
  - *Resiliencia de Red y Reintentos Pasivos:* Describe la estrategia para tolerar caídas de red, timeouts, reintentos en segundo plano (exponential backoff con jitter) y degradación offline.
  - *UI y Skeletons:* Define los componentes estructurales de Skeleton para cargas asíncronas y prevención de saltos de layout (CLS).
  - *Protección de Formularios:* Modela la detección de *dirty state* y la persistencia de borradores (*draft auto-save*) en almacenamiento local o sesión.
  - *Seguridad y Control de Abusos:* Especifica los esquemas de validación, el mecanismo de *debounce* en disparadores de UI para evitar doble submit, y rate-limiting en operaciones críticas.
  - *Mitigación de Contingencias "¿Qué pasaría si...?":* Modela el comportamiento técnico ante timeouts de 30s del servidor, respuestas 500, sesión expirada en vuelo y almacenamiento local lleno.
- **Factibilidad Técnica y Restricciones**: Comprueba que la solución es técnicamente viable con la infraestructura actual. Por ejemplo, operaciones pesadas no deben bloquear el hilo principal ni agotar tiempos de espera cortos.
- **Alineación Tecnológica**: Las opciones deben usar estrictamente las herramientas y patrones ya aprobados en `specs/tech-stack.md`. Respeta los sistemas existentes.
- **Justificar el "Por qué"**: No solo documentes qué se va a hacer, sino el razonamiento. Documenta siempre las alternativas que consideraste y por qué seleccionaste una sobre las demás.
- **Explicitar Suposiciones**: Cualquier creencia sobre infraestructura, datos previos o comportamiento de terceros debe quedar por escrito de antemano.
- **Secuenciación por Lotes / Bloques Lógicos**: Organiza la progresión en bloques pequeños y cohesivos para permitir que `tasks` genere tareas comiteables y revisables por partes (evitando volcados monolíticos).

---

## 2. Estructura obligatoria de `plan.md`

Dentro de la carpeta de la funcionalidad (la misma que tiene `spec.md`), crea o actualiza `plan.md` conforme a `specs/_template/plan.md`:

```markdown
# Plan de Implementación Técnico: <Título de la Funcionalidad / Subfase>

## Información general sobre la arquitectura
Vista general de cómo interactuarán los componentes. Establece el flujo general de los datos y el control sin profundizar en detalles granulares de código.
- **Flujo de datos y capas:** [Descripción de la interacción entre Dominio, Servicios y UI]
- **Estrategia de Resiliencia y Red:** [Reintentos pasivos con backoff exponencial, detección de desconexión y caché local]
- **Estrategia de UI y Feedback de Carga:** [Skeletons estructurales, spinners contextuales y empty states]
- **Estrategia de Protección de Formularios:** [Detección de dirty state y persistencia de borradores]
- **Estrategia de Seguridad y Abuso:** [Esquemas de validación estricta, debounce de envíos y rate-limiting]
- **Estrategia ante Escenarios "¿Qué pasaría si...?":** [Mitigación ante timeouts de 30s, errores 500, sesión expirada y fallos de storage]

## Pila tecnológica y auditoría de dependencias
Documentación explícita de las opciones tecnológicas elegidas y su justificación.

### Auditoría de Versiones (Latest Stable Coexistentes)
| Librería / Paquete | Versión Verificada (`latest stable`) | Justificación | Compatibilidad con el Stack |
|---|---|---|---|
| `[paquete-1]` | `x.y.z` | [Para qué se usa] | Compatible con [runtime/librerías existentes] |

### Decisiones de Diseño Clave
- **[Decisión 1]**: [Descripción]
  - **Por qué:** Evita confusiones futuras explicando la razón técnica detrás de librerías o patrones elegidos.
  - **Alternativas consideradas:** Qué otros enfoques se evaluaron y por qué se descartaron.
  - **RNF cubiertos:** Explica cómo esta arquitectura aborda rendimiento, resiliencia, UX, seguridad, etc.

## Secuencia de implementación (Organizada por Lotes / Grupos Lógicos)
Progresión lógica de los pasos de desarrollo organizada en bloques pequeños y coherentes:
1. **Lote 1 (Setup y Modelos):** Tipos, dependencias auditadas y esquemas de validación.
2. **Lote 2 (Servicios y Resiliencia):** Lógica, cliente HTTP con reintentos pasivos y persistencia.
3. **Lote 3 (UI, Skeletons y Formularios):** Componentes visuales, Skeletons, guardado de borradores y debounce.
4. **Lote 4 (Seguridad, QA y Casos Extremos):** Tests, cobertura de CE y validaciones perimetrales.

## Comprobación de la Constitución
Punto de control explícito. Verifica sistemáticamente que la solución respeta `specs/constitution.md`. **Si la arquitectura propuesta infringe un principio, detén el diseño y busca otro enfoque.**
- [ ] **Dependencias Vigentes:** Paquetes auditados en su versión latest stable compatible.
- [ ] **Resiliencia de Red:** Tolerancia a desconexión y reintentos pasivos con backoff.
- [ ] **UX y Feedback de Carga:** Skeletons estructurales para cargas asíncronas.
- [ ] **Protección de Formularios:** Guardado de borradores y confirmación ante salida con cambios.
- [ ] **Seguridad y Abuso:** Esquemas de validación, debounce y rate-limiting.
- [ ] **Mitigación "¿Qué pasaría si...?":** Escenarios de contingencia (timeout, sesión expirada, fallos 500) abordados.
- [ ] **Codificación y TDD:** Estrategia de pruebas y tareas comiteables por partes.

## Suposiciones y preguntas abiertas
Lista de suposiciones hechas durante el diseño sobre el entorno, integraciones o componentes. Documentar esto de antemano previene desviaciones de alcance. Si una suposición falla durante el desarrollo, el plan deberá actualizarse.
- **Suposición 1**: [Detalle de la suposición]
- **Pregunta abierta 1**: [Punto a validar si surgen bloqueos]
```

---

## 3. Revisión Final

1. Una vez redactado, lee `spec.md` una última vez y verifica que ningún criterio de aceptación haya quedado "huérfano" (sin solución técnica ni asignación a un lote en el plan).
2. Presenta el plan al usuario haciendo énfasis en la **Comprobación de la Constitución**, la tabla de **versiones auditadas**, y las **Suposiciones y preguntas abiertas**.
3. Pídele que confirme el enfoque antes de proceder a la generación de tareas con `tasks`.
