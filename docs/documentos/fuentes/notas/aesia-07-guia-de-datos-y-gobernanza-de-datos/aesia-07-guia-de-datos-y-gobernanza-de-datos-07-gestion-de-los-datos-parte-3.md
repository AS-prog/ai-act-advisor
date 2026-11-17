---
name: aesia-07-guia-de-datos-y-gobernanza-de-datos-07-gestion-de-los-datos-parte-3
description: "AESIA: aesia 07 guia de datos y gobernanza de datos, sección «Gestión de los datos (parte 3)» (págs. 30-37). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-07-guia-de-datos-y-gobernanza-de-datos
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Gestión de los datos (parte 3)"
  paginas: 30-37
  origen: 2026-07-17-aesia-07-guia-de-datos-y-gobernanza-de-datos.pdf
  oficial: false
---
# Gestión de los datos (parte 3)

¿Cuándo puedo abordarlo?
Lo podemos abordar en caso de que, para desarrollar nuestro sistema de IA, precisemos de datos etiquetados y no dispongamos de dichas etiquetas en las fuentes que alimentan nuestro conjunto de datos.
Si atendemos a los tipos más comunes de aprendizaje automático, los datos etiquetados son necesarios en el desarrollo de sistemas de IA basados en aprendizaje supervisado (por ejemplo, clasificadores de imagen). En cambio, los sistemas de IA basados en aprendizaje no supervisado no precisan de datos etiquetados (por ejemplo, segmentaciones de grupos de datos relacionados).
¿Cómo puedo abordarlo?
Las tareas de etiquetado de datos son, generalmente, costosas en tiempo y recursos. Esto se debe a que normalmente precisamos de grandes cantidades de datos para desarrollar nuestros sistemas de IA. Es cierto que también existen herramientas para el etiquetado automático de los datos, no obstante, conviene valorar si debemos incorporar algún tipo de vigilancia humana a dicho proceso (HITL – Human In The Loop) que nos garantice que el etiquetado se adecua a nuestras necesidades (para más detalle de los procesos de vigilancia humana, consultar guía del artículo vigilancia humana).
A continuación, detallamos algunos de los enfoques de etiquetado de datos más comunes:
-

Etiquetado interno: en este caso abordarán el proceso de etiquetado los expertos encargados de los sistemas de IA dentro de la organización. Es una metodología que nos proporcionará garantías en precisión y calidad ya que controlamos internamente todo el proceso, pero también es el tipo de etiquetado que más recursos nos consumirá de forma directa.

-

Etiquetado externo: en este caso contratamos expertos externos a nuestra organización para llevar a cabo las tareas de etiquetado de los datos. Esta opción puede ser especialmente interesante para procesos de etiquetado de alto volumen de trabajo en intervalos cortos de tiempo. No obstante, nos supondrá un coste económico mayor directo que la opción de etiquetado interno.

-

Etiquetado mediante “crowdsourcing”: este enfoque se basa en un proceso de etiquetado de datos distribuido en la web. Existen plataformas que se encargan de diseñar y ofrecer estos servicios. Esta solución es quizá la más eficiente y rentable de todas las descritas, no obstante, no nos aporta las mismas garantías de calidad y precisión que el etiquetado interno ni tenemos un contrato de por medio con una organización que responda en caso de que suceda algún tipo de incidencia.
Adicionalmente, se debe contemplar que el envenenamiento de los datos de entrenamiento supone un posible vector de ataque a nuestro sistema (Ver Guía de
Ciberseguridad).
Etiquetado automático: Este enfoque se basa en un proceso automático que etiqueta los datos en base a un conjunto de reglas definido o en base a un valor almacenado y asociado al objetivo del modelo. La vigilancia humana se realiza en base a una muestra aleatoria y representativa de los registros etiquetados: si hay un número de discrepancias significativas entre lo que habría etiquetado un humano y

-

29

lo que etiqueta el proceso automático se revisa el sistema de reglas o la idoneidad del etiquetado automático. Dicho etiquetado debería acompañarse de suficiente validación y supervisión de forma que se mitigue el riesgo de sesgo y deriva. En este sentido la integración de agentes de IA en marcos de gobernanza de datos como la UNE 0085 y el Reglamento de Gobernanza de Datos (DGA) puede impulsar la innovación al automatizar tareas de gestión y cumplimiento. No obstante, exige una gobernanza específica que garantice transparencia, trazabilidad y supervisión humana. La literatura propone modelos híbridos humano-máquina y arquitecturas de alineación para auditar decisiones automatizadas.

Ejemplo
Supongamos que retomamos el ejemplo del sistema de IA relacionado con el caso de uso de la promoción de empleados. Supongamos que ya hemos seleccionado las características necesarias y recabado el conjunto de datos históricos de los empleados con el que pretendemos entrenar nuestro sistema de IA. Dicho sistema de IA consistirá en un clasificador que nos ayudará a determinar si un empleado debe ser promocionado o no.
En este supuesto, necesitamos incorporar a nuestro conjunto de datos una característica adicional que será la etiqueta utilizada por el sistema de aprendizaje supervisado que entrenaremos. Esta etiqueta consistirá en una marca binaria que identificará si el empleado debe ser promocionado o no.
¿A partir de que información construiremos esa etiqueta? Pues a partir de las características que hemos seleccionado para entrenar nuestro sistema por ser aquellas determinantes para decidir si un empleado debe ser promocionado. Suponemos que el proceso es suficientemente complejo como para necesitar de una evaluación específica de un experto para cada caso concreto (en caso contrario no necesitaríamos entrenar este tipo de sistema y podríamos definir un conjunto de reglas simples).
¿Quién abordará dicha evaluación de cada caso e incorporará la etiqueta de promoción?
Aquí podríamos elegir entre cualquiera de las alternativas explicadas anteriormente. Por ejemplo, podemos suponer un escenario donde nuestra organización dispone de un gran equipo de científicos de datos y en este caso serán ellos quienes se hagan cargo de esta tarea tras alinear una serie de criterios con el departamento de recursos humanos quienes tienen el conocimiento específico de los datos utilizados para la evaluación de los empleados.

4.3.8 Análisis de sesgos en los datos
¿Qué es el sesgo en los datos?
El sesgo es la tendencia o potencial error sistemático al que podríamos incurrir si tuviéramos un desequilibrio en los datos. Éste se produce cuando se sobre ponderan o sobre representan determinados elementos de un conjunto de datos.

30

Ejemplo
Por ejemplo, si entrenásemos nuestro sistema de IA, previamente descrito, de promoción de empleados con datos históricos de cargos directivos entre los años 1900 y 2000, la gran mayoría de casos de promoción exitosa de los que aprendería el sistema sería de personas de género masculino. Si tratamos de utilizar este sistema (entrenado con los datos mencionados) en el contexto actual, podríamos obtener que todos los casos de promoción de empleados propuestos son de personas de género masculino, pues nuestro conjunto de datos estaba sesgado por esta característica y las decisiones de nuestro sistema podrían quedar condicionadas en esta dirección.

¿Cuándo puedo abordarlo?
El análisis de sesgos en los datos, al igual que la medición y mejora de la calidad de los datos, es un proceso imprescindible en un adecuado gobierno de los datos. Como hemos visto en las fases anteriores, debemos atender a unas circunstancias específicas para determinar cuándo abordaremos cada una de ellas. No obstante, el análisis de sesgos en los datos no es un proceso opcional o que dependa de las circunstancias, sino que debe estar siempre presente y adecuadamente implementado en nuestro sistema de gobernanza de datos.
¿Cómo puedo abordar el análisis del sesgo?
El objetivo del análisis del sesgo en los datos es tener la capacidad de identificar y evaluar el potencial sesgo que puedan presentar nuestros datos y cómo podría impactar en el desarrollo de nuestro sistema de IA. También, el poder determinar la necesidad de incorporar medidas que mitiguen dicho impacto.
Hacemos especial énfasis en definir este objetivo ya que es importante destacar que el sesgo en los datos no es un elemento puramente negativo o nocivo que debamos tratar siempre de eliminar o mitigar. Lo que es importante es tener la capacidad de identificarlo y evaluar su impacto.

Ejemplo
Siguiendo el ejemplo anterior, el impacto en el proceso de selección sería negativo para las personas de género diferente al masculino. Lo más importante es que debemos entender que este es un sesgo inherente de los datos históricos que hemos recabado, es decir, los datos no son incorrectos o contienen errores, simplemente representan un desequilibrio con respecto a una característica (en este caso el género).

¿Debemos corregir ese desequilibrio en nuestros datos? Esta es una pregunta que conviene abordar en cada contexto y escenario concretos, no existe una respuesta o solución global para todos los casos.

31

Lo que sí podemos hacer es tratar de diseñar un proceso que describa los pasos que deberemos dar a la hora de enfrentarnos a un análisis de los sesgos y es lo que trataremos de abordar en esta sección de la guía. Este proceso lo dividimos en tres fases que detallamos a continuación, de forma orientativa:
1. Análisis de las principales fuentes de sesgo en los datos: Lo primero que podemos hacer es conocer y comprender cuales son las principales fuentes de sesgo en los datos, es decir, los elementos principales que pueden provocar que mis datos estén sesgados. Para facilitar esta tarea, en el Anexo C.1 se disponen y se detallan algunos ejemplos de las fuentes de sesgo más relevantes.
2. Evaluación del sesgo en los datos: En segundo lugar, podemos hacer uso de las principales técnicas de evaluación del sesgo en los datos. Estas técnicas nos ayudarán a identificar si existe algún tipo de sesgo en nuestros datos y medir y valorar su impacto. Del mismo modo que en la fase anterior, se facilita en el Anexo C.2 un listado detallado de las técnicas más relevantes de evaluación del sesgo en los datos.
3. Tratamiento del sesgo en los datos: Por último, se recomienda determinar la necesidad de implementar medidas de tratamiento de los sesgos identificados y evaluados. Estas medidas nos ayudarán a mitigar el impacto de los sesgos presentes en nuestros datos. Así mismo, en el Anexo C.3 se detallan las medidas de tratamiento del sesgo más relevantes.

4.4 Disposición de los datos
¿Qué es?
Es el proceso consistente en proporcionar los datos, tras pasar por todos los procesos de preparación detallados en las secciones anteriores, para su uso en el sistema de IA.
¿Cómo puedo abordarlo?
En la primera fase del proceso, determinamos los requisitos de información que necesitamos para desarrollar nuestro sistema de IA, después recabamos los datos que contienen y representan dicha información, posteriormente los procesamos y preparamos los datos y ahora se aconseja disponerlos para su adecuado uso en el desarrollo del sistema de IA.
La disposición de los datos consiste en proporcionarlos una vez los hemos preparado, mediante las herramientas técnicas oportunas. Del mismo modo que cuando implantábamos los controles de calidad (donde veíamos como dependía del tipo de plataforma y lenguaje sobre los puntos en los que habíamos definido los controles) el proporcionar los datos dependerá de donde vayamos a implementar nuestro sistema de
IA.

32

Ejemplo
Por ejemplo, supongamos que en la fase de recopilación de datos partíamos de una descarga en una hoja Excel de una fuente de datos abierta, supongamos también que posteriormente cargábamos dicha hoja Excel en nuestra plataforma de Python y allí desarrollábamos todos los procesos de preparación de los datos mediante código en
Python.
Supongamos ahora que hemos diseñado nuestro sistema de IA de forma que únicamente puede ser alimentado mediante una base de datos relacional en SQL para poder garantizar las medidas de seguridad e integridad de la información adecuadas.
En este contexto, para disponer adecuadamente de los datos y que puedan ser utilizados por el encargado de desarrollar el sistema de IA (que podemos ser nosotros mismos)
deberemos cargar los datos en esta base de datos relacional en SQL.

Adicionalmente, también existen otros elementos que conviene considerar para el adecuado desarrollo del proceso de disposición de datos:
-
-
-
-
-

-
-

-
-

Especificar el propio proceso de disposición de datos, dónde se almacenan los datos y cómo debemos acceder a ellos adecuadamente.
Implementar los procesos de autenticación y acceso a los datos.
Documentar y mantener un proceso de control de versiones de los procesos de disposición de los datos.
Mantener un registro de las diferentes actualizaciones de los datos que se dispongan.
Informar acerca de los procesos desarrollados hasta la disposición de los datos:
o Evaluación de requisitos de la información.
o Recopilación de datos.
o Preparación de datos (procesos de medición y mejora de la calidad de datos, transformación, agregación y muestreo de los datos, creación y selección de características, enriquecimiento y etiquetado de los datos y análisis de sesgos).
Informar acerca de la posible presencia de datos personales o de categorías especiales de datos personales (ver sección 5.1).
Informar acerca de las medidas de seguridad y protección de la privacidad (como la seudonimización o la anonimización) que hayan sido implementadas (ver sección
5.1).
Informar acerca de posibles usos indebidos y razonablemente previsibles de los datos dispuestos.
Documentar todo detalle adicional de los datos y metadatos necesario para facilitar la comprensión de éstos y su uso adecuado para el desarrollo del sistema de IA (por ejemplo, la distribución y propiedades estadísticas de los datos, los tipos de datos, el formato de los datos o las fechas de adquisición y actualización de los datos).

33

4.5 Eliminación de los datos
¿Qué es?
Es la última fase del ciclo de vida de los datos, consistente en la retirada de los datos que han sido dispuestos y utilizados para desarrollar el sistema de IA.
¿Cómo puedo abordarlo?
El proceso de eliminación de los datos que hayamos dispuesto y utilizado para el desarrollo de nuestro sistema de IA, generalmente lo llevaremos a cabo, bien mediante la eliminación de estos, o bien mediante su transferencia, tal y como detallamos a continuación.
Para la trasferencia de datos, podemos:
-

-
-
-

Identificar un destinatario que presente las garantías adecuadas para asumir la responsabilidad de custodiar los datos con las respectivas obligaciones legales y contractuales asociadas.
Documentar un acuerdo expreso con el destinatario según el cual acepta hacerse cargo de los datos y las obligaciones asociadas.
Asegurarnos de que la transferencia de datos no supone una violación de ninguna obligación legal, contractual o de retención de datos.
Generar un informe con todo el detalle del proceso de transferencia de datos abordado.

Para la eliminación de los datos, podemos:
-

-
-
-

-

Asegurarnos de que no hay ningún usuario o actor involucrado en el desarrollo del sistema de IA que requiera todavía de acceso a los datos por un motivo o fin determinado.
Asegurarnos de que el proceso de eliminación de datos que vayamos a llevar a cabo no viole ninguna obligación legal, contractual o de retención de datos.
Garantizar que quedan eliminados de todas las ubicaciones donde pudieran estar almacenados.
Evaluar si existe alguna posibilidad de restauración de los datos, parcial o total, a partir del sistema de IA entrenado con estos datos. En este caso, deberemos documentarlo adecuadamente y considerarlo en el proceso de eliminación de datos.
Revisar si los datos tienen algún tipo de importancia cultural, social o histórica. En tal caso, debemos documentar y detallar por qué no optamos por la transferencia de los datos a un destinatario que pueda mantener todas las obligaciones de datos y su importancia.

34

-
-

Revisar si es posible y aporta valor la donación de los datos al dominio público. Ésta puede beneficiar a diferentes campos de investigación.
Generar un informe con todo el detalle del proceso de eliminación de datos abordado.

Adicionalmente, deberemos disponer de los medios adecuados para gestionar las posibles solicitudes específicas de eliminación parcial de datos. Como es conocido, algunas regulaciones como GDPR, pueden obligarnos a eliminar conjuntos específicos de datos en diferentes escenarios y contextos. Con respecto a este proceso de eliminación parcial de datos, deberemos:
-
-

-
-

Evaluar el impacto de esta eliminación de datos parcial sobre el conjunto de datos restante, sus especificaciones y su calidad.
Si los datos restantes han dejado de cumplir con sus especificaciones y propiedades, deberemos documentar e informar a todas las partes interesadas de este suceso y tratar de proporcionar medidas mitigadoras.
Garantizar que los datos que han sido eliminados quedan efectivamente eliminados de todas las ubicaciones donde pudieran estar almacenados.
Generar un informe con todo el detalle del proceso de eliminación parcial de datos abordado.

Ejemplo
Siguiendo con el ejemplo del sistema de IA relacionado con el caso de uso de la promoción de empleados, supongamos ahora que recibimos una solicitud de eliminación de datos por parte de un exempleado y, supongamos también, que la ley de protección de datos respalda esta solicitud en concreto en el contexto y circunstancias en las que sucede.
En este escenario deberíamos:
-

-
-

-

Evaluación del impacto sobre el conjunto total de los datos y el funcionamiento del sistema: en este caso se trata de una eliminación de datos específica de un único exempleado y se ha considerado que no tiene un impacto relevante sobre el conjunto total ni sobre el funcionamiento del sistema.
Documentación e información a las partes interesadas: se envía un correo electrónico a las áreas que disponían de estos datos almacenados en sus sistemas.
Estas son recursos humanos y el equipo de Advanced Analytics.
Eliminación de los datos en todas las ubicaciones: se contacta con el área de recursos humanos (owner de los datos) para consultar la traza funcional e identificar todas las ubicaciones en las que el dato estaba almacenado. Después, en colaboración con el equipo de IT se accede a dichas bases de datos y se procede a eliminar los datos.
Generación del informe: se genera un informe con todo el detalle del proceso de eliminación parcial de datos abordado (descripción de la solicitud, evaluación de

35

impacto, ubicaciones en las que se encontraban los datos, fechas y horas de las acciones realizadas).

36
