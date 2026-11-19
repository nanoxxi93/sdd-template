---
name: close
description: Revisa el diff, pasa QA (lint/tests), valida si es cierre total o parcial (según tasks.md y checklist.md generados por implement), consolida commits parciales si aplica, hace push y opcionalmente genera el PR Markdown.
---

# Close (Cerrar Trabajo y Preparar PR)

Esta skill audita la calidad del código, evalúa el progreso mediante `tasks.md` y `checklist.md`, valida los commits parciales generados por los grupos lógicos y empuja la rama sin hacer merge a `main`.

---

## 0. Punto de partida
- `git status -sb` y `git fetch origin`.
- Debes estar en la rama de trabajo de la subfase (no en `main`).

---

## 1. Revisar el diff y Reglas Técnicas
Lee el diff (`git diff origin/main...HEAD` o `git status -s`). Busca y limpia antes de continuar:
- **Restos de desarrollo**: `console.log`, `debugger`, `it.only`, código comentado, `TODO`s sin justificación o archivos temporales.
- **Validación de Reglas (Constitución/Tech Stack)**:
  - Todo nuevo comportamiento o servicio cuenta con sus tests unitarios.
  - Ningún secreto ni credencial expuesta en archivos o frontend.
  - Tolerancia a desconexión y reintentos pasivos respetados en servicios de red.
  - Skeletons presentes en componentes con carga asíncrona.
  - Formularios con protección de dirty state y persistencia de borradores.
  - Botones con debounce y APIs con rate-limiting.
  - Dependencias instaladas verificadas en versiones `latest stable` compatibles.
  - Si hay variables de entorno nuevas, deben estar registradas en `.env.example`.

---

## 2. Validación SDD (Cierre Total o Parcial)
Revisa `tasks.md` y `checklist.md`:
- Si se realizaron commits parciales por cada grupo lógico durante `implement`, verifica que todos los grupos previstos estén concluidos.
- Si quedan grupos sin completar o tareas marcadas como `BLOQUEADO`, es un **Cierre Parcial**. Informa al usuario del estado y qué grupos quedaron cubiertos.
- Si todas las tareas y el `checklist.md` (con las pruebas de desconexión, skeletons y formularios) están en `[x]`, es un **Cierre Total**.
- Si es Cierre Total, actualiza `specs/roadmap.md` marcando la subfase como concluida `[x]`.

---

## 3. Quality Assurance (QA) Automático
Ejecuta la suite de validación del proyecto:
```bash
npm run lint
npm run typecheck
npm test
```
Si falla, detén la skill y muestra el error exacto.

---

## 4. Changelog
Actualiza el `CHANGELOG.md` bajo `## [Sin publicar]` detallando las capacidades de la subfase en las categorías pertinentes (Añadido, Corregido, Seguridad).

---

## 5. Commit Final y Push
- Si ya se realizaron commits parciales por cada grupo lógico durante `implement`, simplemente haz commit de los ajustes finales de QA, docs y roadmap:
  ```bash
  git add .
  git commit -m "docs(roadmap): cierre de subfase y validación de checklist"
  git push -u origin <nombre-de-rama>
  ```
- Si no se hicieron commits parciales, empaqueta en un commit semántico completo:
  ```bash
  git add .
  git commit -m "<tipo>(<alcance>): <título>" -m "<resumen de grupos implementados>"
  git push -u origin <nombre-de-rama>
  ```

---

## 6. Generación de Markdown para Pull Request
Si el usuario lo solicita, genera el bloque Markdown listo para GitHub basándote en los grupos de `tasks.md` y los casos de `checklist.md`:

```markdown
# [Título del PR - Subfase X.Y]

## Descripción
Resumen del trabajo completado en esta subfase.

## Estado del Cierre
**[Total / Parcial]** *(Si es parcial, detallar qué grupos o bloqueos restan).*

## Grupos y Tareas Implementadas (`tasks.md`)
- [x] Grupo 1.1: Setup y esquemas de datos
- [x] Grupo 2.1: Servicios con reintentos pasivos y tolerancia offline
- [x] Grupo 3.1: Componentes de UI con Skeletons y empty states
- [x] Grupo 3.2: Formularios con auto-guardado de borrador y confirmación dirty state
- [x] Grupo 4.1: Debounce en submits y rate-limiting

## QA y Validación de Checklist (`checklist.md`)
- [x] Resiliencia de red y reintentos pasivos validados
- [x] Skeletons verificados sin parpadeos visuales
- [x] Protección de formularios comprobada ante recarga y salida
- [x] Debounce y rate-limiting verificados
```
