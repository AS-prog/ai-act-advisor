"""Tests del primer corte (PII en la ingesta). Solo librería estándar:

    python -m unittest discover -s tests -v
"""

import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "plugins", "ai-act-advisor", "scripts")
EXAMPLE = os.path.join(ROOT, "examples", "medallion-demo")
sys.path.insert(0, SCRIPTS)

from aiact import core, hooks, miniyaml  # noqa: E402


def rules_of(result):
    return sorted({f["rule"] for f in result["findings"]})


class MiniYamlTest(unittest.TestCase):
    def test_lists_of_maps_and_inline(self):
        data = miniyaml.loads(
            "objects:\n  - name: a  # comentario\n    pii_columns: [email, 'dni']\n  - name: b\n"
        )
        self.assertEqual(data, {"objects": [{"name": "a", "pii_columns": ["email", "dni"]}, {"name": "b"}]})

    def test_sequence_at_key_indent_and_block_scalar(self):
        data = miniyaml.loads("k:\n- x\n- y\ntexto: |\n  uno\n  dos\nn: 3\nok: true\nnada: ~\n")
        self.assertEqual(data, {"k": ["x", "y"], "texto": "uno\ndos", "n": 3, "ok": True, "nada": None})

    def test_knowledge_files_parse(self):
        for name in ("signals.yaml", "dates.yaml", "sources.yaml", "sectors.yaml"):
            self.assertIsNotNone(miniyaml.load(os.path.join(core.KNOWLEDGE, name)), name)


class TermsTest(unittest.TestCase):
    def setUp(self):
        self.signals, _ = core.load_knowledge()

    def test_word_boundaries_avoid_false_positives(self):
        rx = core.term_regex(self.signals["pii_terms"])
        text = "planificadas fullmatch predicate model schema_hash quick_xor movil"
        self.assertEqual(core.terms_in(text, rx, set(self.signals["exclusions"])), set())

    def test_underscore_is_a_boundary(self):
        rx = core.term_regex(self.signals["pii_terms"])
        self.assertEqual(core.terms_in("select cliente_nif, customer_email from t", rx, set()), {"nif", "email"})


class AuditTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = core.audit(EXAMPLE)

    def test_environments(self):
        names = {e["name"] for e in self.result["environments"]}
        self.assertTrue({"Delta Lake", "DuckDB", "PostgreSQL", "SharePoint", "Google Cloud Storage"} <= names)
        self.assertNotIn("SDK de LLM", names)

    def test_repo_rules(self):
        r = self.result["rules"]
        self.assertEqual(r["pii_key"], "pii_columns")
        self.assertEqual(r["source_configs"], ["config/sources/crm_postgres.yaml", "config/sources/sharepoint.yaml"])
        self.assertEqual(r["bronze_writers"], ["ingestion/bronze/writer.py"])
        self.assertEqual(r["exports"], ["transform/gold/exports/partner_upload.py"])

    def test_findings(self):
        self.assertEqual(
            rules_of(self.result),
            ["bronze-schema-merge", "external-export", "no-erasure", "pii-declared-not-applied",
             "pii-terms", "source-without-pii"],
        )
        missing = sorted(f["title"] for f in self.result["findings"] if f["rule"] == "source-without-pii")
        self.assertEqual(len(missing), 2)
        self.assertTrue(any("subscriptions" in t for t in missing))
        self.assertTrue(any("campaign_contacts" in t for t in missing))

    def test_no_findings_from_tests_or_source_declarations(self):
        evidence = {p for f in self.result["findings"] for p in f["evidence"]}
        self.assertFalse(any(p.startswith("tests/") for p in evidence))
        self.assertFalse(any(f["rule"] == "pii-terms" and f["evidence"] == ["config/sources/crm_postgres.yaml"]
                             for f in self.result["findings"]))

    def test_every_finding_cites_norm_and_date(self):
        for f in self.result["findings"]:
            self.assertIn(f["norma"], ("RGPD", "AI Act"))
            self.assertTrue(f["articulos"])
            self.assertTrue(f["aplica"])


class RepoCopy(unittest.TestCase):
    """Copia el ejemplo a una carpeta temporal para poder escribir .ai-act/."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = os.path.join(self.tmp, "repo")
        shutil.copytree(EXAMPLE, self.root)
        self.session = f"test-{id(self)}"
        os.environ["CLAUDE_PROJECT_DIR"] = self.root

    def tearDown(self):
        os.environ.pop("CLAUDE_PROJECT_DIR", None)
        shutil.rmtree(self.tmp, ignore_errors=True)
        try:
            os.remove(hooks._state_path(self.session))
        except OSError:
            pass

    def run_hook(self, fn, payload):
        buf = io.StringIO()
        with redirect_stdout(buf):
            fn(payload)
        out = buf.getvalue().strip()
        return json.loads(out)["hookSpecificOutput"]["additionalContext"] if out else ""

    def edit(self, rel, tool="Edit"):
        return self.run_hook(hooks.post_tool_use, {
            "session_id": self.session, "cwd": self.root, "tool_name": tool,
            "tool_input": {"file_path": os.path.join(self.root, rel)},
        })


class WriteAndBaselineTest(RepoCopy):
    def test_write_outputs_and_keep_status(self):
        result = core.audit(self.root)
        paths = core.write_outputs(self.root, result)
        for p in paths.values():
            self.assertTrue(os.path.exists(p), p)
        with open(paths["report"], encoding="utf-8") as fh:
            report = fh.read()
        self.assertIn("No es asesoramiento legal", report)
        self.assertIn("## Hallazgos", report)

        base = core.load_json(paths["baseline"], {})
        fid = next(iter(base["findings"]))
        base["findings"][fid]["status"] = "aceptado"
        base["findings"][fid]["justification"] = "Riesgo asumido por el cliente"
        with open(paths["baseline"], "w", encoding="utf-8") as fh:
            json.dump(base, fh)
        core.write_outputs(self.root, core.audit(self.root))
        again = core.load_json(paths["baseline"], {})
        self.assertEqual(again["findings"][fid]["status"], "aceptado")
        self.assertEqual(again["findings"][fid]["justification"], "Riesgo asumido por el cliente")


class HooksTest(RepoCopy):
    def test_session_start_without_profile_suggests_init(self):
        ctx = self.run_hook(hooks.session_start, {"cwd": self.root})
        self.assertIn("/project-init", ctx)

    def test_session_start_with_profile_summarises(self):
        os.makedirs(os.path.join(self.root, ".ai-act"))
        shutil.copy(os.path.join(ROOT, "plugins", "ai-act-advisor", "skills", "project-init", "profile.example.yaml"),
                    os.path.join(self.root, ".ai-act", "profile.yaml"))
        ctx = self.run_hook(hooks.session_start, {"cwd": self.root})
        self.assertIn("insurance-life-health", ctx)

    def test_new_object_without_pii_key_warns_once(self):
        core.write_outputs(self.root, core.audit(self.root))  # línea base actual
        path = os.path.join(self.root, "config", "sources", "crm_postgres.yaml")
        with open(path, "a", encoding="utf-8") as fh:
            fh.write("  - name: complaints\n    schema: crm\n")
        ctx = self.edit("config/sources/crm_postgres.yaml")
        self.assertIn("complaints", ctx)
        self.assertNotIn("subscriptions", ctx)  # ya está en la línea base
        self.assertIn("No es asesoramiento legal", ctx)
        self.assertEqual(self.edit("config/sources/crm_postgres.yaml"), "")  # una vez por sesión

    def test_baseline_silences_known_findings(self):
        core.write_outputs(self.root, core.audit(self.root))
        self.assertEqual(self.edit("transform/gold/exports/partner_upload.py"), "")
        self.assertEqual(self.edit("ingestion/bronze/writer.py"), "")

    def test_without_rules_still_flags_pii_terms_and_suggests_init(self):
        ctx = self.edit("transform/silver/build_customers.py", tool="Read")
        self.assertIn("email", ctx)
        self.assertIn("/project-init", ctx)

    def test_new_llm_dependency_suggests_reaudit(self):
        core.write_outputs(self.root, core.audit(self.root))
        with open(os.path.join(self.root, "pyproject.toml"), "a", encoding="utf-8") as fh:
            fh.write('\n[project.optional-dependencies]\nllm = ["openai>=1.40", "scikit-learn"]\n')
        ctx = self.edit("pyproject.toml")
        self.assertIn("relanzar /project-init", ctx)
        self.assertIn("SDK de LLM", ctx)
        self.assertIn("Librerías de ML", ctx)

    def test_dependency_names_need_whole_words(self):
        signals, _ = core.load_knowledge()
        envs = core.detect_environments([("requirements.txt", "openaire-client==1\nmy-torchlight\n")], signals)
        self.assertEqual(envs, [])

    def test_hook_never_blocks(self):
        core.write_outputs(self.root, core.audit(self.root))
        path = os.path.join(self.root, "config", "sources", "sharepoint.yaml")
        with open(path, "a", encoding="utf-8") as fh:
            fh.write("  - name: newsletter_signups\n    library: Marketing\n")
        buf = io.StringIO()
        with redirect_stdout(buf):
            hooks.post_tool_use({"session_id": self.session, "cwd": self.root, "tool_name": "Write",
                                 "tool_input": {"file_path": path}})
        out = json.loads(buf.getvalue())
        self.assertNotIn("decision", out)
        self.assertNotIn("permissionDecision", json.dumps(out))

    def test_ignores_files_outside_repo_and_secrets(self):
        self.assertEqual(self.run_hook(hooks.post_tool_use, {
            "session_id": self.session, "cwd": self.root, "tool_name": "Read",
            "tool_input": {"file_path": "/etc/hosts"}}), "")
        with open(os.path.join(self.root, ".env"), "w") as fh:
            fh.write("email=x\n")
        self.assertEqual(self.edit(".env"), "")


class OtherAgentsTest(RepoCopy):
    """Eventos con los campos de otros agentes, para la instalación con APM."""

    def test_copilot_payload_with_tool_args_as_text(self):
        rel = os.path.join(self.root, "transform/silver/build_customers.py")
        ctx = self.run_hook(hooks.post_tool_use, {
            "sessionId": self.session, "cwd": self.root, "toolName": "view", "toolArgs": json.dumps({"path": rel})})
        self.assertIn("email", ctx)

    def test_copilot_and_cursor_read_top_level_context(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            hooks.session_start({"cwd": self.root, "source": "new"})
        out = json.loads(buf.getvalue())
        self.assertIn("/project-init", out["additionalContext"])
        self.assertEqual(out["additionalContext"], out["additional_context"])

    def test_claude_output_has_no_extra_keys(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            hooks.session_start({"cwd": self.root, "hook_event_name": "SessionStart"})
        self.assertEqual(list(json.loads(buf.getvalue())), ["hookSpecificOutput"])

    def test_codex_apply_patch_finds_the_file(self):
        patch = "*** Begin Patch\n*** Update File: transform/silver/build_customers.py\n@@\n-x\n+y\n*** End Patch"
        ctx = self.run_hook(hooks.post_tool_use, {
            "session_id": self.session, "cwd": self.root, "hook_event_name": "PostToolUse",
            "tool_name": "apply_patch", "tool_input": {"command": patch}})
        self.assertIn("email", ctx)

    def test_gemini_payload_keeps_its_event_name(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            hooks.post_tool_use({"session_id": self.session, "cwd": self.root, "hook_event_name": "AfterTool",
                                 "tool_name": "read_file",
                                 "tool_input": {"file_path": os.path.join(self.root, "transform/silver/build_customers.py")}})
        self.assertEqual(json.loads(buf.getvalue())["hookSpecificOutput"]["hookEventName"], "AfterTool")


class EntryPointsTest(unittest.TestCase):
    def test_hook_entry_point_survives_bad_input(self):
        import subprocess
        p = subprocess.run([sys.executable, os.path.join(SCRIPTS, "hook.py"), "post-tool-use"],
                           input="no es json", capture_output=True, text=True)
        self.assertEqual(p.returncode, 0)
        self.assertEqual(p.stdout, "")

    def test_knowledge_next_to_scripts_as_apm_installs_it(self):
        """APM copia scripts/ y knowledge/ a una carpeta del agente; el hook debe encontrar la base."""
        import subprocess
        tmp = tempfile.mkdtemp()
        try:
            dest = os.path.join(tmp, ".github", "hooks", "scripts", "ai-act-advisor")
            plugin = os.path.dirname(SCRIPTS)
            shutil.copytree(SCRIPTS, os.path.join(dest, "scripts"))
            shutil.copytree(os.path.join(plugin, "knowledge"), os.path.join(dest, "knowledge"))
            env = {k: v for k, v in os.environ.items() if k not in ("CLAUDE_PLUGIN_ROOT", "CLAUDE_PROJECT_DIR")}
            env["AI_ACT_DEBUG"] = "1"
            p = subprocess.run(
                ["sh", os.path.join(dest, "scripts", "run.sh"), "hook.py", "session-start",
                 os.path.join(dest, "knowledge", "VERSION")],
                input=json.dumps({"cwd": tmp}), capture_output=True, text=True, env=env)
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertIn("/project-init", p.stdout)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
