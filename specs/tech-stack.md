# Tech Stack

> **Estado:** Fase Inicial

## 1. Restricciones de plataforma que definen la arquitectura

### Plataforma Principal
{{JUSTIFICACION_DE_LA_PLATAFORMA}}

### Alternativas descartadas
{{POR_QUE_SE_DESCARTARON}}

## 2. Política de Dependencias y Versiones (Latest Stable Coexistentes)

> **Regla Crítica de IA:** Los modelos de lenguaje tienden a sugerir versiones atrasadas basadas en su fecha de corte de entrenamiento. 
> Antes de generar un scaffolding inicial o proponer dependencias en `package.json`, `pyproject.toml`, `Cargo.toml`, etc., la IA **debe auditar activamente las versiones más recientes y estables** (`latest stable` o LTS vigente) consultando el gestor de paquetes respectivo (`npm view <pkg> version`, `pip index versions <pkg>`, etc.).
> **Compatibilidad Cruzada:** Verificar siempre que las dependencias seleccionadas coexistan armónicamente sin romper librerías secundarias, peer dependencies o el motor de ejecución.

| Dependencia | Versión Auditada | Tipo (Core/Dev) | Verificación de Compatibilidad |
|---|---|---|---|
| `{{PAQUETE_1}}` | `latest-stable` | Core | Compatible con runtime y resto del stack |
| `{{PAQUETE_2}}` | `latest-stable` | Core/Dev | Sin conflictos de peer-dependencies |

## 3. Decisiones de Ingeniería Core

| Opción | Estado | Motivo |
|---|---|---|
| {{OPCION_A}} | ❌ Descartada | {{MOTIVO}} |
| {{OPCION_B}} | ✅ **Elegida** | {{MOTIVO}} |

### Configuración obligatoria

Las reglas innegociables de minimización de datos, privacidad, resiliencia y comportamiento pasivo están descritas en [`constitution.md`](constitution.md). Aquí se detallan los módulos técnicos elegidos.

### Sin backend / Backend Serverless

Regla estricta definida en [`constitution.md`](constitution.md). Solo se usa {{HERRAMIENTA_REMOTO}} para configuraciones remotas.

## 4. Arquitectura general y Patrones Transversales

```text
┌──────────────────────── Entorno ────────────────────────┐
│                                                         │
│                    {{DIAGRAMA_AQUI}}                    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Estrategia de conexión, Resiliencia y Reintentos Pasivos
- **Tolerancia a desconexiones:** {{DESCRIPCION_CACHE_LOCAL_O_OFFLINE}}
- **Reintentos Pasivos:** Reintentos en background con backoff exponencial y jitter para peticiones no idempotentes/idempotentes.
- **Flujo de datos:** {{DESCRIPCION_FLUJO}}

### Estrategia de UI: Skeletons y Estados de Carga
- **Indicadores y Skeletons:** {{LIBRERIA_O_COMPONENTE_SKELETONS}}
- **Empty States:** Componentes predefinidos para estados vacíos y feedback inmediato.

### Estrategia de Formularios y Protección de Pérdida de Datos
- **Detección de estado sucio (Dirty form):** Interceptor de navegación / `beforeunload`.
- **Persistencia de borradores:** Almacenamiento local temporal (`sessionStorage` o `localStorage`) con auto-guardado en cambios.

### Estrategia de Seguridad, Rate-Limiting y Abuso
- **Validación de esquemas:** {{LIBRERIA_VALIDACION}} (ej. Zod, Yup, Pydantic) tanto en cliente como en backend/servicios.
- **Control de Abuso y Doble Clic:** Debounce en botones de envío y rate-limiting en llamadas asíncronas sensibles.

## 5. Tecnologías Elegidas

| Área | Elección | Justificación |
|---|---|---|
| Lenguaje | **{{LENGUAJE}}** | {{JUSTIFICACION}} |
| UI | **{{FRAMEWORK_UI}}** | {{JUSTIFICACION}} |
| Arquitectura | **{{PATRON}}** | {{JUSTIFICACION}} |
| Inyección de dependencias | **{{LIBRERIA_DI}}** | {{JUSTIFICACION}} |
| Persistencia | **{{DB_LOCAL}}** | {{JUSTIFICACION}} |
| Validación de Esquemas | **{{LIBRERIA_VALIDACION}}** | Validación estricta en tiempo de ejecución |
| Manejo de Estado / Caché | **{{GESTOR_ESTADO_CACHE}}** | Con soporte de reintentos pasivos y cache offline |

### Estructura de Módulos (Propuesta)
```text
app/                      # Application, configuración, providers
core/model                # Entidades de dominio y esquemas de validación
core/data                 # Repositorios, persistencia local y offline fallback
core/network              # Cliente HTTP con reintentos pasivos y backoff
feature/xyz               # Funcionalidades aisladas
  ├── components/         # Vistas, Skeletons y componentes de UI
  ├── hooks/              # Lógica, gestión de borradores y debounce
  └── services/           # Llamadas a API o controladores
```

## 6. Calidad y entrega

| Área | Herramienta |
|---|---|
| Tests unitarios | {{TEST_FRAMEWORK}} |
| Tests de UI / Componentes | {{UI_TEST_FRAMEWORK}} |
| Lint / formato | {{LINTER}} |
| CI/CD | {{CI_CD}} |

## 7. Riesgos

| Riesgo | Impacto | Mitigación |
|---|---|---|
| {{RIESGO_1}} | Alto | {{MITIGACION_1}} |
| Caída de red o latencia extrema | Medio | Caché local, reintentos pasivos y feedback visual mediante Skeletons |
| Pérdida de datos en formularios | Medio | Borrador temporal persistido y confirmación de salida |
| Vulnerabilidad de paquetes obsoletos | Alto | Auditoría continua contra versiones `latest stable` en cada scaffolding |
