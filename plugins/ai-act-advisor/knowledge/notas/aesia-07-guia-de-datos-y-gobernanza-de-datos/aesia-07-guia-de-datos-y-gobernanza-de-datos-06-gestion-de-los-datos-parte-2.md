---
name: aesia-07-guia-de-datos-y-gobernanza-de-datos-06-gestion-de-los-datos-parte-2
description: "AESIA: aesia 07 guia de datos y gobernanza de datos, sección «Gestión de los datos (parte 2)» (págs. 22-29). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-07-guia-de-datos-y-gobernanza-de-datos
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Gestión de los datos (parte 2)"
  paginas: 22-29
  origen: 2026-07-17-aesia-07-guia-de-datos-y-gobernanza-de-datos.pdf
  oficial: false
---
# Gestión de los datos (parte 2)

-

Requisito de calidad mínima

Evaluación del control

Ratio de datos informados
Registros no nulos del dato A /
(no nulos) en el set de datos Registros totales del dato A

0,90

0,98

Completitud

Ratio de datos informados
Registros no nulos del dato B /
(no nulos) en el set de datos Registros totales del dato B

0,90

0,92

0003

Fecha de salida (C) Completitud

Ratio de datos informados
Registros no nulos del dato C /
(no nulos) en el set de datos Registros totales del dato C

0,90

0,94

0004

Fecha de
Consistencia incorporación (B) y
Fecha de salida (C)

Ratio de datos donde la
Registros donde se cumple B<C / regla de consistencia "B<C" Registros totales donde B y C están se cumple correctamente informados

0,90

0,97

ID

Dato

0001

Situación del empleado (A)

Completitud

0002

Fecha de incorporación (B)

Descripción

Definición del control

Información de tiempos de ejecución:
o

-

Tipo de control

Fecha y hora de la última ejecución de cada control:
-

0001: 28/09/2023 a las 16:45

-

0002: 28/09/2023 a las 16:50

-

0003: 28/09/2023 a las 16:55

-

0004: 28/09/2023 a las 17:00

o

La fecha y hora en la que se elaboró el reporte: 28/09/2023

o

La periodicidad de ejecución de los controles: diaria.

o

La periodicidad de ejecución del reporte: semanal.

Responsables en torno al reporte:
o

Responsable de la ejecución de cada control: departamento de IT.

o

Responsable de la evaluación de los resultados de los controles: el responsable del sistema de IA, es decir, recursos humanos.

o

Responsable de la elaboración del reporte: analista del área de recursos humanos.

o

Responsable de la emisión del reporte: emisión automática tras generación vía correo electrónico.

o

Responsable de la recepción y revisión del reporte: director de recursos humanos.

E. Desarrollar las medidas de mejora de la calidad de los datos
Llegados a este punto, habremos definido e implementado los controles de calidad de los datos y elaborado el reporte correspondiente que nos permite analizar si la calidad de nuestros datos es suficiente o no. Lo que conviene hacer ahora es determinar las medidas oportunas para remediar o corregir las incidencias de calidad de los datos identificadas.
En este punto, es posible que nos surjan dudas como, ¿Quién debe remediar las incidencias?, ¿En caso de haber identificado gran número de incidencias como remediaremos todas ellas?, ¿Cuál deberíamos remediar antes?, ¿Debemos tener en cuenta todos los afectados por estos datos?

21

Para tratar de dar respuesta a estas preguntas y facilitar la comprensión del lector del proceso de remediación de la calidad de los datos, a continuación, detallamos algunos de los elementos más relevantes que pueden considerarse:
-

En primer lugar, conviene inventariar todas las incidencias de calidad de los datos identificadas.

-

Después, se recomienda determinar qué datos y que incidencias son las más críticas para el adecuado funcionamiento de nuestro sistema de IA.

-

Seguidamente se puede consultar a todas las partes interesadas (stakeholders)
que pudieran verse afectadas por la incidencia de calidad de estos datos.

-

A continuación, tras haber analizado la criticidad de las incidencias y tras consensuarlo con las partes interesadas, se aconseja establecer un orden de prioridad de remediación de estas incidencias.

-

Finalmente, conviene definir un plan de remediación para cada incidencia identificada, según el orden de prioridad establecido.

Ejemplo
En este ejemplo, trataremos de mostrar, sin entrar en detalle, algunos ejemplos de cada uno de los elementos que se pueden incorporar. No pretende ser un reflejo exhaustivo de lo que sería un proceso completo de mejora de la calidad de los datos.
Supongamos que seguimos con el ejemplo del sistema de IA relacionado con el caso de uso de la promoción de empleados:
-

En primer lugar, documentaremos todas las incidencias de calidad de los datos identificadas (por ejemplo, inventariándolas en una hoja Excel, donde les asignaremos un ID a cada una de ellas, identificaremos el control que la ha detectado, la persona responsable de dicho control, a que procesos impacta la calidad de ese dato, y toda la documentación que consideremos oportuna para ayudarnos a identificar la incidencia, categorizarla y priorizarla).

-

Después, con la información dispuesta en el inventario de incidencias lo que haremos será, tras consensuarlo con los diferentes actores involucrados (por ejemplo, los propietarios de los datos y los desarrolladores de los sistemas de IA)
determinar un orden de prioridad de dichas incidencias según el cual trataremos de remediar cada una de ellas.
Seguidamente, y de forma igualmente conjunta con los actores involucrados y partes interesadas (stakeholders) que pudieran verse afectadas por la incidencia de calidad de estos datos, acordaremos un plan de remedio.

-

22

4.3.2 Transformación de los datos
¿Qué es?
Es el proceso de conversión de los datos a un formato homogeneizado.
¿Cuándo podemos abordarlo?
Se recomienda abordar este proceso cuando dispongamos de datos no homogéneos para su uso en nuestro sistema de IA. Los datos pueden no ser homogéneos por tener diferente formato, por estar expresados en diferentes unidades de medida o por tratarse de índices en diferente escala, entre otros motivos. Esto podrá suceder, por ejemplo, si estamos recabando datos de diversas fuentes diferentes.
¿Cómo podemos abordarlo?
Mediante la homogeneización, normalización o escalado de los datos recabados.

Ejemplo
Seleccionemos para este ejemplo el sistema de IA relacionado con el caso de uso de la promoción de empleados.
Supongamos también que nuestra organización acaba de absorber a otra organización que desarrollaba una actividad similar a la nuestra. En este contexto, deberemos incorporar a los nuevos trabajadores a nuestro sistema de IA de promoción y ascenso para que también analice sus perfiles y su rendimiento.
Por último, supongamos que nuestra organización, ubicada en Europa incorpora la información relativa a los salarios de los empleados en euros, que la organización absorbida es japonesa e incorpora esta información en yenes. Si esta información es utilizada por nuestro sistema de IA para su análisis de promoción de empleados, conviene homogeneizar este dato, por ejemplo, pasando la información de los nuevos trabajadores de yenes a euros.

4.3.3 Agregación de los datos
¿Qué es?
Es el proceso consistente en agrupar datos con el fin de poder analizarlos y facilitar observaciones para extraer conclusiones sobre la información que éstos representan.
¿Cuándo puedo abordarlo?
Es oportuno abordar este proceso cuando necesitemos conocer características de agrupaciones de los datos.
¿Cómo puedo abordarlo?
Mediante la transformación de los conjuntos de datos originales en conjuntos de datos agrupados en función de las características que consideremos oportuno para el análisis

23

que queramos llevar a cabo. Los datos agregados o calculados deberían tener el mismo esquema de control de la calidad de datos.

Ejemplo
Seleccionemos para este ejemplo el mismo sistema de IA de la sección anterior, es decir, el relacionado con el caso de uso de la promoción de empleados. Supongamos ahora que estamos en la fase más incipiente del proceso de desarrollo del sistema de IA y que estamos seleccionando las características (proceso explicado en la sección 4.3.5) de los datos con los que entrenaremos nuestro sistema de IA.
Supongamos también que en este caso específico estamos desarrollando este sistema de IA en el contexto de una empresa de fabricación de un determinado tipo de piezas industriales.
En esta fase de selección de características, queremos incorporar el número medio de piezas procesado por cada empleado al día. Únicamente disponemos para ello de una base de datos que almacena un registro por cada empleado y día de trabajo con el número total de piezas procesadas en cada día.
En este contexto, si finalmente consideramos incorporar esta característica como dato de entrenamiento de nuestro sistema, el cual queremos entrenar con datos a nivel de empleado, deberemos previamente disponer del dato agregado por empleado. Para ello transformaremos la tabla previamente mencionada y la agregaremos por empleado calculando el número medio de piezas fabricado al día. A continuación, se dispone un ejemplo simple de este proceso:
ID empleado
E00001
E00001
E00001
E00002
E00002
E00002
E00003
E00003
E00003

Día
1
2
3
1
2
3
1
2
3

Piezas procesadas
234
259
289
301
297
278
223
245
237

ID empleado
E00001
E00002
E00003

Media de piezas procesadas al día
260,7
292,0
235,0

Teniendo en cuenta que debería aplicarse el esquema de control de la calidad de los datos, en este caso, se podría tener un control que verifique que el número de piezas procesadas al día esté dentro de un rango.

24

4.3.4 Muestreo de los datos
¿Qué es?
Es el proceso mediante el cual se extrae un subconjunto de datos desde un conjunto de datos más grande.

¿Cuándo puedo abordarlo?
Generalmente haremos uso del muestreo de datos cuando necesitemos generar y ejecutar nuestro sistema de IA ágilmente, por ejemplo, para llevar a cabo una prueba que nos permita observar su funcionamiento sin tener que hacer uso del conjunto de datos completo.
También podremos hacer uso del muestreo de datos a la hora de seleccionar los conjuntos de datos de entrenamiento, validación y prueba.
¿Cómo puedo abordarlo?
Existen dos técnicas principalmente conocidas y utilizadas para llevar a cabo un adecuado muestro de datos:
-

Muestreo aleatorio: cada muestra del conjunto de datos tiene la misma probabilidad de ser seleccionada.

-

Muestreo estratificado: los datos se dividen en subgrupos en función de unas características determinadas. Este tipo de muestreo se utiliza, generalmente, para garantizar que cada subconjunto esté adecuadamente representado.

Ejemplo
Seleccionemos para este ejemplo el mismo sistema de IA de la sección anterior, es decir, el relacionado con el caso de uso de la promoción de empleados. También en este caso estamos desarrollando el sistema de IA en el mismo contexto anterior de una empresa de fabricación de un determinado tipo de piezas industriales.
Supongamos ahora que a la hora de analizar los datos para entrenar nuestro sistema de
IA y seleccionar las características que utilizaremos, nos percatamos que las características que necesitamos recoger para entrenar nuestro sistema de IA no son las mismas para todos los grupos de empleados.
Por ejemplo, para los operarios que fabrican piezas industriales necesitamos la característica relacionada con el número de piezas que cada operario procesa. En cambio, para los empleados que trabajan en las oficinas no disponemos de estos datos, ya que no existen. Para este otro subconjunto, utilizaremos otras características para entrenar nuestro sistema, por ejemplo, el volumen de negocio que cada trabajador gestiona.
En este contexto, una solución será utilizar el muestreo estratificado, de forma que dividamos nuestro conjunto de datos en dos subconjuntos, uno con los datos de los

25

operarios de fábrica y el otro con los datos de los operarios de oficina. De este modo podremos entrenar dos sistemas de IA diferentes y utilizaremos cada uno de ellos en los procesos de promoción de los empleados en función de si son de fábrica o de oficina.

26

4.3.5 Creación y selección de características
¿Qué es?
Son los procesos que nos permiten aumentar o reducir la dimensionalidad de nuestro conjunto de datos. Podemos aumentar la dimensionalidad mediante la creación de nuevas características y la reduciremos mediante la selección de un subconjunto de las características disponibles.
¿Cuándo puedo abordarlo?
Se recomienda crear nuevas características cuando requiramos de ellas y no las dispongamos en nuestro conjunto de características. Por otro lado, podemos seleccionar un subconjunto de las características que tenemos disponibles cuando determinemos que únicamente necesitamos algunas de ellas y no todas.
¿Cómo puedo abordarlo?
El proceso de creación de características generalmente lo abordaremos mediante la combinación de algunas de las características disponibles. La selección de características la llevaremos a cabo determinando que características nos interesa utilizar para entrenar nuestro sistema.
También es posible que nos interese deshacernos de aquellas características que puedan ser redundantes o no aporten valor diferencial a nuestro sistema de IA. Para este escenario concreto existen técnicas como el Análisis de Componentes Principales (PCA – Principal
Component Analysis en inglés). Esta técnica nos permite identificar aquellas características que están altamente correlacionadas y que podrían no aportar un valor diferencial si, por ejemplo, estamos entrenando un clasificador basado en redes neuronales.

Ejemplo (creación de características)
Seleccionemos para este ejemplo el sistema de IA de la bomba de insulina inteligente y supongamos que hemos determinado que las características que necesitamos para entrenar nuestro sistema son el nivel de azúcar en sangre, el ritmo cardíaco y volumen de oxígeno en sangre.
Supongamos también que por una limitación de hardware resulta muy difícil obtener el volumen de oxígeno en sangre, lo que resulta generalmente en mediciones imprecisas o incompletas. Por tanto, medir el volumen de oxígeno en sangre no es una solución viable, pero necesitamos obtener estos datos para poder determinar la insulina que necesita el paciente y, por consiguiente, para poder desarrollar nuestro sistema de IA.
¿Qué podemos hacer? Una opción es investigar si existe alguna forma de estimar estos datos.
Supongamos, en este contexto, que existiese una forma muy precisa de estimar el volumen de oxígeno en sangre mediante el uso de otros parámetros que, sí somos capaces de obtener, por ejemplo, el ritmo cardíaco y el volumen de oxígeno en los pulmones. Si tomamos la decisión de incorporar esta característica estimada del volumen de oxígeno en sangre estaremos creando, de esta forma, una nueva característica en nuestro conjunto de datos.

27

Ejemplo (selección de características)
Sigamos con el ejemplo desarrollado para la creación de características. Supongamos ahora que en nuestro conjunto de datos diseñado inicialmente disponíamos además de la característica que representaba el nivel de colesterol. Supongamos también que desarrollamos un Análisis de Componentes Principales sobre nuestro conjunto de datos y observamos que el nivel de colesterol es una característica totalmente correlacionada con el nivel de azúcar en sangre. En este escenario, generalmente, decidiremos prescindir de una de las dos características ya que no nos aportaría un valor diferencial en el entrenamiento de nuestro sistema de IA.

4.3.6 Enriquecimiento de los datos
¿Qué es?
Este proceso consiste en ampliar las características y datos disponibles en nuestro conjunto de datos. El objetivo es tratar de aportar información de valor adicional a la información disponible.
¿Cuándo puedo abordarlo?
El enriquecimiento de los datos supone la incorporación de datos de nuevas fuentes, y es un proceso estrechamente relacionado con el proceso de recopilación de datos detallado en la sección 4.2 (tal y como ya adelantábamos cuando introdujimos el concepto de enriquecimiento de datos en dicha sección). No obstante, cuando hablamos de enriquecimiento de los datos debemos interpretarlo como un proceso posterior a la recopilación de datos inicial, que abordaremos en caso de identificar necesidades de datos o características de éstos adicionales.
¿Cómo puedo abordarlo?
Lo podemos abordar de la misma forma que abordamos el proceso de recopilación de datos (sección 4.2) para las nuevas fuentes de datos que consideremos

4.3.7 Etiquetado de los datos
¿Qué es?
El etiquetado de datos o anotación de datos es el proceso mediante el cual asignamos etiquetas identificativas a los datos que hemos recabado. Por ejemplo, si hemos recabado datos para desarrollar un clasificador de imágenes de animales, es el proceso mediante el cual le asignamos la etiqueta que identifica el tipo de animal que contiene cada una de las imágenes.

28
