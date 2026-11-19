---
name: implement
description: Construye el código sistemáticamente siguiendo tasks.md, ejecutando y entregando por grupos lógicos de revisión y commits parciales. Toma spec.md, plan.md y tasks.md como base.
---

# Implementar Tareas (Spec-Driven Development)

En el Spec-Driven Development, el comando `implement` ejecuta las tareas definidas en `tasks.md` de forma sistemática y ordenada. 

**REGLA DE ENTREGA: TRABAJO Y REVISIÓN POR GRUPOS LÓGICOS (COMMITS PARCIALES).**
Para evitar cambios gigantescos difíciles de auditar, la implementación se realiza **grupo por grupo** (los bloques `Grupo X.Y` de 2 a 4 tareas definidos en `tasks.md`). Al culminar cada grupo, se realiza una pausa para revisión del código y se genera un commit parcial.

---

## 0. Contexto y Punto de Partida

Antes de escribir código:
1. **Verifica la rama**: Comprueba que estás en la rama de trabajo derivada de `main` creada para esta subfase.
2. **Carga la documentación base**: Lee `spec.md`, `plan.md` y `tasks.md`.
3. **Identifica el Grupo Objetivo**: Por defecto, toma el siguiente Grupo Lógico pendiente (ej. `Grupo 1.1`), o el grupo específico que el usuario indique.

---

## 1. Ciclo de Ejecución por Grupo Lógico

Para el Grupo Lógico en curso:

1. **Auditoría de Dependencias (si aplica):** Si el grupo incluye tareas de setup o paquetes, consulta activamente las versiones `latest stable` vigentes (`npm view`, `pip index`, etc.) comprobando que no rompan librerías existentes antes de añadirlas.
2. **Desarrollo Tarea por Tarea (TDD):**
   - Escribe primero los tests unitarios que verifiquen el comportamiento esperado.
   - Implementa el código mínimo para pasar los tests.
   - Asegura la presencia de los estándares requeridos: Skeletons en UI, reintentos pasivos en red, persistencia de borradores en formularios, debounce en botones de envío.
3. **Ejecutar el Punto de Revisión:**
   - Corre los tests del grupo y linters locales.
   - Comprueba el criterio indicado en la línea `*Punto de Revisión:*` del grupo en `tasks.md`.
4. **Marcar Progreso y Sugerir Commit Parcial:**
   - Marca las casillas de las tareas completadas (`[x]`) en `tasks.md`.
   - Muestra al usuario un resumen conciso del código implementado en este grupo.
   - **Ofrece/ejecuta el commit parcial sugerido** (ej. usando el mensaje semántico especificado en la línea `*Commit Parcial sugerido:*` de `tasks.md`).
5. **Pausa para Validación:** Permite al usuario revisar el commit parcial antes de proceder al siguiente grupo lógico.

---

## 2. Manejo de Ambigüedades (Pausa Obligatoria)

La regla de oro de la implementación es no adivinar. 
- Si durante la programación descubres que una tarea es vaga o un caso extremo no fue contemplado: **PAUSA LA IMPLEMENTACIÓN INMEDIATAMENTE**.
- Busca la intención en `spec.md` y `plan.md`. Si no está, consulta al usuario.
- **Acción Obligatoria**: Actualiza la descripción en `tasks.md` (y si corresponde en `spec.md`) antes de continuar codificando.

---

## 3. Manejo de Bloqueos (Dependencias Externas)

Si una tarea no puede avanzar por factores externos:
- Márcala en `tasks.md` como:
  `- [ ] BLOQUEADO: esperando <razón del bloqueo> - <referencia>`
- Regístrala en la sección `## Bloqueos y Dependencias Externas`.
- Si el resto del grupo puede cerrarse o hay otro grupo independiente, continúa con él.

---

## 4. Al finalizar la interacción

Reporta al usuario:
- Qué Grupo Lógico y tareas completaste (`[x]`).
- El estado de las pruebas locales y el Punto de Revisión.
- El commit parcial generado (o propuesto) con su mensaje semántico.
- El siguiente grupo pendiente en la lista de tareas.
