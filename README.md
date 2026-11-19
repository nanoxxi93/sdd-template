# {{PROJECT_NAME}}

{{PROJECT_SHORT_DESCRIPTION}}

**Specs primero (SDD):** El proyecto usa **Spec-Driven Development**. Toda funcionalidad nueva nace en [`specs/`](./specs) con sus requerimientos, plan técnico y desglose de tareas en grupos lógicos, pasando por un ciclo de auditoría antes de tocar código. La misión, constitución, pila técnica y hoja de ruta viven allí.
El ciclo completo se ejecuta usando las skills ubicadas en [`.agents/skills/`](./.agents/skills) o [`.claude/skills/`](./.claude/skills) en este orden estricto: `specify` → `clarify` → `plan` → `tasks` → `checklist` → `analyze` → `implement` → `close` → `publish`. Para entender el detalle del proceso, **lee siempre [`specs/README.md`](./specs/README.md) primero**.

## Pilares Metodológicos Clave

- **Compatibilidad Multi-Harness Nativa:** Soporte listo para usar en **Google Antigravity**, **OpenAI Codex**, **Cursor** y **Claude Code**. Las instrucciones residen sincronizadas en [`AGENTS.md`](./AGENTS.md), [`GEMINI.md`](./GEMINI.md) y [`CLAUDE.md`](./CLAUDE.md), y las skills en `.agents/skills/` y `.claude/skills/` (gestionables con `python scripts/sync_skills.py`).
- **Auditoría de Dependencias Latest Stable:** Regla estricta contra el sesgo temporal de los LLMs. Toda propuesta de scaffolding o paquete debe auditarse contra la versión estable más reciente compatible antes de escribirse.
- **Roadmap con Subfases Consistentes:** El roadmap se desglosa en subfases atómicas (por módulo o por capa). Cada especificación cubre únicamente una subfase (< 250 líneas) para evitar especificaciones monolíticas.
- **Clarify Explicativo en 1 Sola Pasada:** Auditoría exhaustiva de 360° en una sola interacción con evaluación obligatoria de escenarios **"¿Qué pasaría sí...?"** (cortes de red, recargas accidentales, timeouts de 30s, tokens expirados, doble submit). Cada hallazgo detalla el riesgo, alternativas y recomendación para tomar decisiones con criterio.
- **Tareas por Grupos Lógicos y Commits Parciales:** Tareas agrupadas en bloques de 2 a 4 unidades con puntos de revisión y sugerencias de commits semánticos incrementales.
- **Estándares Transversales Innegociables:** Tolerancia a desconexión y reintentos pasivos; componentes con Skeletons estructurales; protección contra pérdida de datos en formularios (drafts y dirty state); y seguridad con debounce y rate-limiting.

**Memoria Local de la IA:** Para evitar errores repetitivos de entorno local (como usar CRLF en Windows, o ejecutar comandos bash incompatibles con PowerShell), cualquier IA que trabaje en este repo buscará y respetará el archivo **`.ai-context.md`**. Ese archivo NO se commitea, y la IA tiene la orden de **actualizarlo** ante cualquier tropiezo con el sistema operativo local para "recordarlo" en chats futuros.

## Documentación Fundacional

- **Requisitos y Planificación**: Ver [`specs/README.md`](./specs/README.md).
- **Misión y UX**: [`specs/mission.md`](./specs/mission.md).
- **Constitución (Reglas de Oro)**: [`specs/constitution.md`](./specs/constitution.md).
- **Tech Stack y Arquitectura**: [`specs/tech-stack.md`](./specs/tech-stack.md).
- **Hoja de Ruta (Fases y Subfases)**: [`specs/roadmap.md`](./specs/roadmap.md).
- **Intentos Fallidos**: Ver [`specs/intentos-fallidos.md`](./specs/intentos-fallidos.md) antes de proponer soluciones o librerías.
- **Cambios e Historial**: Registrados en [`CHANGELOG.md`](./CHANGELOG.md).
