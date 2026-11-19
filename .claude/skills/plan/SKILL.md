---
name: plan
description: Elabora el documento de diseño técnico (plan.md) que sirve de puente entre los requisitos de spec.md y la implementación. Define la arquitectura, audita versiones latest stable compatibles, diseña la resiliencia, skeletons, protección de datos y seguridad, y secuencia el desarrollo por lotes.
---

# Diseñar el Plan Técnico (plan.md)

En el Spec-Driven Development, esta skill toma los requisitos de alto nivel definidos en `spec.md` (el *qué*) y diseña la estrategia técnica de implementación (el *cómo*). 

La **separación de preocupaciones** es fundamental: la especificación debe permanecer estable definiendo los requisitos, mientras que el plan es un documento vivo que modela la arquitectura técnica, la resiliencia y la auditoría de dependencias.

---

## 1. Reglas estrictas para la Planificación Técnica

Al redactar o refinar el `plan.md`, debes aplicar estos criterios rigurosamente:

1. **Auditoría de Versiones y Dependencias (Latest Stable Coexistentes):**
   - **Prohibido asumir versiones viejas de memoria:** Para cualquier paquete propuesto, consulta e investiga la versión estable más reciente (`latest stable` o LTS activo).
   - **Matriz de Coexistencia:** Valida que las dependencias propuestas no rompan librerías ya instaladas ni generen conflictos de dependencias entre pares (*peer dependencies*).
2. **Diseño Obligatorio de Pilares Transversales:**
   - **Resiliencia de Red y Reintentos Pasivos:** Describe la estrategia para tolerar caídas de red, timeouts, reintentos en segundo plano (exponential backoff con jitter) y degradación offline.
   - **UI y Skeletons:** Define los componentes estructurales de Skeleton para cargas asíncronas y prevención de saltos de layout (CLS).
   - **Protección de Formularios:** Modela la detección de *dirty state* y la persistencia de borradores (*draft auto-save*) en almacenamiento local o sesión.
   - **Seguridad y Control de Abusos:** Especifica los esquemas de validación, el mecanismo de *debounce* en disparadores de UI para evitar doble submit, y rate-limiting en operaciones críticas.
3. **Secuenciación por Lotes / Bloques Lógicos:**
   - Organiza la progresión en bloques pequeños y cohesivos para permitir que `tasks` genere tareas comiteables y revisables por partes (evitando volcados monolíticos).
4. **Cero instrucciones vagas:** Prohibido usar frases como "implementar manejo de errores adecuado". Debes empujar el detalle: ¿Qué errores pueden ocurrir? ¿Cómo se captura cada error? ¿Qué información va a los logs y qué se le muestra al usuario?
5. **Comprobación de la Constitución:** Cada aspecto debe alinearse con `specs/constitution.md` y `specs/tech-stack.md`. Si algo choca, detén el diseño y busca otra alternativa.

---

## 2. Estructura obligatoria de `plan.md`

El archivo `plan.md` dentro de la carpeta de la funcionalidad debe estructurarse conforme a `specs/_template/plan.md`:

```markdown
# Plan de Implementación Técnico: <Título de la Funcionalidad / Subfase>

## Información general sobre la arquitectura
- **Flujo de datos y capas:** [Descripción de la interacción entre Dominio, Servicios y UI]
- **Estrategia de Resiliencia y Red:** [Reintentos pasivos con backoff exponencial, detección de desconexión y caché local]
- **Estrategia de UI y Feedback de Carga:** [Skeletons estructurales, spinners contextuales y empty states]
- **Estrategia de Protección de Formularios:** [Detección de dirty state y persistencia de borradores]
- **Estrategia de Seguridad y Abuso:** [Esquemas de validación estricta, debounce de envíos y rate-limiting]

## Pila tecnológica y auditoría de dependencias

### Auditoría de Versiones (Latest Stable Coexistentes)
| Librería / Paquete | Versión Verificada (`latest stable`) | Justificación | Compatibilidad con el Stack |
|---|---|---|---|
| `[paquete-1]` | `x.y.z` | [Para qué se usa] | Compatible con [runtime/librerías existentes] |

### Decisiones de Diseño Clave
- **[Decisión 1]**: [Descripción]
  - **Por qué:** [Razón técnica]
  - **Alternativas consideradas:** [Qué se evaluó y descartó]
  - **RNF cubiertos:** [Resiliencia, UX, Seguridad, etc.]

## Secuencia de implementación (Organizada por Lotes / Grupos Lógicos)
1. **Lote 1 (Setup y Modelos):** Tipos, dependencias auditadas y esquemas de validación.
2. **Lote 2 (Servicios y Resiliencia):** Lógica, cliente HTTP con reintentos pasivos y persistencia.
3. **Lote 3 (UI, Skeletons y Formularios):** Componentes visuales, Skeletons, guardado de borradores y debounce.
4. **Lote 4 (Seguridad, QA y Casos Extremos):** Tests, cobertura de CE y validaciones perimetrales.

## Comprobación de la Constitución
- [ ] **Dependencias Vigentes:** Paquetes auditados en su versión latest stable compatible.
- [ ] **Resiliencia de Red:** Tolerancia a desconexión y reintentos pasivos con backoff.
- [ ] **UX y Feedback de Carga:** Skeletons estructurales para cargas asíncronas.
- [ ] **Protección de Formularios:** Guardado de borradores y confirmación ante salida con cambios.
- [ ] **Seguridad y Abuso:** Esquemas de validación, debounce y rate-limiting.
- [ ] **Codificación y TDD:** Estrategia de pruebas y tareas comiteables por partes.

## Suposiciones y preguntas abiertas
- **Suposición 1**: [Detalle]
- **Pregunta abierta 1**: [Punto a validar]
```

---

## 3. Revisión Final

1. Revisa que ningún criterio de aceptación de `spec.md` haya quedado sin solución técnica ni sin asignar a un lote.
2. Presenta el plan al usuario destacando la tabla de versiones auditadas y la cobertura de los pilares de resiliencia, skeletons, formularios y seguridad.
3. Solicita confirmación para proceder a generar las tareas con `tasks`.
