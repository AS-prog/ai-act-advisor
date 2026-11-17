# ai-act-advisor

Plugin de Claude Code que avisa a project managers (PM), data engineers (DE) y analytics engineers (AE) de los riesgos del AI Act y del RGPD en proyectos de ingeniería y analítica de datos, y sugiere cómo mitigarlos. Nunca bloquea: informa y deja la decisión a quien trabaja.

> Estado: primer prototipo. La auditoría y los hooks cubren la PII en la ingesta; las siete skills y el agente están escritos. El diseño está en [`docs/diseno/propuesta-prototipo.md`](docs/diseno/propuesta-prototipo.md); la página HTML, en `docs/index.html`.

## Qué hay

| Ruta | Qué es |
|---|---|
| `.claude-plugin/marketplace.json` | El marketplace `ai-act-advisor` |
| `plugins/ai-act-advisor/` | El plugin: manifiesto, skills, agente, hooks, scripts y base de conocimiento |
| `plugins/ai-act-advisor/skills/` | `project-init` y `risk-summary` (PM); `pii-masking`, `special-categories`, `ai-act-classify` y `ai-transparency` (riesgo); `regulatory-update` (mantenimiento) |
| `plugins/ai-act-advisor/hooks/hooks.json` | `SessionStart` y `PostToolUse`: solo añaden contexto |
| `plugins/ai-act-advisor/agents/` | `regulatory-watcher`, que vigila las fuentes oficiales |
| `plugins/ai-act-advisor/knowledge/` | Fechas, señales, sectores, técnicas y fuentes, con la fecha de la base normativa |
| `plugins/ai-act-advisor/adapters/` | Señales y mitigaciones por stack |
| `plugins/ai-act-advisor/scripts/` | `audit.py` (auditoría de solo lectura) y `hook.py` (hooks), en Python sin dependencias |
| `examples/medallion-demo/` | Proyecto ficticio para probar la auditoría y los hooks |
| `tests/` | `python3 -m unittest discover -s tests` |
| `docs/` | Documentación con [asprog-design-system](https://github.com/AS-prog/asprog-design-system): propuesta, investigación y sitio |

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

Las skills y el agente llegan a todos los agentes. Los avisos automáticos (hooks) dependen de cada agente: en Claude Code funcionan igual que con el plugin; en el resto, revisa `plugins/ai-act-advisor/apm.yml` para ver qué se pierde.

## Probar el prototipo

```
python3 plugins/ai-act-advisor/scripts/audit.py report --root examples/medallion-demo
python3 -m unittest discover -s tests
```

En un repo con el plugin instalado, `/project-init` audita, deja `.ai-act/rules.json`, `.ai-act/baseline.json` y `.ai-act/audits/AAAA-MM-DD.md`, y a partir de ahí los hooks solo avisan de riesgos nuevos.

## Aviso

El plugin no es asesoramiento legal. Cada aviso dice de qué norma viene, desde cuándo aplica y la fecha de la base normativa que usa.
