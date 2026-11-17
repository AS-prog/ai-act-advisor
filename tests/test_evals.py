"""Los casos de `claude plugin eval` salen de consultas-citas.json y deben estar al día.

    python -m unittest tests.test_evals -v
"""

import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENERADOR = os.path.join(ROOT, "plugins", "ai-act-advisor", "evals", "generate.py")


class CasosDeEvalTest(unittest.TestCase):
    def test_los_casos_estan_regenerados(self):
        r = subprocess.run([sys.executable, GENERADOR, "--check"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
