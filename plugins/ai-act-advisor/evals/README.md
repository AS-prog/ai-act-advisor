# Evals de las citas

Mide con Claude de verdad si el plugin encuentra y cita la nota normativa correcta cuando un PM, un DE o un AE pregunta en español. Es la medida que falta en `tests/test_buscar.py`, donde las reformulaciones de cada pregunta están escritas a mano: aquí las escribe Claude desde la skill `cite-regulation`.

## Casos

22 casos, uno por carpeta, generados por `generate.py`:

- **01 a 20** (`cita`): las 20 consultas de `tests/consultas-citas.json`, con sus notas esperadas. La pregunta está redactada como la haría una persona; las reformulaciones del JSON no se usan.
- **13, 14 y 21** (`solo-ingles`): la respuesta solo está en directrices del CEPD en inglés. Deben salir como orientación, sin convertirse en la base de una obligación.
- **22** (`negativo`): pregunta por el Reglamento de Servicios Digitales, que no está en las notas. Se espera «sin nota que lo respalde».
- `humo`: tres casos (02, 21 y 22) para probar que todo funciona.

Para cambiar una pregunta o un patrón, edita `generate.py` y vuelve a generar; `tests/test_evals.py` falla si los casos no están al día.

```sh
python3 plugins/ai-act-advisor/evals/generate.py
```

## Cómo se ejecuta

Desde `plugins/ai-act-advisor/`, en un clon del repositorio:

```sh
# prueba de humo: 3 casos, una pasada
claude plugin eval . --tag humo --runs 1 --max-cost-usd 3 --allow-tools Bash --judge-model sonnet --no-publish

# suite completa: 22 casos × 2 brazos × 3 pasadas
claude plugin eval . --allow-tools Bash --judge-model sonnet
```

- `--allow-tools Bash` es necesario: la skill llama a `scripts/buscar.py`. En Linux, Claude Code solo concede Bash dentro de una evaluación si están instalados `bubblewrap` y `socat`.
- La ablación `with-without` va por defecto: cada caso corre con el plugin y sin él, y el informe da la diferencia (Δ).
- **Notas**: viajan con el plugin en `knowledge/notas/` (D21), así que la evaluación funciona igual con el plugin cargado desde el clon que instalado. `AIACT_NOTAS` o `--notas` apuntan a otra carpeta si hace falta.
- Los resultados quedan en `evals/results/`, fuera de git.

## Con varios modelos: `run.py`

`run.py` lanza el eval una vez por modelo, con el juez fijo para que las notas se puedan comparar, y lleva el historial:

```sh
# desde plugins/ai-act-advisor/evals/
python3 run.py ejecutar --modelos claude-haiku-5-5 claude-sonnet-5-5 claude-opus-5-5 --tag humo --runs 1 --max-cost 3
python3 run.py ejecutar --modelos claude-opus-5-5 --dry-run        # enseña el comando sin gastar
python3 run.py historial                                           # una fila por ejecución y modelo
python3 run.py historial --por-caso --modelo 'claude-haiku*'       # detalle por caso
python3 run.py registrar results/x.json --modelo claude-opus-5-5   # añade una ejecución hecha a mano
```

- El JSON completo de cada ejecución va a `results/` (fuera de git). El resumen se añade a `historial/ejecuciones.csv` y `historial/casos.csv`, que sí se versionan.
- Columnas de `ejecuciones.csv`: puntos con y sin plugin, Δ, tasa de aprobados, `skill_activa` (parte de las pasadas en que se cargó la skill), `nota_recuperada`, coste, duración, si fue parcial por el tope de coste, `commit` del repo y `skill_sha` (huella de `cite-regulation/SKILL.md`). Con las dos últimas se compara una versión de la skill con la anterior.
- `--juez` (por defecto `sonnet`), `--runs`, `--tag`, `--max-cost` (por modelo) y `-j` pasan tal cual a `claude plugin eval`.
- `--caso` admite varios globs (`--caso "0[7-9]-*" "1[0-2]-*"`). `claude plugin eval --case` solo entiende `*` y un patrón, así que `run.py` resuelve los nombres y, si hace falta, llama una vez por caso, junta los resultados en un solo JSON y registra una fila con `filtro` = `caso:…`. Si ningún caso coincide, no llama a nada ni registra.

## Qué comprueba cada grader

| Grader | Tipo | Qué comprueba | Puntúa |
| --- | --- | --- | --- |
| `nota-citada` | regex | La respuesta nombra el id de una nota esperada | 1 |
| `articulo-citado` | regex | La respuesta nombra la norma y el artículo o anexo esperados (en los casos del CEPD, al CEPD) | 1 |
| `fuente-oficial` | regex | La respuesta remite al DOUE, al BOE o a un CELEX | 1 |
| `formato-cita` | regex | Hay una línea con la forma `· nota id (Lnn) ·` | 0,5 |
| `guia-como-apoyo` | LLM | Las guías se presentan como orientación y cada obligación va unida a un artículo | 1 |
| `dice-sin-nota` | regex | Caso 22: aparece «sin nota que lo respalde» | 0,5 |
| `no-inventa-cita` | LLM | Caso 22: dice que no tiene fuente verificada del DSA y no lo cita como comprobado | 1 |
| `nota-recuperada` | regex sobre la traza | Una nota esperada apareció en la sesión: el buscador la encontró con las consultas de Claude | no, solo con plugin |
| `usa-buscador` | tool_used | Se llamó a `buscar.py` | no, solo con plugin |
| `usa-skill` | tool_used | Se cargó una skill | no, solo con plugin |

Cómo leer el resultado:

- `nota-recuperada` es la cifra comparable con los 19 de 20 de `test_buscar.py`. Si falla, las consultas de Claude no encontraron la nota; si pasa y falla `nota-citada`, la encontró y no la citó.
- Claude sin plugin no conoce los ids de las notas, así que `nota-citada` y `formato-cita` suman a Δ por construcción. La comparación limpia entre brazos está en `articulo-citado`, `fuente-oficial`, `guia-como-apoyo` y `no-inventa-cita`.
- Los graders LLM usan el modelo de `--judge-model`; conviene que sea distinto del que responde.

## Primera ejecución (2026-11-17)

Casos `humo` (02, 21 y 22), una pasada por brazo, juez `sonnet`: 35 s y 0,46 USD.

| Caso | Con plugin | Sin plugin | Qué pasó |
| --- | --- | --- | --- |
| 02-minimizacion | 1,00 | 0,44 | La skill se activa, llama a `buscar.py` y cita `RGPD art. 5.1.c · nota rgpd-art-5 (L23) · DOUE, CELEX …` |
| 21-singularizacion | 0,00 | 0,29 | La skill **no se activa**: Claude responde de memoria con el Dictamen 05/2014 y el considerando 26, sin buscar en la guía del CEPD |
| 22-sin-nota | 0,67 | 0,00 | La skill **no se activa**: cita el art. 27 del DSA de memoria y avisa de que no está verificado (el juez aprueba `no-inventa-cita` con razón), pero no dice «sin nota que lo respalde» |

Lo que enseña: la búsqueda y el formato funcionan cuando la skill entra, pero su `description` no la activa con preguntas conceptuales («¿qué es…?») ni sobre normas que no están en las notas. Es lo primero que hay que ajustar antes de lanzar los 22 casos con tres pasadas.
