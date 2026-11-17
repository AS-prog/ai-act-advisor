---
name: aesia-11-guia-ciberseguridad-05-reglamento-de-inteligencia-artificial-pa
description: "AESIA: aesia 11 guia ciberseguridad, sección «Reglamento de Inteligencia Artificial (parte 2)» (págs. 25-32). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-11-guia-ciberseguridad
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Reglamento de Inteligencia Artificial (parte 2)"
  paginas: 25-32
  origen: 2026-07-17-aesia-11-guia-ciberseguridad.pdf
  oficial: false
---
# Reglamento de Inteligencia Artificial (parte 2)

4.2.1 Medidas aplicables
Proveedor
Las medidas organizativas a modo orientativo y no vinculante del proveedor relacionadas con los inventarios de activos y actores son:
- Inventariar todos los actores implicados en el proceso de diseño y desarrollo del
sistema de IA. Las acciones de terceros no autorizados no solo se refieren a terceros externos sino a terceros internos con funciones inadecuadas.
- Una vez definidos los actores, establecer el nivel de alcance y permisos que cada
uno de ellos puede tener y definirlos adecuadamente. Ver 7.1 Anexo I: Políticas de acceso. Una aproximación a sistemas de inteligencia artificial de alto riesgo.
- La documentación del sistema de IA puede reflejar claramente los roles implicados
en la utilización de la herramienta, y los permisos que cada uno de ellos deberá tener. Las instrucciones o pasos de instalación podrían reflejar con detalle la relación entre los actores y los elementos y acciones de la instalación.
- Planificación y realización del inventario de activos en el desarrollo del sistema de
Inteligencia Artificial, considerando especialmente las herramientas, datos, procesos y modelo.
- Sobre el inventario de activos, se puede identificar las vulnerabilidades asociadas
a esos activos. Esa identificación se realiza en apartados sucesivos de la guía.
- Las instrucciones del sistema de inteligencia artificial pueden incluir una lista de las
amenazas/vulnerabilidades inherentes al sistema durante su utilización.
- Se puede desarrollar un modelo de amenazas riguroso para comprender todos los
posibles vectores de ataque y con la consideración del riesgo para la vulneración de derechos y libertades de las personas físicas, daños a la salud, daños graves a la propiedad y/o el medio ambiente alineado completamente con el análisis de riesgos realizado (ver guía del sistema de riesgos).
- El modelo de amenazas establecido para cada identificación de
actores/activos/vulnerabilidades se recomienda que mantenga un esquema RACI
(Responsible, Accountable, Consulted, Informed). En los apartados siguientes (del apartado 4.3 al apartado 4.5), se definirán las vulnerabilidades de manera que el proveedor del sistema pueda elaborar un modelo de amenazas riguroso de aplicación a su sistema de inteligencia artificial y establecer los controles técnicos necesarios, añadiendo las características de una matriz RACI tal y como se ha propuesto.
En este proceso de inventariado de los actores implicados y activos del sistema, y aunque su ámbito más específico está indicado dentro de la guía de datos, se puede implicar al delegado de protección de datos DPD o su equipo. Así se podrá establecer un inventario los más completo posible sobre el que se pueda establecer el modelo de amenazas.

24

Las medidas técnicas que el proveedor puede realizar respecto a estos inventarios son meramente de soporte a las organizativas:
- El inventario de activos puede tener un soporte informático adecuado a las
dimensiones y capacidades de la organización. Podrá abarcar desde un archivo ofimático o una base de datos simple donde se almacenen los datos de los activos de
IA hasta herramientas y soluciones de mercado ya existentes para la gestión de inventarios de activos de IT. Asimismo, para dimensionar adecuadamente el sistema, se tendrán en cuenta el nivel de accesos concurrentes y la estacionalidad (aquellos momentos en los que el volumen de accesos puede ser más acusado) para garantizar la disponibilidad del sistema y evitar bloqueos por exceso de intentos de conexión.
- Se recomienda disponer de los medios técnicos necesarios para que las políticas de
accesos establecidas puedan ejecutarse (Ver 7.1 Anexo I: Políticas de acceso. Una aproximación a sistemas de inteligencia artificial de alto riesgo).
- Sistema documental y de gestión de activos indicado, se recomienda que esté
centralizado con los inventarios actualizados y disponibles.

Ejemplo – Sistema automático de concesión de ayudas
El proveedor del sistema de IA realiza las acciones de inventario de activos y actores:
- Activos: datos de entrenamiento, prueba y validación; los datos son especialmente
sensibles y se utilizaran datos completamente anonimizados proporcionados por la Administración General del Estado, que representan datos históricos de concesión/denegación de ayudas de los últimos 10 años. Modelo seleccionado.
Librerías y software que interacciona directamente con el modelo de IA. Herramienta para el control de versiones y entorno de desarrollo. Documentación interna de desarrollo y comercial. Documentación externa.
- Actores: Científicos de datos, Expertos en ML e IA, desarrolladores de software, jefes
de proyecto y equipo de sistemas. También ha identificado dentro de su equipo comercial, a aquellos que se encargarán de promocionar el producto.
El proveedor como pyme de nueva creación (start-up), debe especificar los roles múltiples que parte de su personal realiza sobre los activos, construyendo una matriz de relación de los activos y actores. Así, para cada activo, se ha identificado el actor relacionado, indicando si se dispone de acceso. Esta matriz se ha realizado utilizando una herramienta ofimática convencional para registrar los datos y se ha compartido en la organización a través de la Wiki interna colaborativa.
Con esta matriz se ha localizado una solución técnica de mercado que permita implementar las políticas de acceso.

25

Responsable del despliegue
Para el ámbito de actores y activos, se recomienda que el responsable del despliegue del sistema de inteligencia artificial pueda conocer aquello que directamente le aplica.
Organizativamente podrá considerar:
- Integrar la documentación proporcionada por el proveedor sobre los roles de los
diferentes actores con su organigrama interno. Definir y establecer las funciones y las personas que los cubrirán. Establecer mecanismos de sustitución de estas personas cuando estén solos a cargo de alguna función, de manera que bajas inesperadas o la marcha de un empleado mantenga el sistema y los procesos sin discontinuidades. Siempre que la organización y el tamaño de la empresa lo permitan, los diferentes roles, acorde a lo definido por el proveedor, se asignarán a personas diferentes.
- Si el formato de uso y comercialización del sistema de IA contemplase que el
responsable del despliegue dispusiese del sistema de IA como un activo en sus propias instalaciones, tendrá que considerar el sistema de IA como un activo que se debe proteger en materia de ciberseguridad.
No hay medidas técnicas relevantes en este ámbito para el responsable del despliegue más allá de las necesarias para la implantación correcta de las políticas de seguridad (ver
Anexo I).

4.3 Vulnerabilidades y controles de seguridad para datos
La identificación de vulnerabilidades asociadas a los datos de entrenamiento y el establecimiento de los controles de seguridad necesarios para evitar su alteración o manipulación permiten proteger al sistema de inteligencia artificial de ataques de envenenamiento1.
El Reglamento Europeo de IA, pone especial foco en las vulnerabilidades asociadas a datos cuando establece en su artículo 15.5 relativo a precisión solidez y ciberseguridad:

Art.15.5 – Precisión, solidez y ciberseguridad
Entre las soluciones técnicas destinadas a subsanar vulnerabilidades específicas de la IA figurarán, según corresponda, medidas para prevenir, detectar, combatir, resolver y controlar los ataques que traten de manipular el conjunto de datos de entrenamiento («envenenamiento de datos»)
1

Las palabras y descripciones destacadas se corresponden con términos que son desarrollados en el glosario

26

El objetivo del atacante es alterar el entrenamiento del sistema de inteligencia artificial con la intención de controlar sus resultados o comprometer su funcionamiento. Los cambios no intencionados en los datos de entrenamiento se abordan a modo orientativo en la guía de datos. En el manual de uso del sistema, el proveedor puede enumerar las vulnerabilidades asociadas a los datos. Se recomienda identificar, para cada vulnerabilidad, el control de seguridad aplicado. Todas las vulnerabilidades y los controles asociados a los datos se presentan principalmente en la fase de diseño y entrenamiento del sistema, donde el riesgo de introducción de datos maliciosos es muy elevado y el impacto muy alto.

4.3.1 Medidas aplicables
Proveedor
Se recomienda que el proveedor identifique las vulnerabilidades aplicables a los conjuntos de datos de entrenamiento. Se puede definir la lista, en base a la finalidad prevista del
Sistema de IA. A continuación, se presenta una lista de vulnerabilidades asociadas a la manipulación de datos de entrenamiento, validación y prueba:
- Modelo fácil de envenenar
- Datos insuficientes para incrementar la resistencia al envenenamiento.
- Gestión de derechos de acceso a los datos inadecuada
- Gestión de los datos inadecuada
- Fuentes de datos no controlados
- Falta de control para detectar envenenamiento en el sistema
- No detectar muestras envenenadas en el conjunto de entrenamiento.
- Uso de fuente de etiquetado de datos incorrecto
Queda fuera del ámbito de esta guía, pero es importante que el proveedor tenga en cuenta, dentro del ciclo de vida propio de los datos, la eliminación segura de estos, una vez que deja de estar en producción o el sistema entra en un evolutivo. En la guía de datos, se trata de manera especial este aspecto.
En la tabla siguiente, se indican a modo orientativo y no vinculante algunas de las vulnerabilidades más relevantes y los controles de seguridad aplicables para mitigar su explotación, en el momento de creación de esta guía. Dado el carácter dinámico y la rápida evolución de las amenazas en ciberseguridad, es recomendable estar siempre al tanto de la información técnica más actualizada y de referencia. Entre los recursos recomendados se encuentran el OWASP Machine Learning Security Top Ten, el OWASP Top 10: LLM &
Generative AI Security Risks y el OWASP AI Top Ten, que proporcionan análisis y medidas actualizadas frente a riesgos emergentes en sistemas de inteligencia artificial.

27

Vulnerabilidad

Controles de seguridad

Modelo fácil de envenenar

En fase de diseño, escoger o definir un modelo más resiliente.

Datos insuficientes para incrementar la resistencia al envenenamiento.

Ampliar el conjunto de datos utilizando técnicas de aumento de datos, para sets demasiado pequeños o insuficientes para la finalidad prevista

Gestión de derechos de acceso a los datos inadecuada

Políticas de acceso adecuadas, ver Anexos

Fuentes de datos no controlados

Todas las fuentes de datos deben mantenerse bajo control de versiones, para disponer de una traza de los cambios en los datos y los actores que los han realizado.

Fuentes de datos no controlados
(continuación)

ISO27001/2 - NIST 800-53: Se proponen diversos mecanismos.
Clasificar los datos adecuadamente utilizando herramientas estadísticas, considerando la finalidad prevista y revisar adecuadamente la clasificación; los datos deben estar siempre cifrados en tránsito, utilizar cifrados con garantía de autenticidad, cifrando los datos utilizando cifrados acordes a los estándares vigentes; almacenar siempre cifrado en reposo las fuentes de los datos, a nivel de disco duro y de cifrado de archivo individual, igualmente usando estándares vigentes. Utilizar herramientas de prevención de pérdida de datos (DLP)
en aquellos datos sensibles y relevantes.

Falta de control para detectar envenenamiento en el sistema

Aplicar la técnica STRIP, que implica perturbar los datos de manera controlada y observar la variancia entre los datos perturbados y no perturbados para identificar posibles envenenamientos.

Utilizar técnicas de bagging, boosting, o el algoritmo TRIM durante el entrenamiento para fortalecer la robustez del modelo. Para mitigar el efecto de la aleatoriedad y asegurar la reproducibilidad, utilizar semillas iniciales definidas cuando sea necesario.ISO27001/2 - NIST 800-53:
Realizar auditorías periódicas y regulares sobre la gestión datos y realizar planes de acción para corregir las deficiencias.

5.1 Anexo I: Políticas de acceso. Una aproximación a sistemas de inteligencia artificial de alto riesgo.

28

Vulnerabilidad

Controles de seguridad

No detectar muestras envenenadas en el conjunto de entrenamiento

Utilizar técnicas de saneado de datos para detectar y eliminar los outlier:
Z-score, Local Outlier Factor, Bosques de Aislamiento (Isolation Forest).
Antes de eliminar cualquier dato, realizar un diagnóstico exhaustivo para evitar la eliminación de datos válidos en intervalos extremos:
1. Verificar previamente la hipótesis sobre la distribución de la variable y, si la distribución no es normal, evitar el uso de Z-score.
2. Diagnosticar la naturaleza del outlier para decidir si se debe eliminar o conservar
Para detectar cambios en las muestras, certificar la distribución de los datos de entrenamiento por marginales (distribución estadística empírica de cada variable de la base de datos, ya sea numérica o no), y multivariada (por relaciones bivariantes o más complejas) y periódicamente verificar que se mantiene estable. Ante cambios importantes en la distribución de una de las variables o de la relación entre varias, profundizar para identificar los cambios acontecidos en los datos
Analizar el impacto de los sets de datos en la exactitud del modelo, en procesos de re-entrenamiento o aprendizaje continuo: RONI (reject on negative impact) o tRONI (targeted Reject On Negative Impact).

Uso de fuente de etiquetado de datos incorrecto

ISO27001/2 - NIST 800-53: Gestión de todas las interconexiones con sistemas externos de los que se reciban datos y revisión. Establecer un proceso formal para realizar una revisión de todas las interconexiones y regular y vigilar su utilización.
Usar técnicas de protección frente a intercambio de etiquetas (Label
Flipping), basadas en la identificación por k-NN (k-nearest neighbours)
en el data-set. Esta técnica puede utilizarse cuando los conjuntos de datos etiquetados no sean confiables, pero no exista otra alternativa en los mismos.

Tabla 1 Ataques Envenenamiento: Vulnerabilidades y controles de seguridad
Todos los controles y vulnerabilidades asociadas a datos se focalizan principalmente en la fase de diseño y entrenamiento del sistema, donde el riesgo de introducción de ataque por envenenamiento es muy elevado y el impacto muy alto.
Se recomienda que el proveedor enumere en el manual de uso del sistema de IA, las vulnerabilidades asociadas a los datos de entrenamiento, identificando para cada vulnerabilidad el control de seguridad aplicado. En el caso de que el responsable del despliegue del sistema de IA de alto riesgo deba realizar parte del entrenamiento antes de su puesta en marcha, se recomienda detallar la manera de aplicar los controles de seguridad.

29

Ejemplo – Asistencia al trabajo
El sistema va a trabajar con datos biométricos obtenidos de los empleados para su entrenamiento, prueba y validación, de tal manera que sea capaz de identificar adecuadamente a los empleados desde las diversas ubicaciones de las cámaras (o sensores biométricos) para registrar su asistencia al trabajo.
En el análisis de riesgos se ha identificado la posibilidad de que un usuario actúe de manera malintencionada para alterar las etiquetas de los datos biométricos. Esto podría permitirle asociar sus propios datos con los de otros empleados, comprometiendo así la detección del sistema.
Dado que el principal origen de esta amenaza es el envenenamiento de datos, durante el entrenamiento se utilizan técnicas de perturbación STRIP, específicamente destinadas para detectar disparadores de envenenamiento (o troyanos) en el conjunto de datos.
Adicionalmente, el equipo de diseño decide proteger al sistema de IA contra un posible ataque por Label Flipping (ver Glosario) en el que el atacante haya cambiado malintencionadamente etiquetas de imágenes de diferentes empleados.

Responsable del despliegue
La principal acción organizativa que puede realizar el responsable del despliegue para abordar la protección de sistemas de inteligencia artificial frente a ataques de envenenamiento es realizar una lectura y compresión del manual de instrucciones. Como norma general, el responsable del despliegue no participa de la fase de diseño, desarrollo y entrenamiento del sistema.
No obstante, si el formato de uso y comercialización del sistema de IA contemplase que el responsable del despliegue utilizase el sistema de IA realizando un entrenamiento final del mismo, o en los sistemas de entrenamiento continuo, estando este previamente preentrenado parcialmente por el proveedor, podrían aplicarse todas las medidas de ciberseguridad aplicada a IA del proveedor en materia de los datos. En este escenario, el responsable del despliegue podría asumir pasaría a tener responsabilidades similares a las de proveedor (organizativas y técnicas) en todos los aspectos descritos en el anterior apartado.

4.4 Protección frente a ataques adversarios
Se ha separado a modo orientativo en esta guía los ataques adversarios de tipo envenenamiento de datos, de aquellos relacionados con el propio modelo. Además, el sistema está más expuesto durante la fase de inferencia, una vez se encuentra en producción (tras la puesta en marcha) a este tipo de ataques. A diferencia de la exposición relativa a datos.

30

El Reglamento Europeo de IA en el artículo 15, relativo a precisión solidez y ciberseguridad, párrafo 4 establece:

31
