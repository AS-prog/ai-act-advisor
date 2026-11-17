#!/usr/bin/env bash
# Hook PostToolUse (Read, Edit, Write): solo añade contexto, nunca deniega.
# Por hacer (prototipo):
#   1. Leer de stdin la ruta del fichero tocado; seguir solo con .sql, .py, .ipynb y .yml de dbt.
#   2. Buscar las señales de knowledge/signals.yaml y de los adaptadores activos en el perfil.
#   3. Si hay una señal nueva en la sesión, devolver additionalContext con la señal,
#      el fichero y la skill que conviene cargar.
# Esqueleto: no hace nada todavía.
exit 0
