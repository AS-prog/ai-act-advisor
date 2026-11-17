# Transparencia (art. 50): referencia

Referencia de la skill `ai-transparency`. Sale de `docs/investigacion/ai-act-investigacion.md` (sección 9). Las fechas de aplicación viven en `dates.yaml`. Los criterios con «párr.» vienen de las directrices de la Comisión sobre el art. 50, C(2026) 5054, que no son vinculantes. Multa: hasta 15 M EUR o el 3 % del volumen de negocios (art. 99.4).

## Obligaciones por apartado

| Apdo. | Obligado | Obligación | Excepciones |
|---|---|---|---|
| 50.1 | Proveedor | Sistemas que interactúan directamente con personas (chatbots, agentes, avatares, asistentes de voz): la persona debe saber que habla con una IA | Cuando sea obvio para una persona razonablemente informada; se interpreta de forma restrictiva y no vale si hay grupos vulnerables (párr. 42-45) |
| 50.2 | Proveedor | Contenido sintético de audio, imagen, vídeo o texto: marcado legible por máquina **y** detectable como generado o manipulado | Asistencia a la edición estándar; sistemas que no alteran sustancialmente la entrada ni su sentido |
| 50.3 | Responsable del despliegue | Reconocimiento de emociones o categorización biométrica: informar a las personas expuestas | — |
| 50.4 | Responsable del despliegue | Deepfakes: revelar que el contenido es artificial. Texto publicado para informar al público sobre asuntos de interés público: revelarlo | Obras evidentemente artísticas, satíricas o de ficción (revelación atenuada). Texto con revisión humana y responsabilidad editorial |
| 50.5 | Ambos | Información clara y distinguible, como muy tarde en la primera interacción o exposición, y accesible | — |

El art. 50.2 tiene dos fechas en `dates.yaml`: la general y la de los sistemas generativos comercializados antes de la fecha general (art. 111.4). El contenido generado antes de la fecha general no necesita etiquetado retroactivo (FAQ de la Comisión sobre el art. 50).

## Aviso de IA (50.1)

- **Vale** (párr. 37): etiqueta o banner, saludo en el primer turno, aviso sonoro en voz, icono persistente o el símbolo «AI».
- **Se queda corto** (párr. 38): solo en los términos y condiciones o en una URL, marcas que no se perciben, etiquetas vagas como «asistente», frases genéricas como «este sitio usa IA» o «este sistema usa LLM».
- **Agentes** (párr. 31): revelan su naturaleza y en nombre de quién actúan en cada interacción nueva y en los pasos clave. Incluye los que envían correos o llaman a terceros.
- **Recordatorios** (párr. 40): periódicos con personas vulnerables, en asesoramiento financiero, sanitario o jurídico y en *AI companions*, y siempre que el usuario pregunte.
- **Fuera**: respuestas automáticas basadas en reglas, como un mensaje de ausencia (párr. 30).

## Marcado del contenido (50.2)

- Hacen falta las dos cosas: marcado legible por máquina y detectabilidad (párr. 69-70).
- **Técnicas** (párr. 72-73): marca de agua, metadatos (C2PA, IPTC), procedencia criptográfica, registro y huellas. Se combinan en capas.
- El marcado puede hacerse en el modelo, en la inferencia o a posteriori. El proveedor del sistema responde aunque use la solución de un tercero (párr. 74).
- **Fuera del marcado** (párr. 64-68): salidas muy cortas (palabras sueltas, pies de foto, texto alternativo, etiquetas de interfaz); código fuente, SQL, JSON, YAML, esquemas y API; salidas máquina a máquina; recomendadores que solo ordenan contenido existente; salidas intermedias de un circuito cerrado de producción.
- **Edición estándar** (párr. 90-92): corrección gramatical, formato, traducción, transcripción y reducción de ruido están exentas. Se marcan los resúmenes generados, las reescrituras que cambian el sentido y la inserción o eliminación de personas u objetos en imágenes.
- El Código de buenas prácticas sobre transparencia del contenido generado por IA (versión final de 10-06-2026) sirve para demostrar el cumplimiento, y hay iconos de la UE para etiquetar.

## Deepfakes y texto de interés público (50.4)

- Un deepfake cumple tres criterios (párr. 113-117): semejanza apreciable con algo existente, existencia plausible y apariencia falsa de autenticidad. La intención de engañar es indiferente. Un avatar realista de una persona real lo es.
- El responsable del despliegue pone una etiqueta perceptible por personas; el marcado técnico del proveedor se suma a ella, sin sustituirla.
- La publicación automática de textos de interés público generados sin revisión editorial entra en el 50.4.

## Emociones y biometría (50.3)

Aviso a todas las personas expuestas, también menores, en la primera exposición (párr. 99-108). Si el uso es en el trabajo o en un centro educativo, primero pasa por `ai-act-classify`: puede ser una práctica del art. 5.1.f.
