"""Tests del buscador de notas normativas (prototipo de D21). Solo librería estándar:

    python -m unittest tests.test_buscar -v
"""

import json
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "plugins", "ai-act-advisor", "scripts"))

from aiact import notas  # noqa: E402

NOTAS = os.path.join(ROOT, "plugins", "ai-act-advisor", "knowledge", "notas")
CONSULTAS = os.path.join(ROOT, "tests", "consultas-citas.json")
INDICE = None


def indice():
    global INDICE
    if INDICE is None:
        INDICE = notas.Indice(NOTAS)
    return INDICE


def linea(ruta, n):
    with open(os.path.join(NOTAS, ruta), encoding="utf-8") as fh:
        return fh.read().split("\n")[n - 1]


class ArticuloTest(unittest.TestCase):
    def test_apartado_y_letra_apuntan_a_la_linea_del_fichero(self):
        r = indice().articulo("rgpd", "9.1")
        self.assertEqual(r["nota"], "rgpd-art-9")
        self.assertTrue(linea(r["ruta"], r["linea"]).startswith("1. Quedan prohibidos"))
        r = indice().articulo("rgpd", "5.1.c")
        self.assertTrue(linea(r["ruta"], r["linea"]).startswith("c) adecuados, pertinentes"))

    def test_anexo_con_punto(self):
        r = indice().articulo("ai-act", "anexo III 5.b")
        self.assertEqual(r["nota"], "ai-act-anexo-iii")
        self.assertIn("solvencia", linea(r["ruta"], r["linea"]))

    def test_sin_nota(self):
        self.assertIsNone(indice().articulo("rgpd", "999"))


class PasajesTest(unittest.TestCase):
    def test_excluye_la_version_inglesa_duplicada(self):
        self.assertFalse(any(n.documento() in notas.DUPLICADOS for n in indice().notas))

    def test_idioma_filtra_las_notas(self):
        for r in indice().pasajes([("high-risk classification", "en")], k=5):
            self.assertEqual(r["idioma"], "en")

    def test_citas_separa_normas_y_guias(self):
        r = indice().citas([("categorías especiales de datos", "es")], k=3)
        self.assertTrue(all(x["tipo"] == "norma" for x in r["normas"]))
        self.assertTrue(all(x["tipo"] == "guia" for x in r["guias"]))
        self.assertIn("rgpd-art-9", [x["nota"] for x in r["normas"]])


class ConsultasDePruebaTest(unittest.TestCase):
    """Mide el buscador con preguntas reales. Si baja de MINIMO, algo ha empeorado."""

    MINIMO = 18

    def test_espanol_vocabulario_de_la_norma_e_ingles(self):
        datos = json.load(open(CONSULTAS, encoding="utf-8"))
        aciertos, fallos = 0, []
        for c in datos["consultas"]:
            r = indice().citas([(c["es"], "es"), (c["es_norma"], "es"), (c["en"], "en")], k=datos["k"])
            vistas = [x["nota"] for x in r["normas"] + r["guias"]]
            if any(v == e or v.startswith(e + "-") for v in vistas for e in c["esperadas"]):
                aciertos += 1
            else:
                fallos.append(c["id"])
        self.assertGreaterEqual(aciertos, self.MINIMO, "fallan: %s" % fallos)


if __name__ == "__main__":
    unittest.main()
