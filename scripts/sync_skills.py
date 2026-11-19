import os
import shutil
import sys

"""
Script de sincronización multi-harness para SDD (Spec-Driven Development).
Mantiene sincronizadas las carpetas de skills entre:
- .claude/skills/ (Claude Code)
- .agents/skills/ (Google Antigravity, OpenAI Codex, Cursor)
"""

CLAUDE_SKILLS_DIR = os.path.join(".claude", "skills")
AGENTS_SKILLS_DIR = os.path.join(".agents", "skills")

def sync_skills(source=CLAUDE_SKILLS_DIR, target=AGENTS_SKILLS_DIR):
    if not os.path.exists(source):
        print(f"Error: Directorio origen no encontrado: {source}")
        return False

    os.makedirs(target, exist_ok=True)
    synced_count = 0

    for item in os.listdir(source):
        src_item = os.path.join(source, item)
        tgt_item = os.path.join(target, item)

        if os.path.isdir(src_item):
            # Copiar árbol de directorio de la skill
            if os.path.exists(tgt_item):
                shutil.rmtree(tgt_item)
            shutil.copytree(src_item, tgt_item)
            synced_count += 1
            print(f"  [✓] Sincronizada skill: {item} -> {target}")

    print(f"\nSincronización completada: {synced_count} skills sincronizadas en {target}.")
    return True

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "claude_to_agents"
    if mode == "agents_to_claude":
        sync_skills(AGENTS_SKILLS_DIR, CLAUDE_SKILLS_DIR)
    else:
        sync_skills(CLAUDE_SKILLS_DIR, AGENTS_SKILLS_DIR)
