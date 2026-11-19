# {{PROJECT_NAME}} — Directivas para Google Antigravity / Gemini

{{PROJECT_DESCRIPTION_Y_CONTEXTO_PRINCIPAL}}

- **Spec-Driven Development (SDD)**: El proyecto sigue estrictamente el ciclo de SDD. Las skills se encuentran en `.agents/skills/` (y `.claude/skills/`): `specify` → `clarify` → `plan` → `tasks` → `checklist` → `analyze` → `implement` → `close` → `publish`.
- **Compatibilidad**: Este proyecto usa el estándar universal `AGENTS.md`. Consulta siempre [`AGENTS.md`](./AGENTS.md) para las directivas compartidas del agente.
- **Base del Producto**: `specs/mission.md`, `specs/tech-stack.md`, `specs/roadmap.md`, `specs/constitution.md`.
- **Specs por subfase**: `specs/AAAA-MM-DD-<nombre-subfase>/`.
- Idioma de la documentación: español. Finales de línea: LF.

---

## Directivas Críticas para Antigravity

1. **Auditoría de Dependencias y Scaffolding (Latest Stable):**
   - Antes de generar scaffolding o sugerir dependencias (`package.json`, `pyproject.toml`, etc.), consulta e instala activamente versiones `latest stable` usando comandos de paquete (`npm view`, `pip index`, etc.) comprobando la compatibilidad mutua.
2. **Consistencia de Roadmap y Dimensionalidad de Specs:**
   - 1 Spec = 1 Subfase Atómica (< 250 líneas). Desglosar fases amplias en `specs/roadmap.md` en subfases consistentes (por módulo o por capa).
3. **Clarify en 1 Sola Pasada (Explicativo y con Escenarios "¿Qué pasaría sí...?"):**
   - Evaluar siempre contingencias (caídas de red, cancelaciones, expiración de tokens, timeouts largos, doble clic) y entregar un reporte explicativo fundamentado para toma de decisiones sin rondas infinitas.
4. **Tareas por Grupos Lógicos y Commits Parciales:**
   - Organizar e implementar tareas en bloques de 2 a 4 unidades en `tasks.md`, realizando pausas de revisión y commits semánticos por grupo.
5. **Pilares Transversales Innegociables:**
   - Skeletons en UI, tolerancia offline y reintentos pasivos en red, auto-guardado y dirty state en formularios, debounce y rate-limit en seguridad.

---

## Registros que se mantienen mientras se trabaja

- **`CHANGELOG.md`**: Actualizar bajo `## [Sin publicar]` en el mismo turno en que se realice un cambio significativo.
- **`specs/intentos-fallidos.md`**: Consultar antes de proponer librerías o patrones, y registrar cualquier enfoque fallido o descartado con ID `IF-NNN`.
