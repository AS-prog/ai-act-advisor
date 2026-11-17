"""Búsqueda en las notas normativas (prototipo de D21). Solo librería estándar.

Dos operaciones:

- ``articulo(norma, ref)``: trae una unidad (artículo, anexo o disposición) y, si
  la referencia lleva apartado («9.1», «5.1.c»), la línea donde empieza.
- ``pasajes(consultas)``: BM25 sobre front matter y texto. Admite varias
  consultas (por ejemplo, la misma pregunta en español y en inglés) y une los
  resultados con fusión de rangos recíprocos (RRF).

Las notas en inglés que tienen versión española se excluyen (``DUPLICADOS``).
"""
import math
import os
import re
import unicodedata
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
PLUGIN = os.path.dirname(os.path.dirname(HERE))
REPO = os.path.dirname(os.path.dirname(PLUGIN))
CANDIDATAS = [
    os.path.join(PLUGIN, "knowledge", "notas"),
    os.path.join(REPO, "docs", "documentos", "fuentes", "notas"),
]

# Documentos en inglés con versión española en las notas: se omiten.
DUPLICADOS = {"directrices-art50-transparencia-c2026-5054": "directrices-art50-transparencia-c2026-7702"}

PESO_FRONT = 3  # el front matter cuenta el triple que el cuerpo
K1, B = 1.2, 0.75
RRF_K = 60

PALABRAS_VACIAS = set(
    "que los las del por para con una uno unos unas sus como mas pero sin sobre este esta estos estas "
    "ese esa entre cuando donde sea son ser han hay muy tambien otro otra otros otras dicho dicha "
    "the and for with that this from are was were has have not but can may any all its which such "
    "into other than their these those shall where when also been".split()
)


def directorio_notas(explicito=None):
    if explicito:
        return explicito
    if os.environ.get("AIACT_NOTAS"):
        return os.environ["AIACT_NOTAS"]
    for d in CANDIDATAS:
        if os.path.isdir(d):
            return d
    raise FileNotFoundError("No encuentro las notas normativas; usa --notas o AIACT_NOTAS.")


def _sin_tildes(texto):
    texto = unicodedata.normalize("NFKD", texto.lower())
    return "".join(c for c in texto if not unicodedata.combining(c))


def raiz(palabra):
    """Raíz tosca común a español e inglés: corta a 6 letras tras quitar plurales."""
    for suf in ("es", "s"):
        if len(palabra) > 4 and palabra.endswith(suf):
            palabra = palabra[: -len(suf)]
            break
    return palabra[:6]


def tokens(texto):
    return [raiz(p) for p in re.findall(r"[a-z0-9]{3,}", _sin_tildes(texto)) if p not in PALABRAS_VACIAS]


def _front_matter(texto):
    if not texto.startswith("---"):
        return {}, texto, 0
    fin = texto.find("\n---", 3)
    bloque = texto[3:fin]
    cuerpo = texto[fin + 4 :]
    datos = {}
    for linea in bloque.splitlines():
        m = re.match(r"\s*(\w+):\s*(.*)$", linea)
        if m and m.group(2):
            datos[m.group(1)] = m.group(2).strip().strip('"')
    return datos, cuerpo, bloque.count("\n") + 1


MAX_PASAJE = 1500  # caracteres por pasaje


class Nota:
    __slots__ = ("name", "ruta", "meta", "lineas", "offset", "idioma")

    def __init__(self, ruta, texto):
        meta, cuerpo, offset = _front_matter(texto)
        self.ruta = ruta
        self.meta = meta
        self.name = meta.get("name") or os.path.splitext(os.path.basename(ruta))[0]
        self.lineas = cuerpo.split("\n")
        self.offset = offset  # línea del fichero donde empieza el cuerpo, menos 1
        self.idioma = meta.get("idioma", "es")

    def documento(self):
        return self.meta.get("documento") or self.meta.get("norma") or ""

    def tipo(self):
        return "norma" if self.meta.get("norma") else "guia"

    def cabecera(self):
        return " ".join(self.meta.get(k, "") for k in ("description", "titulo", "seccion", "unidad", "tags", "hoja"))

    def trozos(self):
        """Pasajes de párrafos seguidos hasta MAX_PASAJE caracteres: (línea inicial, texto)."""
        inicio, buf, largo = None, [], 0
        for i, linea in enumerate(self.lineas):
            if inicio is None:
                if not linea.strip():
                    continue
                inicio = i
            buf.append(linea)
            largo += len(linea)
            if largo >= MAX_PASAJE and not linea.strip():
                yield inicio + 1 + self.offset, "\n".join(buf)
                inicio, buf, largo = None, [], 0
        if buf:
            yield inicio + 1 + self.offset, "\n".join(buf)


class Pasaje:
    __slots__ = ("nota", "linea", "tf", "largo")

    def __init__(self, nota, linea, tf, largo):
        self.nota, self.linea, self.tf, self.largo = nota, linea, tf, largo


class Indice:
    def __init__(self, directorio=None):
        self.dir = directorio_notas(directorio)
        self.notas = []
        for raiz_dir, _, ficheros in os.walk(self.dir):
            for f in sorted(ficheros):
                if not f.endswith(".md") or f.startswith("INDICE") or f == "README.md":
                    continue
                ruta = os.path.join(raiz_dir, f)
                with open(ruta, encoding="utf-8") as fh:
                    nota = Nota(ruta, fh.read())
                if nota.documento() in DUPLICADOS:
                    continue
                self.notas.append(nota)
        self.por_nombre = {n.name: n for n in self.notas}
        self.pasajes_ = []
        self.df = Counter()
        for n in self.notas:
            cab = tokens(n.cabecera()) * PESO_FRONT
            for linea, texto in n.trozos():
                toks = cab + tokens(texto)
                p = Pasaje(n, linea, Counter(toks), len(toks))
                self.pasajes_.append(p)
                self.df.update(p.tf.keys())
        self.media = sum(p.largo for p in self.pasajes_) / max(len(self.pasajes_), 1)

    # --- pasajes -------------------------------------------------------
    def _bm25(self, consulta, idioma=None, tipo=None):
        """Ranking de notas (mejor pasaje de cada una) para una consulta."""
        q = set(tokens(consulta))
        total = len(self.pasajes_)
        mejor = {}
        for p in self.pasajes_:
            if idioma and p.nota.idioma != idioma:
                continue
            if tipo and p.nota.tipo() != tipo:
                continue
            s = 0.0
            for t in q:
                f = p.tf.get(t)
                if not f:
                    continue
                idf = math.log(1 + (total - self.df[t] + 0.5) / (self.df[t] + 0.5))
                s += idf * f * (K1 + 1) / (f + K1 * (1 - B + B * p.largo / self.media))
            if s and s > mejor.get(p.nota.name, (0, 0))[0]:
                mejor[p.nota.name] = (s, p.linea)
        orden = sorted(mejor, key=lambda x: mejor[x][0], reverse=True)
        return [(x, mejor[x][1]) for x in orden]

    def pasajes(self, consultas, k=5, tipo=None):
        """consultas: textos o pares (texto, idioma). Con idioma, la consulta solo
        busca en las notas de ese idioma. Las consultas del mismo idioma se unen
        con RRF y los idiomas se intercalan, para que el inglés (pocas notas) no
        quede tapado por varias consultas en español.
        tipo: «norma» (AI Act, RGPD, LOPDGDD, Omnibus) o «guia» (el resto)."""
        if isinstance(consultas, str):
            consultas = [consultas]
        grupos, lineas = {}, {}
        for c in consultas:
            texto, idioma = (c, None) if isinstance(c, str) else c
            fusion = grupos.setdefault(idioma, Counter())
            for i, (name, linea) in enumerate(self._bm25(texto, idioma, tipo)[:100]):
                fusion[name] += 1.0 / (RRF_K + i + 1)
                lineas.setdefault(name, linea)
        rankings = [[n for n, _ in f.most_common()] for f in grupos.values()]
        orden, vistos = [], set()
        for fila in range(max((len(r) for r in rankings), default=0)):
            for r in rankings:
                if fila < len(r) and r[fila] not in vistos:
                    vistos.add(r[fila])
                    orden.append(r[fila])
        salida = []
        for name in orden[:k]:
            n = self.por_nombre[name]
            salida.append(
                {
                    "nota": name,
                    "descripcion": n.meta.get("description", ""),
                    "idioma": n.idioma,
                    "tipo": n.tipo(),
                    "linea": lineas[name],
                    "ruta": os.path.relpath(n.ruta, self.dir),
                }
            )
        return salida

    def citas(self, consultas, k=3):
        """Lo que usa una skill: las normas que pueden ser la cita y las guías que la apoyan."""
        return {"normas": self.pasajes(consultas, k, "norma"), "guias": self.pasajes(consultas, k, "guia")}

    # --- artículo ------------------------------------------------------
    def articulo(self, norma, ref):
        """norma: ai-act, rgpd, lopdgdd, omnibus. ref: «9», «9.1», «5.1.c», «anexo III»."""
        ref = ref.strip()
        m = re.match(r"(?i)anexo\s+([ivxlc]+)(?:[.\s]+(.*))?$", ref)
        if m:
            unidad, resto = "anexo " + m.group(1).lower(), m.group(2)
        else:
            partes = ref.split(".")
            unidad, resto = "artículo " + partes[0], ".".join(partes[1:]) or None
        for n in self.notas:
            if n.meta.get("norma") != norma:
                continue
            if _sin_tildes(n.meta.get("unidad", "")) == _sin_tildes(unidad):
                return {
                    "nota": n.name,
                    "unidad": n.meta.get("unidad"),
                    "titulo": n.meta.get("titulo", ""),
                    "linea": self._linea_apartado(n, resto),
                    "ruta": os.path.relpath(n.ruta, self.dir),
                }
        return None

    def _linea_apartado(self, n, resto):
        """Primera línea del apartado («1») y, si hay, de la letra («1.c» → «c)»)."""
        if not resto:
            return 1 + n.offset
        trozos = [t for t in re.split(r"[.\s]+", resto) if t]
        inicio = 0
        for t in trozos:
            patron = re.compile(r"^%s\.\s" % re.escape(t)) if t.isdigit() else re.compile(r"^%s\)\s" % re.escape(t))
            for i in range(inicio, len(n.lineas)):
                if patron.match(n.lineas[i]):
                    inicio = i
                    break
            else:
                break
        return inicio + 1 + n.offset
