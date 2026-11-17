---
name: aesia-09-guia-de-precision-05-reglamento-de-inteligencia-artificial-pa
description: "AESIA: aesia 09 guia de precision, sección «Reglamento de Inteligencia Artificial (parte 2)» (págs. 20-27). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-09-guia-de-precision
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Reglamento de Inteligencia Artificial (parte 2)"
  paginas: 20-27
  origen: 2026-07-17-aesia-09-guia-de-precision.pdf
  oficial: false
---
# Reglamento de Inteligencia Artificial (parte 2)

4.1.3 Uso de modelos apropiados
La precisión de un modelo tendrá relevancia con respecto a cómo se posiciona con respecto al estado del arte en modelos de su categoría y/o con modelos de referencia base. Es decir, es recomendable comparar y establecer en contexto, las métricas de precisión seleccionadas, junto con aquellos modelos de base con los que está relacionado.
-

-

Por reproducibilidad y sostenibilidad de la precisión del modelo, se podría señalar o reportar estudios sobre la eliminación de los componentes y elementos (ablación en inglés) del modelo, para justificar la composición y complejidad de los componentes y elementos del modelo necesarios para alcanzar la precisión garantizada.
En ellos, se pueden usar modelos de referencia base apropiados (Baselines).
Baselines triviales tales como aquellos que siempre predicen la clase mayoritaria son útiles para calibrar la interpretación de la métrica (ver guía de Transparencia)
pero se recomienda que no sea el único punto de comparación (ISOIEC TS
4213_2)[116].

Ejemplo - Sistema de promoción de empleados
A lo largo del diseño del sistema de IA, y considerando su finalidad prevista, el proveedor del sistema analiza los modelos de referencia base dentro del estado del arte. El objetivo de este análisis es seleccionar uno que sirva tanto de punto de partida para el diseño e implementación del sistema de IA, como también para saber cómo éste se posiciona dentro del contexto de sistemas en la misma categoría.
Para el análisis, el proveedor tiene en cuenta la finalidad prevista de establecer un mecanismo para la promoción de empleados que será el elemento último de decisión en mecanismos de promoción.
Como modelo base seleccionado para esta tarea se opta por un modelo de espacio vectorial o VSM (vector space model) donde los empleados serán descritos a través de las variables (coordenadas) establecidas para su evaluación. Este modelo base trivial será utilizado junto con el resto de las técnicas indicadas en la guía, para la selección de la métrica o métricas de precisión adecuadas y para la evaluación de la precisión del sistema de IA.
El proveedor registra las motivaciones y evaluaciones realizadas sobre los candidatos de modelo de base, así como la indicación de la elección final de éste mismo.
Nota Importante: El carácter técnico de esta guía hace que los ejemplos sean específicos de los casos de uso. Esto implica que las propuestas son específicas para los modelos considerados como ejemplo, y no una solución general para otros tipos de modelo, o incluso modelos de la misma tipología. Los ejemplos deben considerarse demostrativos de la operativa para obtener una conclusión técnica pero nunca como demostrativos de dicha conclusión en sí misma. Cada proveedor deberá,establecer la medida técnica concreta para su tipo de sistema de IA y su finalidad prevista.

19

20

4.1.4 Incertidumbre y precisión
La precisión de un modelo tiene asociada un nivel de certeza o confianza que no siempre acompaña a las salidas de un modelo, si éstas no están calibradas o tienen en cuenta la incertidumbre de este. El sistema de IA puede proporcionar el resultado de su operación acompañado de un indicativo, por ejemplo, en porcentaje (o en cualquier caso normalizado)
de la certeza que otorga a dicho resultado. La incertidumbre de un modelo, entendida como confianza de sus resultados, se recomienda que se documente para garantizar la precisión y facilitar su supervisión y transparencia.

4.2 Evaluando la precisión
Se recomienda que las métricas de precisión aplicables garantizadas por el proveedor en la documentación reflejen y sean una señal de la calidad del sistema. De otro modo, cuando no se puedan garantizar estas métricas de precisión establecidas mínimas, el proveedor podría establecer mecanismos para notificar al humano de que se requiere su supervisión, (por ejemplo, de acuerdo a lo propuesto en la guía de supervisión humana).
En cada paso del ciclo de vida de un sistema de IA de alto riesgo, desde su diseño, desarrollo y validación, hasta su introducción al mercado, se debe establecer un nivel de precisión acorde a la finalidad prevista del sistema, estableciendo unas medidas adecuadas.
Dependiendo de la fase del ciclo de vida las medidas podrán de ser realizadas por proveedor
(diseño, desarrollo) o responsable del despliegue (durante su puesta en producción o funcionamiento), evitando la degradación durante su ciclo de vida.
Proveedor
El proveedor puede debe tomar las siguientes medidas organizativas para asegurar que el sistema de inteligencia artificial de alto riesgo tiene un nivel de precisión adecuado. Es responsabilidad del proveedor realizar la selección de la métrica (o métricas) de precisión más adecuada, desde la concepción y diseño del sistema de IA. Para este proceso se recomienda tener en cuenta dos aspectos importantes:
-
-

Las métricas deben estar relacionadas y motivadas por la finalidad prevista.
Las métricas deben estar motivadas y permitir mitigar los riesgos para los derechos y libertades de las personas físicas, la salud y los daños a la propiedad/medio ambiente identificados en el análisis de riesgos.

Una vez establecidos los requisitos funcionales (normalmente especificados por la funcionalidad que el responsable del despliegue solicitará en los casos de uso típicos del sistema) y los requisitos no funcionales (especificados por el personal técnico proveedor como características técnicas de implementación o métricas cuantificables), se podría diseñar una batería de pruebas significativa y representativa del dominio de aplicación. Mediante estas pruebas, se puede reflejar que, para entradas compatibles, el sistema produzca salidas esperadas dentro de los posibles rangos de salida de datos, siempre en relación directa con la finalidad prevista y con la mitigación de riesgos.

21

La batería de pruebas puede incluir, entre otros:
-
-
-
-

Aquellas pruebas de unidad y de stress acumulados tras el desarrollo del modelo
(por ejemplo, siguiendo metodologías como Test Driven Development).
Test de integración para el encaje de los requisitos funcionales y no funcionales con la finalidad prevista, y que tengan como pieza fundamental la precisión establecida.
Seguimiento de la evolución de la precisión del modelo cuando está en producción.
La degradación del modelo podrá ser monitorizada con paneles de monitorización y herramientas de visualización de la precisión. En la guía indicaremos otras posibles métricas de calidad del modelo asociadas como son las funciones objetivo. Este aspecto está relacionado con la información presentada en la guía de solidez.

Como complemento a estas medidas organizativas, el proveedor puede alinear la precisión del sistema de IA con las siguientes medidas técnicas:
-

-

-

-

-

Proveedores, diseñadores y desarrolladores podrán proporcionar documentación detallada de instalación y puesta en marcha (ver guía de guía de documentación técnica) para usar el sistema, indicando dependencias y otros requisitos o potenciales casos especiales que el responsable del despliegue debiera tener en cuenta para poder tratar con todos los tipos y formatos de datos admitidos por el sistema).
Se podrá indicar el proceso completo necesario para la puesta a punto de datos que requieran un preprocesamiento anteriormente para ser usados como entrada al sistema provisto (guía de datos).
Podrá especificar con detalle suficiente cualquier post procesamiento necesario para poder interpretar la precisión del modelo de manera clara y concisa, y así poder notificar al proveedor cuando no sea el caso.
Podrán proporcionar (según guía de documentación técnica) precisiones sobre el tipo, formato y la cantidad de datos de entrada y salida esperados, y los requisitos de éstos durante su uso en las etapas de entrenamiento, validación y testeo del sistema para obtener el nivel de precisión documentado, con ejemplos de uso de ejecución del sistema para su comprensión y transparencia hacia el responsable del despliegue.
Para que la precisión reportada sea accionable y útil, el proveedor podrá incluir los rangos posibles de los parámetros configurables y tanto de los datos de entradas como de salidas, así como las medidas de latencia esperadas para obtener una precisión esperada (ver guía de solidez).

Para poder reproducir el comportamiento del modelo en cuanto a sus métricas de precisión, se recomienda usar documentación y formateado del modelo en el estándar abierto para interoperabilidad de aprendizaje automático ONNX.
Para detallar el proceso de selección de métricas de precisión y como éstas pueden garantizar los requerimientos específicos del artículo 15, precisión, solidez y ciberseguridad, del

22

Reglamento Europeo de IA tanto en su definición como a lo largo del ciclo de vida, como tal, de manera consistente:
-

-

-

Los apartados 4.2.1 y 4.2.2 abordan la selección de las métricas propuestas tanto propias de precisión, como aquellas relativas a la función objetivo, que como se ha indicado, es muy relevante para el concepto de precisión. Ambos apartados tienen su reflejo en los anexos 7.1 Métricas de precisión y 7.2 Funciones Objetivo, respectivamente.
En el apartado 4.2.3 se proporcionan aspectos generales y complementarios relacionados con las métricas seleccionadas en los apartados anteriores y que deben tenerse en cuenta.
Ambos aspectos están directamente relacionados el apartado anterior 4.1, donde se ha indicado la relación de la precisión con hitos críticos en el ciclo de vida.

Las medidas técnicas a aplicar por el proveedor se traducirán en controles basados en métricas de precisión del modelo, que se relacionarán y establecerán con la finalidad prevista del mismo, y con el objetivo de que la precisión siempre esté destinada a garantizarla, pero con el foco principal en la mitigación de los riesgos para los derechos y libertades de las personas físicas que han sido localizados en el sistema de gestión de riesgos (ver guía de gestión de riesgos).

4.2.1 Selección de métricas de precisión
El proveedor decidirá las métricas de precisión relevantes o KPIs de control de calidad (como ejemplo puede seguirse la guía de gestión de calidad) del sistema a medir y evaluar, y elegirá un mecanismo de almacenar e informa un registro histórico o log (como ejemplo, puede seguirse la guía de registros) con los valores de éstas en el tiempo de uso del sistema, con el fin de monitorizar (ver guía de supervisión humana) la precisión y rendimiento del sistema.
Como vemos, la relación de la precisión es transversal totalmente a los aspectos solicitados por el Reglamento Europeo de IA y su relación con el resto de las guías técnicas que se proponen, las cuales no son vinculantes.
Para proporcionar a los proveedores de una referencia de métricas de precisión, ver el anexo
7.1 Métricas de precisión, donde se presentan una lista de las métricas de precisión aplicables, para una tipología de modelos. El anexo ofrece una clasificación no exhaustiva ni vinculante, que pueda servir para ayudar en la selección de la métrica.
Para el proceso de selección de la métrica de precisión adecuada al sistema de IA recomendamos al proveedor, añadido a la vertiente fuertemente técnica de la selección, tener en consideración dos aspectos fundamentales:
-
-

La finalidad prevista del sistema, considerando aquello que el sistema va a realizar y el objetivo de este.
Los riesgos encontrados detectados en el sistema de gestión de riesgos en relación con las decisiones del sistema y que deban mitigados.

Como medida técnica se recomienda disponer de un repositorio centralizado donde gestionar la información de métricas asociadas al modelo en cualquier punto de su ciclo de vida con cambios asociados para poder trazar los causantes de pérdidas de precisión de este, junto con actores identificados responsables del mismo. Se recomienda que el proveedor
23

dote al sistema de las capacidades que permitan al responsable del despliegue poder acceder y monitorizar las diferentes métricas de precisión y métricas asociadas al modelo, así como las variables protegidas, tomando como referencia a título orientativo si se considera oportuno la guía de datos, para poder observar y reportar posibles cambios en el sistema durante su uso, potenciales riesgos que puedan surgir, o sesgos que puedan emerger, en el sistema de IA alto riesgo.

Ejemplo - Detección de denuncias falsas
El proveedor, considerando que la finalidad prevista del sistema de IA es clasificar entre denuncias falsas y ciertas, con un grado de probabilidad, en una primera aproximación para seleccionar una métrica de precisión, se considera que se está realizando una clasificación binaria. Se ha identificado también, un riesgo de que no haya capacidad discriminatoria y no categorizar adecuadamente una denuncia verdadera, causando que la persona denunciante no tenga el trato adecuado.
Con ambos criterios, se establece que una de las métricas de precisión seleccionadas para este sistema de IA es la utilización del área bajo la curva ROC (ver Anexo 7.1Métricas de precisión). Un valor de 1 representa una clasificación perfecta de la denuncia y un valor de
0,5 significa que la valoración tiene una capacidad discriminatoria nula. De esta manera, a través de la selección de esta métrica de precisión a lo largo de todo el ciclo de vida se puede medir como el sistema de detección de denuncias falsas se comporta en el intervalo
1 (clasificación perfecta) y 0,5 (discriminación nula).

4.2.2 Selección de la función objetivo
Como hemos comentado en la introducción a este apartado, para optimizar la precisión del modelo, las funciones objetivo a optimizar (minimizar o maximizar), vendrán determinadas por los problemas concretos y función a aprender por el sistema de IA y, por tanto, directamente relacionados con la finalidad prevista. Éstas sirven para monitorizar el proceso de aprendizaje automático de modelos.
El proveedor del sistema puede seleccionar una función objetivo que permita, del mismo modo que la métrica de precisión, alcanzar la finalidad prevista. En el anexo 7.1, se presentan una serie de funciones objetivo-clasificadas por modelos, que pueden ser utilizadas como base para el sistema de IA.

4.2.3 Dimensiones complementarias a la precisión
Como dimensiones complementarias, y a modo de ejemplo no vinculante, que respalden la precisión, se consideran los siguientes puntos:
-

Una vez implementado el cómputo de las métricas de precisión, se deberá monitorizar (según guía de supervisión humana), durante el ciclo de vida de funcionamiento del sistema, que las nociones pertinentes al caso de uso, y la precisión del modelo global no varíen o se deterioren significativamente.

24

-

-

Tanto métricas de sesgos, como de imparcialidad y explicabilidad, tendrán un papel especialmente relevante en una fase del ciclo de vida del sistema de IA (ver guía de datos, transparencia y supervisión humana).
Tanto las herramientas de juicio equitativo (fairness) como de explicabilidad no etiquetadas como propietarias son de código abierto y preferibles por el principio de transparencia hacia IA responsable (ver guía de transparencia). Pueden encontrar más herramientas por considerar para alcanzar sistemas de IA responsable en [15].

Los aspectos relativos a estos aspectos complementarios a la precisión se presentan en mayor detalle en el anexo 7.3.
Un aspecto complementario relevante, y que es responsabilidad del proveedor, está relacionado con las capacidades que se le dota al sistema de IA para el responsable del despliegue. Para facilitar la comunicación de las métricas y el buen funcionamiento del sistema al responsable del despliegue, el responsable del despliegue se recomienda que tenga acceso a:
-

-

Una interfaz de obtención de métricas de precisión y rendimiento del sistema que permita notificar deficiencias de este, potenciales errores de funcionamiento. A título orientativo, se entiende que la disponibilidad de dicha interfaz será responsabilidad del proveedor, quién podría estará obligado a dotar al sistema de dichas capacidades, con las instrucciones adecuadas (ver guía de documentación técnica) y con las capacidades de supervisión y transparencia adecuadas (ver guías de supervisión y transparencia respectivamente).
Inspeccionar los datos tanto de entrada como de salida.

Ejemplo - Sistema de promoción de empleados
Siguiendo las indicaciones establecidas en esta guía, el proveedor del sistema de promoción de empleados ha seleccionado las métricas de su sistema de IA. La selección la realiza basándose en proporcionar una medida de la precisión adecuada a la finalidad prevista establecida para el sistema de IA y por diseño y en seleccionar también una función objetivo también adecuada para la finalidad prevista, con ello:
-

-

Por un lado, selecciona Discounted Cumulative Gain como métrica para evaluar la precisión del sistema. Está métrica está considerada para evaluar la relevancia de los resultados obtenidos en relación con una consulta o query. Dada la finalidad prevista, establece que su consulta se construye en base a los parámetros configurados para la promoción.
Por otro lado, dentro de las funciones objetivo (ver anexo 7.2), descarta la utilización de Pointwise o Pairwise por simplificar demasiado su enfoque al aproximar su sistema de AI a un modelo de regresión o una clasificación binaria respectivamente, que no están alineados con la finalidad prevista del sistema de IA y que podría incurrir en excluir candidatos válidos. Se opta por tanto por la utilización de una función objetivo de tipo Listwise que permite maximizar la métrica de precisión seleccionada.

25

Todo el proceso de análisis y selección, tanto de la métrica de precisión, como de la función objetivo son documentados, explicando motivaciones y enfoques, así como todos los resultados que de su aplicación se obtienen durante las fases de diseño y validación del sistema de IA. Todo ello, se incorporará a la documentación técnica tal y como establece la correspondiente guía a modo orientativo.

Responsable del despliegue

Se recomienda que el responsable del despliegue del sistema IA de alto riesgo, conozca, además de tener personal capacitado para entender durante la operación, el nivel de precisión del sistema. Por tanto, la precisión del modelo no será completa si no se provee transparencia de cómo se produce y cómo se computan las métricas de precisión y métricas de rendimiento relacionadas.

Ejemplo - Sistema de promoción de empleados
Una de las empresas que ha contratado la utilización de sistema de IA para la promoción de empleados, siguiendo las indicaciones presentes en este apartado para el responsable del despliegue, decide que aquel personal que va a operar con el sistema de IA reciba una formación que le permita entender, a nivel de operación, el concepto de precisión del sistema y la relación de esta con la finalidad prevista (disponer de un indicador para la promoción de empleados).
Para ello consultan con una empresa especializada en cursos de formación, y siguiendo las instrucciones proporcionadas por el proveedor del sistema de IA sobre precisión, añaden a la formación de uso del sistema unas horas dedicadas a proporcionar adicionalmente la siguiente información:
-
-

El concepto de precisión a alto nivel y su relación con los resultados del sistema dentro de su operativa.
Una explicación a alto nivel de cómo funciona la métrica de precisión seleccionada por el proveedor y su relación con los paneles informativos del sistema.

Esta formación, es complementada con un plan periódico de actualización, para garantizar que se tiene presente el concepto en la operación del sistema.
La transparencia, por tanto, dotará de calidad al modelo, en cuanto al grado de disponibilidad de información sobre el sistema de IA y la manera en que la información es comunicada a las partes relevantes de acuerdo con sus objetivos y saber hacer (en referencia a ISO/IEC 25059,
Software engineering — Systems and software Quality Requirements and Evaluation (73) —
Quality model for AI systems). Dado el contexto de la guía en la que nos encontramos, uno de los aspectos clave para esa información de transparencia, será la información asociada a las métricas de precisión seleccionadas (para más detalle en transparencia consultar la guía de transparencia).
A modo orientativo, se recomienda que el responsable del despliegue capacite a los miembros de su organización que interactúen con el sistema de IA de Alto riesgo para:
26
