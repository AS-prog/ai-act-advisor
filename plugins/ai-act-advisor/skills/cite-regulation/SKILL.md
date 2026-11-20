---
name: cite-regulation
description: "Respuestas legales con cita comprobada: busca en las notas normativas del plugin (AI Act, RGPD, LOPDGDD, Omnibus, RD 723/2026, sentencias y guías de AESIA, AEPD, CEPD y Comisión) el pasaje que respalda la respuesta y lo cita con formato fijo. Úsala antes de responder de memoria a cualquier pregunta sobre normativa de datos o de IA: qué artículo o norma regula algo, si algo es obligatorio o desde cuándo, qué significa un concepto jurídico o técnico de la norma (seudonimización, anonimización, singularización, perfilado, encargado, sistema de IA, alto riesgo…), o qué dicen las guías. Úsala también cuando pregunten por una norma que quizá no esté en las notas (DSA, NIS2, Data Act…), para comprobarlo y decir «sin nota que lo respalde» si no está, y cuando otra skill necesite la cita de una afirmación legal."
---

# cite-regulation

Rol: PM, DE y AE. Responde con la **cita** de la nota que has leído. Una afirmación sin pasaje leído se entrega como «sin nota que lo respalde».

**Carpeta del plugin**: en Claude Code, `${CLAUDE_PLUGIN_ROOT}` llega ya sustituido por una ruta. Si lo ves tal cual, el plugin se instaló con APM: usa en su lugar la primera de estas carpetas, en la raíz del repo, que tenga `knowledge/VERSION` dentro: `.claude/hooks/ai-act-advisor`, `.github/hooks/scripts/ai-act-advisor`, `.codex/hooks/ai-act-advisor`, `.cursor/hooks/ai-act-advisor`, `.gemini/hooks/ai-act-advisor` o `.windsurf/hooks/ai-act-advisor`.

## 1. Reformula la pregunta

Escribe tres consultas:

- la pregunta tal cual;
- la misma con el vocabulario de la norma («chatbot» → «informar a las personas físicas de que están interactuando con un sistema de IA»);
- su traducción al inglés, porque parte de las directrices solo está en inglés.

## 2. Busca

```sh
sh "${CLAUDE_PLUGIN_ROOT}/scripts/run.sh" buscar.py citas -q "PREGUNTA" -q "VOCABULARIO DE LA NORMA" --en "ENGLISH"
```

Devuelve la carpeta de las notas y dos listas, «Normas (cita)» y «Guías (apoyo)»; cada resultado trae el id de la nota, su fichero y la línea del mejor pasaje (`rgpd/rgpd-art-30.md:L17`).

Si ya sabes el artículo, ve directo al apartado: `buscar.py articulo rgpd 30.1` (normas: `ai-act`, `rgpd`, `lopdgdd`, `omnibus`; también `articulo ai-act "anexo III 5.b"`).

Si ningún resultado trata de lo que se pregunta, repite una vez con otro vocabulario. Si el script no encuentra las notas, dilo junto con su mensaje (`--notas DIR` o `AIACT_NOTAS` indican dónde están) y sigue al paso 4 sin cita.

## 3. Lee el pasaje

Abre cada nota que vayas a citar en la línea indicada y lee hasta el final del apartado. De su cabecera toma `celex`. Paso hecho cuando cada afirmación de tu respuesta tiene un pasaje leído que la dice, o queda marcada como «sin nota que lo respalde».

## 4. Responde con la cita

Una línea por cita, con este formato:

```text
RGPD art. 30.1 · nota rgpd-art-30 (L17) · DOUE, CELEX 02016R0679-20160504
```

- **Norma, artículo y apartado**, como los lee una persona.
- **Nota y línea**: el id de la nota y la línea del pasaje leído.
- **Fuente oficial**: `DOUE, CELEX …` para reglamentos de la UE y `BOE, BOE-A-…` para leyes españolas, con el `celex` de la nota.
- **Guías** (AESIA, AEPD, CEPD, Comisión): cítalas como «orientación», con su nota y línea, y junto al artículo de la norma al que se refieren. La obligación la sostiene el artículo; la guía la explica.
- **Sin nota**: si las notas no cubren la norma o el punto preguntado, escribe «sin nota que lo respalde» y qué fuente oficial habría que consultar.

Cierra con la base normativa (fecha de `${CLAUDE_PLUGIN_ROOT}/knowledge/VERSION`) y «No es asesoramiento legal».
