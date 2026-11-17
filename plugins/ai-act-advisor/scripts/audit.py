#!/usr/bin/env python3
"""Auditoría de entornos y riesgos AI Act/RGPD de un repo (solo lectura).

  audit.py scan  --root RUTA            muestra el resultado en JSON (no escribe nada)
  audit.py write --root RUTA [--out D]  escribe .ai-act/rules.json, baseline.json y audits/AAAA-MM-DD.md
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aiact import core  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["scan", "write", "report"])
    ap.add_argument("--root", default=".")
    ap.add_argument("--out", default=None, help="carpeta de estado (por defecto .ai-act)")
    args = ap.parse_args(argv)
    result = core.audit(args.root)
    if args.command == "scan":
        json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
        print()
    elif args.command == "report":
        print(core.render_report(result))
    else:
        paths = core.write_outputs(args.root, result, args.out)
        json.dump({"written": paths, "findings": len(result["findings"])}, sys.stdout, ensure_ascii=False, indent=2)
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
