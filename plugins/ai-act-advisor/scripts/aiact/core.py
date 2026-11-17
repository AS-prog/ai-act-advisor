"""Núcleo de la auditoría: recorre el repo, detecta entornos, genera las
reglas del repo y los hallazgos de riesgo.

Reglas de seguridad (Q16b, Q23d): solo lectura; nunca abre credenciales,
secretos ni ficheros de datos; de un profiles.yml solo lee las líneas «type:».
"""

import datetime as _dt
import fnmatch
import hashlib
import json
import os
import re

from . import miniyaml

PLUGIN_ROOT = os.environ.get("CLAUDE_PLUGIN_ROOT") or os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
KNOWLEDGE = os.path.join(PLUGIN_ROOT, "knowledge")
STATE_DIR = ".ai-act"

SKIP_DIRS = {
    ".git", ".hg", ".svn", "node_modules", ".venv", "venv", "env", "__pycache__",
    ".mypy_cache", ".pytest_cache", ".ruff_cache", ".tox", "dist", "build",
    "site-packages", ".idea", ".vscode", STATE_DIR, "data", "datasets",
}
TEXT_EXT = {
    ".py", ".sql", ".yml", ".yaml", ".toml", ".cfg", ".ini", ".ipynb", ".md",
    ".ps1", ".sh", ".tf", ".txt", ".scala", ".r", ".R",
}
CODE_EXT = {".py", ".sql", ".yml", ".yaml", ".ipynb", ".scala", ".r", ".R"}
DATA_EXT = {
    ".csv", ".tsv", ".parquet", ".avro", ".orc", ".xlsx", ".xls", ".json",
    ".jsonl", ".ndjson", ".db", ".sqlite", ".duckdb", ".pkl", ".feather",
}
SECRET_PATTERNS = [
    ".env", ".env.*", "*secret*", "*credential*", "*.pem", "*.key", "*.p12",
    "*.pfx", "id_rsa*", "*token*", "*.kdbx",
]
MAX_BYTES = 1_000_000


# ---------------------------------------------------------------- utilidades

def today():
    return _dt.date.today().isoformat()


def load_knowledge():
    signals = miniyaml.load(os.path.join(KNOWLEDGE, "signals.yaml")) or {}
    version = miniyaml.load(os.path.join(KNOWLEDGE, "VERSION")) or {}
    return signals, version


def is_secret(name):
    low = name.lower()
    return any(fnmatch.fnmatch(low, p) for p in SECRET_PATTERNS)


def term_regex(terms):
    """Casa cada término como identificador completo («_» separa)."""
    alt = "|".join(sorted((re.escape(t.lower()) for t in terms), key=len, reverse=True))
    return re.compile(r"(?<![a-z0-9])(" + alt + r")(?![a-z0-9])")


def import_regex(modules):
    alt = "|".join(re.escape(m) for m in modules)
    return re.compile(
        r"^\s*(?:from\s+(" + alt + r")(?:\.|\s)|import\s+(" + alt + r")(?:\.|\s|$|,))",
        re.MULTILINE,
    )


def finding_id(rule, *parts):
    h = hashlib.sha1("|".join((rule,) + parts).encode("utf-8")).hexdigest()[:10]
    return f"{rule}:{h}"


def read_text(path):
    """Lee un fichero de texto del repo respetando las reglas de seguridad."""
    name = os.path.basename(path)
    ext = os.path.splitext(name)[1]
    if is_secret(name) or ext.lower() in DATA_EXT:
        return None
    try:
        if os.path.getsize(path) > MAX_BYTES:
            return None
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError:
        return None
    if name == "profiles.yml":
        # De un profiles.yml de dbt solo interesa el tipo de adaptador.
        return "\n".join(l for l in text.splitlines() if re.match(r"\s*type\s*:", l))
    if ext == ".ipynb":
        try:
            nb = json.loads(text)
            cells = [
                "".join(c.get("source", []))
                for c in nb.get("cells", [])
                if c.get("cell_type") in ("code", "markdown")
            ]
            return "\n".join(cells)
        except ValueError:
            return None
    return text


def walk(root):
    """Ficheros de texto del repo, con ruta relativa en formato POSIX."""
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")
                       or d in (".github", ".azuredevops")]
        for fn in filenames:
            ext = os.path.splitext(fn)[1]
            if ext not in TEXT_EXT and fn not in ("Dockerfile",):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            yield rel, full


def is_test(rel):
    parts = rel.lower().split("/")
    return any(p in ("tests", "test", "testing", "fixtures") for p in parts[:-1]) or \
        parts[-1].startswith("test_") or parts[-1].endswith("_test.py")


# ---------------------------------------------------------------- entornos

ENVIRONMENTS = [
    # (nombre, fichero que lo delata, regex sobre el contenido de código/config)
    ("dbt", ["dbt_project.yml"], None),
    ("Databricks", ["databricks.yml"], r"\bdatabricks\b"),
    ("Microsoft Fabric", [".platform", "notebook-content.py"],
     r"\b(notebookutils|mssparkutils|fabric|lakehouse)\b"),
    ("Spark", [], r"\b(pyspark|sparksession|spark\.read|spark\.sql)\b"),
    ("Delta Lake", [], r"\b(deltalake|delta-spark|write_deltalake|format\(\s*[\"']delta)"),
    ("DuckDB", [], r"\bduckdb\b"),
    ("PostgreSQL", [], r"\b(psycopg2?|postgres(ql)?|asyncpg)\b"),
    ("SQL Server", [], r"\b(pyodbc|sqlserver|mssql|pymssql)\b"),
    ("SharePoint", [], r"\b(sharepoint|graph\.microsoft\.com)\b"),
    ("BigQuery", [], r"\b(bigquery|google-cloud-bigquery)\b"),
    ("Snowflake", [], r"\bsnowflake\b"),
    ("Salesforce", [], r"\b(simple[-_]salesforce|salesforce)\b"),
    ("Airflow", [], r"\bfrom\s+airflow\b|\bimport\s+airflow\b"),
    ("Terraform", [], None),
    ("Azure DevOps", ["azure-pipelines.yml"], None),
    ("Google Cloud Storage", [], r"\b(google\.cloud\s+import\s+storage|google\.cloud\.storage|gcsfs)\b"),
    ("Amazon S3", [], r"\b(boto3|s3fs)\b"),
    ("Notebooks Jupyter", [], None),
    ("SDK de LLM", [], None),
    ("Librerías de ML", [], None),
]


def detect_environments(files, signals):
    """files: lista de (rel, texto). Devuelve [{name, evidence:[...], source}]."""
    found = {}

    def add(name, rel, how):
        e = found.setdefault(name, {"name": name, "evidence": [], "source": how})
        if rel not in e["evidence"] and len(e["evidence"]) < 5:
            e["evidence"].append(rel)
        if how == "código" and e["source"] == "documentación":
            e["source"] = "código"

    llm = import_regex(signals.get("llm_imports", []))
    ml = import_regex(signals.get("ml_imports", []))
    for rel, text in files:
        base = rel.rsplit("/", 1)[-1]
        ext = os.path.splitext(base)[1]
        how = "documentación" if ext in (".md", ".txt") else "código"
        if ext == ".tf":
            add("Terraform", rel, "código")
        if ext == ".ipynb":
            add("Notebooks Jupyter", rel, "código")
        if base == "profiles.yml":
            for m in re.finditer(r"type\s*:\s*['\"]?(\w+)", text or ""):
                add({"bigquery": "BigQuery", "snowflake": "Snowflake", "databricks": "Databricks",
                     "postgres": "PostgreSQL", "sqlserver": "SQL Server", "fabric": "Microsoft Fabric",
                     "duckdb": "DuckDB", "spark": "Spark"}.get(m.group(1).lower(), m.group(1)), rel, "código")
        for name, marker_files, rx in ENVIRONMENTS:
            if base in marker_files:
                add(name, rel, "código")
            elif rx and text and re.search(rx, text, re.IGNORECASE):
                add(name, rel, how)
        if text and how == "código":
            if llm.search(text):
                add("SDK de LLM", rel, "código")
            if ml.search(text):
                add("Librerías de ML", rel, "código")
    order = {n: i for i, (n, _, _) in enumerate(ENVIRONMENTS)}
    return sorted(found.values(), key=lambda e: order.get(e["name"], 99))


# ---------------------------------------------------------------- reglas del repo

TABLE_KEYS = ("name", "table", "object", "source_table", "table_name", "dataset", "sheet", "id")
SCHEMA_MERGE = re.compile(r"""schema_mode\s*=\s*["']merge["']|mergeSchema["']?\s*[,=:)]\s*["']?true""", re.I)
DELTA_WRITE = re.compile(r"write_deltalake|\.format\(\s*[\"']delta[\"']\)|saveAsTable|\.write\.", re.I)


def _objects(node, path=()):
    """Mapas dentro de listas que parecen la declaración de una tabla u objeto."""
    if isinstance(node, list):
        for i, item in enumerate(node):
            if isinstance(item, dict) and any(k in item for k in TABLE_KEYS):
                yield path + (i,), item
            yield from _objects(item, path + (i,))
    elif isinstance(node, dict):
        for k, v in node.items():
            yield from _objects(v, path + (k,))


def _obj_name(obj):
    for k in TABLE_KEYS:
        if obj.get(k) not in (None, ""):
            return str(obj[k])
    return "?"


def find_pii_key(files):
    counts = {}
    for _rel, text in files:
        for m in re.finditer(r"(?<![a-z0-9])(pii(?:_[a-z]+)*)(?![a-z0-9])", (text or "").lower()):
            if m.group(1) != "pii":
                counts[m.group(1)] = counts.get(m.group(1), 0) + 1
    if not counts:
        return None
    return max(counts.items(), key=lambda kv: kv[1])[0]


def is_source_config(rel, text, pii_key):
    if not rel.endswith((".yml", ".yaml")) or is_test(rel):
        return False
    low = rel.lower()
    if any(p in low for p in ("source", "fuente", "ingest", "connector", "extract")):
        return True
    return bool(pii_key and text and pii_key in text)


def build_rules(root, files, signals, environments):
    pii_key = find_pii_key(files)
    code = [(r, t) for r, t in files if os.path.splitext(r)[1] in CODE_EXT]
    source_configs, bronze_writers, exports, pii_refs = [], [], [], []
    export_rx = import_regex(signals.get("export_imports", []))
    for rel, text in code:
        if not text:
            continue
        if is_source_config(rel, text, pii_key):
            data = miniyaml.loads(text)
            if any(True for _ in _objects(data)):
                source_configs.append(rel)
        if rel.endswith(".py") and not is_test(rel):
            if DELTA_WRITE.search(text) and ("bronze" in rel.lower() or "bronze" in text.lower()):
                bronze_writers.append(rel)
            if export_rx.search(text) or re.search(r"(^|/)exports?/", rel.lower()):
                exports.append(rel)
            if pii_key and pii_key in text:
                pii_refs.append(rel)
    return {
        "generated": today(),
        "pii_key": pii_key or "pii_columns",
        "pii_key_detected": bool(pii_key),
        "source_configs": sorted(source_configs),
        "bronze_writers": sorted(bronze_writers),
        "exports": sorted(exports),
        "pii_key_references": sorted(pii_refs),
        "exclusions": list(signals.get("exclusions", [])),
        "environments": [e["name"] for e in environments],
        "fingerprint": env_fingerprint(environments),
    }


def env_fingerprint(environments):
    names = sorted(e["name"] for e in environments if e.get("source") == "código")
    return hashlib.sha1("|".join(names).encode()).hexdigest()[:12]


# ---------------------------------------------------------------- hallazgos

RGPD = "RGPD"
AIACT = "AI Act"


def _f(rule, key, severity, title, norma, articulos, aplica, evidence, recommendation,
       escalate=None, skill=None, detail=None):
    return {
        "id": finding_id(rule, key),
        "rule": rule,
        "severity": severity,
        "title": title,
        "norma": norma,
        "articulos": articulos,
        "aplica": aplica,
        "evidence": evidence,
        "detail": detail or "",
        "recommendation": recommendation,
        "escalate": escalate,
        "skill": skill,
    }


def check_source_config(rel, text, pii_key):
    """Objetos declarados sin la clave de PII. Devuelve hallazgos (uno por objeto)."""
    out = []
    data = miniyaml.loads(text or "")
    for _path, obj in _objects(data):
        if pii_key not in obj:
            name = _obj_name(obj)
            out.append(_f(
                "source-without-pii", f"{rel}#{name}", "media",
                f"Objeto «{name}» sin «{pii_key}» declarado",
                RGPD, ["art. 5.1.c", "art. 25", "art. 30"], "ya",
                [rel],
                f"Revisa el esquema de origen de «{name}» antes de llevarlo a Bronze y declara "
                f"«{pii_key}» (aunque sea una lista vacía) para que conste que se revisó.",
                skill="pii-masking",
                detail="La ausencia de la clave cuenta como «no revisado»: no se sabe si el objeto trae datos personales.",
            ))
    return out


def check_schema_merge(rel, text):
    if text and SCHEMA_MERGE.search(text):
        return [_f(
            "bronze-schema-merge", rel, "media",
            "Bronze acepta columnas nuevas del origen sin revisión",
            RGPD, ["art. 25", "art. 5.1.c"], "ya", [rel],
            "Antes de aceptar una columna nueva, compárala con la declaración de PII del objeto o "
            "avisa en la ingesta cuando cambie el esquema.",
            skill="pii-masking",
            detail="Con la evolución de esquema activada, una columna personal nueva llega a Bronze sin que nadie la revise.",
        )]
    return []


def check_export(rel, text, signals):
    rx = import_regex(signals.get("export_imports", []))
    if (text and rx.search(text)) or re.search(r"(^|/)exports?/", rel.lower()):
        return [_f(
            "external-export", rel, "alta",
            "Entrega de datos fuera de la plataforma o a un tercero",
            RGPD, ["art. 28", "arts. 44-49"], "ya", [rel],
            "Confirma la región del destino (transferencia internacional), que hay contrato de "
            "encargado del tratamiento y que no salen columnas personales.",
            escalate="dpo", skill="pii-masking",
        )]
    return []


def check_llm(rel, text, signals):
    if text and import_regex(signals.get("llm_imports", [])).search(text):
        return [_f(
            "llm-sdk", rel, "alta",
            "Uso de un modelo de lenguaje (SDK de LLM)",
            AIACT, ["art. 50"], "ya (desde 2026-08-02)", [rel],
            "Si interactúa con personas, debe avisar de que es una IA; si genera contenido, "
            "debe marcarlo. Revísalo con la skill ai-transparency.",
            escalate="pm", skill="ai-transparency",
        )]
    return []


def terms_in(text, rx, exclusions):
    hits = set()
    for m in rx.finditer((text or "").lower()):
        if m.group(1) not in exclusions:
            hits.add(m.group(1))
    return hits


def check_terms(rel, text, signals, exclusions):
    out = []
    excl = set(exclusions)
    pii = terms_in(text, term_regex(signals.get("pii_terms", [])), excl)
    if pii:
        out.append(_f(
            "pii-terms", rel, "media",
            "Columnas o campos con aspecto de dato personal",
            RGPD, ["art. 5.1.c", "art. 25", "art. 32"], "ya", [rel],
            "Comprueba si son datos personales reales y, si lo son, decide dónde se enmascaran o "
            "seudonimizan (skill pii-masking).",
            skill="pii-masking", detail="Términos: " + ", ".join(sorted(pii)),
        ))
    special = terms_in(text, term_regex(signals.get("special_category_terms", [])), excl)
    if special:
        out.append(_f(
            "special-category-terms", rel, "alta",
            "Posibles categorías especiales de datos",
            RGPD, ["art. 9"], "ya", [rel],
            "Las categorías especiales necesitan una base jurídica del art. 9. Confírmalo con el DPO "
            "antes de tratarlas.",
            escalate="dpo", skill="special-categories", detail="Términos: " + ", ".join(sorted(special)),
        ))
    return out


def audit(root):
    """Auditoría completa del repo. Devuelve dict con entornos, reglas y hallazgos."""
    signals, version = load_knowledge()
    files = [(rel, read_text(full)) for rel, full in walk(root)]
    files = [(r, t) for r, t in files if t is not None]
    environments = detect_environments(files, signals)
    rules = build_rules(root, files, signals, environments)
    text_of = dict(files)
    excl = rules["exclusions"]
    findings = []

    pii_key = rules["pii_key"]
    if not rules["pii_key_detected"]:
        findings.append(_f(
            "no-pii-mechanism", "repo", "media",
            "El repo no tiene una forma de declarar qué columnas son personales",
            RGPD, ["art. 25", "art. 30"], "ya", [],
            f"Añade una clave por objeto (por ejemplo «{pii_key}») en la configuración de las fuentes "
            "para registrar qué datos personales entran y dónde se tratan.",
            skill="pii-masking",
        ))
    for rel in rules["source_configs"]:
        findings += check_source_config(rel, text_of.get(rel), pii_key)

    if rules["pii_key_detected"]:
        masking = term_regex(signals.get("masking_terms", []))
        applied = [r for r in rules["pii_key_references"] if masking.search((text_of.get(r) or "").lower())]
        if rules["pii_key_references"] and not applied:
            findings.append(_f(
                "pii-declared-not-applied", "repo", "alta",
                f"«{pii_key}» se declara pero ningún código lo aplica",
                RGPD, ["art. 25", "art. 32"], "ya", rules["pii_key_references"][:5],
                f"Decide en qué capa se enmascaran o seudonimizan las columnas de «{pii_key}» y "
                "aplícalo en el código; hasta entonces los datos llegan en claro.",
                escalate="dpo", skill="pii-masking",
                detail="Se valida o se copia, pero no hay hash, enmascarado ni eliminación en los ficheros que lo usan.",
            ))

    for rel in rules["bronze_writers"]:
        findings += check_schema_merge(rel, text_of.get(rel))

    if rules["bronze_writers"]:
        erasure = term_regex(signals.get("erasure_terms", []))
        code_text = " ".join((t or "").lower() for r, t in files
                             if os.path.splitext(r)[1] in CODE_EXT and not is_test(r))
        if not erasure.search(code_text):
            findings.append(_f(
                "no-erasure", "repo", "media",
                "Sin mecanismo de supresión ni de retención en las capas de datos",
                RGPD, ["art. 17", "art. 5.1.e"], "ya", rules["bronze_writers"][:5],
                "Define cómo se atiende una petición de supresión y cuánto tiempo se guardan los datos "
                "personales, también en capas de solo añadir filas e históricas.",
                escalate="dpo", skill="pii-masking",
            ))

    for rel in rules["exports"]:
        findings += check_export(rel, text_of.get(rel), signals)

    for rel, text in files:
        ext = os.path.splitext(rel)[1]
        if ext not in CODE_EXT or is_test(rel):
            continue
        if ext in (".py", ".ipynb"):
            findings += check_llm(rel, text, signals)
        if rel not in rules["source_configs"]:
            # En la configuración de fuentes los términos son la propia declaración de PII.
            findings += check_terms(rel, text, signals, excl)

    # Scoring sobre personas: ML + términos de scoring en el mismo repo.
    ml_files = [r for r, t in files if os.path.splitext(r)[1] in (".py", ".ipynb") and not is_test(r)
                and import_regex(signals.get("ml_imports", [])).search(t or "")]
    if ml_files:
        sc = term_regex(signals.get("scoring_terms", []))
        scoring = [r for r in ml_files if sc.search((text_of.get(r) or "").lower())]
        if scoring:
            findings.append(_f(
                "scoring-model", "repo", "alta",
                "Modelo que puntúa o clasifica, posiblemente sobre personas",
                AIACT, ["art. 6", "anexo III"], "desde 2027-12-02", scoring[:5],
                "Según el sector del cliente y la finalidad puede ser de alto riesgo. Clasifícalo con "
                "la skill ai-act-classify.",
                escalate="pm", skill="ai-act-classify",
            ))

    order = {"alta": 0, "media": 1, "baja": 2}
    findings.sort(key=lambda f: (order.get(f["severity"], 3), f["rule"], f["evidence"][:1]))
    return {
        "date": today(),
        "root": os.path.abspath(root),
        "knowledge_version": version,
        "environments": environments,
        "rules": rules,
        "findings": findings,
        "docs_site": os.path.exists(os.path.join(root, "docs", "site", "site.toml")),
    }


# ---------------------------------------------------------------- línea base

def load_json(path, default):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return default


def merge_baseline(old, findings):
    """Conserva el estado y la justificación de lo que ya estaba (Q23b)."""
    old_f = (old or {}).get("findings", {})
    out = {}
    seen = set()
    for f in findings:
        prev = old_f.get(f["id"], {})
        out[f["id"]] = {
            "status": prev.get("status", "abierto"),
            "justification": prev.get("justification", ""),
            "first_seen": prev.get("first_seen", today()),
            "last_seen": today(),
            "rule": f["rule"],
            "severity": f["severity"],
            "title": f["title"],
            "evidence": f["evidence"],
        }
        seen.add(f["id"])
    for fid, prev in old_f.items():
        if fid not in seen:
            item = dict(prev)
            if item.get("status") == "abierto":
                item["status"] = "no detectado"
            out[fid] = item
    return {"updated": today(), "findings": out}


def write_outputs(root, result, out_dir=None):
    out = os.path.join(root, out_dir or STATE_DIR)
    os.makedirs(os.path.join(out, "audits"), exist_ok=True)
    with open(os.path.join(out, "rules.json"), "w", encoding="utf-8") as fh:
        json.dump(result["rules"], fh, ensure_ascii=False, indent=2)
    base_path = os.path.join(out, "baseline.json")
    baseline = merge_baseline(load_json(base_path, {}), result["findings"])
    with open(base_path, "w", encoding="utf-8") as fh:
        json.dump(baseline, fh, ensure_ascii=False, indent=2)
    report = os.path.join(out, "audits", f"{result['date']}.md")
    with open(report, "w", encoding="utf-8") as fh:
        fh.write(render_report(result, baseline))
    return {"rules": os.path.join(out, "rules.json"), "baseline": base_path, "report": report}


# ---------------------------------------------------------------- informe

def render_report(result, baseline=None):
    status = {k: v.get("status", "abierto") for k, v in (baseline or {}).get("findings", {}).items()}
    kv = result.get("knowledge_version") or {}
    lines = [
        f"# Auditoría de riesgos AI Act y RGPD · {result['date']}",
        "",
        "Auditoría de solo lectura generada por `ai-act-advisor`. No se abrieron datos, secretos ni "
        "credenciales. No es asesoramiento legal.",
        "",
        f"- Base normativa: AI Act consolidado de {kv.get('consolidado_ai_act', '?')}, "
        f"revisada el {kv.get('ultima_revision', '?')}.",
        f"- Hallazgos: {len(result['findings'])} "
        f"({sum(1 for f in result['findings'] if f['severity'] == 'alta')} de severidad alta).",
        "",
        "## Entornos detectados",
        "",
        "| Entorno | Detectado en | Evidencia |",
        "|---|---|---|",
    ]
    for e in result["environments"]:
        lines.append(f"| {e['name']} | {e['source']} | " + ", ".join(f"`{p}`" for p in e["evidence"][:3]) + " |")
    r = result["rules"]
    lines += [
        "",
        "## Reglas del repo",
        "",
        "Lo que vigilan los hooks en este repo. El PM puede corregirlo en `.ai-act/rules.json`.",
        "",
        f"- Clave de PII: `{r['pii_key']}`" + ("" if r["pii_key_detected"] else " (propuesta: el repo no tiene ninguna)"),
        "- Configuración de fuentes: " + (", ".join(f"`{p}`" for p in r["source_configs"]) or "ninguna detectada"),
        "- Escritura en Bronze: " + (", ".join(f"`{p}`" for p in r["bronze_writers"]) or "ninguna detectada"),
        "- Salidas fuera de la plataforma: " + (", ".join(f"`{p}`" for p in r["exports"]) or "ninguna detectada"),
        "",
        "## Hallazgos",
        "",
        "| Severidad | Hallazgo | Norma | Aplica | Estado |",
        "|---|---|---|---|---|",
    ]
    for f in result["findings"]:
        lines.append(
            f"| {f['severity']} | {f['title']} | {f['norma']} {', '.join(f['articulos'])} | "
            f"{f['aplica']} | {status.get(f['id'], 'abierto')} |"
        )
    lines.append("")
    for f in result["findings"]:
        lines += [
            f"### {f['title']}",
            "",
            f"- Id: `{f['id']}` · severidad {f['severity']} · {f['norma']} {', '.join(f['articulos'])} · aplica {f['aplica']}",
        ]
        if f["evidence"]:
            lines.append("- Evidencia: " + ", ".join(f"`{p}`" for p in f["evidence"]))
        if f["detail"]:
            lines.append(f"- Detalle: {f['detail']}")
        lines.append(f"- Recomendación: {f['recommendation']}")
        if f["escalate"]:
            lines.append(f"- Escalar a: {f['escalate'].upper()} (contacto en el perfil del proyecto)")
        lines.append("")
    if not any(f["norma"] == AIACT for f in result["findings"]):
        lines += [
            "## AI Act",
            "",
            "No se detectan modelos que puntúen o decidan sobre personas ni SDKs de LLM. Si el proyecto "
            "no infiere, queda fuera del AI Act; siguen aplicando los avisos del RGPD.",
            "",
        ]
    lines += [
        "## Cómo se usa este informe",
        "",
        "Es la línea base del proyecto: cada hallazgo tiene un estado en `.ai-act/baseline.json` "
        "(`abierto`, `mitigado`, `aceptado` con justificación). Los avisos del día a día solo hablan de lo "
        "que no está aquí.",
        "",
    ]
    return "\n".join(lines)
