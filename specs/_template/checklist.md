# Lista de Comprobación y QA: [Nombre de la Funcionalidad / Subfase]

## Entornos de Prueba Requeridos
- [ ] Entorno local de desarrollo (CLI / Dev Server)
- [ ] Navegador web (Chrome / Firefox / Safari) con DevTools (Throttling de red y emulación offline)
- [ ] Suite de pruebas automatizadas (Tests unitarios y de integración)

---

## Casos de Prueba (Criterios de Aceptación)

| ID | Entorno | Acción / Pasos a seguir | Resultado Esperado | Estado (`[ ]` / `[x]`) | Observaciones |
|---|---|---|---|---|---|
| CA-1 | Local / Web | 1. Ejecutar el flujo funcional principal con datos válidos | El flujo se completa satisfactoriamente y persiste los datos | [ ] | |
| CA-2 | Local / Web | 2. Ejecutar validaciones de negocio esperadas | Muestra mensajes correctos y restringe acciones inválidas | [ ] | |

---

## Pruebas de Resiliencia, Red y Tolerancia a Desconexiones

| ID | Entorno | Acción / Pasos a seguir | Resultado Esperado | Estado (`[ ]` / `[x]`) | Observaciones |
|---|---|---|---|---|---|
| QA-RED-1 | DevTools (Offline) | 1. Iniciar acción o navegación con la red desconectada | La app no crashea, informa con honestidad y degrada limpiamente o usa caché local | [ ] | |
| QA-RED-2 | DevTools (Slow 3G) | 2. Forzar latencia alta en llamadas a servicios | Los reintentos pasivos se ejecutan en background sin bloquear la navegación del usuario | [ ] | |
| QA-RED-3 | DevTools (Reconexión) | 3. Desconectar la red, reintentar y volver a conectar | Se reanuda la sincronización automáticamente sin pérdida de estado | [ ] | |

---

## Pruebas de UX, Skeletons y Estados de Carga

| ID | Entorno | Acción / Pasos a seguir | Resultado Esperado | Estado (`[ ]` / `[x]`) | Observaciones |
|---|---|---|---|---|---|
| QA-UX-1 | DevTools (Fast 3G) | 1. Recargar una vista que consume datos asíncronos | Se visualizan Skeletons acordes a la forma del contenido; no hay pantallas en blanco ni parpadeos bruscos | [ ] | |
| QA-UX-2 | Local / Web | 2. Cargar una vista cuando la colección de datos está vacía | Se visualiza un Empty State ilustrativo y descriptivo con llamada a la acción clara | [ ] | |

---

## Pruebas de Formularios y Protección contra Pérdida de Datos

| ID | Entorno | Acción / Pasos a seguir | Resultado Esperado | Estado (`[ ]` / `[x]`) | Observaciones |
|---|---|---|---|---|---|
| QA-FORM-1 | Local / Web | 1. Llenar campos de un formulario y cerrar la pestaña o recargar | El navegador muestra advertencia de confirmación por cambios sin guardar (*dirty form*) | [ ] | |
| QA-FORM-2 | Local / Web | 2. Recargar o volver a la vista tras salir abruptamente | Los datos previamente ingresados se recuperan automáticamente desde el borrador local | [ ] | |
| QA-FORM-3 | Local / Web | 3. Enviar exitosamente el formulario | El borrador temporal se limpia automáticamente | [ ] | |

---

## Pruebas de Seguridad, Control de Abusos y Escenarios "¿Qué pasaría si...?"

| ID | Entorno | Acción / Pasos a seguir | Resultado Esperado | Estado (`[ ]` / `[x]`) | Observaciones |
|---|---|---|---|---|---|
| QA-SEG-1 | Local / Web | 1. Hacer doble clic rápido o clics repetitivos en el botón de submit | El botón se deshabilita de inmediato y se procesa una única solicitud (debounce activo) | [ ] | |
| QA-SEG-2 | Local / API | 2. Enviar solicitudes repetidas por encima del umbral permitido | El sistema activa el rate-limiting y devuelve respuesta 429 limpia con tiempo de espera | [ ] | |
| QA-CE-1 | Local / Web | 3. Introducir caracteres especiales, scripts o payloads gigantes | Los esquemas de validación rechazan la entrada limpiamente sin inyecciones ni errores 500 | [ ] | |
| QA-CE-2 | Local / Simulación | 4. Simular respuesta de error 500 o timeout de 30s del servidor | La app no queda congelada con spinner infinito; muestra pantalla degradada con botón de reintento | [ ] | |
| QA-CE-3 | Local / Simulación | 5. Simular expiración de sesión/token antes de enviar | El borrador de datos no se pierde; se renueva token o solicita re-login y permite continuar | [ ] | |

---

## Verificación de Dependencias y Scaffolding

| ID | Entorno | Acción / Pasos a seguir | Resultado Esperado | Estado (`[ ]` / `[x]`) | Observaciones |
|---|---|---|---|---|---|
| QA-DEP-1 | CLI | 1. Ejecutar auditoría de dependencias (`npm audit` o equivalente) | Cero vulnerabilidades críticas o altas; dependencias en versiones estables | [ ] | |
