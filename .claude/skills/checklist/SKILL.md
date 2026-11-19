---
name: checklist
description: Genera el plan de pruebas manuales y calidad (checklist.md) basándose en Criterios de Aceptación, Casos Extremos y los pilares transversales (resiliencia, skeletons, formularios protegidos y seguridad).
---

# Generar Lista de Comprobación y QA (checklist.md)

En el Spec-Driven Development, la skill `checklist` toma los requerimientos y casos extremos del documento de especificación y los convierte en un plan estricto de Control de Calidad (QA) manual y de aceptación. Es el equivalente a escribir "pruebas unitarias para la prosa". 

Su objetivo es comprobar la integridad de los requisitos asegurando que cada uno pueda ser validado empíricamente una vez implementado el código, tanto en condiciones normales como ante fallos de red, cargas lentas o abusos de interfaz.

---

## 1. Reglas de Generación y Cobertura Obligatoria

Al construir el `checklist.md`, debes aplicar rigurosamente estas reglas:

- **Trazabilidad estricta**: Cada "Criterio de Aceptación" (`CA-X`) y cada "Caso Extremo" (`CE-X`) definidos en el archivo `spec.md` de la funcionalidad actual debe convertirse en, al menos, un elemento verificable en el checklist.
- **Contexto de entorno**: Debes inferir dónde se realiza la prueba basándote en la funcionalidad (ej. si interactúa con hardware o la red sin conexión, requiere el **emulador** o throttling de DevTools; si es de interfaz estándar, se prueba en el **navegador**; si es de modelos o lógica, en suite CLI). Apóyate en `specs/intentos-fallidos.md` si tienes dudas.
- **Pasos accionables**: No uses descripciones vagas como *"Probar la carga de archivos"*. Define explícitamente qué acciones debe tomar quien hace el QA para validar el flujo paso a paso y cuál es el resultado observable esperado.

Debes cubrir obligatoriamente estas 6 áreas conforme a `specs/_template/checklist.md`:

1. **Casos de Aceptación Funcionales (CAs):** Pasos paso a paso para comprobar los flujos felices y reglas de negocio descritas en `spec.md`.
2. **Resiliencia de Red y Desconexión:**
   - Simulación de modo offline (corte de red durante navegación o envío).
   - Reintentos pasivos en background ante latencia alta (Slow 3G).
   - Reconexión automática sin pérdida de estado.
3. **UX, Skeletons y Feedback de Carga:**
   - Inspección visual de Skeletons estructurales durante cargas asíncronas (evitar pantallas en blanco y saltos de layout / CLS).
   - Verificación de estados vacíos (*empty states*) descriptivos y feedback contextual.
4. **Formularios y Prevención de Pérdida de Datos:**
   - Intento de salida o recarga con datos sin guardar (verificar alerta de confirmación por *dirty form*).
   - Recarga de página tras cierre forzoso (verificar recuperación automática del borrador local).
   - Limpieza automática del borrador tras envío exitoso.
5. **Seguridad, Control de Abusos y Escenarios "¿Qué pasaría si...?":**
   - Prueba de clics repetitivos rápidos en botón de envío (comprobar debounce y deshabilitación inmediata).
   - Rate-limiting ante solicitudes masivas.
   - Envío de datos límite o malformados (rechazo limpio sin inyecciones ni errores 500).
   - Simulación de respuestas de error del servidor (500/503) o timeouts largos (mostrar pantalla degradada con botón de reintento).
   - Expiración de token/sesión en pleno flujo (preservación de borrador).
6. **Verificación de Dependencias:**
   - Comprobación de que no se hayan introducido paquetes obsoletos o con vulnerabilidades reportadas (`npm audit` o equivalente).

---

## 2. Estructura de `checklist.md`

Genera el archivo en la carpeta de la funcionalidad usando la estructura de tablas por área:

```markdown
# Lista de Comprobación y QA: <Nombre de la Funcionalidad / Subfase>

## Entornos de Prueba Requeridos
- [ ] Entorno local de desarrollo (CLI / Dev Server)
- [ ] Navegador web con DevTools (Throttling de red y simulación offline)
- [ ] Suite de pruebas automatizadas

## Casos de Prueba (Criterios de Aceptación)
| ID | Entorno | Acción / Pasos a seguir | Resultado Esperado | Estado (`[ ]` / `[x]`) | Observaciones |

## Pruebas de Resiliencia, Red y Tolerancia a Desconexiones
| ID | Entorno | Acción / Pasos a seguir | Resultado Esperado | Estado (`[ ]` / `[x]`) | Observaciones |

## Pruebas de UX, Skeletons y Estados de Carga
| ID | Entorno | Acción / Pasos a seguir | Resultado Esperado | Estado (`[ ]` / `[x]`) | Observaciones |

## Pruebas de Formularios y Protección contra Pérdida de Datos
| ID | Entorno | Acción / Pasos a seguir | Resultado Esperado | Estado (`[ ]` / `[x]`) | Observaciones |

## Pruebas de Seguridad, Control de Abusos y Escenarios "¿Qué pasaría si...?"
| ID | Entorno | Acción / Pasos a seguir | Resultado Esperado | Estado (`[ ]` / `[x]`) | Observaciones |

## Verificación de Dependencias y Scaffolding
| ID | Entorno | Acción / Pasos a seguir | Resultado Esperado | Estado (`[ ]` / `[x]`) | Observaciones |
```

---

## 3. Revisión Final e Instrucciones

1. Al finalizar de redactar la tabla, cruza mentalmente los IDs generados contra el `spec.md` original para confirmar cobertura total de Criterios de Aceptación y Casos Extremos.
2. Infórmale al usuario que el plan de pruebas de QA ha sido creado con éxito, destacando los escenarios de resiliencia, skeletons y formularios incluidos.
3. Recuérdale que el archivo `checklist.md` será evaluado por la skill `close` al final del desarrollo; no se podrá consolidar la subfase ni llevar el código a `main` si existen casos de prueba sin marcar (`[x]`).
