---
name: aesia-13-guia-vigilancia-poscomercializacion-05-reglamento-de-inteligencia-artificial-pa
description: "AESIA: aesia 13 guia vigilancia poscomercializacion, sección «Reglamento de Inteligencia Artificial (parte 2)» (págs. 20-25). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-13-guia-vigilancia-poscomercializacion
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Reglamento de Inteligencia Artificial (parte 2)"
  paginas: 20-25
  origen: 2026-07-17-aesia-13-guia-vigilancia-poscomercializacion.pdf
  oficial: false
---
# Reglamento de Inteligencia Artificial (parte 2)

Existen varias técnicas para evaluar el rendimiento y la precisión de un sistema de IA, algunas de las cuales incluyen:
-

-

Pruebas de rendimiento: se utilizan para medir el tiempo de respuesta del sistema y su capacidad para manejar grandes cantidades de datos. Son las conocidas pruebas de estrés que permiten llevar al límite el sistema inteligente en un entorno de prueba y valorar la respuesta ofrecida ante dicho escenario.
Pruebas de precisión: se utilizan para medir la precisión del sistema al realizar tareas específicas, como el reconocimiento de objetos en imágenes o la traducción de idiomas. En concreto, se deberá seleccionar previamente las métricas de precisión asociadas al modelo de IA (sección de la Guía de Precisión: “Métricas de precisión asociadas al modelo de IA”) y los niveles de precisión pertinentes para el sistema
(sección de la Guía de Precisión: “Niveles de Precisión, Documentación y
Monitorización de los modelos de IA.”).

No obstante, en algunos casos, medir la precisión del algoritmo puede ser muy complicado debido al caso de uso en sí, como puede verse en el siguiente ejemplo.

Ejemplo – Sistema de evaluación para la promoción de personal
Siguiendo con el ejemplo propuesto del sistema inteligente de promoción, ¿Cómo podríamos evaluar si el sistema inteligente ha acertado o no en su predicción? ¿Cómo podemos valorar que ha acertado al no promocionar a un empleado en particular? En estos casos se recomienda mantener una muestra control que siga el procedimiento anterior a la implantación del sistema para poder comparar los resultados obtenidos con los que hubiera ofrecido el sistema. Para ello, se dejaría una muestra de los empleados para ser evaluada y promocionada de forma manual y tras dicho proceso se evaluaría las decisiones que hubiera tomado el modelo en base a las métricas anteriores frente a las decisiones manuales obtenidas por el equipo de RRHH.

Además de las pruebas anteriores hay que tener en cuenta las siguientes recomendaciones:
-

-

Histórico de resultados: Tal y como indica la Guía de Precisión en su sección
“Medidas técnicas Generales”, se deberá de contar con un historial de los resultados obtenidos en las pruebas anteriores para descubrir tendencias de reducción de rendimiento de forma temprana. A modo de ejemplo, si los encargados del sistema de promoción realizarán el primer mes de despliegue en producción de un sistema inteligente diferentes pruebas obteniendo una precisión del 99.8%, 99.6% y 99.2% de forma sucesiva, si el criterio mínimo de precisión fuera del 98%, esta tendencia de pérdida de rendimiento podría pasar desapercibida. Sin embargo, al contar con un historial de pruebas se podrá observar la tendencia en los resultados.
Especial cuidado con la mejora en las métricas sin variación del sistema: en algunos casos puede que las decisiones tomadas por los resultados del sistema inteligente

19

produzcan una tendencia a la mejora de las métricas del sistema buscando de forma indirecta las entradas que se adaptan a la mejora del rendimiento del algoritmo.

Ejemplo – Sistema de evaluación para la promoción de personal
Siguiendo con nuestro ejemplo, si el sistema de selección de candidatos de promoción se reentrenara sobre datos sobre los que ha predicho, se estaría sesgando a sí mismo.
Es decir, si el algoritmo da una mayor probabilidad a empleados con unas determinadas características, estos terminan siendo ascendidos y el sistema es de nuevo entrenado sobre los resultados obtenidos, irá progresivamente sesgando hacia las decisiones que tomó de forma inicial acrecentando su seguridad. Este escenario puede corregirse a través del entrenamiento sobre una muestra de control que ha sido promocionada a través de expertos en recursos humanos.

4.3 Informes de incidentes
A la hora de establecer un sistema de recopilación y análisis de informes de incidentes relacionados con el sistema de IA ofrecemos las siguientes recomendaciones:
Definir los objetivos del sistema: determinar los objetivos del sistema de recopilación y análisis de incidentes. Es decir, responder a la siguiente pregunta: ¿Qué información se espera recopilar y cómo se utilizará esta información?
Diseño del sistema: definición del proceso de recopilación y análisis de los informes de incidentes. Esto incluye establecer los procesos para reportar incidentes, la estructura de los informes y los mecanismos de análisis de datos.
Implementación del sistema: Incluye el desarrollo de una plataforma para recopilar y almacenar los informes, así como crear herramientas de análisis de datos.
Capacitación: Se debe trabajar en la formación de las personas involucradas en el sistema, incluyendo a los usuarios finales, los administradores del sistema y el equipo de análisis de datos.
Vigilar continuamente: Esta vigilancia incluye: recolectar retroalimentación de los usuarios, revisar los informes de incidentes y analizar las tendencias para identificar posibles problemas y oportunidades de mejora.

20

Ejemplo – Bomba de insulina inteligente
Tras la detección de un comportamiento anómalo en la bomba de insulina inteligente se ha generado un informe con la siguiente información:
-

Características y objetivos del sistema: una descripción del sistema en cuestión para facilitar la evaluación de impacto por parte de personas sin conocimientos relacionados con el sistema. Esta información debe de estar previamente cumplimentada en el informe.

-

Comportamiento anómalo detectado: en este caso el indicador anómalo ha sido el número de predicciones por minuto de la bomba. También se describe información del contexto como el número de sistemas afectados, inicio de la anomalía, impacto producido y demás factores relacionados que puedan ayudar a la comprensión de la situación.

-

Acciones desarrolladas hasta el momento: se ha revisado la interfaz de monitorización y los registros de indicadores. El problema se ha producido en un solo dispositivo y se requiere de una revisión in situ.

-

Otras secciones que puedan ofrecer más contexto de la anomalía detectada en el sistema inteligente:
-

Configuración y Ajustes del Sistema en el momento en el que se produjo el comportamiento anómalo.

-

Extracto del histórico de registros e indicadores del sistema inteligente.

-

Notas de los supervisores que puedan añadir contexto a la situación.

Una vez completado el informe se deberá de trasladar a través del sistema de envío predefinido.

4.4 Comunicación transparente
La comunicación de las características del sistema, el rendimiento de este y las consecuencias de su uso en producción deberían adaptarse al receptor de dicha información para facilitar una comprensión correcta de todas las implicaciones de su empleo.
Medidas para llevarlo a cabo
Es importante proporcionar información clara y transparente sobre el rendimiento y la seguridad del sistema de IA a los responsables del despliegue, reguladores y otros interesados. Para ello se recomienda establecer indicadores de rendimiento y seguridad claros y cuantificables para medir el rendimiento y la seguridad del sistema de IA. Estos indicadores deberían ser relevantes para los responsables del despliegue, reguladores y otros interesados.

21

Por otro lado, también es relevante la recopilación de datos sobre el rendimiento y la seguridad del sistema de IA, así como su posterior análisis, con el fin de obtener información sobre su desempeño.
Como medida destacada en este ámbito, pero no de carácter obligatorio, resulta fundamental ofrecer información clara sobre el rendimiento y la seguridad del sistema de
IA a los responsables del despliegue, los reguladores y otros interesados. Esto puede incluir informes periódicos, paneles de seguimiento o un sitio web dedicado.
En este sentido, es recomendable proporcionar detalles sobre el funcionamiento del sistema, incluyendo su algoritmo, los datos que utiliza y las decisiones que toma. Esto ayudará a los distintos interesados a comprender mejor el sistema y a evaluar su rendimiento y su seguridad.

Ejemplo – Sistema de evaluación para la promoción de personal
Un ejemplo de estas medidas, empleando el ejemplo del sistema de promoción de empleados, sería la adaptación en la forma de comunicar las métricas de precisión por parte de los supervisores del sistema a la hora de ser reportada a los decisores de este.
En este caso, en lugar de mencionar que:
“El sistema inteligente cuenta con un 96% de precisión” se podría digerir el mensaje para indicar que:
“El sistema inteligente cuenta con un 96% de precisión, es decir, de cada 100 empleados que el sistema indicó que deberían de ser promocionados el sistema acertó en 96 de ellos y cometió error en indicar una promoción para 4 de ellos. Sin embargo, esta métrica no considera los errores que se produjeron entre los empleados que no fueron promocionados y se deben de considerar otras métricas junto con la actual.”

4.5 Capacitación
A la hora de capacitar a los supervisores conviene proporcionar una formación básica sobre cómo funciona el sistema de IA y cómo se utiliza. Esto incluye información sobre los algoritmos utilizados, los datos que se utilizan y cómo se toman decisiones. También es importante proporcionar ejemplos de funcionamiento anómalo, incluyendo ejemplos de errores, fallos y comportamiento inesperado.

22

Ejemplo – Sistema de evaluación para la promoción de personal
En el caso del ejemplo, el proveedor del sistema inteligente de selección de personal para promociones internas debería contar con supervisores con los siguientes requisitos:
-

Formación acerca del contexto en el que se está empleando el sistema y las consecuencias devenidas de las predicciones generadas para los empleados.

-

Conocer los datos que está teniendo en consideración para llevar a cabo las predicciones (experiencia del empleado, proyectos realizados, disponibilidad de traslado entre otras) y cómo pueden verse afectadas por factores externos
(latencia en la introducción de nuevas actualizaciones en los CV de los empleados por parte del equipo de recursos humanos).
Comprensión acerca del algoritmo o algoritmos empleados en el sistema y qué sistema emplea para la generalización de conocimiento sobre los empleados. A modo de ejemplo, conocer que se trata de un algoritmo basado en reglas ayudará.

-

Experiencia a través de ejemplos audiovisuales o en escenarios prácticos de comportamientos anómalos del sistema inteligente en el que no genere una predicción adecuada para los empleados o no permita realizar predicciones por una sobrecarga de la infraestructura y cómo deberían de actuar en tal caso.

Por la parte de los propios usuarios del sistema, los especialistas de recursos humanos, también se deberían de formar en la detección de este tipo de escenarios y las medidas adecuadas para reportar cualquier situación anómala al proveedor del servicio.

4.6 Flexibilidad
Mantener un plan flexible y escalable es fundamental para mejorar la vigilancia del sistema.
Por un lado, se encuentra el hecho de que los sistemas de IA están en constante evolución y mejora, por lo que esta característica puede permitirle adoptar nuevas tecnologías y técnicas para mejorar el rendimiento. Igualmente, en cuestiones de seguridad, la flexibilidad permite adaptarse a nuevas amenazas y vulnerabilidades, así como garantizar la protección de los datos y la privacidad de los usuarios, y adaptarse a nuevos cambios en la regulación.
En definitiva, la flexibilidad es la adaptación del sistema inteligente a los cambios internos y externos que puedan afectar a su funcionamiento.
Medidas recomendadas para llevarlo a cabo a) Identificar las regulaciones aplicables: Incluye las regulaciones sectoriales y las regulaciones de protección de datos.
b) Evaluar el rendimiento y la seguridad del sistema: se recomienda la utilización de indicadores de rendimiento y seguridad claros y cuantificables.

23

c) Identificar los riesgos: Incluye los riesgos de rendimiento y los riesgos de seguridad.
d) Establecer procedimientos para prevenir los riesgos: Incluye procedimientos para comunicar incidentes, investigar incidentes e implementar soluciones.
e) Vigilar el cumplimiento con la regulación existente: Incluye el cumplimiento de las regulaciones sectoriales y las regulaciones de protección de datos.
f) Establecer un plan de contingencia: Esta cuestión es importante con el objetivo de prevenir incidentes o fallos críticos en el sistema de IA.
g) Implementar un sistema de revisión continua: Su objetivo es la evaluación del rendimiento y la seguridad del sistema de IA, identificar problemas y tomar medidas para mejorarlo.
h) Formación específica sobre las regulaciones existentes en IA, y protección de datos, además de ‘mejores prácticas’ (Ética en IA).

Ejemplo – Sistema de evaluación para la promoción de personal
La empresa proveedora del sistema inteligente de promoción de empleados tiene un cambio en su dirección y en su política de incorporación y promoción de empleados, tras producirse una fusión con otra empresa cuyos datos no han sido incorporados al sistema. El proveedor deberá adaptar el plan de vigilancia y el sistema de vigilancia a los nuevos cambios:
-

Evaluar si tras la incorporación existen nuevas regulaciones aplicables.

-

Revisar que los indicadores sigan siendo los adecuados para una vigilancia adecuada en base a la nueva evaluación de riesgos.

-

Llevar a cabo las actividades formativas necesarias en el caso de que se incorporen al equipo de supervisión miembros de la nueva empresa.

-

Revisar los procedimientos de notificación si es necesario incluir nuevos decisores en la cadena de comunicación.

-

Evaluar si la infraestructura sobre la que está alojada el sistema de vigilancia debe de ser actualizada con nuevas conexiones.

-

Todas aquellas medidas destinadas a mantener activo el sistema y el plan de vigilancia.

24
