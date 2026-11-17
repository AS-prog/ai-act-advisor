---
name: aesia-07-guia-de-datos-y-gobernanza-de-datos-14-anexos-parte-4
description: "AESIA: aesia 07 guia de datos y gobernanza de datos, sección «Anexos (parte 4)» (págs. 71-77). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-07-guia-de-datos-y-gobernanza-de-datos
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Anexos (parte 4)"
  paginas: 71-77
  origen: 2026-07-17-aesia-07-guia-de-datos-y-gobernanza-de-datos.pdf
  oficial: false
---
# Anexos (parte 4)

2.3 Entrenamiento
2.3.1 Datos de entrenamiento
Un enfoque aparentemente sencillo para la mitigación del sesgo es eliminar las características relevantes que podrían ser responsables del sesgo directamente. Para ilustrar eso, en un caso de uso que preselecciona automáticamente a los candidatos en función de la información del currículum, ejemplos de tales características son la raza, el género y la edad. Al mismo tiempo, las características que son relevantes para el caso de uso incluyen experiencia, habilidades, calificación, certificación y membresía profesional.
Si bien la eliminación de la raza, el género y la edad podría abordar el problema, otras características y variables indirectas podrían reflejar indirectamente sesgos. Por ejemplo, características como el saludo/prefijo (Sr./Sra.) o la ocupación pueden revelar el género.
Por lo tanto, eliminar solo las características asociadas con el sesgo puede no funcionar siempre.
Se pueden usar métodos basados en datos para mitigar el sesgo en los datos de entrenamiento. La reponderación de datos, por ejemplo, podría aumentar el peso de las muestras que se alinean con un objetivo. Tales técnicas incluyen:
-

Técnicas de muestreo para medir la representatividad de muestras de diferentes fuentes para evaluar el sesgo de selección.
- Muestreo de estratificación para superar un fenómeno de rareza. El muestreo
estratificado podría utilizarse aumentando la frecuencia relativa de los casos positivos en comparación con los negativos.
- Selección cuidadosa de las características en los casos en que las características de
la muestra tienen una fuerte correlación con el sesgo a excluir (por ejemplo, género o color).
Otro enfoque es averiguar la cantidad de sesgo presente en los datos y compensar el sesgo del resultado. Usando una serie de pasos, es posible averiguar la contribución de la característica y la importancia relativa de cada característica en la predicción del modelo.
Es posible compensar toda la influencia por una característica que causa el sesgo. El proceso de determinar la importancia relativa de las características puede incluir lo siguiente:
-

-

Proyección ortogonal iterativa de características. Dada la entrada y salida de un modelo de ML, el método busca producir una clasificación de entrada que corresponda a la dependencia del sistema de aprendizaje automático de cada entrada en su proceso de toma de decisiones y, por lo tanto, podría detectar sesgos que involucran ciertas características.
Redundancia mínima, relevancia máxima. La selección de características identifica subconjuntos de datos que son relevantes para los parámetros utilizados. Un esquema es seleccionar las características que se correlacionan más fuertemente con la variable de clasificación y al mismo tiempo están mutuamente distantes entre sí. Se ha descubierto que este esquema, denominado selección de redundancia mínima y relevancia máxima, es más potente que otros modos de selección de características.

70

-

-

Regresión Ridge/Regresión LASSO. LASSO y Ridge son métodos de regresión lineal con regularización para evitar el sobreajuste a los datos de entrenamiento. Estas técnicas también se utilizan para ayudar con la selección de características.
Random Forest. Random Forest es un enfoque que combina varios árboles de decisión aleatorios y agrega sus predicciones promediando. Esta técnica ha demostrado un excelente rendimiento en entornos donde el número de variables es mucho mayor que el número de observaciones.

2.3.2 Testeo
La evaluación del sesgo es una tarea difícil. Los métodos de agrupación y visualización de los datos de entrenamiento, las características derivadas o las predicciones resultantes pueden ayudar a detectar desequilibrios o posibles sesgos en los datos o el sistema de entrenamiento. En muchos casos, la preparación o conservación de un conjunto de datos equilibrado puede ocupar la mayor parte del tiempo de desarrollo en sistemas basados en el aprendizaje profundo. Tener equipos separados trabajando en la capacitación y la evaluación también podría evitar la influencia de los sesgos cognitivos individuales.
La investigación de defectos aparentes en el modelo podría revelar por qué no está maximizando la precisión general. La resolución de estos defectos podría mejorar la precisión general. Los conjuntos de datos sub representativos de ciertos grupos podrían necesitar datos de entrenamiento adicionales para mejorar la precisión en la toma de decisiones y reducir los resultados sesgados.
2.3.3 Ajuste
Se han creado algoritmos de mitigación de sesgos para lograr varios objetivos. Los algoritmos de mitigación de sesgo (también denominados a veces algoritmos justos) se pueden clasificar de la siguiente manera:
-

Métodos basados en datos, como el muestreo ascendente de poblaciones subrepresentadas o el uso de datos sintéticos.
- Métodos basados en modelos, como la adición de términos de regularización o
restricciones que imponen un objetivo durante la optimización, o el aprendizaje de la representación para ocultar o reducir el efecto de una variable específica.
- Métodos post-hoc, como identificar umbrales de decisión específicos del grupo
basados en resultados previstos para igualar las tasas de falsos positivos u otras métricas relevantes.
Ejemplos de algoritmos de mitigación de sesgo que se aplican son:
-

-

Removedor de impacto dispar: Una técnica de preprocesamiento que edita valores que se utilizarán como características de tal manera que se reduzcan los diferentes tratamientos entre los grupos;
Detector y eliminador de sesgo individual: Una técnica que crea un nuevo modelo de ML para individuos en el grupo desfavorecido que reciben una decisión diferente en comparación con individuos similares en el grupo favorecido. A veces puede aplicar diferentes umbrales para la clasificación positiva entre los grupos;

71

-

-

-

Clasificadores desacoplados: Una técnica para entrenar un clasificador separado en cada grupo. Los clasificadores separados podrían considerarse equivalentemente como un único clasificador que se ramifica en la función de grupo.
Función de pérdida articular: Una técnica para capturar la paridad de grupo mediante el uso de una función de pérdida conjunta que penaliza las diferencias en las estadísticas de clasificación entre grupos.
Aprendizaje por transferencia: Una técnica para mitigar los problemas de bajo volumen de datos para grupos donde hay una población de datos más pequeña.

2.4 Evaluación del sesgo
El sesgo en los sistemas de IA se mide de manera comparable a cómo se miden otras propiedades, como el rendimiento agregado. Sin embargo, es posible que las métricas de rendimiento agregadas en todo el conjunto de validación no indiquen si hay sesgo en el modelo. Las métricas generales en la matriz de confusión pueden parecer que funcionan bien en todo el conjunto. Sin embargo, calcular la precisión y el recuerdo en subconjuntos de categorías demográficamente importantes o ciertas a menudo puede revelar sesgos como una menor precisión para las mujeres que para los hombres, o una menor precisión para un grupo demográfico específico. Estas diferencias en el rendimiento probablemente indican que los sesgos no detectados están presentes en las primeras etapas del proceso de desarrollo. Por ejemplo, un determinado grupo podría estar infrarrepresentado en los datos de entrenamiento.
2.5 Métodos adversarios para mitigar el sesgo
Un método para mitigar el sesgo es incorporar una unidad adversarial en la arquitectura del modelo. En estos métodos, un "adversario" está prediciendo alguna propiedad o característica que define grupos hacia los cuales se desea la equidad. La salida del modelo para el cual se está mitigando el sesgo es la entrada al modelo adversarial. La actualización de peso para ese modelo se modifica para que, además de estar optimizada para la tarea que está realizando, también reduzca la cantidad de información que pone a disposición del adversario útil para su predicción. El efecto neto de este sistema es que el sistema aprende a realizar su tarea de manera ortogonal a las características para las cuales el sesgo no es deseado.
3. Verificación y validación
La verificación y validación de un modelo de ML recientemente desarrollado podría identificar y mitigar posibles sesgos antes de la implementación. Un conjunto de datos de retención obtenido de un origen de datos independiente de los datos de entrenamiento se utiliza normalmente en la comprobación y validación. Esta salvaguarda para la generalización del modelo también es importante para protegerse contra cualquier sesgo implícito en el conjunto de datos de entrenamiento. En general, cualquier paso tomado durante el procesamiento de conjuntos de datos y la capacitación de modelos sería beneficioso para aplicar a los datos y procedimientos de validación cuando corresponda.
Si bien la verificación de los sistemas de ML se lleva a cabo de forma intensiva utilizando conjuntos de datos de entrenamiento y prueba, se limita a la verificación de los resultados

72

basada en la selección y variación de los datos disponibles. Es posible que sea necesario evaluar un sistema de IA en un contexto específico.
Las pruebas de software tradicionalmente se basan en un "cuerpo de conocimiento utilizado como base para el diseño de pruebas y casos de prueba". El éxito de cualquier actividad de prueba empírica suele estar limitado por el grado en que los requisitos circundantes o los procesos de gestión de riesgos han identificado explícitamente posibles sesgos o fuentes de sesgo.
Las técnicas descritas en esta sección están destinadas a llevarse a cabo a una escala estadísticamente significativa. Las técnicas generalmente miden la sensibilidad del resultado a un subgrupo no incluido explícitamente en los datos de entrada.
Esta sección está destinada a aplicarse al desarrollo de nuevos sistemas, al despliegue de sistemas existentes y a la evaluación de si los sistemas mantienen la calidad a lo largo del tiempo. Un cambio en la relación entre los datos de entrada esperados y reales puede ser motivo de evaluación. La evaluación también puede incluir los resultados de la implementación en responsables del despliegue del sistema y espectadores (como personas u objetos que están presentes incidentalmente pero que no son el objetivo o el sujeto de una implementación del sistema de IA). Por ejemplo, un sistema que es injusto con respecto al género y la raza independientemente podría ser justo con una combinación específica de los dos.
3.1 Análisis estático de datos de entrenamiento y preparación de datos
El análisis de los datos de capacitación y entrada podría proporcionar información útil y detectar los tipos de sesgo de datos descritos en el Anexo C.1.
Los evaluadores pueden identificar el perfil de los datos de capacitación y entrada y validar si la propagación de una determinada variable representa el conjunto de datos real esperado. Un ejemplo de esto es identificar que los registros de un determinado grupo de edad se han utilizado para el entrenamiento, cuando se espera una distribución diferente de edades en conjuntos de datos reales. Esta actividad podría tener como objetivo validar el potencial de sesgo de selección, sesgo de muestreo y sesgo de cobertura, pero no puede hacerlo de manera exhaustiva, ya que está limitada por el conocimiento del evaluador.
Los evaluadores podrían identificar etapas en el proceso de preparación de datos que podrían introducir sesgos a través de "datos faltantes". Por ejemplo, si datos específicos no están disponibles de forma coherente en un conjunto de datos de entrada, los ingenieros pueden imputar esa información para los registros restantes o pueden eliminarla. Si la ausencia de ese elemento de datos se correlaciona con grupos específicos de registros, esto podría dar lugar a un sesgo que normalmente no se detectaría en las pruebas del modelo.
3.2 Muestras de controles de etiquetas
El riesgo de etiquetado incorrecto descrito en el Anexo C.1, es decir, etiquetadoras humanas que especifican incorrectamente las etiquetas para un conjunto de datos de

73

entrada que luego se utilizan para entrenar el modelo, podría evaluarse mediante controles de muestra de las etiquetas presentadas.
El etiquetado basado en la opinión de expertos podría ser más complicado de evaluar.
Puede ser necesario realizar revisiones doble ciego, o evaluar la evaluación de múltiples expertos, para evaluar la calidad de la etiqueta inicial.
3.3 Pruebas de validez interna
Las pruebas de validez interna evalúan la correlación entre los datos de entrada individuales y las salidas del sistema. Las pruebas de validez interna luego revisan si estas correlaciones son adversas en el contexto de requisitos específicos o criterios de aceptación.
Este proceso se basa en los datos que causan que se incluya un sesgo en el dominio de datos de entrada. Podría detectar sesgos en los modelos y su interacción.
Esto podría incluir la evaluación en un entorno totalmente integrado, con el fin de detectar cualquier sesgo en las actividades de recopilación o preparación de datos utilizadas durante el desarrollo del sistema de IA. La integración también puede detectar muestreos no representativos. Por ejemplo, los datos recopilados en un entorno integrado pueden tener características variables, como los niveles de iluminación o la frecuencia de actualización del sensor. Esas variaciones pueden influir en los datos de entrada al sistema de IA.
3.4 Pruebas de validez externas
Las pruebas de validez externas pueden implicar la reevaluación de observaciones previas utilizando fuentes de datos externas. Esta es una técnica útil porque puede detectar muchos tipos de sesgo que se han descrito en este documento, incluido el sesgo indirecto.
El aspecto de los datos de entrada al que se refiere el sesgo indirecto no está contenido explícitamente dentro de los datos de entrada, sino que es una derivación de segundo orden.
Por ejemplo, algunos informes de los medios de comunicación sobre el sesgo de la IA se han centrado en la investigación que correlaciona los resultados del modelo con los datos del censo o del código postal con los resultados para ilustrar la disparidad de los resultados.
Las pruebas de validez externas también pueden incluir la integración de nuevos datos de entrada y la validación de que los resultados son coherentes con las pruebas de validez internas.
Las pruebas de validez externa son particularmente importantes para los sesgos indirectos introducidos por variables proxy. Si un diseñador de modelos intenta mitigar el sesgo simplemente eliminando la información demográfica de la entrada, es probable que el sesgo siga existiendo a través de variables proxy. Por ejemplo, el modelo podría perpetuar el racismo "daltónico", un concepto sociológico que describe cómo las afirmaciones de no
"ver" el color de la piel de una persona impiden comprender y abordar la persistencia de la desigualdad racial en la sociedad. Para evitar este resultado, las pruebas de validez externas podrían necesitar incluir datos demográficos excluidos originalmente, o una

74

exploración de los efectos de la variable proxy. Una investigación más profunda podría ser necesaria para comprender por qué existen tales proxies y si el propósito puede cumplirse sin ellos. Las pruebas de validez externas también podrían necesitar incluir datos cualitativos que demuestren impactos dispares de la misma clasificación. Por ejemplo, si se utiliza un determinado modelo para identificar a las personas antes de abordar un avión, el daño emocional de un falso negativo podría ser mayor para aquellos grupos estereotipados como probables "terroristas" que para otros grupos.
En este contexto, podría ser necesario integrar conjuntos de datos de entrada con puntos de datos adicionales para evaluar adecuadamente el sesgo del sistema.
3.5 Pruebas de usuario
Las pruebas con diferentes tipos de usuarios finales pueden ser útiles cuando la interacción de un usuario con el sistema influye en los resultados y las predicciones de una manera correlacionada con la pertenencia del usuario a un grupo.
Evaluar la experiencia del usuario en escenarios del mundo real en un amplio espectro de usuarios, casos de uso y contextos de uso es una técnica útil para detectar sesgos en las interacciones del modelo, problemas de procesamiento de datos y problemas con las etiquetas de datos.
3.6 Pruebas exploratorias
Los desarrolladores de sistemas podrían organizar un grupo de probadores confiables y diversos que podrían probar adversariamente el sistema e incorporar una variedad de entradas potencialmente dañinas en pruebas unitarias o funcionales. Esto podría ayudar a descubrir formas imprevistas en que un sistema podría estar sesgado.
4. Despliegue
Una vez implementado, la capacitación y el soporte adecuados para el sistema de IA son importantes para que los responsables del despliegue permitan un uso efectivo del producto. Esto incluye orientación para los desarrolladores de sistemas sobre lo que constituye una implementación apropiada e inapropiada de un modelo dentro de un sistema de software. Por ejemplo, un sistema de seguimiento de la atención podría percibirse como injusto si se utiliza en un sistema educativo para monitorear el comportamiento de los estudiantes, pero ese podría no ser el caso si el mismo sistema se utiliza como herramienta de investigación en un experimento de psicología.
Los sistemas implementados también pueden incluir instrucciones para los usuarios finales del sistema. Por ejemplo, es deseable que los reclutadores que utilizan un sistema de recomendación de contratación comprendan las capacidades y limitaciones del sistema.
Es posible que tanto los desarrolladores de sistemas como los usuarios finales de software deban ser conscientes de las áreas conocidas de sesgo. Esto se puede lograr a través de una herramienta de transparencia, que contiene información sobre los datos en los que se entrenó el modelo, distribuciones para poblaciones de sus errores falsos positivos y falsos negativos, y otra información asociada.
Los interesados, las personas a las que se refieren los datos de entrenamiento, no son necesariamente responsables del despliegue del sistema. No necesitan ser entrenados,

75

pero es posible que necesiten ser informados de cualquier sesgo dentro del sistema que pueda afectarlos, en un lenguaje apropiado para el contexto. Los fallos en la capacitación o el soporte pueden dar lugar a sesgos adicionales que pueden ser difíciles de detectar antes.
4.1 Validación continua
Los modelos pueden degradarse y perder rendimiento con el tiempo. La degradación del rendimiento puede atribuirse a los cambios en el entorno, los nuevos comportamientos emergentes, los cambios en la composición de la población de insumos y los cambios en los requisitos. Además, un sistema podría estar sesgado hacia una posición histórica.
Es posible que sea necesario supervisar el rendimiento continuo cuando se implemente el sistema. Esto incluye verificar el rendimiento del sistema, especialmente los resultados atípicos, tanto manualmente como utilizando diferentes métricas y técnicas para evaluar el sesgo y la equidad. Si hay indicios de sesgo, es posible que sea necesario volver a entrenar o rediseñar el sistema.
El monitoreo es un proceso conocido en muchas industrias que aprovechan la toma de decisiones automatizada en sus procesos. Por ejemplo, en la banca, se están desarrollando e introduciendo modelos de cuadros de mando junto con sus procesos de monitoreo aprobados. Los procesos de monitoreo no solo podrían aplicarse a la precisión y rendimiento de modelos/sistemas, pero también podría utilizarse para la identificación y el seguimiento de sesgos en sistemas o modelos.

76
