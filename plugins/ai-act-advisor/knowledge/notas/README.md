# Notas normativas (fuentes legales troceadas)

Fuentes oficiales troceadas en notas con front matter con formato skill (`name`, `description`, `metadata`), para encontrarlas con grep, con un índice o con `scripts/buscar.py`. Viajan con el plugin (decisión D21), también en las instalaciones con APM, que copian `knowledge/` entero. Las fuentes de las que salen están en `docs/documentos/fuentes/` del repo, y el campo `origen` de cada nota es relativo a esa carpeta.

- **Normas** (`INDICE.md`): una nota por artículo, anexo o disposición del AI Act, el RGPD, la LOPDGDD y el Omnibus 2026/1744. Se generan desde `docs/documentos/fuentes/md/` con `python3 -I docs/documentos/fuentes/md/conversion/trocear.py`. El Omnibus solo se trocea en sus artículos propios (1 a 4 y 75 ter, quater y quinquies).
- **Guías y directrices** (`INDICE-guias.md`): guías AESIA 01-16, directrices de la Comisión (definición de sistema de IA, prácticas prohibidas, art. 6, art. 50), directrices del CEPD, documentos de la AEPD y el RD 723/2026. Se generan desde los PDF con `python3 -I docs/documentos/fuentes/md/conversion/trocear_pdf.py` (necesita `pdftotext` y `pypdf`). Se trocean por marcadores del PDF, por el índice de la guía o por bloques de 8 páginas; la extracción de texto no recupera bien tablas ni maquetación.
- Las notas son derivadas: no se editan a mano, se regeneran.
- **Sentencia TJUE C-184/20 y checklists Excel de AESIA** (`INDICE-otros.md`): `python3 -I docs/documentos/fuentes/md/conversion/trocear_otros.py` (necesita pandoc, bs4 y openpyxl). La sentencia se trocea por secciones; cada hoja con datos de cada Excel es una nota con tabla Markdown (las hojas vacías de autoevaluación se omiten).
- Solo hace fe el texto del Diario Oficial o del BOE.

Ejemplos, desde la raíz del repo:

```sh
grep -rl "gobernanza de datos" plugins/ai-act-advisor/knowledge/notas
python3 plugins/ai-act-advisor/scripts/buscar.py articulo rgpd 9.1
```
