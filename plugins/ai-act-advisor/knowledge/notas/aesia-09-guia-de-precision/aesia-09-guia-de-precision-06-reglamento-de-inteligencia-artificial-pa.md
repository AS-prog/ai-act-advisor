---
name: aesia-09-guia-de-precision-06-reglamento-de-inteligencia-artificial-pa
description: "AESIA: aesia 09 guia de precision, sección «Reglamento de Inteligencia Artificial (parte 3)» (págs. 28-32). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-09-guia-de-precision
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Reglamento de Inteligencia Artificial (parte 3)"
  paginas: 28-32
  origen: 2026-07-17-aesia-09-guia-de-precision.pdf
  oficial: false
---
# Reglamento de Inteligencia Artificial (parte 3)

-

-

-

-

-

Saber utilizar e interpretar visualizaciones de monitoreo de la precisión relacionadas con todas las métricas, acorde a la finalidad prevista y su explicabilidad e incertidumbres asociadas en cualquier momento del ciclo de vida del sistema.
Saber usar la salida del sistema, identificando requisitos que podrían ser necesarios para usarlo como entrada en otro sistema de IA. (Ver ISO de Sesgos, SC42_N1011
ISOIEC_TS_4213_2 [116]).
Poder inspeccionar tanto datos de entrada como de salida y tener permiso para corregir y/o notificar al proveedor de potenciales datos o salidas erróneas, o la ausencia de estas.
Disponer de conocimiento sobre las interfaces que proveen transparencia sobre el funcionamiento, salida y métricas de evaluación del modelo de IA, y su interpretación de acuerdo con la explicabilidad del modelo [35] para interpretarla.
Responsabilizarse de entender los potenciales sesgos e imparcialidad que puedan comprometer la precisión del modelo. Por ejemplo, conocer los conceptos de discriminación algorítmica, sesgos e imparcialidad, para detectar posibles problemas o potenciales degradaciones de la salida del modelo. Así como, la degradación de la precisión de forma no favorable para una clase minoritaria o
(grupo de) variables protegidas.

En línea con el ejemplo anteriormente indicado, sobre el sistema de IA para la promoción de empleados, la empresa responsable del despliegue del mismo se recomienda que se asegure de que todos los puntos anteriores son adecuadamente trasladados al personal de recursos humanos.

4.3 Garantizando la precisión
Se recomienda que las métricas de precisión aplicables garantizadas por el proveedor en la documentación técnica deben refleje y sea una señal de la calidad del sistema. De otro modo, cuando no se puedan garantizar estas métricas de precisión establecidas mínimas, el proveedor podría facilitará al responsable del despliegue mecanismos para notificar al humano se requiere su supervisión (según guía de supervisión humana). A modo de ejemplo, el responsable del despliegue podría estar obligado a conocer dicha información y disponer de procesos internos para poderlos llevar a cabo.
En el apartado anterior hemos indicado cómo seleccionar las métricas de precisión para el sistema de IA y como estas se relacionan con otras acciones complementarias. En este apartado vamos a proporcionar la información necesaria para que las métricas seleccionadas, se mantengan de manera consistente a lo largo del ciclo de vida, tal y como establece el
Reglamento Europeo de IA.
Proveedor
El proveedor del sistema de IA es el principal garante de que la precisión se mantenga de manera consistente a lo largo del ciclo de vida de IA, con la aplicación de las medidas que lo garanticen.

27

4.3.1 Medidas técnicas
Las medidas técnicas que el proveedor puede implementar en relación con los inventarios de métricas de precisión y funciones objetivo mencionadas en el apartado anterior (ver apartado 4.2) se identifican con las siguientes acciones:
-

-

Para que la precisión reportada por el sistema de IA sea accionable y útil, dicha documentación puede incluir los rangos posibles de los parámetros configurables, así como los datos de entrada y salida del sistema, y las medidas de latencia esperadas para alcanzar la precisión deseada (ver Guía de Solidez).
La salida del sistema, idealmente, podría acompañarse de una medida de incertidumbre asociada a la precisión de dicha salida.

-

Se recomienda que el proveedor elegirá un mecanismo para almacenar todas las precisiones comunicadas al responsable del despliegue en un registro histórico, conforme a la Guía de Registros, con el fin de permitir la trazabilidad de las métricas de precisión a lo largo del tiempo de uso del sistema y así monitorear su rendimiento (según la Guía de Solidez).

-

Se podrá proporcionar al responsable del despliegue una interfaz gráfica que permita observar las métricas de precisión en el tiempo y detectar incoherencias o mal funcionamiento del sistema (según la Guía de Supervisión Humana), y monitorizarlas (según la Guía de Solidez).

-

La base del razonamiento para seleccionar una métrica u otra para evaluar la precisión del modelo debe documentarse (conforme a la Guía de Documentación
Técnica); véase también el apartado 5, donde se abordan los aspectos relativos a la documentación de las acciones indicadas en esta guía.

Ejemplo - Sistema de promoción de empleados
Durante la fase de análisis del sistema de IA, se ha concluido que una de las medidas establecidas para mantener la precisión a lo largo del tiempo, es disponer en la operación del sistema de un panel donde se muestre las métricas de precisión y su evolución en el tiempo, de esta manera es posible mantener visible el progreso de la precisión y por tanto poder actuar sobre ella en caso de que abandone los rangos de trabajo definidos. El sistema además de mostrar los datos realiza un registro de la información de precisión presentada acorde a lo establecido en los registros.
Del mismo modo durante el análisis del sistema se encuentra que es importante acompañar, tal y como se recomienda en esta guía, de una información de la incertidumbre, el resultado de la salida del sistema, para ello se plantea la utilización de un conjunto de modelos combinados (ensemble learning). La utilización de esta técnica permite establecer un valor de confianza del resultado, basado en las respuestas de los diferentes modelos (ensembles)
combinadas para poder proporcionar una medida de la incertidumbre del resultado.

28

4.3.2 Evaluaciones de significancia estadística
Durante el proceso de selección de la métrica de precisión (así como las funciones objetivo), para dar validez estadística a los resultados para el sistema de IA, se pueden utilizar métricas específicas que podría acompañarse de evaluaciones estadísticas. Las evaluaciones de significancia estadística podrán considerar la distribución de los datos (evaluación paramétricos o no), la dependencia entre ellos (independientes e idénticamente distribuidas, i.i.d, o no) y otras suposiciones concretas de cada evaluación, para así elegir adecuadamente la evaluación relevante (ver guía de datos). Entre ellos, y a modo orientativo:
-
-
-

La evaluación de ranking con signo Wilcoxon. No paramétrico, es decir libre de suposiciones sobre la distribución, y datos dependientes.
Evaluación paramétricos o no.
Se podrán usar el Paired student T-Test, análisis de varianzas, evaluación de KruskalWallis, evaluación Chi-Squared, evaluación de Fisher exacto, test de McNemar,
(incluyendo comparación múltiple, la corrección Bonferroni y la tasa de descubrimiento falsa) u otros.

Muchos de éstos podrán requerirán test adicionales de normalidad en los datos, por ejemplo, análisis de varianzas (ANOVA) para determinar si las medias de más de dos grupos son iguales, o sus diferencias en precisión (accuracy) entre 3 o más modelos son estadísticamente significativos, para lo cual ANOVA asume distribuciones normales y que la varianza sea homogénea. También tener en cuenta la aplicabilidad de este según el Teorema Central del
Límite (Central Limit Theorem).

Ejemplo - Sistema de promoción de empleados
En este sistema de IA, como se ha explicado en el apartado anterior, el proveedor ha realizado la selección de Discounted Cumulative Gain como métrica para evaluar la precisión del sistema.
Sobre este sistema de IA, se realizan una batería de evaluaciones de significancia estadística utilizando la métrica establecida. Para ello se realizan una serie de conjuntos de datos de prueba y validación agrupados por sectores profesionales, para mantenerlos en conjuntos de datos con relación entre ellos y que permitan consolidar adecuadamente los resultados.
Habiendo considerado que los resultados posibles de los diferentes conjuntos de datos no tienen una distribución normal, se ha seleccionado ranking con signo Wilcoxon, para realizar dicha evaluación como mejor herramienta para validar el proceso.
La evaluación de la significancia estadística es utilizada durante el proceso de entrenamiento/prueba para verificar que el modelo se ajusta a las especificaciones definidas en la fase de diseño, y acorde a la finalidad prevista (disponer de un indicador para la promoción de empleados). Permite comparar la evolución del modelo entre sí a lo largo de su evolución en el tiempo, o comparar diferentes modelos candidatos entre sí en un momento del proceso (ensemble learning), sin dejar de considerar la métrica de precisión ni las especificaciones y guiando en el proceso de entrenamiento y prueba.

29

Para más información se puede consultar ISO SC42 N1011.ISOIEC TS 4213_2 (Clasif. Perf)
[116]

4.3.3 Benchmarks de bases de datos y modelos
En la información completa sobre la métrica o métricas de precisión seleccionadas para el sistema de IA, se puede proporcionar información de la realización de benchmarks (pruebas de rendimiento) de los datos y del modelo. Estos benchmarks, deben tener en consideración a la finalidad prevista del sistema. Así se recomienda que la precisión se puede poner en contexto no solo interno dentro del propio sistema de IA, si no el contexto externo en relación con datos y modelos en relación con pruebas repetibles y medibles.
Sería recomendable usar y reportar todas las métricas convenientes para medir la precisión del modelo y conforme a los protocolos establecidos por las evaluaciones benchmark de cada tarea de aprendizaje automático. Podrán usarse y documentarse los benchmarks más usados por la comunidad científica relevante en aprendizaje automático e IA y sus campos de aplicación.
Los benchmarks dependen de la tarea y el estado del arte del campo; por tanto, se recomienda actualizar conforme pasa el tiempo y los modelos y bases de datos evolucionan.
Ejemplos de bases de datos y modelos correspondientes que actúan bien como el estado del arte o bien como modelos de referencia base (baseline) en la tarea de clasificación de imágenes son:
-

-

-

-

En modelos de visión por computador o que procesan imágenes:
o Benchmark / Base de datos ImageNet: Modelos base AlexNet, VGG-19, ResNet50, EfficientNet-B7.
o Base de datos MNIST: Modelos base RDML, MCDNN, LeNet.
o Base de datos CIFAR-10: Modelos base EfficientNet-B7, ColorNet, DenseNet.
o Base de datos LFW: Modelos base FaceNet, DeepID3, DeepFace, etc…
En modelos de lenguaje, Los modelos LSTM, BERT, GPT1, 2, 3, [...], etc. se consideran baselines con respecto al estado del arte. Considerar, además las métricas específicas a la tarea concreta (traducción automática, comprensión lectora, resumen, etc.). Para ello, ver tabla H.1 [4] para un conjunto de tareas y métricas significativas en modelos de lenguaje.
En modelos generativos de imagen se miden el fotorrealismo o diversidad de muestra
(SSIM, MMD, IS, MS, FID, LPIPS). Por ejemplo, para evaluar la consistencia física: IoU (en modelos de segmentación de imágenes) o FVPS [5].
Bases de datos para la imparcialidad incluyen COMPAS recid, COMPAS viol. recid,
Diabetes, OULAD, Credit card clients and many others (ver Tabla 1 en [9]).

Más medidas, a modo orientativo, para asegurar la precisión y documentación del modelo pueden verse en la ISO SC42_N1011_ISOIEC_TS_4213_2 [116].
Responsable del despliegue
Organizativamente, el responsable del despliegue podrá considerar:

30

-

-

El responsable del despliegue tiene la responsabilidad de consultar el manual de instrucciones del sistema de IA para conocer, aplicar y mantener vigilado el modelo
(según guía de datos y guía de supervisión humana).
Tanto responsable del despliegue como todas las partes implicadas o stakeholders
(desde el mayor gestor responsable o top mánager, product owner, project manager y data scientist) es posible que tengan acceso a la justificación de la precisión del sistema y sus métricas asociadas en cualquier momento del ciclo de vida útil del mismo. Para ello se recomienda usar interfaces adaptadas a diferentes audiencias que puedan requerir una explicación del modelo o su auditoría, para así facilitar la transparencia del proceso de razonamiento.

Se recomienda que el responsable del despliegue se familiarice y comprenda al nivel adecuado la interpretación de las nociones y métricas del modelo en cuanto a su precisión y su relación con la finalidad.

31
