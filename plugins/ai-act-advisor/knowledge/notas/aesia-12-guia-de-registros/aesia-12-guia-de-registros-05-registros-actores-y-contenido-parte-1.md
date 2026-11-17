---
name: aesia-12-guia-de-registros-05-registros-actores-y-contenido-parte-1
description: "AESIA: aesia 12 guia de registros, sección «Registros: actores y contenido (parte 1)» (págs. 14-21). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-12-guia-de-registros
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Registros: actores y contenido (parte 1)"
  paginas: 14-21
  origen: 2026-07-17-aesia-12-guia-de-registros.pdf
  oficial: false
---
# Registros: actores y contenido (parte 1)

4. Registros: actores y contenido
4.1.

Agentes responsables de los registros

Las obligaciones asociadas a los sistemas de IA de alto riesgo en relación con la conservación de los registros, a los que se refiere el artículo 12, recaen tanto sobre el proveedor como sobre el responsable del despliegue del sistema de alto riesgo.
-

Si soy el proveedor o el responsable del despliegue del sistema de IA de alto riesgo:
a) Deberé encargarme de la conservación de los registros que genere mi sistema (ver apartado 5.3) siempre y cuando estos registros estén bajo mi control.
b) Los deberé conservar durante un periodo de al menos seis meses salvo que se disponga lo contrario en el Derecho de la Unión o nacional aplicable, en particular en el Derecho de la Unión en materia de protección de datos personales.
c) Si soy una entidad financiera deberé mantener los registros como parte de la documentación conservada en virtud de la legislación pertinente en materia de servicios financieros.

En el apartado 3.2 se citan los artículos del Reglamento que especifican las obligaciones del proveedor y responsables del despliegue en relación con los requisitos en materia de registros.

4.2.
¿Qué información puede contener generalmente un registro?
Los registros deben representar la información que se haya identificado como necesaria tras el proceso de evaluación (ver apartado 5.1). Para dar una idea más detallada de la información que generalmente puede contener un registro de un sistema de IA, se adjunta a continuación los atributos más frecuentes:
a) Un identificador único del registro.
b) La identidad del usuario o el sistema que registró el evento.
c) Una descripción del contenido del registro.
d) La estructura del registro (por ejemplo, su forma y formato).
e) El contexto y finalidad en el que se crea, se recibe y se utiliza el registro.
f) Las acciones y eventos a lo largo de la existencia del registro.
g) Fecha y hora de cada acción realizada en el sistema.
h) Identificación del modelo o algoritmo de IA utilizado, incluyendo la versión y los parámetros de configuración utilizados.
i) Identificación de los datos de entrada utilizados por el sistema de IA.
j) Fuente de los datos de entrada utilizados por el sistema de IA.
k) El tipo de datos de entrada utilizados por el sistema de IA.

13

l)

Resultados producidos por el sistema de IA, incluyendo la salida del modelo o algoritmo y cualquier información adicional generada por el sistema.
m) Métricas de calidad de los resultados (por ejemplo, la precisión).
n) Información de monitoreo de rendimiento y capacidad, como el uso de recursos
(CPU, memoria, almacenamiento), el tiempo de respuesta y la tasa de errores.
o) Información de seguridad y privacidad, como la autenticación y autorización de usuarios, el cifrado de datos y la detección de intentos de acceso no autorizados.
p) Alertas o notificaciones generadas por el sistema, como advertencias de errores en los datos de entrada o fallas en el sistema.
q) Relaciones con otros registros.
r) Información que consideremos necesaria para cumplir la función de evidencia para la que se ha diseñado el registro (ver apartado 5.1).
s) Otra información necesaria para recuperar y presentar el registro (por ejemplo, la información de almacenamiento).

Ejemplo - Sistema de IA de promoción y ascenso
Tomando como ejemplo el sistema de IA de promoción y ascenso de los empleados, un ejemplo de un registro que se podría generar (en el apartado 5.1 se analiza en detalle cuando y porque interesará generar un registro) es aquel que recogiera la siguiente información:
-
-
-
-
-
-

Fecha y hora de cada acción realizada en el sistema, como el envío de solicitudes de promoción o la revisión de perfiles de candidatos.
Identificación del usuario o usuarios que realizaron cada acción, ya que esto permitiría una trazabilidad completa de las acciones en el sistema y una detección temprana de cualquier conducta discriminatoria.
Perfil de los candidatos evaluados para cada puesto, incluyendo información relevante como la educación, experiencia laboral y habilidades requeridas para el puesto.
Resultados de cada evaluación de candidatos, incluyendo puntuaciones, comentarios y notas realizadas por los evaluadores.
Cualquier acción tomada en respuesta a las evaluaciones, como decisiones de contratación o promoción, y la justificación de dichas decisiones.
Alertas o notificaciones generadas por el sistema en caso de detección de patrones discriminatorios, como la promoción frecuente de candidatos de un determinado género o etnia.

Ejemplo – Sistema de IA de administración de insulina
Tomando como ejemplo el sistema de IA de administración de insulina, un ejemplo de un registro que se podría generar (en el apartado 5.1 se analiza en detalle cuando y porque nos interesará generar un registro) es aquel que recogiera la siguiente información:
-
-
-
-

Fecha y hora de cada administración de insulina.
Tipo y cantidad de insulina administrada.
Nivel de glucosa en sangre antes de la administración.
Nivel de glucosa en sangre después de la administración.

14

-
-
-

Alertas o notificaciones generadas por el sistema en caso de detección de patrones anormales o peligrosos, como niveles de glucosa demasiado bajos o altos, o administraciones frecuentes de insulina en un corto período de tiempo.
Interacciones con otros medicamentos o tratamientos médicos del paciente.
Cualquier otro evento relevante registrado por el sistema, como cambios en la dosis de insulina prescrita por el médico o cambios en la dieta del paciente.

4.3.
¿Qué información debería contener un registro de un sistema de identificación biométrica remota?
Un sistema de identificación biométrica remota es, según el Reglamento, “un sistema de IA destinado a identificar a personas físicas generalmente a distancia, sin su participación activa, comparando sus datos biométricos con los que figuran en un repositorio de datos de referencia”.
En este sentido, además de los elementos comunes de los registros de un sistema de IA, si el sistema es de identificación biométrica remota (sistemas de IA que figuran en el punto
1, letra a), del anexo III) deberá incorporar algunos elementos específicos, los cuales se indican en el apartado 3 del artículo:

AI Act
Art.12.3 - Registros
En el caso de los sistemas de IA de alto riesgo mencionados en el anexo III, punto 1, letra a), las capacidades de registro incluirán, como mínimo:
a) un registro del período de cada uso del sistema (la fecha y la hora de inicio y la fecha y la hora de finalización de cada uso);
b) la base de datos de referencia con la que el sistema ha cotejado los datos de entrada;
c) los datos de entrada con los que la búsqueda ha arrojado una correspondencia;
d) la identificación de las personas físicas implicadas en la verificación de los resultados que se mencionan en el artículo 14, apartado 5 (el cual indica lo siguiente: En el caso de los sistemas de IA mencionados en el anexo III, punto 1, letra a), las medidas a que se refiere el apartado 3 del presente artículo garantizarán, además, que el responsable del despliegue no actúe ni tome ninguna decisión basándose en la identificación generada por el sistema, salvo si al menos dos personas físicas con la competencia, formación y autoridad necesarias han verificado y confirmado por separado dicha identificación. El requisito de la verificación separada por parte de al menos dos personas físicas por separado no se aplicará a los sistemas de IA de alto riesgo utilizados con fines de garantía del cumplimiento del Derecho, de migración, de control fronterizo o de asilo cuando el
15

Derecho nacional o de la Unión considere que la aplicación de este requisito es desproporcionada.)

En este contexto, lo que se deberá hacer si se ha desarrollado un sistema biométrico, es asegurarse de recabar en los registros esta información adicional.
A continuación, se dispone un ejemplo para un caso de uso de un sistema de IA de identificación biométrica remota en la asistencia al trabajo:

Ejemplo – Sistema de IA de identificación biométrica remota en la asistencia al trabajo
Tomando como ejemplo el sistema de IA de identificación biométrica remota en la asistencia al trabajo, un ejemplo de un registro que se podría generar (en el apartado
5.1 se analiza en detalle cuando y porque nos interesará generar un registro) es aquel que recogiera la siguiente información:
-
-
-
-
-
-
-
-

Fecha y hora de cada identificación realizada por el sistema (la fecha y la hora de inicio y la fecha y la hora de finalización de cada uso).
La base de datos de referencia con la que el sistema ha cotejado los datos de entrada.
Una imagen de la cara que fue analizada (los datos de entrada con los que la búsqueda ha arrojado una correspondencia).
La identificación de las dos o más personas físicas implicadas en la verificación de los resultados.
Resultados de la identificación, incluyendo la persona identificada, si se realizó una coincidencia, el nivel de confianza de la identificación y cualquier error o anomalía detectada.
Información sobre la cámara o dispositivo utilizado para capturar la imagen facial.
Información sobre la ubicación y el contexto de la identificación, como el lugar donde se utilizó el sistema y la finalidad de la identificación (controlar el tiempo trabajado).
Cualquier cambio en el sistema, como actualizaciones de software o hardware, que puedan afectar el comportamiento del sistema de IA.

La información recogida en estos tres ejemplos sobre los aspectos que debería contener un registro, que debe ser contemplado como un ejemplo y no como una obligación, se mencionará también en el capítulo 5, ya que se pretende ubicar este diseño de los registros en el proceso global de gestión y mantenimiento de registros.

16

5. ¿Qué elementos puedo implantar y cómo puedo hacerlo para desarrollar un adecuado sistema de gestión de registros?
En esta sección se describen los procesos que se recomienda abordar para el desarrollo de una adecuada y completa gestión de registros, desde la evaluación de la necesidad para la creación de los registros hasta su disposición y eliminación:

5.1.

Evaluación y diseño de los registros

¿Qué es?
La evaluación es el proceso de análisis mediante el cual se determina la necesidad de generar registros y los requisitos sobre estos registros. Esto ayudará a determinar qué información se debe recabar en los registros, estableciendo así qué registros debemos crear y capturar.
¿Cómo puedo abordarlo?
En términos generales, esta primera fase consiste en analizar y determinar la necesidad de generar el registro, definir los objetivos específicos para la generación del registro y establecer su alcance. Además, en esta fase se diseñará el registro, mediante la identificación de los campos y categorías para la recopilación de información. Esta fase es crucial para establecer unos registros útiles y efectivos que cumplan con los objetivos del sistema de gestión de registros.
17

De este modo, podemos identificar los siguientes elementos, a modo de ejemplo, dentro del proceso de evaluación y creación de los registros:
-

-

-

-

-

Identificación de la necesidad: El primer paso es identificar la necesidad del registro. ¿Por qué se necesita el registro? ¿Cuáles son los objetivos del registro? Es importante definir claramente la necesidad para asegurar que el registro sea útil y relevante.
Identificación de los objetivos: Una vez identificada la necesidad del registro, es necesario definir los objetivos específicos del registro. ¿Qué se espera lograr con el registro? ¿Cuáles son los resultados que se espera obtener? Es importante que los objetivos sean claros y específicos para que se pueda evaluar la efectividad del registro.
Definición del alcance: El siguiente paso es definir el alcance del registro. ¿Qué tipo de información se registrará? ¿Cuánto tiempo se mantendrá el registro? Es importante establecer el alcance para evitar la recopilación de información innecesaria o irrelevante.
Diseño del registro: Una vez definidos los objetivos y el alcance del registro, es necesario diseñar el registro. Esto implica definir los campos y categorías que se utilizarán para registrar la información, así como las herramientas y software que se utilizarán para capturar, almacenar y acceder a la información.
Identificación de los responsables: Finalmente, es importante identificar a los responsables del registro. ¿Quién será el encargado de recopilar y mantener la información? ¿Quién será responsable de garantizar la precisión y la integridad del registro? Es importante definir claramente los roles y responsabilidades para garantizar la efectividad del registro.

Se recomienda a cada organización determinar cuáles son sus necesidades para la generación de registros. No obstante, en el contexto del Reglamento Europeo de la IA, hay una serie de capacidades que los registros deben aportar al sistema de IA. En concreto, el texto del Reglamento expone lo siguiente:

AI Act
Art.12.2 - Registros
Para garantizar un nivel de trazabilidad del funcionamiento del sistema de IA de alto riesgo que resulte adecuado para la finalidad prevista del sistema, las capacidades de registro permitirán que se registren acontecimientos pertinentes para:
a) la detección de situaciones que puedan dar lugar a que el sistema de IA de alto riesgo presente un riesgo en el sentido del artículo 79, apartado 1, o a una modificación sustancial;
b) la facilitación de la vigilancia poscomercialización a que se refiere el artículo 72, y c) la vigilancia del funcionamiento de los sistemas de IA de alto riesgo a que se refiere el artículo 26, apartado 5.

18

En este sentido, el proceso de evaluación consistirá en analizar estos tres elementos y determinar qué registros conviene crear y capturar. A continuación, se entra más en detalle en cada uno de estos tres focos.

5.1.1. Situaciones de riesgo
Antes de poder abordar este punto se recomienda haber implementado las medidas detalladas en la guía que describe el sistema de gestión de riesgos (consultar guía asociada al artículo del sistema de gestión de riesgos).
Una vez abordada la guía del sistema de gestión de riesgos, se debería disponer de un inventario con las medidas de tratamiento de los riesgos identificados y analizados.
Como se detalla en dicha guía, el foco principal es la gestión de aquellos riesgos que puedan afectar a la salud, seguridad o derechos fundamentales de las personas.
El siguiente paso será analizar y decidir para cada una de estas medidas si se considera necesario o no evidenciar un determinado suceso, y consecuentemente generar un registro con los requisitos y contenidos que se establezca. Esta decisión y en su caso la especificación de los sucesos y registros asociados debería ser incorporada como proceda documentalmente como parte de las medidas de tratamiento de los riesgos asociados.
A continuación, se dispone un ejemplo detallado para el desarrollo de los diferentes elementos que componen la fase de evaluación y diseño de los registros en el contexto de la detección de situaciones que puedan dar lugar a que el sistema de IA presente un riesgo para la salud, seguridad o derechos fundamentales de las personas.

Ejemplo – Sistema de IA de identificación biométrica remota en la asistencia al trabajo
En el ejemplo del sistema de IA de identificación biométrica remota en la asistencia al trabajo, las fases propuestas de forma orientativa para la evaluación de la necesidad y diseño del registro enfocado en garantizar un proceso no discriminatorio con el fin de mitigar riesgos relacionados con una posible violación del derecho fundamental a la no discriminación se centrarían en lo siguiente:
-

-

-

Identificación de la necesidad: En esta fase, se identificaría la necesidad de contar con unos registros que permitan garantizar un proceso no discriminatorio en el sistema de IA de identificación biométrica remota utilizado en la asistencia al trabajo. Esta necesidad se basaría en la preocupación por garantizar la igualdad de oportunidades y evitar la discriminación por cualquier motivo, como la raza, género, orientación sexual, religión, etc.
Identificación de los objetivos: En esta fase, se definirían los objetivos específicos del registro para el sistema de IA de identificación biométrica remota.
Por ejemplo, se podrían establecer objetivos como: garantizar que el sistema no discrimine por motivos de raza, género u otros factores, asegurar que la precisión del sistema sea equitativa para todos los empleados, etc.
Definición del alcance: En esta fase, se establecería el alcance del registro. En el caso de un Sistema de IA de identificación biométrica remota en la asistencia al trabajo, se definirían los aspectos técnicos del sistema, como los algoritmos de identificación biométrica remota utilizados, la forma en que se capturan y procesan las características biométricas de los empleados, etc.
19

-

-

Diseño del registro: En esta fase, se diseñaría el registro para el Sistema de IA de identificación biométrica remota en la asistencia al trabajo. Se definirían los campos y categorías para la recopilación de información, la forma en que se almacenaría la información, y las herramientas y software que se utilizarían para capturar, almacenar y acceder a la información. Algunos ejemplos de datos que podrían recabarse serían:
o Fecha y hora de cada identificación realizada por el sistema (la fecha y la hora de inicio y la fecha y la hora de finalización de cada uso).
o La base de datos de referencia con la que el sistema ha cotejado los datos de entrada.
o Una imagen de la cara que fue analizada (los datos de entrada con los que la búsqueda ha arrojado una correspondencia).
o La identificación de las dos o más personas físicas implicadas en la verificación de los resultados.
o Resultados de la identificación, incluyendo la persona identificada, si se realizó una coincidencia, el nivel de confianza de la identificación y cualquier error o anomalía detectada.
o Información sobre la cámara o dispositivo utilizado para capturar la imagen facial.
o Información sobre la ubicación y el contexto de la identificación, como el lugar donde se utilizó el sistema y la finalidad de la identificación
(controlar el tiempo trabajado).
o Cualquier cambio en el sistema, como actualizaciones de software o hardware, que puedan afectar el comportamiento del sistema de IA.
Identificación de los responsables: Finalmente, se identificarían a los responsables de la gestión del registro. En este caso, se podría asignar la responsabilidad de recopilar y mantener la información a un equipo específico encargado de la gestión de los registros, y la responsabilidad de garantizar la precisión y la integridad del registro a los desarrolladores del Sistema de IA de identificación biométrica remota.

Todo ello con el objetivo de garantizar la no violación del derecho fundamental a la no discriminación y evitar, por tanto, la discriminación en el proceso de asistencia al trabajo mediante el uso del Sistema de IA de identificación biométrica remota.

5.1.2. Vigilancia poscomercialización
Del mismo modo que se indicaba en la sección anterior, antes de poder abordar este punto conviene haber implementado las medidas detalladas en la guía que describe el sistema de vigilancia poscomercialización (consultar guía asociada al artículo del sistema de vigilancia poscomercialización).
Una vez abordada la guía que describe el sistema de vigilancia poscomercialización, se atiende a lo detallado en el apartado 2 del artículo 72:

20
