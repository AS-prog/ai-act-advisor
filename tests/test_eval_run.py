"""Tests de evals/run.py (CLI de evals por modelo). Solo librería estándar."""

import importlib.util
import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("eval_run", os.path.join(ROOT, "plugins", "ai-act-advisor", "evals", "run.py"))
run = importlib.util.module_from_spec(spec)
spec.loader.exec_module(run)


def pasada(**graders):
    return {"graders": [{"name": n, "passed": p} for n, p in graders.items()]}


RESULTADO = {
    "startedAt": "2026-11-17T20:00:00.000Z",
    "costUsd": 0.5,
    "durationSeconds": 30,
    "partial": False,
    "suite": {"judgeModel": "sonnet", "tagFilters": ["humo"]},
    "aggregates": {"casesTotal": 2, "overallScore": 0.75, "overallPassRate": 0.5, "meanDelta": 0.4},
    "cases": [
        {"name": "a", "aggregates": {"score": 1, "scoreWithout": 0.5, "delta": 0.5, "passRateWithout": 0},
         "arms": {"with": [pasada(**{"usa-skill": True, "nota-recuperada": True}), pasada(**{"usa-skill": True, "nota-recuperada": False})]}},
        {"name": "b", "aggregates": {"score": 0.5, "scoreWithout": 0.2, "delta": 0.3, "passRateWithout": 0},
         "arms": {"with": [pasada(**{"usa-skill": False}), pasada(**{"usa-skill": False})]}},
    ],
}


class FilasTest(unittest.TestCase):
    def test_ejecucion_y_casos(self):
        e, casos = run.filas(RESULTADO, "m", "", commit="abc", sha="def")
        self.assertEqual((e["modelo"], e["juez"], e["filtro"], e["casos"], e["pasadas"]), ("m", "sonnet", "humo", 2, 2))
        self.assertEqual((e["puntos_con"], e["puntos_sin"], e["delta"]), (0.75, 0.35, 0.4))
        self.assertEqual(e["skill_activa"], 0.5)  # 1,0 en «a» y 0,0 en «b»
        self.assertEqual(e["nota_recuperada"], 0.5)  # solo «a» lo tiene
        self.assertEqual([c["caso"] for c in casos], ["a", "b"])
        self.assertEqual(casos[1]["nota_recuperada"], "")

    def test_comando_fija_juez_y_modelo(self):
        import argparse
        args = argparse.Namespace(juez="sonnet", publicar=False, tag=["humo"], caso=None, runs=1, max_cost=3, concurrencia=None)
        cmd = run.comando(args, "claude-haiku-5-5", "/tmp/x.json")
        self.assertIn("--model", cmd)
        self.assertEqual(cmd[cmd.index("--judge-model") + 1], "sonnet")
        self.assertIn("--no-publish", cmd)


if __name__ == "__main__":
    unittest.main()
