#!/usr/bin/env python3
"""Trocea las conversiones Markdown de fuentes/md/ en notas por artículo.

Cada nota lleva front matter (name, description, tags...) en formato skill para
poder buscarlas con grep, un índice o una herramienta de búsqueda.
Uso: python3 trocear.py   (desde cualquier carpeta; reescribe plugins/ai-act-advisor/knowledge/notas/)
Solo stdlib. Las notas son derivadas: se editan las conversiones y se regenera.
"""
import re
import shutil
import unicodedata
from pathlib import Path

AQUI = Path(__file__).resolve().parent
MD = AQUI.parent
# Las notas viajan con el plugin (D21): plugins/ai-act-advisor/knowledge/notas/.
SALIDA = MD.parents[3] / "plugins" / "ai-act-advisor" / "knowledge" / "notas"

NORMAS = [
    dict(slug="ai-act", fichero="2026-07-27-ai-act-2024-1689-consolidado-es.md",
         corto="AI Act", largo="Reglamento (UE) 2024/1689", celex="02024R1689-20260727",
         version="consolidado 2026-07-27", tags=["ai-act", "reglamento-ue"]),
    dict(slug="rgpd", fichero="2016-05-04-rgpd-2016-679-consolidado-es.md",
         corto="RGPD", largo="Reglamento (UE) 2016/679", celex="02016R0679-20160504",
         version="consolidado 2016-05-04", tags=["rgpd", "reglamento-ue", "proteccion-datos"]),
    dict(slug="lopdgdd", fichero="2025-12-27-lopdgdd-3-2018-consolidado-boe.md",
         corto="LOPDGDD", largo="Ley Orgánica 3/2018", celex="BOE-A-2018-16673",
         version="consolidado 2025-12-27", tags=["lopdgdd", "espana", "proteccion-datos"]),
    dict(slug="omnibus", fichero="2026-07-24-omnibus-2026-1744-es.md",
         corto="Omnibus IA", largo="Reglamento (UE) 2026/1744", celex="32026R1744",
         version="DO 2026-07-24", tags=["omnibus", "ai-act", "reglamento-ue", "modificacion"]),
]

HEAD = re.compile(r"^(#{2,4}) (.+?)\s*$")
UNIDAD = re.compile(r"^(Artículo|Disposición|ANEXO)\b", re.I)
NIVEL = re.compile(r"^(CAPÍTULO|TÍTULO|SECCIÓN|Sección)\b", re.I)


def slug(txt):
    t = unicodedata.normalize("NFD", txt.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def id_unidad(titulo):
    """art-10, art-4-bis, anexo-iii, disp-adic-primera..."""
    m = re.match(r"Artículo\s+(\d+)\s*(bis|ter|quater|quinquies|sexies|septies|octies|nonies|decies)?", titulo, re.I)
    if m:
        return "art-" + m.group(1) + ("-" + m.group(2).lower() if m.group(2) else "")
    m = re.match(r"ANEXO\s+([IVXLC]+)", titulo)
    if m:
        return "anexo-" + m.group(1).lower()
    m = re.match(r"Disposición\s+(\w+)\s+(.+?)\.", titulo)
    if m:
        return "disp-" + slug(m.group(1))[:6] + "-" + slug(m.group(2))[:20]
    return slug(titulo)[:40]


def split_titulo(texto):
    """'Artículo 10 — Datos' o 'Artículo 4. Exactitud.' -> (etiqueta, titulo)"""
    for sep in (" — ", ". "):
        if sep in texto:
            a, b = texto.split(sep, 1)
            return a.strip(), b.strip().rstrip(".")
    return texto.strip(), ""


def procesar(n):
    lineas = (MD / n["fichero"]).read_text(encoding="utf-8").splitlines()
    contexto = {}  # nivel(2/3) -> texto
    unidades = []
    actual = None
    for i, l in enumerate(lineas):
        m = HEAD.match(l)
        if m and m.group(1) in ("##", "###", "####") and not m.group(2).startswith("«"):
            nivel, texto = len(m.group(1)), m.group(2)
            if UNIDAD.match(texto):
                if actual:
                    actual["fin"] = i
                actual = dict(texto=texto, ini=i, ctx=dict(contexto), fin=len(lineas))
                unidades.append(actual)
                continue
            if nivel in (2, 3) and NIVEL.match(texto):
                contexto = {k: v for k, v in contexto.items() if k < nivel}
                contexto[nivel] = texto
                if actual:
                    actual["fin"] = i
                    actual = None
    return lineas, unidades


def main():
    SALIDA.mkdir(exist_ok=True)
    for n in NORMAS:
        shutil.rmtree(SALIDA / n['slug'], ignore_errors=True)
    indice = ["# Índice de notas normativas", "",
              "Generado por `md/conversion/trocear.py`. No editar a mano: edita la conversión y regenera.", ""]
    total = 0
    for n in NORMAS:
        lineas, unidades = procesar(n)
        carpeta = SALIDA / n["slug"]
        carpeta.mkdir(parents=True)
        indice += [f"## {n['corto']} — {n['largo']} ({n['version']})", ""]
        vistos = {}
        for u in unidades:
            etiqueta, titulo = split_titulo(u["texto"])
            uid = id_unidad(u["texto"])
            vistos[uid] = vistos.get(uid, 0) + 1
            if vistos[uid] > 1:
                uid += f"-{vistos[uid]}"
            nombre = f"{n['slug']}-{uid}"
            cuerpo = "\n".join(lineas[u["ini"] + 1:u["fin"]]).strip()
            ctx = " · ".join(u["ctx"][k] for k in sorted(u["ctx"]))
            desc = f"{n['corto']}, {etiqueta}" + (f": {titulo}" if titulo else "") + "."
            if ctx:
                desc += f" Ubicación: {ctx}."
            desc += f" Texto {n['version']} ({n['largo']})."
            desc = desc.replace('"', "'")
            tags = n["tags"] + ["anexo" if uid.startswith("anexo") else "articulo" if uid.startswith("art") else "disposicion"]
            if titulo:
                tags += [w for w in slug(titulo).split("-") if len(w) > 5][:4]
            fm = ["---", f"name: {nombre}", f'description: "{desc}"',
                  "metadata:", "  type: reference",
                  f"  norma: {n['slug']}", f"  celex: {n['celex']}",
                  f"  unidad: {etiqueta}", f'  titulo: "{titulo.replace(chr(34), chr(39))}"',
                  f'  ubicacion: "{ctx.replace(chr(34), chr(39))}"',
                  f"  tags: [{', '.join(dict.fromkeys(tags))}]",
                  f"  origen: md/{n['fichero']}#L{u['ini'] + 1}-L{u['fin']}",
                  "  oficial: false", "---", ""]
            (carpeta / f"{nombre}.md").write_text(
                "\n".join(fm) + f"# {u['texto']}\n\n{cuerpo}\n", encoding="utf-8")
            indice.append(f"- [{nombre}]({n['slug']}/{nombre}.md) — {etiqueta}" + (f": {titulo}" if titulo else ""))
            total += 1
        indice.append("")
    (SALIDA / "INDICE.md").write_text("\n".join(indice), encoding="utf-8")
    print(f"{total} notas en {SALIDA}")


if __name__ == "__main__":
    main()
