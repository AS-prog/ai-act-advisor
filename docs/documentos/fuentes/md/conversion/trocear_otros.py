#!/usr/bin/env python3
"""Notas con front matter para lo que no es norma ni PDF: la sentencia TJUE C-184/20
(XHTML) y los checklists y ejemplos de AESIA (zip de Excel).

Requiere pandoc, beautifulsoup4 (flatten.py) y openpyxl. Escribe en plugins/ai-act-advisor/knowledge/notas/.
Uso: python3 -I trocear_otros.py
"""
import re
import shutil
import subprocess
import tempfile
import unicodedata
import zipfile
from pathlib import Path

import openpyxl

AQUI = Path(__file__).resolve().parent
FUENTES = AQUI.parent.parent
# Las notas viajan con el plugin (D21): plugins/ai-act-advisor/knowledge/notas/.
SALIDA = FUENTES.parents[2] / "plugins" / "ai-act-advisor" / "knowledge" / "notas"
SENTENCIA = FUENTES / "2022-08-01-tjue-c-184-20-sentencia-es.xhtml"
ZIP = FUENTES / "2026-07-30-aesia-checklists-y-ejemplos.zip"
CABECERAS = ["Marco jurídico", "Litigio principal y cuestiones prejudiciales",
             "Sobre la admisibilidad de la petición de decisión prejudicial",
             "Sobre las cuestiones prejudiciales", "Primera cuestión prejudicial",
             "Segunda cuestión prejudicial", "Costas"]
OMITIR_HOJA = re.compile(r"^(TO_DO|Portada|Control de|Intro|helper|Leyenda)", re.I)


def slug(t, n=50):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:n].strip("-")


def front(nombre, desc, meta):
    desc = desc.replace('"', "'")
    lineas = ["---", f"name: {nombre}", f'description: "{desc}"', "metadata:", "  type: reference"]
    lineas += [f'  {k}: "{str(v).replace(chr(34), chr(39))}"' for k, v in meta.items()]
    return "\n".join(lineas + ["  oficial: false", "---", ""])


def sentencia():
    carpeta = SALIDA / "tjue-c-184-20-sentencia"
    shutil.rmtree(carpeta, ignore_errors=True)
    carpeta.mkdir(parents=True)
    with tempfile.TemporaryDirectory() as tmp:
        plano = Path(tmp) / "s.html"
        subprocess.run(["python3", "-I", str(AQUI / "flatten.py"), str(SENTENCIA), str(plano)], check=True)
        md = subprocess.run(["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none", str(plano)],
                            capture_output=True, text=True, check=True).stdout
    lineas = md.splitlines()
    cortes = [(0, "Encabezamiento")]
    for i, l in enumerate(lineas):
        if l.strip() in CABECERAS:
            cortes.append((i, l.strip()))
    cortes.append((len(lineas), None))
    n = 0
    for (a, t), (b, _) in zip(cortes, cortes[1:]):
        cuerpo = re.sub(r"\n{3,}", "\n\n", "\n".join(lineas[a:b])).strip()
        n += 1
        nombre = f"tjue-c-184-20-{n:02d}-{slug(t)}"
        desc = (f"TJUE, sentencia de 2022-08-01, asunto C-184/20 (OT y Vyriausioji tarnybinės etikos komisija), "
                f"sección «{t}». Datos personales, categorías especiales (art. 9 RGPD) y datos que revelan indirectamente información sensible.")
        (carpeta / f"{nombre}.md").write_text(
            front(nombre, desc, dict(documento="tjue-c-184-20-sentencia", emisor="TJUE",
                                     fecha="2022-08-01", idioma="es", seccion=t,
                                     origen=SENTENCIA.name)) + f"# {t}\n\n{cuerpo}\n", encoding="utf-8")
    return n


def celda(v):
    return re.sub(r"\s+", " ", str(v)).replace("|", "\\|").strip()


def hoja_a_md(ws):
    filas = [[c for c in fila] for fila in ws.iter_rows(values_only=True)]
    filas = [f for f in filas if any(c is not None and str(c).strip() for c in f)]
    if len(filas) < 2:
        return None
    ancho = max(i for f in filas for i, c in enumerate(f) if c is not None and str(c).strip()) + 1
    usadas = [j for j in range(ancho) if any(j < len(f) and f[j] is not None and str(f[j]).strip() for f in filas)]
    filas = [[celda(f[j]) if j < len(f) and f[j] is not None else "" for j in usadas] for f in filas]
    cab, resto = filas[0], filas[1:]
    out = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    out += ["| " + " | ".join(f) + " |" for f in resto]
    return "\n".join(out), len(resto)


def checklists():
    n = 0
    with tempfile.TemporaryDirectory() as tmp:
        zipfile.ZipFile(ZIP).extractall(tmp)
        for x in sorted(Path(tmp).glob("*.xlsx")):
            nombre_doc = re.sub(r"#U([0-9a-f]{4})", lambda m: chr(int(m.group(1), 16)), x.stem)
            base = "aesia-checklist-" + slug(nombre_doc.replace("_Checklist", ""), 40)
            carpeta = SALIDA / base
            shutil.rmtree(carpeta, ignore_errors=True)
            wb = openpyxl.load_workbook(x, data_only=True)
            k = 0
            for ws in wb.worksheets:
                if OMITIR_HOJA.match(ws.title):
                    continue
                r = hoja_a_md(ws)
                if not r:
                    continue
                tabla, filas = r
                k += 1
                carpeta.mkdir(parents=True, exist_ok=True)
                nombre = f"{base}-{k:02d}-{slug(ws.title, 40)}"
                desc = (f"AESIA, checklist «{nombre_doc.replace('_Checklist', '')}», hoja «{ws.title}» "
                        f"({filas} filas). Hoja del Excel de autoevaluación de las guías de requisitos, 2026-07-30.")
                (carpeta / f"{nombre}.md").write_text(
                    front(nombre, desc, dict(documento=base, emisor="AESIA", fecha="2026-07-30",
                                             idioma="es", hoja=ws.title, filas=filas,
                                             origen=f"{ZIP.name}/{x.name}")) + f"# {ws.title}\n\n{tabla}\n",
                    encoding="utf-8")
                n += 1
    return n


def main():
    a, b = sentencia(), checklists()
    print(f"sentencia: {a} notas; checklists: {b} notas")
    ind = ["# Índice: sentencia TJUE C-184/20 y checklists AESIA", "",
           "Generado por `md/conversion/trocear_otros.py`. Conversión no oficial.", ""]
    for d in sorted(SALIDA.glob("tjue-*")) + sorted(SALIDA.glob("aesia-checklist-*")):
        ind += [f"## {d.name}", ""]
        for f in sorted(d.glob("*.md")):
            t = re.search(r"^# (.+)$", f.read_text(encoding="utf-8"), re.M).group(1)
            ind.append(f"- [{f.stem}]({d.name}/{f.name}) — {t}")
        ind.append("")
    (SALIDA / "INDICE-otros.md").write_text("\n".join(ind), encoding="utf-8")


if __name__ == "__main__":
    main()
