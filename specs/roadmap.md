# Hoja de ruta (Roadmap)

> **Versión publicada:** Ninguna
> **Estado actual:** Fase 0

---

## 📌 Guía de Estructura y Consistencia del Roadmap

1. **Principio de Dimensionalidad (1 Spec = 1 Subfase o Módulo Acotado):**
   - Una especificación (`spec.md`) **nunca** debe intentar resolver una fase completa si esta abarca múltiples subsistemas o capas.
   - Si una fase es amplia, **es obligatorio desglosarla en Subfases** (por módulo de negocio o por capa técnica: ej. Datos/Entidades, API/Servicios, UI/Vistas, Resiliencia/Seguridad).
2. **Desglose Dinámico de Specs Sobredimensionadas:**
   - Si durante `specify` o `clarify` se detecta que una funcionalidad es demasiado grande (> 250 líneas o múltiples capas/flujos), **detente y actualiza este roadmap**: divide la fase en subfases atómicas, acota la spec actual a la primera subfase y añade las restantes a la lista de pendientes.

---

## Fase 0: Validación Técnica y Spikes
Experimentos acotados para descartar riesgos críticos y auditar versiones estables de librerías.
- [ ] **Subfase 0.1: Spike de Arquitectura y Dependencias**
  - [ ] Experimento 1: Validar compatibilidad de versiones `latest stable` del stack
  - [ ] Experimento 2: Validar viabilidad técnica de X
- [ ] **Subfase 0.2: Prototipo de Resiliencia**
  - [ ] Experimento 3: Validar persistencia local y comportamiento offline/reintentos

## Fase 1: MVP (Mínimo Producto Viable)
Dividido rigurosamente en subfases por módulo o por capa para mantener especificaciones atómicas y verificables.

### Subfase 1.1: Núcleo y Contratos de Datos (Capa Dominio/Modelos)
- [ ] Definición de esquemas de datos y validaciones estrictas
- [ ] Entidades de dominio base y pruebas unitarias

### Subfase 1.2: Servicios y Conectividad (Capa Lógica y Resiliencia)
- [ ] Servicios principales con reintentos pasivos y manejo de errores transitorios
- [ ] Persistencia de datos y soporte offline inicial

### Subfase 1.3: Interfaz de Usuario y Experiencia (Capa UI/UX)
- [ ] Vistas principales con componentes Skeleton para carga asíncrona
- [ ] Formularios protegidos con detección de cambios (*dirty*) y auto-guardado de borradores
- [ ] Estados vacíos (*empty states*) y feedback contextual

### Subfase 1.4: Seguridad y Endurecimiento
- [ ] Control de abusos: debounce en disparadores de UI y rate-limiting
- [ ] Aislamiento de secretos y sanitización de datos

---

## Fase 2: Expansión
- [ ] **Subfase 2.1: Funcionalidad Complementaria 1**
  - [ ] Backend y Dominio de Módulo Complementario 1
  - [ ] Interfaz y Skeletons de Módulo Complementario 1
- [ ] **Subfase 2.2: Funcionalidad Complementaria 2**
  - [ ] Integración y lógica de Módulo Complementario 2

---

## Fase 3: Monetización o Escala
- [ ] **Subfase 3.1: Funcionalidad Avanzada / Escala**
  - [ ] Funcionalidad avanzada y monetización
  - [ ] Métricas de rendimiento, optimización de caché y robustez de red

---

## Tareas Sueltas y Seguimiento

### En curso
<!-- Las funcionalidades activas se listan aquí enlazando su subfase correspondiente: -->
<!-- - [Subfase 1.1: Núcleo](AAAA-MM-DD-nombre-subfase/) — Breve descripción del alcance -->
- Ninguna

### En main, sin versión todavía
- Ninguna

### Después de la 1.0.0
- Ninguna
