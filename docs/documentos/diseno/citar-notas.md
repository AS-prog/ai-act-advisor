---
title: Cómo recuperar y citar las notas normativas
description: Cómo encuentran las skills y los hooks la nota normativa que respalda cada aviso y cómo la citan, desde la búsqueda por metadatos de hoy hasta el MCP con embeddings de la versión madura.
date: 2026-11-17
status: borrador
---

# Cómo recuperar y citar las notas normativas

Cómo encuentran las skills y los hooks la nota normativa que respalda cada
aviso y cómo la citan, desde la búsqueda por metadatos de hoy hasta el MCP
con embeddings de la versión madura (D02).

## Conclusión

Propongo no empezar por RAG. Las tres operaciones que la propuesta del
prototipo reserva para el MCP (traer un artículo por su número, buscar
pasajes por pregunta y contrastar una afirmación) se pueden hacer ya sin
dependencias, en tres capas que devuelven lo mismo: una **cita con formato
fijo**.

1. **Cita fija.** Cada aviso cita norma, artículo y apartado, el id de la
   nota y la fuente oficial. Las guías y directrices apoyan, pero nunca son
   la base de una obligación.
2. **Mapa curado de señal a cita** en `knowledge/citas.yaml`. Los hooks y
   las skills lo leen para citar sin buscar. Es determinista y se revisa
   en PR, como el resto de `knowledge/`.
3. **Buscador para las preguntas abiertas**, en Python stdlib, con BM25
   por pasajes. Claude, que es quien lo llama, reformula la pregunta en el
   vocabulario de la norma y la traduce al inglés; el buscador lanza cada
   consulta sobre las notas de su idioma y devuelve por separado normas
   (la cita) y guías (el apoyo). Hay prototipo: `scripts/buscar.py`.

Los embeddings entran después detrás de la misma interfaz (entra una
consulta y salen ids de nota), así que las skills no cambian el día que
llegue el MCP.

## Contexto

Lo que se ha medido sobre `docs/documentos/fuentes/notas/` (806 notas,
7,5 MB) el 2026-11-17:

- **Las notas no viajan con el plugin.** El marketplace instala
  `./plugins/ai-act-advisor` y las notas están en `docs/`. Hoy ninguna
  skill ni hook puede leerlas en el proyecto de un usuario. Las normas
  (AI Act, RGPD, LOPDGDD, Omnibus) ocupan unos 2 MB; guías, directrices,
  checklists y sentencia, unos 5,4 MB.
- **El front matter es desigual.** Las 383 notas de normas tienen `norma`,
  `unidad`, `titulo` y `tags`. Las 423 de guías y otros documentos no
  tienen `tags`, ni `norma`, ni a qué artículos se refieren, y su
  `description` repite el nombre del fichero.
- **Los tags actuales no discriminan.** Hay 457 distintos y salen del
  título: `articulo` está en 330 notas y `proteccion-datos` en 243. Para
  «seudonimización», con 17 notas que la mencionan, ninguna `description`
  la nombra.
- **Las guías se pueden enlazar a artículos.** 110 de las 413 notas de
  guías y directrices citan un artículo con la forma «artículo N», así que
  un campo `articulos` se puede extraer al trocear.
- **El texto completo funciona en español y falla en inglés.** Un BM25 de
  50 líneas en stdlib, con el front matter puntuando el triple, encontró
  la nota esperada entre las cinco primeras en 6 de 7 consultas en
  español («categorías especiales de datos salud» → `rgpd-art-9`,
  «evaluación de impacto» → `rgpd-art-35`). En inglés, que es como
  escribe el código, falló en las 3: «credit scoring» no llega al anexo
  III y «pseudonymisation hash email» no llega al art. 4 ni al 32 del
  RGPD.
- **Una nota es un artículo entero.** Los avisos citan apartados (art.
  10.5) y la mediana de nota es de 3,8 KB, pero el 10 % pasa de 20 KB y
  `omnibus-art-1` llega a 61 KB. Leer la nota entera para citar un
  apartado gasta contexto; los apartados están numerados («1.», «2.») y
  se pueden localizar por línea.

## Propuesta

<figure class="figwrap">
  <svg viewBox="0 0 720 360" role="img" aria-labelledby="citas-title citas-desc">
    <title id="citas-title">De la señal a la cita</title>
    <desc id="citas-desc">Un hook o una skill parten de una señal o de una pregunta. Si la señal está en el mapa curado, la cita sale directa. Si es una pregunta abierta, el buscador filtra por metadatos y después busca por texto, con las consultas que Claude reformula en español y en inglés. Todo acaba en una cita con formato fijo que remite a la nota y a la fuente oficial. El MCP con embeddings sustituye al buscador más adelante con la misma salida.</desc>
    <defs>
      <marker id="citas-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon class="d-bar" points="0 0, 8 3, 0 6"/></marker>
    </defs>
    <rect class="d-box" x="16" y="16" width="200" height="56"/>
    <text class="d-t" x="32" y="40">Señal del hook</text>
    <text class="d-sm" x="32" y="60">pii-terms, scoring-model…</text>
    <rect class="d-box" x="16" y="208" width="200" height="56"/>
    <text class="d-t" x="32" y="232">Pregunta abierta</text>
    <text class="d-sm" x="32" y="252">skill o PM, en lenguaje natural</text>
    <line class="d-line" x1="216" y1="44" x2="264" y2="44" marker-end="url(#citas-arrow)"/>
    <line class="d-line" x1="216" y1="236" x2="264" y2="236" marker-end="url(#citas-arrow)"/>
    <rect class="d-fill" x="264" y="16" width="208" height="56"/>
    <text class="d-t" x="280" y="40">Mapa curado</text>
    <text class="d-sm" x="280" y="60">knowledge/citas.yaml</text>
    <rect class="d-box" x="264" y="160" width="208" height="152"/>
    <text class="d-t" x="280" y="184">Buscador stdlib</text>
    <text class="d-sm" x="280" y="210">1 · Claude: es, norma y en</text>
    <text class="d-sm" x="280" y="232">2 · BM25 por pasajes e idioma</text>
    <text class="d-sm" x="280" y="254">3 · normas y guías aparte</text>
    <text class="d-sm" x="280" y="292">salida: ids de nota + líneas</text>
    <line class="d-line" x1="472" y1="44" x2="520" y2="120" marker-end="url(#citas-arrow)"/>
    <line class="d-line" x1="472" y1="236" x2="520" y2="160" marker-end="url(#citas-arrow)"/>
    <rect class="d-fill" x="520" y="104" width="184" height="72"/>
    <text class="d-t" x="536" y="130">Cita fija</text>
    <text class="d-sm" x="536" y="150">norma · art. · apartado</text>
    <text class="d-sm" x="536" y="166">nota · fuente oficial</text>
    <rect class="d-box" x="216" y="328" width="304" height="24"/>
    <text class="d-tm" x="232" y="344">MÁS ADELANTE · MCP CON EMBEDDINGS</text>
    <line class="d-line" x1="368" y1="328" x2="368" y2="314" marker-end="url(#citas-arrow)"/>
  </svg>
  <figcaption>Las dos entradas acaban en la misma <strong>cita fija</strong>. El MCP sustituye al buscador sin cambiar lo que reciben las skills.</figcaption>
</figure>

### 1. Formato de la cita

Cada aviso que hoy dice «Norma y artículo» pasa a llevar una cita con
cuatro partes:

```text
RGPD art. 9.1 · nota rgpd-art-9 (L19) · DOUE L 119, 4.5.2016, CELEX 32016R0679
```

- **Norma, artículo y apartado**: lo que lee la persona.
- **Id de la nota y líneas**: el `name` del front matter, para que Claude
  abra el pasaje sin leer la nota entera.
- **Fuente oficial**: lo único que hace fe (DOUE o BOE), sacado de
  `celex` o del manifiesto de `fuentes/`.
- Si la cita es de una guía (AESIA, AEPD, CEPD, Comisión), se dice que es
  orientación y se cita además el artículo al que se refiere. Una guía no
  basta para afirmar que algo es obligatorio.
- Si no hay nota que respalde la afirmación, el aviso lo dice («sin nota
  que lo respalde») en lugar de inventar la cita.

### 2. Mapa curado: `knowledge/citas.yaml`

Un fichero que une cada señal y cada tema de las skills con sus citas.
Los hooks, que son Python stdlib, lo leen igual que `signals.yaml`:

```yaml
pii-terms:
  - {cita: "RGPD art. 5.1.c", nota: rgpd-art-5, lineas: L23}
  - {cita: "RGPD art. 25", nota: rgpd-art-25}
  - {apoyo: "AESIA guía 07, «Otros elementos a considerar»", nota: aesia-07-guia-de-datos-y-gobernanza-de-datos-08-otros-elementos-a-considerar}
scoring-model:
  - {cita: "AI Act anexo III, punto 5.b", nota: ai-act-anexo-iii, lineas: L51}
```

Las líneas se calculan al regenerar las notas y un test comprueba que cada
`nota` existe y que el texto citado sigue en esas líneas. Así un cambio
normativo que mueva el texto rompe el test, no el aviso.

### 3. Buscador para preguntas abiertas

Prototipo en `scripts/buscar.py` (lógica en `scripts/aiact/notas.py`),
sin dependencias. Indexa las 806 notas en 2 614 pasajes en medio segundo.
Lleva dos de las tres operaciones que la propuesta del prototipo preveía
para el MCP; la tercera queda para después:

| Operación | Ejemplo | Cómo |
| --- | --- | --- |
| Traer un artículo | `buscar.py articulo rgpd 5.1.c` | Por `norma` y `unidad`; devuelve la línea del apartado y la letra |
| Buscar citas | `buscar.py citas -q "…" -q "…" --en "…"` | BM25 por pasajes; cada `-q` busca en notas en español y cada `--en` en las inglesas; devuelve normas y guías por separado, con la línea del mejor pasaje |
| Contrastar (pendiente) | `buscar.py contrastar "el art. 50 aplica desde 2026-08-02"` | Trae los pasajes que nombran ese artículo para que Claude los lea |

**El idioma lo resuelve Claude, no un glosario.** Andrés señaló que se
preguntará en español y parte de las fuentes solo está en inglés. Son 50
notas: las directrices del art. 6 (borrador) y las dos del CEPD. Otras
58 son la versión inglesa de las directrices del art. 50, que ya están
en español, y el buscador las omite. La skill pide a Claude tres
consultas: la pregunta tal cual, la misma con el vocabulario de la norma
(«chatbot» → «interactuar con un sistema de IA») y su traducción al
inglés. Cada una busca solo en las notas de su idioma; las del mismo
idioma se unen con RRF y los idiomas se intercalan, para que el inglés no
quede tapado.

Resultado con las 20 consultas de prueba (acierto si una nota esperada
sale entre las 3 normas o las 3 guías primeras):

| Consultas que recibe el buscador | Aciertos |
| --- | --- |
| Solo la pregunta en español | 15 de 20 |
| Español y su traducción al inglés | 17 de 20 |
| Español y vocabulario de la norma | 17 de 20 |
| Español, vocabulario de la norma e inglés | **19 de 20** |

Falla «exportar datos a un proveedor fuera del EEE»: la reformulación
encuentra el art. 44 del RGPD, pero la pregunta coloquial la empuja fuera
de las tres primeras. Las reformulaciones de la prueba las he escrito yo
como las haría Claude; falta medirlas con Claude de verdad desde una
skill.

Para pasar del prototipo al plugin hacen falta tres cambios en el
troceado:

- **Notas dentro del plugin.** `trocear*.py` escribe en
  `plugins/ai-act-advisor/knowledge/notas/` (o el build las copia). Con
  normas y guías son 7,5 MB; solo con normas, 2 MB.
- **Front matter común.** Todas las notas con `tags` de un vocabulario
  cerrado (los temas de `signals.yaml` y de las skills, no palabras del
  título) y las de guías con `norma` y `articulos`.
- **Anclas por apartado.** Un campo `apartados` con la línea de cada
  apartado, para traer solo el que se cita.

Los hooks no pasan por Claude, así que no pueden reformular: para ellos
está el mapa curado del punto 2.

### 4. Versión madura: MCP con embeddings

Cuando el buscador se quede corto, el MCP de D02 expone las mismas tres
operaciones y devuelve el mismo formato. Las skills no cambian. Los
embeddings resuelven sinónimos y preguntas largas sin reformular, pero
traen un modelo, un índice que regenerar y resultados que no se pueden
reproducir con un grep. Merece la pena cuando haya preguntas reales de
PM que el buscador no responda, y eso se mide con el conjunto de
consultas de prueba de abajo.

## Alternativas

| Opción | Dependencias | Inglés y sinónimos | Reproducible | Mantenimiento | Uso |
| --- | --- | --- | --- | --- | --- |
| Grep sobre texto y front matter | Ninguna | No | Sí | Ninguno | Base de todo |
| Mapa curado señal → cita | Ninguna | No aplica | Sí | Una línea por señal, revisada en PR | Avisos de hooks y skills |
| BM25 stdlib con consultas reformuladas por Claude | Ninguna | Sí, vía Claude | Sí, dadas las consultas | Ninguno | Preguntas abiertas, ahora (prototipo) |
| RAG con embeddings locales (MCP) | Modelo y servidor | Sí | No del todo | Índice por versión | Versión madura |
| RAG como servicio | Cuenta externa y red | Sí | No | Servicio | Descartado: saca la consulta del proyecto |

## Cómo se mide

`tests/consultas-citas.json` guarda 20 preguntas con su reformulación,
su traducción y las notas esperadas; `tests/test_buscar.py` falla si el
buscador baja de 18 aciertos. Es el mismo conjunto que decidirá cuándo
pasar a embeddings: cuando las preguntas reales de PM y DE que se añadan
dejen de salir.

## Pendiente

> [!PENDING] D21 · decisiones para Andrés (issue #15)
> 1. Si las notas viajan con el plugin enteras (7,5 MB) o solo las normas
>    (2 MB) y las guías se consultan desde el repo.
> 2. Si el formato de cita de arriba vale, en particular las líneas.
> 3. Si se empieza por el mapa curado y el buscador stdlib y el MCP con
>    embeddings queda para cuando el conjunto de consultas lo pida.
