# ai-act-advisor

Plugin de Claude Code que avisa a project managers (PM), data engineers (DE) y analytics engineers (AE) de los riesgos del AI Act y del RGPD en proyectos de ingeniería y analítica de datos, y sugiere cómo mitigarlos. Nunca bloquea: informa y deja la decisión a quien trabaja.

> Estado: primer prototipo. La auditoría y los hooks cubren la PII en la ingesta; las siete skills y el agente están escritos. El diseño está en [`docs/documentos/diseno/propuesta-prototipo.md`](docs/documentos/diseno/propuesta-prototipo.md); el sitio HTML empieza en `docs/site/index.html` y la guía de uso está en `docs/site/guia/como-se-usa.html`.

## De qué trata

En un proyecto de datos los riesgos legales aparecen en el código antes que en ningún documento: una columna de email que entra en Bronze sin proteger, una exportación a un tercero, un modelo que puntúa a personas, un chatbot que no dice que es una IA. Quien escribe ese código rara vez tiene a mano el artículo que aplica ni la fecha desde la que obliga.

`ai-act-advisor` lleva ese conocimiento a la sesión de Claude Code de cada rol:

- **PM**: al arrancar, `/project-init` hace el perfil del proyecto (cliente, sector, finalidad, rol, datos personales, stack) y, si ya hay código, una auditoría de solo lectura de entornos y riesgos. Después, `risk-summary` resume los riesgos y las decisiones para el cliente o el DPO.
- **DE y AE**: mientras trabajan, los hooks detectan señales (PII sin clave declarada, escritura en Bronze con cambio de esquema, exportaciones, SDK de LLM) y avisan una sola vez por sesión. Las skills explican el riesgo, la norma y el artículo, y proponen opciones adaptadas al stack: enmascarar, seudonimizar, generalizar, clasificar el sistema o añadir el aviso de IA.
- **Mantenimiento**: el agente `regulatory-watcher` revisa las fuentes oficiales (EUR-Lex, Comisión, AESIA, AEPD, CEPD) y propone actualizar la base normativa.

El plugin no bloquea nada: informa, propone y deja la decisión a quien trabaja. Cada decisión queda en `.ai-act/baseline.json` (abierto, mitigado o aceptado con justificación, con quién decide y cuándo), y los avisos solo vuelven si aparece algo nuevo o queda algo abierto que nadie ha revisado.

Además de como plugin de Claude Code, se puede instalar con [APM](https://github.com/microsoft/apm) en otros agentes (Copilot, Cursor, Codex, Gemini…). Es experimental: las skills llegan a todos, pero algunos avisos automáticos se pierden según el agente (ver [Con APM](#con-apm-otros-agentes-experimental)).

El marco es el AI Act tras el Omnibus 2026/1744, bajando al RGPD y la LOPDGDD, con la normativa española (AESIA, AEPD). Hoy el foco está en el RGPD y la PII en la ingesta, que es lo que más aparece en proyectos reales.

## Qué hay

| Ruta | Qué es |
|---|---|
| `.claude-plugin/marketplace.json` | El marketplace `ai-act-advisor` |
| `plugins/ai-act-advisor/` | El plugin: manifiesto, skills, agente, hooks, scripts y base de conocimiento |
| `plugins/ai-act-advisor/skills/` | `project-init` y `risk-summary` (PM); `pii-masking`, `special-categories`, `ai-act-classify` y `ai-transparency` (riesgo); `regulatory-update` (mantenimiento) |
| `plugins/ai-act-advisor/apm.yml` | Manifiesto para instalar el plugin con APM en otros agentes |
| `plugins/ai-act-advisor/hooks/hooks.json` | `SessionStart` y `PostToolUse`: solo añaden contexto |
| `plugins/ai-act-advisor/agents/` | `regulatory-watcher`, que vigila las fuentes oficiales |
| `plugins/ai-act-advisor/knowledge/` | Fechas, señales, sectores, técnicas y fuentes, con la fecha de la base normativa |
| `plugins/ai-act-advisor/adapters/` | Señales y mitigaciones por stack |
| `plugins/ai-act-advisor/scripts/` | `audit.py` (auditoría de solo lectura) y `hook.py` (hooks), en Python sin dependencias |
| `examples/medallion-demo/` | Proyecto ficticio para probar la auditoría y los hooks |
| `examples/demo/` | La demo guiada: fase 2 del proyecto ficticio, perfil, `preparar.py` y `ensayo.py` |
| `tests/` | `python3 -m unittest discover -s tests` |
| `docs/site/` | El sitio HTML con [asprog-design-system](https://github.com/AS-prog/asprog-design-system): portada (`index.html`), páginas, copia del sistema de diseño y `site.toml` |
| `docs/documentos/` | Los documentos fuente: Markdown de cada página, investigación, pendientes y, en `fuentes/`, los textos oficiales (PDF, XHTML) con su manifiesto |

## Instalar

```
/plugin marketplace add AS-prog/ai-act-advisor
/plugin install ai-act-advisor@ai-act-advisor
```

### Con APM (otros agentes, experimental)

[APM](https://github.com/microsoft/apm) instala el mismo plugin en el repo del proyecto y lo traduce a cada agente (Copilot, Codex, Cursor, Gemini…). Desde la raíz del repo del proyecto:

```
apm install AS-prog/ai-act-advisor/plugins/ai-act-advisor --target copilot
```

Las 7 skills llegan a todos los agentes; el agente `regulatory-watcher`, a todos salvo Gemini y Windsurf. Los avisos automáticos (hooks) dependen del agente:

| Agente | Aviso al abrir sesión | Aviso al leer o editar un fichero |
|---|---|---|
| Claude Code | Sí | Sí |
| Copilot (CLI y VS Code) | Sí | Sí, según la documentación; sin probar en el agente |
| Cursor | Sí | Sí, según la documentación; sin probar en el agente |
| Codex | Sí | Solo al editar (no salta al leer) |
| Gemini CLI | Sí | No: sus herramientas se llaman distinto y el filtro no las reconoce |
| Windsurf | Sin comprobar | Sin comprobar |
| OpenCode | No (no tiene hooks) | No |

Los hooks se lanzan con `sh` y Python 3. En Windows, Claude Code usa Git Bash; los demás agentes pueden necesitarlo instalado. La base normativa se copia al repo del proyecto: tras una actualización, `apm update` la refresca.

## Probar el prototipo

```
python3 plugins/ai-act-advisor/scripts/audit.py report --root examples/medallion-demo
python3 -m unittest discover -s tests
```

Para probarlo entero con Claude Code hay una demo guiada de una hora, con un proyecto ficticio en dos fases y catorce pasos por rol (PM, DE y AE) que ejercitan las siete skills, el agente y los dos hooks. El guion está en `docs/site/guia/demo.html` y los ficheros en `examples/demo/`:

```
python3 examples/demo/ensayo.py                       # ensayo sin Claude: comprueba cada aviso del guion
python3 examples/demo/preparar.py --dest ~/ai-act-demo  # prepara la carpeta de trabajo
cd ~/ai-act-demo && claude --plugin-dir <clon>/plugins/ai-act-advisor
```

En un repo con el plugin instalado, `/project-init` audita, deja `.ai-act/rules.json`, `.ai-act/baseline.json` y `.ai-act/audits/AAAA-MM-DD.md`, y a partir de ahí los hooks avisan de los riesgos nuevos y de los abiertos que nadie ha revisado.

## Aviso

El plugin no es asesoramiento legal. Cada aviso dice de qué norma viene, desde cuándo aplica y la fecha de la base normativa que usa.
