---
name: risk-summary
description: "Resumen de riesgos AI Act y RGPD de un proyecto en una página, para el PM: hallazgos abiertos por severidad, aceptados con su justificación, mitigados, y qué escalar y a quién. Sirve para un repo o para un proyecto de varios repos. Úsala cuando pidan «resumen de riesgos», «estado de cumplimiento», «qué tengo que escalar» o «riesgos del proyecto»."
---

# risk-summary

Rol: PM. Se lanza con `/risk-summary`. Es una lectura del estado: informa y deja las decisiones al PM. La única escritura posible es el propio resumen, y solo si el PM lo pide.

## 1. Lee el perfil

`.ai-act/profile.yaml`: cliente y sector, finalidad, rol, datos personales, `classification` con su fecha, contactos de `escalation` y, si el proyecto ocupa varios repos, la lista de repos. Sin perfil, dilo, sugiere `/project-init` y termina aquí.

## 2. Reúne los hallazgos de cada repo

La línea base guarda el estado y la decisión; la norma, la fecha y el escalado de cada hallazgo los da la auditoría. Hacen falta las dos, unidas por el id.

Por cada repo (el actual, y los de la lista del perfil que estén clonados en esta máquina):

1. Lee `.ai-act/baseline.json`: por id, `status`, `justification`, `severity`, `title`, `evidence`, `first_seen` y `last_seen`.
2. Ejecuta la auditoría en modo consulta, que no escribe nada, y toma de cada hallazgo `norma`, `articulos`, `aplica`, `escalate` y `skill`:

   ```sh
   sh "${CLAUDE_PLUGIN_ROOT}/scripts/run.sh" audit.py scan --root RUTA_DEL_REPO
   ```

3. Une por id. Lo que sale en la auditoría y falta en la línea base va al grupo **nuevo sin registrar**. Lo que está en la línea base y ya no sale en la auditoría conserva los datos de la línea base.

Un repo de la lista que no esté al alcance, o que no tenga `.ai-act/`, figura en el resumen como **sin leer**, con su motivo.

Hecho cuando cada id de cada línea base leída está en un grupo y solo en uno: abierto, aceptado, mitigado, no detectado o nuevo sin registrar. Comprueba que los recuentos por grupo suman el total antes de escribir.

## 3. Escribe la página

En este orden. Con varios repos, cada hallazgo lleva delante el nombre de su repo y los recuentos se dan por repo y en total.

1. **Cabecera**: proyecto, sector, rol, clasificación AI Act con la fecha en que se revisó, fecha del resumen y repos leídos y sin leer.
2. **Abiertos, severidad alta**: uno por uno con la forma del aviso de abajo, en dos o tres líneas cada uno.
3. **Abiertos, severidad media**: tabla con hallazgo, evidencia, norma y skill que ayuda.
4. **Nuevos sin registrar**: lista, con la sugerencia de relanzar `/project-init` para que entren en la línea base.
5. **Aceptados**: tabla con hallazgo, justificación y desde cuándo. Un aceptado con la justificación vacía se señala: la decisión existe, pero falta su motivo.
6. **Mitigados** y **no detectados**: recuento y lista corta.
7. **Qué escalar y a quién**: los abiertos con `escalate`, agrupados por destinatario, con el contacto de `escalation` del perfil. Los hallazgos de categorías especiales van siempre al DPO.
8. **Qué aplica ya y qué después**: los hallazgos del AI Act ordenados por fecha, con `${CLAUDE_PLUGIN_ROOT}/knowledge/dates.yaml` y la fecha de hoy.
9. **Pendiente de decidir**: qué decisión falta en cada abierto y de quién es (PM, DPO, legal o el ingeniero).
10. **Pie**: base normativa de `knowledge/VERSION` y «No es asesoramiento legal».

Señala también una clasificación envejecida: `classification.reviewed` anterior al último hallazgo `scoring-model` o `llm-sdk` abierto, o el nivel `minimal` u `out-of-scope` junto a uno de esos hallazgos. La skill que la revisa es `ai-act-classify`.

## 4. Entrega y, si el PM quiere, guarda

Enseña la página en la conversación. Si el PM pide guardarla, escríbela en `.ai-act/risk-summary.md` del repo actual; en un proyecto de varios repos ese es el repo de gestión, donde vive el consolidado. Se sobrescribe en cada lanzamiento y el historial lo lleva git.

Si al leer el resumen el PM decide sobre un hallazgo, la decisión se registra en la línea base del repo al que pertenece: `status` a `aceptado` con su `justification`, o a `mitigado` cuando esté hecho. Relanzar la auditoría conserva ambos campos.

## Forma del aviso

Riesgo · Norma y artículo · Aplica ya o desde AAAA-MM-DD · Qué puede pasar · Opciones · A quién escalar · Base normativa de AAAA-MM-DD (de `knowledge/VERSION`) · No es asesoramiento legal.

## Límites

- La línea base guarda una justificación en texto libre, sin autor ni fecha de la decisión: quién aceptó y cuándo solo consta si alguien lo escribió ahí o en el historial de git.
- El plugin no tiene código que consolide varios repos, y el perfil de ejemplo no fija la clave de la lista: esta skill lee la que haya y recorre los repos uno a uno. Los que no están clonados quedan sin leer.
- El resumen refleja el código de hoy frente a la última línea base. Si la auditoría lleva tiempo sin relanzarse, el grupo de nuevos sin registrar crece: es la señal para relanzar `/project-init`.
