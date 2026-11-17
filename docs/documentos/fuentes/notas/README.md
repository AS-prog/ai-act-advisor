# Notas normativas (fuentes legales troceadas)

Una nota por artículo, anexo o disposición del AI Act, el RGPD, la LOPDGDD y el Omnibus 2026/1744. Cada nota lleva front matter con formato skill (`name`, `description`, `metadata.tags`, `metadata.origen`) para encontrarla con grep o con un índice.

- Son **derivadas** de `../md/` (conversiones no oficiales). No se editan a mano: `python3 -I ../md/conversion/trocear.py` las regenera.
- `INDICE.md` lista todas las notas.
- El Omnibus se trocea solo por sus artículos propios (1 a 4 y 75 ter, quater y quinquies), así que `omnibus-art-1` es larga.
- Solo hace fe el texto del Diario Oficial o del BOE.

Ejemplo: `grep -rl "gobernanza de datos" docs/documentos/fuentes/notas`.
