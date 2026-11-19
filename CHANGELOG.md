# Changelog

Registro de cambios de {{PROJECT_NAME}}. Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/); el proyecto usa [Versionado Semántico](https://semver.org/lang/es/) desde la primera versión publicada.

Mientras no haya versiones, todo va en **Sin publicar**, agrupado por fecha (la más reciente arriba).

Categorías: **Añadido** (algo nuevo) · **Cambiado** (algo existente se comporta distinto) · **Obsoleto** (se eliminará pronto) · **Eliminado** · **Corregido** (bugs) · **Seguridad**.

## [Sin publicar]

### 2026-11-19

#### Añadido
- **Compatibilidad Multi-Harness Nativa (Antigravity, Codex, Cursor y Claude Code):**
  - Creación de archivos maestros de instrucciones a nivel raíz: `AGENTS.md` (estándar universal para Codex/Cursor/Antigravity) y `GEMINI.md` (para Gemini/Antigravity), manteniendo paridad total con `CLAUDE.md`.
  - Estructuración de carpetas de skills duales: `.agents/skills/` (descubierta automáticamente por Antigravity y Codex) y `.claude/skills/` (descubierta por Claude Code).
  - Script de sincronización de skills `scripts/sync_skills.py` y validación en `scripts/validate_sdd.py`.
- **Reporte Explicativo y Fundamentado en `clarify`:**
  - Evolución del reporte consolidado: cada hallazgo detalla qué se detectó, el riesgo e impacto real, las alternativas consideradas y la justificación técnica de la recomendación, facilitando una toma de decisiones informada.
- **Evaluación Sistemática de Escenarios "¿Qué pasaría si...?":**
  - Incorporación del marco de estrés y contingencias en `clarify`, `spec.md`, `plan.md`, `checklist.md` y `constitution.md`: caídas de red en vuelo, interrupciones y recargas del usuario, expiración de tokens/sesión, timeouts largos del servidor (500/503), concurrencia/doble submit y fallos de almacenamiento local.

### 2026-11-18

#### Añadido
- **Auditoría obligatoria de Dependencias y Scaffolding (`latest stable`):** Regla en `constitution.md`, `tech-stack.md` y `.claude/skills/plan` para contrastar paquetes propuestos contra versiones vigentes y estables, evitando dependencias desactualizadas por corte de entrenamiento de los LLMs y asegurando compatibilidad mutua.
- **Estructuración del Roadmap en Fases y Subfases:** Desglose obligatorio en `roadmap.md` por módulo o por capa arquitectónica, acotando cada `spec.md` a una subfase atómica (< 250 líneas) y permitiendo particionar specs sobredimensionadas dinámicamente.
- **Auditoría exhaustiva en 1 Sola Pasada para `clarify`:** Matriz de inspección 360° que evalúa contratos, UI, red, formularios, seguridad y casos extremos en una única interacción con soluciones recomendadas, eliminando ciclos interminables de preguntas.
- **Organización de Tareas por Grupos Lógicos y Commits Parciales:** Reestructuración de `tasks.md` y de las skills `tasks` e `implement` para agrupar tareas en bloques de 2 a 4 unidades con puntos de revisión y sugerencias de commits semánticos incrementales.
- **Estándares Transversales Innegociables en Plantillas y Skills:**
  - Tolerancia a desconexiones y reintentos pasivos en segundo plano (exponential backoff + jitter).
  - Componentes Skeleton estructurales para cargas asíncronas y estados vacíos descriptivos.
  - Protección contra pérdida de datos en formularios (auto-guardado de borradores y advertencia ante *dirty state*).
  - Medidas de seguridad y control de abusos (debounce contra doble submit, rate-limiting y validación estricta de esquemas).

### {{YYYY-MM-DD}}

#### Añadido
- Inicialización del repositorio y base SDD.
