#!/usr/bin/env bash
# Convierte los textos oficiales (XHTML de EUR-Lex y XML de la API de legislación
# consolidada del BOE) a Markdown no oficial, con artículos como encabezados.
# Requisitos: pandoc >= 3, python3 con beautifulsoup4 y lxml, curl.
# Uso desde la raíz del repo: bash docs/fuentes/conversion/convertir.sh docs/fuentes docs/fuentes/md
#   <dir_fuentes> debe contener los .xhtml descargados de EUR-Lex con los nombres de docs/fuentes.
set -euo pipefail
SRC=${1:?dir de fuentes}; OUT=${2:?dir de salida}
HERE=$(cd "$(dirname "$0")" && pwd); TMP=$(mktemp -d); mkdir -p "$OUT"

eurlex() { # $1 = nombre base del .xhtml, $2 = título, $3 = fuente oficial
  python3 -I "$HERE/flatten.py" "$SRC/$1.xhtml" "$TMP/$1.html"
  pandoc -f html -t gfm-raw_html --wrap=none "$TMP/$1.html" -o "$TMP/$1.md"
  python3 -I "$HERE/clean.py" "$TMP/$1.md" "$OUT/$1.md" "# $2

> **Conversión a Markdown no oficial** ($(date +%d-%m-%Y)) de \`$1.xhtml\`.
> Fuente oficial: $3
> Solo hacen fe los textos publicados en el Diario Oficial. Los marcadores ▼B, ▼M1, ►C1 indican el acto de origen de cada fragmento."
}

eurlex 2026-07-27-ai-act-2024-1689-consolidado-es "Reglamento (UE) 2024/1689 (AI Act), texto consolidado a 27-07-2026" \
  "EUR-Lex, CELEX 02024R1689-20260727, https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/spa"
eurlex 2026-07-24-omnibus-2026-1744-es "Reglamento (UE) 2026/1744 (Digital Omnibus sobre IA)" \
  "DO L, CELEX 32026R1744, https://eur-lex.europa.eu/eli/reg/2026/1744/oj/spa"
eurlex 2016-05-04-rgpd-2016-679-consolidado-es "Reglamento (UE) 2016/679 (RGPD), texto consolidado a 04-05-2016" \
  "EUR-Lex, CELEX 02016R0679-20160504, https://eur-lex.europa.eu/eli/reg/2016/679/oj/spa"

# LOPDGDD: API de legislación consolidada del BOE
curl -sS -H 'Accept: application/xml' -o "$TMP/lopdgdd.xml" \
  "https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/BOE-A-2018-16673/texto"
python3 -I "$HERE/boe.py" "$TMP/lopdgdd.xml" "$OUT/2025-12-27-lopdgdd-3-2018-consolidado-boe.md" "# Ley Orgánica 3/2018 (LOPDGDD), texto consolidado

> **Conversión a Markdown no oficial** ($(date +%d-%m-%Y)) desde la API de legislación consolidada del BOE (versión más reciente de cada bloque).
> Fuente oficial: https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673
> Solo hace fe el texto publicado en el BOE."

# Comprobaciones: ninguna tabla perdida
if grep -l '\[TABLE\]' "$OUT"/*.md; then echo "ERROR: pandoc dejó tablas sin convertir" >&2; exit 1; fi
for f in "$OUT"/*.md; do echo "$(basename "$f"): $(grep -c '^#### ' "$f") encabezados de artículo"; done
rm -rf "$TMP"
