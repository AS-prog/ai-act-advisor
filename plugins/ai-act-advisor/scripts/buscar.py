#!/usr/bin/env python3
"""Busca y cita en las notas normativas (prototipo de D21, solo lectura).

  buscar.py articulo rgpd 9.1                 trae la nota y la línea del apartado
  buscar.py articulo ai-act "anexo III 5.b"
  buscar.py citas -q "avisar de que habla con un chatbot" \\
                  -q "informar de que están interactuando con un sistema de IA" \\
                  --en "inform users they are interacting with an AI system"

La salida de texto empieza por la carpeta de las notas, para abrir el pasaje.
«citas» devuelve dos listas: normas que pueden ser la cita y guías que la
apoyan. Cada -q busca en las notas en español y cada --en en las notas en
inglés (directrices del art. 6 en borrador y del CEPD). Quien llama (Claude)
pasa la pregunta tal cual, la misma pregunta con el vocabulario de la norma y
su traducción al inglés.

Opciones: --notas DIR (o AIACT_NOTAS), -k N, --json.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from aiact import notas  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--notas", default=None)
    ap.add_argument("--json", action="store_true")
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("articulo")
    a.add_argument("norma", choices=["ai-act", "rgpd", "lopdgdd", "omnibus"])
    a.add_argument("ref")
    c = sub.add_parser("citas")
    c.add_argument("-q", "--es", dest="es", action="append", default=[], help="consulta en español")
    c.add_argument("--en", action="append", default=[], help="consulta en inglés")
    c.add_argument("-k", type=int, default=3)
    args = ap.parse_args(argv)

    try:
        indice = notas.Indice(args.notas)
    except FileNotFoundError as e:
        print(e)
        return 1
    if args.cmd == "articulo":
        r = indice.articulo(args.norma, args.ref)
        if args.json:
            print(json.dumps(r, ensure_ascii=False, indent=2))
        elif r is None:
            print("Sin nota para %s %s" % (args.norma, args.ref))
            return 1
        else:
            print("Notas en %s" % indice.dir)
            print("%s · %s — %s · %s:L%s" % (args.norma, r["unidad"], r["titulo"], r["ruta"], r["linea"]))
        return 0

    consultas = [(q, "es") for q in args.es] + [(q, "en") for q in args.en]
    if not consultas:
        ap.error("citas necesita al menos un -q o un --en")
    res = indice.citas(consultas, k=args.k)
    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0
    print("Notas en %s" % indice.dir)
    for titulo, clave in (("Normas (cita)", "normas"), ("Guías (apoyo)", "guias")):
        print(titulo)
        for r in res[clave]:
            print("  %s  [%s]  %s:L%s\n      %s" % (r["nota"], r["idioma"], r["ruta"], r["linea"], r["descripcion"][:140]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
