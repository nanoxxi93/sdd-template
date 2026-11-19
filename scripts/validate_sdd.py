import os
import sys
import re

FEATURE_FOLDER_REGEX = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9-]+$")

REQUIRED_SECTIONS = {
    "spec.md": [
        "## Resumen",
        "## Criterios de aceptación"
    ],
    "plan.md": [
        "## Información general sobre la arquitectura",
        "## Comprobación de la Constitución"
    ],
    "tasks.md": [
        "## Fase "
    ],
    "checklist.md": [
        "## Casos de Prueba"
    ]
}

def validate_harness_compatibility():
    """Valida la compatibilidad multi-harness (Antigravity, Codex, Claude)."""
    has_errors = False
    print("Validando compatibilidad multi-harness (Antigravity / Codex / Claude)...")

    # Archivos maestros requeridos
    required_root_files = ["AGENTS.md", "CLAUDE.md", "GEMINI.md"]
    for rf in required_root_files:
        if not os.path.exists(rf):
            print(f"  [X] Falta archivo de instrucciones maestro: {rf}")
            has_errors = True
        else:
            print(f"  [✓] {rf} presente")

    # Carpetas de skills
    claude_dir = os.path.join(".claude", "skills")
    agents_dir = os.path.join(".agents", "skills")

    claude_skills = set(os.listdir(claude_dir)) if os.path.exists(claude_dir) else set()
    agents_skills = set(os.listdir(agents_dir)) if os.path.exists(agents_dir) else set()

    if not claude_skills:
        print(f"  [X] Falta directorio o skills en {claude_dir}")
        has_errors = True
    if not agents_skills:
        print(f"  [X] Falta directorio o skills en {agents_dir} (Requerido para Antigravity y Codex)")
        has_errors = True

    if claude_skills and agents_skills:
        diff = claude_skills.symmetric_difference(agents_skills)
        if diff:
            print(f"  [!] Advertencia: Desincronización de skills detectada: {diff}. Ejecuta 'python scripts/sync_skills.py'.")
            has_errors = True
        else:
            print(f"  [✓] Skills sincronizadas entre {claude_dir} y {agents_dir} ({len(claude_skills)} skills)")

    return not has_errors

def validate_specs():
    if not validate_harness_compatibility():
        print("\nAdvertencia en compatibilidad multi-harness. Revisa los mensajes arriba.")

    specs_dir = "specs"
    if not os.path.exists(specs_dir):
        print(f"Error: No se encontró el directorio '{specs_dir}'")
        sys.exit(1)

    has_errors = False
    feature_count = 0

    # Iterar sobre las carpetas dentro de specs/
    for item in sorted(os.listdir(specs_dir)):
        item_path = os.path.join(specs_dir, item)
        if not os.path.isdir(item_path):
            continue

        # Ignorar carpetas especiales de plantilla o internas
        if item.startswith("_") or item.startswith("."):
            continue

        feature_count += 1
        print(f"\nValidando especificación de funcionalidad: {item}")

        # 1. Validar convención de nomenclatura (AAAA-MM-DD-nombre-en-kebab)
        if not FEATURE_FOLDER_REGEX.match(item):
            print(f"  [X] Error de formato en carpeta '{item}': Debe seguir 'AAAA-MM-DD-nombre-en-kebab'")
            has_errors = True

        # 2. Validar existencia y tamaño de los 4 artefactos obligatorios
        required_files = {
            "spec.md": os.path.join(item_path, "spec.md"),
            "plan.md": os.path.join(item_path, "plan.md"),
            "tasks.md": os.path.join(item_path, "tasks.md"),
            "checklist.md": os.path.join(item_path, "checklist.md")
        }

        for file_name, file_path in required_files.items():
            if not os.path.exists(file_path):
                print(f"  [X] Falta archivo obligatorio: {file_name}")
                has_errors = True
                continue

            size = os.path.getsize(file_path)
            if size < 50:
                print(f"  [X] El archivo {file_name} está vacío o incompleto (< 50 bytes)")
                has_errors = True
                continue

            # 3. Validar secciones mínimas obligatorias
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                missing_sections = []
                for section in REQUIRED_SECTIONS.get(file_name, []):
                    if section not in content:
                        missing_sections.append(section)

                if missing_sections:
                    print(f"  [X] En {file_name} faltan secciones obligatorias: {', '.join(missing_sections)}")
                    has_errors = True
                else:
                    print(f"  [✓] {file_name} verificado correctamente")

                # Comprobación de calidad: Grupos lógicos en tasks.md
                if file_name == "tasks.md" and "### Grupo " not in content:
                    print("  [!] Recomendación: En tasks.md no se detectaron '### Grupo '. Organiza las tareas en grupos lógicos para facilitar revisiones y commits parciales.")
            except Exception as e:
                print(f"  [X] Error leyendo {file_name}: {e}")
                has_errors = True

    if feature_count == 0:
        print("\nNo se encontraron carpetas de funcionalidades en specs/ (solo documentación base y plantillas).")
        print("Estructura de specs válida.")
        return

    if has_errors:
        print("\nValidación de Especificaciones SDD: FALLIDA. Corrige los errores arriba para continuar.")
        sys.exit(1)
    else:
        print(f"\nValidación de Especificaciones SDD: EXITOSA ({feature_count} funcionalidades auditadas).")

if __name__ == "__main__":
    validate_specs()
