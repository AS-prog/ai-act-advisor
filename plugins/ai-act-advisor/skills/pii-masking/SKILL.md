---
name: pii-masking
description: "Explica el riesgo de trabajar con datos personales sin proteger y propone técnicas (supresión, seudonimización, hashing con clave, tokenización, generalización, masking dinámico) adaptadas al stack y a la capa medallion. Úsala cuando aparezcan columnas con PII en SQL, dbt, Spark o Python, una fuente sin clave de PII declarada, PII declarada que no se aplica o una exportación a terceros."
---

# pii-masking

Rol: DE y AE. Carga automática cuando un hook o el usuario la mencionan. Nunca bloquea: explica, propone y deja la decisión al ingeniero.

**Carpeta del plugin**: en Claude Code, `${CLAUDE_PLUGIN_ROOT}` llega ya sustituido por una ruta. Si lo ves tal cual, el plugin se instaló con APM: usa en su lugar la primera de estas carpetas, en la raíz del repo, que tenga `knowledge/VERSION` dentro: `.claude/hooks/ai-act-advisor`, `.github/hooks/scripts/ai-act-advisor`, `.codex/hooks/ai-act-advisor`, `.cursor/hooks/ai-act-advisor`, `.gemini/hooks/ai-act-advisor` o `.windsurf/hooks/ai-act-advisor`. Haz lo mismo con `$CLAUDE_PROJECT_DIR`, que es la raíz del repo.

## 1. Entiende qué hay

- Columnas afectadas y tipo de dato personal (contacto, identificador, financiero, ubicación). Si alguna es de categoría especial (salud, biometría, ideología…), cambia a la skill `special-categories`.
- Capa en la que aparecen (fuente, Bronze, Silver, Gold, exportación) y si salen del perímetro del cliente.
- Stack, desde `.ai-act/profile.yaml` o `.ai-act/rules.json`. Si el repo declara la PII con una clave propia (`pii_key`, por ejemplo `pii_columns`), úsala en tus propuestas en lugar de inventar otra.

No abras ficheros de datos para comprobarlo: trabaja con el código y la configuración.

## 2. Explica el riesgo en pocas líneas

- RGPD art. 5.1.c (minimización) y art. 25 (protección desde el diseño): aplican ya.
- Art. 32 (seguridad) si la PII queda en claro en almacenamiento compartido; art. 17 (supresión) si no hay forma de borrar a una persona; art. 28 y 44-49 si se exporta a un tercero o fuera del EEE.
- Qué puede pasar en concreto: copia en claro en Bronze que nadie revisa, filtración en logs o exportaciones, imposibilidad de atender un derecho de supresión, reutilización para entrenar un modelo sin base jurídica.

## 3. Propón opciones

Lee `${CLAUDE_PLUGIN_ROOT}/knowledge/masking-techniques.md` y ofrece dos o tres opciones que encajen con el stack y la capa, con su límite (qué no protege). Orden habitual:

1. No traer la columna si nadie la usa (supresión en la ingesta).
2. Seudonimizar en la frontera Bronze → Silver con hash con clave (HMAC) o tokenización, guardando la clave fuera del repo.
3. Generalizar lo que se usa para analítica (fecha de nacimiento → año o tramo de edad, código postal → provincia).
4. Masking dinámico o políticas de columna del warehouse para quien solo consulta.

Si el repo ya tiene una clave de PII que se valida pero no se aplica, la propuesta natural es aplicar esa misma clave en el escritor de Bronze o Silver. Enséñalo con un fragmento corto en el lenguaje del repo, sin editar nada salvo que el ingeniero lo pida.

## 4. Deja la decisión

Termina con: qué recomiendas, a quién escalar si decide no protegerla (DPO si son datos de clientes finales, PM si cambia alcance o coste) y cómo registrar la decisión: estado `aceptado` y `justification` en `.ai-act/baseline.json`, o `mitigado` cuando esté hecho, siempre con `decided_by` (quién decide) y `decided_on` (la fecha del día, AAAA-MM-DD).

## Forma del aviso

Riesgo · Norma y artículo · Aplica ya · Qué puede pasar · Opciones · A quién escalar · Base normativa de AAAA-MM-DD (de `knowledge/VERSION`) · No es asesoramiento legal.

**Cita de la norma.** Antes de escribir «Norma y artículo», trae el pasaje: `sh "${CLAUDE_PLUGIN_ROOT}/scripts/run.sh" buscar.py articulo <ai-act|rgpd|lopdgdd|omnibus> <ref>` (por ejemplo `articulo ai-act "anexo III 5.b"`), lee la línea que devuelve y cita como la skill `cite-regulation`: `AI Act anexo III 5.b · nota ai-act-anexo-iii (L51) · DOUE, CELEX …`. Si no sabes el artículo, usa `buscar.py citas` como explica esa skill. Si no hay nota que lo diga, escribe «sin nota que lo respalde» en lugar de citar de memoria.
