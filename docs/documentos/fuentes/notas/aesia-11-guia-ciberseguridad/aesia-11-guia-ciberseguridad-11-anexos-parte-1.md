---
name: aesia-11-guia-ciberseguridad-11-anexos-parte-1
description: "AESIA: aesia 11 guia ciberseguridad, sección «Anexos (parte 1)» (págs. 54-61). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-11-guia-ciberseguridad
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Anexos (parte 1)"
  paginas: 54-61
  origen: 2026-07-17-aesia-11-guia-ciberseguridad.pdf
  oficial: false
---
# Anexos (parte 1)

- Los activos y actores identificados en el análisis de ciberseguridad.
- Las vulnerabilidades identificadas y los controles aplicados sobre los datos para los
ataques de envenenamiento.
- Las vulnerabilidades identificadas y los controles aplicados para la protección frente
a ataques adversarios.
- Las vulnerabilidades y controles asociados a los defectos del modelo, incluyendo
las medidas de prevención y detección implementadas.
Además, esta documentación puede tomar como referencia los procedimientos e indicaciones proporcionados en esta guía, especificando las técnicas utilizadas para evaluar y mitigar riesgos, su relación directa con los riesgos mitigados y las vulnerabilidades abordadas y un enfoque claro para su mantenimiento y actualización en el ciclo de vida del sistema.

53

6. Cuestionario de autoevaluación
Para realizar una autoevaluación del cumplimiento de los requisitos del Reglamento de
Inteligencia Artificial referidos en esta guía, a título orientativo y no vinculante se ha generado un cuestionario de autoevaluación global. Este cuestionario incluye, a modo de ejemplo, una serie de preguntas con los puntos clave a tener en cuenta respecto a las obligaciones que dictaminan los artículos del Reglamento de IA mencionados en esta guía.

54

7. Anexos
7.1 Anexo I: Políticas de acceso. Una aproximación a sistemas de inteligencia artificial de alto riesgo
Podemos decir que la primera y autentica línea de defensa respecto a muchas de las medidas específicas de IA, se basa en controlar de manera adecuada el acceso a todos los activos durante el ciclo de vida.
Las políticas de acceso, aun no tratándose de un tema específico de inteligencia artificial, se encuentran lo suficientemente cerca de todos los activos y procesos a lo largo del ciclo de vida para dedicarle un enfoque que permita trazar a la organización una continuidad que asegure la protección.

7.1.1 Para el proveedor
Las políticas de acceso, entendidas como las reglas de acceso a los activos, así como las reglas de acción sobre estos son muy importantes a la hora de aplicar medidas específicas de ciberseguridad a los sistemas de IA de alto riesgo. Estas políticas establecen qué puede hacerse y quién puede hacerlo sobre los activos del sistema de IA y procesos del ciclo de vida de este. Los activos protegidos son cruciales en la ciberseguridad del sistema. Dejarlos expuestos es un riesgo inasumible para cualquier sistema de IA.
Se recomienda que las políticas de acceso se sustenten sobre el paradigma RBAC (Sistema de acceso basado en roles), que permita asignar roles a los responsables del despliegue y acciones permitidas a dichos roles.
El enfoque de las políticas de acceso se recomienda que sea debe ser de mínimos privilegios y se establezca un mecanismo de autentificación robusto, rotación de contraseñas y/o acceso mediante certificados en función del sistema. Se recomienda la inclusión de un sistema de factor múltiple de autenticación, que evite la suplantación, por un compromiso de una contraseña. Las políticas de revocación de accesos pueden formar parte de los mecanismos de salida de la compañía para evitar la existencia de accesos para personas que ya no están en la organización.
Se recomienda que sea compatible con soluciones de gestión de identidad de mercado, extendidas en las organizaciones, como puede ser Active Directory o equivalente. Dicha integración se recomienda que esté documentada en el manual de instrucciones para facilitar el proceso a los usuarios del sistema.
¿A quién aplica dentro de la organización?
Se recomienda que las políticas de acceso al sistema de IA apliquen a todo el personal que tenga interacción con el sistema a cualquier nivel desde su desarrollo, implementación y

55

comercialización. Es muy importante trasladar a cada uno de los grupos de actores indicados los mínimos privilegios posibles.
Estos grupos podrán ser:
- Actores sobre datos: perfiles que actúen sobre los datos que alimentan el
aprendizaje del sistema de IA (Analistas de datos, Científicos de datos, Expertos en
IA, etc.)
- Actores sobre la configuración y operación del sistema de IA (Expertos en AI,
Administradores del sistema de IA, Analistas de sistemas, Expertos en ML, etc.)
- Desarrolladores de integración y/o interacción con el sistema de IA (Incluido
MLOps, en su caso).
- Actores de administración de sistemas que hospedan y operan el sistema de IA
(Administradores del sistema de IA, Analistas de sistemas, etc.)
- Actores sobre el diseño, implementación y mantenimiento del software que
materializa el sistema de IA en sí mismo (Incluido en su caso el uso de firmware o similares) (Desarrolladores, Analistas, Expertos en IA, etc.).
- Actores sobre la arquitectura, administración y mantenimiento del sistema de IA en
su ciclo de vida, tanto durante el desarrollo como una vez puesto en marcha
(Expertos en AI, Administradores del sistema de IA, Expertos en ML, etc.).
- El personal general de la organización aplicando la política de mínimos privilegios,
no deberá tener acceso al sistema de IA, al desarrollo del modelo o a los datos. En aquellos casos fuera de los actores identificados en los puntos anteriores, el acceso debe analizarse y registrar la necesidad, si esta es temporal deberá revocarse adecuadamente.
A modo orientativo se puede consultar la ISO/IEC 22989:2022 Information technology —
Artificial Intelligence — Artificial intelligence concepts and terminology
¿Qué aspectos se recomienda que cubra?
Las políticas de acceso establecidas sobre cualquiera de los activos descritos en este apartado se recomiendan que se revisen periódicamente estando actualizados los siguientes puntos:
- Personas y roles asignados, actualización y cambios.
- Roles definidos y acciones.
- Proceso de revocación y eliminación de permisos.
- Permisos sin asignación a un usuario.
- Sistema de registro de accesos y monitorización de uso.
Las acciones sobre datos de entrenamiento pueden estar protegido por las políticas de seguridad, considerando al menos:
- Incorporación de nuevos datos.
- Eliminación de datos existentes.
- Edición de datos existentes.

56

- Utilización de los datos.
La segmentación de las acciones sobre datos es fundamental para tener un control y protección sobre los riesgos del envenenamiento de datos.
Se recomienda que el modelo como parte fundamental del sistema de inteligencia artificial esté protegido por las políticas de seguridad. Se pueden controlar al menos, las siguientes acciones:
-
-
-
-
-
-

Acceso (visualización) al código del modelo.
Edición del código del modelo.
Utilización de modelo para entrenamiento.
Proceso de entrenamiento.
Validación y despliegue (liberación) del modelo a producción.
Acceso, edición y supresión de cualquier documentación técnica y de diseño relativa al modelo y descriptiva de la naturaleza del sistema y sus componentes.

La segmentación de las acciones sobre el propio modelo permite proteger a este de manipulaciones inadvertidas del mismo, tanto intencionadas realizadas por atacantes malintencionados, como erróneas por personas no cualificadas (sin el permiso establecido)
introduciendo errores en el modelo. Se recomienda evitar la exfiltración de este para ataques de transferencia y controla el proceso de entrenamiento para la protección contra ataques adversarios.

7.1.2 Para el responsable del despliegue
Se recomienda que los responsables del despliegue también tengan establecida y definida unas políticas de acceso al sistema de IA. Los accesos a los sistemas de Inteligencia Artificial de alto riesgo por parte del personal del responsable del despliegue se recomiendan que no sean anónimos y sin acceso controlado.
Adicionalmente, y de acuerdo con el modelo de comercialización del sistema de inteligencia artificial, se pueden establecer otras políticas de acceso.
El enfoque de las políticas de acceso debe ser de mínimos privilegios y se podría establecer un mecanismo de rotación de contraseñas robusto.
¿A quién podría aplicar dentro de la organización?
El personal de la organización usuaria que tenga acceso al sistema y a su interacción. Si debido al modelo comercialización, es esta organización la que administra el sistema (ya sea in-cloud, on-premise o cualquier variante) podrá incluirse en las políticas de acceso todo el personal relacionado.
Los accesos, su actividad y las personas autorizadas se recomienda que estén registrados y auditados periódicamente, especialmente las revocaciones de permisos, que deberán surtir efecto inmediato.

57

El sistema de IA podrá integrarse, en aquellos escenarios de comercialización, donde sea necesario, con el mecanismo de identidad de la organización usuaria para el acceso al sistema de IA, siguiendo las indicaciones y recomendaciones del manual de instrucciones proporcionado por el proveedor.
¿Qué aspectos se recomienda que cubra?
El principal activo protegido por políticas de seguridad para el caso del responsable del despliegue es el propio sistema de IA. El acceso al sistema, a su panel de control, interfaz o equivalente, se recomienda que esté protegido siguiendo las instrucciones del proveedor, e integrado con los mecanismos de identificación propios de la organización del responsable del despliegue en aquellos casos en los que aplique.
Es responsabilidad del responsable del despliegue gestionar este acceso y disponer de políticas adecuadas.

7.2 Anexo II: Formación en ciberseguridad y sistemas de inteligencia artificial de alto riesgo
Como se ha comentado en la introducción, la formación permite fortalecer la cadena de seguridad que protege el sistema de inteligencia artificial de alto riesgo. De nuevo este anexo cubre un aspecto que no es central para la ciberseguridad de la AI, pero que se encuentra en una región de frontera y que recomendamos cubrir.

7.2.1 Para el proveedor
La ciberseguridad para IA aplica al proveedor durante todo el ciclo de vida del sistema de
IA y a lo largo de todos los activos (datos, modelo etc.) de dicho sistema. Para que las políticas de ciberseguridad sean efectivas, estas se recomiendan que se comuniquen a todo el personal implicado. La formación en ciberseguridad para sistemas de IA tiene un objetivo doble dependiendo del alcance de la ciberseguridad en la organización del proveedor:
- Si el proveedor ya cuenta con un proceso de ciberseguridad, este tendrá como uno
de sus pilares la formación. Esta formación puede verse ampliada para cubrir los tópicos aquí descritos y alcanzar a las personas consideradas.
- Si el proveedor no cuenta con un proceso ciberseguridad específicamente
diseñado, podrá organizar unos planes de formación que cubran los aspectos descritos en este apartado.
La formación proveedor- responsable del despliegue se recomienda que esté definida. En aquellos modelos de comercialización y/o puesta en servicio del sistema de inteligencia artificial que requieran participación del personal del responsable del despliegue, más allá de la propia utilización del sistema, los aspectos básicos a cubrir por el plan de formación en ciberseguridad podrían estar descritos en el manual de instrucciones.

58

¿A quién puede aplicar dentro de la organización?
Los receptores de la formación en ciberseguridad podrán ser:
- Actores sobre datos: perfiles que actúen sobre los datos que alimentan el
aprendizaje del sistema de IA (Analistas de datos, Científicos de datos, Expertos en
IA, etc.)
- Actores sobre la configuración y operación del sistema de IA (Expertos en AI,
Administradores del sistema de IA, Analistas de sistemas, Expertos en ML, etc.)
- Desarrolladores de integración y/o interacción con el sistema de IA (Incluido
MLOps, en su caso).
- Actores de administración de sistemas que hospedan y operan el sistema de IA
(Administradores del sistema de IA, Analistas de sistemas, etc.)
- Actores sobre el diseño, implementación y mantenimiento del software que
materializa el sistema de IA en sí mismo (Incluido en su caso el uso de firmware o similares) (Desarrolladores, Analistas, Expertos en IA, etc.).
- Actores sobre la arquitectura, administración y mantenimiento del sistema de IA en
su ciclo de vida, tanto durante el desarrollo como una vez puesto en marcha
(Expertos en AI, Administradores del sistema de IA, Expertos en ML, etc.).
- El personal general de la organización aplicando la política de mínimos privilegios,
no deberá tener acceso al sistema de IA, al desarrollo del modelo o a los datos. En aquellos casos fuera de los actores identificados en los puntos anteriores, el acceso puede analizarse y registrar la necesidad, si esta es temporal deberá revocarse adecuadamente.
Se recomienda a modo orientativo consultar la ISO/IEC 22989:2022 Information technology — Artificial intelligence — Artificial intelligence concepts and terminology
¿Qué aspectos puede cubrir?
Los aspectos aquí descritos pueden tratarse en diferente profundidad, según el personal receptor de los mismos y su vinculación con el sistema de inteligencia artificial. Este alcance podrá ir desde una sensibilización para todo el personal a una mayor complejidad para aquellos directamente relacionados con el sistema de IA.
Esta formación se recomienda que cubra, al menos, los siguientes tópicos de ciberseguridad aplicada a sistemas de inteligencia artificial:
- ¿Por qué es importante la ciberseguridad en IA? Ciberseguridad durante el ciclo de
vida del sistema de IA.
- La ciberseguridad de los datos de entrenamiento: riesgos de envenenamiento de
los datos de entrenamiento.
- Protección del sistema de IA. Riesgos de filtración de información y código del
sistema de IA o manipulación.
- ¿Qué son los ataques adversarios? Definición. Diferentes tipos. Ataques adversarios
para el sistema de Inteligencia Artificial en consideración.

59

- Explotación de defectos del modelo. Definición de ataques por transferencia.
Necesidad de utilización de modelos/frameworks seguros. ¿Qué son los defectos intrínsecos del modelo? Configuración e integración segura. Evitar errores en el modelo por el uso de malas prácticas.
- La importancia del control de acceso basado en roles (RBAC) para acceso tanto a
los datos como al modelo y robustez del sistema de autenticación, incluyendo refuerzos como autenticación de doble factor.
La formación podría actualizarse en relación con los cambios del modelo y el paradigma de ciberseguridad en inteligencia artificial, que es un área cambiante y en continua evolución.
Podrá requerir que la recepción de la formación por determinados perfiles (científicos de datos, expertos en ML/AI) requiera la realización de pruebas y/o certificaciones.
Para el responsable del despliegue del sistema de IA se puede desarrollar una indicación del material formativo, explicando el nivel de ciberseguridad requerido para la utilización del sistema de Inteligencia artificial: FAQs, documentación explicativa, descripciones paso a paso de la operación y puntos críticos. Todo ello adaptado al nivel de comercialización del sistema de IA (SaaS, On-premise, in-cloud etc.)

7.2.2 Para el responsable del despliegue
La formación en ciberseguridad de aplicación al responsable del despliegue dependerá del enfoque que tenga el modelo de comercialización del sistema de inteligencia artificial considerado. En aquellos escenarios en los que el sistema se instale en infraestructura del responsable del despliegue (modelos on-premise, in-house) el responsable del despliegue podrá adecuar sus planes de formación en materia de ciberseguridad para cubrir los aspectos indicados en el manual de instrucciones del sistema.
¿A quién puede aplicar dentro de la organización?
El personal de la organización usuaria del sistema de inteligencia artificial, que vaya a realizar la interacción directa con este. Dependiendo del enfoque de comercialización:
- Personal de administración de sistemas.
- Personal responsable de la configuración del sistema de IA.
- Personal responsable de la supervisión del sistema de IA.
¿Qué aspectos puede cubrir?
El responsable del despliegue podrá utilizar el material generado por el proveedor en materia de ciberseguridad aplicada a su sistema de IA para orientar y cubrir los conocimientos y/o perfiles necesarios.
Independientemente del formato de comercialización en que reciba el sistema, todo su personal en interacción directa con el sistema de IA podrá recibir formación en materia de

60
