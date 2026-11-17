---
name: aesia-10-guia-solidez-06-reglamento-de-inteligencia-artificial-pa
description: "AESIA: aesia 10 guia solidez, sección «Reglamento de Inteligencia Artificial (parte 3)» (págs. 31-38). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-10-guia-solidez
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Reglamento de Inteligencia Artificial (parte 3)"
  paginas: 31-38
  origen: 2026-07-17-aesia-10-guia-solidez.pdf
  oficial: false
---
# Reglamento de Inteligencia Artificial (parte 3)

4.3 Redundancia y planes de respaldo
El camino de conocer, garantizar y conservar la solidez del sistema como característica del sistema, tiene la derivada adicional de disponer de técnicas de redundancia para el funcionamiento del sistema de IA, de tal manera que esta pueda garantizarse.

AI Act
Art.15.4 – Precisión, solidez y ciberseguridad
La solidez de los sistemas de IA de alto riesgo puede lograrse mediante soluciones de redundancia técnica, tales como copias de seguridad o planes de prevención contra fallos.

Por tanto, una parte de los mecanismos para alcanzar la solidez se fundamentan en las técnicas de redundancia, que incluyan planes de respaldo o a prueba de fallos.
El proveedor el principal responsable de establecer las técnicas de redundancia en el
Sistema de IA y que estos estén acorde a la finalidad prevista del sistema y prestando atención también a los resultados no deseados previsibles.
El proveedor se recomienda que documente y facilite el monitoreo del nivel de cobertura de las pruebas de calidad realizadas sobre el sistema (ver guías de ciberseguridad, precisión y esta misma, así como la guía de sistema de gestión de calidad), análisis de correlación y redundancia que puedan desvelar potenciales ataques al sistema o la degradación de la calidad de este. Ejemplos de técnicas a utilizar son: correlación de controles y medidas, por ejemplo, restauraciones de datos, del Sistema, medidas KPI
(número de restauraciones de datos incorrectas), grado de cobertura de defensas preventivas, test de cobertura, pruebas de calidad y restauración de datos.
El proveedor podrá proveer acciones para el diseño continuo del sistema basado en la salvaguarda de riesgos, para avalar el sistema de IA con resiliencia a ataques, solidez a cambios en el entorno operativo, minimizar el daño inesperado no intencionado, y reproducibilidad.
El proveedor podrá proporcionar:
1. Mecanismos de copia de datos automático (según guía de registros) que permitan la redundancia de modelos, algoritmos, logs o registros provistos por las librerías de MLOps y DevOps, datos y ejecuciones del modelo.
2. Mecanismos de seguridad ante fallos aplicables a los componentes a lo largo de todo el ciclo de vida del sistema de IA.
3. Herramientas que permitan ejecutar un plan de actuación cuando se haya producido el fallo, para la recuperación efectiva de datos, modelos, algoritmos y el sistema de IA.
4. Herramientas de reproducibilidad, trazado (según guía de registros), procedencia o linaje de los datos que garanticen la solidez del modelo utilizado y permitan
30

detectar modificaciones en los datos que lleven a cambios significativos en la solidez o rendimiento del modelo.
Tanto la redundancia como el plan de actuación de los mismos componentes arriba señalados se recomienda que sea local y global; idealmente, utilizando un segundo dispositivo o mecanismo, como por ej., un alojamiento seguro en la nube.
Para ejecutar técnicamente los puntos anteriores 1, 2, y 3, se recomienda seguir las siguientes metodologías y herramientas de MLOps:
- Medidas de redundancia geográfica.
- Sistemas escalables en capacidad según la demanda, sistema de monitorización de
disponibilidad y rendimiento.
- Implementaciones de sistemas de copias de seguridad y seguimiento de versiones
de datos.
- Modelos y algoritmos que se incluyan en plataformas de DevOps tales como de
todas las existentes en el mercado, tanto comerciales como código abierto
(gratuitas). Éstas proveen características clave como automatización de operaciones de desarrollo y distribución, cómputo en la nube centralizado, monitoreo de errores continuo, y tecnología de contenedores para ejecutar microservicios o aplicaciones con recursos limitados en entornos múltiples, que permitirían orquestas los escenarios de redundancia geográfica y la escalabilidad acorde a la demanda.

Ejemplo – Detección de denuncias falsas
El tramitado de denuncias en las comisarías, es un proceso que requiere una continuidad y una disponibilidad en el tiempo, que permita que un ciudadano pueda presentar una denuncia en cualquier comisaria en cualquier momento.
Para garantizar que el sistema de IA puede realizar las operaciones de evaluación de las denuncias, con alta disponibilidad el sistema de IA se encuentra distribuido en CPDs
(centros de procesos de datos), con sistemas de redundancia en diferentes ubicaciones físicas, tanto en almacenamiento como en servidores de aplicaciones, para evitar que un fallo en una de las ubicaciones del CPD pueda suspender la ejecución del servicio.
Introducen un sistema de respuesta auto escalable, que permite al sistema aumentar el rendimiento de la base de datos y aplicaciones acorde a la demanda.
Para la integración de todo ello con el proceso de distribución de nuevas versiones, se conecta una herramienta de DevOps de código abierto, que antes de liberar una nueva versión verificada y validada, realiza una batería de pruebas unitarias, de integración y comprueba la precisión del sistema y si todo es correcto distribuye la actualización sobre la infraestructura.
Con estas consideraciones, el sistema de IA tiene una infraestructura que garantiza la redundancia y un mecanismo de despliegue que garantiza que se cumplen los requisitos necesarios para su puesta en marcha establecidos desde el diseño y a través del análisis de riesgos.
31

En cuanto a los datos (punto 4 anterior), parámetros de configuración o del modelo aprendido, se recomienda que puedan descargarse para fomentar su reproducibilidad.
Para promover la publicación de resultados y el linaje de modelos, cuando los pesos de un modelo, modelos pre-entrenados o conjuntos de datos no sean posibles almacenarlos en el repositorio de código principal que almacene el mismo, se promoverá el uso de herramientas abiertas Open Access y repositorios de confianza.
Para mantener un seguimiento y registro de las bases de datos usadas y las modificaciones que éstas sufren, se podrán usar herramientas gratuitas de control de versiones específicas para bases de datos.
Por su parte, el responsable del despliegue en este aspecto se recomienda que conozca las medidas de redundancia que se proporcionan, así como los planes de respaldo y a pruebas de fallos.
Especialmente lo será si el sistema de IA es instalado por el responsable del despliegue en unas instalaciones propias. En ese caso, es probable que sea responsabilidad del responsable del despliegue replicar con precisión las instrucciones de instalación y mantenimiento que el proveedor haya proporcionado, asociadas a las medidas descritas en el apartado anterior.
Organizativamente, la responsabilidad del responsable del despliegue será conocer, aplicar y mantener vigiladas las métricas de precisión y estadísticas asociadas, pudiendo reflejar cambios entre las distribuciones de los datos de entrenamiento y de inferencia
(pudiendo exhibir desplazamiento de distribución o datos (shift del conjunto de datos o distribución shift)).
En cuanto a formación técnica, se recomienda que el responsable del despliegue conozca, aplique y mantenga vigilado el sistema de respaldo de fallos en caso de fallo, si así lo especifica la documentación del proveedor.

4.4 Solidez para sistemas que continúan aprendiendo
El comportamiento de los sistemas de IA que continúan aprendiendo después de ser comercializados, requiere un foco y tratamiento especial para garantizar su solidez especialmente en la posibilidad de aparición de sesgos.

AI Act
Art.15.4 – Precisión, solidez y ciberseguridad
Los sistemas de IA de alto riesgo que continúan aprendiendo tras su introducción en el mercado o puesta en servicio se desarrollarán de tal modo que se elimine o reduzca lo máximo posible el riesgo de que los resultados de salida que pueden estar sesgados influyan en la información de entrada de futuras operaciones (bucles de retroalimentación) y se garantice que dichos

32

bucles se subsanen debidamente con las medidas de reducción de riesgos adecuadas.

Es importante considerar que el aprendizaje continuo debe extenderse, conceptualmente en lo que a cobertura de las medidas propuestas se supone, cuando este se actualice al haber sido reentrenado siguiendo un proceso de actualización, y no solo los sistemas que continúan aprendiendo de manera automática durante su utilización.
Se recomienda que proveedor y responsable del despliegue aseguren que el entrenamiento constante y continuado en el tiempo del sistema de IA no deteriora sus métricas de solidez, precisión y rendimiento.
El proveedor, como responsable del diseño, implementación, verificación y validación del sistema de IA, es el principal responsable para cubrir los requerimientos que establecemos en este apartado. A nivel de organizativo se proponen las siguientes medidas:
- El proveedor del sistema de IA puede tener expertos que puedan cubrir el monitoreo
de la degradación del sistema durante todas y cada una de las diferentes etapas por las que el modelo puede sufrir degradación a nivel de científico de datos, ingeniero de datos, así como a cambios en el funcionamiento de las MLOps y DevOps.
- A nivel de diseño y concepción del modelo, estrategias de aprendizaje continuo,
compresión de modelos de aprendizaje profundo podrán ser consideradas para atajar el posible olvido catastrófico. Otras medidas de solidez a estudiar en estas etapas de incepción del sistema el diseño de mecanismos (Mechanism Design [113,
53, 51]).
- Se recomienda asegurar que el entrenamiento constante y continuado en el tiempo
del sistema de IA no deteriora sus KPIs y métricas de precisión, solidez, rendimiento, y resto de métricas que alcancen los principios de IA confiable.
- Se recomienda que el el proveedor indique técnicas formales de anotación en la
documentación del sistema, sobre casos concretos de ejecución del sistema de IA cuando éste deba o tenga la opción de interactuar, interoperar con otros sistemas o humanos, reusarse o integrarse con otros sistemas. Especialmente, se deberá anotar la retroalimentación o mejoras provistas por humanos para que la versión futura del modelo actualizado las tenga en cuenta, dentro del paradigma e IA centrada en el humano, Computación Humana, Human on the Loop (HOTL) y Human in the Loop
(HITL).
Se recomienda que el proveedor, en relación con esos datos notificados, mantenga pública una base de datos de lecciones aprendidas de fallos, que debe servir para mantener una base de conocimiento actualizada continuamente y que integra la seguridad en el diseño y el paradigma del diseño de salvaguarda. Éste puede evocar, situaciones o visualizaciones de ejemplos que pueden ayudar a discernir y prevenir escenarios no favorables de HRAIS a evitar.
Se recomienda que el responsable del despliegue tenga y estar familiarizado con la funcionalidad del sistema para poder visualizar y reportar, en cualquier momento, si es
33

necesario, al proveedor, de anomalías que no aseguren que el entrenamiento constante y continuado en el tiempo del sistema de IA no deteriora sus KPI y métricas de calidad, solidez, eficiencia, rendimiento e incertidumbre, entre otras.

4.4.1 Tipos de degradación del sistema de IA y planes de mitigación, estrategias y herramientas
La calidad en términos de solidez de un sistema de IA es tan buena 1) como buenos sean los datos (ver Guía de Datos), y 2) como sólido sea el modelo y su infraestructura una vez en producción.
Una vez entrenado el modelo, el proveedor se puede ver obligado a encontrar un compromiso en la contraprestación entre precisión y estabilidad. Sin embargo, un sistema sólido debe evitar la degradación de este, para ello es necesario que para las taxonomías de degradación que puedan existir, podamos trasladar mecanismos de corrección o de detección.
Existen tres tipos principales de posible degradación de un modelo de IA, conforme éste se sigue entrenando o usando para inferencia; Se recomienda que se controlen y evalúen todas desde la fase de desarrollo, hasta la fase de ejecución durante el ciclo de vida:
1. La desviación del modelo: Se refiere a la diferencia entre las predicciones promedio del modelo y los valores reales. Representa el error sistemático que indica la capacidad del modelo para capturar las relaciones subyacentes en los datos. Una desviación alta sugiere que el modelo es demasiado simple y no logra captar patrones complejos, lo que conduce a un subajuste. Para mitigar la desviación, es recomendable aumentar la complejidad del modelo o mejorar la calidad y cantidad de los datos de entrenamiento. Es esencial equilibrar la desviación y la varianza para evitar tanto el subajuste como el sobreajuste del modelo.
2. La desviación o deriva del modelo en el tiempo: es un fenómeno en que las predicciones del modelo aprendido se degradan debido a alteraciones en el entorno. Ocurre cuando P(Y|X) cambia: las mismas entradas producen diferentes salidas. Estrategias para mitigar y monitorear este tipo de derivas: la batería de pruebas debe encargarse de detectar fallos del modelo y del sistema silenciosamente, el impacto del cambio en los datos con respecto a los datos de entrenamiento original del modelo y su impacto en la precisión y métricas asociadas.
3. La desviación de los datos en el tiempo: ocurre cuando los datos (o variable independiente) de entrada de un modelo (la distribución conjunta, P(X)) cambian.
Es una de las mayores razones por las que un modelo degrada su exactitud en el tiempo. Se produce cuando P(X) cambia, o P_t1 (X) ≠ P_t2 (X)). Cuando P(X) cambia, ocurre un desplazamiento del dominio.

34

4.4.2 Estrategias para mitigar cambios en la degradación de la precisión y solidez del modelo y/o de sus datos
Tanto para mitigar la desviación del modelo como la desviación de los datos, el reentreno de la red suele ser una solución, pero no siempre viable, especialmente en contextos de aprendizaje continuo.
Caracterizar la desviación del modelo y adaptar el modelo al mismo [58], usar estrategias de desviación del conjunto de datos [60], o de generalización fuera de distribución (outof-distribution, OOD) o zero-shot generalization [61]. Para que el modelo continúe aprendiendo y adaptándose al cambio en la distribución, estrategias de aprendizaje continuo pueden ser útiles para la desviación de datos [62] y para aprender continuamente con modelos que no paran de entrenar. Por ejemplo, la utilización de Elastic Weight
Consolidation (EWC), Piggyback [112], modelos de Experience Replay (replay buffer, prototype experience replay, rehearsal), replay con modelos generativos (pseudo rehearsal), o Memory networks, entre muchos otros [25].

Ejemplo – Detección de denuncias falsas
En el diseño del sistema de IA de alto riesgo, el proveedor ha considerado que, aunque la base de entrenamiento es amplia (ver ejemplos en guía de precisión), el modelo puede degradarse por cambios en los datos presentes en las denuncias a lo largo del tiempo pudiendo sufrir: desviación de los datos y desplazamiento del dominio. El concepto que se establece no es que puedan ocurrir, si no que ocurrirán, por lo que se hace necesario mitigarlos (en la medida de lo posible) y proporcionar un mecanismo de retroalimentación que amplie la base de entrenamiento con la evaluación final de un agente humano.
Con el objetivo de mitigar la desviación de los datos y desplazamiento del dominio en las denuncias (tanto provenientes de su contenido estructurado: provincias, direcciones;
como del contenido textual) se utiliza la técnica de la adaptación del dominio (domain adaptation) propuesta en esta guía sobre los conjuntos de denuncias de entrenamiento y verificación/prueba.
Dado que el reentrenamiento del sistema no es viable de manera continua. El sistema de IA se dota de un proceso que permite a los agentes añadir la veracidad/falsedad real de una denuncia en la que el sistema ha cometido un error, con esta información el sistema de IA prepara un ejemplar de entrenamiento despersonalizado y anonimizado que podrá incorporarse a los conjuntos de entrenamiento en las actualizaciones futuras sucesivas. Esta información se incorpora al sistema de MLOps descrito en esta guía para este mismo sistema de IA.
Para mitigar la desviación de los datos y desplazamiento del dominio, se pueden usar técnicas de adaptación del dominio (domain adaptation) [59] o transferencia de conocimiento (transfer learning).

35

Cuando los conjuntos de datos sean visuales, se recomienda además estudiar la potencial ocurrencia de sesgo general, de selección, de marco o de etiqueta y todos sus subtipos
(Tabla 1 en [88] y lista de requerimientos asociado en apéndice).
Para detectar relaciones causales que puedan ser una fuente de sesgo, se pueden utilizar clasificadores para discernir la presencia de ciertos objetos o atributos en un clasificador, para detectar el sesgo de selección [93], a través del Neural Causation Coefficient (NCC,
[92]).
- Cuando no se tiene acceso al objetivo real: Confidence-based Performance
estimation (CBPE) para modelos de clasificación, y Direct Loss Estimation (DLE) para problemas de regresión.
- Se procurar establecer mecanismos para detectar el fallo silencioso del modelo, por
ejemplo, con sistemas de alertas. Por ejemplo: NannyML afirma ser a día de hoy el único algoritmo de código abierto capaz de capturar completamente el impacto de la desviación de los datos en la precisión, y AzureML de Microsoft con el diagnóstico de errores a nivel de MLOps.
- Para estimar relaciones causales que pueden comprometer la solidez, el sesgo de
variable omitida que explica las variables dependiente e independiente conlleva a estimaciones sesgadas. Para ello se pueden usar métodos que reducen el riesgo de este sesgo: variable instrumento o least squares estimator, o el regression discontinuity design.
Para monitorizar el buen conocido fenómeno del olvido catastrófico y la incapacidad de aprender de manera continua [25], se recomienda usar modelos de aprendizaje profundo continuo (continual learning o lifelong learning), considerar y reportar métricas de control del olvido y de monitorización del aprendizaje continuo, por ejemplo, Backward transfer, forward transfer, model size efficiency, samples storage size efficiency, y computational efficiency [28].
Organizativamente, se recomienda que el sistema de IA implemente funcionalidad que permita el cómputo, monitoreo y notificación automática o por parte del responsable del despliegue de las degradaciones a las que pueda estar expuesto el sistema. Por tanto, será responsabilidad del responsable del despliegue conocer dicho sistema proporcionado por el proveedor, y acceder a la documentación técnica del mismo.
En cuanto a medidas técnicas, a modo orientativo se pueden destacar:
- El responsable del despliegue tiene la responsabilidad de conocer, aplicar y
mantener vigilado el modelo a través de las interfaces provistas para transmitir la precisión, sesgos (según Guía de Datos) e incertidumbre de este.
- Así, deberá usar los manuales de instrucciones de las interfaces de las herramientas
que proveen todas las métricas relacionadas, para estar en posición de interpretar
(ver guía de Transparencia), verificar que la salida del modelo se corresponden con su precisión y métricas asociadas, y que la explicación señala las razones correctas esperadas [113], para así evaluar si el sistema está funcionando correctamente, sin sesgo (evitando por ejemplo alucinación de elementos [114,115], ver Sesgos en Guía de Datos). Una vez identificados los sesgos, actuará en consecuencia según guía de supervisión humana).
36

Más información sobre medidas orientativas y no vinculantes para monitorizar y controlar la solidez de sistemas de IA en la ISOS:
- [SC42_N483_ISO_IEC_TR_24029-1] ISO/IEC TR 24029-1, Artificial Intelligence (AI) —
Assessment of the robustness of neural networks — Part 1: Overview
- [ISO/IEC 24029-2:2023 SC42 N938 ISO IEC CD 24029-2], Artificial intelligence (AI) —
Assessment of the robustness of neural networks — Part 2: Methodology for the use of formal methods
- (ISO/IEC 24029-2:2023, ISO /IEC JTC 1/SC 42/WG 3 Secretariat: ANSI Date: 2021-0906).

37
