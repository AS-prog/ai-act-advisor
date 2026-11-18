# ai-act-advisor

## What this is

Plugin de Claude Code que avisa a PM, DE y AE de los riesgos del AI Act y del RGPD en proyectos de datos, sin bloquear nunca.

## Place in the setup

- Develop on: Mac mini. El Air y el teléfono entran por Remote Control.
- Delegates to: nadie. No delega trabajo a la Pi.
- Role: ninguno. Sesión de trabajo normal.

## Knowledge packages

Ninguno. Este repo no declara paquetes en `apm.yml`.

## How to verify

`python3 -m unittest discover -s tests`; las páginas de `docs/site/` pasan `delphos-check`.

## Handoff

El estado se deja en una rama con su PR en borrador: qué está hecho, qué falta y cómo se comprueba. Lo que no es código va al PR o a las notas del vault. Nada queda solo en la sesión.

## Repo notes

### Del AGENTS.md anterior

- **Idioma**: el código va en inglés (carpetas, ficheros, claves, identificadores); todo texto visible, comentarios, commits y documentación, en español.
- **Nunca bloquear**: ningún hook deniega una acción. Los hooks solo añaden contexto; las skills informan y proponen opciones.
- **Una sola fuente**: hooks y skills leen `plugins/ai-act-advisor/knowledge/`. Una fecha o un artículo se cambia ahí, no en una skill.
- **Cada aviso con su norma**: artículo, «aplica ya» o «aplica desde AAAA-MM-DD», fecha de la base normativa y «no es asesoramiento legal».
- **Actualizaciones normativas**: siempre por PR con revisión humana.
- **Documentación**: con el plugin `documentation` de `asprog-design-system`. `docs/site/` solo lleva HTML (más `site.toml` y la copia del sistema de diseño); su fuente Markdown, la investigación, los pendientes y los textos oficiales van en `docs/documentos/`, con la misma subcarpeta que su página (`guia/`, `diseno/`, `tecnica/`). Cada página está en `docs/site/site.toml`; tras añadir una, `site.py build`. Las páginas pasan `delphos-check`.
