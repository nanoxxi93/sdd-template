---
name: constitution
description: Aplica los principios, restricciones y estándares no negociables definidos en /specs/constitution.md para el Spec-Driven Development. Úsala para validar especificaciones, planes, tareas o código.
---

# Desarrollo Guiado por Especificaciones: Constitución

Esta skill instruye al agente a aplicar y respetar la constitución del proyecto en el desarrollo asistido por IA (Spec-Driven Development), usando el archivo `/specs/constitution.md`.

## El archivo de constitución

Un archivo de constitución captura principios, restricciones y estándares no negociables que rigen el proyecto. También sirve como barandilla para el desarrollo asistido por IA. 

Cuando el agente genera especificaciones, planes, tareas o código, **debe hacer referencia a la constitución** para comprobar que las propuestas cumplen con sus estándares. Para proyectos brownfield, documenta los patrones y restricciones arquitectónicos existentes.

## Ventajas principales

- **Aplicación de la coherencia:** Garantiza la alineación con las decisiones arquitectónicas durante proyectos largos con varios desarrolladores.
- **Documentación de cumplimiento:** Hace que los requisitos normativos y las directivas de seguridad sean explícitos y auditables.
- **Captura de conocimientos institucionales:** Conserva las lecciones ganadas de forma que guía la generación de código de inteligencia artificial.
- **Carga cognitiva reducida:** Automatiza la aplicación de directivas organizativas durante el desarrollo.

## Estructura de la Constitución

Una constitución bien estructurada organiza los principios en categorías a las que los asistentes de inteligencia artificial pueden hacer referencia fácilmente. Las secciones comunes que contiene `/specs/constitution.md` son:

- **Estándares tecnológicos y dependencias:** Se usan para especificar tecnologías, plataformas y marcos aprobados, incluyendo la regla obligatoria de auditar versiones `latest stable` compatibles (prohibido instalar paquetes desactualizados por inercia del LLM).
- **Resiliencia y conectividad:** Expectativas de tolerancia a desconexión, reintentos pasivos en background (backoff con jitter) y previsión obligatoria de contingencias "¿Qué pasaría si...?".
- **Experiencia de Usuario (UX) y Frontend:** Componentes con Skeletons estructurales para cargas asíncronas y protección obligatoria contra pérdida de datos en formularios (dirty state y guardado de borradores).
- **Requisitos de seguridad y control de abusos:** Elementos como autenticación, autorización, cifrado, reglas de protección de datos, validación estricta con esquemas, límites de tasa (*rate-limiting*) y *debounce* en botones contra doble clic.
- **Rendimiento y escalabilidad:** Establecen expectativas para el comportamiento del sistema bajo carga.
- **Estándares de codificación:** Proporcionan requisitos que ayudan a garantizar la calidad del código, como Test-Driven Development (TDD) e implementación por grupos lógicos con commits parciales.
- **Cumplimiento y gobernanza:** Se utilizan para documentar los requisitos normativos y de políticas internas.

## Instrucciones para el Agente

1. **Validación:** Antes de proponer una nueva arquitectura, escribir especificaciones o generar código, lee `/specs/constitution.md` y verifica que la propuesta cumple con las reglas descritas.
2. **Defensa de los estándares:** Si se propone algo que entra en conflicto con la constitución (ej. componentes sin skeleton, peticiones sin reintentos, paquetes obsoletos o almacenamiento inseguro), señala la violación de los estándares documentados y propón la alternativa alineada.
3. **Mantenimiento:** Si se acuerdan nuevas reglas o restricciones innegociables durante el proyecto, sugiere añadirlas a `/specs/constitution.md`.
