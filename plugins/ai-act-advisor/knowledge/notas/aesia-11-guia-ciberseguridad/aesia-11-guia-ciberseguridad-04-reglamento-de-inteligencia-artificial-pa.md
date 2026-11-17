---
name: aesia-11-guia-ciberseguridad-04-reglamento-de-inteligencia-artificial-pa
description: "AESIA: aesia 11 guia ciberseguridad, sección «Reglamento de Inteligencia Artificial (parte 1)» (págs. 17-24). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-11-guia-ciberseguridad
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Reglamento de Inteligencia Artificial (parte 1)"
  paginas: 17-24
  origen: 2026-07-17-aesia-11-guia-ciberseguridad.pdf
  oficial: false
---
# Reglamento de Inteligencia Artificial (parte 1)

Las soluciones técnicas encaminadas a garantizar la ciberseguridad de los sistemas de IA de alto riesgo serán adecuadas a las circunstancias y los riesgos pertinentes.
Entre las soluciones técnicas destinadas a subsanar vulnerabilidades específicas de la IA figurarán, según corresponda, medidas para prevenir, detectar, combatir, resolver y controlar los ataques que traten de manipular el conjunto de datos de entrenamiento («envenenamiento de datos»), o los componentes entrenados previamente utilizados en el entrenamiento
(«envenenamiento de modelos»), la información de entrada diseñada para hacer que el modelo de IA cometa un error («ejemplos adversarios» o «evasión de modelos»), los ataques a la confidencialidad o los defectos en el modelo.

3.3 Correspondencia del artículo con los apartados de la guía
En la tabla dispuesta a continuación se detalle en que secciones de esta guía se abordan los diferentes elementos de dicho artículo:
Artículo Reglamento
15.1

Requerimiento Reglamento
Nivel de ciberseguridad consistencia.

Sección guía y

Apartado 4.1

15.5

Sistemas resistentes a alteraciones de uso.

Apartado 4.2

15.5

Prevenir y controlar la manipulación del conjunto de datos.

Apartado 4.3

15.5

Protección adversarios.

Apartado 4.4

15.5

Protección frente a los defectos del sistema.

frente

a

ataques

Apartado 4.5

16

4. ¿Cómo podemos abordar los requisitos?
4.1 Nivel de ciberseguridad y consistencia
En el Reglamento Europeo de Inteligencia Artificial, en el artículo 15 relativo a precisión, solidez y ciberseguridad, se indica lo siguiente:

Art.15.1 – Precisión, solidez y ciberseguridad
Los sistemas de IA de alto riesgo se diseñarán y desarrollarán de modo que alcancen un nivel adecuado de precisión, solidez y ciberseguridad y funcionen de manera uniforme en esos sentidos durante todo su ciclo de vida.

A lo largo de este apartado vamos a indicar las medidas de alto nivel que, a modo de ejemplo y no vinculante, se relacionan con el artículo, teniendo en cuenta que serán más desarrolladas en aspectos específicos en los apartados siguientes. El enfoque de este apartado es permitir al proveedor o al responsable del despliegue conocer el alcance de los controles de ciberseguridad para IA necesarios para cubrir las vulnerabilidades detalladas en la guía que le sean de aplicación. Es importante que se sea consciente que se presenta una información en la guía que en ningún caso pretende ser exhaustiva al respecto de las vulnerabilidades existentes, sino que estas se muestran como una lista de aquellas posibles, y que, dados los ámbitos indicados, (envenenamiento de datos, ataques adversarios o manipulación de defectos) estos se recomiendan que se amplíen acorde a las necesidades del sistema de IA para la finalidad prevista. Especialmente con el objetivo de cubrir los riesgos en materia de derechos y libertades.
En cada elemento del ciclo de vida de un sistema de IA de alto riesgo, se establece un nivel de ciberseguridad acorde a la finalidad prevista del sistema, estableciendo diferentes medidas. Dependiendo de la fase del ciclo de vida las medidas deberán de ser realizadas por proveedor (diseño, desarrollo) o funcionamiento (responsable del despliegue).
En este contexto se entiende “ciclo de vida del sistema de IA”, como la duración para el sistema de IA, desde su concepción, diseño, implementación y puesta en marcha, hasta su retirada. Diferentes fases pueden aplicar a diferentes sistemas de IA dependiendo de su finalidad prevista y forma de comercialización, por lo que en términos generales consideramos estas fases:

17

-

Concepción.

-

Diseño.

-

Implementación.

-

Verificación y prueba.

-

Puesta en marcha.

-

Vigilancia poscomercialización.

-

Retirada.

Este ciclo de vida aquí descrito aplica al sistema de IA, en exclusiva, y en ningún caso se puede considerar representativo de otros elementos, como por ejemplo del ciclo de vida de los datos (que se aborda en la guía de datos), o el ciclo de vida de otros sistemas de información o infraestructura utilizados para soportar el sistema de IA. Del mismo modo, la relación de la ciberseguridad como establecimiento de controles de seguridad está directamente relacionada con el sistema de gestión de riesgos (ver guía de gestión de riesgos), especialmente aquellos relacionados con los derechos y libertades de las personas físicas, daños a la salud, daños graves a la propiedad y/o el medio ambiente. La protección del sistema frente a la tipología de amenazas descritas en esta guía está directamente relacionada con la solidez del sistema de IA de alto riesgo (ver guía de solidez).

4.1.1 Medidas aplicables
Se recomienda que las medidas técnicas se traduzcan en controles de seguridad, aplicados al inventario de activos para defenderse ante amenazas y prevenir los riesgos, de manera que así sean según el Reglamento Europeo de IA en su Art. 15:

Art.15.5 – Precisión, solidez y ciberseguridad
[...] adecuadas a las circunstancias y los riesgos pertinentes.

Una vez definidas y puesta en marcha las medidas, estas se recomienda que se garanticen durante todo el ciclo de vida, de manera que el nivel sea el adecuado, no solo a las amenazas y las medidas de seguridad necesarias en el momento de la puesta en marcha del sistema, sino que se adapten y adecuen a nuevas amenazas que puedan aparecer, sin que se degrade el nivel de ciberseguridad.
Se debe de destacar el papel fundamental del Análisis de Riesgos desarrollado. En este caso, durante dicho análisis y con una visión global del sistema, se recomienda determinar

18

los riesgos iniciales de ciberseguridad detectados, que se deberán de tratar durante el desarrollo de las actividades de la presente Guía.
Proveedor
El proveedor puede tomar en consideración las siguientes medidas organizativas:
Planificar de manera global el nivel de ciberseguridad aplicada a IA durante el diseño y desarrollo.
- Cuando se disponga de esta figura, se recomienda implicar al delegado de
protección de datos (DPD), desde el diseño del sistema de IA y para la planificación de la ciberseguridad, como interlocutor dentro del grupo de trabajo establecido para desarrollar la planificación. Podrá, además, estar presente cuando se tomen decisiones específicas de ciberseguridad para comprobar su implicación con la protección de datos.
- Las instrucciones de uso del sistema de inteligencia artificial se recomiendan que
vayan acompañadas de las recomendaciones de alto nivel en medidas de ciberseguridad enfocada a IA, específicas del sistema de IA y su finalidad prevista, para tener en cuenta por el responsable del despliegue. Además, se recomienda que el sistema de IA, a través de la interfaz de interacción para el usuario final disponga de recomendaciones de uso en materia de ciberseguridad, de manera que estén accesibles para el usuario final del sistema. Es posible también incluir un mecanismo de interacción (tipo ventana de confirmación o similar) cada vez que se acceda al mismo que garanticen que las instrucciones en materia de ciberseguridad han sido leídas.
- Dentro del proceso de diseño se pueden establecer responsables del seguimiento
de las medidas de ciberseguridad aplicada al sistema de IA. Definir un cuadro de mando para el seguimiento de la operación. Se podrán establecer los indicadores de ciberseguridad para IA obligatorios a incluir en el cuadro de mando para el seguimiento de la operación del sistema de IA. Se establecerá la periodicidad mínima en la que se realizará una auditoría de seguridad del sistema de IA, independientemente de que sea interna o externa.
- Las medidas de ciberseguridad aplicables durante todo el ciclo de vida del sistema
de inteligencia artificial, que se detallan en esta guía, serán todas ellas aplicables por parte del proveedor, si este proporciona al responsable del despliegue el sistema de IA como un MLaaS (Machine Learning as a Service) u otras formas de comercialización y puesta en marcha que impliquen una instalación automática por el responsable del despliegue donde no haya configuración del sistema.
- Si el sistema de IA va a ser entregado al responsable del despliegue en un formato
on-premise o in-cloud, gestionado por el responsable del despliegue, se recomienda que el proveedor proporcione unas instrucciones adecuadas para realizar la protección del sistema especialmente durante el tiempo de inferencia del sistema de IA en producción. El proceso de instalación del sistema de IA se recomienda que conste de mecanismos que garanticen que la instalación tenga en cuenta las instrucciones de manera obligatoria, bien a través de procedimientos de script automáticos o semi automáticos, la obligación de disponer de las

19

instrucciones abiertas para el proceso antes de continuar, la solicitud explícita de la lectura de estas o la referencia a la lectura específica a conocer para cada paso del proceso.
Como complemento a estas medidas organizativas, el proveedor podrá alinear las siguientes medidas técnicas:
- En los procesos de instalación y/o configuración del sistema de Inteligencia Artificial
y en el manual de instrucciones, el proveedor puede incluir información relativa a los riesgos de ciberseguridad específicos del sistema y cómo este se encuentra protegido.
- Durante el ciclo de vida del sistema de IA de alto riesgo se pueden utilizar
herramientas que permitan automatizar las pruebas de seguridad. El uso de estas herramientas, desde el inicio del desarrollo del sistema, permite realizar un diseño orientado a seguridad, concibiendo las pruebas de ataque al sistema en paralelo a su desarrollo y ciclo de vida. Existen, tanto en el mercado como variantes de código abierto, una gran variedad de herramientas que cumplen con lo indicado.
- Las actualizaciones del sistema de IA se recomiendan que se desarrollen aplicando
las medidas técnicas descritas en los sucesivos apartados para que el nivel de ciberseguridad aplicable a IA sea consistente, continuo y no se degrade con la aplicación de estas.

Ejemplo - Asistencia al trabajo
Para abordar la ejecución de las medidas de ciberseguridad en IA, dentro del equipo de análisis y diseño del sistema de IA de alto riesgo, se establecen las responsabilidades y las personas que realizarán las acciones. Se han comprobado los perfiles presentes en la organización y se ha valorado la posibilidad de ampliar su personal para cubrir los esfuerzos necesarios para la ciberseguridad enfocada a IA del sistema. El proveedor ha concluido que, con sus actuales recursos de personal asociados a la gestión de riesgos, desarrollo y análisis del sistema de IA, así como el equipo de implantación, pueden llevar a cabo los aspectos necesarios.
El DPD, en el caso de que la organización cuente con él, se ha incluido en el equipo de trabajo desde la fase de diseño, asegurando su participación en todas las decisiones de ciberseguridad. También se ha desarrollado un plan integral de gestión de riesgos que contempla específicamente las amenazas relacionadas con sistemas de IA y se ha actualizado el proceso de control de seguridad de entrega de software para incluir pruebas específicas contra estas amenazas (este plan se revisa y actualiza trimestralmente).
Se han implementado herramientas automatizadas de análisis de vulnerabilidades que se ejecutan en cada nueva release del sistema y cuando se incorporan nuevos conjuntos de datos de entrenamiento. Estas herramientas incluyen escáneres de seguridad especializados en IA y sistemas de vigilancia continua del modelo. Se ha establecido un programa de

20

auditorías con revisiones internas trimestrales y una auditoría externa anual obligatoria, documentando los hallazgos y acciones correctivas en el plan de gestión de riesgos.
Tras definir todos los puntos anteriores, el proveedor ha programado una formación para todo el personal implicado, que permite consolidar los conocimientos y el proceso de ciberseguridad en IA dentro de la organización, utilizando como base esta guía y la aproximación indicada en el apartado 7.2 de la presente guía. Se ha incluido en el plan de seguridad del proveedor la formación específica en ciberseguridad para sistemas IA, con actualizaciones semestrales del programa formativo para incorporar nuevas amenazas y contramedidas.

Responsable del despliegue
Las medidas organizativas en materia de ciberseguridad aplicables al responsable del despliegue dependen del nivel de implicación de este en el ciclo de vida del sistema de
Inteligencia Artificial de alto riesgo.
- Se recomienda distribuir la información de instalación y configuración en su
organización.
- Si el sistema se encontrase en sus instalaciones, o fuese gestionado por este (onpremise o in-cloud gestionada por el responsable del despliegue), puede
establecer, dentro de su política general de ciberseguridad todos los activos asociados al sistema de Inteligencia Artificial que pudieran serle de aplicación. Estos podrán ser datos, modelo, procesos, entornos/herramientas y artefactos. Además de la identificación de los actores en su organización sobre cada uno de estos activos. Así sobre el conjunto de activos a las condiciones de uso que haga del sistema de IA, acorde a su finalidad prevista, a modo orientativo se pueden aplicar las consideraciones indicadas en esta guía, especialmente aquellas centradas en fase de inferencia con el sistema de IA en producción.
Como medida técnica se puede disponer de un repositorio centralizado donde gestionar la información, accesible para aquellos actores identificados en el desarrollo del sistema de inteligencia artificial.

Ejemplo – Sistema automático de concesión de ayudas
Los responsables del despliegue del sistema de IA pueden ser la Administración
General del Estado y otras Administraciones Públicas, como Comunidades Autónomas o entidades locales. En cualquiera de los casos, pueden optar por una instalación onpremise del sistema. El proveedor ha proporcionado, por un lado, un manual de instrucciones y por otro, de la configuración del sistema (que se realizará on-premise).
En ambos documentos se recoge específicamente la información de ciberseguridad relacionada con ambos procesos. Sobre ella se realizan dos acciones:

21

- El personal de la Administración Pública encargado de gestionar la respuesta del
sistema de IA ha recibido el manual de instrucciones y una formación específica en ciberseguridad para IA acorde a su alcance.
- El personal de administración de sistemas y tecnologías IT relacionado ha
recibido el manual de configuración del sistema y los aspectos centrados en ciberseguridad. Particularmente en las Entidades Locales, se considera actualizar los conocimientos del personal en el área de ciberseguridad de IA con una formación adaptada a sus conocimientos técnicos. Este personal específicamente recibe también esta guía.

4.2 Sistemas resistentes a alteraciones de uso
Como establece el Reglamento Europeo de IA en el apartado 5 de su artículo 15 relativo a precisión, solidez y ciberseguridad:

Art.15.5 – Precisión, solidez y ciberseguridad
Los sistemas de IA de alto riesgo serán resistentes a los intentos de terceros no autorizados de alterar su uso, sus resultados de salida o su funcionamiento aprovechando las vulnerabilidades del sistema.
Las soluciones técnicas encaminadas a garantizar la ciberseguridad de los sistemas de IA de alto riesgo serán adecuadas a las circunstancias y los riesgos pertinentes.

Las medidas descritas en el apartado anterior, a título orientativo, podrían ir van acompañadas de la realización de inventarios de los activos del sistema de inteligencia artificial durante su ciclo de vida, y los actores que interactúan con dichos activos. Estos inventarios podrían ayudar a cubrir dos aspectos indicados por el Reglamento Europeo de
IA tal y como se ha indicado al principio del punto 5 del artículo 15:
- Establecer la base para proteger el sistema de los intentos de terceros no
autorizados de alterar el uso y funcionamiento del sistema de inteligencia artificial.
Al disponer de inventarios de activos y actores se pueden aplicar políticas de acceso
(ver Anexo I).
- Poder dimensionar sobre los activos identificados soluciones técnicas que
garanticen la ciberseguridad, identificar las vulnerabilidades sobre estos y sus controles (ver en detalle del subapartado 4.3 Vulnerabilidades y controles de seguridad para datos al subapartado 4.5 Ataques a los defectos del sistema de IA).

22

23
