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
- **Notas**: aún no viajan con el plugin (decisión pendiente de D21). `buscar.py` las encuentra en `docs/documentos/fuentes/notas/` subiendo desde su propia carpeta, así que la evaluación funciona con el plugin cargado desde el clon. Con el plugin instalado desde el marketplace no hay notas y los casos fallan.
- Los resultados quedan en `evals/results/`, fuera de git.

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
