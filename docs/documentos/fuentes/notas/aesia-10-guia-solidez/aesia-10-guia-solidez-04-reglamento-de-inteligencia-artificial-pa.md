---
name: aesia-10-guia-solidez-04-reglamento-de-inteligencia-artificial-pa
description: "AESIA: aesia 10 guia solidez, sección «Reglamento de Inteligencia Artificial (parte 1)» (págs. 15-22). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-10-guia-solidez
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Reglamento de Inteligencia Artificial (parte 1)"
  paginas: 15-22
  origen: 2026-07-17-aesia-10-guia-solidez.pdf
  oficial: false
---
# Reglamento de Inteligencia Artificial (parte 1)

3. Reglamento de Inteligencia
Artificial
3.1 Análisis previo y relación de los artículos
Este artículo establece los requerimientos que deben cumplirse en materia de tres aspectos fundamentales “Precisión, solidez y ciberseguridad”. Ciberseguridad y precisión son tratadas de manera específica en sus guías.
En este apartado vamos a realizar énfasis en los párrafos de dicho artículo que están orientados específicamente a la solidez en sistemas de IA de alto riesgo, que se concentran en los apartados 1 y 4.
Artículo 15 Precisión, solidez y ciberseguridad apartado 1 → establece la necesidad de mantener adecuados niveles de precisión durante todo el ciclo de vida del sistema de
IA, por lo que indicaremos una serie de medidas destinadas a que los sistemas de IA no degraden sus especificaciones de rendimiento y solidez una vez puestos en marcha, durante todo su ciclo de vida.
Los sistemas de IA no deben de presentar problemas de funcionamiento (compatibilidad con antiguas librerías que usen o datos que procesen) ni de calidad en cuanto a la solidez de éstos conforme se usan en el tiempo. Para ello, deberán alcanzar y respetar niveles mínimos razonables de solidez (y métricas asociadas) preestablecidos en los requisitos de estos y concretos a la tarea que resuelven, que garanticen su seguridad y buen funcionamiento.
Artículo 15 Precisión, solidez y ciberseguridad apartado 4 → establece la necesidad de medidas de protección frente a errores, fallos o incoherencias.
Estos aspectos descritos en estos apartados amplían el foco requerimientos del
Reglamento Europeo de la IA relativos a la solidez abordando los fallos y sistemas de redundancia como un requerimiento importante. Del mismo modo, el artículo refleja que la solidez para aquellos sistemas que continúan aprendiendo tras su puesta en marcha debe ser considerada de manera específica y con medidas particulares.
El concepto e interpretación de la solidez, en términos de medidas técnicas y métricas de evaluación, es inseparable y dependiente del dominio de aplicación y, por tanto, su finalidad prevista.

14

3.2 Contenido de los artículos en el Reglamento de IA

AI Act
Art.15 – Precisión, solidez y ciberseguridad
1. Los sistemas de IA de alto riesgo se diseñarán y desarrollarán de modo que alcancen un nivel adecuado de precisión, solidez y ciberseguridad y funcionen de manera uniforme en esos sentidos durante todo su ciclo de vida.
2. Para abordar los aspectos técnicos sobre la forma de medir los niveles adecuados de precisión y solidez establecidos en el apartado 1 y cualquier otro parámetro de rendimiento pertinente, la Comisión, en cooperación con las partes interesadas y organizaciones pertinentes, como las autoridades de metrología y de evaluación comparativa, fomentará, según proceda, el desarrollo de parámetros de referencia y metodologías de medición.
3. En las instrucciones de uso que acompañen a los sistemas de IA de alto riesgo se indicarán los niveles de precisión de dichos sistemas, así como los parámetros pertinentes para medirla.
4. Los sistemas de IA de alto riesgo serán lo más resistentes posible en lo que respecta a los errores, fallos o incoherencias que pueden surgir en los propios sistemas o en el entorno en el que funcionan, en particular a causa de su interacción con personas físicas u otros sistemas. Se adoptarán medidas técnicas y organizativas a este respecto.
La solidez de los sistemas de IA de alto riesgo puede lograrse mediante soluciones de redundancia técnica, tales como copias de seguridad o planes de prevención contra fallos.
Los sistemas de IA de alto riesgo que continúan aprendiendo tras su introducción en el mercado o puesta en servicio se desarrollarán de tal modo que se elimine o reduzca lo máximo posible el riesgo de que los resultados de salida que pueden estar sesgados influyan en la información de entrada de futuras operaciones (bucles de retroalimentación) y se garantice que dichos bucles se subsanen debidamente con las medidas de reducción de riesgos adecuadas.
5. Los sistemas de IA de alto riesgo serán resistentes a los intentos de terceros no autorizados de alterar su uso, sus resultados de salida o su funcionamiento aprovechando las vulnerabilidades del sistema.
Las soluciones técnicas encaminadas a garantizar la ciberseguridad de los sistemas de
IA de alto riesgo serán adecuadas a las circunstancias y los riesgos pertinentes.
Entre las soluciones técnicas destinadas a subsanar vulnerabilidades específicas de la
IA figurarán, según corresponda, medidas para prevenir, detectar, combatir, resolver y controlar los ataques que traten de manipular el conjunto de datos de entrenamiento
(«envenenamiento de datos»), o los componentes entrenados previamente utilizados en el entrenamiento («envenenamiento de modelos»), la información de entrada diseñada para hacer que el modelo de IA cometa un error («ejemplos adversarios» o
«evasión de modelos»), los ataques a la confidencialidad o los defectos en el modelo.

15

3.3 Correspondencia del articulado con los apartados de la guía
En la tabla dispuesta a continuación se detalle en que secciones de esta guía se abordan los diferentes elementos de dicho artículo:
Artículo
Reglamento

Requerimiento Reglamento

Sección guía

15.1 párrafo 1

Nivel adecuado y consistente de solidez durante todo el ciclo de vida.

Apartado 4.1

15.4 párrafo 1

Resistencia a errores, fallos e incoherencias.

Apartado 4.2

15.4 párrafo 2

Planes de redundancia, respaldo y a prueba de fallos.

Apartado 4.3

15.4 párrafo 3

Sistemas que siguen aprendiendo tras su puesta en marcha.

Apartado 4.4

16

4. ¿Cómo puedo abordar los requisitos?
4.1 Evaluación de la solidez
Las métricas de solidez aplicables garantizadas por el proveedor en la documentación deben reflejar y ser una señal de la calidad del sistema. De otro modo, cuando no se puedan garantizar los requisitos establecidos en la documentación en cuanto a nociones o métricas de solidez establecidas mínimas, el proveedor pondrá a disposición del responsable del sistema mecanismos para notificar al humano que se requiere su supervisión (según guía de supervisión humana), tanto para una variación temporal de estas métricas de solidez, como en el caso de una variación persistente en forma de una degradación de la respuesta.
Los proveedores del sistema de IA se recomiendan que implementen capacidades que lo provean de la solidez necesaria acorde a la finalidad prevista y con el objetivo de mitigar los riesgos encontrados en el plan de riesgos (ver guía de riesgos).
Se recomienda que durante cualquier momento del ciclo de vida válido del sistema, el proveedor pueda:
- Facilitar al responsable del despliegue mecanismos para observar, supervisar y
reportar diferentes tipos de degradación del modelo (salidas del modelo fuera de rango, posibles ataques por adversarios o perturbaciones que datos o modelo puedan sufrir) que sobrepasen los límites documentados como razonables para cada métrica de solidez, con el fin de hacerlos reproducibles para su corrección.
- Cuando los requisitos de solidez garantizados cambien, corregirlos para garantizar
los estándares o métricas provistas según la documentación. Cuando irremediablemente esto no sea posible, y se incumplan las garantías documentadas, tanto la documentación como la tarjeta de base de datos como la tarjeta de modelo de IA responsable se recomienda que se actualicen y se deberá notificar a los responsables del despliegue implicados (ver guía de precisión). Si este ajuste se realiza con una actualización, se puede explicar la motivación del cambio en la documentación técnica, tal y como ésta indica para las actualizaciones.
Las medidas que puede tomar el proveedor en marcha incluirán aquellas que miden la calidad de un sistema basada en su capacidad de mantener cierto nivel de solidez asociado a su precisión bajo cualquier circunstancia [SC42 N483 ISO IEC TR 24029-1]. Para demostrar esta capacidad se pueden hacer análisis estadísticos, pero para probarla se requiere alguna forma de análisis formal (Ver enfoques en [ISO SC42 N938 ISO IEC CD
24029-2], ISO/IEC 25059:2023], método SQuaRE [75] y métodos en [ISO/IEC TR 240291:2021 para evaluar la solidez sin el uso de métodos formales).

17

En este apartado vamos a desarrollar, por tanto, las medidas que, a modo orientativo, son responsabilidad del proveedor, y las vamos a agrupar por aspectos específicos del sistema de IA, para poder poner la solidez en perspectiva para cada una de ellas.
Los siguientes puntos representan una indicación de los temas que se van a abordar, relacionados con la evaluación de la solidez:
- La relación del ciclo de vida y la solidez, considerada como una vertical para el
sistema de IA.
- Se presenta un enfoque para seleccionar las métricas de solidez del sistema de IA.
- Se establece el proceso de verificación y validación de las métricas seleccionadas.
- Se considera que tanto eficiencia, como rendimiento, son elementos asociados a la
solidez, por lo que proporcionamos indicaciones para como alcanzarlos.
- Finalmente se aborda el aspecto de monitorizar la solidez
Organizativamente, se recomienda que el responsable del despliegue tenga formación suficiente para detectar cuando se produce una degradación del sistema y así poder retroalimentar al proveedor cuando así lo requiera la documentación del producto. Así, el responsable del despliegue podrá:
1. Conocer los conceptos básicos asociados a la solidez y familiarizarse con la documentación que le da acceso para:
a. Visualizar cuadros de mando de monitoreo de todas las métricas de solidez.
Estos cuadros de mando deben ser integrados en el sistema de AI por el proveedor, pueden desarrollarse utilizando soluciones comerciales, de código abierto o desarrollos propios.
b. Interpretar y usar la salida del sistema en cuanto a su solidez, a nivel de funcionalidad, modelo y sistema.
2. Acceder a los tutoriales disponibles (en línea, tutoriales, material didáctico adicional) más allá de la documentación del producto para poder comprender la funcionalidad del producto de IA en su totalidad cuando sea necesario para conseguir el punto anterior. Dado que se trata de sistemas de alto riesgo, plantearse planes específicos de formación para el personal cuando la cualificación o la formación de los operadores pueda no ser suficiente.
Debe entenderse que los medios técnicos integrados en el sistema de IA de alto riesgo han sido puestos a disposición del responsable del despliegue por parte del proveedor del sistema, proporcionando conocimiento de estos durante la fase de comercialización y a lo largo de todo el ciclo de vida del propio sistema.
Técnicamente, para que el responsable del despliegue pueda evaluar la salida del sistema de IA en su conjunto, y para una entrada de datos concreta, se recomienda que conozca con suficiente nivel de detalle la documentación para poder actuar según la guía de supervisión, si la solidez se degrada bajo los niveles mínimos garantizados. Así, a modo orientativo, es responsabilidad del responsable del despliegue:
Saber usar y acceder la interfaz de obtención de métricas de solidez y eficiencia computacional asociadas. Para poder usar el sistema, el responsable del despliegue se recomienda que se familiarice con:
18

- La interfaz del sistema y de las salidas de este, para cada funcionalidad del sistema, y
para el sistema en su conjunto. Dentro de su finalidad prevista y acorde al uso de éste.
- Estadísticas que sirvan para comparar el funcionamiento y métricas del sistema
provisto con otros modelos existentes del estado del arte o usados como algoritmo/modelo base.
- Mecanismos de gestión de notificaciones de potenciales errores de funcionamiento
documentados, procedimientos de inspección, supervisión, corrección, notificación de potenciales salidas erróneas, o la ausencia de estas.
- Posibles acciones que tomar cuando la salida no esté dotada de explicabilidad
coherente con su solidez, o cuando presencie niveles no aceptables de solidez o incertidumbre en la salida.
Además, podrá mejorar su experiencia de usuario estudiando la relevancia de las métricas de solidez aplicables y las elegidas, según el caso de uso, para observar y comprender las diferencias en significancia estadística de los modelos.
1.
2.

Saber explorar las métricas de solidez y otras métricas de calidad asociadas a la buena funcionalidad y supervisión de éste.
Conocer cómo notificar o corregir potenciales errores de funcionamiento (salidas erróneas, ausencia de éstas, etc.) al proveedor, e inspeccionar datos de entrada y salida.

4.1.1 Ciclo de vida
En cada elemento del ciclo de vida de un sistema de IA de alto riesgo, se establece un nivel de solidez acorde a la finalidad prevista del sistema, estableciendo unas medidas adecuadas. Dependiendo de la fase del ciclo de vida las medidas deberán de ser realizadas por proveedor (diseño, desarrollo) o responsable del despliegue (durante su puesta en producción o funcionamiento), evitando la degradación, y cualquier problema de funcionamiento que aminore la solidez del sistema durante su ciclo de vida.
La solidez de un sistema de IA se recomienda que sea verificada durante todo el ciclo de vida definido en este orden:
- Diseño y desarrollo. Se pueden identificar las características reconocidas y se debe
verificar la separabilidad. Se diseñarán experimentos para evaluar las capacidades del sistema de IA en cuanto a un conjunto deliberado de variables a las cuales el modelo debe mostrar solidez. Por ejemplo, se considerarán enfoques de aprendizaje por conjuntos (técnica que combina múltiples modelos individuales para crear un modelo final, ensemble learning) para incrementar la solidez de los modelos, incluyendo la resistencia a ataques adversarios o de evasión. En este aspecto, y relacionado con los datos, podemos considerar el siguiente ejemplo: en un sistema de reconocimiento del habla automático, se demostrará el uso de datos lo suficientemente grandes y diversos, que llevan al modelo a soportar y tratar, adecuadamente, acentos, ruido de fondo y vocabulario técnico.
- Verificación y validación (V&V). Se pueden verificar las partes cubiertas del dominio
de entrada (por ejemplo, con criterios de sensibilidad, o usando métodos formales)
19

y se puede medir el impacto de la perturbación forzando en el proceso de verificación y validación la perturbación intencionada, formal y relacionada con la finalidad prevista adecuada. En el apartado 4.1.3 se presentan diferentes medidas para abordar este aspecto.
- Puesta en producción / implantación. En este caso, se puede verificar el impacto de
problemas causados por la precisión numérica (compiladores que reorganizan o reemplazan operaciones, reducen precisión numérica o cambian el proceso de redondeo). En estos escenarios, y tal como se ha definido en la guía de ciberseguridad, para evitar los fallos originados por problemas de configuración, los entornos de validación y producción del sistema de IA tienen que ser idénticos, o dotados de los mecanismos que les permitan ser idénticos (como se indica en la citada guía, utilizar tecnologías de contenedores o equivalentes). En el apartado
4.1.6, abordamos en detalle aspectos centrados en la solidez y los sistemas en producción.

4.1.2 Selección de métricas
Hasta ahora hemos visto el concepto de solidez y sus propiedades deseables, en el marco organizativo del sistema de IA. Este marco organizativo es el andamiaje necesario para que sobre él establezcamos el detalle de la operativa técnica sobre como cuantificar la solidez.
En sucesivos apartados vamos a abordar como se enfoca la solidez, técnicamente, con metodologías aplicables y métricas asociadas.
La metodología orientativa que presentamos para evaluar la solidez de un modelo se basa en los siguientes pasos:
1.

2.

3.

4.
5.

Establecer requisitos u objetivos de solidez y métricas asociadas: ¿Hasta qué punto el sistema requiere ser sólido? ¿Cuáles son las características de solidez de interés? Las propiedades de solidez demuestran el grado de generalización del modelo a datos nuevos, en comparación con su precisión en los datos con que fue entrenado, o con datos esperados en operaciones típicas. Se debe constituir el conjunto de criterios de decisión de propiedades de solidez. Dados estos, se recomienda identificar las métricas que cuantifican los elementos que demuestran conseguir la solidez.
Planificación de experimentos que demuestran solidez. Éstos se basarán en métodos estadísticos, formales o empíricos, o en la práctica, en una combinación de varios.
Conducir los experimentos: Los experimentos definidos en el paso 1 pueden ejecutarse acorde al plan establecido y se deben registrar los resultados, los conjuntos de datos utilizados y los valores de salida, con los que se calculan las métricas de manera agregada.
Analizar resultados contra las métricas establecidas seleccionadas en el punto 1.
Interpretar los resultados para informar la decisión, estos se recomienda que sean interpretados no solo en el valor de la propia métrica, si no en relación de su evaluación con todos los experimentos, tanto de manera progresiva (evolución en el tiempo) como agregada (estadísticamente).

20

6.

Decidir la solidez del sistema dados los criterios e interpretación identificados antes. Si la solidez es insuficiente, volver a la etapa que alivie sus deficiencias:
añadiendo objetivos de solidez, métricas, otras medidas, replantear experimentos o modificar el protocolo de recogida de datos para el experimento o corregir el análisis. Esta iteración se recomienda que se repita hasta que se alcance el objetivo de solidez establecido.

Ejemplo – Sistema de promoción de empleados
Durante la fase de diseño del sistema de IA de cara a establecer los criterios de solidez y cómo estos se van a aplicar al sistema, el proveedor del sistema sigue las siguientes consideraciones, alineadas con los puntos destacados en este apartado:
1. Se seleccionan las siguientes características para el sistema de IA: fiabilidad, estabilidad, sensibilidad y relevancia. De acuerdo con el equipo de diseño, se establecen los umbrales para cada una de ellas, y como se deben de mantener a lo largo del ciclo de vida del sistema. Se generan conjuntos datos de validación y verificación para cada una de las diferentes características, datos que no son usados durante el entrenamiento. Además, se dispone de un grupo de control para todos los demás que también se evalúa frente a esas características.
2. Dado que no se puede desarrollar un método formal adecuado para el sistema de IA (ver apartado 7.2.1) que pueda construir un sistema al que aplicar un optimizador matemático, se opta por una combinación de métodos estadísticos y empíricos para realizar los experimentos
3. Se establece el plan de experimentación y los mecanismos de registro. El proveedor opta por mantener dentro de su sistema de control de versiones, asociado a las versiones del modelo, el acumulado de los experimentos para cada paso de las iteraciones de validación y verificación.
4. El análisis de los resultados se realizará utilizando las técnicas AUC y Lift.
5. Con el análisis se interpretan los resultados en relación con los valores de especificaciones definidos en el punto 1.
6. Se iterará hasta alcanzar la solidez deseada en el proceso de validación y verificación.
Aunque las especificaciones pueden implementarse de formas diferentes, durante el desarrollo se podrá decidir, por ejemplo, algunos valores específicos de umbrales para finalizar la optimización. Este valor no es necesariamente especificado de antemano y, por tanto, el sistema será más o menos preciso, dependiendo de los datos. Es por esto por lo que es necesario validar el modelo testeando en datos concretos para observar cómo se comporta (validación del rendimiento), y estos datos dependerán de la finalidad prevista.
Para la selección de métricas, el 7.1 Anexo I: Métricas y pruebas para sistemas de IA, se presentan una lista de referencia que a modo orientativo puede ser consultada, con la consideración que el proveedor seleccione, si así lo considera oportuno,la métrica más adecuada para la medición de la solidez siempre considerando la finalidad prevista y los riesgos.

21
