#!/usr/bin/env python3
"""Convierte los PDF de fuentes/ en notas Markdown con front matter, troceadas por sección.

Requiere `pdftotext` (poppler) y `pypdf`. Escribe en plugins/ai-act-advisor/knowledge/notas/<documento>/.
Troceado, por orden: marcadores del PDF (nivel 1); índice «Contenido general» de las
guías AESIA; bloques de páginas si el documento es largo; una sola nota si es corto.
Los PDF que ya tienen conversión fina en fuentes/md/ (AI Act, RGPD, LOPDGDD) se omiten.
Uso: python3 -I trocear_pdf.py
"""
import re
import shutil
import statistics
import subprocess
import unicodedata
from pathlib import Path

import pypdf

AQUI = Path(__file__).resolve().parent
FUENTES = AQUI.parent.parent
# Las notas viajan con el plugin (D21): plugins/ai-act-advisor/knowledge/notas/.
SALIDA = FUENTES.parents[2] / "plugins" / "ai-act-advisor" / "knowledge" / "notas"

OMITIR = ("2016-05-04-rgpd-2016-679-doue", "2024-07-12-ai-act-2024-1689-original",
          "2025-12-27-lopdgdd-3-2018-consolidado-boe.pdf")
EMISORES = {"aesia": "AESIA", "aepd": "AEPD", "cepd": "CEPD", "directrices": "Comisión Europea",
            "rd": "BOE"}
BLOQUE = 8          # páginas por nota cuando no hay estructura
CORTO = 25          # un documento de menos páginas va en una sola nota


def slug(t, n=60):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:n].strip("-")


def texto(pdf, a, b):
    out = subprocess.run(["pdftotext", "-f", str(a), "-l", str(b), str(pdf), "-"],
                         capture_output=True, text=True).stdout
    return limpiar(out)


def limpiar(t):
    t = t.replace("\f", "\n\n").replace("­", "")
    t = re.sub(r"^[•●▪◦] ?", "- ", t, flags=re.M)
    lineas, res = t.split("\n"), []
    for l in lineas:
        l = l.rstrip()
        if (res and l and res[-1] and not re.search(r"[.:;?!)\]»]$|^- |\.{4,}", res[-1])
                and not l.startswith(("- ", "#")) and l[0].islower()):
            res[-1] += " " + l
        else:
            res.append(l)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(res)).strip()


def secciones_outline(r):
    sec = []
    for o in r.outline:
        if isinstance(o, list):
            continue
        try:
            p = r.get_destination_page_number(o) + 1
        except Exception:
            continue
        titulo = re.sub(r"^Destination\s+\d+\.\s*", "", o.title).strip()
        sec.append((titulo, p))
    return sec if len(sec) >= 3 else []


def secciones_toc(pdf, r):
    """Índice «Contenido general» de las guías AESIA: títulos con puntos y página impresa."""
    n = min(len(r.pages), 6)
    pat = re.compile(r"^(?:\d+\.\s*)?([A-ZÁÉÍÓÚ][^\n]{3,}?)\s*\.{5,}\s*(\d+)\s*$", re.M)
    cabecera = texto(pdf, 1, n)
    corte = re.search(r"Índice detallado|Detailed (?:table of )?contents", cabecera, re.I)
    if corte:
        cabecera = cabecera[:corte.start()]
    entradas, ult = [], 0
    for t, imp in pat.findall(cabecera):
        if int(imp) >= ult:
            entradas.append((t, imp))
            ult = int(imp)
    if len(entradas) < 3:
        return []
    paginas = [texto(pdf, i, i) for i in range(1, len(r.pages) + 1)]
    desfases = []
    for t, imp in entradas:
        for i in range(n, len(paginas)):
            if re.search(r"^(?:\d+\.\s*)?" + re.escape(t) + r"\s*$", paginas[i], re.M):
                desfases.append(i + 1 - int(imp))
                break
    if not desfases:
        return []
    d = int(statistics.median(desfases))
    return [(t, int(imp) + d) for t, imp in entradas if 1 <= int(imp) + d <= len(r.pages)]


def subdividir(partes):
    res = []
    for t, a, b in partes:
        if b - a + 1 <= 12:
            res.append((t, a, b))
            continue
        for k, i in enumerate(range(a, b + 1, BLOQUE), 1):
            res.append((f"{t} (parte {k})", i, min(i + BLOQUE - 1, b)))
    return res


def trozos(pdf, r):
    return subdividir(_trozos(pdf, r))


def _trozos(pdf, r):
    total = len(r.pages)
    sec = secciones_outline(r) or secciones_toc(pdf, r)
    if sec:
        sec.sort(key=lambda x: x[1])
        if sec[0][1] > 1:
            sec.insert(0, ("Portada y preliminares", 1))
        res = []
        for k, (t, p) in enumerate(sec):
            fin = sec[k + 1][1] if k + 1 < len(sec) else total
            if fin > p and k + 1 < len(sec):
                fin -= 0 if fin == p else 1
            res.append((t, p, max(p, fin)))
        return res
    if total <= CORTO:
        return [("Texto completo", 1, total)]
    return [(f"Páginas {a}-{min(a + BLOQUE - 1, total)}", a, min(a + BLOQUE - 1, total))
            for a in range(1, total + 1, BLOQUE)]


def main():
    SALIDA.mkdir(exist_ok=True)
    indice = ["# Índice de notas de guías y directrices", "",
              "Generado por `md/conversion/trocear_pdf.py` desde los PDF de `fuentes/`. "
              "Conversión no oficial; hace fe el PDF.", ""]
    total_notas = 0
    for pdf in sorted(FUENTES.glob("*.pdf")):
        if any(pdf.name.startswith(o) or pdf.name == o for o in OMITIR):
            continue
        m = re.match(r"(\d{4}-\d{2}-\d{2})-(.+)\.pdf", pdf.name)
        fecha, resto = m.groups()
        idioma = "en" if resto.endswith("-en") else "es"
        base = re.sub(r"-(es|en)$", "", resto)
        emisor = EMISORES.get(base.split("-")[0], "")
        titulo_doc = base.replace("-", " ")
        carpeta = SALIDA / base
        if carpeta.exists():
            shutil.rmtree(carpeta)
        carpeta.mkdir(parents=True)
        r = pypdf.PdfReader(str(pdf))
        partes = trozos(pdf, r)
        indice += [f"## {base} ({emisor}, {fecha}, {idioma}, {len(r.pages)} págs.)", ""]
        for k, (sec, a, b) in enumerate(partes, 1):
            cuerpo = texto(pdf, a, b)
            if not cuerpo:
                continue
            nombre = f"{base}-{k:02d}-{slug(sec, 40) or 'seccion'}"
            desc = (f"{emisor}: {titulo_doc}, sección «{sec}» (págs. {a}-{b}). "
                    f"Documento de {fecha}, idioma {idioma}.").replace('"', "'")
            fm = ["---", f"name: {nombre[:100]}", f'description: "{desc}"',
                  "metadata:", "  type: reference", f"  documento: {base}",
                  f"  emisor: {emisor}", f"  fecha: {fecha}", f"  idioma: {idioma}",
                  f'  seccion: "{sec.replace(chr(34), chr(39))}"', f"  paginas: {a}-{b}",
                  f"  origen: {pdf.name}", "  oficial: false", "---", ""]
            (carpeta / f"{nombre}.md").write_text(
                "\n".join(fm) + f"# {sec}\n\n{cuerpo}\n", encoding="utf-8")
            indice.append(f"- [{nombre}]({base}/{nombre}.md) — {sec} (págs. {a}-{b})")
            total_notas += 1
        indice.append("")
    (SALIDA / "INDICE-guias.md").write_text("\n".join(indice), encoding="utf-8")
    print(f"{total_notas} notas")


if __name__ == "__main__":
    main()
