---
name: aesia-10-guia-solidez-05-reglamento-de-inteligencia-artificial-pa
description: "AESIA: aesia 10 guia solidez, sección «Reglamento de Inteligencia Artificial (parte 2)» (págs. 23-30). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-10-guia-solidez
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Reglamento de Inteligencia Artificial (parte 2)"
  paginas: 23-30
  origen: 2026-07-17-aesia-10-guia-solidez.pdf
  oficial: false
---
# Reglamento de Inteligencia Artificial (parte 2)

4.1.3 Validación y Verificación
La evaluación de la solidez requiere de la intervención de dos pasos muy importantes que se pueden identificar claramente, validación y verificación:
- Verificación: Confirmación, mediante la provisión de evidencia objetiva, de que se
han cumplido los requisitos especificados (ver ISO/IEC 25000:2014 - Systems and software engineering 4.43 e ISO/IEC 25030:2019 - Systems and software engineering
3.22) de acuerdo con la forma en que se especificaron2. Esta fase, no requiere ejecutar el programa con datos reales y se ejecuta antes de la validación.
- Validación: Confirmación, a través de la provisión de evidencia objetiva, de que se
han cumplido los requisitos de la finalidad prevista del sistema de IA (ver ISO/IEC
25000:2014 - Systems and software engineering 4.41 e ISO/IEC 25030:2019 - Systems and software engineering 3.21). La validación incluye probar el sistema de IA, previamente verificado, utilizando conjuntos de datos reales, ejecutar el código para validar que hace lo que debería hacer y funciona como se esperaba.
La mayoría de los tipos de datos procesados por diferentes arquitecturas, por ejemplo, de redes neuronales, pueden ser analizados por al menos un método formal (ver ISO/IEC
24029-2:2023. Artificial intelligence (AI) — Assessment of the robustness of neural networks
— Part 2: Methodology for the use of formal methods). Cada método, con sus ventajas e inconvenientes (principalmente la escalabilidad, etc.) puede atajar uno o más criterios de entre los deseados en el modelo de evaluación de solidez: estabilidad, sensibilidad, relevancia o alcanzabilidad. En el 7.1 Anexo I: Métricas y pruebas para sistemas de IA, se ofrece una serie de mecanismos que pueden ser utilizados para el análisis de estos tipos de datos.

Ejemplo – Detección de denuncias falsas
Para ampliar los mecanismos de verificación y validación del modelo de detección de denuncias falsas se establece un método formal incompleto de caja negra y determinista (ver en el Anexo I).
Para ello entre las denuncias establecidas como ciertas y las denuncias establecidas como falsas, se extrae un grupo de control. Del conjunto total original, se extrae un listado de palabras relacionadas con ambos tipos de denuncias. Con esta lista de palabras, para cada denuncia de este grupo de control, se establece el conteo estadístico de frecuencia de aparición.
Con estos datos se construye una función que proporciona en relación con la distribución de palabras, el resultado exacto para cada una de las denuncias del grupo de control.
En la fase de validación y verificación se comparan las predicciones del sistema de IA, con las predicciones de la función establecida, tanto para ejemplares del grupo de

Cumpliendo especificaciones especificadas, verificaciones tempranas de errores de programación, verificación de programas y documentos a través de un recorrido del sistema con un tutorial paso a paso, etc.
2

22

control como fuera de éste. De esta manera este método formal complementa el proceso de verificación y validación.

4.1.4 Eficiencia en sistemas de IA
Los sistemas de IA de alto riesgo pueden ejecutarse en entornos con diferentes capacidades de cómputo, tanto para aquellos que se encuentran en etapa de inferencia como para aquellos que continúan aprendiendo con el tiempo, la capacidad de cómputo disponible va a afectar profundamente a la solidez del sistema.
Es muy importante, por tanto, que las métricas escogidas para validar las características de la solidez se validen y verifiquen (ver apartado 4.1.3) en entornos hardware que repliquen exactamente las capacidades de cómputo (memoria, CPU, precisión numérica, velocidad de procesado etc.) finales a las que tendrá acceso el sistema de IA. Si el sistema va a ser instalado por el responsable del despliegue las instrucciones de instalación, se recomienda que tengan indicadas las necesidades de ese hardware y su relación directa con la precisión del sistema.
En aquellos casos en los que además puedan existir restricciones de cómputo o memoria, proporcionamos ejemplos orientativos de medidas:
1. Aprendizaje máquina en el filo, cuando se requiera obtener precisión y solidez con recursos computacionales limitados, tales como ejecutar un modelo en un dispositivo móvil como un teléfono en tiempo real o incluso en dispositivos IoT
(sensores inteligentes) u otros dispositivos (cámaras).
2. Destilación [47], cuando existen limitaciones en la memoria del sistema que ejecutará el sistema de IA.
3. Aprendizaje privilegiado destilado [92], cuando no se dispongan de todas las modalidades de datos que se usaron durante el entrenamiento en tiempo de inferencia.
4. Aprendizaje continuo [25], cuando el modelo no pueda crecer en arquitectura y número de parámetros conforme aumenten las tareas de aprendizaje, y deba mantener niveles mínimos de precisión para todas las tareas para las que fue entrenado.
5. Técnicas de compresión y poda de redes (cuando la memoria ocupada por los modelos se exceda de un umbral de memoria) u otros.

4.1.5 Rendimiento en sistemas de IA
Las métricas de solidez asociadas al hardware y rendimiento del sistema se recomienda que se describan en la documentación del sistema antes de diseñar las pruebas de precisión y rendimiento de la etapa de ejecución del sistema. De esta manera se establecerá el rendimiento y eficiencia objetivo para, por ejemplo, tratar un número específico de consultas o solicitudes por hora.
- Se podrá considerar la solidez de la precisión, rendimiento y las estrategias de su
implementación dentro del sistema de IA como un todo, y cómo están restringidas
23

por limitaciones en la disponibilidad de recursos, tales como la memoria o energía.
Por ejemplo, una métrica puede ser el rendimiento por potencia en vatios o rendimiento por vatio (6.6.5 ISO SC42 N1011), aunque julios por vatio o nano julios por píxel puede ser más intuitivos para calcular estadísticas agregadas [38]. A nivel de hardware, la capacidad de memoria requerida (por ejemplo, en Python, se puede usar Memray para el seguimiento de reservas de memoria y producir informes).
- Métricas de complejidad computacional: pueden medir la degradación en la parte
de solidez. Por ejemplo, en modelos de aprendizaje automático, se traducirían a latencia de inferencia (por ej. latencia de clasificación, eficiencia de clasificación, rendimiento de clasificación y consumo de energía).
- Métricas de rendimiento: como capacidad de procesado en cortos periodos de
tiempo, por ej. en FLOPS (Floating Point Operations Per Second), o eficiencia, capacidad de procesamiento mantenida durante una unidad representante de un largo periodo de tiempo, por ej. en FLOPY (Floating Point Operations Per Year). Por ejemplo, aunque la latencia se suele usar para medir interacciones de cara al cliente, y rendimiento en aplicaciones de servidor, en IA se recomienda que se adapten al problema concreto, por ejemplo, en un clasificador de imágenes, la eficiencia puede medirse en el número de imágenes procesadas en un segundo para un tamaño de lote mucho mayor de 1, o en latencia cuando el tamaño de lote es uno (la latencia es inversamente proporcional a la eficiencia).
Otras consideraciones adicionales que contribuyen a alcanzar la solidez adecuada del modelo se basan en el hardware y su monitorización durante diferentes puntos del ciclo de vida del modelo de IA:
- Hardware para el uso de arquitecturas más complejas. Para alcanzar los valores
deseables de las métricas de precisión y solidez especificadas en los requerimientos del sistema, los proveedores podrán utilizar medidas de aceleración de cómputo para hardware especializado, unidades de procesamiento gráfico (GPUs), circuitos integrados de aplicación específica, o conjuntos de instrucciones embebidos en unidades de procesamiento central (CPUs)3.
- El hardware y arquitecturas asociadas a un nivel de precisión y solidez se recomienda
que sea transparente, fijo, y actualizado en su caso, en la documentación establecida
(según guía de Documentación Técnica).
- Se podrán considerar las posibles incoherencias en el sistema debido a diferencias
latencias4 de clasificación.
- Reforzamos de nuevo una continuidad exacta entre entornos hardware de
desarrollo, verificación y validación, que permita que las métricas obtenidas sean entendibles en contextos de idéntica capacidad de cómputo y arquitectura. En aquellas situaciones en las que no sea posible disponer del mismo entorno entre
3

Otros aceleradores pueden aplicarse a funciones simples (como la multiplicación de matrices) o complejas (una función
ResNet). Además, debido a restricciones de medidas de ahorro debido a recursos energéticos, la prolongación de entrenamiento de ciertos modelos podría favorecer la precisión sobre otros entrenados durante menor tiempo.
4

La latencia de clasificación mide la duración entre la entrada de datos del usuario al modelo y la salida de la inferencia del modelo, y determina la calidad (en este caso, la precisión y solidez) del servicio provisto, la cual debe caer dentro de un intervalo paraguas que defina las restricciones operacionales de la implementación de este, y reporte cuando la ejecución de la inferencia del modelo sobrepasa límites no razonables (ISO SC42 N1011).

24

fases del ciclo de vida, será necesario, establecer unas condiciones de solidez específicas para cada entorno, de cara a permitir el paso de diseño a verificación y de ésta a validación. En ese caso los valores y consideraciones objetivo (definidas como especificaciones) pueden estar establecidas en el hardware y su arquitectura del sistema final. De nuevo recordamos que, si el sistema va a ser instalado en las instalaciones del responsable del despliegue, en cualquier formato de comercialización posible, se deben definir claramente unos requisitos mínimos (e idealmente recomendados) en los que se pueden garantizar los requisitos de solidez.

Ejemplo – Sistema de promoción de empleados
El sistema de promoción de empleados en uno de sus formatos de comercialización se entrega al responsable del despliegue para que este realice la instalación de éste. El proveedor decide establecer una serie de métricas adicionales a la solidez: latencia de una evaluación individual y capacidad de procesamiento por segundo de evaluaciones, considerando en el diseño del sistema que estos dos elementos son claves para evitar que un procesado demasiado lento pueda perjudicar la posición en la clasificación de una persona por retraso en el cálculo de su puntuación.
Dado que estos dos puntos son fuertemente dependientes de la relación con el hardware, y durante las fases de diseño y validación/verificación no se tendrá acceso a los mismos recursos hardware que durante la producción:
-
-

-

-

Se establecen los valores mínimos para el hardware de desarrollo y preproducción, que deben alcanzarse siempre en cualquier iteración del algoritmo.
Se establecen unas especificaciones mínimas de hardware sobre las que se alcancen los valores esperados en un entorno productivo. Estas pruebas se ejecutan siempre que se considera una versión lista para producción y son condición necesaria para que pueda darse la versión como correcta (siempre unida a otros elementos significativos de la solidez, no como condición única).
El sistema incluye un registro especial de las dos características (latencia y evaluaciones por segundo) durante su ejecución para informar de su posible degradación, tanto por cambios en los datos, como por modificaciones en las volumetrías iniciales.
Se genera en las instrucciones del sistema las indicaciones de los requisitos mínimos y las volumetrías consideradas, para que el usuario pueda establecer unos requisitos hardware en sus instalaciones que le garanticen el funcionamiento del sistema de IA.

4.1.6 Monitorización de la solidez
Los sistemas de IA son artefactos software con una naturaleza muy especial, eso hace que su comportamiento a lo largo del tiempo pueda variar, no solo en aquellos casos en los que el sistema continúa aprendiendo con el tiempo, si no en general en todos los escenarios.
25

La aparición de espacios de dominio no esperados en los datos de entrada, o incluso la existencia de errores o fallos no detectados que pueden afectar a la precisión, solidez o incluso a la finalidad prevista causando daño a las personas o afectar derechos y libertades, son aspectos que no pueden ser descartados.
Este tipo de monitorización encaja en el escenario de una monitorización post comercialización (consultar dicha guía).
Centrado en la solidez, un monitoreo adecuado involucra observar estadísticas, distribución de los datos y cambios en el uso del negocio. Otras nociones para tener en cuenta a modo orientativo son:
- Se podrán proveer mecanismos de retroalimentación para distinguir entre errores
del responsable del despliegue haciendo mal uso del sistema de los del propio sistema siendo inflexible para satisfacer las necesidades del responsable del despliegue (errores del sistema), o el sistema haciendo suposiciones erróneas sobre el responsable del despliegue (Errores de contexto).
- Se recomienda anotar los tipos de errores en un proceso de resolución de problemas
que incluya un registro de problemas, su razonamiento o causa y tipo de arreglo, permanente o a corto plazo y su efectividad (y según guía de registros) y se documentará siguiendo las indicaciones para cambios y actualizaciones tal y como se indica en la documentación técnica.
- Los proveedores podrán implementar la capacidad de auditar los modelos basados
en principios éticos (por ejemplo, [57]), de forma que se señalen las tensiones clave responsables bajo las consecuencias éticas, y reconocer éstas como compromisos.
Para ello, se deberán usar metodologías de evaluación de solidez (basadas en la evaluación de la Estabilidad, sensibilidad, Relevancia o Alcanzabilidad [ISO/IEC
24029-2:2023 SC42 N938 ISO IEC CD 24029-2]), o la evaluación de conformidad para guiar los procesos que preservan los principios de IA responsable de CapAI [57].
Existen diferentes plataformas que permitan realizar este control o seguimiento, tanto comerciales como de código abierto. El proveedor puede seleccionar cualquiera de ellas para formalizar este seguimiento, u optar por un desarrollo propio siempre que la solución elegida cumpla con los requisitos del Reglamento Europeo de Inteligencia Artificial.
La solidez no se puede entender sin estar relacionada con la supervisión y la transparencia que establecen como se comunica la información del estado del sistema y el impacto que esta tiene en la toma de decisiones, se recomienda consultar o revisitar las guías respectivas de estos aspectos. Es importante considerar que se informe a un experto en el dominio de la finalidad prevista del sistema, que no necesariamente pueda tener conocimientos de IA.

4.2 Solidez y resistencia a errores
En el apartado introductorio de la guía hemos visto, apoyados en las consideraciones que proporciona el Reglamento Europeo de IA, que el sistema debe disponer de solidez técnica (tal y como lo indica el considerando (75) del Reglamento) para evitar que los fallos,
26

errores o incoherencias puedan tener consecuencias para la seguridad, o afectar de manera negativa derechos fundamentales.
Igualmente, a lo largo del apartado 4.1, se han desarrollado a modo orientativo las medidas organizativas y técnicas necesarias para establecer la solidez del sistema y como medirla en el tiempo.
Sobre este aspecto, es el propio Artículo 15 del Reglamento Europeo de la IA en el párrafo
4, el que indica que:

AI Act
Art.15.4 – Precisión, solidez y ciberseguridad
Los sistemas de IA de alto riesgo serán lo más resistentes posible en lo que respecta a los errores, fallos o incoherencias que pueden surgir en los propios sistemas o en el entorno en el que funcionan, en particular a causa de su interacción con personas físicas u otros sistemas. Se adoptarán medidas técnicas y organizativas a este respecto.

Por tanto, es evidente que es necesario, asociado al concepto de solidez, establecer estrategias de predicción de fallos, consecuencias no intencionadas de efecto negativo y efectos que afecten a la seguridad de las personas o que afecten de manera negativa derechos fundamentales tendrán que ser estudiadas y valoradas para evitar su alcance en posibles mal ejecuciones del sistema de IA.
El proveedor es el responsable de poner en marcha las medidas destinadas a mitigar la falta de solidez en sistemas de IA frente a errores, fallos e incoherencias.
Organizativamente y a modo de ejemplo orientativo y no vinculante, el proveedor:
- Facilitará la implementación de técnicas de alerta (señalando qué casos especiales
necesitan cambios en las reglas para corregir esas decisiones en el futuro) a las partes responsables o, en último caso, si no se recibe respuesta de éstas en un tiempo establecido como seguro, se implementará funcionalidad que permita el apagado automático del sistema. En el caso específico de solidez que nos ocupa, el sistema se recomienda que esté preparado para cuando la solidez este comprometida, lanzar dichas alertas. La implantación automática basada en IA debe usar protocolos de seguridad ante fallos, como por ejemplo permitir en cualquier momento la intervención del humano. Este aspecto se detalla en la guía de supervisión humana.
- Introducir protocolos de seguridad ante fallos. El desarrollo de tecnologías de IA con
protocolos de seguridad ante fallos se recomienda que permita a los humanos predecir percances catastróficos, aunque su aparición sea rara, deberá reservar una planificación de diseño que conllevará un dedicado esfuerzo a intentar predecir futuros riesgos y trampas en que puede caer el sistema.

27

Medidas técnicas para preservar la solidez como resistencia a fallos, errores o incoherencias técnicas incluyen los aspectos que se detallan a continuación.
Previo al desarrollo del sistema de IA, se podrán establecer diálogos con diferentes partes involucradas, maximizando la diversidad e inclusión de diferentes perfiles del dominio durante el diseño, desarrollo, mantenimiento, aplicación, supervisión y uso del sistema. El objetivo es prevenir consecuencias catastróficas del posterior uso del sistema cuando haya sido implantado.
Una aproximación orientativa de este enfoque es elaborar diferentes comités de evaluación del diseño del modelo que serán involucrados, con diferentes puntos de vista de expertos con diversa trayectoria, para poder predecir (y atajar, en fase de diseño), incoherencias de diseño o implementación del sistema que puedan conducir a consecuencias inesperadas no deseadas. En pymes y empresas de nueva creación, estos comités pueden enfocarse a grupos de trabajo de toda la compañía donde se pueda evaluar una operativa transversal del proceso.
El pensamiento para instaurar consiste en la idea de la “IA segura basada en el sufrimiento, a favor de un comportamiento seguro ante fallos ": Es más fácil esforzarse en evitar desencadenamientos muy trágicos que podrían ocurrir el desplegar un sistema de IA dado, que intentar asegurarnos de que todos los aspectos del sistema funcionarán siempre correctamente y como es esperado [40].
Otro enfoque es el clásico en IA segura del compromiso o contraprestación entre la probabilidad de éxito y la controlabilidad. En este caso, si es difícil controlar los valores del resultante agente artificial, entonces el riesgo que se supone es un callejón sin salida, mientras que en la IA del fracaso seguro no requiere preocuparse de la controlabilidad del sistema al mismo nivel, mientras haya suficiente controlabilidad para predecir que se pueden evitar.
En la IA segura centrada en el sufrimiento, se proponen estrategias de intervención tales como:
- Influenciar las salidas del sistema con IA controlada, a través de la propagación de los
valores fundamentales del mismo, o estrategias de IA segura dirigidas como el progreso diferencial para alejar diferencialmente al sistema del peor caso. También identificar IA segura donde más se necesita, identificando el peor evento que podría ocurrir por un fallo controlado, y trabajar hacia identificar un control general o mecanismos de apago del sistema.
- Diseñando maneras de hacer fallar al sistema de IA con fallos agraciados o
"benignos”, de manera que hubiese aún peores fallos que el diseño de este fallo agraciado5.

5

La implementación de valores seguros del sistema puede hacerse preguntándose si la corregibilidad reduce los riesgos de que el sistema provoque sufrimiento [41].

28

Ejemplo – Sistema de promoción de empleados
Durante el análisis de riesgos del sistema de IA se ha considerado como un riesgo que el sistema no cuente con la misma cantidad de información para todos los empleados, lo que puede causar que la evaluación no se realice correctamente causando que aquellos empleados que tengan menos información dentro del sistema resulten discriminados. Los errores que pueden causar que la información no se incorpore en el sistema para un empleado dado, son muy variados, y de difícil inventario pues el sistema se integra con varias fuentes.
Para subsanarlo se considera la posibilidad de falta de información (es decir el fallo en la entrada de datos) como posible para todos los empleados. Para ello se crean dos formas de tratar con este potencial error:
-

-

El sistema elabora un listado de todos los empleados que tienen menos información que la media, y elabora alertas sobre ellos para que pueda ser revisado por el personal y subsanada la falta de información, por cualquiera de los orígenes.
El sistema es capaz de proporcionar una lista alternativa de valoración de empleados, en los que se añade una valoración sobre la información faltante para aquellos empleados que no está completa, basada en un análisis de los datos de aquellos que, si cuentan con la información completa, para disponer de una aproximación del estado de promoción para aquellos empleados con fallo de incorporación de información.

Organizativamente, a modo de ejemplo orientativo y no vinculante, los responsables del despliegue deberán familiarizarse con casos pasados y las lecciones aprendidas en casos de uso similares reportados, documentados y mantenidos al día por el proveedor en la documentación actualizada del sistema.
El responsable del despliegue es el responsable de utilizar los canales proporcionados por el proveedor para notificar adecuadamente la presencia de errores, dado que vigilarlos es su responsabilidad. Se recomienda, por tanto, que el proveedor proporcione medios para gestionar la recepción de notificación de la presencia de errores, por parte del responsable del despliegue.
Técnicamente, el responsable del despliegue se recomienda que esté preparado para:
1. Disponer de personal con conocimiento, o formarlo, en caso necesario, sobre los conceptos y posibles implementaciones de mecanismos de seguridad ante fallos definidos por el proveedor.
2. Actuar ante la falta de solidez como concepto de degradación del modelo.

29
