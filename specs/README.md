# Especificaciones (Spec-Driven Development)

{{PROJECT_NAME}} sigue la metodología **Spec-Driven Development (SDD)**. Antes de escribir una sola línea de código, cada funcionalidad se diseña, se valida, se desglosa y se audita de forma rigurosa.

Este directorio (`specs/`) contiene tanto los documentos fundacionales del proyecto como las carpetas individuales de cada funcionalidad o subfase a implementar.

---

## 1. Documentos Fundacionales (La Base)

Estos archivos mandan sobre todo el código y deben ser consultados continuamente por las skills:

- [`mission.md`](mission.md) — Qué es {{PROJECT_NAME}}, para quién está diseñado y sus principios de experiencia de usuario.
- [`tech-stack.md`](tech-stack.md) — La pila tecnológica, política de dependencias `latest stable`, patrones aprobados y arquitectura.
- [`roadmap.md`](roadmap.md) — La hoja de ruta estructurada en fases y subfases atómicas.
- [`constitution.md`](constitution.md) — Los principios no negociables (seguridad, resiliencia, skeletons, protección de formularios, contingencias "¿Qué pasaría si...?", TDD).
- [`intentos-fallidos.md`](intentos-fallidos.md) — Registro de enfoques y herramientas que fallaron y no deben repetirse.

---

## 2. Reglas Cardinales del Desarrollo SDD

1. **Compatibilidad Multi-Harness Nativa (Antigravity, OpenAI Codex, Claude Code):**
   - El proyecto es compatible de fábrica con cualquier entorno de agentes. Las instrucciones se mantienen sincronizadas en `AGENTS.md`, `GEMINI.md` y `CLAUDE.md`, y las skills en `.agents/skills/` y `.claude/skills/` (sincronizables vía `python scripts/sync_skills.py`).
2. **Dimensionalidad y Consistencia (1 Spec = 1 Subfase o Módulo Acotado):**
   - Una especificación nunca debe abarcar fases gigantescas. Si una funcionalidad abarca múltiples capas o subsistemas, se desglosa en `roadmap.md` mediante **subfases** (por módulo o por capa) y se especifica una subfase a la vez (< 250 líneas).
3. **Auditoría de Dependencias Latest Stable:**
   - Prohibido instalar o proponer paquetes viejos basados en el corte de entrenamiento de los LLMs. Se debe auditar y verificar que las dependencias sean las versiones estables más recientes compatibles sin romper el ecosistema del proyecto.
4. **Clarify Explicativo en 1 Sola Pasada con Escenarios "¿Qué pasaría sí...?":**
   - La skill `clarify` escanea 360° todos los ejes, evalúa activamente contingencias y estrés (caídas de red, abandonos de usuario, timeouts largos, expiración de tokens, doble submit) y entrega un reporte explicativo con justificaciones, alternativas y recomendaciones para tomar decisiones con criterio en una sola interacción.
5. **Tareas por Grupos Lógicos y Commits Parciales:**
   - `tasks.md` organiza el trabajo en grupos pequeños (2 a 4 tareas) con puntos de revisión y sugerencias de commit semántico, permitiendo auditar el código y comitear de manera incremental.
6. **Los 5 Pilares Universales Obligatorios:**
   - Resiliencia de red y reintentos pasivos con backoff exponencial.
   - Skeletons estructurales para cargas asíncronas y empty states descriptivos.
   - Protección contra pérdida de datos en formularios (draft auto-save y confirmación ante dirty state).
   - Seguridad, rate-limiting y debounce contra doble clic.
   - Verificación de paquetes y compatibilidad.

---

## 3. El Flujo de Trabajo SDD (Paso a Paso)

Cuando se va a implementar una funcionalidad o subfase nueva, el trabajo se guarda en su propia carpeta `specs/AAAA-MM-DD-nombre-subfase/`. 

Las skills de IA se ejecutan estrictamente en este orden (accesibles desde `.agents/skills/` o `.claude/skills/`):

### Etapa 1: Diseño y Requisitos (El Qué)
1. **`specify`**: Dialoga contigo para definir la subfase. Si la tarea es amplia, desglosa el roadmap en subfases primero. Genera el **`spec.md`** cubriendo Criterios de Aceptación, Requisitos, Pilares transversales y Casos Extremos.
2. **`clarify`**: Actúa como un Analista de Sistemas Senior. Aplica la matriz 360°, formula escenarios "¿Qué pasaría si...?" y entrega un **Reporte Explicativo** con riesgos, alternativas y soluciones recomendadas para aprobar en bloque. Reescribe `spec.md` para blindarlo.

### Etapa 2: Arquitectura y Tareas (El Cómo)
3. **`plan`**: Diseña la arquitectura en **`plan.md`**. Audita las versiones `latest stable` de dependencias, define la estrategia de skeletons, reintentos y persistencia, planifica la mitigación de contingencias y verifica la constitución.
4. **`tasks`**: Genera la hoja de ruta **`tasks.md`** dividida en **Grupos Lógicos pequeños (2 a 4 tareas)** con puntos de revisión y commits parciales sugeridos.
5. **`checklist`**: Vuelve a `spec.md` y genera el plan de pruebas manuales y QA en **`checklist.md`**, incluyendo pruebas de desconexión, skeletons, formularios, abuso y escenarios "¿Qué pasaría si...?".

### Etapa 3: Auditoría y Construcción (La Ejecución)
6. **`analyze`**: Control de calidad cruzado. Revisa que nada se haya escapado entre `spec`, `plan`, `tasks`, `checklist` y `constitution` antes de codificar.
7. **`implement`**: El motor de desarrollo. Lee `tasks.md` y ejecuta grupo por grupo. Al terminar cada grupo, valida los tests y permite revisar y realizar el commit parcial correspondiente.

### Etapa 4: Finalización
8. **`close`**: Corre linters y tests, verifica que `tasks.md` y `checklist.md` estén completos, empuja la rama y genera el Markdown para el PR.
9. **`publish`**: Se usa desde `main` para el salto SemVer, actualización de CHANGELOG, compilación de artefactos y lanzamiento en GitHub.

---

## 4. Mantenimiento de Especificaciones (Changelog de Spec)

No uses el CHANGELOG global para cambios internos de requisitos durante el desarrollo. Mantén la sección `## Changelog de la Especificación` al final de `spec.md`.
