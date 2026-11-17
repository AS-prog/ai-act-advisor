#!/usr/bin/env python3
"""Punto de entrada de los hooks: hook.py session-start | post-tool-use.

Lee el JSON del evento por stdin. Nunca bloquea: ante cualquier error sale con 0
sin decir nada, para no estorbar el trabajo del usuario.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main():
    try:
        from aiact import hooks
        payload = json.load(sys.stdin) if not sys.stdin.isatty() else {}
        event = sys.argv[1] if len(sys.argv) > 1 else ""
        if event == "session-start":
            hooks.session_start(payload)
        elif event == "post-tool-use":
            hooks.post_tool_use(payload)
    except Exception as exc:  # noqa: BLE001
        if os.environ.get("AI_ACT_DEBUG"):
            raise
        print(f"ai-act-advisor: hook omitido ({type(exc).__name__})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
