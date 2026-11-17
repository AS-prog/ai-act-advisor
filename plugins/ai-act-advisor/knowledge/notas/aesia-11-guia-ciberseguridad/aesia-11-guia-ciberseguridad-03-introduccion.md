---
name: aesia-11-guia-ciberseguridad-03-introduccion
description: "AESIA: aesia 11 guia ciberseguridad, sección «Introducción» (págs. 12-16). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-11-guia-ciberseguridad
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Introducción"
  paginas: 12-16
  origen: 2026-07-17-aesia-11-guia-ciberseguridad.pdf
  oficial: false
---
# Introducción

Envenenamiento de datos: Consiste en la introducción de datos maliciosos o manipulados en el conjunto de datos de entrenamiento. El objetivo es alterar el aprendizaje del modelo para que genere resultados controlados o insertar puertas traseras que puedan ser explotadas posteriormente.
Aunque sus efectos suelen manifestarse durante la fase de inferencia, el ataque ocurre principalmente en la fase de desarrollo y entrenamiento del sistema.
○ Envenenamiento de modelos: a diferencia del envenenamiento de datos, en este caso el ataque manipula directamente el modelo de IA en sí, generalmente durante su actualización o en entornos de aprendizaje federado. En estos escenarios, el modelo se entrena de manera distribuida en múltiples dispositivos o entidades, lo que aumenta el riesgo de manipulación. El atacante puede modificar los parámetros del modelo o insertar comportamientos maliciosos que comprometan su funcionamiento sin necesidad de actuar sobre los datos de entrenamiento.
Ataques de evasión: En este tipo de ataque, el adversario intenta que el sistema de inteligencia artificial haga predicciones incorrectas, ya sea de manera global o en casos específicos. Estos ataques se producen en la fase de inferencia, cuando el sistema ya está en producción, por lo que es esencial que el sistema cuente con mecanismos de seguridad para detectarlos. Las contramedidas se recomiendan que se diseñen durante las etapas de diseño y entrenamiento para maximizar la resiliencia del sistema ante estos ataques.
Ataques de inversión: La privacidad es el principal riesgo en este tipo de ataques, pero combinados con otros tipos de ataques (por ejemplo, de extracción) tienen efectos devastadores. El objetivo del atacante es obtener conocimiento de los datos de entrenamiento del modelo. Al igual que otros ataques, se produce en fase de inferencia con el sistema de IA en producción, pero el sistema podrá ser diseñado y entrenado con el objetivo de resistirlos en la mayor medida posible.
Ataques de extracción: Estos ataques intentan obtener información sobre el modelo, con el objetivo de replicar o entrenar un modelo similar. La forma más común es a través de interacciones con el sistema, aunque también pueden implicar mecanismos laterales, como el robo del modelo o la extracción de información a partir de sus respuestas. Los ataques de extracción pueden facilitar ataques de transferencia, en los que, una vez conocido el modelo, es posible aplicar otros tipos de ataques (evasión, inversión) al sistema de IA de alto riesgo atacado. Al igual que otros ataques, estos ocurren en la fase de inferencia con el sistema de IA en producción, pero el sistema se recomienda que se diseñe y entrene para resistirlos en la mayor medida posible.
Ataques de canal lateral: Este tipo de ataque busca obtener información del sistema de IA a través de características físicas observables durante su funcionamiento, como patrones de consumo energético, tiempos de respuesta o emisiones electromagnéticas. A diferencia de los ataques directos sobre el modelo o los datos, estos ataques aprovechan vulnerabilidades en la implementación física o el hardware donde se ejecuta el sistema. Los ataques de canal lateral pueden ocurrir tanto en fase de inferencia con el sistema en producción como durante el
○

-

-

-

-

11

-

entrenamiento, y pueden facilitar otros tipos de ataques al revelar información sobre la arquitectura o los parámetros del modelo. Es fundamental implementar contramedidas específicas a nivel de hardware y software para minimizar las fugas de información a través de estos canales.
Ataques a la cadena de suministro: Estos ataques se centran en comprometer la integridad del sistema de IA a través de vulnerabilidades en su cadena de suministro, desde el desarrollo hasta el despliegue. El atacante puede introducir componentes maliciosos o manipulados en cualquier punto del ciclo de vida del sistema, incluyendo:
○ Componentes de software: La introducción de dependencias comprometidas, bibliotecas maliciosas o código vulnerable en el proceso de desarrollo puede crear puertas traseras o vulnerabilidades explotables una vez que el sistema está en producción. Esto es especialmente crítico en sistemas que dependen de múltiples componentes de código abierto o de terceros.
○ Infraestructura y hardware: La manipulación de los componentes físicos o la infraestructura de computación puede permitir ataques persistentes que son difíciles de detectar y mitigar.
Estos ataques pueden afectar tanto a la fase de entrenamiento como a la de inferencia, y requieren una rigurosa verificación y validación de todos los elementos de la cadena de suministro.

-

Ataques de Denegación de Servicio (DoS): Este tipo de ataque busca interrumpir o degradar el funcionamiento normal del sistema de IA, sobrecargando sus recursos computacionales o saturando sus capacidades de procesamiento. A diferencia de los DoS tradicionales que se centran en la infraestructura de red, los ataques DoS específicos para IA pueden explotar características únicas de estos sistemas:
○ Sobrecarga computacional: Consiste en generar consultas específicamente diseñadas para maximizar el consumo de recursos del modelo, por ejemplo, mediante entradas que requieren cálculos especialmente intensivos o que activan los peores casos de rendimiento del sistema. Estos ataques son particularmente efectivos en sistemas de IA que operan en tiempo real o tienen requisitos estrictos de latencia.
○ Ataques de agotamiento de otros recursos: Se centran en explotar limitaciones en los recursos empleados por el sistema inteligente para poder desarrollar la tarea encomendada. Por ejemplo, el sistema puede generar un número masivo de ficheros que comprometan el funcionamiento del sistema operativo. Al igual que otros ataques, ocurren principalmente en fase de inferencia con el sistema en producción, pero requieren consideraciones especiales durante el diseño y desarrollo para implementar mecanismos de protección efectivos.

El acceso de terceros no autorizados a los activos presentes en la cadena de valor de un sistema de inteligencia de alto riesgo, sin ser una vulnerabilidad directamente relacionada

12

con la IA, sí supone un amplio vector de ataque para cualquiera de los ataques anteriormente mencionados, con el riesgo de escalar los ataques de caja negra donde el atacante no tiene conocimiento del sistema a caja blanca o gris donde hay un conocimiento parcial o incluso total. En esta guía se presenta en un Anexo, la relación entre las políticas de acceso y los sistemas de inteligencia artificial de alto riesgo.
Otro concepto fundamental de ciberseguridad de la IA son los bucles de retroalimentación, particularmente importantes en sistemas de entrenamiento continuo.
que continúan aprendiendo después de su despliegue. Estos bucles pueden resultar en la amplificación de sesgos o en un comportamiento no deseado del sistema si los resultados de salida influyen en los datos de entrada de futuras operaciones.
Se suele decir que “una cadena es tan fuerte como su eslabón más débil”, y esto es especialmente relevante en el contexto de la ciberseguridad. La formación es una herramienta muy potente dentro de una organización para establecer eslabones sólidos.
Se aborda en la guía de manera resumida, en otro Anexo dedicado a ello, aspectos relativos a cómo pueden las organizaciones (de proveedor y de responsable del despliegue) formar a sus equipos en el ámbito de la ciberseguridad orientada a inteligencia artificial. Esto permite tener una distribución a lo largo de la organización de los conceptos y riesgos inherentes en materia de ciberseguridad para los sistemas de inteligencia artificial de alto riesgo.

Imagen 1. Esquema de las principales amenazas dentro de la ciberseguridad para sistemas inteligentes relacionando su momento de aparición con el ciclo de vida del sistema inteligente.

13

3. Reglamento de Inteligencia
Artificial
La puesta en servicio o la utilización de sistemas de IA de alto riesgo debe supeditarse al cumplimiento de determinados requisitos obligatorios, entre los cuales están los de ciberseguridad. Estos requisitos tienen como objetivo garantizar que los sistemas de
IA de alto riesgo disponibles en la Unión o cuyos resultados de salida se utilicen en la Unión no representen riesgos inaceptables para intereses públicos importantes reconocidos y protegidos por el Derecho de la Unión.
El Reglamento 2024/1689 del Parlamento Europeo y del Consejo, de 13 de junio de 2024
(Reglamento Europeo de Inteligencia Artificial), ya en su considerando (76) establece claramente sus objetivos, indicando que existe una ciberseguridad específica para la inteligencia artificial, estrechamente relacionada con el concepto ya existente, pero con particularidades propias. En este apartado se incluyen los artículos referentes a la generación de ciberseguridad del Reglamento Europeo de Inteligencia Artificial y se detalla en qué secciones de esta guía se abordan los diferentes elementos de dichos artículos.

3.1 Análisis previo y relación de los artículos
El artículo 15 establece los requerimientos que deben cumplirse en materia de tres aspectos fundamentales “Precisión, solidez y ciberseguridad”. Precisión y solidez son tratados de manera específica en sus guías.
En el artículo 15 se indica también que estos sistemas tendrán que estar protegidos frente a ataques de envenenamiento de los datos, ataques de adversario en todas sus variantes y deberán estar diseñados y desarrollados de tal manera que pueda ser resistentes a la explotación de fallos por terceros. Los ataques de terceros podrán ser realizados por usuarios, legítimos o no, los cuales pudieran emplear la capacidad del sistema de IA para fines ilícitos o ilegales que no se correspondan en ningún caso con la finalidad prevista del sistema. Por ejemplo, usuarios legítimos podrían utilizar el sistema para extraer consultas realizadas por usuarios previos.
En esta guía se va a realizar énfasis en las partes de dicho artículo que están orientadas específicamente a ciberseguridad en IA, que son del artículo 15 los puntos 1 y 5.
Artículo 15: Precisión, solidez y ciberseguridad, punto 1 establece la necesidad de un adecuado nivel de ciberseguridad de manera uniforme durante todo su ciclo de vida.

14

Artículo 15: Precisión, solidez y ciberseguridad, punto 5 incide en las medidas y componentes en materia de ciberseguridad específica de la IA sobre los que se desarrolla el contenido a lo largo de la guía.

3.2 Requisitos del Reglamento de IA

Art.15 – Precisión, solidez y ciberseguridad
1. Los sistemas de IA de alto riesgo se diseñarán y desarrollarán de modo que alcancen un nivel adecuado de precisión, solidez y ciberseguridad y funcionen de manera uniforme en esos sentidos durante todo su ciclo de vida.
2. Para abordar los aspectos técnicos sobre la forma de medir los niveles adecuados de precisión y solidez establecidos en el apartado 1 y cualquier otro parámetro de rendimiento pertinente, la Comisión, en cooperación con las partes interesadas y organizaciones pertinentes, como las autoridades de metrología y de evaluación comparativa, fomentará, según proceda, el desarrollo de parámetros de referencia y metodologías de medición.
3. En las instrucciones de uso que acompañen a los sistemas de IA de alto riesgo se indicarán los niveles de precisión de dichos sistemas, así como los parámetros pertinentes para medirla.
4. Los sistemas de IA de alto riesgo serán lo más resistentes posible en lo que respecta a los errores, fallos o incoherencias que pueden surgir en los propios sistemas o en el entorno en el que funcionan, en particular a causa de su interacción con personas físicas u otros sistemas. Se adoptarán medidas técnicas y organizativas a este respecto.
La solidez de los sistemas de IA de alto riesgo puede lograrse mediante soluciones de redundancia técnica, tales como copias de seguridad o planes de prevención contra fallos.
Los sistemas de IA de alto riesgo que continúan aprendiendo tras su introducción en el mercado o puesta en servicio se desarrollarán de tal modo que se elimine o reduzca lo máximo posible el riesgo de que los resultados de salida que pueden estar sesgados influyan en la información de entrada de futuras operaciones (bucles de retroalimentación) y se garantice que dichos bucles se subsanen debidamente con las medidas de reducción de riesgos adecuadas.
5. Los sistemas de IA de alto riesgo serán resistentes a los intentos de terceros no autorizados de alterar su uso, sus resultados de salida o su funcionamiento aprovechando las vulnerabilidades del sistema.

15
