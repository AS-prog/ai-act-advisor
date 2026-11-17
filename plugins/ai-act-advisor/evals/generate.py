#!/usr/bin/env python3
"""Genera los casos de `claude plugin eval` a partir de tests/consultas-citas.json.

    python3 plugins/ai-act-advisor/evals/generate.py          escribe evals/NN-id/case.yaml
    python3 plugins/ai-act-advisor/evals/generate.py --check  falla si algún caso no está al día

Cada consulta de prueba del buscador es un caso: la pregunta la hace una persona
(PREGUNTAS), las reformulaciones las escribe Claude y las notas esperadas son las
del JSON. Los dos casos de EXTRA no están en el JSON. Solo librería estándar.
"""
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
CONSULTAS = os.path.join(REPO, "tests", "consultas-citas.json")

RGPD = r"RGPD|GDPR|2016/679|Reglamento General de Protecci[oó]n de Datos"
LOPDGDD = r"LOPDGDD|Ley Org[aá]nica 3/2018"
AI_ACT = r"AI Act|\bRIA\b|2024/1689|Reglamento de (?:Inteligencia Artificial|IA)"
CEPD = r"CEPD|EDPB|Comit[eé] Europeo de Protecci[oó]n de Datos|European Data Protection Board"


def articulo(norma, *numeros):
    """Patrón: la respuesta nombra la norma y alguno de los artículos."""
    return r"^(?=[\s\S]*?(?:%s))(?=[\s\S]*?art(?:[íi]culos?|s?\.?)\s*(?:%s)(?!\d))" % (norma, "|".join(numeros))


def anexo_iii():
    return r"^(?=[\s\S]*?(?:%s))(?=[\s\S]*?anexo\s+III(?![IV]))" % AI_ACT


# id de la consulta → (pregunta como la haría un PM, DE o AE; patrón de la norma y el artículo; etiquetas)
PREGUNTAS = {
    "cat-especiales": ("Vamos a cruzar los datos de clientes con su historial médico para un modelo de propensión. ¿Qué norma regula el uso de datos de salud y qué exige?", articulo(RGPD + "|" + LOPDGDD, "9"), []),
    "minimizacion": ("En la ingesta a Bronze traemos todas las columnas del CRM aunque solo usamos cuatro. ¿Hay algún artículo que obligue a traer solo lo necesario?", articulo(RGPD, "5"), ["humo"]),
    "seudonimizacion": ("¿Hashear los correos electrónicos de los clientes cuenta como medida de protección según la norma? ¿Qué artículo lo respalda?", articulo(RGPD, "4", "25", "32"), []),
    "eipd": ("Antes de lanzar un modelo que perfila a clientes a gran escala, ¿tenemos que hacer una evaluación de impacto? ¿Dónde lo dice?", articulo(RGPD, "35"), []),
    "decisiones-automatizadas": ("El modelo va a denegar solicitudes automáticamente, sin que nadie las revise. ¿Qué artículo regula las decisiones automatizadas?", articulo(RGPD, "22"), []),
    "gobernanza": ("¿Qué exige la norma sobre la calidad y los sesgos de los datos con los que entrenamos un sistema de alto riesgo?", articulo(AI_ACT, "10"), []),
    "solvencia": ("Estamos construyendo un modelo de scoring de solvencia crediticia de clientes particulares. ¿Es de alto riesgo según la norma? Cita dónde lo dice.", anexo_iii(), []),
    "chatbot": ("¿Hay que avisar al usuario de que está hablando con un chatbot? ¿Qué artículo lo exige?", articulo(AI_ACT, "50"), []),
    "contenido-generado": ("Generamos imágenes y textos de marketing con IA. ¿Hay que marcarlos de alguna forma? ¿Dónde lo dice?", articulo(AI_ACT, "50"), []),
    "deepfake": ("Marketing quiere un vídeo con un avatar que imita a una persona real. ¿Qué obligación hay y en qué artículo está?", articulo(AI_ACT, "50"), []),
    "emociones": ("RR. HH. quiere detectar las emociones de los empleados en las videollamadas. ¿Lo permite la norma?", articulo(AI_ACT, "5"), []),
    "seleccion-personal": ("Queremos un modelo que filtre los currículos de los candidatos en los procesos de selección. ¿Cómo lo clasifica la norma?", anexo_iii(), []),
    "anonimizacion": ("Si anonimizamos el dataset antes de compartirlo, ¿cómo se valora el riesgo de reidentificación? ¿Hay criterios publicados?", CEPD, ["solo-ingles"]),
    "web-scraping": ("¿Podemos extraer datos de webs públicas para entrenar un modelo generativo? ¿Qué dicen las autoridades de protección de datos?", CEPD, ["solo-ingles"]),
    "excepcion-6-3": ("Nuestro sistema encaja en el anexo III, pero solo hace una tarea procedimental limitada. ¿Hay alguna excepción para no tratarlo como de alto riesgo?", articulo(AI_ACT, "6"), []),
    "alfabetizacion": ("¿Estamos obligados a formar al personal que usa herramientas de IA? ¿Qué artículo lo dice?", articulo(AI_ACT, "4"), []),
    "transferencias": ("Vamos a exportar datos de clientes a un proveedor de fuera del EEE. ¿Qué artículos lo regulan?", articulo(RGPD, "44", "45", "46", "49"), []),
    "encargado": ("Un proveedor externo va a tratar datos de clientes por nuestra cuenta. ¿Qué tiene que llevar el contrato y dónde lo dice?", articulo(RGPD + "|" + LOPDGDD, "28", "33"), []),
    "supresion": ("Un cliente pide que borremos todos sus datos. ¿Qué artículo regula ese derecho?", articulo(RGPD + "|" + LOPDGDD, "17", "15"), []),
    "trabajadores": ("¿Tenemos que informar a la plantilla de los algoritmos que afectan a sus condiciones de trabajo? ¿Qué norma lo exige?", r"723/2026|Estatuto de los Trabajadores", []),
}

# El JSON espera lopdgdd-art-64 para «trabajadores», pero ese artículo trata del
# procedimiento sancionador (el 64.4 que cita la AEPD es del Estatuto de los
# Trabajadores). Aquí no cuenta como acierto.
NO_ESPERADAS = {"trabajadores": {"lopdgdd-art-64"}}

EXTRA = [
    {
        "id": "singularizacion",
        "es": "caso solo en inglés: la singularización solo la tratan las directrices 02/2026 del CEPD",
        "pregunta": "¿Qué es la «singularización» de una persona y cómo se usa para decidir si un dataset está de verdad anonimizado?",
        "esperadas": ["cepd-directrices-02-2026-anonimizacion-v1"],
        "patron": CEPD,
        "tags": ["solo-ingles", "humo"],
    },
]

SIN_NOTA = {
    "id": "sin-nota",
    "es": "caso negativo: ninguna nota recoge el Reglamento de Servicios Digitales",
    "pregunta": "¿Qué artículo del Reglamento de Servicios Digitales (DSA) nos obliga a explicar los parámetros de nuestro sistema de recomendación?",
    "tags": ["negativo", "humo"],
}

HERRAMIENTAS = ["Skill", "Read", "Glob", "Grep", "Bash"]

FUENTE_OFICIAL = r"DOUE|BOE|CELEX|Diario Oficial|EUR-Lex"
FORMATO = r"·\s*nota\s+`?[a-z0-9-]+`?\s*\(L\d+(?:\s*[-–]\s*L?\d+)?\)\s*·"
GUIA_APOYO = (
    "Aprueba si se cumplen las dos condiciones:\n"
    "1. Cada vez que la respuesta menciona una guía, unas directrices o un documento de una autoridad "
    "(AESIA, AEPD, CEPD/EDPB, Comisión Europea), lo presenta como orientación, criterio o apoyo, y no "
    "como la norma que obliga.\n"
    "2. Cada cosa que la respuesta presenta como obligatoria o prohibida va unida a un artículo o anexo "
    "de una norma (reglamento, ley o real decreto), o la respuesta dice de forma expresa que no tiene "
    "norma que la respalde.\n"
    "Si la respuesta no menciona ninguna guía, basta con la condición 2.\n"
    "Suspende si alguna obligación se apoya solo en una guía o en directrices, o si la respuesta está "
    "vacía o no contesta a la pregunta."
)
HONESTIDAD = (
    "La pregunta es sobre el Reglamento de Servicios Digitales (DSA), que no está entre las fuentes "
    "verificadas del asistente. Aprueba solo si la respuesta dice de forma expresa que no tiene una fuente "
    "o nota verificada que respalde lo que afirma sobre el DSA y remite a consultar el texto oficial. "
    "Puede mencionar de memoria un artículo del DSA si lo marca como no verificado. Suspende si da un "
    "artículo del DSA como cierto sin esa advertencia, o si lo cita con el mismo formato que una fuente "
    "comprobada, o si la respuesta está vacía."
)


def q(texto):
    """Escalar YAML entre comillas dobles (JSON es YAML válido)."""
    return json.dumps(texto, ensure_ascii=False)


def patron_notas(esperadas):
    # Igual que tests/test_buscar.py: vale la nota o una que empiece por «nota-».
    return "(?:%s)(?![a-z0-9])" % "|".join(sorted(esperadas))


def grader(tipo, nombre, **campos):
    lineas = ["  - type: %s" % tipo, "    name: %s" % nombre]
    for clave, valor in campos.items():
        lineas.append("    %s: %s" % (clave, valor if isinstance(valor, (int, float)) else q(valor)))
    return lineas


def uso():
    return grader("tool_used", "usa-skill", tool="Skill") + grader(
        "tool_used", "usa-buscador", tool="Bash", input_match=r"buscar\.py", arm="with-only"
    )


def caso(numero, c):
    nombre = "%02d-%s" % (numero, c["id"])
    g = []
    if "esperadas" in c:
        notas = patron_notas(c["esperadas"])
        g += grader("regex", "nota-recuperada", target="trace", pattern=notas, arm="with-only")
        g += grader("regex", "nota-citada", pattern=notas)
        g += grader("regex", "articulo-citado", pattern=c["patron"], flags="i")
        if "solo-ingles" not in c["tags"]:
            g += grader("regex", "fuente-oficial", pattern=FUENTE_OFICIAL)
        g += grader("regex", "formato-cita", pattern=FORMATO, weight=0.5)
        g += grader("llm", "guia-como-apoyo", criteria=GUIA_APOYO)
    else:
        g += grader("regex", "dice-sin-nota", pattern=r"sin nota que l[oa]s? respalde", flags="i", weight=0.5)
        g += grader("llm", "no-inventa-cita", criteria=HONESTIDAD)
    g += uso()
    lineas = [
        "# Generado por evals/generate.py: no editar a mano.",
        'schema_version: "1.0"',
        "name: %s" % nombre,
        "description: %s" % q("Consulta «%s»: %s" % (c["id"], c["es"])),
        "tags: [%s]" % ", ".join(c["tags"]),
        "execution:",
        "  prompt: %s" % q(c["pregunta"]),
        "  max_turns: 20",
        "  timeout_seconds: 300",
        "  allowed_tools: [%s]" % ", ".join(HERRAMIENTAS),
        "runs: 3",
        "graders:",
    ] + g
    return nombre, "\n".join(lineas) + "\n"


def casos():
    with open(CONSULTAS, encoding="utf-8") as fh:
        consultas = json.load(fh)["consultas"]
    ids = [c["id"] for c in consultas]
    if set(ids) != set(PREGUNTAS):
        raise SystemExit("PREGUNTAS y consultas-citas.json no tienen los mismos ids: %s" % sorted(set(ids) ^ set(PREGUNTAS)))
    lista = []
    for c in consultas:
        pregunta, patron, tags = PREGUNTAS[c["id"]]
        esperadas = [e for e in c["esperadas"] if e not in NO_ESPERADAS.get(c["id"], ())]
        lista.append({"id": c["id"], "es": c["es"], "pregunta": pregunta, "esperadas": esperadas, "patron": patron, "tags": ["cita"] + tags})
    lista += EXTRA + [SIN_NOTA]
    return [caso(i + 1, c) for i, c in enumerate(lista)]


def main(argv):
    comprobar = "--check" in argv
    desfasados = []
    generados = casos()
    for nombre, texto in generados:
        ruta = os.path.join(HERE, nombre, "case.yaml")
        actual = open(ruta, encoding="utf-8").read() if os.path.exists(ruta) else None
        if actual == texto:
            continue
        desfasados.append(nombre)
        if not comprobar:
            os.makedirs(os.path.dirname(ruta), exist_ok=True)
            with open(ruta, "w", encoding="utf-8") as fh:
                fh.write(texto)
    nombres = {n for n, _ in generados}
    for d in sorted(os.listdir(HERE)):
        if os.path.isfile(os.path.join(HERE, d, "case.yaml")) and d not in nombres:
            desfasados.append(d)
            if not comprobar:
                shutil.rmtree(os.path.join(HERE, d))
    if comprobar and desfasados:
        print("Casos sin regenerar: %s" % ", ".join(desfasados))
        return 1
    print("%d casos%s" % (len(generados), "" if comprobar else ", %d escritos o borrados" % len(desfasados)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
