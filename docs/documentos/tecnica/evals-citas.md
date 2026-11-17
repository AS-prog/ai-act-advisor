---
title: Cómo funciona el eval de las citas
description: Qué mide la suite de claude plugin eval de las citas normativas, cómo corre cada caso con y sin plugin, qué comprueba cada grader y qué salió en la primera ejecución.
date: 2026-11-17
code: ai-act-advisor@2648639
---

# Cómo funciona el eval de las citas

Qué mide la suite de `claude plugin eval` de las citas normativas, cómo
corre cada caso con y sin plugin, qué comprueba cada grader y qué salió
en la primera ejecución.

## En una frase

Cada caso hace a Claude una pregunta normativa en español, como la haría
un PM, un DE o un AE, dos veces: con el plugin, donde la skill
`cite-regulation` busca en las notas y cita con formato fijo, y sin él,
donde Claude responde de memoria. Unos graders puntúan las dos respuestas
y el informe da la diferencia.

## Por qué hace falta

`tests/test_buscar.py` ya mide el buscador: 19 de 20 preguntas encuentran
la nota esperada. Pero las tres consultas que recibe el buscador (la
pregunta, la misma con el vocabulario de la norma y su traducción al
inglés) las escribí a mano imitando a Claude. El eval quita esa
suposición: las consultas las escribe Claude desde la skill, y además
mide si la skill se activa, si lee el pasaje y si cita bien.

## Cómo corre un caso

<figure class="figwrap">
  <svg viewBox="0 0 720 352" role="img" aria-labelledby="eval-title eval-desc">
    <title id="eval-title">Un caso del eval, con y sin plugin</title>
    <desc id="eval-desc">La misma pregunta va a dos brazos. Con plugin, Claude carga la skill cite-regulation, escribe tres consultas, llama a buscar.py, lee la nota en la línea indicada y responde con la cita. Sin plugin, Claude responde de memoria. Los graders puntúan las dos respuestas; algunos miran también la traza del brazo con plugin. El informe da la puntuación de cada brazo y la diferencia.</desc>
    <defs>
      <marker id="eval-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon class="d-bar" points="0 0, 8 3, 0 6"/></marker>
    </defs>
    <rect class="d-box" x="16" y="136" width="136" height="72"/>
    <text class="d-t" x="28" y="162">Pregunta</text>
    <text class="d-sm" x="28" y="182">en español, de</text>
    <text class="d-sm" x="28" y="198">PM, DE o AE</text>
    <line class="d-line" x1="152" y1="160" x2="184" y2="72" marker-end="url(#eval-arrow)"/>
    <line class="d-line" x1="152" y1="184" x2="184" y2="284" marker-end="url(#eval-arrow)"/>
    <text class="d-tm" x="184" y="22">CON PLUGIN</text>
    <rect class="d-fill" x="184" y="32" width="336" height="168"/>
    <text class="d-t" x="200" y="58">1 · skill cite-regulation</text>
    <text class="d-sm" x="200" y="80">tres consultas: pregunta, norma, inglés</text>
    <text class="d-t" x="200" y="110">2 · buscar.py citas</text>
    <text class="d-sm" x="200" y="132">normas y guías, con nota y línea</text>
    <text class="d-t" x="200" y="162">3 · lee el pasaje y cita</text>
    <text class="d-sm" x="200" y="184">RGPD art. 5.1.c · nota … (L23) · DOUE</text>
    <text class="d-tm" x="184" y="250">SIN PLUGIN</text>
    <rect class="d-box" x="184" y="260" width="336" height="56"/>
    <text class="d-t" x="200" y="284">Claude responde de memoria</text>
    <text class="d-sm" x="200" y="304">sin notas ni formato de cita</text>
    <line class="d-line" x1="520" y1="116" x2="560" y2="160" marker-end="url(#eval-arrow)"/>
    <line class="d-line" x1="520" y1="288" x2="560" y2="208" marker-end="url(#eval-arrow)"/>
    <rect class="d-box" x="560" y="136" width="144" height="96"/>
    <text class="d-t" x="572" y="160">Graders</text>
    <text class="d-sm" x="572" y="182">regex · traza</text>
    <text class="d-sm" x="572" y="200">herramienta · juez</text>
    <text class="d-sm" x="572" y="222">puntos y Δ</text>
  </svg>
  <figcaption>La misma pregunta corre en dos brazos. La diferencia entre ellos (<strong>Δ</strong>) es lo que aporta el plugin.</figcaption>
</figure>

1. **Pregunta.** Cada caso es un `case.yaml` con una pregunta en lenguaje
   natural («En la ingesta a Bronze traemos todas las columnas del CRM
   aunque solo usamos cuatro. ¿Hay algún artículo que obligue a traer
   solo lo necesario?»).
2. **Dos brazos.** `claude plugin eval` lanza un Claude con el plugin
   cargado y otro sin él (ablación `with-without`). Los dos pueden usar
   `Bash`, `Read`, `Glob` y `Grep`.
3. **Con plugin.** Si la skill `cite-regulation` se activa, Claude escribe
   las tres consultas, llama a `scripts/buscar.py citas`, abre la nota en
   la línea que le da y responde con una línea de cita por afirmación:
   norma y artículo, nota y línea, y fuente oficial.
4. **Graders.** Puntúan la respuesta final de cada brazo; los marcados
   «solo con plugin» miran también la traza (qué herramientas usó y qué
   salió en la sesión) y no cuentan para la nota.
5. **Informe.** Puntuación por caso y brazo, tasa de aprobados y Δ.

## Los casos

22 casos en `plugins/ai-act-advisor/evals/`, generados por
`evals/generate.py` desde `tests/consultas-citas.json`, para que el eval y
el test offline usen las mismas preguntas y las mismas notas esperadas.

| Casos | Etiqueta | Qué prueban |
| --- | --- | --- |
| 01 a 20 | `cita` | Las 20 preguntas del test offline: RGPD, LOPDGDD, AI Act, guías |
| 13, 14 y 21 | `solo-ingles` | La respuesta solo está en directrices del CEPD en inglés; deben salir como orientación, no como obligación |
| 22 | `negativo` | Pregunta por el Reglamento de Servicios Digitales, que no está en las notas; se espera «sin nota que lo respalde» |
| 02, 21 y 22 | `humo` | Tres casos para comprobar que todo corre |

## Qué comprueba cada grader

| Grader | Tipo | Qué comprueba | Peso |
| --- | --- | --- | --- |
| `nota-citada` | regex | La respuesta nombra el id de una nota esperada | 1 |
| `articulo-citado` | regex | Nombra la norma y el artículo o anexo esperados | 1 |
| `fuente-oficial` | regex | Remite al DOUE, al BOE o a un CELEX | 1 |
| `formato-cita` | regex | Hay una línea con la forma `· nota id (Lnn) ·` | 0,5 |
| `guia-como-apoyo` | juez LLM | Las guías salen como orientación y cada obligación va unida a un artículo | 1 |
| `dice-sin-nota` | regex | Caso 22: aparece «sin nota que lo respalde» | 0,5 |
| `no-inventa-cita` | juez LLM | Caso 22: no presenta el DSA como fuente comprobada | 1 |
| `nota-recuperada` | regex sobre la traza | El buscador encontró una nota esperada con las consultas de Claude | solo con plugin |
| `usa-buscador` | herramienta | Se llamó a `buscar.py` | solo con plugin |
| `usa-skill` | herramienta | Se cargó una skill | solo con plugin |

Cómo leerlos:

- **`nota-recuperada`** es la cifra comparable con los 19 de 20 del test
  offline. Si falla, las consultas de Claude no encontraron la nota; si
  pasa y falla `nota-citada`, la encontró y no la citó.
- **Δ está inflada por construcción.** Claude sin plugin no conoce los
  ids de las notas, así que `nota-citada` y `formato-cita` siempre suman a
  favor del plugin. La comparación limpia está en `articulo-citado`,
  `fuente-oficial` y los dos jueces.
- **El juez** es otro modelo (`--judge-model sonnet`), para que no se
  califique a sí mismo.

## Primera ejecución

2026-11-17, casos `humo`, una pasada por brazo, juez `sonnet`: 35
segundos y 0,46 USD.

| Caso | Con plugin | Sin plugin | Qué pasó |
| --- | --- | --- | --- |
| 02 · minimización | **1,00** | 0,44 | La skill se activa, llama a `buscar.py` en 6 turnos y cita `RGPD art. 5.1.c · nota rgpd-art-5 (L23) · DOUE, CELEX 02016R0679-20160504` y el art. 25.2 |
| 21 · singularización | 0,00 | 0,29 | La skill **no se activa**: Claude responde de memoria con el Dictamen 05/2014 y el considerando 26, sin la guía del CEPD |
| 22 · DSA, sin nota | 0,67 | 0,00 | La skill **no se activa**: cita de memoria el art. 27 del DSA; el juez lo aprueba en `no-inventa-cita`, pero no dice «sin nota que lo respalde» |

Lo que enseña:

- **Cuando la skill entra, funciona.** Encuentra la nota, lee el
  apartado y cita con el formato completo. El brazo sin plugin acierta el
  artículo, pero sin nota ni fuente oficial.
- **La skill no se activa sola en dos tipos de pregunta.** Las
  conceptuales («¿qué es…?») y las de normas que no están en las notas.
  Es un problema de su `description`, no del buscador.
- **El juez de `no-inventa-cita` es blando.** Aprobó una cita del DSA de
  memoria sin la advertencia que pide su criterio. Hay que revisarlo con
  más pasadas.

## Cómo se ejecuta

Desde `plugins/ai-act-advisor/`, en un clon del repositorio:

```sh
# prueba de humo: 3 casos, una pasada
claude plugin eval . --tag humo --runs 1 --max-cost-usd 3 \
  --allow-tools Bash --judge-model sonnet --no-publish

# suite completa: 22 casos, 2 brazos, 3 pasadas
claude plugin eval . --allow-tools Bash --judge-model sonnet
```

- **Bash** hace falta porque la skill llama a `buscar.py`. En Linux,
  Claude Code solo lo concede dentro de un eval si están instalados
  `bubblewrap` y `socat`.
- **Notas.** Aún no viajan con el plugin (decisión 1 de D21, issue #15).
  `buscar.py` las encuentra en `docs/documentos/fuentes/notas/` subiendo
  desde su carpeta, así que el eval funciona con el plugin cargado desde
  el clon y falla con el instalado desde el marketplace.
- **Resultados** en `evals/results/`, fuera de git, con un informe HTML.
- Para cambiar una pregunta, edita `generate.py` y regenera;
  `tests/test_evals.py` falla si los casos no están al día.

## Siguientes pasos

1. Ajustar la `description` de `cite-regulation` para que se active con
   preguntas conceptuales y con normas que no están en las notas, y
   repetir los casos `humo`.
2. Endurecer el criterio del juez `no-inventa-cita`.
3. Lanzar la suite completa (22 casos, 2 brazos, 3 pasadas; unos 10 USD)
   y comparar `nota-recuperada` con los 19 de 20 del test offline.
