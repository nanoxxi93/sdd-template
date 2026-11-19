---
name: checklist
description: Genera el plan de pruebas manuales y calidad (checklist.md) basándose en Criterios de Aceptación, Casos Extremos y los pilares transversales (resiliencia, skeletons, formularios protegidos y seguridad).
---

# Generar Lista de Comprobación y QA (checklist.md)

En el Spec-Driven Development, la skill `checklist` toma los requisitos y casos extremos de `spec.md` y diseña el plan exhaustivo de Control de Calidad (QA) manual y de aceptación. 

Su objetivo es comprobar empíricamente que la funcionalidad responde adecuadamente tanto en condiciones normales como ante fallos de red, cargas lentas o abusos de interfaz.

---

## 1. Reglas de Generación y Cobertura Obligatoria

Al construir el `checklist.md`, debes incluir obligatoriamente estas 6 áreas de prueba conforme a `specs/_template/checklist.md`:

1. **Casos de Aceptación Funcionales (CAs):** Pasos paso a paso para comprobar los flujos felices y reglas de negocio descritas en `spec.md`.
2. **Resiliencia de Red y Desconexión:**
   - Simulación de modo offline (corte de red durante navegación o envío).
   - Reintentos pasivos en background ante latencia alta (Slow 3G).
   - Reconexión automática sin pérdida de estado.
3. **UX, Skeletons y Feedback de Carga:**
   - Inspección visual de Skeletons estructurales durante cargas asíncronas (evitar pantallas en blanco y CLS).
   - Verificación de estados vacíos (*empty states*) descriptivos.
4. **Formularios y Prevención de Pérdida de Datos:**
   - Intento de salida o recarga con datos sin guardar (verificar alerta de confirmación por *dirty form*).
   - Recarga de página tras cierre forzoso (verificar recuperación automática del borrador local).
   - Limpieza automática del borrador tras envío exitoso.
5. **Seguridad, Control de Abusos y Casos Extremos:**
   - Prueba de clics repetitivos rápidos en botón de envío (comprobar debounce y deshabilitación inmediata).
   - Rate-limiting ante solicitudes masivas.
   - Envío de datos límite o malformados (rechazo limpio sin errores 500).
6. **Verificación de Dependencias:**
   - Comprobación de que no se hayan introducido paquetes obsoletos o con vulnerabilidades reportadas.

---

## 2. Estructura de `checklist.md`

Genera el archivo en la carpeta de la funcionalidad usando la estructura de tablas por área:

```markdown
# Lista de Comprobación y QA: <Nombre de la Funcionalidad / Subfase>

## Entornos de Prueba Requeridos
- [ ] Entorno local de desarrollo
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

## Pruebas de Seguridad, Control de Abusos y Casos Extremos
| ID | Entorno | Acción / Pasos a seguir | Resultado Esperado | Estado (`[ ]` / `[x]`) | Observaciones |

## Verificación de Dependencias y Scaffolding
| ID | Entorno | Acción / Pasos a seguir | Resultado Esperado | Estado (`[ ]` / `[x]`) | Observaciones |
```

---

## 3. Revisión Final

1. Verifica que todos los `CA-X` y `CE-X` de `spec.md` tengan su correspondiente prueba en la tabla.
2. Presenta el checklist al usuario confirmando los escenarios de resiliencia, skeletons y formularios incluidos.
3. Recuerda que este checklist será auditado por `close` antes de permitir el merge de la subfase.
