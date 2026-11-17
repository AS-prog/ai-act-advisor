# Demo de ai-act-advisor

Kit para probar el plugin de punta a punta con Claude Code. El guion, paso a paso por rol (PM, DE y AE), está en `docs/site/guia/demo.html` (fuente: `docs/documentos/guia/demo.md`).

Todo es ficticio: la empresa, los contactos y el código. No hay ficheros de datos.

| Fichero | Qué es |
|---|---|
| `preparar.py` | Copia `examples/medallion-demo` a una carpeta de trabajo (fase 1), le añade la fase 2 (`--fase 2`) o prepara una base normativa de hace 120 días (`--base-antigua`) |
| `ensayo.py` | Recorre el guion sin Claude, con la auditoría y los hooks reales, y comprueba que cada aviso sale donde debe |
| `fase-2/` | Lo que pide el cliente en la fase 2: modelo de impago, asistente con LLM, encuesta de accesibilidad y una fuente nueva |
| `perfil.yaml` | El perfil que deja `/project-init` con las respuestas del guion |

```
python3 examples/demo/ensayo.py
python3 examples/demo/preparar.py --dest ~/ai-act-demo
cd ~/ai-act-demo && claude --plugin-dir <clon>/plugins/ai-act-advisor
```

La carpeta de trabajo queda fuera de este repo: la demo no cambia nada aquí.
