#!/usr/bin/env python3
"""Prepara la demo de ai-act-advisor en una carpeta de trabajo, fuera de este repo.

  preparar.py [--dest DIR]               fase 1: copia examples/medallion-demo y hace git init
  preparar.py --fase 2 [--dest DIR]      fase 2: añade el modelo de impago, el asistente y la encuesta
  preparar.py --base-antigua [--dest D]  copia la base normativa con fecha de hace 120 días

Solo librería estándar. No toca este repo: todo se escribe en DIR (por defecto, una carpeta
«ai-act-demo» en el directorio temporal del sistema).
"""
import argparse
import datetime as _dt
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
EXAMPLE = os.path.join(REPO, "examples", "medallion-demo")
PHASE2 = os.path.join(HERE, "fase-2")
PLUGIN = os.path.join(REPO, "plugins", "ai-act-advisor")
DEFAULT_DEST = os.path.join(tempfile.gettempdir(), "ai-act-demo")


def phase2_files():
    """Ficheros de la fase 2, como rutas relativas a la raíz del proyecto de la demo."""
    out = []
    for dirpath, _dirs, files in os.walk(PHASE2):
        for name in files:
            out.append(os.path.relpath(os.path.join(dirpath, name), PHASE2).replace(os.sep, "/"))
    return sorted(out)


def _git(dest, *args):
    if shutil.which("git") is None:
        return False
    env = dict(os.environ, GIT_AUTHOR_NAME="demo", GIT_AUTHOR_EMAIL="demo@example.invalid",
               GIT_COMMITTER_NAME="demo", GIT_COMMITTER_EMAIL="demo@example.invalid")
    return subprocess.run(["git", *args], cwd=dest, env=env, capture_output=True).returncode == 0


def phase1(dest, force=False):
    if os.path.exists(dest):
        if not force:
            raise SystemExit(f"{dest} ya existe. Bórralo o usa --force para empezar de cero.")
        shutil.rmtree(dest)
    shutil.copytree(EXAMPLE, dest, ignore=shutil.ignore_patterns("__pycache__", ".ai-act"))
    if _git(dest, "init", "-q"):
        _git(dest, "add", "-A")
        _git(dest, "commit", "-qm", "Fase 1: medallion de clientes")
    return dest


def phase2(dest):
    if not os.path.isdir(dest):
        raise SystemExit(f"{dest} no existe. Prepara antes la fase 1.")
    copied = []
    for rel in phase2_files():
        target = os.path.join(dest, rel)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        shutil.copy(os.path.join(PHASE2, rel), target)
        copied.append(rel)
    return copied


def old_knowledge(dest, days=120):
    """Copia knowledge/ junto a DEST (no dentro: la auditoría la leería) con la revisión atrasada."""
    target = dest.rstrip("/\\") + "-base-antigua"
    if os.path.exists(target):
        shutil.rmtree(target)
    shutil.copytree(os.path.join(PLUGIN, "knowledge"), target)
    old = (_dt.date.today() - _dt.timedelta(days=days)).isoformat()
    path = os.path.join(target, "VERSION")
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    lines = [f"ultima_revision: {old}" if ln.startswith("ultima_revision:") else ln for ln in lines]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    return target


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dest", default=DEFAULT_DEST, help=f"carpeta de trabajo (por defecto {DEFAULT_DEST})")
    ap.add_argument("--fase", type=int, choices=[1, 2], default=1)
    ap.add_argument("--force", action="store_true", help="en la fase 1, borra DEST si ya existe")
    ap.add_argument("--base-antigua", action="store_true", help="prepara una base normativa de hace 120 días")
    args = ap.parse_args(argv)
    dest = os.path.abspath(args.dest)

    if args.base_antigua:
        target = old_knowledge(dest)
        print(f"Base normativa atrasada en {target}\n")
        print("Abre una sesión con ella para ver el aviso de base antigua:\n")
        print(f'  cd "{dest}"')
        print(f'  AI_ACT_KNOWLEDGE="{target}" claude --plugin-dir "{PLUGIN}"')
        return 0

    if args.fase == 1:
        phase1(dest, args.force)
        print(f"Fase 1 lista en {dest}\n")
        print("Abre Claude Code con el plugin de esta rama:\n")
        print(f'  cd "{dest}"')
        print(f'  claude --plugin-dir "{PLUGIN}"')
        print("\nY sigue el guion desde el paso 1 (docs/site/guia/demo.html).")
    else:
        copied = phase2(dest)
        print(f"Fase 2 aplicada en {dest}:\n")
        for rel in copied:
            print(f"  {rel}")
        print("\nLas dependencias nuevas (scikit-learn y anthropic) no se copian: en el paso 8 se las")
        print("pides a Claude, para que el aviso de entornos nuevos salga al editar pyproject.toml.")
        print("Vuelve a la sesión de Claude Code y sigue el guion desde la fase 2.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
