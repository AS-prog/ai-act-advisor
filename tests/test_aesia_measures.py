"""Tests del catálogo de medidas de AESIA (issue #20). Solo librería estándar:

    python -m unittest tests.test_aesia_measures -v
"""

import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "plugins", "ai-act-advisor", "scripts"))
sys.path.insert(0, os.path.join(ROOT, "docs", "documentos", "fuentes", "md", "conversion"))

import aesia_measures  # noqa: E402
from aiact import miniyaml  # noqa: E402

KNOWLEDGE = os.path.join(ROOT, "plugins", "ai-act-advisor", "knowledge")
CATALOG = os.path.join(KNOWLEDGE, "aesia-measures.yaml")
NOTES = os.path.join(KNOWLEDGE, "notas")


def note_exists(name):
    for _dirpath, dirnames, filenames in os.walk(NOTES):
        if f"{name}.md" in filenames or name in dirnames:
            return True
    return False


class TestCatalog(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = miniyaml.load(CATALOG)
        cls.by_id = {c["id"]: c for c in cls.data["checklists"]}

    def test_up_to_date(self):
        keys = self.data["checklists_included"]
        with open(CATALOG, encoding="utf-8") as fh:
            self.assertEqual(fh.read(), aesia_measures.generate(keys),
                             "Vuelve a generar aesia-measures.yaml con aesia_measures.py")

    def test_first_checklists(self):
        self.assertEqual(self.data["checklists_included"], ["gobernanza-del-dato", "registros"])
        gob, reg = self.by_id["gobernanza-del-dato"], self.by_id["registros"]
        self.assertEqual((len(gob["clauses"]), len(gob["measures"])), (20, 21))
        self.assertEqual(sum(len(c["measures"]) for c in gob["clauses"]), 65)
        self.assertEqual(sum(len(c["measures"]) for c in reg["clauses"]), 37)

    def test_measures_and_clauses_agree(self):
        for ck in self.data["checklists"]:
            ids = {m["id"] for m in ck["measures"]}
            for clause in ck["clauses"]:
                self.assertTrue(set(clause["measures"]) <= ids, clause["id"])
                for mid in clause["measures"]:
                    measure = next(m for m in ck["measures"] if m["id"] == mid)
                    self.assertIn(clause["id"], measure["clauses"])
            for m in ck["measures"]:
                self.assertTrue(m["questions"], f"{ck['id']} {m['id']} sin cuestiones")

    def test_notes_exist(self):
        for ck in self.data["checklists"]:
            self.assertTrue(note_exists(ck["notes"]), ck["notes"])
            for clause in ck["clauses"]:
                self.assertTrue(note_exists(clause["note"]), clause["note"])
                if "amended" in clause and "note" in clause["amended"]:
                    self.assertTrue(note_exists(clause["amended"]["note"]))

    def test_article_10_5_moved_to_4_bis(self):
        clauses = {c["id"]: c for c in self.by_id["gobernanza-del-dato"]["clauses"]}
        for cid in ["10.5", "10.5.a", "10.5.f"]:
            self.assertEqual(clauses[cid]["amended"]["status"], "suprimido")
            self.assertEqual(clauses[cid]["amended"]["moved_to"], "art. 4 bis")
        self.assertNotIn("amended", clauses["10.6"])

    def test_bias_measures(self):
        clauses = {c["id"]: c for c in self.by_id["gobernanza-del-dato"]["clauses"]}
        self.assertEqual(clauses["10.2.f"]["measures"], ["MG14", "MG15", "MG16"])


class TestParser(unittest.TestCase):
    def test_matrix_labels(self):
        self.assertEqual(aesia_measures.matrix_clause("10.2.f. Posibles sesgos"), "10.2.f")
        self.assertEqual(aesia_measures.matrix_clause("13.3.b.vii. Información de salida"), "13.3.b.vii")
        self.assertEqual(aesia_measures.matrix_clause("IV.1. a) Contenido mínimo"), "IV.1.a")
        self.assertEqual(aesia_measures.matrix_clause("IV.9. Contenido mínimo"), "IV.9")

    def test_number(self):
        self.assertEqual(aesia_measures.number("10.199999999999999"), "10.2")
        self.assertEqual(aesia_measures.number("12"), "12")

    def test_all_checklists_parse(self):
        data = miniyaml.loads(aesia_measures.generate(list(aesia_measures.CHECKLISTS)))
        self.assertEqual(len(data["checklists"]), 12)
        self.assertEqual(sum(len(m["questions"]) > 0 for c in data["checklists"] for m in c["measures"]), 193)
        self.assertEqual(sum(len(cl["measures"]) for c in data["checklists"] for cl in c["clauses"]), 510)


if __name__ == "__main__":
    unittest.main()
