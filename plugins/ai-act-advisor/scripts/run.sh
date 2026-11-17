#!/usr/bin/env sh
# Lanza un script del plugin con el Python que haya (python3 en macOS/Linux, python en Windows).
DIR="$(cd "$(dirname "$0")" && pwd)"
if command -v python3 >/dev/null 2>&1; then PY=python3
elif command -v python >/dev/null 2>&1; then PY=python
else exit 0
fi
exec "$PY" "$DIR/$@"
