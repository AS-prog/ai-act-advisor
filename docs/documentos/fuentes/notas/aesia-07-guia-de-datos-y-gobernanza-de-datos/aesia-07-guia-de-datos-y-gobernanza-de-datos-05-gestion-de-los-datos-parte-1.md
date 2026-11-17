---
name: aesia-07-guia-de-datos-y-gobernanza-de-datos-05-gestion-de-los-datos-parte-1
description: "AESIA: aesia 07 guia de datos y gobernanza de datos, sección «Gestión de los datos (parte 1)» (págs. 14-21). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-07-guia-de-datos-y-gobernanza-de-datos
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Gestión de los datos (parte 1)"
  paginas: 14-21
  origen: 2026-07-17-aesia-07-guia-de-datos-y-gobernanza-de-datos.pdf
  oficial: false
---
# Gestión de los datos (parte 1)

4. Gestión de los datos
En este apartado de la guía se van a desarrollar en detalle las etapas del modelo de gestión de datos presentados en la introducción.

4.1 Requisitos de información
¿Qué es?
Es el proceso consistente en establecer con qué información necesitamos alimentar nuestro sistema de IA para lograr el objetivo para el que éste ha sido diseñado.
¿Cómo puedo abordarlo?
Todo sistema de IA se crea con un objetivo o finalidad, por ejemplo, dar solución a un problema existente o cubrir una necesidad identificada. Esta será la primera fase del ciclo de vida de un sistema de IA. En lo que respecta a los datos, lo primero que conviene hacer es identificar qué información necesitamos para cubrir esa necesidad o resolver ese problema.

Ejemplo
Tomando como ejemplo el sistema de IA de la bomba de insulina inteligente, el primer paso será analizar la solución que queremos implementar y el objetivo que buscamos alcanzar, que en este caso es determinar la cantidad de insulina que un paciente diabético necesita en un momento determinado. Así, los datos que necesitaremos recabar, por ejemplo, serán el nivel de azúcar en sangre, el ritmo cardíaco o volumen de oxígeno en sangre.

4.2 Recopilación de los datos
¿Qué es?
Es el proceso consistente en obtener los datos que contengan la información necesaria para el desarrollo de nuestro sistema de IA, que serán los datos que alimentarán nuestro sistema de IA para lograr el objetivo para el que éste ha sido diseñado.
¿Cómo puedo abordarlo?
El proceso de recopilación de datos, generalmente, se lleva a cabo mediante la extracción de datos de diferentes fuentes y este es un elemento especialmente relevante. ¿Por qué?
Porque la precisión y calidad de la solución que desarrollemos mediante nuestro sistema de IA dependerá, entre otros elementos, de lo representativos y suficientes que sean estos datos (la cantidad, suficiencia, completitud y adecuación de los datos, junto con otros elementos relacionados, los trataremos más en detalle en la sección 4.3).

13

Por ello, si recabamos datos de una única fuente de información corremos el riesgo de que la precisión de nuestro sistema de IA genere ciertas dependencias con dicha fuente de datos. Es decir, que obtengamos buenos resultados cuando utilicemos datos de dicha fuente para probar nuestro sistema, pero nos encontremos con un escenario de precisión totalmente diferente si probamos nuestro sistema con datos de una fuente nueva. En otras palabras, si entrenamos nuestro sistema con datos sesgados, corremos el riesgo de obtener un sistema que toma decisiones sesgadas (para más detalle de los sesgos en los datos, ver sección 4.3.8).
Por otro lado, uno de los problemas habituales es tener múltiples repositorios de la misma información. Para ello, es recomendable seleccionar la base más fiable (fuente de la verdad) con Data Owner y un modelo de control de la calidad en el origen del dato (no solo en el repositorio que aprovisiona el modelo).

Ejemplo
Tomemos ahora como ejemplo el sistema de IA de registro de la asistencia al trabajo mediante reconocimiento biométrico. Si, por ejemplo, entrenamos este sistema con imágenes sesgadas por género y raza, existe un alto riesgo de que el sistema también muestre sesgos y discriminación en su comportamiento.
Por ejemplo, si utilizamos principalmente imágenes de hombres blancos para entrenar el sistema de reconocimiento facial, es probable que el sistema tenga dificultades para reconocer y clasificar con precisión a personas de otros géneros y razas. Esto podría llevar a que el sistema cometa errores en la identificación de personas de ciertas razas o géneros, y por lo tanto a una discriminación por parte del sistema.

En este contexto, existen diferentes métodos y vías mediante las que podemos abordar el proceso de recopilación de datos. En el Anexo A se muestra un listado detallado de algunos de estos métodos y vías, con el fin de ofrecer al lector de esta guía algunos ejemplos representativos.
Es importante destacar que el proceso de recopilación de datos está estrechamente relacionado con los procesos de evaluación de la disponibilidad, cantidad y adecuación de los datos detallados en la sección 4.3. Una vez abordamos estos procesos, es aconsejable analizar si es necesario reevaluar o modificar el proceso de recopilación de datos (por ejemplo, incorporando datos de nuevas fuentes). Este proceso de incorporación de nuevos datos de fuentes adicionales tiene un nombre específico y es el proceso de enriquecimiento de los datos que detallaremos en la sección 4.3.6.
Adicionalmente, hay que señalar que el proceso de recopilación de datos y las fuentes que finalmente se seleccionen dependerá de la necesidad a cubrir y del contexto de la implementación de cada sistema de IA. También es conveniente tener en especial

14

consideración la normativa aplicable en materia de protección de datos de carácter personal1.

4.3 Preparación de los datos
¿Qué es?
Es la fase de procesado y acondicionamiento de los datos recopilados en la fase anterior para su disposición y uso en el sistema de IA.
¿Cómo puedo abordarlo?
Este procesado y acondicionamiento de los datos está compuesto, generalmente, por un conjunto de operaciones que podremos llevar a cabo en función de la naturaleza de los datos que hemos recabado en la fase anterior. Es decir, hemos recabado unos datos y necesitamos acondicionarlos para poder utilizarlos y para ello es recomendable abordar una secuencia de tratamientos en función de cómo estén esos datos.
En las siguientes subsecciones, vamos a describir las principales operaciones o tratamientos que completan esta fase de preparación de los datos.
En cada sección abordaremos, qué es cada elemento y cómo podemos abordarlo.
Adicionalmente, incluiremos la reflexión de cuándo podemos abordarlo, esto se debe a que no siempre deberemos enfrentarnos a cada uno de los procesos indicados en esta sección, dependerá de las circunstancias y eso es lo que trataremos de resolver en dicho apartado.

4.3.1 Medición y mejora de la calidad de los datos
¿Qué es?
La calidad de los datos es el grado de adecuación de los datos al propósito para el que han sido definidos o recabados. La medición de la calidad de los datos consiste en analizar cuánto se adecúan los datos a dicho propósito. La mejora es el proceso que nos permite ajustar el grado de adecuación de los datos a su propósito, es decir, nos permite aumentar la calidad de los datos.
Maximizar la calidad de los datos es, sin lugar a duda, uno de los elementos más importantes en el proceso de preparación de los datos.
¿Cuándo puedo abordarlo?
La medición de la calidad de los datos y la consecuente mejora de aquellos que no dispongan de una calidad suficiente es un proceso imprescindible en un adecuado gobierno de los datos. Como veremos en las siguientes fases y como hemos comentado
1

Reglamento (UE) 2016/679 del Parlamento Europeo y del Consejo, de 27 de abril de 2016, relativo a la protección de las personas físicas en lo que respecta al tratamiento de datos personales y a la libre circulación de estos datos y por el que se deroga la Directiva 95/46/CE (Reglamento general de protección de datos); Ley Orgánica 3/2018, de 5 de diciembre, de
Protección de Datos Personales y garantía de los derechos digitales; Ley Orgánica 7/2021, de 26 de mayo, de protección de datos personales tratados para fines de prevención, detección, investigación y enjuiciamiento de infracciones penales y de ejecución de sanciones penales.

15

previamente, conviene abordar cada una de ellas en función de una serie de circunstancias que analizaremos en cada caso. No obstante, la medición y mejora de la calidad de los datos no es un proceso opcional o que dependa de las circunstancias, sino que debe estar siempre presente y adecuadamente implementado en nuestro sistema de gobernanza de datos.
¿Cómo puedo abordarlo?
La forma idónea de abordar todo proceso de medición y mejora de la calidad de los datos es estableciendo una metodología de calidad de datos adecuada. En esta sección pretendemos acompañar al lector de la guía en el proceso de desarrollo de su metodología de calidad de datos. Para ello, detallaremos a continuación las fases que se recomienda afrontar en este proceso:
A. Determinar las dimensiones de calidad a evaluar
El primer paso es determinar cuáles son las dimensiones de calidad que vamos a evaluar para nuestros datos. Para ello, debemos conocer y comprender cuales son estas dimensiones y después determinar cuáles de ellas necesitamos para que nuestros datos tengan la calidad adecuada para cumplir su función. Es importante destacar que conviene abordar este ejercicio para cada uno de los datos cuya calidad queramos garantizar, es decir, las dimensiones de calidad han de analizarse de forma individual para cada dato.
Para facilitar esta tarea, en el Anexo B.1 se disponen y se detallan algunos ejemplos de las dimensiones de calidad de los datos más comunes y relevantes (tales como la completitud, representatividad, auditabilidad, consistencia, relevancia, diversidad o credibilidad).
En este contexto, lo primero que deberemos hacer es seleccionar cuáles de estas dimensiones (u otras que nuestra organización considere y no estén en el inventario facilitado en el Anexo B.1) necesitamos para que cada uno de nuestros datos tengan la calidad adecuada para cumplir su función. Por ejemplo, es bastante probable que la dimensión de completitud sea necesaria para todos nuestros datos. Sin embargo, la dimensión de consistencia entre datos será necesaria únicamente en ciertos casos, por ejemplo, si tenemos dos datos que representan fechas relacionadas entre sí (la fecha de entrada a una infraestructura deberá ser menor que la fecha de salida).

Ejemplo
Seleccionemos para este ejemplo el sistema de IA relacionado con el caso de uso de la promoción de empleados, supongamos que somos una organización que decide desarrollar este sistema de IA que analiza los perfiles y el rendimiento de los trabajadores y nos ayuda a determinar quién merece en mayor medida un ascenso.
Supongamos también que nos disponemos a determinar las dimensiones de calidad de los datos que nuestro sistema de IA utiliza, entre ellos se encuentran los datos
“fecha de incorporación a la empresa”, “situación del empleado” y “fecha de salida de la empresa” de los empleados, y decidimos empezar a definir las dimensiones de calidad para éstos.

16

Ahora, lo que resulta conveniente preguntarse es lo siguiente: ¿Qué dimensiones de calidad necesito que tengan mis datos para que éstos cumplan su objetivo y mi sistema de IA funcione adecuadamente? Comencemos seleccionando para desarrollar este ejemplo, dos de las dimensiones dispuestas en el Anexo B.1,
“Completitud” y “Consistencia”. Nosotros, que conocemos nuestro objetivo y nuestros datos, determinamos que los datos “situación del empleado” y “fecha de incorporación a la empresa” deben estar siempre informados ya que todo empleado debe disponer de una fecha de incorporación y una situación (por ejemplo, activo, de baja, exempleado). En cambio, el dato “fecha de salida de la empresa” únicamente estará informado para aquellos exempleados que ya no estén en nuestra organización. En cuanto a la “Consistencia”, tenemos varias relaciones que han de cumplirse entre estos datos. Por ejemplo, si el dato “fecha de salida de la empresa” está informado, entonces el dato “situación del empleado” únicamente podrá tomar el valor “exempleado”. Además, el dato “fecha de salida de la empresa” tiene que ser mayor que el dato “fecha de incorporación a la empresa”.

B. Definir los controles de calidad a implementar para cada dimensión
Una vez identificadas las dimensiones de calidad de nuestros datos, lo que podemos hacer es definir los controles de calidad de los datos para cada requisito. Definir un control de calidad consiste en establecer una métrica que nos aporte la información que necesitamos obtener acerca del estado de la calidad de nuestro dato.
La selección de las dimensiones de calidad podía ser una tarea relativamente sencilla puesto que generalmente dependerá de la propia naturaleza de los datos, como hemos visto en la fase anterior. Sin embargo, es probable que llegados a este punto nos preguntemos, ¿qué controles he de definir?, y, ¿cuántos deberé definir? De nuevo la respuesta va ligada al objetivo de este ejercicio que es garantizar que cada uno de nuestros datos tengan la calidad adecuada para cumplir su función.Para ello, resulta útil analizar y determinar qué controles son los adecuados en cada caso para poder conseguir este objetivo.
Para facilitar esta tarea, en el Anexo B.2 se disponen y se detallan algunos ejemplos de controles de calidad de los datos más comunes y relevantes para cada una de las dimensiones detallados en el Anexo B.1. Adicionalmente, se incorpora también el detalle de cómo definirlos en cada caso.

Ejemplo
Siguiendo con el ejemplo descrito en la fase anterior, estamos analizando ahora qué controles necesitamos para el requisito de completitud de los datos “situación del empleado”, “fecha de incorporación a la empresa” y “fecha de salida de la empresa” y para el requisito de consistencia entre los dos últimos. Apoyándonos en el inventario de controles facilitado en el Anexo B.2 decidimos definir los siguientes controles para garantizar la calidad de nuestros datos:

17

ID
0001

Dato
Situación del empleado (A)

Tipo de control
Descripción
Definición del control
Completitud
Ratio de datos informados
Registros no nulos del dato A /
(no nulos) en el set de datos Registros totales del dato A

0002

Fecha de incorporación (B)

Completitud

Ratio de datos informados
Registros no nulos del dato B /
(no nulos) en el set de datos Registros totales del dato B

0003

Fecha de salida (C) Completitud

Ratio de datos informados
Registros no nulos del dato C /
(no nulos) en el set de datos Registros totales del dato C

0004

Fecha de
Consistencia incorporación (B) y
Fecha de salida (C)

Ratio de datos donde la
Registros donde se cumple B<C / regla de consistencia "B<C" Registros totales donde B y C están se cumple correctamente informados

Adicionalmente, es importante destacar que la definición de los controles de calidad de los datos conviene abordarla en cada uno de los puntos del ciclo de vida de los datos en los que consideremos oportuno para garantizar que llegan con la calidad adecuada cuando son utilizados por nuestro sistema de IA.

Ejemplo
Supongamos que descargo los datos de una fuente de datos abierta y los vuelco sobre una hoja Excel. Esta hoja Excel la cargo directamente en una base de datos en
SQL y de ahí hago una extracción sobre mi plataforma de Python donde tengo implementado mi sistema de IA. En este ciclo de vida tenemos nuestros datos en tres repositorios diferentes y para ello tienen lugar tres procesos diferentes, supongamos los siguientes:
a) Descarga de internet a la hoja Excel.
b) Carga de la hoja Excel a base de datos SQL.
c) Extracción de una selección de los datos de la base de datos SQL a plataforma Python.
La definición de los controles de calidad podrá ser diferente en función del repositorio. Retomando por un momento el ejemplo anterior, si al pasar de “b)” a
“c)” ya no seleccionamos la “fecha de incorporación a la empresa”, en el punto “b)” podremos definir los controles mencionados en el ejemplo anterior, pero en “c)” ya no podremos definir los controles que implicaban al dato que no hemos seleccionado.

En este contexto, conviene decidir en qué puntos de ese ciclo de vida debemos definir y posteriormente implementar los controles de calidad.Para determinarlo, es recomendable analizar nuestro ciclo de vida y las necesidades que consideremos oportunas para garantizar la calidad de nuestros datos. En cuanto a medición de la calidad de los datos, idealmente debería realizarse en los repositorios origen. A partir de ahí los controles en las diferentes capas o puntos del ciclo de vida deberían estar más focalizados a la calidad del proceso (es decir, que los datos se hayan copiado/ingestado/transferido correctamente; siendo por tanto controles más de nivel

18

técnico y no tanto funcionales). Con esto se evita la duplicidad de los mismos controles en diferentes capas y la dificultad que conlleva para su gestión y remediación.
En el ejemplo anterior, es un ciclo de vida muy corto y es posible que tengamos capacidad de definir e implementar controles de calidad en todos los puntos. Pero ¿Y si tenemos un ciclo de vida mucho mayor? Entonces se recomienda determinar qué puntos son los más críticos y cuáles son los que nos permiten garantizar mejor la calidad de nuestros datos.
Por último, conviene determinar para cada control los requisitos de calidad necesarios, esto nos permitirá evaluar si la calidad de nuestros datos es suficiente o no. Por ejemplo, si la completitud de una de las características del conjunto de datos que alimenta nuestro sistema de IA es imprescindible, deberemos establecer un requisito de calidad para el control de completitud de ese dato del 100%.
C. Implementar los controles definidos
La siguiente fase es implementar los controles de calidad definidos en la fase anterior.
Consiste en desarrollar técnicamente los controles que hemos definido, es decir, traducir las reglas definidas al lenguaje técnico de cada punto del ciclo de vida del dato. Por ello, este ejercicio dependerá del tipo de plataforma y lenguaje sobre los puntos en los que hayamos definido los controles. A continuación, listamos algunos ejemplos con el fin de ayudar al lector a comprender mejor este proceso:

Ejemplo
Supongamos que hemos definido los controles de calidad indicados en el ejemplo anterior y que los hemos definido para los tres puntos del ciclo de vida del dato especificados en dicho ejemplo. En este contexto, podemos ahora implementar estos controles y, tal y como hemos explicado, el cómo lo hagamos dependerá de cada tipo de plataforma.
En este contexto, podremos implementar las reglas que nos permitan contar el número de registros informados (no nulos) y las reglas que nos permitan comparar los registros de las fechas de incorporación y salida en el lenguaje de cada uno de estos puntos, así:
a) Implantación de controles en Excel -> utilizaremos Macros de Excel y el lenguaje VBA.
b) Implantación de controles en SQL -> utilizaremos el propio lenguaje de SQL.
c) Implantación de controles en Python -> utilizaremos el propio lenguaje de
Python.

D. Reportar los resultados de los controles
En las fases anteriores nos hemos encargado de definir e implementar los controles de calidad de los datos, es decir, hemos dispuesto los medios oportunos para la medición de la calidad de nuestros datos.

19

Llegados a este punto, la siguiente tarea será reportar los resultados de los controles y disponer estos resultados adecuadamente para llevar a cabo el análisis del grado de adecuación de los datos al propósito para el que han sido definidos o recabados, es decir, de su calidad.
Para ello, lo que tendremos que hacer es determinar cómo queremos reportar estos resultados y que información queremos incorporar en estos reportes. Para facilitar esta tarea, detallamos a continuación algunos de los elementos más relevantes que puede contener un adecuado reporte de calidad de los datos:
-

Contexto del reporte: en esta sección explicaremos el ámbito y contexto del reporte y el objetivo que pretende cubrir.

-

Información que se reporta: qué datos están incorporados, la definición de los controles de calidad reportados, los requisitos de calidad de cada control, la valoración de la calidad de los datos, así como cualquier información o detalle adicional que se considere necesario.
Información de tiempos de ejecución: la fecha y hora en la que se ha ejecutado cada control, la fecha y hora en la que se elaboró el reporte, la periodicidad de ejecución de los controles, la periodicidad de ejecución del reporte, así como cualquier información relacionada con periodicidades y momentos de ejecución que se considere necesario.

-

-

Responsables en torno al reporte: entre ellos destacan: responsable de la ejecución de cada control, responsable de la evaluación de los resultados de los controles, responsable de remediación, responsable de la elaboración del reporte, responsable de la emisión del reporte, responsable de la recepción y revisión del reporte.

-

Condiciones de almacenamiento del reporte: deberá informarse la ubicación de almacenamiento del reporte, para cualquier consulta posterior.

Ejemplo
En este ejemplo trataremos de disponer, sin entrar en detalle, algunos ejemplos de cada uno de los elementos a incorporar. No pretende ser un reflejo exhaustivo de lo que sería un reporte completo de los resultados de la evaluación de la calidad de los datos.
Supongamos que seguimos con el ejemplo del sistema de IA relacionado con el caso de uso de la promoción de empleados:
-

-

Contexto del reporte: este reporte representa un informe donde se recogen los resultados de los controles de calidad de los datos que alimentan el sistema de IA de promoción de empleados. El objetivo principal de este reporte es proporcionar una evaluación transparente y precisa de la confiabilidad de los datos utilizados por el sistema.
Información que se reporta:

20
