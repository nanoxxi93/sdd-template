# {{PROJECT_NAME}}

{{PROJECT_DESCRIPTION_Y_CONTEXTO_PRINCIPAL}}

- **Spec-Driven Development (SDD)**: El proyecto sigue estrictamente el ciclo de SDD. Todo desarrollo pasa por las skills en `.claude/skills/` (o `.agents/skills/`): `specify` → `clarify` → `plan` → `tasks` → `checklist` → `analyze` → `implement` → `close` → `publish`.
- **Compatibilidad Multi-Harness**: Este repositorio es compatible de forma nativa con **Claude Code**, **Google Antigravity**, **OpenAI Codex** y **Cursor**. Las instrucciones maestras residen sincronizadas en `CLAUDE.md`, `AGENTS.md` y `GEMINI.md`, y las skills en `.claude/skills/` y `.agents/skills/`.
- **Base del Producto**: `specs/mission.md`, `specs/tech-stack.md`, `specs/roadmap.md`, `specs/constitution.md`. Siempre consúltalos.
- **Specs por subfase**: `specs/AAAA-MM-DD-<nombre-subfase>/` generadas por las skills.
- Idioma de la documentación: español. Finales de línea: LF.

## Directivas Críticas para la IA

1. **Auditoría de Dependencias y Scaffolding (Latest Stable):**
   - Los LLMs tienden a sugerir dependencias desactualizadas por la fecha de corte de su entrenamiento.
   - **Regla Obligatoria:** Antes de generar scaffolding inicial o agregar paquetes a `package.json`, `pyproject.toml`, etc., consulta e instala activamente las versiones `latest stable` vigentes usando las herramientas del gestor de paquetes (`npm view`, `pip index`, etc.), verificando que no existan conflictos de compatibilidad cruzada entre librerías.
2. **Consistencia de Roadmap y Dimensionalidad de Specs:**
   - **1 Spec = 1 Subfase Atómica (< 250 líneas):** Nunca crees una spec monolítica para una fase amplia. Desglosa la fase en `specs/roadmap.md` en subfases consistentes (por módulo o por capa) y redacta la spec solo para la subfase actual.
3. **Clarify en 1 Sola Pasada (Explicativo y con Escenarios "¿Qué pasaría sí...?"):**
   - La skill `clarify` escanea la spec de forma integral contra la matriz 360° y formula activamente escenarios de contingencia (*¿Qué pasaría si se cae la red? ¿Si el usuario recarga? ¿Si el token expira? ¿Si hay doble clic rápido? ¿Si el servicio tarda 30s?*).
   - Entrega un reporte **explicativo y fundamentado** con el impacto, las opciones consideradas y la recomendación justificada para tomar decisiones con criterio en una sola interacción.
4. **Tareas por Grupos Lógicos y Commits Parciales:**
   - `tasks.md` organiza el trabajo en grupos cohesivos de 2 a 4 tareas con puntos de revisión y sugerencias de commit semántico. Durante `implement`, entrega y comitea grupo por grupo para facilitar la revisión del código.
5. **Pilares Transversales Obligatorios:**
   - Toda funcionalidad relevante debe contemplar: tolerancia a desconexión y reintentos pasivos en red; skeletons estructurales y empty states en UI; protección contra pérdida de datos en formularios (dirty state y auto-guardado de borradores); y seguridad (debounce en botones, rate-limit y esquemas estrictos).

---

## Registros que se mantienen mientras se trabaja

### `CHANGELOG.md` — qué cambió
Agrega una entrada **en el mismo turno** en que termines un cambio que afecte al producto, la arquitectura, las specs o la configuración del repo:
- Dentro de `## [Sin publicar]`, bajo el encabezado de la fecha de hoy (`date +%F`); créalo arriba de los demás si no existe.
- En la categoría que corresponda (Añadido, Cambiado, Obsoleto, Eliminado, Corregido, Seguridad). Crea la categoría si no existe en esa fecha.
- Una línea por cambio, desde el punto de vista de quien lee el proyecto, no la lista de archivos tocados. Enlaza la spec si la hay.
- No registres ediciones menores sin efecto (typos, formato).

### `specs/intentos-fallidos.md` — qué no funcionó
Antes de proponer un enfoque, una librería o una solución a un bug, **busca en este archivo**. Si ya está registrado, no lo repitas salvo que se cumpla su condición de *Reconsiderar si*, y dilo explícitamente.

Agrega una entrada cuando:
- Algo que se probó falló: build, test, librería, configuración, experimento de la Fase 0, comportamiento de un dispositivo.
- Un enfoque se descartó tras analizarlo y es probable que alguien lo vuelva a proponer.

Cómo:
- Usa la plantilla del archivo, con el siguiente ID `IF-NNN`, y agrégala **arriba** de las demás y en el índice.
- Anota la causa, no solo el síntoma, e incluye mensajes de error textuales y versiones.
- Las entradas no se borran. Si algo cambia (p. ej. una nueva versión de la librería lo arregla), agrega una nota con fecha al final de la entrada.
- No registres errores triviales corregidos al momento (typos, imports faltantes).
