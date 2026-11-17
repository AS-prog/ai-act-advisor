"""Hooks del plugin. Solo añaden contexto: nunca deniegan ni bloquean."""

import datetime as _dt
import json
import os
import re
import tempfile

from . import core, miniyaml

FINGERPRINT_FILES = {
    "pyproject.toml", "requirements.txt", "requirements-dev.txt", "environment.yml",
    "dbt_project.yml", "profiles.yml", "databricks.yml", "package.json", "azure-pipelines.yml",
}
WATCH_EXT = {".py", ".sql", ".yml", ".yaml", ".ipynb", ".toml"}
DISCLAIMER = "No es asesoramiento legal."


# Nombres de herramienta que escriben, por agente: Claude Code, Copilot, Codex y Gemini CLI.
WRITE_TOOLS = {"Edit", "Write", "MultiEdit", "NotebookEdit", "edit", "create", "str_replace_editor",
               "apply_patch", "write_file", "replace"}


def _project_root(payload):
    return (os.environ.get("CLAUDE_PROJECT_DIR") or os.environ.get("GEMINI_PROJECT_DIR")
            or payload.get("cwd") or os.getcwd())


def _emit(event, text, payload=None):
    """Añade contexto con el formato del agente que lanzó el hook.

    Claude Code, Gemini CLI y Codex leen hookSpecificOutput.additionalContext y mandan
    hook_event_name en PascalCase. Copilot (CLI y VS Code) lee additionalContext y Cursor
    additional_context, ambos en el primer nivel: si el evento no es de los primeros, van los tres.
    """
    if not text:
        return
    name = (payload or {}).get("hook_event_name") or ""
    out = {"hookSpecificOutput": {"hookEventName": name or event, "additionalContext": text}}
    if not name[:1].isupper():
        out.update({"additionalContext": text, "additional_context": text})
    print(json.dumps(out, ensure_ascii=False))


def _tool_and_path(payload):
    """Herramienta y fichero del evento, con los nombres de campo de cada agente."""
    tool = payload.get("tool_name") or payload.get("toolName") or ""
    args = payload.get("tool_input") or payload.get("toolArgs") or {}
    if isinstance(args, str):  # Copilot CLI manda los argumentos como texto JSON
        try:
            args = json.loads(args)
        except ValueError:
            args = {}
    if not isinstance(args, dict):
        args = {}
    path = (args.get("file_path") or args.get("notebook_path") or args.get("absolute_path")
            or args.get("path") or payload.get("file_path"))
    if not path:  # Codex edita con apply_patch: el fichero va dentro del parche
        patch = args.get("command") or args.get("input") or args.get("patch") or ""
        if isinstance(patch, list):
            patch = "\n".join(map(str, patch))
        m = re.search(r"^\*\*\* (?:Update|Add) File: (.+)$", str(patch), re.M)
        if m:
            path = m.group(1).strip()
            if not os.path.isabs(path):
                path = os.path.join(_project_root(payload), path)
    return tool, path


def _state_path(session_id):
    d = os.path.join(tempfile.gettempdir(), "ai-act-advisor")
    os.makedirs(d, exist_ok=True)
    safe = re.sub(r"[^A-Za-z0-9_-]", "_", session_id or "default")
    return os.path.join(d, f"{safe}.json")


def _base_line(version):
    return f"Base normativa {version.get('consolidado_ai_act', '?')} (revisada {version.get('ultima_revision', '?')}). {DISCLAIMER}"


# ---------------------------------------------------------------- SessionStart

def session_start(payload):
    root = _project_root(payload)
    state = os.path.join(root, core.STATE_DIR)
    _signals, version = core.load_knowledge()
    msgs = []

    profile_path = os.path.join(state, "profile.yaml")
    if not os.path.exists(profile_path):
        msgs.append(
            "ai-act-advisor: este repo no tiene perfil AI Act/RGPD (.ai-act/profile.yaml). "
            "Si el usuario trabaja con datos personales o modelos, sugiere una vez lanzar /project-init "
            "(configura el proyecto y, si ya está encaminado, hace una auditoría de riesgos de solo lectura)."
        )
    else:
        p = miniyaml.load(profile_path) or {}
        client = p.get("client") or {}
        cls = p.get("classification") or {}
        stack = p.get("stack") or {}
        msgs.append(
            "ai-act-advisor: perfil del proyecto · sector "
            f"{client.get('sector', '?')} · clasificación AI Act {cls.get('ai_act_level', '?')} · "
            f"datos personales {', '.join(map(str, p.get('personal_data') or [])) or 'sin declarar'}."
        )
        if isinstance(stack, dict) and stack.get("status") == "declarado":
            msgs.append("El stack está declarado pero no auditado: cuando haya código, sugiere relanzar /project-init.")
        base = core.load_json(os.path.join(state, "baseline.json"), {}).get("findings", {})
        open_high = [f for f in base.values() if f.get("status") == "abierto" and f.get("severity") == "alta"]
        if open_high:
            msgs.append(f"Línea base: {len(open_high)} hallazgos de severidad alta abiertos "
                        "(ver .ai-act/audits/). No los repitas salvo que el usuario trabaje en ellos.")

    rev = version.get("ultima_revision")
    try:
        age = (_dt.date.today() - _dt.date.fromisoformat(str(rev))).days
    except ValueError:
        age = None
    if age is not None and age > 90:
        msgs.append(f"La base normativa del plugin tiene {age} días: conviene lanzar /regulatory-update.")
    _emit("SessionStart", "\n".join(msgs), payload)


# ---------------------------------------------------------------- PostToolUse

def _rel(root, path):
    try:
        rel = os.path.relpath(os.path.abspath(path), os.path.abspath(root))
    except ValueError:
        return None
    if rel.startswith(".."):
        return None
    return rel.replace(os.sep, "/")


def post_tool_use(payload):
    tool, path = _tool_and_path(payload)
    if not path:
        return
    root = _project_root(payload)
    rel = _rel(root, path)
    if not rel or rel.startswith(core.STATE_DIR + "/"):
        return
    base = os.path.basename(rel)
    ext = os.path.splitext(base)[1]
    if ext not in WATCH_EXT and base not in FINGERPRINT_FILES:
        return
    full = os.path.join(root, rel)
    text = core.read_text(full)
    if text is None:
        return

    signals, version = core.load_knowledge()
    state_dir = os.path.join(root, core.STATE_DIR)
    rules = core.load_json(os.path.join(state_dir, "rules.json"), None)
    baseline = core.load_json(os.path.join(state_dir, "baseline.json"), {}).get("findings", {})
    exclusions = (rules or {}).get("exclusions") or signals.get("exclusions", [])
    writing = tool in WRITE_TOOLS

    findings = []
    notes = []
    is_source = False
    if rules:
        pii_key = rules.get("pii_key", "pii_columns")
        if rel in rules.get("source_configs", []) or core.is_source_config(rel, text, pii_key if rules.get("pii_key_detected") else None):
            is_source = True
            findings += core.check_source_config(rel, text, pii_key)
        if ext == ".py" and not core.is_test(rel):
            if rel in rules.get("bronze_writers", []) or "bronze" in rel.lower():
                findings += core.check_schema_merge(rel, text)
            findings += core.check_export(rel, text, signals) if (
                rel in rules.get("exports", []) or core.import_regex(signals.get("export_imports", [])).search(text)
            ) else []
        if writing and base in FINGERPRINT_FILES:
            files = [(rel, text)]
            envs = core.detect_environments(files, signals)
            new = [e["name"] for e in envs if e["name"] not in rules.get("environments", [])]
            if new:
                notes.append(
                    f"ai-act-advisor: en `{rel}` aparecen entornos que la auditoría no tenía "
                    f"({', '.join(new)}). Sugiere al PM relanzar /project-init para actualizar las reglas."
                )
    if ext in (".py", ".ipynb") and not core.is_test(rel):
        findings += core.check_llm(rel, text, signals)
        findings += core.check_scoring(rel, text, signals)
    if ext in core.CODE_EXT and not core.is_test(rel) and not is_source:
        findings += core.check_terms(rel, text, signals, exclusions)

    findings = [f for f in findings if f["id"] not in baseline]
    seen_path = _state_path(payload.get("session_id") or payload.get("sessionId"))
    seen = set(core.load_json(seen_path, []))
    fresh = [f for f in findings if f["id"] not in seen]
    if not fresh and not notes:
        return
    seen.update(f["id"] for f in fresh)
    try:
        with open(seen_path, "w", encoding="utf-8") as fh:
            json.dump(sorted(seen), fh)
    except OSError:
        pass

    lines = []
    if fresh:
        lines.append(
            f"ai-act-advisor: señales de riesgo en `{rel}` (no están en la línea base del proyecto). "
            "Cuéntaselo al usuario en pocas líneas cuando encaje con lo que está haciendo; no bloquees "
            "su trabajo: la decisión es suya. Si quiere detalle, carga la skill indicada."
        )
        for f in fresh[:4]:
            esc = f" · escalar a {f['escalate'].upper()}" if f.get("escalate") else ""
            det = f" ({f['detail']})" if f.get("detail") and f["rule"].endswith("terms") else ""
            lines.append(
                f"- [{f['severity']}] {f['title']}{det} · {f['norma']} {', '.join(f['articulos'])} · "
                f"aplica {f['aplica']}{esc} · skill {f['skill']} · id {f['id']}\n"
                f"  Opción sugerida: {f['recommendation']}"
            )
        if len(fresh) > 4:
            lines.append(f"- … y {len(fresh) - 4} más del mismo fichero.")
        lines.append(_base_line(version))
        if not rules:
            lines.append("El repo no tiene reglas propias (.ai-act/rules.json): sugiere una vez /project-init.")
    lines += notes
    _emit("PostToolUse", "\n".join(lines), payload)
