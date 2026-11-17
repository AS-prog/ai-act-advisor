---
name: aesia-04-guia-del-sistema-de-gestion-de-la-calidad-05-reglamento-de-inteligencia-artificial-pa
description: "AESIA: aesia 04 guia del sistema de gestion de la calidad, sección «Reglamento de Inteligencia Artificial (parte 2)» (págs. 17-24). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-04-guia-del-sistema-de-gestion-de-la-calidad
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Reglamento de Inteligencia Artificial (parte 2)"
  paginas: 17-24
  origen: 2026-07-17-aesia-04-guia-del-sistema-de-gestion-de-la-calidad.pdf
  oficial: false
---
# Reglamento de Inteligencia Artificial (parte 2)

4.3 Desarrollo, control y aseguramiento de la calidad

AI Act
Art.17.1c - Sistema de gestión de calidad
Las técnicas, los procedimientos y las actuaciones sistemáticas que se utilizarán en el desarrollo y el control y el aseguramiento de la calidad del sistema de IA de alto riesgo.

Del mismo modo que el diseño se propone procedimientos sistemáticos para los tres aspectos relacionados con los requerimientos técnicos relativos a ciberseguridad, precisión y solidez, es responsabilidad del proveedor extender dichos procedimientos al proceso de desarrollo del sistema de IA.
Para ello de manera general el proveedor podría realizar un seguimiento de las especificaciones establecidas en el diseño, su traza y cumplimiento, acorde a los requerimientos que se deben cubrir, en relación con ciberseguridad, precisión y solidez.
Este seguimiento puede realizarse con diversas herramientas de mercado (open source o comerciales) que permitan definir una operativa de ML-OPS que pueda seguir la traza de las acciones realizadas desde el diseño y su implementación durante el desarrollo de la solución.
Las acciones aquí descritas, podrían estar incluidas dentro de los procesos de ML-OPS del sistema de IA, de manera iterativa en cada paso del proceso de desarrollo y garantizando que se cumplen las especificaciones establecidas en el diseño del sistema.
Específico de cada uno de los elementos que hemos considerado en anteriores apartados se puede considerar lo siguiente.
Ciberseguridad
En la guía de ciberseguridad se establece que, durante la implementación del sistema de
IA, se deben abordar la implementación de los controles de seguridad acorde a las vulnerabilidades identificadas.
Estos controles de seguridad van dirigidos a establecer salvaguardias sobre las vulnerabilidades relativas a los datos, los ataques adversarios y la explotación de fallos del sistema de IA.
Como medidas de aseguramiento de la calidad para la ciberseguridad durante el proceso de desarrollo en la guía de ciberseguridad se proponen al proveedor, entre otras, las siguientes acciones: mecánicas de equipo rojo/azul, pruebas específicas con test automáticos, SAST Y DAST continuos, análisis de vulnerabilidades conocidas tipo
CVE/VWE y pruebas de penetración genéricas y especificas al sistema de IA sobre vectores de vulnerabilidad de AI (ataques adversarios o de penetración)

16

La calidad durante el desarrollo del sistema exige un análisis de los indicadores de ciberseguridad establecidos en el cuadro de mando para garantizar que durante todo el desarrollo estos se mantienen correctos. Las evidencias del seguimiento de los indicadores de ciberseguridad y su garantía de mantenimiento es una manera de ilustrar cómo se demuestran las acciones de calidad.
Precisión
El aseguramiento de la calidad de la precisión durante el desarrollo del sistema de IA se basa en la ejecución de pruebas automatizadas o manuales diseñadas para validar, en cada etapa del desarrollo del modelo, su relación con la precisión definida en el diseño. Por ello, estas pruebas automatizadas podrían tener en cuenta los siguientes puntos:
-
-
-

El preprocesamiento de los datos (en la guía de precisión).
Durante el proceso de desarrollo, se recomienda evitar el sobreaprendizaje, detallado en la guía de precisión).
Los modelos de contraste o baseline models seleccionados, con los que se establece una comparación para el seguimiento del desarrollo y asegurar su control de calidad (ver apartado 4.1.3 de la guía de precisión).

El objetivo principal del control de calidad durante el desarrollo es asegurar que las métricas y sus valores definidos en el diseño se mantengan dentro de los rangos especificados, y que el sistema, en esta fase, funcione conforme a lo previsto o logre progresivamente el comportamiento esperado. Por lo tanto, es necesario conservar evidencia de todas las validaciones realizadas.
Solidez
El control de calidad de la solidez se establece en un procedimiento de dos pasos que se realizan durante todo el desarrollo del sistema de IA:
-
-

Verificación: Entendida como la confirmación, con la provisión de evidencias de que los requisitos especificados en el diseño se cumplen tal y como fueron establecidos.
Validación: Entendido como la confirmación de los requisitos establecidos sobre la finalidad prevista, y en relación con los criterios para la solidez que se han establecido en la fase de diseño.

Adicionalmente, en este proceso de verificación y validación, se podría tener en consideración como métricas asociadas a las ya seleccionadas dos parámetros adicionales cuyos valores pueden ser establecidos en diseño y garantizados en desarrollo:
-

-

Eficiencia: durante el desarrollo se recomienda generar en validación y en verificación evidencias de la eficiencia del sistema, como se detalla en la guía de solidez.
Rendimiento: en la sección Rendimiento en sistemas de IA se profundiza en el rendimiento relacionado con la solidez.

En el apartado Validación y Verificación, de la guía de solidez, se abordan estos dos aspectos. El proveedor durante el desarrollo del sistema deberá asegurarse que el sistema es verificado y validado, y que se registran evidencias del proceso.

17

4.4 Examen, prueba y validación

AI Act
Art.17.1d - Sistema de gestión de calidad
Los procedimientos de examen, prueba y validación que se llevarán a cabo antes, durante y después del desarrollo del sistema de IA de alto riesgo, así como la frecuencia con que tendrán lugar.
A lo largo de las guías relacionadas del sandbox relativas a ciberseguridad, precisión y solidez que acompañan a esta se han especificado las medidas de examen, prueba y validación que son de aplicación para los sistemas de IA, de acuerdo con el cumplimiento de los requerimientos establecidos en el Reglamento Europeo de IA.
Las pruebas necesarias dependerán del tipo de sistema y los riesgos identificados. Las acciones descritas a continuación combinan requisitos del Reglamento con buenas prácticas recomendadas para el sandbox.
El aseguramiento de la calidad de los controles de seguridad aplicados para mitigar las vulnerabilidades del sistema, son en sí mismos procedimientos de prueba adecuados para validar que dicha calidad se alcanza. En ese sentido, todas las pruebas realizadas en el apartado anterior, con el objetivo de garantizar la calidad durante el desarrollo podrían registrar como mínimo:
-
-
-
-
-

La versión de los datos con las que se han realizado, junto con la versión del modelo.
Los resultados esperados.
Los resultados obtenidos.
Si la prueba permite la validación del aspecto validado o no.
En caso de que no se valide, indicar la criticidad.

Para el caso de que se esté corrigiendo pruebas no exitosas anteriores, se puede incluir al menos:
-
-

La referencia de la batería de pruebas anterior en la que se registró el error
La solución aplicada para corregirlo.

No todos los sistemas requerirán el mismo nivel de complejidad en las pruebas. El alcance deberá ser proporcional al riesgo y al diseño del sistema, según el artículo 17.2.
Ciberseguridad
En el caso de ciberseguridad, su aseguramiento es en sí mismo un proceso de examen, prueba y validación pues no puede entenderse la calidad en ciberseguridad, sin que esta se encuentre constantemente tensionada y puesta a prueba. Por ello los métodos descritos en el apartado anterior son considerados como mecanismos de examen y prueba. Para asegurar que se valida adecuadamente la ciberseguridad se podría seguir el proceso de pruebas descrito en este apartado.

18

Precisión
Los procedimientos destinados al examen y prueba de la precisión son algo más específicos dada su naturaleza formal, aunque podrían registrarse y revisarse tal y como se indica en este apartado. Estos procedimientos pueden establecerse en dos grandes grupos:
-

-

Test de significancia estadística (ver apartado 4.3.2 guía de precisión). Este tipo de test permiten dar validez estadística a la validación de la métrica de precisión seleccionada. El detalle de la tipología de tipos posibles y su realización puede verse en la guía de precisión.
Benchmarks de bases de datos y modelos (ver apartado 4.3.3 de la guía de precisión). Los benchmarks dependen de la tarea y el estado del arte del campo;
por tanto, se recomienda que se actualicen conforme pasa el tiempo y los modelos y bases de datos evolucionan.

Solidez
Estas pruebas sirven para cuantificar que el sistema alcanza la solidez establecida por diseño, en todos los pasos del ciclo de vida, pero especialmente para la puesta en marcha de un sistema o la distribución de una aplicación. Estos experimentos se han de sumar a las operaciones de verificación y validación realizadas durante el desarrollo.
Los pasos en el proceso de experimentación para la solidez implican: planificar (ver Anexos de la guía de solidez), conducir los experimentos, analizar los resultados, interpretarlos y decidir sobre el resultado la acción a realizar. Durante todos estos pasos se han de dejar las evidencias necesarias de su actuación, que justifiquen el paso siguiente y las decisiones realizadas.
En el apartado 7.1.2, se aborda en detalle el proceso aquí indicado, para la realización de pruebas destinadas a garantizar la solidez del sistema acorde a los requisitos establecidos y al procedimiento de diseño referido. Es un control de calidad para la solidez del sistema que el proveedor puede implementar. Como se ha indicado han de registrarse adecuadamente los resultados de los experimentos.

4.5 Especificaciones técnicas, normas y normas armonizadas

AI Act
Art.17.1e - Sistema de gestión de calidad
Las especificaciones técnicas, incluidas las normas, que se aplicarán y, cuando las normas armonizadas pertinentes no se apliquen en su totalidad o no cubran todos los requisitos pertinentes establecidos en la sección 2, los medios que se utilizarán para velar por que el sistema de IA de alto riesgo cumpla dichos requisitos.

19

El sistema de gestión de calidad definido deberá incorporar en su documentación algunos de los siguientes elementos:
-
-

-

Cuando las haya y se hayan utilizado por parte del proveedor, listado de normas armonizadas aplicadas junto con los requisitos del Reglamento que estas cubren.
Cuando las haya y se hayan utilizado por parte del proveedor, listado de especificaciones comunes aplicadas junto con los requisitos del Reglamento que estas cubren.
Especificaciones técnicas aplicadas junto con los requisitos del Reglamento que estas cubren. En el caso de que el proveedor haya cubierto todos los requisitos del
Reglamento con la aplicación de normas armonizadas o especificaciones técnicas comunes, no será necesario indicar otras especificaciones técnicas y estándares nacionales e internacionales.

Para documentar este apartado recomendamos lo siguiente: el sistema de gestión de la calidad podría incorporar las normas armonizadas que cubren algunos o parte de los requisitos exigibles a los sistemas de IA y a su vez otra serie de normas y estándares internacionales que cubren el resto de los requisitos restantes.
Hoy en día no existen normas armonizadas aprobadas por los organismos europeos de normalización ni especificaciones comunes aprobadas por la Comisión Europea que cubran los requisitos que se exigen a los sistemas de IA por parte del Reglamento.
Mientras no existan normas armonizadas ni especificaciones comunes, o no se apliquen por el proveedor, el sistema de gestión de la calidad podría contener aquellas especificaciones técnicas que se hayan aplicado por parte del proveedor para cubrir los requisitos del Reglamento, en este caso se recomienda indicar:
-

Las especificaciones técnicas basadas en los estándares nacionales o internacionales que se hayan podido utilizar junto con los requisitos que cubren del Reglamento.

La forma de documentar esta información podría tomar como referencia la siguiente tabla
(ejemplo no real ni vinculante):
Requisito cubierto

Norma armonizada/especificación común/estándar

Artículo 12.2

Estándar nacional X

Artículos 14. Apartado 1 y 2

Norma armonizada X

Artículo 15. Apartados 1, 2 y Norma ISO X
3.

La tabla es orientativa: no todos los requisitos del Reglamento deberán vincularse necesariamente a una norma o estándar.
Para más información consulte la Guía de Evaluación de la Conformidad y la Guía de
Documentación Técnica.

20

4.6 Sistemas y procedimientos de gestión de datos

AI Act
Art.17.1f – Sistema de gestión de calidad
Los sistemas y procedimientos de gestión de datos, lo que incluye su recopilación, análisis, etiquetado, almacenamiento, filtrado, prospección, agregación, conservación y cualquier otra operación relacionada con los datos que se lleve a cabo antes de la introducción en el mercado o puesta en servicio de sistemas de IA de alto riesgo y con ese fin.
El sistema de gestión de calidad definido podrá incorporar en su documentación, los sistemas y procedimientos de gestión de datos descritos en este apartado. El artículo del
Reglamento “Datos y gobernanza de datos” recoge un listado de requisitos más amplio que todo sistema de IA de alto riesgo debe cumplir. De forma resumida, los conjuntos de datos de entrenamiento, validación y prueba se someterán a las siguientes prácticas de gobernanza y gestión de datos:
-
-
-
-
-

-

-

Elección de un diseño adecuado.
Procesos de recopilación de datos.
Operaciones de tratamiento para la preparación de los datos (la anotación, el etiquetado, la depuración, el enriquecimiento y la agregación).
Formulación de los supuestos pertinentes con respecto a la información de los datos que miden y representan.
Evaluación previa de la disponibilidad, la cantidad y la adecuación de los conjuntos de datos necesarios:
- Serán pertinentes y representativos.
- Estarán completos.
- Tendrán las propiedades estadísticas adecuadas.
- Tendrán en cuenta, en función de su finalidad prevista, las características o
elementos particulares del contexto geográfico, conductual o funcional en el que se pretende utilizar el HRAIS.
Análisis de sesgos (atendiendo aquellos que puedan afectar a la salud y la seguridad de las personas o dar lugar a algún tipo de discriminación prohibida por el Derecho de la Unión).
Detección y remediación de lagunas o deficiencias en los datos:
- Carecerán de errores.

El proveedor podrá documentar en su SGC cómo se implementan estos procesos, indicando responsables, herramientas, evidencias y criterios de revisión. Estos requisitos se recomiendan que se apliquen sin perjuicio de los principios y obligaciones del RGPD, incluyendo minimización, limitación de finalidad y evaluaciones de impacto cuando proceda

21

Además, en la medida en que sea estrictamente necesario para garantizar la vigilancia, la detección y la corrección de los sesgos, se podrán tratar las categorías especiales de datos personales, ofreciendo siempre las salvaguardias adecuadas para los derechos y las libertades fundamentales de las personas.
Para el adecuado cumplimiento de estos requisitos, a título ilustrativo y no vinculante, se ha desarrollado la “Guía de datos y gobernanza de datos”. En dicha guía se presentan las medidas que podrían implementar los proveedores y responsables del despliegue con relación al artículo “Datos y gobernanza de datos”. A modo de ejemplo, en la sección
“Documentación técnica” de dicha guía se detalla cómo se deberá abordar la documentación de cada medida.

4.7 Sistema de gestión de riesgos

AI Act
Art.17.1g – Sistema de gestión de calidad.
El sistema de gestión de riesgos que se menciona en el artículo 9.

Un sistema de gestión de riesgos tiene por objetivo la identificación y análisis de riesgos y la implementación de medidas mitigadoras. Entendemos por riesgo, cualquier factor con una probabilidad de suceder y un impacto en caso de que suceda. De hecho, el riesgo se calcula como el producto de dichos factores, probabilidad e impacto.
En el contexto del Reglamento Europeo de la IA, el sistema de gestión de riesgos que se desarrolle deberá prestar especial atención a los riesgos que puedan afectar a la salud, la seguridad y los derechos fundamentales de las personas. En este sentido, se deberá poner el foco en la identificación y análisis de cualquier riesgo que pueda tener especial afectación en los elementos mencionados. Por consiguiente, se deberán implementar las medidas adecuadas que permitan mitigar los riesgos identificados y evaluados.
Para el adecuado cumplimiento de estos requisitos se ha desarrollado la “Guía de gestión de riesgos”. En dicha guía se presentan las medidas que podrían implementar los proveedores y responsables del despliegue con relación al artículo “Sistema de gestión de riesgos”. A modo de ejemplo, en la sección “Documentación técnica” de dicha guía se detalla cómo se deberá abordar la documentación de cada medida.

22

4.8 Sistema de vigilancia poscomercialización

AI Act
Art.17.1h – Sistema de gestión de calidad
El establecimiento, la implantación y el mantenimiento de un sistema de vigilancia poscomercialización con arreglo al artículo 72.
Un sistema de vigilancia poscomercialización de sistema s de IA de alto riesgo se concibe como un conjunto de procesos y herramientas orientados a recabar datos de un sistema para transformarlos en una serie de indicadores sobre su actividad con el objetivo de supervisar los sistemas de inteligencia artificial (IA) después de su introducción en el mercado o puesta en servicio, según corresponda. El objetivo es que el proveedor pueda evaluar si los sistemas de IA cumplen los requisitos establecidos en el capítulo III, sección 2, a lo largo de todo el ciclo de vida del sistema inteligente.
Para el adecuado cumplimiento de estos requisitos se ha desarrollado la “Guía de sistema de vigilancia poscomercialización”. En dicha guía se presentan las medidas que podrían implementar los proveedores y responsables del despliegue con relación al artículo
“Vigilancia poscomercialización”. El sistema de vigilancia se articula principalmente a través del proveedor, sin perjuicio de las obligaciones de uso, supervisión y notificación que corresponden al responsable del despliegue. A modo de ejemplo, en la sección
“Documentación técnica” de dicha guía se detalla cómo se deberá abordar la documentación de cada medida.

4.9 Notificación de incidentes graves

AI Act
Art.17.1i – Sistema de gestión de calidad
Los procedimientos asociados a la notificación de un incidente grave con arreglo al artículo 73.
La guía de gestión de incidentes establece en su apartado 4.1.1, cómo abordar los requisitos de notificación de incidentes graves acorde al Reglamento Europeo de IA. En dicho apartado se describe el procedimiento de notificación de incidentes graves, y las medidas que permiten abordar dicho procedimiento. Un aspecto importante de los procedimientos de notificación de incidentes es que también implican al responsable del despliegue, en la medida en la que este es responsable de notificar al proveedor del sistema de IA a través del canal establecido para ello. Especial atención requiere el apartado 4.1.1 de la citada guía que resume de manera visual el procedimiento de
23
