---
name: ai-act-classify
description: "Clasificación AI Act de un proyecto: práctica prohibida (art. 5), candidato a alto riesgo (anexo III según sector y finalidad), transparencia (art. 50), riesgo mínimo o fuera de alcance, y rol de proveedor o responsable del despliegue. Úsala cuando aparezca un modelo de scoring, propensión o decisión sobre personas, cuando un aviso hable de un «modelo que puntúa o clasifica», cuando cambie la finalidad o el sector, o cuando pregunten «¿esto es alto riesgo?» o «¿somos proveedor?»."
---

# ai-act-classify

Rol: PM, con el DE o AE que conoce el modelo. Propone una clasificación razonada y deja la decisión al PM; el perfil solo cambia cuando el PM la confirma.

Referencia: `${CLAUDE_PLUGIN_ROOT}/knowledge/ai-act-classification.md` (árbol, art. 5, anexo III, art. 6.3 y roles). Léela antes del paso 2.

## 1. Reúne los hechos

La clasificación depende de la **finalidad** prevista (art. 3.12), que está en las personas y en los documentos, y solo a medias en el código.

- `.ai-act/profile.yaml`: `client.sector`, `project.purpose`, `deliverable_infers`, `ai_type`, `role`, `eu_affected`, `personal_data` y la `classification` actual. Sin perfil, trabaja con lo que diga la conversación y sugiere `/project-init`.
- `.ai-act/baseline.json`: hallazgos `scoring-model` y `llm-sdk`, con su evidencia. Abre esos ficheros para ver qué predice el modelo, sobre quién y con qué variables.
- Pregunta al PM lo que falte, en una sola tanda: qué decisión se toma con la salida, sobre qué personas, quién la toma y con qué nombre o marca se entrega el sistema.

Hecho cuando puedes escribir en una frase qué infiere el sistema, sobre quién y para qué decisión.

## 2. Recorre el árbol

Sigue los seis pasos del árbol de la referencia, en orden. Para el paso 4:

- Busca el sector del perfil en `${CLAUDE_PLUGIN_ROOT}/knowledge/sectors.yaml` y lee los puntos del anexo III que sugiere. El sector orienta; la finalidad decide. Un cliente de energía con un modelo de selección de personal cae en el área 4.
- Lee las exclusiones expresas del punto (la detección de fraude queda fuera del 5.b).
- Revisa la excepción del art. 6.3 y, antes de proponerla, el perfilado: si el modelo perfila a personas físicas, es candidato a alto riesgo sin excepción.

Hecho cuando cada paso tiene su respuesta y el hecho del repo o del PM que la apoya, o queda marcado como «falta dato» con la pregunta que lo resolvería.

## 3. Fija el rol

Con la tabla de roles de la referencia: `provider`, `deployer` o `both`. En una consultora la respuesta suele estar en el contrato (quién pone el sistema en servicio y con qué marca). Si el contrato calla, la pregunta va a legal y el rol queda como «por confirmar».

## 4. Da el aviso

Con la forma de abajo. Las fechas salen de `${CLAUDE_PLUGIN_ROOT}/knowledge/dates.yaml`, comparadas con la fecha de hoy: «aplica ya» o «aplica desde AAAA-MM-DD». Según el nivel:

| Nivel | Qué dice el aviso | A quién escalar |
|---|---|---|
| `prohibited` | Letra del art. 5 y por qué encaja. Dilo con claridad: seguir, rediseñar o parar lo deciden el PM y legal | `escalation.legal` y `escalation.pm`, hoy |
| `high-risk-candidate` | Punto del anexo III, si cabe la excepción del 6.3, la fecha desde la que aplica y qué trae según el rol (lista corta de la referencia). Hasta esa fecha es preparación, no incumplimiento | `escalation.legal`; añade `escalation.dpo` si hay datos personales o perfilado |
| `transparency` | Que aplica el art. 50 y que el detalle lo da la skill `ai-transparency` | `escalation.pm` |
| `minimal` | Solo el art. 4 | Nadie |
| `out-of-scope` | Por qué queda fuera (no infiere, o exclusión del art. 2) y que siguen los avisos del RGPD | Nadie |

Opciones habituales para un candidato a alto riesgo: cambiar la finalidad o el uso de la salida para salir del punto, documentar la excepción del 6.3, o asumirlo y planificar las obligaciones antes de la fecha.

## 5. Confirma con el PM y actualiza el perfil

Enseña el nivel propuesto junto al actual y pregunta al PM si lo confirma.

- **Confirma**: escribe `classification.ai_act_level` y `classification.reviewed` (fecha de hoy) en `.ai-act/profile.yaml`, y `project.role` si cambió.
- **Sin confirmación** (duda, quiere consultar a legal, o quien trabaja es el DE o AE): el perfil queda como está y la propuesta se entrega por escrito para el PM.

## 6. Registra la decisión

En `.ai-act/baseline.json`, sobre el hallazgo `scoring-model` (si falta en la línea base, `audit.py write` lo añade como `abierto`):

- `aceptado`, con `justification` que diga el nivel, el punto del anexo III o el motivo de exclusión, y quién lo confirmó.
- `mitigado`, si se cambió la finalidad o el diseño para salir del punto; la justificación dice qué cambió.
- `abierto`, mientras la respuesta de legal esté pendiente.

## Forma del aviso

Riesgo · Norma y artículo · Aplica ya o desde AAAA-MM-DD · Qué puede pasar · Opciones · A quién escalar · Base normativa de AAAA-MM-DD (de `knowledge/VERSION`) · No es asesoramiento legal.

## Límites

- El perfil guarda un solo `ai_act_level`. Cuando un candidato a alto riesgo tiene además obligaciones del art. 50 (se acumulan, art. 50.6), se escribe el nivel más grave y la transparencia se menciona en el aviso y en la justificación.
- La auditoría señala un `scoring-model` cuando ve una librería de ML junto a términos de scoring; no sabe si se puntúa a personas. Los hooks del día a día no emiten este hallazgo: aparece al relanzar `/project-init`.
- Es una propuesta de clasificación para decidir con legal. Las directrices de la Comisión sobre el art. 6 siguen en borrador.
