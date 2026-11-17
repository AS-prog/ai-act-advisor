---
name: regulatory-update
description: "Actualización de la base normativa del plugin: revisa las fuentes oficiales de knowledge/sources.yaml, las compara con knowledge/ y deja los cambios en una rama con PR para revisión humana. Úsala en la tarea semanal, cuando un aviso diga que la base normativa tiene más de 90 días o cuando pidan «actualiza la normativa» o «revisa si ha cambiado el AI Act»."
---

# regulatory-update

Rol: mantenimiento del plugin. Tu trabajo termina con una PR abierta: quien mantiene el plugin la revisa y la fusiona. Una fecha mal leída haría avisar mal en todos los proyectos a la vez, así que cada cambio entra con su cita y con una persona que lo confirma.

**Carpeta del plugin**: en Claude Code, `${CLAUDE_PLUGIN_ROOT}` llega ya sustituido por una ruta. Si lo ves tal cual, el plugin se instaló con APM: usa en su lugar la primera de estas carpetas, en la raíz del repo, que tenga `knowledge/VERSION` dentro: `.claude/hooks/ai-act-advisor`, `.github/hooks/scripts/ai-act-advisor`, `.codex/hooks/ai-act-advisor`, `.cursor/hooks/ai-act-advisor`, `.gemini/hooks/ai-act-advisor` o `.windsurf/hooks/ai-act-advisor`. Haz lo mismo con `$CLAUDE_PROJECT_DIR`, que es la raíz del repo.

## 1. Sitúate en el repo del plugin

Hace falta un clon de `ai-act-advisor` con git, donde la base vive en `plugins/ai-act-advisor/knowledge/`. Compruébalo con `git rev-parse --show-toplevel` y la existencia de `knowledge/VERSION`.

Si la sesión está en otro repo o en la copia instalada del plugin (sin git), sigue en **modo informe**: haz los pasos 2 y 3 leyendo `${CLAUDE_PLUGIN_ROOT}/knowledge/`, entrega el informe y di que la PR queda por hacer desde un clon.

## 2. Lanza el vigilante

Delega la lectura de fuentes en el agente `regulatory-watcher`, para que las páginas no llenen este contexto. Pásale la ruta absoluta de `knowledge/` y la fecha de hoy. Devuelve un informe con cuatro partes: fuentes leídas y no leídas, cambios confirmados (cada uno con URL, cita literal, fichero afectado, valor actual y valor propuesto), cambios por verificar y novedades sin efecto en la base.

## 3. Tría el informe

Abre el fichero de `knowledge/` que señala cada cambio y comprueba que el valor actual que dice el informe es el que hay.

- **Confirmado**, con cita literal de una fuente oficial que sostiene el valor propuesto: entra en la rama.
- **Por verificar**, o confirmado cuya cita no sostiene el valor: va a la descripción de la PR como pendiente y `knowledge/` queda como está.

Hecho cuando cada cambio del informe está en una de las dos listas.

## 4. Aplica los cambios en una rama

Rama `regulatory/AAAA-MM-DD` desde la rama principal al día. Cada dato tiene un solo sitio:

| Qué cambia | Dónde |
|---|---|
| Una fecha de aplicación | `dates.yaml` |
| Un artículo, un punto del anexo III o un criterio de directrices | `ai-act-classification.md`, `transparency-art50.md`, `special-categories.md`, `masking-techniques.md` |
| El mapa de sector a anexo III | `sectors.yaml` |
| Una señal detectable | `signals.yaml` |
| Una URL o una fuente nueva | `sources.yaml` |

Después, los tres campos de control:

- `sources.yaml`: `last_checked` con la fecha de hoy en cada fuente que el vigilante leyó de verdad. Las no leídas conservan su valor.
- `VERSION`, `ultima_revision`: fecha de hoy **si se leyeron todas las fuentes**. Con alguna sin leer se queda como está y la PR dice cuáles faltaron: así la alerta de 90 días sigue reflejando la última revisión completa.
- `VERSION`, `consolidado_ai_act` y `reglamentos`: cambian solo si el informe trae un consolidado nuevo o un reglamento modificador nuevo en EUR-Lex.

Una revisión completa sin cambios también lleva PR, con solo `last_checked` y `ultima_revision`.

## 5. Busca las copias fuera de knowledge/

Las fechas y los artículos también están escritos en otros sitios, que no se actualizan solos. Por cada valor que cambió, busca el valor antiguo:

```sh
git grep -n "VALOR_ANTIGUO" -- plugins/ docs/ README.md
```

- Coincidencias en `plugins/ai-act-advisor/skills/`: corrígelas en la misma rama.
- Coincidencias en `plugins/ai-act-advisor/scripts/` (el campo `aplica` de los hallazgos está escrito en `core.py`) y en `docs/`: lístalas en la PR con fichero y línea. Cambiar código pide tests, y `docs/` se regenera con el sistema de diseño: lo decide quien revisa.

## 6. Comprueba y entrega

1. `python3 -m unittest discover -s tests` pasa (los ficheros de `knowledge/` se leen con un lector de YAML propio, más estricto que el estándar).
2. Commit en español y `git push` de la rama.
3. Abre la PR con `gh pr create`. Sin `gh` o sin permiso para subir, deja la rama en local y entrega el texto de la PR en la conversación.

La PR queda abierta y sin fusionar: ese es el final de esta skill.

## Forma de la PR

Título: `Base normativa: revisión de AAAA-MM-DD` (añade «sin cambios» si es el caso).

Cuerpo, en este orden:

1. **Resumen**: qué cambia para los avisos, en dos o tres líneas.
2. **Cambios**: tabla con fichero, valor anterior, valor nuevo, fuente (URL) y cita literal.
3. **Por verificar**: lo que el vigilante vio y no entra, con el motivo y qué habría que leer para confirmarlo.
4. **Copias fuera de knowledge/**: fichero y línea de lo que queda por cambiar a mano.
5. **Fuentes**: leídas y no leídas, con el motivo de las no leídas.
6. **Efecto en proyectos**: qué avisos cambian de «aplica desde» a «aplica ya», o al revés, y si conviene que los proyectos relancen `/project-init`.

## Límites

- El plugin no programa la tarea semanal: se configura fuera (una tarea programada de Claude Code o del CI que lance `/regulatory-update`).
- El vigilante lee páginas públicas. Algunas fuentes oficiales rechazan lectores automáticos o devuelven el texto truncado; esas quedan como no leídas, y revisarlas a mano es parte de la revisión de la PR.
- La base resume la norma; no guarda el texto íntegro. Un cambio de redacción que no mueve una fecha, un artículo citado o un criterio puede pasar sin efecto en `knowledge/`.
