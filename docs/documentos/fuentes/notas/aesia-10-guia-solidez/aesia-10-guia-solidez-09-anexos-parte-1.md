---
name: aesia-10-guia-solidez-09-anexos-parte-1
description: "AESIA: aesia 10 guia solidez, sección «Anexos (parte 1)» (págs. 43-50). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-10-guia-solidez
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Anexos (parte 1)"
  paginas: 43-50
  origen: 2026-07-17-aesia-10-guia-solidez.pdf
  oficial: false
---
# Anexos (parte 1)

7. Anexos
7.1 Anexo I: Métricas y pruebas para sistemas de IA
7.1.1 Métricas para establecer la solidez
Además de las identificadas en la guía de precisión, se podrán reportar métricas específicas de solidez de los modelos de inteligencia artificial. A modo orientativo se indican las siguientes:
Clasificación multiclase:
-
-
-
-

Coeficiente Kappa de Cohen: Mide el acuerdo entre anotadores, ajustando por la probabilidad de acuerdo aleatorio.
Matriz de confusión y métricas derivadas: Proporciona una visión detallada del rendimiento del modelo, incluyendo verdaderos positivos, falsos positivos, verdaderos negativos y falsos negativos.
Hinge Loss: Utilizada principalmente en máquinas de soporte vectorial, evalúa la pérdida basada en el margen de clasificación.
Coeficiente de correlación de Matthews (MCC): Ofrece una medida equilibrada del rendimiento del modelo, especialmente útil en conjuntos de datos desbalanceados.

Es importante destacar que, en conjuntos de datos desbalanceados, métricas como el Área
Bajo la Curva ROC (AUROC) pueden no ser adecuadas, ya que no reflejan correctamente la proporción de falsos positivos y verdaderos positivos.
Clasificación binaria:
-
-
-

Curva Precisión-Recall: Útil cuando las clases están desbalanceadas, ya que se centra en la capacidad del modelo para identificar correctamente las instancias positivas.
Curva ROC: Muestra la relación entre la tasa de verdaderos positivos y la tasa de falsos positivos a diferentes umbrales.
Exactitud balanceada: Promedia la sensibilidad y la especificidad, proporcionando una medida más equilibrada en casos de clases desbalanceadas.

Clasificación multietiqueta:
-

Puntuación F1: Combina precisión y recall en una sola métrica, siendo especialmente útil cuando se manejan múltiples etiquetas por instancia.

Sistemas de puntuación:
-

Área Bajo la Curva (AUC): Evalúa la capacidad del modelo para distinguir entre clases.
42

-

Lift: Mide la mejora de las predicciones del modelo en comparación con una estrategia aleatoria.

Métodos estadísticos:
-
-
-
-

Error Cuadrático Medio (RMSE): Calcula la raíz cuadrada del promedio de los errores al cuadrado, proporcionando una medida de la magnitud del error.
Error Máximo (MaxError): Indica la mayor diferencia entre los valores predichos y los reales.
Correlación entre valores actuales y predichos: Evalúa la relación lineal entre las predicciones del modelo y los valores reales.
Validación cruzada: Incluye técnicas como K-fold, Group K-fold, Leave-One-Out,
Leave-One-Group-Out y validación cruzada de Monte Carlo, que ayudan a evaluar la generalización del modelo.

Además, para medir la robustez asociada a la precisión del modelo, se pueden utilizar:
-
-
-
-

AUROC: Aunque debe emplearse con precaución en conjuntos de datos desbalanceados. [ISO SC42 N1011]
Curva de Respuesta Acumulativa (CRC) o Curva de Ganancia: Alternativas a la curva ROC cuando el objetivo se centra en una proporción específica de la base de datos. 7
Hamming Loss: Mide la fracción de etiquetas incorrectamente predichas en problemas de clasificación multietiqueta; valores más bajos indican mayor robustez.
Esquemas de validación cruzada 5x2: Proporcionan una evaluación más robusta del rendimiento del modelo.

La selección de métricas debe alinearse con los objetivos específicos del modelo y las características del conjunto de datos, garantizando una evaluación justa y precisa de su rendimiento y robustez.

7.1.2 Métodos de prueba
Los métodos estadísticos confían en procesos de pruebas matemáticas capaces de ilustrar cierto nivel de confianza en los resultados. Permiten a los ingenieros verificar si las propiedades del sistema alcanzan un umbral deseado objetivo. Por ejemplo, ¿Cuántas predicciones producidas son defectuosas o presentan incoherencias?
Para ello se proponen los siguientes métodos de prueba:
- Los métodos formales se basan en pruebas formales firmes, para demostrar una
propiedad matemática sobre un dominio. Los métodos formales incluyen análisis de incertidumbre para probar la estabilidad de la interpolación, usar optimizadores
(solvers, por ej. un optimizador SMT para probar la ausencia o existencia de ejemplos adversarios y la capacidad de exhibirlo), técnicas de optimización (como Branch and
Bound o programación por restricciones -constraint programing) o interpretaciones

43

abstractas para probar una propiedad de espacio estable máximo (Maximum stable space property).
- Los métodos empíricos confían en la experimentación, observación y juicio experto.
para evaluar el punto hasta el que las propiedades del sistema son ciertas en los escenarios testeados. Los ensayos de campo (field trials) que pueden usar estándares de testeo de software (por ej. ISO/IEC/IEEE 29119-3:2021, donde se indica el riesgo residual con relación a lo evaluado por las pruebas para poder encontrar defectos en el elemento testeado), testeado a posteriori (con evaluación entrada-salida, o validación por testeo).
Realizar pruebas de perturbación de las entradas, para consolidar la solidez del sistema, es un mecanismo de prueba que permite evaluar el comportamiento del sistema de IA en condiciones de producción, donde las entradas son menos controladas. A continuación, mostramos tres ejemplos de perturbaciones según los tipos de sistemas de IA:
- Para evaluar la solidez de un modelo contra una perturbación específica (por
ejemplo, presencia de gotas de líquido causantes de defectos de imagen en lentes)
usando un método formal debemos tener una función describiendo el proceso de aplicación de la perturbación que se base en un parámetro limitado que puede ser variado para presentar variaciones aceptables de perturbación, y es preferible tener una composición conmutativa de funciones. Otras perturbaciones podrían ser vibración, rotación, brillo, turbulencias atmosféricas, ruido homogéneo, borrosidad, sobreexposición (blooming bright spots) o manchas (smear).
- En datos de sonido, se pueden estudiar los rangos de frecuencia audibles por
humanos o no (como las perturbaciones basadas en ultrasonidos).
- En aprendizaje por refuerzo (RL) se puede: aplicar fuerzas disturbantes al agente hace
el agente más sólido, influenciar a un agente para que tome siempre la peor acción posible puede verse como un ataque que conlleva a una mejor solidez del agente entrenado en entornos con propiedades físicas diferentes. Reducir la precisión o eficiencia de un agente es también posible incluso si el adversario es solo parte del entorno de la víctima y, por tanto, parte de sus observaciones. Un ejemplo de técnica en este caso es entrenamiento de liga (league training) [81].

7.1.2.1 Métodos formales
Los métodos formales son técnicas matemáticas para la especificación rigurosa y verificación de sistemas de software y hardware que tienen como objetivo probar la corrección del sistema. Los métodos formales permiten hacer corresponder el sistema de
IA en relación con la finalidad prevista con un modelo matemático. Pueden complementar a otros métodos e incrementar la confianza en la solidez de los modelos, razonar sobre estos y demostrar si satisfacen las propiedades de solidez relevantes (ver apartado 2.1
Propiedades asociadas a la solidez).
Generalmente, establecen un enlace en el modelo (por ej. red neuronal) a través de las entradas a las salidas sobre un dominio, que permite saber cuánto impacta cada entrada a cada salida. Hay diversos tipos de métodos formales. Generalmente se distingue entre:

44

- Completos (proveen respuestas exactas) e incompletos. Los últimos pueden resultar
más realistas para su aplicación a la verificación de redes neuronales que consiguen alta precisión en tareas de datos complejas, pues usan técnicas de abstracción que escalan a éstas. Sin embargo, pueden fracasar en demostrar una propiedad de solidez que en realidad se satisface.
- Deterministas o no. Los últimos pueden verificar modelos como mixture density
networks o autoencoders variacionales que no producen una salida determinista sino una distribución. Para demostrar garantías formales de su solidez con alta probabilidad, los métodos no deterministas pueden establecer los parámetros de esta distribución de salida determinísticamente.
- De caja blanca (conscientes) o de caja negra (agnósticos al modelo). Los verificadores
de caja blanca requieren acceso a la representación interna de la red, su arquitectura y parámetros aprendidos, pero no a los datos de entrenamiento ni al algoritmo usado para entrenar la red neuronal. Los verificadores de caja negra pueden ser usados cuando el modelo está encriptado y no es accesible. Sin embargo, requieren la capacidad de ejecutar el modelo para entradas concretas, lo cual puede hacerlos menos precisos que los de caja blanca.
- Aritmética de computador o real. Aunque en muchos casos no es así, los
verificadores pueden tener en cuenta los errores de redondeo hechos con la aritmética de computador y razonar, bajo la semántica establecida para esa aritmética concreta, sobre las salidas de una red neuronal6.

7.1.2.2 Métodos formales y su aplicabilidad para verificar la solidez de sistemas de
IA basados en redes neuronales artificiales
La aplicación de métodos formales, como mecanismo de verificación de la solidez, permiten, en las redes neuronales establecer dos propiedades formales de la solidez de un sistema:
- La estabilidad de la interpolación calcula la incertidumbre de una red neuronal como
una manera de detectar cuando la red tendrá capacidad de interpolación insuficiente y, por tanto, insuficiente solidez.
- Un espacio estable máximo (Maximum stable space): calcula el tamaño del dominio
donde la red neuronal tendrá una predicción de clasificación estable. Los métodos formales pueden dividirse según al tipo de modelo al que se aplican:
o Métodos de verificación de redes neuronales lineales por partes (Piecewise linear neural networks -PLNN): Se puede verificar la solidez de estas redes neuronales con optimizadores satisfiability modulo theories (SMT) solver, con programación lineal en enteros mixta (PLEM, o mixed integer linear program, MILP) u otros reflejados en ISO /IEC DTR 24029:2021 como FastLin – Fast-Lip, CROWN y formal safety analysis.

6

Para evitar que las garantías de solidez no se cumplan para los cómputos realmente hechos con aritmética en coma flotante u otras, los verificadores formales consideran la semántica del tipo de aritmética de cómputo, estándar o no, y garantizan que la salida captura las salidas posibles de la red bajo esa semántica. Solamente cuando los operadores redondean correctamente según lo establecido en el estándar IEEE 754, los verificadores pueden tener en cuenta cambios en el orden de los cómputos y pueden aproximar el redondeo hecho en cada operador.

45

o

o

o

Métodos para verificar redes neuronales binarizadas (binarized neural nets,
BNNs): Crean una representación exacta de la BNN con fórmulas booleanas tal que todos los pares válidos de entrada y salida sean soluciones de esta fórmula, y la verificación se consigue usando satisfacibilidad booleana,
Integer Linear Programming, ILP).
Métodos de verificación a través de optimizadores (solvers): MILP, SMT
(Satisfiability Modulo Theories): Todos son determinísticos y de caja blanca.
Codifican todo cómputo de una red neuronal como una restricción y, dependiendo de la arquitectura, pueden ser verificadores completos o incompletos7. Si los elementos en los límites de la restricción de solidez satisfacen las restricciones, la propiedad queda demostrada.
Verificadores de Interpretación Abstracta. Marcos para el análisis escalable de sistemas probabilísticos y determinísticos grandes y complejos que, en el contexto de redes neuronales, proveen un método de caja blanca determinista, incompleto que puede verificar la solidez de arquitecturas grandes a través de la abstracción de las entradas del modelo por medio de formas geométricas, cajas, zonotopos, poliedros u otros, por lo que hay un compromiso inherente entre precisión y escalabilidad. Por ejemplo, usando cajas para acotar las entradas escala a millones de neuronas por segundo, pero es impreciso para verificar propiedades de solidez; mientras que las relajaciones semidefinidas son más precisas, pero no escalan a arquitecturas grandes.

7.1.2.3 Métodos para verificar formalmente la solidez de otros modelos particulares de redes neuronales
Los modelos de tipo transformers, se pueden verificar descomponiendo capas en subcapas donde se calculan límites que actúan de garantía desde la primera subcapa (de transformaciones lineales, funciones no lineales y operaciones de self-attention) a la última
[99]. Verificando y validando la solidez por tanto en cada una de las etapas establecidas.
Para el caso de redes recurrentes (RNNs), éstas se pueden considerar como máquinas de estados infinitos o autómatas de estados finitos, por lo que se puede medir la solidez local de las RNNs para clasificación con model checking y abstract interpretation. Abstract interpretation es un marco para el análisis escalable de sistemas deterministas de gran escala, complejos y probabilísticos que proporciona un método incompleto, determinista y de caja blanca que puede verificar la solidez de grandes redes neuronales.
En sistemas de IA basados en aprendizaje por refuerzo (RL): La estabilidad y solidez debe ser considerada a la hora de documentar la solidez de los sistemas, haciendo pruebas tanto en simulación como en el mundo real [68], y usando métricas adaptadas a la tarea y contexto [69, 105].

7

Por ej. funciones de activación hiperbólicas como la sigmoide y tanh son demasiado complejas para codificarlas precisamente, por lo que los optimizadores las aproximan con abstracciones formales.

46

Para otros tipos de datos como las redes neuronales basadas en grafos requerirán métodos específicos especializados8.

7.2 Anexo II: Solidez e incertidumbre
En este Anexo presentamos la relación existente entre la incertidumbre y la solidez para el sistema de IA. Se recomienda que el proveedor considere este anexo en relación con la evaluación de la solidez, como detalle y extensión de las medidas indicadas en el apartado
4.

7.2.1 La solidez como capacidad de tratamiento y minimización de la incertidumbre
La fiabilidad de la precisión y solidez reportada para un modelo de IA depende de la fiabilidad de los datos y la estimación de los factores que generan los datos, su hipótesis en relación con la finalidad prevista, etc. [1]. Sí los datos se degradan (cuando los datos que procesa ya no siguen la distribución de los datos usados cuando se entrenó), el modelo también lo hará. (ver Guía de Datos).
Una representación fiable de la incertidumbre de un modelo es clave para cualquier modelo de IA. Al menos, hay dos tipos principales de incertidumbre asociados a un modelo predictivo: 1) Aleatoria, y 2) Epistémica. La aleatoria no es reducible, pues se debe a la inherente naturaleza estocástica de la dependencia entre instancias x y salidas y. La epistémica es reducible por el modelo: podría eliminarla recogiendo más datos para los conjuntos de trabajo [1].
Se recomienda que el proveedor provea infraestructura para monitorizar y notificar, durante todo el ciclo de vida del sistema de IA, de potenciales:
1. Cambios en la distribución de datos de entrenamiento y test (shift del conjunto de datos);
2. Disparidades en cuanto al cambio del dominio o tarea de aprendizaje automático requiriendo el ajuste al nuevo dominio de datos por medio de fine-tuning con congelación de pesos en redes neuronales, o con procesos de transferencia de aprendizaje (transfer learning).
3. Cambios en el mecanismo de adquisición de nuevos datos, involucrando, por ejemplo, la introducción de artefactos no deseados, datos que incluyen indicadores que pueden introducir un sesgo indirectamente, o un simple desequilibrio de estos.
4. Olvido catastrófico y la incapacidad de aprender de manera continua [25].
En cuanto a medidas técnicas, detallamos en las secciones siguientes, diferentes medidas para tratar diferentes dimensiones que conducen a la solidez de un sistema de IA.

8

Por ejemplo, cuando se tengan datos tabulares que combinan datos de varios tipos (numéricos, simbólicos, textuales) y expresen relaciones entre ellos, esto puede impedir el uso de métodos formales debido a la gran cantidad de filas y a la dificultad de estimar la varianza dentro de cada fila.

47

7.2.2 Métodos para medir y cuantificar la incertidumbre de la salida de un modelo de IA
A modo orientativo se señalan varias técnicas para cuantificar la incertidumbre asociada a un modelo:
- Calibrar los modelos de clasificación (con regresión isotónica o Sigmoid / Platt
scaling), es decir usar una técnica de post-procesamiento con el fin de mejorar la estimación de la probabilidad o mejorar el error de la distribución.
- Evaluar la incertidumbre indirectamente (evaluando su utilidad para una predicción
mejorada y toma de decisiones), por ejemplo, con curvas (accuracy-rejection curves)
u otras estrategias [1].
- Usando otras medidas de calibración: Macro-average accuracy, proportion of
classes, MSE, LogLoss, CalBin, CalLoss, Avg error, relative error, Anderson-Darlin
(A2) test [2].
Herramientas de estimación y monitoreo (ver guía de Supervisión Humana) de la degradación de la precisión y solidez del modelo a través de la incertidumbre asociada a la misma:
- IBM Uncertainty Quantification 360 Toolkit (para estimar, comunicar y usar la
incertidumbre en modelos predictivos y así mejorar tanto la precisión como la solidez del modelo).
- NannyML (para estimar la incertidumbre de modelos tras la puesta en producción del
modelo, antes y después de que los datos de salida objetivo dejen de estar disponibles, detecta data y model drift que posiblemente lo causan).

7.3 Glosario
Término

Abstract interpretation

Definición
Es una técnica que simplifica el análisis de programas al crear representaciones abstractas que capturan propiedades esenciales.
Ayuda a comprender y razonar sobre el comportamiento de los programas sin necesidad de ejecutarlos realmente, lo que facilita la detección de errores y la optimización en la inteligencia artificial.

48

Término

Definición
La Prueba de Anderson-Darling es una prueba estadística utilizada para determinar si un conjunto de datos sigue una distribución específica. Se utiliza para evaluar si los datos se ajustan a una distribución teórica, como la distribución normal, exponencial o uniforme.

La prueba se basa en la comparación de los valores observados con los valores esperados bajo la distribución teórica. Calcula una medida de ajuste llamada estadística de Anderson-Darling, que
Anderson-Darling (A2)
tiene en cuenta las diferencias entre los valores observados y test esperados, dando más peso a las desviaciones en las colas de la distribución.
La hipótesis nula de la prueba es que los datos siguen la distribución teórica, mientras que la hipótesis alternativa es que los datos no se ajustan a la distribución teórica. Si el valor de la estadística de Anderson-Darling es mayor que un valor crítico dado, se rechaza la hipótesis nula y se concluye que los datos no siguen la distribución teórica.

Aprendizaje privilegiado destilado

Es una técnica de aprendizaje automático que utiliza información adicional o conocimiento privilegiado disponible durante la etapa de entrenamiento para mejorar el rendimiento del modelo final. Se entrena un modelo secundario para aprender a predecir esta información privilegiada y se utiliza para enseñar al modelo base a aprovecharla y mejorar sus predicciones.

AUROC

El AUROC es una métrica que resume la calidad de la curva ROC y proporciona una medida cuantitativa del rendimiento del modelo.
Cuanto mayor sea el valor del AUROC, mejor será el rendimiento del modelo.

Autoencoders variacionales

Son modelos de aprendizaje automático que generan representaciones latentes siguiendo una distribución específica.
Estos modelos permiten reconstruir los datos originales y también generar nuevos datos similares a los originales. Son útiles en tareas de generación de datos y otras aplicaciones donde se requiere la captura de la incertidumbre asociada con la generación de datos.

49
