---
name: aesia-09-guia-de-precision-04-reglamento-de-inteligencia-artificial-pa
description: "AESIA: aesia 09 guia de precision, sección «Reglamento de Inteligencia Artificial (parte 1)» (págs. 12-19). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-09-guia-de-precision
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Reglamento de Inteligencia Artificial (parte 1)"
  paginas: 12-19
  origen: 2026-07-17-aesia-09-guia-de-precision.pdf
  oficial: false
---
# Reglamento de Inteligencia Artificial (parte 1)

3. Reglamento de Inteligencia
Artificial
La puesta en servicio o la utilización de sistemas de IA de alto riesgo debe supeditarse al cumplimiento de determinados requisitos obligatorios, entre los cuales está el de precisión. Estos requisitos tienen como objetivo garantizar que los sistemas de IA de alto riesgo disponibles en la Unión o cuyos resultados de salida se utilicen en la Unión no representen riesgos inaceptables para intereses públicos importantes, reconocidos y protegidos por el Derecho de la Unión.

En este apartado se incluye los artículos referentes a la generación de precisión del
Reglamento 2024/1689 del Parlamento Europeo y del Consejo, de 13 de junio de 2024
(Reglamento Europeo de Inteligencia Artificial) y se detalla en que secciones de esta guía se abordan los diferentes elementos de dichos artículos.

3.1 Análisis previo y relación de los artículos
Como hemos indicado en la introducción, la precisión en el Reglamento Europeo de IA está claramente relacionada y presente con otros ámbitos del propio sistema de IA. Es dentro del artículo 15, precisión, solidez y ciberseguridad, del Reglamento Europeo de IA, donde se aborda de manera específica los requerimientos que debe cumplir el sistema de IA, en los aspectos relativos a la precisión.
Este artículo establece los requisitos que deben cumplirse en materia de tres aspectos fundamentales “Precisión, solidez y ciberseguridad”. Los requisitos de ciberseguridad y solidez son tratados de manera específica en sus guías.
En esta guía vamos a realizar énfasis en los párrafos de dicho artículo que están orientados específicamente a la precisión en IA.
Por ello, indicaremos una serie de medidas destinadas a que los sistemas de IA no degraden sus especificaciones de rendimiento y exactitud una vez puestos en marcha, durante todo su ciclo de vida.
Los sistemas de IA no deben de presentar problemas de funcionamiento (compatibilidad con antiguas librerías que usen o datos que procesen) ni de calidad en cuanto a la precisión de estos, conforme se usan en el tiempo. Para ello, deberán respetar niveles mínimos de precisión y/o métricas asociadas concretas a la tarea, preestablecidas, garantizando así que esta sea consistente durante todo el ciclo de vida.
Además, el Reglamento Europeo de IA indica (Art. 15, precisión, solidez y ciberseguridad
Párrafo 2):
Las instrucciones sobre cómo obtener los niveles precisión propuestos, cómo usarlos e interpretarlos (guía de transparencia), sus umbrales y métricas asociadas a ella deben documentarse según la guía de documentación técnica, ver el apartado 5.
11

Dentro del análisis del articulado que se definen en esta guía, se puede resumir en los siguientes puntos:
- Analizar y establecer la relación entre el ciclo de vida del sistema de IA de alto riesgo y la
precisión, en los puntos críticos del ciclo de vida. Este aspecto, se revisa en el apartado
4.1 Precisión y ciclo de vida. En este apartado se aborda como aspectos del ciclo de vida del sistema de IA, pueden influir en la precisión final del sistema, y como éstos deben de considerarse, con el objetivo de que la precisión sea consistente a lo largo este.
- Acorde al modelo de nuestro sistema de IA, seleccionar las métricas más adecuadas para
la medida de la precisión, en el apartado 4.2, se aborda como se pueden seleccionar dichas métricas.
- Además, estas métricas incluirán la selección de una función objetivo que será utilizada
para alcanzar durante el entrenamiento la precisión indicada.
- Una vez seleccionadas las métricas y sus valores acorde a la finalidad prevista, el
proveedor debe garantizar la precisión a lo largo del ciclo de vida de manera consistente tal y como establece el Reglamento Europeo de IA. En el apartado 4.3, se proporcionan, a modo de ejemplo, las medidas que entendemos que pueden ayudan a cubrir ese requisito específico.
- Finalmente, todo el proceso se recomienda que esté acompañado de una correcta
documentación acorde tanto a la documentación técnica (ver la propia guía de documentación técnica en detalle) como de las medidas propuestas en esta guía que deben ser adecuadamente documentadas. Abordamos en el apartado 5, cómo se propone realizar esta acción.

3.2 Contenido de los artículos en el Reglamento de IA
Aclarar, que dentro del artículo 15 en el que se trata de precisión, solidez y ciberseguridad, se habla específicamente de precisión exclusivamente en los puntos uno, dos y tres.

AI Act
Art.15 – Precisión, solidez y ciberseguridad
1. Los sistemas de IA de alto riesgo se diseñarán y desarrollarán de modo que alcancen un nivel adecuado de precisión, solidez y ciberseguridad y funcionen de manera uniforme en esos sentidos durante todo su ciclo de vida.
2. Para abordar los aspectos técnicos sobre la forma de medir los niveles adecuados de precisión y solidez establecidos en el apartado 1 y cualquier otro parámetro de rendimiento pertinente, la Comisión, en cooperación con las partes interesadas y organizaciones pertinentes, como las autoridades de metrología y de evaluación comparativa, fomentará, según proceda, el desarrollo de parámetros de referencia y metodologías de medición.
3. En las instrucciones de uso que acompañen a los sistemas de IA de alto riesgo se indicarán los niveles de precisión de dichos sistemas, así como los parámetros pertinentes para medirla.
12

4. Los sistemas de IA de alto riesgo serán lo más resistentes posible en lo que respecta a los errores, fallos o incoherencias que pueden surgir en los propios sistemas o en el entorno en el que funcionan, en particular a causa de su interacción con personas físicas u otros sistemas. Se adoptarán medidas técnicas y organizativas a este respecto.
La solidez de los sistemas de IA de alto riesgo puede lograrse mediante soluciones de redundancia técnica, tales como copias de seguridad o planes de prevención contra fallos.
Los sistemas de IA de alto riesgo que continúan aprendiendo tras su introducción en el mercado o puesta en servicio se desarrollarán de tal modo que se elimine o reduzca lo máximo posible el riesgo de que los resultados de salida que pueden estar sesgados influyan en la información de entrada de futuras operaciones
(bucles de retroalimentación) y se garantice que dichos bucles se subsanen debidamente con las medidas de reducción de riesgos adecuadas.
5. Los sistemas de IA de alto riesgo serán resistentes a los intentos de terceros no autorizados de alterar su uso, sus resultados de salida o su funcionamiento aprovechando las vulnerabilidades del sistema.
Las soluciones técnicas encaminadas a garantizar la ciberseguridad de los sistemas de IA de alto riesgo serán adecuadas a las circunstancias y los riesgos pertinentes.
Entre las soluciones técnicas destinadas a subsanar vulnerabilidades específicas de la IA figurarán, según corresponda, medidas para prevenir, detectar, combatir, resolver y controlar los ataques que traten de manipular el conjunto de datos de entrenamiento («envenenamiento de datos»), o los componentes entrenados previamente utilizados en el entrenamiento («envenenamiento de modelos»), la información de entrada diseñada para hacer que el modelo de IA cometa un error
(«ejemplos adversarios» o «evasión de modelos»), los ataques a la confidencialidad o los defectos en el modelo.

3.3 Correspondencia del articulado con los apartados de la guía
En la tabla dispuesta a continuación se detalle en que secciones de esta guía se abordan los diferentes elementos de dicho artículo:
Artículo Reglamento

Requerimiento Reglamento

Sección guía
Apartado 4.1 y

15.1

Nivel adecuado de precisión.

15.1

Precisión consistente a lo largo del ciclo de vida.

Apartado 4.1

15.2

Aspectos técnicos de la precisión.

Apartado 5

Apartado 4.3

13

15.3

Instrucciones y niveles de precisión pertinentes.

Apartado 5

14

4. ¿Cómo puedo abordar los requisitos?
4.1 Precisión y ciclo de vida
Establecer y medir la precisión del sistema de IA es un proceso que abarca todo el ciclo de vida de este, tal y como hemos indicado. Existen, no obstante, puntos durante el ciclo de vida donde establecer la precisión del sistema acorde a su finalidad prevista es crítico. A continuación, para completar el proceso de trabajo descrito, presentamos estos puntos críticos, cómo estos afectan a la precisión, y cómo abordarlos.

4.1.1 Preprocesamiento de los datos
La precisión de un modelo dependerá de la calidad de los datos de entrenamiento y, por tanto, de su preprocesado. Además de las medidas de la guía de Datos, existen cuestiones relevantes que pueden, a título orientativo y no vinculante, tenerse en cuenta en el preprocesamiento de los datos para garantizar la precisión del modelo son:
-

-

-

-

Los datos usados para probar el modelo de machine learning deben ser representativos de la finalidad prevista que se pretende dar al sistema (ver Guía de
Datos).
Los datos de entrenamiento del modelo deben estar libres de sesgo de muestreo.
Además, los datos de entrenamiento para una tarea particular no necesariamente son extensibles a otras tareas diferentes. Debe ponerse especial atención al dividir bases de datos no balanceadas para asegurar que se mantienen distribuciones similares entre datos de entrenamiento, validación y evaluación (ver Guía de Datos).
Cuando se preprocesen datos de forma diferente, con el objetivo de encontrar la precisión adecuada a la finalidad prevista, no se podrá atribuir la diferencia en precisión al algoritmo siendo evaluado (el modelo con el objetivo o tarea final,
“downstream algorithm”). Por tanto, para comparar la precisión entre varios modelos deberán usarse idénticas maneras de preprocesado de datos, y el mismo conjunto de evaluación (test) deberá ser usado para comparar dos modelos, de forma que los conjuntos de validación y evaluación nunca contendrán muestras que estén incluidas también en el conjunto de entrenamiento. Ver ISO/IEC TS
4213:2022, Information technology — Artificial intelligence — Assessment of machine learning classification performance [116].
Las tareas de preentrenamiento del modelo, si difieren de las tareas del modelo final, deberán documentarse de forma precisa y reproducible igualmente, y se velará porque coincidan tanto en fase de entrenamiento, como de validación y de puesta en producción.

Más información sobre sesgos en sistemas de IA en ISO/IEC TR 24027 y en Guía de Datos.

15

Ejemplo - Detección de denuncias falsas
Durante la fase de diseño del sistema, se establece que la precisión seleccionada para el sistema debe de garantizarse para un amplio abanico de denuncias, y que la precisión no debe verse afectada por elementos de categorización de la denuncia en sí misma como dirección o pertenencia a minorías.
Para ello, se toma la decisión, tal y como se indica en este apartado, de realizar un trabajo sobre esos conjuntos de datos, con el objetivo de disponer de una base de datos que permita a lo largo de todo el ciclo de vida definir, establecer y documentar la métrica de precisión elegida. Para ello:
-

Se recaban denuncias de todo el territorio nacional en castellano. La recopilación es representativa en equivalente proporción por cada territorio, para evitar sesgos de tamaño de población.
Sumado al punto anterior, para mitigar el sesgo de muestreo, se realiza una mezcla aleatoria de las denuncias, que garantice una distribución uniforme a lo largo de los conjuntos de entrenamiento, prueba y validación.
El preprocesado requerido para el proceso de anonimización, es idéntico para todos los orígenes territoriales y conjuntos de datos. Para ello, se desarrolla una pieza de software específico de preprocesado única para todos los territorios y que será utilizada para remitir los datos. De esta manera el equipo de diseño, desarrollo e implantación ya recibe datos anonimizados.

-
-

Todo este proceso, es documentado en cada uno de los pasos indicando las decisiones tomadas y la motivación.

4.1.2 Sobreaprendizaje (Overfitting)
Los algoritmos generativos se entrenan optimizando parámetros del modelo de aprendizaje de manera que se maximiza la probabilidad de acierto, sobre la muestra de los datos de entrenamiento disponibles y acorde a las categorías de clasificación establecidas, mientras que los discriminativos optimizan sus parámetros para maximizar la exactitud de la clasificación
[116].
Para evitar el común problema del sobreaprendizaje se podrían tomar medidas de acuerdo con el tipo de modelo y finalidad prevista. En general, y a modo orientativo y no vinculante, estas son:
-

-

Todos los hiperparámetros pueden ser reportados en los procesos de entrenamiento/prueba y validación del modelo, así como sus valores para cada modelo. El sesgo por selección de hiperparámetros puede tenerse en cuenta cuando se comparan modelos, pues diferentes modelos tienen diferentes capacidades de ajuste, por lo que el nivel de sobreaprendizaje durante entrenamiento puede diferir entre algoritmos, especialmente en aprendizaje profundo.
Ninguna información del conjunto de datos de prueba se recomienda que se use cuando se ajusten los hiperparámetros, esto típicamente lleva a sobreestimar las métricas de precisión con optimismo. Cuando la información de etiqueta es
16

-

necesaria para un ajuste o tuning, típicamente se usan las de un conjunto de datos separado, el conjunto de validación, el cual es disjunto del de prueba. Este desafío se puede enfocar, por ejemplo, con validación cruzada anidada, donde un bucle exterior mide la precisión de la predicción mientras que el bucle interior ajusta los hiperparámetros de los modelos individuales. De esta manera, los métodos pueden elegir la configuración óptima de parámetros, para los modelos predictivos se eligen en el bucle exterior.
Idealmente, se podría utilizar herramientas para la automatización de la búsqueda de hiperparámetros, por ejemplo, Hyperband, Hyperopt u Optuna1 (comúnmente usados en aprendizaje por refuerzo).

Ejemplo - Detección de denuncias falsas
El sistema de gestión de riesgos del proveedor para el sistema de IA ha establecido que existe un riesgo para los derechos y libertades si el sistema está sobre ajustado (overfitting)
respecto a los sets de entrenamiento. Un overfitting puede causar que denuncias verdaderas sean procesadas como falsas llevando a un procedimiento de tramitación diferente, por lo que este overfitting pueda afectar al proceso final. De esta manera, el sobreajuste al conjunto de datos de entrenamiento, prueba y validación puede proporcionar una medida excelente de la métrica de precisión elegida, pero cuando el sistema se encuentra en producción, provocar resultados inadecuados para su finalidad prevista.
Para ello y siguiendo las indicaciones presentes en esta guía, el proveedor establece que:
-

-

-

-

Los hiperparámetros de entrenamiento se van a almacenar asociados al código del modelo de IA, para que estos estén siempre accesibles e identificables, de tal manera que el equipo de desarrollo pueda consultar un histórico de estos y estudiar la posibilidad de overfitting.
Los conjuntos de entrenamiento, prueba y validación se organizan y estructuran de manera que todos tienen una combinación aleatoria de orígenes, para que los orígenes de las denuncias anónimas ya clasificadas se encuentres uniformemente distribuidos en la muestra. Para cada denuncia se genera un identificador único (a través del cálculo de un hash 256 de su contenido en texto). Este sistema se utiliza para que los conjuntos de entrenamiento, prueba y validación sean completamente disjuntos y no contengan ninguna muestra en común.
Cuando se está realizando el entrenamiento se aplica la indicación propuesta en este apartado de dos bucles de programación, que además llevan la cuenta del origen de los datos, para poder detectar intercambio de datos entre conjuntos. Así no solo se garantiza el ajuste de hiperparámetros si no que se garantiza adecuadamente que los conjuntos son disjuntos.
Dentro del framework de trabajo para el sistema de IA, el equipo de desarrollo ha utilizado, combinado con el proceso descrito en los puntos anteriores, una librería específica del framework para el ajuste automatizado de los hiperparámetros.

Las palabras y descripciones destacadas se corresponden con términos que son desarrollados en el glosario (ver 7.4).
1

17

18
