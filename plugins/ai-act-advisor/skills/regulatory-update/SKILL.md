---
name: regulatory-update
description: "Revisa las fuentes oficiales (EUR-Lex, Oficina de IA, AESIA, AEPD, CEPD), compara con la base de conocimiento del plugin y prepara un PR con los cambios para revisión humana. Úsala en la tarea semanal o cuando pidan «actualiza la normativa»."
---

# regulatory-update

> Esqueleto del prototipo. El diseño está en `docs/diseno/propuesta-prototipo.md`.

Rol: mantenimiento. Tarea programada semanal o lanzamiento manual.

## Qué hará

1. Delegar la lectura de fuentes en el agente `regulatory-watcher`.
2. Actualizar `knowledge/` en una rama y abrir un PR con el resumen. Nunca fusionar.
3. Actualizar `knowledge/VERSION` y `last_checked` en `knowledge/sources.yaml`.

## Forma del aviso

Riesgo · Norma y artículo · Aplica ya o desde AAAA-MM-DD · Qué puede pasar · Opciones · A quién escalar · Base normativa de AAAA-MM-DD · No es asesoramiento legal.

Nunca bloquea: informa y deja la decisión a quien trabaja.
