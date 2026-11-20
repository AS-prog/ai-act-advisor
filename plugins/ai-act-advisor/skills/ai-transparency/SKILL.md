---
name: ai-transparency
description: "Transparencia del art. 50 del AI Act: aviso de que se habla con una IA y marcado del contenido generado. Úsala cuando un aviso hable de un «SDK de LLM», cuando el proyecto tenga un chatbot, un asistente de voz o un agente que escribe o llama a personas, cuando genere texto, imagen, audio o vídeo que llega a personas, cuando haya un deepfake o un avatar de una persona real, o cuando pregunten «¿hay que avisar de que es IA?» o «¿hay que marcar el contenido?»."
---

# ai-transparency

Rol: DE y AE. Explica, propone y deja la decisión a quien trabaja.

**Carpeta del plugin**: en Claude Code, `${CLAUDE_PLUGIN_ROOT}` llega ya sustituido por una ruta. Si lo ves tal cual, el plugin se instaló con APM: usa en su lugar la primera de estas carpetas, en la raíz del repo, que tenga `knowledge/VERSION` dentro: `.claude/hooks/ai-act-advisor`, `.github/hooks/scripts/ai-act-advisor`, `.codex/hooks/ai-act-advisor`, `.cursor/hooks/ai-act-advisor`, `.gemini/hooks/ai-act-advisor` o `.windsurf/hooks/ai-act-advisor`. Haz lo mismo con `$CLAUDE_PROJECT_DIR`, que es la raíz del repo.

Referencia: `${CLAUDE_PLUGIN_ROOT}/knowledge/transparency-art50.md` (obligaciones por apartado, qué aviso vale, técnicas de marcado y qué queda fuera). Léela antes del paso 1.

## 1. Asigna cada uso del LLM a una rama

Parte de los hallazgos `llm-sdk` de `.ai-act/baseline.json` o del aviso del hook (uno por fichero) y lee cada fichero de evidencia: qué entra al modelo, qué sale y quién lo recibe.

- **Conversa**: la salida la lee o la oye una persona en un intercambio (chat, voz, avatar, agente que escribe correos o llama). Art. 50.1.
- **Genera contenido**: produce texto, imagen, audio o vídeo que llega a personas fuera del intercambio (informes, descripciones, creatividades, resúmenes). Art. 50.2, y 50.4 si es un deepfake o texto de interés público que se publica sin revisión editorial.
- **Máquina a máquina**: la salida es código, SQL, JSON, etiquetas, embeddings o un paso intermedio que consume otro proceso. Queda fuera del marcado.
- **Emociones o biometría**: infiere emociones o categoriza por rasgos biométricos. Art. 50.3, y antes la skill `ai-act-classify`.

Hecho cuando cada fichero de evidencia tiene rama. Un fichero puede tener dos.

## 2. Busca lo que ya hay

- **Conversa**: el aviso de IA en la interfaz, en el saludo del primer turno o en la plantilla del mensaje. Compáralo con las listas «vale» y «se queda corto» de la referencia. En un agente, mira además si dice en nombre de quién actúa.
- **Genera contenido**: marca de agua, metadatos de procedencia o registro de lo generado, y una forma de detectarlo. Si el marcado lo pone el modelo de un tercero, comprueba que sobrevive al pipeline (redimensionar, convertir o copiar el texto puede quitarlo).

Si la interfaz vive en otro repo, dilo y deja la comprobación como pregunta para quien la mantiene.

## 3. Fija quién responde y desde cuándo

- **Quién**: el 50.1 y el 50.2 obligan al proveedor del sistema; el 50.3 y el 50.4, al responsable del despliegue. Lee `project.role` del perfil. Si el rol está por confirmar, el aviso cubre los dos casos y la pregunta va al PM.
- **Desde cuándo**: fechas del art. 50 en `${CLAUDE_PLUGIN_ROOT}/knowledge/dates.yaml`, comparadas con hoy. Para el marcado del 50.2 hay dos: pregunta si el sistema ya estaba en servicio antes de la fecha general del art. 50; si lo estaba, vale la fecha de los sistemas anteriores (art. 111.4).

## 4. Da el aviso

Con la forma de abajo, un aviso por rama con obligación. Opciones habituales:

- **Conversa**: banner o etiqueta persistente; saludo en el primer turno («Soy un asistente de IA de…»); aviso sonoro en voz; en agentes, firma que diga que es una IA y en nombre de quién actúa. Añade recordatorios si el público es vulnerable o el tema es financiero, sanitario o jurídico.
- **Genera contenido**: metadatos de procedencia en el fichero; marca de agua del modelo o propia; registro de lo generado para poder detectarlo. La referencia pide marcado y detectabilidad a la vez: propone una opción de cada tipo.
- **Deepfake o texto de interés público**: etiqueta visible para las personas, además del marcado técnico; o revisión editorial humana con responsable, en el caso del texto.
- **Máquina a máquina**: sin obligación de marcado. Recomienda dejar escrito por qué (qué sale y quién lo consume) para que el hallazgo quede cerrado con su motivo.

Escalado: `escalation.pm` del perfil (es quien recibe los hallazgos `llm-sdk`). Añade `escalation.legal` si hay un deepfake, si el rol está en duda o si se quiere usar la excepción de «obvio para el usuario».

## 5. Registra la decisión

En `.ai-act/baseline.json`, sobre cada id `llm-sdk:…` (si falta en la línea base, `audit.py write` lo añade como `abierto`):

- `mitigado`, con `justification` que diga dónde está el aviso o el marcado (ruta o pantalla).
- `aceptado`, con `justification` que diga la rama y el motivo: «máquina a máquina: devuelve JSON a la tabla X», o la decisión del PM de asumirlo y hasta cuándo.

En los dos casos rellena `decided_by` (quién decide) y `decided_on` (la fecha del día, AAAA-MM-DD).

## Forma del aviso

Riesgo · Norma y artículo · Aplica ya o desde AAAA-MM-DD · Qué puede pasar · Opciones · A quién escalar · Base normativa de AAAA-MM-DD (de `knowledge/VERSION`) · No es asesoramiento legal.

**Cita de la norma.** Antes de escribir «Norma y artículo», trae el pasaje: `sh "${CLAUDE_PLUGIN_ROOT}/scripts/run.sh" buscar.py articulo <ai-act|rgpd|lopdgdd|omnibus> <ref>` (por ejemplo `articulo ai-act "anexo III 5.b"`), lee la línea que devuelve y cita como la skill `cite-regulation`: `AI Act anexo III 5.b · nota ai-act-anexo-iii (L51) · DOUE, CELEX …`. Si no sabes el artículo, usa `buscar.py citas` como explica esa skill. Si no hay nota que lo diga, escribe «sin nota que lo respalde» en lugar de citar de memoria.

## Límites

- La señal es el import o la dependencia de un SDK de LLM. El plugin no ve la interfaz ni comprueba que una marca de agua funcione: eso se revisa a mano.
- Las obligaciones de los modelos de uso general (arts. 51-55) son del proveedor del modelo, y quedan fuera de esta skill aunque el proyecto llame a su API.
- Los criterios de «vale» y «se queda corto» vienen de directrices no vinculantes de la Comisión; el aviso lo dice cuando se apoya en ellas.
