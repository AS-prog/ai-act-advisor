#!/usr/bin/env python3
"""Ensayo de la demo sin Claude: recorre el guion con la auditoría y los hooks reales.

  ensayo.py            imprime cada paso y lo que recibiría Claude
  ensayo.py --quiet    solo el resultado de las comprobaciones (lo usan los tests)

Sirve para comprobar, antes de la demo en vivo, que cada aviso del guion sale donde debe.
Las skills (que son instrucciones para Claude) no se ejecutan aquí: el guion dice qué
pedirle a Claude en cada paso y qué debe contestar.

Todo pasa en una carpeta temporal que se borra al terminar. Solo librería estándar.
"""
import argparse
import io
import json
import os
import shutil
import sys
import tempfile
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import preparar  # noqa: E402

sys.path.insert(0, os.path.join(preparar.PLUGIN, "scripts"))
from aiact import core, hooks  # noqa: E402


class Ensayo:
    def __init__(self, root, quiet=False):
        self.root = root
        self.quiet = quiet
        self.ok = 0
        self.fail = []
        self.sessions = []

    # ------------------------------------------------------------ salida

    def say(self, text=""):
        if not self.quiet:
            print(text)

    def step(self, n, role, title):
        self.say(f"\n{'=' * 78}\nPaso {n} · {role} · {title}\n{'=' * 78}")

    def show(self, label, text):
        self.say(f"\n--- {label} ---")
        self.say(text.strip() if text.strip() else "(nada: el plugin calla)")

    def check(self, cond, what):
        if cond:
            self.ok += 1
            self.say(f"  [ok] {what}")
        else:
            self.fail.append(what)
            self.say(f"  [FALLA] {what}")

    # ------------------------------------------------------------ hooks

    def session(self, name):
        sid = f"ensayo-{os.getpid()}-{name}"
        self.sessions.append(sid)
        return sid

    def _run(self, fn, payload):
        buf = io.StringIO()
        with redirect_stdout(buf):
            fn(payload)
        out = buf.getvalue().strip()
        if not out:
            return ""
        data = json.loads(out)
        return data["hookSpecificOutput"]["additionalContext"]

    def session_start(self, sid):
        return self._run(hooks.session_start, {"session_id": sid, "cwd": self.root,
                                               "hook_event_name": "SessionStart"})

    def tool(self, sid, tool, rel):
        return self._run(hooks.post_tool_use, {
            "session_id": sid, "cwd": self.root, "hook_event_name": "PostToolUse",
            "tool_name": tool, "tool_input": {"file_path": os.path.join(self.root, rel)}})

    def cleanup(self):
        for sid in self.sessions:
            try:
                os.remove(hooks._state_path(sid))
            except OSError:
                pass

    # ------------------------------------------------------------ estado

    def baseline(self):
        return core.load_json(os.path.join(self.root, ".ai-act", "baseline.json"), {}).get("findings", {})

    def decide(self, rule, status, justification):
        path = os.path.join(self.root, ".ai-act", "baseline.json")
        base = core.load_json(path, {})
        hit = [fid for fid, f in base["findings"].items() if f["rule"] == rule]
        for fid in hit:
            base["findings"][fid]["status"] = status
            base["findings"][fid]["justification"] = justification
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(base, fh, ensure_ascii=False, indent=2)
        return hit

    def set_classification(self, level):
        path = os.path.join(self.root, ".ai-act", "profile.yaml")
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        text = text.replace("ai_act_level: out-of-scope", f"ai_act_level: {level}")
        text = text.replace("deliverable_infers: false", "deliverable_infers: true")
        text = text.replace("ai_type: []", "ai_type: [ml, llm]")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)

    def counts(self):
        by = {}
        for f in self.baseline().values():
            key = (f.get("status"), f.get("severity"))
            by[key] = by.get(key, 0) + 1
        return "\n".join(f"{st} · {sev}: {n}" for (st, sev), n in sorted(by.items()))

    def summary(self, result):
        sev = {}
        for f in result["findings"]:
            sev[f["severity"]] = sev.get(f["severity"], 0) + 1
        return ", ".join(f"{n} {s}" for s, n in sorted(sev.items(), key=lambda kv: ["alta", "media", "baja"].index(kv[0])))

    # ------------------------------------------------------------ guion

    def run(self):
        # ---------------------------------------------------- fase 1
        self.step(1, "PM", "abre Claude Code en un repo sin configurar")
        pm = self.session("pm")
        ctx = self.session_start(pm)
        self.show("Contexto de SessionStart", ctx)
        self.check("/project-init" in ctx, "sugiere /project-init porque no hay perfil")

        self.step(2, "PM", "/project-init: auditoría de solo lectura, perfil y estado en .ai-act/")
        result = core.audit(self.root)
        envs = [e["name"] for e in result["environments"]]
        rules = sorted({f["rule"] for f in result["findings"]})
        self.show("Entornos", ", ".join(envs))
        self.show("Hallazgos", f"{len(result['findings'])} ({self.summary(result)}): " + ", ".join(rules))
        self.check({"Delta Lake", "PostgreSQL", "SharePoint", "Google Cloud Storage"} <= set(envs),
                   "detecta Delta, PostgreSQL, SharePoint y GCS")
        self.check("SDK de LLM" not in envs and "scoring-model" not in rules,
                   "fase 1 sin señales del AI Act (no hay modelos ni LLM)")
        self.check({"source-without-pii", "pii-declared-not-applied", "external-export",
                    "bronze-schema-merge", "no-erasure"} <= set(rules),
                   "encuentra los cinco riesgos de RGPD del ejemplo")

        os.makedirs(os.path.join(self.root, ".ai-act"), exist_ok=True)
        shutil.copy(os.path.join(HERE, "perfil.yaml"), os.path.join(self.root, ".ai-act", "profile.yaml"))
        paths = core.write_outputs(self.root, result)
        self.show("Ficheros escritos", "\n".join(os.path.relpath(p, self.root) for p in paths.values()))
        with open(paths["report"], encoding="utf-8") as fh:
            report = fh.read()
        self.check("No es asesoramiento legal" in report and "## AI Act" in report,
                   "el informe lleva el aviso legal y dice que el proyecto queda fuera del AI Act")

        self.step(3, "PM", "registra una decisión en la línea base")
        hit = self.decide("external-export", "aceptado",
                          "Contrato de encargado firmado con el socio de medios; bucket en la UE (ficticio). Decide: PM")
        self.show("Decisión", "external-export → aceptado, con justificación")
        self.check(len(hit) == 1, "la exportación queda aceptada con justificación")
        core.write_outputs(self.root, core.audit(self.root))
        kept = [f for f in self.baseline().values() if f["rule"] == "external-export"]
        self.check(kept and kept[0]["status"] == "aceptado", "relanzar la auditoría conserva la decisión")

        self.step(4, "DE", "abre su sesión y lee la Silver de clientes")
        de = self.session("de")
        ctx = self.session_start(de)
        self.show("Contexto de SessionStart", ctx)
        self.check("retail-marketing" in ctx and "out-of-scope" in ctx, "resume el perfil: sector y clasificación")
        self.check("severidad alta abiertos" in ctx, "recuerda cuántos hallazgos altos siguen abiertos")
        ctx = self.tool(de, "Read", "transform/silver/build_customers.py")
        self.show("Aviso al leer build_customers.py", ctx)
        self.check(ctx == "", "calla: ese riesgo ya está en la línea base")

        self.step(5, "DE", "añade una fuente nueva de SharePoint sin declarar la PII")
        with open(os.path.join(self.root, "config", "sources", "sharepoint.yaml"), "a", encoding="utf-8") as fh:
            fh.write("  - name: newsletter_signups\n    library: Marketing\n    sheet: altas_newsletter\n    active: true\n")
        ctx = self.tool(de, "Edit", "config/sources/sharepoint.yaml")
        self.show("Aviso al editar sharepoint.yaml", ctx)
        self.check("newsletter_signups" in ctx and "pii-masking" in ctx, "avisa del objeto nuevo y apunta a pii-masking")
        self.check("campaign_contacts" not in ctx, "no repite el objeto que ya estaba en la línea base")
        self.check("No es asesoramiento legal" in ctx and "Base normativa" in ctx, "lleva fecha de la base y aviso legal")
        again = self.tool(de, "Edit", "config/sources/sharepoint.yaml")
        self.check(again == "", "el mismo aviso no se repite en la sesión")

        self.step(6, "AE", "crea un modelo Gold de clientes por ciudad y edad")
        ae = self.session("ae")
        os.makedirs(os.path.join(self.root, "transform", "gold"), exist_ok=True)
        with open(os.path.join(self.root, "transform", "gold", "customers_by_age.sql"), "w", encoding="utf-8") as fh:
            fh.write("select city, date_diff('year', birth_date, current_date) as age, count(*) as customers\n"
                     "from silver_customers\ngroup by 1, 2\n")
        ctx = self.tool(ae, "Write", "transform/gold/customers_by_age.sql")
        self.show("Aviso al escribir customers_by_age.sql", ctx)
        self.check("birth_date" in ctx and "pii-masking" in ctx, "avisa de birth_date en Gold y apunta a pii-masking")

        self.step(7, "PM", "/risk-summary al cierre de la fase 1")
        core.write_outputs(self.root, core.audit(self.root))
        phase1_ids = set(self.baseline())
        self.show("Recuento", self.counts())
        self.check(any(f.get("status") == "aceptado" and f.get("justification") for f in self.baseline().values()),
                   "el resumen tiene un aceptado con justificación")

        # ---------------------------------------------------- fase 2
        self.step(8, "DE", "fase 2: añade las dependencias del modelo y del chatbot")
        copied = preparar.phase2(self.root)
        self.show("Ficheros de la fase 2 (preparar.py --fase 2)", "\n".join(copied))
        # En vivo se lo pide el DE a Claude: «añade scikit-learn y anthropic a las dependencias».
        path = os.path.join(self.root, "pyproject.toml")
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text.replace('  "google-cloud-storage",\n', '  "google-cloud-storage",\n  "scikit-learn",\n  "anthropic",\n'))
        ctx = self.tool(de, "Edit", "pyproject.toml")
        self.show("Aviso al editar pyproject.toml", ctx)
        self.check("relanzar /project-init" in ctx and "SDK de LLM" in ctx and "Librerías de ML" in ctx,
                   "detecta entornos nuevos (ML y LLM) y sugiere relanzar /project-init")

        self.step(9, "DE", "revisa la fuente de solicitudes de pago a plazos")
        ctx = self.tool(de, "Read", "config/sources/crm_postgres.yaml")
        self.show("Aviso al leer crm_postgres.yaml", ctx)
        self.check("instalment_applications" in ctx, "avisa de las solicitudes de pago a plazos sin PII declarada")

        self.step(10, "DE", "revisa el asistente de la web")
        ctx = self.tool(de, "Read", "assistant/support_bot.py")
        self.show("Aviso al leer assistant/support_bot.py", ctx)
        self.check("art. 50" in ctx and "ai-transparency" in ctx, "chatbot: art. 50, skill ai-transparency")

        self.step(11, "AE", "revisa la encuesta de accesibilidad")
        ctx = self.tool(ae, "Read", "transform/silver/accessibility_survey.sql")
        self.show("Aviso al leer accessibility_survey.sql", ctx)
        self.check("art. 9" in ctx and "special-categories" in ctx and "DPO" in ctx,
                   "encuesta: categoría especial (art. 9), skill special-categories, escala al DPO")

        self.step(12, "DE y PM", "revisa el modelo de impago y lo clasifica con /ai-act-classify")
        ctx = self.tool(de, "Read", "ml/instalment_scoring.py")
        self.show("Aviso al leer ml/instalment_scoring.py", ctx)
        self.check("ai-act-classify" in ctx and "anexo III" in ctx and "2027-12-02" in ctx,
                   "modelo que puntúa: anexo III, desde 2027-12-02, skill ai-act-classify")
        core.write_outputs(self.root, core.audit(self.root))
        self.decide("scoring-model", "aceptado",
                    "Candidato a alto riesgo, anexo III 5.b (solvencia de personas físicas). Rol por confirmar con "
                    "legal. Confirmado por el PM; obligaciones de alto riesgo desde 2027-12-02")
        self.set_classification("high-risk-candidate")
        ctx = self.session_start(self.session("de-2"))
        self.show("SessionStart tras clasificar", ctx)
        self.check("high-risk-candidate" in ctx, "el perfil refleja la clasificación confirmada")
        ctx = self.tool(self.session("de-3"), "Read", "ml/instalment_scoring.py")
        self.check(ctx == "", "el modelo ya clasificado no vuelve a avisar")

        self.step(13, "PM", "relanza /project-init y /risk-summary")
        result = core.audit(self.root)
        new = [f for f in result["findings"] if f["id"] not in phase1_ids]
        self.show("Hallazgos nuevos desde la fase 1",
                  "\n".join(f"[{f['severity']}] {f['title']} · {f['norma']} {', '.join(f['articulos'])}" for f in new))
        self.check({"scoring-model", "llm-sdk", "special-category-terms", "source-without-pii"} <= {f["rule"] for f in new},
                   "la auditoría recoge los riesgos nuevos de la fase 2")
        core.write_outputs(self.root, result)
        base = self.baseline()
        self.show("Recuento", self.counts())
        accepted = [f for f in base.values() if f.get("status") == "aceptado"]
        self.check(len(accepted) == 2 and all(f.get("justification") for f in accepted),
                   "dos riesgos aceptados, los dos con justificación")
        self.check(any(f.get("status") == "abierto" and f.get("severity") == "alta" for f in base.values()),
                   "quedan altos abiertos que escalar")

        # ---------------------------------------------------- mantenimiento
        self.step(14, "Mantenimiento", "la base normativa tiene más de 90 días")
        tmp = tempfile.mkdtemp()
        try:
            target = preparar.old_knowledge(os.path.join(tmp, "demo"))
            saved = core.KNOWLEDGE
            core.KNOWLEDGE = target
            try:
                ctx = self.session_start(self.session("mant"))
            finally:
                core.KNOWLEDGE = saved
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        self.show("Contexto de SessionStart con la base atrasada", ctx)
        self.check("/regulatory-update" in ctx and "120 días" in ctx, "sugiere /regulatory-update")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)
    tmp = tempfile.mkdtemp(prefix="ai-act-ensayo-")
    root = os.path.join(tmp, "medallion-demo")
    saved_env = os.environ.pop("CLAUDE_PROJECT_DIR", None)
    os.environ["CLAUDE_PROJECT_DIR"] = root
    e = Ensayo(root, args.quiet)
    try:
        preparar.phase1(root)
        e.run()
    finally:
        e.cleanup()
        shutil.rmtree(tmp, ignore_errors=True)
        os.environ.pop("CLAUDE_PROJECT_DIR", None)
        if saved_env is not None:
            os.environ["CLAUDE_PROJECT_DIR"] = saved_env
    total = e.ok + len(e.fail)
    print(f"\nEnsayo: {e.ok} de {total} comprobaciones correctas.")
    for what in e.fail:
        print(f"  Falla: {what}")
    return 0 if not e.fail else 1


if __name__ == "__main__":
    sys.exit(main())
