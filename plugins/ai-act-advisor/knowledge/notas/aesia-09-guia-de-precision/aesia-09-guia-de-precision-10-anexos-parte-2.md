---
name: aesia-09-guia-de-precision-10-anexos-parte-2
description: "AESIA: aesia 09 guia de precision, sección «Anexos (parte 2)» (págs. 47-54). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-09-guia-de-precision
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Anexos (parte 2)"
  paginas: 47-54
  origen: 2026-07-17-aesia-09-guia-de-precision.pdf
  oficial: false
---
# Anexos (parte 2)

Término

Definición
- b: distancia entre la muestra y todos los puntos del siguiente cluster más
cercano.
Así s = (b-a)/max(a,b)

Cross-entropía binaria

Se trata de una función objetivo, que mide el rendimiento de un modelo de clasificación cuya salida es un valor de probabilidad entre 0 y 1. La pérdida de entropía cruzada aumenta a medida que la probabilidad predicha diverge de la etiqueta real. Así, predecir una probabilidad de
0,012 cuando la etiqueta de observación real es 1 sería malo y daría lugar a un valor de pérdida alto. Un modelo perfecto tendría una pérdida logarítmica de 0.

Curva elevación curve)

de Mide el rendimiento de un clasificador elegido frente a un clasificador
(lift aleatorio.
La curva muestra la relación entre el número de casos que se predijeron positivos y los que son efectivamente positivos y, por tanto, mide el rendimiento de un clasificador elegido frente a un clasificador aleatorio.
El gráfico se construye con el número acumulado de casos (en orden descendente de probabilidad) en el eje de abscisas y el número acumulado de verdaderos positivos en el eje de ordenadas.

Curva respuesta cumulativa

de Esta curva muestra la proporción de ganancias en el total de positivos con respecto a la proporción de registros del conjunto de prueba. Así, podemos analizar qué proporción del conjunto de pruebas es necesaria para obtener un determinado porcentaje de ganancia en el total de positivos.

DCG
(Discounted
Cumulative
Gain)

Se utiliza para sistemas de IA donde se establece un ranking u ordenación, es decir, cuando la puntuación verdadera de una muestra d es un valor discreto en una escala que mide la relevancia con respecto a una consulta q.
Para una consulta q dada y las muestras D = {d₁, ..., dₙ}, se considera la késima muestra. La ganancia Gₖ mide la utilidad de esta muestra, mientras que el descuento Dₖ = 1/log(k+1) penaliza los documentos recuperados con un rango inferior.

46

Término

Definición
La suma de los términos de ganancia descontados GₖDₖ para k = 1...n es la ganancia acumulada descontada (DCG)

Disparate impact

Es la relación de probabilidad de resultados favorables entre los grupos desfavorecidos y privilegiados, permitiendo detectar sesgos o errores de precisión entre ambos conjuntos, privilegiados y desfavorecidos.

Distancia Cook

La distancia de Cook es una medida utilizada para identificar valores atípicos en modelos de regresión. Calcula el cambio en las predicciones del modelo al eliminar una observación específica. Un valor alto en la distancia de Cook indica que esa observación tiene una gran influencia sobre el modelo, lo que puede indicar que es un valor atípico

Divergencia KL La característica principal de la divergencia KL, es medir como una o Divergencia distribución de probabilidad se diferencia de otra. Por su naturaleza, se
Kullback-Lieber trata de una métrica no simétrica, por lo que en sí misma no es una métrica o medida de distancia. Considerada como un enfoque de optimización se puede considerar que tiene dos formas: Forward y Reverse KL.
Especifididad y La sensibilidad es la métrica que evalúa la capacidad de un modelo para sensibilidad predecir verdaderos positivos de cada categoría a predecir por nuestro modelo. La especificidad es la métrica que evalúa la capacidad de un modelo para predecir los verdaderos negativos de cada categoría disponible. Estas métricas se aplican a cualquier modelo categórico.
F-beta

La puntuación F-beta es una métrica utilizada en el campo de la inteligencia artificial para evaluar el rendimiento de un modelo de aprendizaje automático en un problema de clasificación, teniendo en cuenta tanto la precisión (precisión) como el recall (también conocido como sensibilidad o true positive rate). Esta métrica es una medida combinada que proporciona un equilibrio entre precisión y recall.

47

Término

Definición

F1 con media El promedio ponderado de la puntuación F1 (Weighted Averages of F1
Score) es una métrica que se utiliza cuando las clases están
Ponderada desequilibradas y se desea tener en cuenta la importancia relativa de cada clase en la evaluación global del modelo.
La puntuación F1 es una métrica que combina tanto la precisión
(precisión) como el recall. Representa el equilibrio entre la capacidad del modelo para identificar correctamente los casos positivos (recall) y la capacidad de clasificar correctamente los casos positivos entre todas las predicciones positivas (precisión).
Prueba exacta La prueba exacta de Fisher es una prueba estadística utilizada para determinar si existe una asociación significativa entre dos variables de Fisher categóricas en una tabla de contingencia 2x2. Es especialmente útil cuando los recuentos de celdas son bajos, ya que no requiere los supuestos de la prueba Chi-cuadrado.
Focal loss

Una función de pérdida focal aborda el desequilibrio de clase durante el entrenamiento en tareas como la detección de objetos. La pérdida focal aplica un término modulador a la pérdida de entropía cruzada para enfocar el aprendizaje en ejemplos mal clasificados. Es una pérdida de entropía cruzada escalada dinámicamente, donde el factor de escala decae a cero a medida que aumenta la confianza en la clase correcta.
Intuitivamente, este factor de escala puede reducir automáticamente la contribución de ejemplos fáciles durante el entrenamiento y enfocar rápidamente el modelo en ejemplos difíciles.

Frechet
Information
Distance (FID)

La Frechet Inception Distance, o FID para abreviar, es una métrica para evaluar la calidad de las imágenes generadas y desarrollada específicamente para evaluar el rendimiento de las redes generativas antagónicas. Fue propuesta como una mejora con respecto a Inception
Score (IS).

GAN
Condicional
(CGAN)

Las GAN condicionales (CGAN) son una variante de las Redes Generativas
Adversariales (GAN) que incorporan una variable de condición adicional para permitir la generación controlada y condicionada de datos sintéticos.
Esto permite la generación específica de datos basada en información adicional suministrada, lo que amplía las capacidades de las GAN en diversas aplicaciones de generación de datos.

Hamming Loss

Es una métrica que mide la precisión de un modelo de clasificación multietiqueta al calcular la tasa promedio de etiquetas clasificadas incorrectamente. Proporciona una medida general del rendimiento del modelo en la clasificación multi-etiqueta, independientemente del desequilibrio de las etiquetas.

48

Término

Definición

Hinge embedding loss

Es una función de pérdida utilizada en algoritmos de clasificación binaria, como las máquinas de vectores de soporte (SVM). Su objetivo es maximizar el margen entre las clases y penalizar las clasificaciones incorrectas y las muestras cercanas al margen.

Hubber loss

Es una función de pérdida utilizada en el aprendizaje automático. A diferencia de otras funciones de pérdida, como el Error Cuadrático Medio
(MSE), el Huber Loss es menos sensible a los valores atípicos en los datos.
El Huber Loss combina las ventajas del Error Cuadrático Medio y del Error
Absoluto Medio, adaptando su comportamiento en función de un parámetro de tolerancia.

Hyperband
(tool)

Hyperband es un algoritmo de optimización de hiperparámetros que asigna recursos de forma selectiva a diferentes configuraciones de hiperparámetros. Emplea un enfoque de eliminación temprana, descartando rápidamente configuraciones de bajo rendimiento y asignando más recursos a configuraciones prometedoras, lo que permite una búsqueda de hiperparámetros más rápida y eficiente.

Hyperopt

Es una biblioteca de Python que se utiliza para la optimización automática de hiperparámetros. Proporciona herramientas y algoritmos que permiten realizar una búsqueda eficiente de hiperparámetros en el aprendizaje automático.

Inception Score Es una métrica utilizada para evaluar la calidad y diversidad de las imágenes generadas por modelos de generación de imágenes, como las
(IS)
GAN. Se basa en la clasificación de imágenes mediante una red Inception pre-entrenada y combina medidas de diversidad y calidad para proporcionar una puntuación que indica la calidad general de las imágenes generadas.
Índice
FowlkesMallows

de Es una métrica utilizada para evaluar la calidad de las agrupaciones obtenidas en el análisis de datos. Se basa en la comparación de las etiquetas reales y las etiquetas asignadas por un algoritmo de agrupamiento, y calcula un valor que indica la similitud entre las agrupaciones. Un valor más cercano a 1 indica una mayor similitud, mientras que un valor de 0 indica diferencias completas entre las agrupaciones.

Índice de Es una métrica que mide la similitud entre dos conjuntos o regiones. Se
Jaccard utiliza para calcular la superposición entre los conjuntos dividiendo el tamaño de la intersección entre el tamaño de la unión. Es ampliamente
(también IoU)
utilizado en el campo de la visión por computadora y otras áreas donde se necesita medir la similitud o la coincidencia entre conjuntos.

49

Término

Definición

Índice de Rand

Es una métrica utilizada para evaluar la similitud entre dos agrupaciones.
Calcula la proporción de pares de datos que están asignados de la misma manera en ambas agrupaciones. Un Índice de Rand más alto indica una mayor similitud entre las agrupaciones, mientras que un Índice de Rand más bajo indica una menor similitud o una asignación aleatoria de los clústeres.

Información mutua Ajustada

La información mutua ajustada es una métrica utilizada en el análisis de agrupamientos para medir la similitud entre dos conjuntos de etiquetas.
Esta métrica ajusta la información mutua para corregir por azar, proporcionando una estimación de la dependencia entre las etiquetas sin inflarse cuando el número de agrupamientos es alto.

Kruskal-Wallis

Es una prueba no paramétrica utilizada para determinar si hay diferencias significativas entre las medianas de dos o más grupos independientes. Se basa en la comparación de los rangos de los datos y utiliza una estadística de prueba para evaluar la hipótesis nula de igualdad de medianas.

Language
Model
Probability

La probabilidad de modelo de lenguaje es una métrica que evalúa qué tan probable es que un modelo de lenguaje genere una secuencia específica de palabras. Esta métrica se basa en las probabilidades condicionales de cada palabra dada su contexto previo y mide tanto la coherencia como la naturalidad de las secuencias generadas.

LogCosh
(logaritmo coseno hiperbólico)

Es una función de pérdida suave utilizada en problemas de optimización en aprendizaje automático. Es menos sensible a valores atípicos y busca minimizar la diferencia entre las predicciones y los valores verdaderos de manera estable.

Mean Average Es una métrica de evaluación que mide el promedio de las diferencias absolutas entre las predicciones y los valores reales. Es una medida
Error (MAE)
comúnmente utilizada en problemas de regresión para evaluar la precisión de un modelo de aprendizaje automático.
Mean Absolute Es uno de los KPI más utilizados para medir la precisión del pronóstico.
Percentage
Error (MAPE)
MAPE es la suma de los errores absolutos individuales dividida por la demanda (cada período por separado). Es el promedio de los errores porcentuales.
Margin Ranking Es una función de pérdida utilizada en problemas de clasificación y aprendizaje por pares. Su objetivo es maximizar la diferencia entre las
Loss puntuaciones de elementos similares y no similares para entrenar modelos que puedan clasificar elementos o comparar pares de manera efectiva.

50

Término
Matriz confusión

Definición de La matriz de confusión es una tabla que muestra las predicciones de un modelo de clasificación en comparación con los valores reales. Tiene cuatro celdas: verdaderos positivos, falsos positivos, falsos negativos y verdaderos negativos. Esta matriz permite evaluar el rendimiento del modelo y calcular métricas como precisión, exhaustividad y puntuación
F1. Es una herramienta útil para entender cómo el modelo clasifica diferentes clases y mejorar su precisión.

Matriz de Una matriz de contingencia es una tabla que muestra la distribución conjunta de dos o más variables categóricas. Permite visualizar la relación contingencia y las frecuencias de cada combinación de categorías. Es útil para analizar asociaciones entre variables y revelar patrones en los datos.
McNemar

Es una prueba no paramétrica para datos nominales emparejados. Se usa cuando está interesado en encontrar un cambio en la proporción de los datos emparejados. Por ejemplo, podría utilizar esta prueba para analizar estudios retrospectivos de casos y controles, en los que cada tratamiento se empareja con un control. También podría usarse para analizar un experimento en el que se administran dos tratamientos a pares emparejados. Esta prueba a veces se denomina prueba Chi-Cuadrado de
McNemar porque la estadística de prueba tiene una distribución de Chicuadrado.

Mean Squared Es una métrica de evaluación que mide el promedio de las diferencias al
Error (MSE o L2 cuadrado entre las predicciones y los valores reales en un problema de regresión. Es ampliamente utilizado y penaliza más los errores grandes, loss)
pero puede ser sensible a la escala de los datos.
Mean Squared Es una métrica de evaluación utilizada en problemas de regresión. Calcula
Logarithmic la diferencia al cuadrado entre los logaritmos de las predicciones y los logaritmos de los valores reales. Es útil para penalizar más los errores en
Error los extremos y cuando se desea enfocarse en la precisión relativa en lugar de la absoluta.
METEOR

Metric for Evaluation of Translation with Explicit ORdering, es una métrica de evaluación de traducción que tiene en cuenta tanto la fluidez del texto como la correspondencia semántica entre la traducción y la referencia.

Métrica de También conocida como recall, mide la capacidad de un modelo para identificar todos los elementos positivos en un conjunto de datos. Se
Completitud calcula como la proporción de verdaderos positivos sobre la suma de verdaderos positivos y falsos negativos. Una completitud alta indica una buena capacidad para identificar elementos positivos, pero debe considerarse en conjunto con otras métricas para evaluar el rendimiento general del modelo.

51

Término

Definición

Min-max Loss

Es una función de pérdida utilizada en problemas de clasificación.
Penaliza las predicciones incorrectas al maximizar la diferencia entre la probabilidad asignada a la clase correcta y la probabilidad máxima entre las clases incorrectas. Su objetivo es mejorar la capacidad del modelo para distinguir entre las clases y reducir los errores de clasificación.

Modelo de Es un enfoque utilizado en el procesamiento del lenguaje natural para espacio representar y analizar documentos de texto. Los documentos se vectorial (VSM) representan como vectores en un espacio multidimensional, donde cada dimensión corresponde a un término o una característica del texto. Esto permite calcular similitudes o distancias entre los documentos y realizar diversas tareas de análisis de textos.
NIST LRE

NIST Language Recognition Evaluation, el objetivo de esta métrica es establecer una medida de base para el rendimiento y la capacidad de reconocimiento de lenguaje hablado a través del teléfono.

Non saturating Se utiliza en GANs para entrenar el generador de imágenes y superar problemas de saturación y desvanecimiento del gradiente. Proporciona
GAN loss una alternativa efectiva a la pérdida clásica de GAN y ha demostrado ser útil en el entrenamiento de generadores más estables y de alta calidad.
Optuna (tool)

Es una biblioteca de optimización de hiperparámetros que se utiliza para automatizar y facilitar la búsqueda de la configuración óptima de los hiperparámetros de un modelo de aprendizaje automático.

Paired student Es una prueba estadística utilizada para comparar las medias de dos conjuntos de datos relacionados. Se utiliza para determinar si hay una
T-Test diferencia significativa entre los dos conjuntos de datos y se basa en el supuesto de distribución normal de los datos emparejados.
Plotly sunburst Es una representación visual interactiva que muestra la estructura plot (tool)
jerárquica de los datos en forma de anillos concéntricos. Cada anillo representa una categoría o subcategoría y el tamaño de las porciones en el gráfico refleja una métrica específica. Es una herramienta útil para visualizar datos jerárquicos y explorar su distribución de manera intuitiva.

52

Término

Definición

Pointwise
Methods,
Pairwise
Methods,
Listwise
Methods

Todos los modelos de Learning to Rank utilizan un modelo base de aprendizaje para calcular s = f (x). La elección de la función de pérdida es el elemento distintivo para los modelos Learning to Rank. En general, tenemos 3 enfoques, dependiendo de cómo se calcule la pérdida.
Pointwise Methods: la pérdida total se calcula como la suma de los términos de pérdida definidos en cada documento di (por lo tanto, puntualmente) como la distancia entre la puntuación predicha si y la verdad fundamental yi, para i = 1 ... Al hacer esto, transformamos nuestra tarea en un problema de regresión, donde entrenamos un modelo para predecir.
Pairwise Methods: la pérdida total se calcula como la suma de los términos de pérdida definidos en cada par de documentos di, dj (por lo tanto, por pares), para i, j = 1 ... n. El objetivo sobre el que se entrena el modelo es predecir si yi > yj o no, es decir, cuál de los dos documentos es más relevante. Al hacer esto, transformamos nuestra tarea en un problema de clasificación binaria.
Listwise Methods: la pérdida se calcula directamente en toda la lista de documentos (por lo tanto, listwise) con los rangos previstos correspondientes. De esta manera, las métricas de clasificación se pueden incorporar más directamente a la pérdida.

Precisión
Recall (curva)
PRC y Área debajo
PRC
(AUPRC)
Predictive parity

La precisión-recall (PRC) es una métrica que evalúa el rendimiento de un modelo de clasificación en términos de precisión y recall a medida que se varía el umbral de clasificación. La curva PRC traza estos valores, y el área debajo de la curva (AUPRC) resume el rendimiento general del modelo.
Métrica de equidad que comprueba si, para un clasificador determinado, los índices de precisión son equivalentes para los subgrupos considerados.
Por ejemplo, un modelo que predice la aceptación en la universidad satisfaría la paridad predictiva para la nacionalidad si su índice de precisión es el mismo independiente de la nacionalidad de origen
A veces, la paridad predictiva también se denomina paridad de tasa predictiva.

R2

R² es una métrica estadística que mide la proporción de variación en la variable dependiente que es explicada por el modelo de regresión. Indica qué tan bien se ajustan los datos al modelo, con valores de 0 a 1, donde un valor más cercano a 1 sugiere un mejor ajuste.

53
