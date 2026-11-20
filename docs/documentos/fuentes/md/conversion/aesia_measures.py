#!/usr/bin/env python3
"""Catálogo estructurado de las medidas guía de los checklists de AESIA (issue #20).

Lee los Excel de `2026-07-30-aesia-checklists-y-ejemplos.zip` sin dependencias
(un .xlsx es un zip de XML) y escribe `plugins/ai-act-advisor/knowledge/aesia-measures.yaml`:
por checklist, los apartados del artículo, las medidas guía con sus cuestiones
orientativas y los cruces apartado → medida de la hoja «Relación MG-Apart.».

Lee los valores que Excel dejó calculados, no las fórmulas. Los apartados que el
Reglamento 2026/1744 cambió se marcan con AMENDMENTS, que se revisa a mano.
Explicación de los libros: docs/documentos/tecnica/checklists-aesia.md.

Uso:
    python3 -I aesia_measures.py              # Gobernanza del dato y Registros
    python3 -I aesia_measures.py --all        # los 12 checklists
    python3 -I aesia_measures.py --check      # falla si el YAML no está al día
"""
import argparse
import hashlib
import io
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path, PurePosixPath

HERE = Path(__file__).resolve().parent
SOURCES = HERE.parent.parent
ZIP = SOURCES / "2026-07-30-aesia-checklists-y-ejemplos.zip"
OUTPUT = SOURCES.parents[2] / "plugins" / "ai-act-advisor" / "knowledge" / "aesia-measures.yaml"

NS = {
    "m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}

# Fichero del zip (sin extensión ni «_Checklist») → id, título y guía de AESIA.
CHECKLISTS = {
    "gobernanza-del-dato": ("Gobernanza del dato", "07"),
    "registros": ("Registros", "12"),
    "gestion-de-calidad": ("Gestión de la calidad", "04"),
    "gestion-de-riesgos": ("Gestión de riesgos", "05"),
    "supervision-humana": ("Supervisión humana", "06"),
    "transparencia": ("Transparencia", "08"),
    "precision": ("Precisión", "09"),
    "solidez": ("Solidez", "10"),
    "ciberseguridad": ("Ciberseguridad", "11"),
    "vigilancia-poscomercializacion": ("Vigilancia poscomercialización", "13"),
    "gestion-de-incidentes": ("Gestión de incidentes", "14"),
    "documentacion-tecnica": ("Documentación técnica", "15"),
}
DEFAULT = ["gobernanza-del-dato", "registros"]

# Apartados que el Reglamento 2026/1744 cambió después de los checklists (v1.0, 2025-12-10).
# Clave: prefijo del apartado; se aplica a él y a sus letras.
AMENDMENTS = {
    "10.5": {
        "status": "suprimido",
        "moved_to": "art. 4 bis",
        "note": "ai-act-art-4-bis",
        "by": "Reglamento (UE) 2026/1744",
        "comment": "El art. 10.5 se suprimió y su contenido pasó al art. 4 bis; el art. 10.6 remite a él.",
    },
    "11.1": {
        "status": "modificado",
        "by": "Reglamento (UE) 2026/1744",
        "comment": "Documentación técnica simplificada para pymes y pequeñas empresas de mediana capitalización.",
    },
    "17.2": {
        "status": "modificado",
        "by": "Reglamento (UE) 2026/1744",
        "comment": "Proporcionalidad según el tamaño del proveedor, incluidas las pequeñas mid-caps.",
    },
    "72.3": {
        "status": "modificado",
        "by": "Reglamento (UE) 2026/1744",
        "comment": "La Comisión adoptará orientaciones con un modelo de plan antes del 2027-09-02.",
    },
}

# Erratas conocidas de los Excel que el catálogo corrige o señala.
ERRATA = {
    "registros": "El Excel repite el apartado 12.3; sus medidas se unen en uno.",
    "vigilancia-poscomercializacion": "El Excel pone IDArt AR73 en los apartados del art. 72.",
}

MG_ID = re.compile(r"^MG\d{2}$")
REF_ARTICLE = re.compile(r"^Art[íi]culo\s+0*(\d+)", re.I)


def slug(text):
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def clean(value):
    """Texto de una celda en una línea, sin comillas dobles (miniyaml no las escapa)."""
    if value is None:
        return ""
    text = str(value).replace('"', "'").replace(" ", " ")
    return re.sub(r"\s+", " ", text).strip()


def column_index(ref):
    letters = re.match(r"[A-Z]+", ref).group(0)
    n = 0
    for ch in letters:
        n = n * 26 + ord(ch) - 64
    return n


def number(text):
    """Número de celda con su representación más corta: 10.199999999999999 → 10.2."""
    try:
        f = float(text)
    except ValueError:
        return text
    return str(int(f)) if f.is_integer() else repr(f)


class Workbook:
    """Lector mínimo de .xlsx: valores en caché de cada celda, por hoja."""

    def __init__(self, data):
        self.zip = zipfile.ZipFile(data)
        self.strings = self._shared_strings()
        self.paths = self._sheet_paths()

    def _xml(self, name):
        return ET.fromstring(self.zip.read(name))

    def _shared_strings(self):
        if "xl/sharedStrings.xml" not in self.zip.namelist():
            return []
        root = self._xml("xl/sharedStrings.xml")
        return ["".join(t.text or "" for t in si.iter(f"{{{NS['m']}}}t")) for si in root.findall("m:si", NS)]

    def _sheet_paths(self):
        rels = {
            r.get("Id"): r.get("Target")
            for r in self._xml("xl/_rels/workbook.xml.rels").findall("rel:Relationship", NS)
        }
        paths = {}
        for sheet in self._xml("xl/workbook.xml").find("m:sheets", NS):
            target = rels[sheet.get(f"{{{NS['r']}}}id")]
            target = target.lstrip("/") if target.startswith("/") else str(PurePosixPath("xl") / target)
            paths[sheet.get("name")] = target
        return paths

    def rows(self, name):
        """{fila: {columna: valor}} con el valor calculado de cada celda."""
        out = {}
        for c in self._xml(self.paths[name]).iter(f"{{{NS['m']}}}c"):
            kind = c.get("t")
            if kind == "inlineStr":
                value = "".join(t.text or "" for t in c.iter(f"{{{NS['m']}}}t"))
            else:
                v = c.find("m:v", NS)
                if v is None or v.text is None:
                    continue
                value = self.strings[int(v.text)] if kind == "s" else v.text
                if kind in (None, "n"):
                    value = number(value)
            ref = c.get("r")
            row = int(re.search(r"\d+", ref).group(0))
            out.setdefault(row, {})[column_index(ref)] = value
        return out


def checklist_files(archive):
    found = {}
    for name in archive.namelist():
        if name.endswith("_Checklist.xlsx"):
            stem = name.rsplit("/", 1)[-1][: -len("_Checklist.xlsx")]
            # El zip guarda las tildes como #U00f3.
            stem = re.sub(r"#U([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), stem)
            found[slug(stem)] = name
    return found


def header_row(rows, label):
    for r in sorted(rows):
        if any(clean(v).lower().startswith(label) for v in rows[r].values()):
            return r
    raise ValueError(f"No encuentro la cabecera «{label}»")


def parse_articles(rows):
    head = header_row(rows, "idart")
    cols = {clean(v).lower(): c for c, v in rows[head].items()}
    c_art, c_clause = cols["idart"], cols["apartado"]
    c_text, c_summary = cols["descripción"], cols["descripción resumida"]
    out = []
    for r in sorted(k for k in rows if k > head):
        cells = rows[r]
        clause = clean(cells.get(c_clause))
        if not clause:
            continue
        out.append({
            "id": clause.rstrip("."),
            "article": clean(cells.get(c_art)),
            "summary": clean(cells.get(c_summary)),
            "text": clean(cells.get(c_text)),
        })
    return out


def parse_measures(rows):
    head = header_row(rows, "idmedida")
    cols = {clean(v).lower(): c for c, v in rows[head].items()}
    c_id = cols["idmedida"]
    c_desc = cols["descripción"]
    c_q = next(c for k, c in cols.items() if k.startswith("cuestiones"))
    out = []
    for r in sorted(k for k in rows if k > head):
        cells = rows[r]
        mid = clean(cells.get(c_id))
        if not MG_ID.match(mid):
            continue
        title = clean(cells.get(c_desc))
        raw = str(cells.get(c_q) or "")
        questions = [clean(q) for q in re.split(r"(?:^|\s)\*\s*", raw) if clean(q)]
        measure = {"id": mid, "title": title, "questions": questions}
        ref = REF_ARTICLE.match(title)
        if ref:
            measure["refers_to"] = f"art. {int(ref.group(1))}"
        out.append(measure)
    return out


MATRIX_LABEL = re.compile(r"^((?:\d+|[IVX]+)(?:\.\w+)*?)\.?(?:\s+([a-z])\))?\s")


def matrix_clause(label):
    """«10.2.f. Posibles sesgos» → 10.2.f; «IV.1. a) Contenido…» → IV.1.a."""
    m = MATRIX_LABEL.match(label + " ")
    if not m:
        raise ValueError(f"Fila de la matriz sin apartado: «{label}»")
    return m.group(1) + (f".{m.group(2)}" if m.group(2) else "")


def parse_matrix(rows, clauses):
    """Cruces apartado → medidas de «Relación MG-Apart.», por id de apartado."""
    head = header_row(rows, "apartados")
    columns = {}
    for c, v in sorted(rows[head].items()):
        mid = clean(v)
        if MG_ID.match(mid) and mid not in columns.values():
            columns[c] = mid
    known = {c["id"] for c in clauses}
    links = {}
    # La matriz acaba en la primera fila vacía; debajo algunos libros repiten la lista de MG.
    r = head + 1
    while clean(rows.get(r, {}).get(2)):
        cid = matrix_clause(clean(rows[r][2]))
        if cid not in known:
            raise ValueError(f"La matriz cita el apartado {cid}, que no está en «Artículo RIA»")
        found = links.setdefault(cid, [])
        found += [mid for c, mid in columns.items() if clean(rows[r].get(c)).upper() == "X" and mid not in found]
        r += 1
    return links


def amendment(clause_id):
    for prefix, change in AMENDMENTS.items():
        if clause_id == prefix or clause_id.startswith(prefix + "."):
            return change
    return None


def article_note(clause_id):
    if clause_id.upper().startswith("IV"):
        return "ai-act-anexo-iv"
    return f"ai-act-art-{clause_id.split('.')[0]}"


def article_label(note):
    """ai-act-art-10 → art. 10; ai-act-anexo-iv → anexo IV."""
    tail = note.removeprefix("ai-act-")
    if tail.startswith("anexo-"):
        return "anexo " + tail.removeprefix("anexo-").upper()
    return "art. " + tail.removeprefix("art-").replace("-", " ")


def build(key, data):
    book = Workbook(data)
    clauses = parse_articles(book.rows("Artículo RIA"))
    measures = parse_measures(book.rows("Medidas guías (MG)"))
    links = parse_matrix(book.rows("Relación MG-Apart."), clauses)
    known = {m["id"] for m in measures}

    merged = {}
    for clause in clauses:
        mids = links.get(clause["id"], [])
        unknown = set(mids) - known
        if unknown:
            raise ValueError(f"{key}: medidas sin describir {sorted(unknown)}")
        if clause["id"] in merged:  # apartado repetido en el Excel (Registros, 12.3)
            continue
        entry = {"id": clause["id"], "summary": clause["summary"], "text": clause["text"],
                 "note": article_note(clause["id"]), "measures": mids}
        change = amendment(clause["id"])
        if change:
            entry["amended"] = change
        merged[clause["id"]] = entry

    by_measure = {m["id"]: [] for m in measures}
    for entry in merged.values():
        for mid in entry["measures"]:
            by_measure[mid].append(entry["id"])
    for m in measures:
        m["clauses"] = by_measure[m["id"]]

    articles = []
    for entry in merged.values():
        art = article_label(entry["note"])
        if art not in articles:
            articles.append(art)

    title, guide = CHECKLISTS[key]
    return {
        "id": key,
        "title": title,
        "guide": guide,
        "articles": articles,
        "notes": f"aesia-checklist-{key}",
        "guide_notes": f"aesia-{guide}-",
        "errata": ERRATA.get(key),
        "clauses": list(merged.values()),
        "measures": measures,
    }


def q(text):
    return f'"{text}"'


def dump(catalog, zip_sha, keys):
    lines = [
        "# Catálogo de las medidas guía de los checklists de AESIA. GENERADO: no editar a mano.",
        "# Lo escribe docs/documentos/fuentes/md/conversion/aesia_measures.py desde el zip de AESIA.",
        "# Qué es cada hoja y cada campo: docs/documentos/tecnica/checklists-aesia.md.",
        "# Las medidas orientan sobre CÓMO cumplir; la obligación está en el artículo (campo note).",
        "source:",
        f"  file: {q('docs/documentos/fuentes/2026-07-30-aesia-checklists-y-ejemplos.zip')}",
        f"  sha256: {q(zip_sha)}",
        f"  publisher: {q('AESIA')}",
        f"  checklists_version: {q('1.0 (2025-12-10)')}",
        f"  license: {q('CC BY 4.0')}",
        f"  legal_basis: {q('AI Act consolidado de 2026-07-27')}",
        "  scope: " + q("Proveedores de sistemas de IA de alto riesgo; aplica desde 2027-12-02 (anexo III) y 2028-08-02 (anexo I)"),
        f"checklists_included: [{', '.join(keys)}]",
        "checklists:",
    ]
    for ck in catalog:
        lines += [
            f"  - id: {ck['id']}",
            f"    title: {q(ck['title'])}",
            f"    guide: {q(ck['guide'])}",
            f"    articles: [{', '.join(q(a) for a in ck['articles'])}]",
            f"    notes: {q(ck['notes'])}",
            f"    guide_notes: {q(ck['guide_notes'])}",
        ]
        if ck["errata"]:
            lines.append(f"    errata: {q(ck['errata'])}")
        lines.append("    clauses:")
        for c in ck["clauses"]:
            lines += [
                f"      - id: {q(c['id'])}",
                f"        summary: {q(c['summary'])}",
                f"        note: {q(c['note'])}",
                f"        measures: [{', '.join(c['measures'])}]",
            ]
            if "amended" in c:
                lines.append("        amended:")
                lines += [f"          {k}: {q(v)}" for k, v in c["amended"].items()]
        lines.append("    measures:")
        for m in ck["measures"]:
            lines += [
                f"      - id: {m['id']}",
                f"        title: {q(m['title'])}",
                f"        clauses: [{', '.join(q(c) for c in m['clauses'])}]",
            ]
            if "refers_to" in m:
                lines.append(f"        refers_to: {q(m['refers_to'])}")
            lines.append("        questions:")
            lines += [f"          - {q(x)}" for x in m["questions"]]
    return "\n".join(lines) + "\n"


def generate(keys, zip_path=ZIP):
    data = zip_path.read_bytes()
    archive = zipfile.ZipFile(zip_path)
    files = checklist_files(archive)
    catalog = []
    for key in keys:
        if key not in files:
            raise SystemExit(f"No está en el zip: {key}. Hay: {', '.join(sorted(files))}")
        catalog.append(build(key, io.BytesIO(archive.read(files[key]))))
    return dump(catalog, hashlib.sha256(data).hexdigest(), keys)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--all", action="store_true", help="los 12 checklists")
    ap.add_argument("--only", nargs="+", metavar="ID", help="checklists concretos")
    ap.add_argument("--check", action="store_true", help="falla si el YAML no coincide")
    args = ap.parse_args(argv)
    keys = list(CHECKLISTS) if args.all else (args.only or DEFAULT)
    text = generate(keys)
    if args.check:
        current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if current != text:
            print(f"{OUTPUT} no está al día: vuelve a generarlo.", file=sys.stderr)
            return 1
        print("Al día.")
        return 0
    OUTPUT.write_text(text, encoding="utf-8")
    print(f"Escrito {OUTPUT} ({len(keys)} checklists)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
