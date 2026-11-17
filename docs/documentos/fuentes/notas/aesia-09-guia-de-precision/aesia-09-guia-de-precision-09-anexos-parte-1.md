---
name: aesia-09-guia-de-precision-09-anexos-parte-1
description: "AESIA: aesia 09 guia de precision, sección «Anexos (parte 1)» (págs. 39-46). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-09-guia-de-precision
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Anexos (parte 1)"
  paginas: 39-46
  origen: 2026-07-17-aesia-09-guia-de-precision.pdf
  oficial: false
---
# Anexos (parte 1)

7. Anexos
7.1 Métricas de precisión
En este anexo presentamos, a título orientativo y no vinculante, una serie de métricas de precisión que pueden ser utilizadas y los tipos de modelos con los que se relacionan. Este
Anexo no pretende ser una enumeración exhaustiva de métricas existentes, sino una presentación de aquellas que, a modo de ejemplo, se puedan aplicar a los tipos de modelos presentados. El proveedor deberá tener en cuenta que una tipología específica de modelo o finalidad prevista (o la combinación de ambas) podrá requerir un análisis más específico de la métrica a seleccionar y que podría esta no encontrase en el listado presentado.
En los siguientes puntos se describen las métricas de precisión propuestas para medir la precisión, agrupadas por la tipología del modelo asociado.
1. Métricas de error para modelos regresión: MSE, RMSE, MAE, MAPE. R² y R² ajustada.
2. En modelos de clasificación, el cómputo de métricas incluirá el uso de elementos básicos de precisión, exactitud, tasas de aciertos y otras métricas de rendimiento del modelo, de acuerdo con la relevancia de la finalidad prevista del sistema del sistema de IA. En este sentido, podrá incluir:
-
-
-

Matriz de confusión.
Exactitud o tasa de aciertos (accuracy).
Precisión, recall y especificidad y sensibilidad, el valor F1, F_beta, y/o la divergencia Kullback-Lieber.

2.i. Clasificación Binaria. En particular, los modelos implementados para realizar clasificación binaria podrían reportar:
-
-
-
-
-

Matriz de confusión.
Tasa de aciertos.
Valor F (F1 o F_beta cuando se quiere dar importancia mayor a precisión (que a exhaustividad o, al contrario), y/o la divergencia Kullback-Lieber.
Curva de Precisión y recall, área bajo la curva ROC (Característica Operativa del
Receptor) y área bajo la curva AUROC.
Curva de respuesta cumulativa, y curva de elevación (lift curve).

2.ii Métricas de evaluación en clasificación multiclase: Error de cobertura, el valor de precisión media del ranking de etiqueta, y Ranking loss, curva AUROC (útil cuando hay datos no balanceados y el ranking entre predicciones es importante). Además, los modelos de clasificación multiclase se recomienda que se reporten:
-
-

Precisión (accuracy), precisión macro-media, micro-media y media-ponderada.
Métricas de distancia o diferencias en distribuciones. Por ejemplo, en destilación, se puede medir la fidelidad entre distribuciones (la métrica de acuerdo medio o la divergencia KL media [33] entre distribuciones).

38

Por ejemplo, la fidelidad (divergencia KL media) se puede usar para medir el grado de alineación entre el modelo aprendido por el modelo estudiante y el modelo profesor, cuando el estudiante simplifica el del profesor, aplicando aprendizaje con destilación.
2.iii Métricas de evaluación en clasificación multi-etiqueta: Se recomienda reportar al menos una de las siguientes métricas:
-
-
-
-

Función objetivo Hamming Loss.
Ratio del match exacto.
Índice de Jaccard, o IoU (intersección sobre unión).
Métricas de distancia o diferencias de distribución.

3. Métricas de evaluación de clustering: éstas incluyen el valor de información mutua ajustada, índice de Rand, el valor de Calinski y Harabaz, de Davies-Bouldin, matriz de contingencia, la métrica de completitud, el índice Fowlkes-Mallows, el coeficiente Silueta medio, etc.
4. En otras tareas de aprendizaje automático más concretos, estudiar la métrica más conveniente para cuantificar la precisión del modelo. Por ejemplo:
4.i Métricas de evaluación en problemas de aprendizaje automático con datos no balanceados: Se usan métricas de clasificadores de una clase (unary o one-class classifiers) y de detección de anomalías. En particular, una curva precisión-recall (PRC) y el área bajo ella (AUPRC) son métricas más adecuadas que una curva ROC y la métrica
AUROC para mostrar precisión con datos no balanceados. Valor F1 con media ponderada (Weighted-average F1) también es una métrica representativa en estos casos.
4.ii Evaluación de modelos del lenguaje: En reconocimiento del habla se usa la perplejidad de los datos de evaluación, tasa de errores por palabra (Word Error Rate,
WER). Otras métricas más genéricas son Language Model Probability y Word Accuracy,
BLEU, METEOR, NIST LRE y otras.
4.iii Para evaluar modelos de imágenes, se pueden usar métricas específicas a la tarea;
Por ejemplo, en segmentación de objetos en imágenes: intersección sobre la unión
(IoU). En modelos generativos, se podrá reportar la Frechet Information Distance (FID) o
Inception Score (IS). En modelos de autoencoders como VAE se pueden usar sharpness,
Inception score. FID score, entre otras métricas [3].

7.2 Funciones Objetivo
En este anexo presentamos, a modo orientativo y no vinculante, una serie de funciones objetivo, agrupadas por las tipologías de modelo o tareas con los que se relacionan.

7.2.1 Funciones objetivo regresión, clasificación o ranking
A continuación, listamos funciones objetivo de regresión, de clasificación o de ranking:
1. En regresión se podrán usar: MAE (Mean Average Error), MSE (Mean Squared Error o L2 loss), MAPE (Mean Absolute percentage Error), Mean Squared Logarithmic Error (robusta a valores anómalos), similaridad coseno, logaritmo del coseno hiperbólico (LogCosh), Huber loss (menos sensible a valores anómalos).
39

2. En clasificación dependiendo del mecanismo del modelo utilizado.
2.i Clasificación binaria se recomienda la utilización de las funciones objetivo: Hinge embedding loss (también para aprender representaciones o embeddings no lineares o tareas semi supervisadas), cross-entropía binaria (BCE), divergencia KL, etc.
2.ii Clasificación multi clase se podrán usar funciones objetivo como la probabilidad logarítmica negativa (negative log likelihood NLL), Entropía cruzada (Crossentropy),
Entropía cruzada categórica, Entropía cruzada categórica sparse, de Poisson,
Divergencia KL (para asegurarse que la distribución de las predicciones es similar a la de los datos de entrenamiento) y para aproximar funciones complejas).
2.iii Clasificación multi-etiqueta: La función objetivo Hamming Loss.

7.2.2 Funciones objetivo en otros tipos de modelo
Para otros tipos de modelo del sistema de IA de alto riesgo, se enumeran en este apartado un compendio de otras posibles funciones de objetivo aplicables, con el objetivo de establecer la precisión de los modelos.
-
-

-
-

-

-

En clasificadores con datos no balanceados, o detección de objetos: Focal loss.
En problemas de ranking, se podrán usar funciones objetivo como la función objetivo de ranking de margen (Margin Ranking Loss para predecir la distancia relativa entre entradas), y métricas como AUC entre otras.
En problemas de ranking también se puede utilizar Pointwise Methods, Pairwise
Methods, Listwise Methods.
En problemas de aprendizaje de representaciones o embeddings y de aprender similaritud relativa entre entradas y problemas basados en la recuperación basada en contenido: objetivo del margen tripleta (Triplet margin loss).
En modelos generativos como las GANs, se pueden usar funciones objetivo de discriminador y generador como funciones básicas objetivo clásicas de min-max loss de GAN, la non saturating GAN loss, y alternativas como la Wasserstein GAN loss, función objetivo de GAN condicional (CGAN), Sharpness Loss, Distancia Cook, u otras https://neptune.ai/blog/gan-loss-functions. Además, en modelos VAE se puede usar
Log Hyperbolic Cosine Loss (LogCosh).
En aprendizaje por refuerzo, las funciones objetivo vendrán dadas por funciones de recompensa adaptadas al problema y entorno a resolver. La elección específica en cada caso se recomienda que se evidencie en la documentación técnica. Se ha de describir en dicha documentación la motivación de la elección de la función objetivo seleccionada, y cómo esta se relaciona con la precisión establecida para la finalidad prevista del sistema.

7.3 Precisión, sesgos e imparcialidad
En este apartado vamos a abordar la relación de la precisión con dos aspectos del sistema de
IA de alto riesgo en particular: sesgos e imparcialidad. El objetivo es, por tanto, establecer las fronteras entre la precisión y el resto de los aspectos aquí tratados para que el proveedor del sistema de IA tenga una visión completa.

40

7.3.1 Sesgos y precisión
La presencia de sesgos puede afectar significativamente a la precisión del sistema. Incluso sin un análisis adecuado de sesgos, una métrica de precisión podría resultar engañosa e inútil.
Por ello es fundamental que, durante el desarrollo, la validación y el establecimiento de las métricas de precisión del sistema de IA, se realice una verificación y mitigación de sesgos en:
los datos, el funcionamiento y las salidas generadas por el sistema de IA.
Se recomienda que se verifiquen los posibles sesgos a evitar, en el diseño, y a verificar y mitigar durante el ciclo de vida de uso del modelo de IA según guía de datos; éstos se detallan en la
ISO en Sesgo ISO/IEC TR 24027:2021, Information technology — Artificial intelligence (AI) —
Bias in AI systems and AI aided decision making, el catálogo de sesgos
(https://catalogofbias.org/) y el catálogo de sesgos ejemplificado [7].
Especialmente en la etapa de diseño, la taxonomía de sesgos cognitivos BIASeD, o equivalente, se recomienda que sea tenida en cuenta metódicamente para considerar y evitar cada sesgo y cada efecto listados en la misma [112].
-

-

Verificación de nociones de imparcialidad. Las métricas de precisión serán fiables si son justas o imparciales (fair), y transmiten la información necesaria para facilitar la transparencia del modelo para llegar a ellas (según la guía transparencia).
Verificación de la explicabilidad del modelo, para así, facilitar los dos puntos anteriores
(ver guía de datos).

Se recomienda evitar una serie de sesgos en los datos, considerando las perspectivas de uso del modelo en el contexto de la IA ética:
-
-
-
-

Sesgo de representación.
Sesgo histórico.
Sesgo de población, de muestreo, de variables omitidas.
Sesgo de máscara (masking bias), interseccional y el sesgo algorítmico [18] entre otros aplicables de relación directa con la finalidad prevista del sistema de IA (ver guía de datos).

Otros sesgos más genéricos podrían también estar presentes según aplicabilidad: el sesgo de selección, de colisionador (collider bias), de información, de exhaustividad (recall), de comprobación (ascertainment), de desgaste o atrición (attrition), de tiempo inmortal, el sesgo de variables de confusión (confounding), de clasificación errónea, o el efecto Hawthorne, entre muchos [8].
Todos estos sesgos se pueden monitorizarse desde la recogida de los datos hasta el fin del ciclo de vida de funcionamiento, especialmente tras la puesta en marcha [62]. Para completar la lista de herramientas y facilitar la aplicación de monitorización de sesgos e imparcialidad, de nuevo aparece una relación clara entre las guías de datos y supervisión humana y la noción y métrica de precisión.
Existen en el ecosistema de imparcialidad para sistemas de IA herramientas que pueden ser utilizadas por el proveedor tanto comerciales como, en gran medida de código abierto. A modo de ejemplo orientativo, las nociones de imparcialidad pueden asegurarse, cuando tenga sentido, de acuerdo con las escalas de riesgo especificadas en la Guía de Riesgos.

41

Por ejemplo, los modelos de predicción de reincidencia de crímenes: deben exhibir equidad de exactitud (accuracy equity) y paridad predictiva (predictive parity) [16]. Por ejemplo, dada la proximidad con el concepto indicado, y la finalidad prevista del sistema de detección de denuncias falsas, el proveedor añade como criterio de precisión añadido al ya seleccionado, cumplir con ambos conceptos.

7.3.2 La imparcialidad para mitigar sesgos
Asumiendo que el preprocesado de los datos se ha hecho de forma adecuada a la finalidad prevista (según guía de datos) y de forma justa para todas las variables (protegidas y no), cuando se haya detectado un sesgo de la guía de datos o noción de imparcialidad que no se satisface, se podrán aplicar técnicas de imparcialidad.
Las métricas de imparcialidad relevantes tienen como objetivo descubrir el posible sesgo en los datos, modelo o el propio diseñador / desarrollador del modelo, que pueda requerir acciones de mitigación. Generalmente, éstas se basan en diferencias, ratios, y evaluaciones de imparcialidad estadística. La ontología de posibles nociones y métricas de imparcialidad para medir tipos de sesgos se divide en las siguientes dos categorías (Fig.2 de [18]):
El cómputo de la precisión del modelo se recomienda que tenga en cuenta adecuadamente las métricas de imparcialidad para minimizar la posible discriminación del modelo hacia grupos de valores pertenecientes a variables sensibles (como minorías por orientación sexual, raza, género o sexo). Según aplicabilidad, las diferentes nociones de imparcialidad se implementarán a través de métricas de ratios, diferencias o test estadísticos según la aplicabilidad de cada métrica. Por ejemplo:
Nociones de imparcialidad de grupo:
-
-
-
-
-
-

Imparcialidad de independencia de clase (paridad estadística, paridad estadística condicional).
Imparcialidad de separación de clase: igualdad de probabilidades (Equalized Odds), igual oportunidad, igualdad predictiva, imparcialidad total.
Imparcialidad de suficiencia de clase (igualdad de exactitud de uso condicional, paridad predictiva, calibración Well).
Imparcialidad total.
Igualdad de tratamiento.
Igualdad de exactitud (accuracy) general.

Nociones de imparcialidad relajada:
-

Nociones de imparcialidad con umbral y basada en evaluaciones estadísticas [18].

7.3.2.1 Taxonomías y métricas de imparcialidad.
Una guía comprensiva debe evaluarse previo uso. Pueden verse en [9], la Fairness Ontology
[18], y en taxonomía de sesgos cognitivos BIASeD [112]. Habrá casos en que no se puedan obtener todos los principios [63], y el compromiso de tal conflicto puede documentarse según la guía de documentación técnica y en la tarjeta del modelo.
42

Técnicas para evaluar y establecer imparcialidad, incluyen, por ejemplo, entre otras técnicas:
-
-

-
-

-

-

Ponderación (reweighting) para mitigar el sesgo en la fase de colección de datos de entrenamiento.
Técnicas para evaluar los nuevos datos transformados, como el balanced accuracy o el average odds difference, para evitar impacto dispar (disparate impact) o resultados que no preservan la igualdad (unequal outcomes) entre variables protegidas [62].
Calcular el Área Bajo las Curvas ROC absoluta para grupos protegidos y no (Absolute
Between-ROC Área, ABROCA) [113]).
Cuando se dude qué métricas de imparcialidad deben evaluarse, se puede aplicar la ontología de imparcialidad [18]. El grupo privilegiado será considerado como aquel que históricamente se observó tener ventaja sistemática, mientras que el grupo no privilegiado representaría aquel con desventaja sistemática en la historia.
Las variaciones de acuerdo con estos grupos y la noción de imparcialidad elegida pueden representarse de forma gráfica para describir visualmente los sesgos en combinaciones estratificadas de atributos protegidos con gráficos de ráfagas de sol
(Plotly sunburst plot). Ver Fig. 6 en [50].
Para la verificación de nociones de imparcialidad, se podrán establecer equivalencias:
por ejemplo la igualdad entre diferentes métricas de la matriz de confusión equivale a la igualdad de oportunidad; tasas iguales de falsos negativos y falsos positivos entre grupos equivale a satisfacer Equality of Odds [50].

7.4 Glosario
Término

Definición

Absolute
Between-ROC
Área, ABROCA

ABROCA mide el valor absoluto del área entre la curva ROC del grupo de referencia y las curvas ROC de uno o más grupos de comparación. De esta forma, ABROCA cuantifica la divergencia entre las curvas ROC de distintos grupos a través de todos los umbrales posibles, agregando esta divergencia sin importar qué subgrupo tiene mejor rendimiento en algún umbral específico. Esto permite evaluar imparcialidad en el rendimiento del modelo para diferentes subgrupos.
Ver desarrollo de la técnica en https://homes.cs.washington.edu/~jpgard/papers/lak19_slicing.pdf

Accuracy

La accuracy, o exactitud, en el contexto de modelos de clasificación es la proporción de predicciones correctas sobre el total de predicciones realizadas. Es una medida de rendimiento que indica qué tan bien el modelo clasifica correctamente las instancias en el conjunto de datos.

Accuracy equity Un sistema de IA muestra equidad en la precisión (accuracy equity) si puede discriminar de igual manera entre la clasificación posible de su espacio de salida para grupos diferentes.
43

Término

Definición

Accuracy macro-media, micro-media y mediaponderada

Un macro-media calculará la métrica de forma independiente para cada clase y, a continuación, sacará la media (por tanto, tratará a todas las clases por igual), mientras que una micro-media agregará las contribuciones de todas las clases para calcular la métrica media. En una clasificación multiclase, es preferible el micro-media si se sospecha que puede haber desequilibrio entre las clases (es decir, si tiene muchos más ejemplos de una clase que de otras).
Por otro lado, para calcular una media ponderada, cada número del conjunto de datos se multiplica por un peso predeterminado antes de realizar el cálculo final.

ANOVA

Analysis of Variance (ANOVA). Fórmula estadística utilizada para comparar las varianzas entre las medias (o promedios) de distintos grupos. Se utiliza para determinar si existe alguna diferencia entre las medias de distintos grupos.
Este cociente muestra la diferencia entre la varianza dentro del grupo y la varianza entre grupos, lo que en última instancia produce una cifra que permite concluir que se apoya o rechaza la hipótesis nula. Si hay una diferencia significativa entre los grupos, no se apoya la hipótesis nula.

Average odds Es la media de la diferencia en las tasas de falsos positivos y verdaderos difference positivos entre los grupos no privilegiados y privilegiados. Un valor de 0 implica que ambos grupos se benefician por igual.
Balanced accuracy

Base model

BIASeD

Está métrica se puede utilizar para analizar la precisión (performance) de un modelo de clasificación. Se calcula sumando la ratio de verdaderos positivos con la ratio de verdaderos negativos y se divide entre dos. Es especialmente útil cuando las clases no están balanceadas. Cuanto más cerca está de 1 este valor, mejor es el modelo para realizar clasificaciones correctas.
Line Son modelos sencillos que funcionan como referencia para el sistema de
IA. Su principal función es contextualizar el resultado de los entrenamientos del modelo de IA. Generalmente estos modelos carecen de complejidad y tiene poco poder predictivo. Sirven de referencia y para establecer comparaciones con el sistema de IA y permiten conocer mejor los datos de trabajo.
Se trata de una categorización o taxonomía de sesgos cognitivos conocidos, desde la perspectiva de los sistemas de IA. Este catálogo y el trabajo de investigación realizado, pretende alinear los sesgos en IA con los propios sesgos del género humano. El estudio completo se puede encontrar en https://arxiv.org/abs/2210.01122

44

Término

Definición

BLEU

BLEU es una métrica utilizada en traducción automática para evaluar la calidad de una traducción generada en comparación con una traducción de referencia. Su cálculo se basa en la coincidencia de n-gramas entre el texto traducido y el texto de referencia, proporcionando una puntuación que refleja la similitud y precisión de la traducción generada.

Central
Limit El teorema del límite central (CLT) afirma que la distribución de una variable muestral se aproxima a una distribución normal (es decir, a una
Theorem
"curva de campana") a medida que aumenta el tamaño de la muestra, suponiendo que todas las muestras son idénticas en tamaño e independientemente de la forma real de la distribución de la población.
Dicho de otro modo, la CLT es una premisa estadística según la cual, dado un tamaño de muestra suficientemente grande de una población con un nivel finito de varianza, la media de todas las variables muestreadas de la misma población será aproximadamente igual a la media de toda la población.
Clasificación
(clasificación binaria, multiclase, multietiqueta

La clasificación binaria implica predecir entre dos posibles categorías o etiquetas. La clasificación multiclase incluye más de dos etiquetas posibles, asignando una sola etiqueta a cada instancia. La clasificación multi-etiqueta permite asignar múltiples etiquetas a cada instancia, lo cual es útil en situaciones donde un mismo ejemplo puede pertenecer a más de una categoría simultáneamente.

Clustering

Como tipo de aprendizaje no supervisado, el clustering es el proceso de ordenar un grupo de objetos de tal manera que los objetos del mismo grupo (que se denomina cluster) sean más similares entre sí que a los objetos de cualquier otro grupo. Existen diferentes tipos de algoritmos de clustering (K-means, MeanShift, DBSCAN etc.).

Coeficiente
Silueta medio

Este es un coeficiente que mide la calidad del agrupamiento, en el que valores más altos indican clusters mejor definidos, tomando valores entre
-1 y +1. La interpretación es la siguiente:
- Valores cercanos a -1 indican un agrupamiento incorrecto.
- Valores cercanos a cero indican clusters traslapados.
- Valores cercanos a +1 indican clusters altamente densos.
Se calcula considerando:
- a: Promedio de la distancia entre una muestra y todos los demás puntos
de la misma clase (cluster)

45
