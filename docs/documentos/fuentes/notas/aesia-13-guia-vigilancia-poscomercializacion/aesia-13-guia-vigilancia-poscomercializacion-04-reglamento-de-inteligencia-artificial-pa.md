---
name: aesia-13-guia-vigilancia-poscomercializacion-04-reglamento-de-inteligencia-artificial-pa
description: "AESIA: aesia 13 guia vigilancia poscomercializacion, sección «Reglamento de Inteligencia Artificial (parte 1)» (págs. 12-19). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-13-guia-vigilancia-poscomercializacion
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Reglamento de Inteligencia Artificial (parte 1)"
  paginas: 12-19
  origen: 2026-07-17-aesia-13-guia-vigilancia-poscomercializacion.pdf
  oficial: false
---
# Reglamento de Inteligencia Artificial (parte 1)

3. Reglamento de Inteligencia
Artificial
3.1 Análisis previo y relación de los artículos
En esta sección se simplifica y estructura el contenido del artículo con el objetivo de facilitar su comprensión. Asimismo, se presenta la estructura seguida en esta guía para dar cobertura al contenido de dicho artículo.
Qué entendemos del artículo
El artículo aborda los factores exigidos para la implementación y documentación de sistemas de vigilancia poscomercialización para sistemas de IA de alto riesgo. Con ello, pretende garantizar que dichos sistemas continúen cumpliendo con los requisitos necesarios establecidos en el AI Act una vez puestos en el mercado, y durante todo el ciclo de vida del sistema.
Qué medidas clave entendemos que establece el artículo
-
-
-
-

Establecimiento de sistemas de vigilancia proporcionales a los riesgos.
Recopilación, documentación y análisis de datos relevantes sobre el rendimiento de los sistemas de IA.
Creación de un plan de vigilancia poscomercialización como parte de la documentación técnica.
Aceptación de documentación de vigilancia existente si esta cumple con ciertos actos legislativos y regulaciones financieras.

11

3.2 Contenido de los artículos en el Reglamento de IA

AI Act
Art.72 Vigilancia poscomercialización por parte de los proveedores y plan de vigilancia poscomercialización para sistemas de IA de alto riesgo
1. Los proveedores establecerán y documentarán un sistema de vigilancia poscomercialización de forma proporcionada a la naturaleza de las tecnologías de IA y a los riesgos de los sistemas de IA de alto riesgo.
2. El sistema de vigilancia poscomercialización recopilará, documentará y analizará de manera activa y sistemática los datos pertinentes que pueden facilitar los responsables del despliegue o que pueden recopilarse a través de otras fuentes sobre el funcionamiento de los sistemas de IA de alto riesgo durante toda su vida útil, y que permiten al proveedor evaluar el cumplimiento permanente de los requisitos establecidos en el capítulo III, sección 2, por parte de los sistemas de IA. Cuando proceda, la vigilancia poscomercialización incluirá un análisis de la interacción con otros sistemas de IA. Esta obligación no comprenderá los datos operativos sensibles de los responsables del despliegue que sean autoridades garantes del cumplimiento del Derecho.
3. El sistema de vigilancia poscomercialización se basará en un plan de vigilancia poscomercialización. El plan de vigilancia poscomercialización formará parte de la documentación técnica a que se refiere el anexo IV. La
Comisión ofrecerá orientaciones de contenido mínimo para el plan de vigilancia poscomercialización y la lista de elementos que deberán incluirse en él, sin que en ningún caso tenga carácter vinculante en términos de formato y contenido, dando libertad en cuanto a su formato a las entidades.
4. En el caso de los sistemas de IA de alto riesgo regulados por los actos legislativos de armonización de la Unión enumerados en el anexo I, sección A, cuando ya se haya establecido un sistema y un plan de vigilancia poscomercialización con arreglo a dichos actos, con el fin de garantizar la coherencia, evitar duplicidades y reducir al mínimo las cargas adicionales, los proveedores podrán optar por integrar, según proceda, los elementos necesarios descritos en los apartados 1, 2 y 3, utilizando el modelo a que se refiere el apartado 3, en los sistemas y planes que ya existan en virtud de dicha legislación, siempre que alcance un nivel de protección equivalente.
El párrafo primero del presente apartado también se aplicará a los sistemas de
IA de alto riesgo a que se refiere el anexo III, punto 5, introducidos en el mercado o puestos en servicio por entidades financieras sujetas a requisitos relativos a su gobernanza, sus sistemas o sus procesos internos en virtud del
Derecho de la Unión en materia de servicios financieros.
12

3.3 Correspondencia del articulado con los apartados de la guía
En esta tabla se detalla la correspondencia de las secciones de esta guía que abordan los elementos de dicho artículo:
Artículo
Reglamento

Requerimiento Reglamento

Sección guía

72.1

Proporcionalidad del sistema de vigilancia poscomercialización en base a la naturaleza de las tecnologías de IA aplicadas.

72.2

Datos facilitados por los responsables del despliegue o recopilados a través del sistema de vigilancia sobre el funcionamiento de los sistemas de IA de alto riesgo durante toda su vida útil.

Apartado 4.1 y
Apartado 4.2

72.3

El Plan de vigilancia poscomercialización formará parte de la documentación técnica al que se refiere el anexo
IV.

Apartado 6

72.4

Documentación específica de sistemas de IA de alto riesgo regulados por los actos legislativos de armonización de la Unión enumerados en el anexo I, sección A y en el Anexo III.5 introducidos en el mercado o puestos en servicio por entidades financieras.

Apartado 6

Apartado 4

13

4. ¿Qué elementos implantar y cómo puedo hacerlo para desarrollar un adecuado sistema de vigilancia poscomercialización?
En base a lo comentado en el punto 1 acerca de qué es un sistema de vigilancia poscomercialización y qué componentes debe de tener, podemos seguir el siguiente diagrama de flujo en su diseño:

¿Cómo implementar el sistema de vigilancia poscomercialización?
Para poder llevar a cabo las principales actividades de vigilancia, el proveedor deberá diseñar, desplegar y validar los componentes que forman parte del sistema. En concreto:
14

1. Selección de indicadores: se deberá establecer cuáles son los indicadores más relevantes para la correcta vigilancia del sistema (véase Anexo A de la presente guía: “Indicadores de vigilancia”).
La selección de estos indicadores podrá basarse en el sistema de gestión de riesgos previamente desarrollado.
Una vez seleccionados, el sistema inteligente deberá generar registros con la información asociada a dichos indicadores, pudiendo basarse en las recomendaciones técnicas de la Guía de Registros: “¿Qué elementos debo implantar y cómo debo hacerlo para desarrollar un adecuado sistema de gestión de registros?”.
Tras concretar el diseño de los registros, el sistema inteligente deberá depositarlos en un archivo de log temporal o similar para que el sistema de captación comience su procesamiento.
También puede darse el caso de que el propio sistema inteligente envíe directamente los registros al sistema de registro de indicadores, sin necesidad de utilizar un archivo temporal. Ambas opciones son válidas y dependerán de la arquitectura del sistema inteligente.
2. Desarrollo de sistemas de captación y envío de indicadores: Los sistemas de captación recolectarán los datos de los archivos logs donde sean depositados por parte del sistema inteligente y serán enviados a los sistemas de registro de indicadores. Estos sistemas deberían prestar especial atención a la seguridad en el envío de registros.
3. Sistema de registro de indicadores: Conviene implementar un sistema de gestión de registros donde los sistemas de captación de indicadores enviarán los datos generados por el sistema. Este sistema podrá ser cualquier tipo de base de datos estructurada o no estructurada de almacenamiento de registros. Además, se tendrán que establecer las políticas de control de acceso, retención y eliminación de dichos registros tal como indica la Guía de Registros.
4. Desarrollo conjunto del sistema de alertas y la interfaz de análisis para supervisores: A partir de los registros se recomienda contar con un sistema de vigilancia de indicadores para la alerta temprana frente a valores anómalos. Se podrá desarrollar una solución propia o emplear alguna de las soluciones de visualización y vigilancia de registros. Se deberá de contar tanto con:
a. Un sistema de alerta asignado a los supervisores del sistema. Se recomienda que el sistema envíe las alertas por diferentes medios de comunicación y notifique también periódicamente sobre el comportamiento adecuado del sistema.
b. Una interfaz para la supervisión en tiempo real de los indicadores del sistema. Dicha interfaz deberá mostrar de forma evidente cuándo uno de los indicadores del sistema se encuentra fuera de la escala esperada. También deberá permitir la exploración manual de los registros para realizar una inspección más profunda sobre los datos recabados.
15

Se recomienda que todos los componentes del sistema cuenten con tests de funcionalidad a nivel de unidad y de integración con el resto para asegurar el correcto funcionamiento del sistema de vigilancia.
Antes de llevar a cabo el diseño y la implementación de dicho sistema de vigilancia, se debería establecer un plan de vigilancia poscomercialización en el que se aconseja incluir las siguientes labores y características: vigilancia continua, vigilancia periódica, informe de incidentes, comunicación transparente, capacitación, flexibilidad y evaluación independiente (si es posible). A continuación, se describen los elementos enumerados:
-

-
-

-

-

-

Vigilancia continua: monitorear el rendimiento y el comportamiento del sistema de
IA en un entorno de producción para detectar y corregir problemas a partir de los indicadores seleccionados en la evaluación de riesgos.
Vigilancia periódica: llevar a cabo evaluaciones regulares para medir el rendimiento y la precisión del sistema de IA y detectar cualquier problema.
Informes de incidentes: establecer un sistema para recopilar y analizar informes de incidentes relacionados con el sistema de IA, incluidos errores, problemas relativos a la privacidad y la seguridad.
Comunicación transparente: proporcionar, a través de los informes, información clara y transparente sobre el rendimiento y la seguridad del sistema de IA a los usuarios, reguladores y otros interesados.
Capacitación: capacitar a los usuarios y operadores del sistema de IA para que puedan detectar y manejar problemas asociados al funcionamiento anómalo del sistema.
Flexibilidad: tener un plan flexible y escalable para adaptarse a los cambios en el rendimiento y la seguridad del sistema de IA y para cumplir con las regulaciones actuales y futuras.

En el caso de que fuera posible, sería valorable una evaluación independiente, que pudiera proporcionar una visión objetiva sobre su rendimiento y seguridad. Por ejemplo, la consecución de un sello o certificación que dé garantía de ello por parte de una entidad acreditada.
Las siguientes secciones desarrollan cada uno de estos elementos en mayor profundidad.
Posteriormente, en la sección 4 de “Documentación técnica” se indicará la manera en la que documentar tanto el sistema de vigilancia como el plan de vigilancia propuesto.

4.1 Vigilancia continua
La vigilancia continua de los sistemas de IA de alto riesgo es necesaria para garantizar que el sistema continúe funcionando de manera segura y eficaz una vez en el mercado, y para evitar problemas de rendimiento, seguridad y responsabilidad legal. Esta vigilancia resulta especialmente relevante ante cambios abruptos en el comportamiento del sistema.
Hay que tener en cuenta que los sistemas de IA operan en entornos cambiantes, y pueden verse afectados por cambios en los datos de entrada, las condiciones del entorno, y las

16

regulaciones. La vigilancia continua de los indicadores seleccionados tras la evaluación de riesgos permite detectar y corregir problemas relacionados con estos cambios.
Además, los sistemas de IA pueden experimentar problemas de rendimiento debido a una variedad de factores, como el envejecimiento de los datos de entrenamiento, el uso de datos de entrenamiento insuficientes o inexactos, o la falta de capacitación adecuada. La vigilancia continua permite detectar y corregir problemas de rendimiento antes de que afecten significativamente el sistema.
No se debe olvidar que estos sistemas pueden ser objeto de ataques maliciosos, como el aprendizaje adversarial, el phishing, y el robo de datos. La vigilancia continua permite detectar y corregir problemas de seguridad antes de que causen daños significativos.
Medidas para llevarlo a cabo
Entre las técnicas existentes para monitorizar el rendimiento y el comportamiento de un sistema de IA en un entorno de producción se destacan las siguientes:
-

-

-

-
-

Vigilar los indicadores del sistema inteligente: consiste en la recopilación y análisis de datos sobre el rendimiento y el comportamiento del sistema de IA para detectar patrones y tendencias. Se pueden utilizar herramientas de análisis de datos para detectar problemas, como errores y desviaciones.
Vigilar los indicadores sobre las acciones de los usuarios: recopilación de información sobre cómo los usuarios interactúan con el sistema de IA, incluidos los comandos, las consultas y las respuestas. Esto puede ayudar a detectar problemas de usabilidad y a proporcionar retroalimentación para mejorar el sistema.
Vigilar los indicadores de la infraestructura: monitorizar el estado de los componentes del sistema de IA, como la CPU, la memoria y el almacenamiento, para detectar problemas de rendimiento y capacidad.
Vigilar los indicadores de seguridad: El objetivo es detectar y prevenir brechas en la seguridad, incluidos ataques de phishing, fuerza bruta y malwares.
Supervisión de cambios en los indicadores mediante alertas: configuración de alertas para detectar eventos anómalos, como errores, violaciones de seguridad y problemas de privacidad. Esto puede incluir la configuración de reglas para detectar patrones específicos o la configuración de umbrales para detectar desviaciones.

Ejemplo – Bomba de insulina inteligente
Usando el ejemplo de la bomba de insulina inteligente, la monitorización continua se centraría en la supervisión de los indicadores seleccionados para evitar cambios de rendimiento abruptos.
Supongamos que el indicador de número de predicciones, que de forma continuada tenía valores cercanos a 45 predicciones por minuto, ha pasado a ser 3640 predicciones por minuto.

17

Primero, los registros con los indicadores serán transferidos por el sistema de captación y envío de indicadores al sistema de gestión de registros a través de un protocolo de comunicación seguro. Posteriormente, el sistema de alertas analizará los datos obtenidos y detectará la anomalía respecto a la escala de normalidad del indicador en base a las reglas preestablecidas en su diseño. Por último, el sistema de alertas lanzará las notificaciones a los supervisores a través de los medios definidos en su diseño:
emails, SMS o cualquier otro sistema de comunicación de la organización.
Tras la notificación el equipo responsable de supervisión evaluará a través de la interfaz de supervisión los indicadores captados y procederá a la revisión del sistema.

4.2 Vigilancia periódica
La realización de evaluaciones regulares para medir el rendimiento y la precisión del sistema de inteligencia artificial es esencial para garantizar que este sigue siendo preciso, escalable y útil en un entorno real, una revisión más dilatada en el tiempo, dependiendo dicha periodicidad de las características del propio sistema, permitiendo detectar problemas temprano y tomar medidas para corregirlos.
Por un lado, es importante asegurar la precisión del sistema: a través de pruebas de precisión, por ejemplo, se puede evaluar cómo el sistema está realizando tareas específicas, como el reconocimiento de objetos en imágenes o la traducción de idiomas, y detectar si hay algún problema que esté afectando su precisión.
Además, también es necesario identificar problemas con antelación: esto se puede conseguir realizando pruebas de seguimiento, se puede monitorear el rendimiento del sistema en el tiempo, detectando cualquier disminución en la precisión o el rendimiento, lo cual permite detectar con antelación posibles problemas y tomar medidas para corregirlos antes de que se vuelvan graves. Estas medidas deben servir como ejemplo y no tienen que ser aplicadas necesariamente
También permite asegurar la escalabilidad del sistema: a través de pruebas de rendimiento, se puede evaluar cómo el sistema está manejando grandes cantidades de datos y detectar cualquier problema que pueda afectar su capacidad para escalar.

Ejemplo – Sistema de evaluación para la promoción de personal
Empleando el ejemplo del sistema de promoción de personal, el sistema inteligente podría perder rendimiento al no reentrenar el sistema durante años y tomar decisiones de promoción que terminan en despidos o equipos poco cohesionados. La monitorización periódica de las métricas de rendimiento permitirá evaluar su utilidad y prevenir este tipo de escenarios.

Medidas para llevarlo a cabo

18
