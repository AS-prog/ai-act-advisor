---
name: aesia-08-guia-transparencia-07-medidas-aplicables-para-conseguir-transp
description: "AESIA: aesia 08 guia transparencia, sección «Medidas aplicables para conseguir Transparencia (parte 1)» (págs. 29-36). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-08-guia-transparencia
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Medidas aplicables para conseguir Transparencia (parte 1)"
  paginas: 29-36
  origen: 2026-07-17-aesia-08-guia-transparencia.pdf
  oficial: false
---
# Medidas aplicables para conseguir Transparencia (parte 1)

5. Medidas aplicables conseguir Transparencia

para

Este capítulo recoge las medidas de diseño y desarrollo que pueden permitir que un sistema de IA sea Transparente (Apartado 1 del artículo 13), y que además son aplicables a la información específica que recoge el Apartado 3 de dicho artículo para que ésta pueda ser transmitida de manera Transparente.

5.1.

Proporcionar contacto con el proveedor

La labor del proveedor no termina con la implantación, sino que también continua a partir de que el sistema está en producción. Esta relación, habitual en cualquier sistema software, es especialmente importante en los sistemas de IA, dada su complejidad, y particularmente en los de alto riesgo dada la criticidad de los procesos que soportan. Por tanto, dentro de su estructura organizativa y del modelo de gobierno asociada al sistema de IA proporcionado, las entidades proveedoras habilitarán para sus entidades responsables del despliegue un punto de contacto claro. Las funciones de dicho contacto serán:
-

-

Supervisar de manera proactiva que el sistema cumple la normativa, teniendo en cuenta que el cumplimiento es una actividad constante en el tiempo por dos motivos:
o Al igual que cualquier otro sistema software es susceptible de cometer errores, está sujeto a políticas de actualización, etc.
o Aun no teniendo errores propios del software, su proceso de aprendizaje y sus acciones posteriores (predicciones, toma de decisiones, etc.) puede acabar degradando debido a la aparición de nuevos escenarios.
Atender de manera reactiva a las peticiones realizadas por la entidad responsable del despliegue, ya sea por incidencias detectadas por ésta, bien por solicitudes orientadas a entender el funcionamiento del sistema de IA. Sin perjuicio de los mecanismos del proveedor existentes para la atención y resolución de incidencias del sistema de IA.

El canal de contacto deberá permitir la gestión de las peticiones e incidencias de la entidad responsable del despliegue de manera online mediante el registro de las mismas, su gestión a través de workflows de trabajo por parte de los perfiles funcionales y técnicos de la entidad proveedora necesarios para su resolución, la monitorización de todas las peticiones e incidencias gestionadas, y el histórico necesario para su resolución, etc. Estos procesos podrán ser soportados por un canal de la demanda IT, un estándar de dicha industria.
A quién aplica
-
-

El proveedor podrá proporcionar dicho contacto y el canal a través del cual se producirá.
El responsable del despliegue podrá igualmente identificar a los responsables dentro de su organización encargados de activar dicho contacto con el proveedor ante situaciones como las anteriormente descritas.

28

Ejemplo - Concesión de ayudas
Los responsables de la entidad responsable del despliegue detectan que la cuantía propuesta para la ayuda de una familia no es homogénea respecto a otras proporcionadas en el pasado a familias con características similares. Dichos responsables activan el contacto con el proveedor mediante la apertura de una petición en el sistema de gestión de la demanda.

Ejemplo - Bomba de insulina
Un responsable médico de la entidad responsable del despliegue detecta mediante una alarma proporcionada por el sistema que la siguiente dosis prescrita a un paciente no es la habitual pese a tener parámetros similares en sangre. Dicho responsable médico activa el contacto con el proveedor mediante la apertura de una petición en el sistema de gestión de la demanda, además de tomar las medidas oportunas bajo su criterio médico sobre la dosis, y contactar con el paciente para entender posibles variables médicas de entorno no contempladas por el sistema de IA.

A qué apartados aplica esta medida
-
-

Apartado 3a. Contacto
Apartado 3c. Cambios

5.2.

Atender al dominio de la funcionalidad

Esta medida es trivial en cualquier sistema informático, pero cobra especial importancia al tratarse de la aplicación de una tecnología con las peculiaridades de la Inteligencia Artificial, dado que se pueden plantear escenarios diferentes no identificados con otro tipo de tecnologías.
Por eso, durante el diseño del sistema de IA, es fundamental identificar cuáles son las necesidades de transparencia aplicables al dominio al que pertenece (Seguros, Finanzas,
Sanidad, Retail, Trasporte, Industria, AAPP, etc.), identificar las características claves de
Transparencia que se han de tener en cuenta en cada caso de uso y el porqué de las mismas ya que, por ejemplo, las necesidades de transparencia son diferentes para un sistema de identificación biométrica que para uno dedicado a la gestión de infraestructuras críticas en el sector industrial. Incluso son diferentes en función del caso de uso concreto de ambas tipologías, ambas categorizadas como de alto riesgo por el reglamento.
Todo ello sin perjuicio de la legislación específica en materia de transparencia, en particular en las AAPP.

29

Ejemplo - Concesión de ayudas
En nuestro caso de uso, estas son los principales requisitos que deberán ser soportados por el sistema atendiendo al dominio de la funcionalidad del mismo y que, atendiendo a la transparencia, deberán ser explícitamente expuestos en las condiciones de uso del sistema.
Además, se deberá poder monitorizar durante el funcionamiento del sistema que dichos criterios se siguen manteniendo y que no se degeneran durante su funcionamiento:
-

-

-

El criterio global que se está siguiendo para predecir el riesgo de exclusión social, o para conceder las ayudas, Por ejemplo:
o Familia que lleve un determinado periodo de tiempo con ingresos inferiores a una determinada cantidad mensual.
o Que dicha cantidad esté ponderada por el número de miembros y edad de los mismos, dando más peso a los miembros en edad escolar sin capacidad de aportar recursos económicos a la familia a corto/medio plazo.
o Que tenga gastos recurrentes (p. ej.: hipoteca, tratamientos médicos no cubiertos por la seguridad social, etc.).
o Que dicho criterio pondere con más peso aquellas familias que tengan miembros dependientes o con algún tipo de minusvalía.
o El grado de desarrollo económico de la geografía en la que se ubique el lugar de residencia.
o Dado que el sistema ha sido entrenado con datos históricos de estructuras familiares de décadas anteriores y de familias tradicionales que siguen siendo mayoría en la actualidad, sobre las que se realizan predicciones , se asegure el mismo trato a familias con nuevas estructuras familiares (por ejemplo, monoparentales/parentales, constituidas por personas del mismo género, etc.).
El sistema deberá poder comparar decisiones tomadas sobre un conjunto de familias con características similares en base a los criterios anteriormente indicados, permitiendo comprobar que las decisiones son homogéneas en dicho conjunto.
El sistema deberá poder detallar internamente, y a la familia solicitante, el motivo por el cual se concede/deniega la ayuda, en base al criterio global de funcionamiento del sistema. En caso de denegación se deberán detallar, por ejemplo, en qué condiciones se les concedería, o a partir de cuándo.

30

Ejemplo - Bomba de insulina
Estos son algunos de los requisitos que deberán ser soportados por el sistema atendiendo al dominio del negocio del mismo y que deberán ser explícitamente expuestos en las condiciones de uso del sistema. Además, se deberá poder monitorizar durante el funcionamiento del mismo que dichos criterios se siguen manteniendo y que no se degeneran durante su funcionamiento:
-

-

-

El criterio global seguido para predecir una tendencia y realizar el suministro de insulina de manera automática; detallando las variables en sangre y sus valores, el historial médico del paciente, las condiciones medioambientales y, como consecuencia, la dosis suministrada.
El sistema deberá poder comparar decisiones tomadas sobre un conjunto de pacientes con características similares en base a los criterios anteriormente indicados, permitiendo asegurar que las decisiones son homogéneas en dicho conjunto.
El sistema deberá poder detallar internamente y a un paciente concreto el motivo por el cual se le varía la dosis, en base al criterio global de funcionamiento del sistema anteriormente descrito.

A quién aplica
Esta medida aplica a la entidad responsable del despliegue ya que, es la responsable de definir los requisitos funcionales del sistema de IA que soportará su caso de uso, atendiendo al dominio de negocio de dicho caso. Estos requisitos son independientes de la tecnología utilizada y el proveedor que se la proporcione. Como parte de dichos requisitos deberá identificar los relacionados con la transparencia del mismo.
Por otra parte, el proveedor podrá informar con detalle del alcance funcional del sistema de
IA que pone finalmente a disposición de la entidad responsable del despliegue, para que esta pueda asegurar la alineación entre sus necesidades y las soportadas por dicho sistema, especificando también los posibles riesgos por usos no previstos tal y como indica el apartado
3b.iii del presente artículo.
A qué apartados aplica esta medida
-
-
-

Apartado 1. Diseño y desarrollo
Apartado 3b.i. Finalidad
Apartado 3d. Vigilancia humana

31

5.3.

Asegurar el objetivo funcional del sistema

Para asegurar el objetivo funcional del sistema, y gestionar el riesgo de que sea utilizado para un fin distinto para el que fue concebido será necesario:
-
-

Identificar las circunstancias previsibles donde pudieran darse dichos usos.
Definir un plan de riesgos para dichos usos, supervisando de manera proactiva que dichos escenarios no se producen durante el funcionamiento del sistema (descrito en la guía de gestión de riesgos, artículo 9).

A quién aplica
Esta medida de supervisión aplica tanto a la entidad proveedora como a la responsable del despliegue, siendo el contacto de la entidad proveedora y su espejo en el responsable del despliegue los roles de dicha supervisión.

Ejemplo - Concesión de ayudas
El sistema de concesión de ayudas utiliza datos de la unidad familiar. Dichos datos han de ser tratados con especial vigilancia, asegurando que su uso se circunscriba únicamente al objetivo funcional del sistema (la concesión de ayudas), ya que menores de dieciocho años pueden formar parte de dicha unidad familiar, y este grupo de personas es especialmente detallado en el Artículo 9 del Reglamento Europeo de la IA (gestión de riesgos), indicando que “se prestará especial atención a la probabilidad de que personas menores de dieciocho años se vean afectadas”. El potencial uso de dichos datos con una finalidad distinta a la prevista debe ser especialmente gestionado, y además previsto en el plan de riesgos del sistema de IA.

Ejemplo - Bomba de insulina
El sistema de administración de insulina utiliza datos aplicables específicamente a un paciente en función de su patología y de su estado actual, en base a los cuales determina la dosis exacta necesaria que el paciente deberá cargar, ya que este es uno de los beneficios de utilizar este sistema. Dicha información es obtenida del historial médico del paciente y de los datos online que el sistema recoge del mismo.
El sistema deberá informar al paciente de manera transparente que el producto inoculado es el prescrito por su médico responsable y no otra variante, que la dosis incorporada al dispositivo por el paciente es la prescrita por el dispositivo en función del análisis online de su situación realizada por el dispositivo, y que dicha dosis está validada por el médico.

A qué apartados aplica esta medida
-
-
-

Apartado 1. Diseño y desarrollo
Apartado 3b.iii. Riesgos por usos previstos
Apartado 3d. Vigilancia humana

32

5.4.

Transparencia sobre los datos utilizados

Es fundamental conocer el funcionamiento del sistema de IA. Pero también es fundamental comprender los datos que maneja dicho sistema (estructurados o no estructurados, imágenes o lenguaje natural, por ejemplo). Esta acción puede aplicar tanto para datos para el aprendizaje del sistema de IA como para los datos de utilización en si por el responsable del despliegue. De esta manera se podrá:
-
-

Detallar con Transparencia los resultados que proporcione el sistema de IA.
Entender, y evaluar si la muestra de datos es justa y representativa para el objetivo del sistema de IA.

Para ello, es importante:
-
-

Enumerar las fuentes de datos utilizadas por el sistema,
Realizar un análisis exploratorio de datos (EDA) de dichas fuentes, para conocer su esencia, su metainformación asociada, los valores críticos o atípicos de los mismos, etc., entendiendo su significado ya que, a veces, las características de un conjunto dado de datos son visibles a primera vista, pero otras veces están entrelazadas, y esto puede tener implicaciones para aplicar transparencia al sistema.

A quién aplica
-

-

Al responsable del despliegue, ya que es el propietario final de los datos utilizados por dicho sistema, y debe ser conocedor del significado de sus datos, su utilidad y la implicación en el uso de los mismos.
Al proveedor, ya que es quien puede proporcionar las herramientas que permitan el análisis descriptivo y exploratorio de los datos.

33

Ejemplo - Concesión de ayudas
Enumeración de las fuentes de datos utilizadas:
- Información histórica de la evolución de familias que tuvieron carencias económicas y
finalmente necesitaron de algún tipo de ayuda.
- Información con el contexto económico general de la geografía a la que pertenecían
cuando se produjo dicha situación.
- Datos macroeconómicos acerca del contexto económico actual y previsiones del
mismo.
Análisis exploratorio de datos (EDA) de dichas fuentes con el objetivo de asegurar que las fuentes de datos incluyen, por ejemplo:
- Familias de distintas ubicaciones geográficas.
- Familias que, aunque en periodos importantes hayan llegado a tener ingresos
suficientes, finalmente han derivado en una situación de exclusión social (situación atípica pero posible), con datos que permitan entender cómo finalmente llegaron a dicha situación.
- Familias que ni tan siquiera tienen registro de ingresos, lo cual puede excluirles del
proceso al ser un valor crítico no contemplado.
- Metainformación no visible a primera vista, como la relación entre familia en situación
de exclusión y miembros de la misma con necesidades de dependencia o pertenecientes a grupos de personas vulnerables (p. ej., por cualquier tipo de discapacidad).
- Datos actuales, pero también históricos que permitan detectar el riesgo futuro en base
a patrones.
- Que los datos macroeconómicos incluyen todos los sectores profesionales en los que
cualquier familia pueda centrar su actividad.

Ejemplo - Bomba de insulina
Enumeración de las fuentes de datos utilizadas, como, por ejemplo:
- Información histórica de los parámetros en sangre evaluados por el sistema para la
administración de la dosis.
- Información histórica de las dosis suministradas a todos los pacientes, así como su
reacción a las mismas.
- Información de los compuestos suministrados
Análisis exploratorio de datos (EDA) de dichas fuentes con el objetivo de asegurar que las fuentes de datos incluyen, por ejemplo:
- Pacientes de distintas geografías con diferentes condiciones climáticas.
- Pacientes de diferentes edades, sexo, características morfológicas (peso, altura, etc.),
nivel de actividad física, etc.
- Casos de reacciones adversas a las dosis suministradas, con datos que permitan
entender qué produjo dicha reacción.
- Datos de pacientes sin más patologías que la diabetes, así como datos de pacientes
con otras patologías adicionales.

34

A qué apartados aplica esta medida
-
-
-
-
-

Apartado 1. Diseño y desarrollo
Apartado 3b.v. Impacto en personas
Apartado 3b.vi. Datos de entrada
Apartado 3b.vii. Información de salida
Apartado 3d. Vigilancia humana

5.5.

Detallar de lo más global a lo más particular

La información interna proporcionada por el sistema de IA debe ser concisa y lo más completa posible, por tanto, es necesario comprender el funcionamiento de dicho sistema desde lo más general a lo más particular, habilitando medidas técnicas que permitan abordar el mayor grado posible de detalle en:
-
-
-

El mecanismo de razonamiento global del sistema de IA.
Las predicciones y decisiones tomadas sobre un subconjunto de información con características parecidas, para garantizar la homogeneidad de su funcionamiento.
E incluso de cada una de dichas predicciones y decisiones de manera individual.

A quién aplica
El proveedor podrá dotar al sistema de los mecanismos técnicos que faciliten esta necesidad y así asegurar a la entidad usuaria el completo control y entendimiento del sistema bajo un lenguaje entendible por todos los actores que interactúan con él a lo largo de todo su ciclo de vida.
A qué apartados aplica esta medida
-
-

Apartado 1. Diseño y desarrollo
Apartado 3d. Vigilancia humana

Ejemplo - Concesión de ayudas
El sistema deberá ofrecer mecanismos que permitan a la entidad responsable del despliegue conocer:
- El criterio global seguido para conceder las ayudas (detallado en el ejemplo de la
medida Atender al dominio de la funcionalidad).
- Decisiones tomadas (evaluación del riesgo de exclusión social de una familia, tiempo
en el que se produciría, importe asignado, etc.) sobre un conjunto de familias con características similares (por ejemplo, en base al número de personas que la componen, nivel de ingresos, ubicación geográfica), permitiendo comprobar a los responsables del despliegue que las decisiones son homogéneas en dicho conjunto.
- Decisiones tomadas sobre una familia concreta, en base al criterio global de
funcionamiento del sistema. Además, en caso de no concederles la ayuda, detallará bajo qué valores de los criterios utilizados les sería asignada (siguiendo el criterio de contrafactualidad).

35
