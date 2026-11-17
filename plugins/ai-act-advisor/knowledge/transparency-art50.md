# Transparencia (art. 50): referencia

Referencia de la skill `ai-transparency`. Contrastada el 2026-11-17 con el consolidado en español del Reglamento (CELEX 02024R1689-20260727). Las fechas de aplicación viven en `dates.yaml`. Los criterios con «párr.» vienen de las Directrices de la Comisión sobre el art. 50, Comunicación C(2026) 7702 final, de 5-11-2026 (su contenido se aprobó el 20-07-2026 como C(2026) 5054, con la misma numeración de párrafos). No son vinculantes (párr. 5). Multa: hasta 15 M EUR o el 3 % del volumen de negocios (art. 99.4.g).

## Obligaciones por apartado

| Apdo. | Obligado | Obligación | Excepciones |
|---|---|---|---|
| 50.1 | Proveedor | Sistemas que interactúan directamente con personas (chatbots, agentes, avatares, asistentes de voz): la persona debe saber que habla con una IA | Cuando resulte evidente para una persona razonablemente informada, atenta y perspicaz; se interpreta de forma restrictiva (párr. 45) y teniendo en cuenta a los grupos vulnerables del público previsible |
| 50.2 | Proveedor | Contenido sintético de audio, imagen, vídeo o texto: marcado legible por máquina **y** detectable como generado o manipulado | Función de apoyo a la edición estándar; sistemas que no alteran sustancialmente los datos de entrada ni su semántica |
| 50.3 | Responsable del despliegue | Reconocimiento de emociones o categorización biométrica: informar a las personas expuestas | — |
| 50.4 | Responsable del despliegue | Ultrafalsificaciones (deepfakes): hacer público que el contenido se ha generado o manipulado de manera artificial. Texto publicado para informar al público sobre asuntos de interés público: revelarlo | Obras manifiestamente creativas, satíricas, artísticas o de ficción (basta con hacer pública la existencia del contenido generado, sin dificultar el disfrute de la obra). Texto sometido a revisión humana o control editorial, con un responsable editorial |
| 50.5 | Ambos | Información clara y distinguible, a más tardar con ocasión de la primera interacción o exposición, y accesible | — |

La tabla deja fuera la excepción de uso policial autorizado por ley, que tienen los apartados 1 a 4.

El art. 50.2 tiene dos fechas en `dates.yaml`: la general y la de los sistemas generativos comercializados antes de la fecha general (art. 111.4). El contenido generado antes de la fecha general no necesita etiquetado retroactivo (FAQ de la Comisión sobre el art. 50).

## Aviso de IA (50.1)

- **Vale** (párr. 37): etiqueta o banner, saludo en el primer turno, aviso sonoro en voz, icono persistente o el símbolo «AI».
- **Se queda corto** (párr. 38): información solo en las condiciones generales, en una URL o en la documentación; marcas legibles por máquina que el usuario no percibe; referencias genéricas al «asistente»; divulgaciones generales como «Los servicios en este sitio web utilizan la IA»; descripciones técnicas como «este sistema utiliza grandes modelos de lenguaje».
- **Agentes** (párr. 31): revelan su naturaleza y en nombre de quién actúan en cada interacción nueva y en los pasos clave. Incluye los que envían correos o llaman a terceros.
- **Recordatorios** (párr. 40): una notificación destacada antes de la primera interacción suele bastar; hacen falta recordatorios periódicos con personas vulnerables, en asesoramiento financiero, de seguros, jurídico o sanitario, con acompañantes de IA y para mantener el control sobre lo que hace un agente.
- **Fuera**: respuestas automáticas basadas en reglas, como un mensaje de ausencia (párr. 30).

## Marcado del contenido (50.2)

- Hacen falta las dos cosas: marcado legible por máquina y detectabilidad (párr. 69-70).
- **Técnicas** (párr. 72-73): marca de agua, metadatos (C2PA, IPTC), procedencia criptográfica, registro y huellas. Se combinan en capas.
- El marcado puede hacerse en el modelo, en la inferencia o a posteriori. El proveedor del sistema responde aunque use la solución de un tercero (párr. 74).
- **Fuera del marcado** (párr. 64-68): salidas muy cortas (palabras sueltas, pies de foto, texto alternativo, etiquetas de interfaz); código fuente, SQL, JSON, YAML, esquemas y API; salidas máquina a máquina; recomendadores que solo seleccionan u ordenan contenido existente; salidas intermedias de un circuito cerrado de producción.
- **Edición estándar** (párr. 90-92): corrección gramatical, formato, traducción, transcripción y reducción de ruido están exentas. Se marcan los resúmenes generados, las reescrituras que cambian el sentido y la inserción o eliminación de personas u objetos en imágenes.
- El Código de buenas prácticas sobre transparencia del contenido generado por IA (versión final de 10-06-2026) sirve para demostrar el cumplimiento, y hay iconos de la UE para etiquetar.

## Ultrafalsificaciones y texto de interés público (50.4)

El Reglamento llama «ultrafalsificación» a lo que en el oficio se conoce como deepfake (art. 3.60).

- Una ultrafalsificación cumple cuatro criterios acumulativos (párr. 113): semejanza apreciable; con personas, objetos, lugares, entidades o sucesos; existentes; y que puede inducir a una persona a pensar erróneamente que son auténticos o verídicos. La intención de engañar es indiferente (párr. 114). Un avatar realista de una persona real lo es.
- El responsable del despliegue pone una etiqueta perceptible por personas; el marcado técnico del proveedor se suma a ella, sin sustituirla (párr. 117).
- La publicación automática de textos de interés público generados sin revisión editorial entra en el 50.4.

## Emociones y biometría (50.3)

Aviso a todas las personas expuestas, también menores, en la primera exposición (párr. 99-108). Si el uso es en el trabajo o en un centro educativo, primero pasa por `ai-act-classify`: puede ser una práctica del art. 5.1.f.
