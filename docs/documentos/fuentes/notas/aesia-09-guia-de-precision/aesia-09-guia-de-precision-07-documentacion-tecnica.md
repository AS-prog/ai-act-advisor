---
name: aesia-09-guia-de-precision-07-documentacion-tecnica
description: "AESIA: aesia 09 guia de precision, sección «Documentación técnica» (págs. 33-37). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-09-guia-de-precision
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Documentación técnica"
  paginas: 33-37
  origen: 2026-07-17-aesia-09-guia-de-precision.pdf
  oficial: false
---
# Documentación técnica

5. Documentación técnica
En la guía de documentación técnica que se proporciona dentro del marco del sandbox de
IA, se indica de manera detallada y acorde al Reglamento Europeo de IA, la estructura y el contenido de la documentación técnica de sistema de IA de alto riesgo. En este apartado vamos a entrar en detalle en aspectos específicos de como documentar el proceso de selección y aseguramiento de la precisión que se ha detallado en esta guía.
El Reglamento Europeo de IA establece que no solo la definición y selección de métricas de precisión es relevante, si no también elevar su alcance al responsable del despliegue del sistema en las instrucciones pertinentes. Así, refleja en el párrafo 2 y 3 de su artículo 15 sobre precisión, solidez y ciberseguridad:

AI Act
Art.15.2 y 3 – Precisión, solidez y ciberseguridad
2. Para abordar los aspectos técnicos sobre la forma de medir los niveles adecuados de precisión y solidez establecidos en el apartado 1 y cualquier otro parámetro de rendimiento pertinente, la Comisión, en cooperación con las partes interesadas y organizaciones pertinentes, como las autoridades de metrología y de evaluación comparativa, fomentará, según proceda, el desarrollo de parámetros de referencia y metodologías de medición.
3. En las instrucciones de uso que acompañen a los sistemas de IA de alto riesgo se indicarán los niveles de precisión de dichos sistemas, así como los parámetros pertinentes para medirla.

Las instrucciones sobre cómo se propone obtener la precisión, cómo reportarla (guía de transparencia), cómo interpretar y usar sus umbrales y métricas asociadas a ella se podrían documentar en los apartados específicos detallados en la guía de documentación técnica acorde a la selección y valoración de estas, tal y como se ha detallado en los apartados anteriores y en el anexo 7.1.
En el anexo IV de la documentación técnica mínima requerida para los sistemas de IA de alto riesgo, encontramos algunos puntos referentes a la precisión del sistema:
-

Punto 2(g): “Los procedimientos de validación y prueba utilizados, incluida la información acerca de los datos de validación y prueba empleados y sus características principales; los parámetros utilizados para medir la precisión, la solidez y el cumplimiento de otros requisitos pertinentes establecidos en el capítulo III, sección 2, así como los efectos potencialmente discriminatorios; los archivos de registro de las pruebas y todos los informes de las pruebas fechados y firmados por las personas responsables…”

32

Este punto es el núcleo documental sobre la documentación de la precisión, porque obliga a describir cómo se mide, con qué datos, bajo qué condiciones y con qué métricas. Se recomienda documentar el diseño de las pruebas, los conjuntos de validación, las fórmulas o indicadores de precisión (referirse al anexo 7.1), los resultados obtenidos y las evidencias que los respalden.
-

Punto 3: “Información detallada acerca de la supervisión, el funcionamiento y el control del sistema de IA, en particular con respecto a sus capacidades y limitaciones de funcionamiento, incluidos los niveles de precisión para las personas o colectivos de personas específicos en relación con los que está previsto que se utilice el sistema y el nivel general de precisión esperado en relación con su finalidad prevista…”

Este apartado exige declarar el nivel de precisión alcanzado y esperado del sistema en condiciones reales de uso, diferenciando por grupos o contextos cuando sea relevante. Se debe documentar la metodología para medir esa precisión operativa, las limitaciones conocidas, los márgenes de error y la justificación de que el rendimiento es adecuado para la finalidad prevista.
-

Punto 4: “Una descripción de la idoneidad de los parámetros de rendimiento para el sistema de IA concreto.”

Aquí se recomienda justificar que las métricas o indicadores empleados para medir la precisión son adecuados y representativos del uso previsto del sistema, así como, documentar por qué se eligieron esos parámetros, su relevancia técnica y cómo reflejan correctamente el rendimiento real o esperado del modelo.
-

Punto 9: “Descripción detallada del sistema establecido para evaluar el funcionamiento del sistema de IA en la fase posterior a la comercialización, incluido el plan de vigilancia poscomercialización…”

Este punto vincula la precisión con su seguimiento continuo tras la comercialización. Se recomienda mantener un procedimiento documentado para monitorizar la evolución del rendimiento (incluida la precisión) a lo largo del tiempo, registrar degradaciones o desviaciones y establecer acciones correctivas.
El proveedor puede facilitar en la documentación dos elementos descriptivos relevantes: La tarjeta del modelo y la tarjeta descriptiva de la base de datos empleada.

5.1 Tarjeta del Modelo
A modo de ejemplo, y sin que sea vinculante, una tarjeta del modelo(s) usados por el sistema, con sus métricas de precisión, solidez, capacidades operativas, limitaciones y sus relaciones en torno a cambios en la precisión y solidez del sistema. Este apartado está en relación con lo descrito en la guía de Documentación Técnica, pues se recomienda que se incorpore a dicha documentación.
Las tarjetas de modelo (Model Cards) pueden incluir secciones especificando:
-
-

Tamaño del modelo, incluyendo el número de parámetros en las configuraciones clave.
Fecha de publicación.
33

-
-
-
-
-
-

Tipo de modelo, indicando si ha sido desarrollado desde cero o si se ha utilizado un modelo de base.
Finalidad prevista.
Términos de identidad, con referencia a grupos frecuentemente vulnerables o afectados, como los centrados en la orientación sexual, género y raza.
Artículos y referencias clave, en caso de que existan.
Detalles del uso del modelo en entrenamiento, validación y evaluación, junto con información sobre rendimiento, eficiencia y limitaciones.
Implicaciones de mayor alcance y consideraciones éticas, riesgos y recomendaciones
[50].

En particular, las tarjetas de modelo pueden incluir, con respecto a las métricas de precisión
(performance) o calidad de este, respuesta a las siguientes preguntas en un apartado específico para las métricas, que midan e ilustren los errores de precisión del modelo desproporcionadas entre subgrupos
-

-

-

-

-

-

-

Medidas de precisión del modelo: ¿Qué métricas se reportan y por qué fueron seleccionadas? Pueden especificarse todas las métricas que reflejen el potencial impacto real del modelo, incluyendo medidas de precisión y otras métricas relacionadas con el rendimiento (performance).
Umbrales de decisión: Si se usan, ¿por qué se seleccionaron esos valores específicos?
En las tarjetas de modelo en formato digital, se recomienda incluir una barra deslizante interactiva para mostrar las métricas de precisión en función de distintos umbrales de decisión.
Enfoques hacia la incertidumbre y variabilidad: ¿Cómo se calculan las medidas de incertidumbre y estimaciones de estas métricas? Esto podría incluir desviación estándar, varianza, intervalos de confianza o divergencia KL.
Métodos de cálculo y origen de los valores: Detalles sobre cómo se obtienen los valores de estas métricas se recomienda que estén incluidos (por ejemplo, media de cinco ejecuciones, validación cruzada de 10 iteraciones o pliegues, etc.).
Interpretabilidad del modelo: ¿Qué métodos o herramientas se han implementado para facilitar la comprensión del modelo y sus predicciones? (Por ejemplo, SHAP, LIME, o visualizaciones de importancia de características).
Adaptabilidad del modelo: Información sobre la capacidad del modelo para adaptarse a nuevos datos o condiciones, incluyendo detalles sobre procesos de fine-tuning o actualización periódica.
Uso responsable: Advertencias o limitaciones del modelo en términos de su aplicación para evitar malentendidos o uso indebido. Esto podría incluir advertencias sobre aplicaciones sensibles o contextos inapropiados, y cómo estos podrían impactar negativamente en los resultados.

Las tarjetas de modelos constituyen una herramienta de transparencia, importantes también en relación con la solidez (ver guía de solidez correspondiente) y documentación técnica, favoreciendo la auditoría técnica y no técnica por los analistas, así como mecanismos de retroalimentación por el responsable del despliegue más inclusivos.

34

Sin embargo, hasta que su estandardización o formalización no se lleve a cabo de forma que evite representaciones de resultados engañosos o confusos, la utilidad y precisión de las tarjetas de modelo se basan en la integridad del creador de la misma tarjeta [50].

Ejemplo - Detección de denuncias falsas
Para cumplimentar la tarjeta del modelo, siguiendo las directrices establecidas en esta guía, el proveedor del sistema de IA proporciona en dicha tarjeta la entre otras cuestiones, la información siguiente:
- Se indica que se ha seleccionado área bajo la curva ROC como métrica de precisión y a
ésta se le ha complementado con la información de la matriz de confusión del sistema, como hemos indicado, entendido el sistema de IA como una clasificación binaria.
- Dado que el sistema de IA realiza un procesamiento del texto de las denuncias, también
se ha considerado la perplejidad como métrica de precisión. En la ficha del modelo se detalla cómo durante el entrenamiento y prueba se ha analizado los resultados de perplejidad.
- Para gestionar la incertidumbre y la variabilidad, añade información a la tarjeta del
modelo, del procedimiento seguido. Se han realizado divisiones de los datos de validación aleatorias, y por conjuntos específicos de origen, para estudiar cómo se comportan las métricas de precisión en los diferentes conjuntos.
Nota: El proveedor, ha completado la información de la tarjeta del modelo añadiendo los campos que se han indicado en la guía, y en este ejemplo hemos indicado aquellos de mayor relevancia y en consonancia con el tratamiento de este caso de uso desarrollado a lo largo de la guía.

5.2 Tarjeta de base de datos
Las tarjetas de bases de datos (Datasheets for datasets) [10] son aconsejables para dar visión más holística de las métricas de precisión provistas y de la proveniencia de los datos usados para el entrenamiento del modelo. Si ésta cambia con el uso del modelo, se recomienda que las tarjetas del modelo también se actualicen.
Pueden estudiarse metodologías de documentación asociadas a la transparencia como las mencionadas, entre otras adecuadas a venir potencialmente en el futuro, para dar una visión más amplia a las métricas de precisión y visualizar, si las hubiese, posibles disparidades interseccionales, por ejemplo, en la precisión en la tarea realizada por el modelo.
Se puede consultar un ejemplo de disparidad interseccional para la precisión (accuracy) en clasificación comercial de género está disponible en [17], y un ejemplo de tarjeta de modelo se puede ver en https://github.com/openai/whisper/blob/main/model-card.md.
El proveedor podrá atender a taxonomías de imparcialidad y sesgo para elegir aquellas métricas que complementen y enriquezcan la noción de precisión provista por el sistema en la finalidad prevista del sistema.

35

Se recomienda que el proveedor documente las pruebas hechas para posibles tipos de sesgos que pueda sufrir el sistema afectando a la precisión para categorías de datos que puedan resultar ser discriminadas. Del mismo modo, se podría documentar cómo las mismas métricas provistas, a nivel global de modelos, no presentan impacto desigual o disparatado (disparate impact) para diferentes grupos pertenecientes a variables sensibles. Para éstas, la salida del modelo debe ser imparcial y no discriminar (ver guía de datos).

36
