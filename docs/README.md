# Documentación de ai-act-advisor

Aquí está todo lo que explica el plugin: un sitio HTML para leerlo y los documentos de los que sale.

| Carpeta | Qué contiene |
|---|---|
| `site/` | Solo HTML: el sitio publicado, hecho con [asprog-design-system](https://github.com/AS-prog/asprog-design-system). Empieza en `site/index.html` |
| `documentos/` | Las fuentes de cada página en Markdown, la investigación, los pendientes y, en `fuentes/`, los textos oficiales (PDF, XHTML, XML) con su manifiesto |

Cada página HTML tiene su Markdown en la misma subcarpeta de `documentos/`. Por ejemplo, `site/guia/como-se-usa.html` sale de `documentos/guia/como-se-usa.md`.

## Qué leer

- **Guía** (`guia/como-se-usa`): cómo se instala y se usa el plugin, aviso a aviso. Empieza aquí si vas a usarlo.
- **Demo** (`guia/demo`): guion de una hora para probar el plugin entero con un proyecto ficticio, paso a paso por rol.
- **Técnica** (`tecnica/uso-del-prototipo`): qué hay por dentro, con las salidas reales sobre el proyecto de ejemplo.
- **Diseño** (`diseno/propuesta-prototipo`): la propuesta y las decisiones tomadas.
- **Pendientes** (`pendientes`): dudas normativas (P), decisiones abiertas (D) y lo ya verificado con fuente (V).
- **Investigación** (`documentos/investigacion/`): el AI Act tras el Omnibus 2026/1744 y las señales que usa el plugin.
- **Fuentes** (`documentos/fuentes/`): 37 documentos oficiales con nombre `AAAA-MM-DD-documento` y su `sha256` en el `README.md`. La carpeta `md/` tiene conversiones a Markdown, que no son oficiales, y `conversion/` los scripts que las generan.

## Regenerar el sitio

La configuración está en `site/site.toml`. La portada y la navegación se regeneran con la skill `site` del sistema de diseño:

```
uv run --no-project --with markdown python <asprog-design-system>/plugins/documentation/skills/site/scripts/site.py build --root .
```
