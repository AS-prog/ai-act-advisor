# Guía para agentes

- **Idioma**: el código va en inglés (carpetas, ficheros, claves, identificadores); todo texto visible, comentarios, commits y documentación, en español.
- **Nunca bloquear**: ningún hook deniega una acción. Los hooks solo añaden contexto; las skills informan y proponen opciones.
- **Una sola fuente**: hooks y skills leen `plugins/ai-act-advisor/knowledge/`. Una fecha o un artículo se cambia ahí, no en una skill.
- **Cada aviso con su norma**: artículo, «aplica ya» o «aplica desde AAAA-MM-DD», fecha de la base normativa y «no es asesoramiento legal».
- **Actualizaciones normativas**: siempre por PR con revisión humana.
- **Documentación**: con el plugin `documentation` de `asprog-design-system`. Cada página vive en el sitio (`docs/site/site.toml`); tras añadir una, `site.py build`. Las páginas pasan `delphos-check`.
