---
name: aesia-10-guia-solidez-10-anexos-parte-2
description: "AESIA: aesia 10 guia solidez, sección «Anexos (parte 2)» (págs. 51-58). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-10-guia-solidez
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Anexos (parte 2)"
  paginas: 51-58
  origen: 2026-07-17-aesia-10-guia-solidez.pdf
  oficial: false
---
# Anexos (parte 2)

Término

Definición
El error medio (ME, por sus siglas en inglés) es una medida utilizada para evaluar el sesgo o la tendencia sistemática de un modelo o estimación al predecir los valores. Se calcula tomando la diferencia promedio entre las predicciones y los valores reales.

Él ME es una medida que tiene en cuenta la dirección del error. Si las predicciones son sistemáticamente mayores que los valores
Mean error / relative reales, el ME será un número positivo, lo que indica un sesgo error positivo. Por otro lado, si las predicciones son sistemáticamente menores, el ME será un número negativo, indicando un sesgo negativo. El error relativo (RE), por otro lado, proporciona una medida del error en relación con el valor real. Al expresarlo como un porcentaje, es útil para evaluar la precisión relativa del modelo o estimación en diferentes escalas de datos. El RE permite una comparación más directa de la precisión entre diferentes modelos o estimaciones, independientemente de la magnitud de los valores.
En el contexto del aprendizaje automático y el entrenamiento de modelos, el backward transfer (transferencia hacia atrás) y el forward transfer (transferencia hacia adelante) se refieren a la influencia que puede tener el aprendizaje de una tarea en el rendimiento de otras tareas relacionadas.
El backward transfer se produce cuando el aprendizaje de una tarea anterior mejora el rendimiento en tareas posteriores. Es decir, el conocimiento adquirido al aprender una tarea previa ayuda a
Backward transfer, mejorar el rendimiento en tareas subsiguientes.
Por otro lado, el forward transfer ocurre cuando el aprendizaje de forward transfer una tarea posterior mejora el rendimiento en tareas previas. En este caso, el conocimiento adquirido al aprender una tarea posterior influye en la mejora del rendimiento en tareas anteriores.
Estas transferencias pueden ocurrir cuando las tareas tienen cierta relación o similitud en términos de características o estructura subyacente. Si el conocimiento aprendido en una tarea puede ser aplicado de manera efectiva en tareas relacionadas, se produce una transferencia de aprendizaje, ya sea hacia atrás o hacia adelante.

Blooming bright spots

Se refiere a un fenómeno visual que puede ocurrir en imágenes digitales, especialmente en imágenes capturadas por cámaras digitales o sensores CCD (dispositivos de carga acoplada). Está relacionado con la presencia de ruido en las imágenes.

50

Término

Definición

Branch and Bound

Es una técnica utilizada para resolver problemas de optimización explorando sistemáticamente todas las posibles soluciones. Utiliza estrategias de ramificación para dividir el espacio de búsqueda y técnicas de acotamiento para eliminar soluciones no prometedoras. El objetivo es encontrar una solución óptima o aproximarse a ella de manera eficiente.

CalBin

Es una medida de calibración basada en el agrupamiento solapado.
Para cada clase se debe ordenar todos los casos según la predicción p(i, j) reasignando los índices. Se tomarán los 100 primeros elementos como primer bin, se calculará el porcentaje de casos de la clase j en esta casilla como probabilidad real, fj.
𝛴𝑖𝜖|⋯100 |𝑝(𝑖, 𝑗) − 𝑓𝑗|
El error para este bin es,
Posteriormente se calculare el error para el resto de bins.
Finalmente se calculará la media de los errores.

CalLoss

Un clasificador perfectamente calibrado siempre da una curva ROC convexa. Sin embargo, un clasificador puede producir puntuaciones muya latas (AUC alto), pero las probabilidades quizas difieren de las probabilidades reales. Un metodo para calibar un clasificador es calcular el casco convexo o, lo quees lo mismo utilizar la regresión isotonica. Flach y Matsubara (2007) descomponen la puntuación de Brier en pérdida de calibración y pérdida de refinamiento. CalLoss es definida como la desviación media al cuadrado de las probabilidades empiricas derivadas de la pendiente de los segmentos ROC.

Cohen Kappa

Es una medida de acuerdo, utilizada para evaluar la concordancia entre dos evaluadores o clasificadores. Proporciona una medida más robusta que la simple coincidencia en la clasificación y tiene en cuenta el acuerdo esperado por casualidad. Un valor de kappa cercano a 1 indica un alto grado de acuerdo, mientras que un valor cercano a 0 indica un acuerdo similar al esperado por casualidad.

Computational efficiency

La eficiencia computacional en el aprendizaje automático se refiere a la capacidad de los algoritmos y modelos de machine learning para realizar tareas de manera rápida y eficiente en términos de recursos computacionales, como el tiempo de ejecución y la capacidad de almacenamiento.
En el contexto del aprendizaje automático, la eficiencia computacional es un aspecto importante debido a la creciente complejidad de los conjuntos de datos y los modelos. Se busca optimizar el uso de recursos computacionales para lograr un

51

Término

Definición equilibrio entre el rendimiento del modelo y los recursos requeridos.

Confidence-based
Performance estimation (CBPE)

Es una técnica que utiliza las medidas de confianza o probabilidad asignadas por un modelo de clasificación para evaluar su rendimiento. Al establecer un umbral de confianza, se calcula la precisión del modelo solo para las predicciones con una medida de confianza superior a ese umbral, lo que permite obtener una estimación más precisa del rendimiento del modelo en situaciones críticas.
La correlación entre controles y mediciones se refiere a la relación o dependencia que existe entre los valores de los controles utilizados en un sistema y las mediciones resultantes. En el contexto de sistemas de control y monitoreo, es importante comprender cómo los cambios en los controles afectan las mediciones y viceversa.

Correlating and measures

Cuando existe una correlación fuerte entre los controles y las mediciones, significa que los cambios en los valores de los controles tienen un impacto significativo en las mediciones obtenidas. Esto puede ser deseable en algunos casos, ya que indica que los controles tienen un efecto predecible y pueden utilizarse controls para influir en las mediciones de manera controlada.
Sin embargo, también puede haber situaciones donde una correlación fuerte entre los controles y las mediciones no sea deseable. Por ejemplo, si existen factores externos que pueden afectar las mediciones independientemente de los controles, una correlación fuerte puede dificultar la identificación de la verdadera causa de las variaciones en las mediciones.
La comprensión de la correlación entre los controles y las mediciones es esencial en muchos campos, como la ingeniería, la física y la ciencia de datos. Permite analizar y modelar adecuadamente los sistemas, identificar relaciones causales, optimizar los controles para lograr los resultados deseados y

52

Término

Definición entender el comportamiento de los sistemas en diferentes condiciones.

Coverage tests

Son técnicas utilizadas para evaluar qué parte del código fuente ha sido ejecutada durante las pruebas. Hay diferentes tipos de cobertura, como cobertura de línea, cobertura de rama, cobertura de condición y cobertura de camino, que se enfocan en diferentes aspectos del código. Las pruebas de cobertura son útiles para medir y mejorar la calidad del software, aunque no garantizan la ausencia de errores.

Crammer-Singer

Es un método iterativo utilizado para resolver el problema de clasificación multiclase. A través de una serie de transformaciones y optimizaciones, busca maximizar la separabilidad entre las clases en un espacio de características. Este enfoque evita la necesidad de descomponer el problema en clasificadores binarios independientes y puede mejorar el rendimiento de la clasificación al considerar información adicional.

CROWN

Siglas de "Convex Relaxation Of Nonlinear layer" (Relajación
Convexa de Capas No Lineales), es un enfoque utilizado en el campo del aprendizaje automático y las redes neuronales. Es un enfoque que utiliza la programación matemática convexa para aproximar la función de propagación hacia adelante de una red neuronal no lineal mediante una formulación convexa. Proporciona límites superiores e inferiores para la salida de la red neuronal en función de los límites de las entradas, lo que permite realizar análisis de robustez y certificar propiedades de seguridad para el modelo.

Data differentials

Diferencias o cambios en los datos entre diferentes puntos o momentos en el tiempo. Son una medida utilizada para analizar cómo los datos varían o difieren en diferentes situaciones y pueden proporcionar información valiosa sobre las tendencias, patrones y cambios en los datos.

Data shift

Cambio en la distribución de los datos entre el conjunto de entrenamiento y el conjunto de prueba o entre diferentes momentos en el tiempo. Puede afectar negativamente el rendimiento del modelo y requiere enfoques específicos para abordar el problema y mitigar su impacto.

Dataset shift

Se produce cuando hay una discrepancia o cambio en la distribución de los datos entre conjuntos de datos relacionados.
Puede tener un impacto negativo en el rendimiento del modelo y requiere técnicas específicas para mitigar su efecto y mejorar la generalización del modelo.
53

Término

Definición

Destilación

Se refiere a transferir el conocimiento de un modelo maestro más grande y complejo a un modelo alumno más pequeño y simplificado. Se utiliza para entrenar al modelo alumno de manera más eficiente y efectiva, utilizando etiquetas suaves generadas por el modelo maestro en lugar de etiquetas categóricas. Esto permite que el modelo alumno capture el conocimiento y la estructura subyacente de los datos y generalice mejor.

Es un enfoque en el aprendizaje automático que busca estimar directamente la función de pérdida asociada a un problema en
Direct Loss Estimation lugar de utilizar la función de pérdida convencional. El objetivo es
(DLE)
obtener estimaciones más precisas de la pérdida y mejorar el rendimiento del modelo en tareas específicas, teniendo en cuenta aspectos particulares del problema.
Es un método utilizado en el aprendizaje automático para mitigar el olvido catastrófico de conocimientos previamente aprendidos al entrenar modelos en nuevas tareas. Protege selectivamente los
Elastic
Weight pesos importantes para tareas anteriores mediante una función de
Consolidation (EWC)
penalización que evita cambios drásticos en esos pesos durante el entrenamiento en nuevas tareas. Esto permite que el modelo conserve y utilice eficientemente los conocimientos previos adquiridos.

Ensemble Learning

Es un enfoque en el aprendizaje automático que combina múltiples modelos de aprendizaje para mejorar la precisión y el rendimiento general. Al aprovechar la diversidad de los modelos y combinar sus predicciones individuales, se obtiene una predicción final más sólida y confiable. Este enfoque se basa en la premisa de que la combinación de modelos independientes puede superar las limitaciones individuales y mejorar la capacidad de generalización.

54

Término

Definición
Experience Replay, también conocido como replay buffer, prototype experience replay o rehearsal, es una técnica utilizada en el entrenamiento de modelos de aprendizaje profundo, especialmente en algoritmos de aprendizaje por refuerzo.

La idea central de Experience Replay es almacenar y reutilizar experiencias pasadas durante el entrenamiento en lugar de utilizar solo las experiencias más recientes. Esto se logra mediante el almacenamiento de transiciones de experiencia, que consisten en pares de estados y acciones tomadas en un entorno, en una memoria de almacenamiento llamada replay buffer.
Durante el entrenamiento, en lugar de utilizar solo las transiciones más recientes, se muestrean aleatoriamente las transiciones almacenadas en el replay buffer. Esto permite al modelo de
Experience
Replay aprendizaje profundo volver a experimentar una variedad de
(replay buffer, situaciones pasadas, lo que ayuda a evitar la dependencia excesiva prototype experience de las experiencias más recientes y a mejorar la eficiencia y la replay, rehearsal)
estabilidad del entrenamiento.
El uso de Experience Replay ofrece varias ventajas. En primer lugar, ayuda a decorrelacionar las transiciones de experiencia, ya que las experiencias adyacentes en el tiempo pueden estar altamente correlacionadas. Esto evita que el modelo se entrene solo en situaciones similares y mejora su capacidad para generalizar a diferentes situaciones. Además, el replay buffer permite una exploración más efectiva, ya que las transiciones se muestrean aleatoriamente y se pueden evitar comportamientos subóptimos.
Existen variaciones de Experience Replay, como Prototype
Experience Replay, que se enfoca en almacenar y utilizar ejemplos representativos o prototipos para mejorar el rendimiento del modelo.

F1-Score

El F1 score es una medida estadística que combina la precisión y el recuerdo (recall) de un modelo de clasificación. Es útil cuando se tienen clases desequilibradas en los datos. Proporciona una única métrica que representa la precisión y el recuerdo de manera equilibrada, y su valor oscila entre 0 y 1, siendo 1 el mejor resultado posible. Un F1 score alto indica un equilibrio entre la precisión y el recuerdo del modelo en la clasificación de las clases.

Fast-Lin

Algoritmo computacionalmente eficiente. Calcula un límite inferior certificado sobre las perturbaciones de entrada permitidas para redes ReLU utilizando un enfoque capa por capa y búsqueda binaria en el dominio de entrada.

55

Término

Definición

Fast-Lip

Algoritmo computacionalmente eficiente. Depende de Fast-Lin para calcular los límites de las funciones de activación y, además, estima la constante local de Lipschitz de la red. En general, Fast-Lin es más escalable que Fast-Lip, mientras que Fast-Lip proporciona mejores soluciones para límites ℓ1.

Formal safety analysis

Se requiere un análisis formal de las redes neuronales debido a los riesgos asociados con las predicciones erróneas en situaciones adversas. Este enfoque permite verificar propiedades de seguridad y encontrar contraejemplos concretos en redes más grandes, lo que mejora significativamente la capacidad de análisis existente.
Además, este enfoque puede contribuir a mejorar la explicabilidad y la robustez de las redes neuronales.

Es una técnica de evaluación de modelos que tiene en cuenta la estructura grupal de los datos. Divide los datos en grupos predefinidos y evalúa el rendimiento del modelo en conjuntos de
Group K fold cross prueba y entrenamiento que son representativos de diferentes validation grupos. Esto permite una evaluación más precisa del rendimiento del modelo en situaciones del mundo real donde los datos tienen una estructura grupal.

K-fold cross validation

Es una técnica que divide los datos en k pliegues y realiza k iteraciones para evaluar y seleccionar modelos. Proporciona una estimación más precisa del rendimiento del modelo y ayuda a evitar problemas de sobreajuste o subajuste al utilizar todos los datos de manera más efectiva.

League training

Es una técnica de entrenamiento en la que múltiples agentes son entrenados en paralelo y compiten entre sí en un entorno de juego.
A través de la competencia interna, los agentes aprenden y mejoran sus estrategias con el objetivo de alcanzar un rendimiento óptimo en la liga.

Leave-one-group-out cross validation

Es una técnica de validación cruzada que deja fuera un grupo completo en cada iteración como conjunto de prueba. Es útil cuando los datos tienen una estructura de grupos relacionados y permite evaluar el rendimiento del modelo teniendo en cuenta las características específicas de cada grupo.

Leave-one-out validation

Es una técnica de validación cruzada en la que se deja fuera una cross única muestra como conjunto de prueba en cada iteración. Permite una evaluación exhaustiva del modelo utilizando todos los datos disponibles, aunque puede ser computacionalmente costoso.

56

Término

LogLoss

Definición
También conocida como pérdida logarítmica o pérdida de entropía cruzada, es una métrica de evaluación común para los modelos de clasificación binaria. Mide el rendimiento de un modelo cuantificando la diferencia entre las probabilidades predichas y los valores reales. La pérdida logarítmica es indicativa de cuán cerca está la probabilidad de predicción del valor real / verdadero correspondiente (0 o 1 en el caso de la clasificación binaria), penalizando las predicciones inexactas con valores más altos. Una menor pérdida de registro indica un mejor rendimiento del modelo.
Log Loss es la métrica de clasificación más importante basada en probabilidades. Es difícil interpretar los valores de pérdida de registro sin procesar, pero la pérdida de registro sigue siendo una buena métrica para comparar modelos. Para cualquier problema dado, un valor de pérdida logarítmica más bajo significa mejores predicciones.

Macro-average accuracy

Es una métrica utilizada para evaluar el rendimiento de un modelo de clasificación en problemas multiclase. En lugar de calcular la precisión para cada clase individualmente y promediar los resultados, la precisión promedio macro calcula la precisión por clase y luego realiza un promedio no ponderado de estas precisiones. Toma en cuenta el rendimiento de todas las clases por igual y no se ve afectada por el desequilibrio de clases en los datos.
Cada clase contribuye de manera equitativa al cálculo de la precisión promedio macro, lo que la hace adecuada cuando se desea evaluar el rendimiento general del modelo en todas las clases por igual.

Es una métrica utilizada para evaluar el rendimiento de un modelo de clasificación binaria. Proporciona una medida del equilibrio entre los verdaderos positivos, los verdaderos negativos, los falsos positivos y los falsos negativos. Es una métrica útil cuando se trabaja
Matthews correlation con conjuntos de datos desequilibrados, donde las clases positivas coefficient y negativas tienen diferentes proporciones. A diferencia de la precisión o el recall, el MCC no se ve afectado por el desequilibrio de clases y proporciona una evaluación más equilibrada del rendimiento del modelo.
MaxError

ME o Error Máximo es el valor absoluto de la diferencia más significativa entre una variable predicha y su valor real.

57
