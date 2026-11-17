#!/usr/bin/env python3
"""Ejecuta los evals de las citas con uno o varios modelos y lleva el historial.

  run.py ejecutar --modelos claude-haiku-5-5 claude-sonnet-5-5 --tag humo --runs 1
  run.py ejecutar --modelos claude-opus-5-5 --dry-run       # enseña el comando, no gasta
  run.py registrar resultado.json --modelo claude-opus-5-5  # añade una ejecución hecha a mano
  run.py historial                                          # comparativa por ejecución
  run.py historial --por-caso --tag humo                    # detalle por caso

«ejecutar» llama a `claude plugin eval` una vez por modelo, guarda el JSON
completo en evals/results/ (fuera de git) y añade una fila por ejecución a
evals/historial/ejecuciones.csv y una por caso a evals/historial/casos.csv
(versionados). El juez queda fijo entre modelos para que las notas se puedan
comparar. Solo librería estándar.
"""
import argparse
import csv
import datetime
import fnmatch
import hashlib
import json
import os
import shutil
import subprocess
import sys

EVALS = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.dirname(EVALS)
REPO = os.path.dirname(os.path.dirname(PLUGIN))
RESULTS = os.path.join(EVALS, "results")
HISTORIAL = os.path.join(EVALS, "historial")
SKILL = os.path.join(PLUGIN, "skills", "cite-regulation", "SKILL.md")

COLS_EJECUCION = [
    "fecha", "modelo", "juez", "filtro", "casos", "pasadas", "puntos_con", "puntos_sin", "delta",
    "aprobados_con", "aprobados_sin", "skill_activa", "nota_recuperada", "coste_usd", "duracion_s",
    "parcial", "commit", "skill_sha", "json",
]
COLS_CASO = ["fecha", "modelo", "caso", "puntos_con", "puntos_sin", "delta", "skill_activa", "nota_recuperada"]


# --- utilidades -------------------------------------------------------------
def _git(*args):
    try:
        return subprocess.run(["git", "-C", REPO, *args], capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def commit_actual():
    sha = _git("rev-parse", "--short", "HEAD")
    # Solo cuenta lo que cambia la respuesta de Claude, no los propios evals.
    sucio = _git("status", "--porcelain", "--", *("plugins/ai-act-advisor/" + d for d in ("skills", "scripts", "knowledge")))
    return sha + ("+cambios" if sha and sucio else "")


def skill_sha():
    try:
        with open(SKILL, "rb") as fh:
            return hashlib.sha256(fh.read()).hexdigest()[:10]
    except OSError:
        return ""


def _r(x, n=3):
    return "" if x is None else round(float(x), n)


def _fraccion(runs, grader):
    """Parte de las pasadas del brazo con plugin en que el grader aprobó (None si no existe)."""
    vistos = [g["passed"] for r in runs for g in r.get("graders", []) if g.get("name") == grader]
    return sum(vistos) / len(vistos) if vistos else None


def _media(valores):
    valores = [v for v in valores if v is not None]
    return sum(valores) / len(valores) if valores else None


# --- registrar --------------------------------------------------------------
def filas(resultado, modelo, ruta_json, commit=None, sha=None):
    """Convierte la salida JSON de `claude plugin eval` en una fila de ejecución y filas por caso."""
    fecha = (resultado.get("startedAt") or datetime.datetime.utcnow().isoformat())[:19]
    suite = resultado.get("suite", {})
    agg = resultado.get("aggregates", {})
    casos = []
    for c in resultado.get("cases", []):
        a = c.get("aggregates", {})
        con = c.get("arms", {}).get("with", [])
        casos.append({
            "fecha": fecha, "modelo": modelo, "caso": c.get("name"),
            "puntos_con": _r(a.get("score")), "puntos_sin": _r(a.get("scoreWithout")), "delta": _r(a.get("delta")),
            "skill_activa": _r(_fraccion(con, "usa-skill"), 2), "nota_recuperada": _r(_fraccion(con, "nota-recuperada"), 2),
        })
    aprobados_sin = _media([c.get("aggregates", {}).get("passRateWithout") for c in resultado.get("cases", [])])
    puntos_sin = _media([c.get("aggregates", {}).get("scoreWithout") for c in resultado.get("cases", [])])
    ejecucion = {
        "fecha": fecha, "modelo": modelo, "juez": suite.get("judgeModel", ""),
        "filtro": " ".join(suite.get("tagFilters") or []) or "todos",
        "casos": agg.get("casesTotal", len(casos)),
        "pasadas": max((len(c.get("arms", {}).get("with", [])) for c in resultado.get("cases", [])), default=0),
        "puntos_con": _r(agg.get("overallScore")), "puntos_sin": _r(puntos_sin), "delta": _r(agg.get("meanDelta")),
        "aprobados_con": _r(agg.get("overallPassRate")), "aprobados_sin": _r(aprobados_sin),
        "skill_activa": _r(_media([c["skill_activa"] for c in casos if c["skill_activa"] != ""]), 2),
        "nota_recuperada": _r(_media([c["nota_recuperada"] for c in casos if c["nota_recuperada"] != ""]), 2),
        "coste_usd": _r(resultado.get("costUsd"), 2), "duracion_s": resultado.get("durationSeconds", ""),
        "parcial": "sí" if resultado.get("partial") else "no",
        "commit": commit if commit is not None else commit_actual(),
        "skill_sha": sha if sha is not None else skill_sha(),
        "json": os.path.relpath(ruta_json, EVALS) if ruta_json else "",
    }
    return ejecucion, casos


def _append(nombre, cols, rows):
    os.makedirs(HISTORIAL, exist_ok=True)
    ruta = os.path.join(HISTORIAL, nombre)
    nuevo = not os.path.exists(ruta)
    with open(ruta, "a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        if nuevo:
            w.writeheader()
        w.writerows(rows)
    return ruta


def registrar(ruta_json, modelo):
    with open(ruta_json, encoding="utf-8") as fh:
        resultado = json.load(fh)
    ejecucion, casos = filas(resultado, modelo, ruta_json)
    _append("ejecuciones.csv", COLS_EJECUCION, [ejecucion])
    _append("casos.csv", COLS_CASO, casos)
    return ejecucion


# --- ejecutar ---------------------------------------------------------------
def comando(args, modelo, ruta_json):
    cmd = ["claude", "plugin", "eval", ".", "--model", modelo, "--judge-model", args.juez,
           "--allow-tools", "Bash", "--trust-plugin", "--json", ruta_json]
    if not args.publicar:
        cmd.append("--no-publish")
    for t in args.tag or []:
        cmd += ["--tag", t]
    if args.caso:
        cmd += ["--case", args.caso]
    if args.runs:
        cmd += ["--runs", str(args.runs)]
    if args.max_cost:
        cmd += ["--max-cost-usd", str(args.max_cost)]
    if args.concurrencia:
        cmd += ["-j", str(args.concurrencia)]
    return cmd


def ejecutar(args):
    if not args.dry_run and not shutil.which("claude"):
        print("No encuentro el comando «claude» en el PATH.")
        return 1
    os.makedirs(RESULTS, exist_ok=True)
    sello = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M")
    codigo = 0
    for modelo in args.modelos:
        ruta_json = os.path.join(RESULTS, "%s-%s.json" % (sello, modelo.replace("/", "_")))
        cmd = comando(args, modelo, ruta_json)
        print("\n== %s\n$ (cd %s) %s" % (modelo, os.path.relpath(PLUGIN, os.getcwd()), " ".join(cmd)), flush=True)
        if args.dry_run:
            continue
        proc = subprocess.run(cmd, cwd=PLUGIN)
        # 0: todo por encima del umbral; 1: algún caso por debajo; 2: tope de coste (resultado parcial).
        if not os.path.exists(ruta_json):
            print("Sin resultado para %s (código %s); no se registra." % (modelo, proc.returncode))
            codigo = 1
            continue
        if args.sin_registro:
            print("Resultado en %s (sin registrar)." % ruta_json)
            continue
        e = registrar(ruta_json, modelo)
        print("Registrado: con plugin %s · sin plugin %s · Δ %s · skill activa %s · %s USD" % (
            e["puntos_con"], e["puntos_sin"], e["delta"], e["skill_activa"], e["coste_usd"]))
    if not args.dry_run and not args.sin_registro:
        print()
        historial(argparse.Namespace(por_caso=False, modelo=None, tag=None, ultimas=len(args.modelos)))
    return codigo


# --- historial --------------------------------------------------------------
def _leer(nombre):
    ruta = os.path.join(HISTORIAL, nombre)
    if not os.path.exists(ruta):
        return []
    with open(ruta, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _tabla(rows, cols):
    anchos = [max(len(c), *(len(str(r.get(c, ""))) for r in rows)) for c in cols]
    linea = lambda vals: "  ".join(str(v).ljust(a) for v, a in zip(vals, anchos))  # noqa: E731
    print(linea(cols))
    print(linea(["-" * a for a in anchos]))
    for r in rows:
        print(linea([r.get(c, "") for c in cols]))


def historial(args):
    if args.por_caso:
        rows = _leer("casos.csv")
        if args.tag:
            # el filtro por etiqueta se resuelve con las ejecuciones que lo usaron
            fechas = {(e["fecha"], e["modelo"]) for e in _leer("ejecuciones.csv") if args.tag in e["filtro"].split()}
            rows = [r for r in rows if (r["fecha"], r["modelo"]) in fechas]
        cols = COLS_CASO
    else:
        rows = _leer("ejecuciones.csv")
        if args.tag:
            rows = [r for r in rows if args.tag in r["filtro"].split()]
        cols = ["fecha", "modelo", "juez", "filtro", "casos", "pasadas", "puntos_con", "puntos_sin", "delta",
                "skill_activa", "nota_recuperada", "coste_usd", "commit", "skill_sha"]
    if args.modelo:
        rows = [r for r in rows if fnmatch.fnmatch(r["modelo"], args.modelo)]
    if args.ultimas:
        claves = []
        for r in rows:
            k = (r["fecha"], r["modelo"])
            if k not in claves:
                claves.append(k)
        keep = set(claves[-args.ultimas:])
        rows = [r for r in rows if (r["fecha"], r["modelo"]) in keep]
    if not rows:
        print("Historial vacío. Lanza «run.py ejecutar --modelos …».")
        return 0
    _tabla(rows, cols)
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    e = sub.add_parser("ejecutar", help="lanza el eval con uno o varios modelos")
    e.add_argument("--modelos", nargs="+", required=True, help="ids de modelo, p. ej. claude-sonnet-5-5")
    e.add_argument("--tag", action="append", help="filtra casos por etiqueta (humo, cita, solo-ingles, negativo)")
    e.add_argument("--caso", help="filtra casos por nombre (glob)")
    e.add_argument("--runs", type=int, help="pasadas por caso (por defecto, las del case.yaml: 3)")
    e.add_argument("--juez", default="sonnet", help="modelo juez, fijo entre modelos (por defecto sonnet)")
    e.add_argument("--max-cost", type=float, help="tope de coste en USD por modelo")
    e.add_argument("-j", "--concurrencia", type=int, help="ejecuciones en paralelo (1-8)")
    e.add_argument("--publicar", action="store_true", help="publica el informe HTML en claude.ai")
    e.add_argument("--sin-registro", action="store_true", help="no añade nada al historial")
    e.add_argument("--dry-run", action="store_true", help="enseña los comandos sin ejecutarlos")

    r = sub.add_parser("registrar", help="añade al historial un JSON de una ejecución hecha a mano")
    r.add_argument("json")
    r.add_argument("--modelo", required=True)

    h = sub.add_parser("historial", help="enseña la comparativa")
    h.add_argument("--por-caso", action="store_true")
    h.add_argument("--modelo", help="filtra por modelo (glob)")
    h.add_argument("--tag", help="solo ejecuciones con esta etiqueta")
    h.add_argument("--ultimas", type=int, help="solo las N últimas ejecuciones")

    args = ap.parse_args(argv)
    if args.cmd == "ejecutar":
        return ejecutar(args)
    if args.cmd == "registrar":
        e = registrar(args.json, args.modelo)
        print("Registrado %s %s en %s" % (e["fecha"], e["modelo"], os.path.relpath(HISTORIAL, os.getcwd())))
        return 0
    return historial(args)


if __name__ == "__main__":
    sys.exit(main())
