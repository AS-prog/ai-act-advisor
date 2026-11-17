---
name: aesia-11-guia-ciberseguridad-12-anexos-parte-2
description: "AESIA: aesia 11 guia ciberseguridad, sección «Anexos (parte 2)» (págs. 62-67). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-11-guia-ciberseguridad
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Anexos (parte 2)"
  paginas: 62-67
  origen: 2026-07-17-aesia-11-guia-ciberseguridad.pdf
  oficial: false
---
# Anexos (parte 2)

sensibilización, vulnerabilidades de los sistemas de IA, envenenamiento, ataques adversarios…
El personal que interactúa con el sistema de IA y que es encargado de trabajar con este se recomienda que reciba una formación específica en ataques adversarios para el sistema de IA y su finalidad prevista.
Acorde a los formatos de comercialización, si la configuración o la administración del sistema de IA se realiza por personal del responsable del despliegue (administración de sistemas propia, por ejemplo) la formación podrá incluir:
- Explotación de defectos del modelo. Definición de ataques por transferencia. ¿Qué
son los defectos intrínsecos del modelo? Configuración e integración segura.
La formación se recomienda que sea periódica y se actualice acorde a los cambios y actualizaciones que proporcione el proveedor.

7.3 Glosario orientativo
Término

Definición

Ataque
Adversario

Los ataques que se realizan contra un sistema de inteligencia artificial, se consideran ataques adversarios. En relación con el nivel de conocimiento que el atacante los ataques adversarios puede ser:
- Caja Blanca: Acceso la arquitectura del modelo, datos de
entrenamiento, parámetros e hiper parámetros.
Caja
Negra:
entradas y salidas.
Caja gris:
una mezcla de ambas.
En relación con el modo de operación los ataques pueden ser (consultar en detalle las definiciones en el glosario):
Envenenamiento.
- Evasión, que en ocasiones se consideran directamente de manera
genérica los ataques adversarios, aunque realmente se trata de un tipo específico de los mismos.
Extracción.
- Inversión.

Ataque
Evasión

Un tipo de ataque que se producen durante la fase de inferencia con el sistema de IA en producción. El atacante no tiene acceso a los datos de entrenamiento, solo se comunica con el sistema vía interfaz (física, visual o tipo API). En general este tipo de ataques busca que una predicción del modelo sea errónea.

61

Término

Definición

Ataque
Extracción

Tipo de ataque durante la fase de inferencia con el sistema de IA en producción. Sin acceso a los datos de entrenamiento, solo se comunica con el sistema vía interfaz (física, visual o tipo API). El atacante mediante el acceso al modelo proporciona inputs a éste, y registras los outputs, para inferir una réplica total o parcial del modelo a través de sus respuestas.

Ataque
Inversión

Es un tipo de ataque que se produce durante la fase inferencia con el sistema de IA en producción. En estos ataques el usuario no tiene acceso directo a los datos, pero si puede tener acceso al modelo a través de su interfaz (ya sea esta física, visual o tipo API). Los ataques de inversión como objetivo la obtención de conocimiento de los datos del modelo.
Como se ha indicado en la guía pueden ser:
-

Membership Inference Attack para conocer si una muestra pertenece a los datos de entrenamiento.
- Property Inference Attack, que busca conocer los datos
utilizados por el modelo durante en el entrenamiento para realizar las predicciones.
- Existe un tercer tipo que es reconstrucción, que es más
complicado de ejecutar, porque su intención es reconstruir todos los datos de entrada.

AttributionEste concepto se relaciona con que existe una conexión entre la
Driven Causal resistencia a las perturbaciones adversariales y la explicación basada en
Analysis la atribución de las decisiones individuales generadas por los modelos de aprendizaje automático. Las entradas adversariales no son robustas en el espacio de atribución, es decir, el enmascaramiento de unos pocos rasgos con alta atribución lleva a cambiar la indecisión del modelo de aprendizaje automático en los ejemplos adversariales. En cambio, las entradas naturales son robustas en el espacio de atribución. El concepto ha sido desarrollado en un artículo, que puede ser encontrado aquí https://arxiv.org/abs/1903.05821
Bagging

Utilización de modelos entrenados en paralelo para constituir el sistema de inteligencia artificial. El objetivo es aprovechar la independencia entre los modelos entrenados de manera separada sobre diferentes subconjuntos del conjunto original de datos de entrenamiento (con la misma finalidad prevista para el sistema) para promediar su salida. Este tipo de técnica es un mecanismo de protección frente a envenenamiento de datos. También es una técnica eficiente frente a los ataques de evasión, al no depender de un único modelo que pueda ser vulnerable al ataque considerado. Para clasificaciones, los diferentes modelos entrenados realizan una votación de la pertenencia a una clase,

62

Término

Definición para aquellas operaciones que no realizan una clasificación
(regresiones, estimaciones etc.) se realiza una media aritmética. En ocasiones aparece también como Bootstrap Aggregation.

Boosting

El refuerzo es una técnica de conjunto que busca cambiar los datos de entrenamiento y ajustar el peso de las observaciones en función de la clasificación anterior. A diferencia del enfoque bagging, el boosting implica la dependencia de modelos débiles. Los aprendices débiles tienen en cuenta los resultados del modelo débil anterior y ajustan los pesos de los puntos de datos, convirtiéndolo en un modelo fuerte. El
Boosting cambia el peso asociado a una observación que fue clasificada incorrectamente tratando de aumentar el peso asociado a ella. El refuerzo tiende a disminuir el error de sesgo, pero a veces puede llevar a un sobreajuste del conjunto de datos de entrenamiento.

CAT-Gen

Al desarrollar modelos de NLP podremos realizar diferentes tareas de manera automática como traducir textos, resumirlos, etc. El problema de este tipo de modelos es que son muy poco robustos frente a pequeñas modificaciones en los datos de entrada. Sin embargo, en la utilización de esta técnica demuestra como al introducir el aprendizaje adversario, en este tipo de modelos, la robustez frente a cambios en los datos de entrada mejora notablemente
Este método puede generar textos adversarios más diversos y fluidos.
La utilización de estos textos adversarios permite mejorar los modelos mediante el entrenamiento adversario.
El desarrollo de la técnica está detallado por los autores se puede encontrar en https://arxiv.org/abs/2010.02338

CVE

Common Vulnerabilities and Exposures (CVE) es una lista de vulnerabilidades y exposiciones de seguridad de la información divulgadas públicamente.
Existe una lista accesible en https://www.cve.org/

CWE

Common Weakness Enumeration (CWE) es un sistema de categorías para las debilidades y vulnerabilidades del software. Se puede consultar en https://cwe.mitre.org/

Defensive
Distillation

La destilación defensiva es una técnica de entrenamiento adversarial que añade flexibilidad al proceso de clasificación de un algoritmo para que el modelo sea menos susceptible de ser explotado. En el entrenamiento de destilación, un modelo se entrena para predecir las

63

Término

Definición probabilidades de salida de otro modelo que fue entrenado en un estándar de referencia anterior para enfatizar la precisión.
El primer modelo se entrena con etiquetas "duras" para lograr la máxima precisión, por ejemplo, exigiendo un umbral de probabilidad del 100%.
Si un atacante aprende qué características y parámetros busca el sistema, puede enviar unos datos de entrada sólo con las características relevantes, lo que genera una coincidencia falsa positiva.
El primer modelo proporciona entonces etiquetas "blandas" con una probabilidad del 95%. Esta incertidumbre se utiliza para entrenar al segundo modelo para que actúe como un filtro adicional. Como ahora hay un elemento de aleatoriedad para conseguir una coincidencia perfecta, el segundo algoritmo o "destilado" es mucho más robusto y puede detectar más fácilmente los intentos de suplantación.

DLP
(herramientas
)

Son herramientas destinadas a evitar la pérdida de datos. Su relación con la ciberseguridad para inteligencia artificial viene dictada por la necesidad de control, estabilidad y seguimiento de los conjuntos de datos de entrenamiento. De esta manera el control que establecen estas herramientas permite añadir un control de seguridad sobre los ataques de envenenamiento de datos. Existen varias herramientas de mercado y soluciones opensource.

Envenenamie nto
(poisoning)

El envenenamiento es un tipo de ataque, en la fase de diseño y entrenamiento, que trata de manipular el conjunto de datos de entrenamiento, con el objetivo de controlar las predicciones del sistema de inteligencia artificial de tal manera que el modelo transforme, en la fase de inferencia una vez desplegado en producción, entradas maliciosas en resultados correctos.

Feature
Denoising

Este concepto se basa en que las perturbaciones adversariales realizadas en imágenes provocan ruido en las características construidas por las redes neuronales. Se trata de una arquitectura que incremente la resistencia a ataques adversarios realizando una eliminación de ruido en las características. Esta arquitectura ha sido propuesta en un artículo que puede ser encontrado en https://arxiv.org/abs/1812.03411

Feature
Squeezing

Esta técnica puede utilizarse para proteger los modelos mediante la detección de ejemplos adversos. En la reducción (squeezing) de características disminuye el espacio de búsqueda disponible para un adversario al fusionar muestras que corresponden a muchos vectores de características diferentes en el espacio original en una sola muestra.

64

Término

Definición
Al comparar la predicción de un modelo DNN sobre la entrada original con la de la entrada comprimida, esta técnica detecta los ejemplos adversarios con gran precisión y pocos falsos positivos. Si los ejemplos originales y comprimidos producen resultados sustancialmente diferentes del modelo, es probable que la entrada sea adversa. Los autores de esta técnica han publicado sus resultados en https://evademl.org/squeezing/

GPAI (general De acuerdo con Reglamento Europeo de Inteligencia Artificial, en el purpose AI)
Artículo 3 Definiciones (1b):
"un sistema de IA que -independientemente de cómo se comercialice o se ponga en servicio, incluso como software de código abierto- está destinado por el proveedor a realizar funciones de aplicación general, como el reconocimiento de imágenes y del habla, la generación de audio y vídeo, la detección de patrones, la respuesta a preguntas, la traducción y otras; un sistema de IA de propósito general puede utilizarse en una pluralidad de contextos e integrarse en una pluralidad de otros sistemas de IA".
Dado que la utilización de este tipo de sistemas en el desarrollo de un sistema de inteligencia artificial, puede ser posible, cabe aclarar aquí, y añadido a la definición indicada un extracto del considerando 12c siguiente:
"[...] los proveedores de sistemas de inteligencia artificial de propósito general, independientemente de que puedan ser utilizados como sistemas de inteligencia artificial de alto riesgo como tales por otros proveedores o como componentes de sistemas de inteligencia artificial de alto riesgo, deben cooperar, según proceda, con los proveedores finales de los respectivos sistemas de inteligencia artificial de alto riesgo para permitir su cumplimiento de las obligaciones pertinentes en virtud del presente Reglamento y con las autoridades competentes establecidas en virtud del mismo".
Highly
Confident
Near
Neighbor
(HCNN)

Se trata de un framework de trabajo en redes neuronales que combina la información de confianza y la búsqueda del vecino más cercano, para reforzar la robustez adversarial de un modelo base. Esto puede ayudar a distinguir entre las predicciones correctas y erróneas del modelo en una vecindad de un punto muestreado de la distribución de entrenamiento utilizada. La técnica está desarrollada en un artículo al que se puede acceder en el siguiente enlace https://arxiv.org/abs/1711.08001

65

Término

Definición

Input gradient regularisation

Consiste en imponer restricciones al gradiente de entrada, o regularización. La técnica de regularización en general consiste en restringir las estimaciones de los coeficientes a cero. Esta técnica permite evitar un overfitting sobre el conjunto de entrenamiento, y fundamentalmente es una técnica utilizada para proporcionar resistencia a los ataques adversarios, o a la mitigación de estos. La regularización en el gradiente de entrada evita que este sea demasiado grande, lo que hace que las redes neuronales sean vulnerables a los ataques adversarios.

Isolation
Forest

Este método, se basa en el algoritmo del árbol de decisión. Aísla los valores atípicos seleccionando aleatoriamente una característica del conjunto de características dado y, a continuación, seleccionando aleatoriamente un valor de división entre los valores máximo y mínimo de esa característica. Esta partición aleatoria de las características producirá recorridos más cortos en los árboles para los puntos de datos anómalos, distinguiéndolos así del resto de los datos. Este algoritmo se basa en el principio de que las anomalías son observaciones que son pocas y diferentes, lo que debería facilitar su identificación. Isolation
Forest utiliza un conjunto de árboles de aislamiento para los puntos de datos dados para aislar las anomalías.
De esta manera tanto los outliers presentes en el set de datos, como aquellos que puedan haber sido introducidos para generar un envenenamiento pueden ser detectados y mitigado el impacto

Label
Flipping

Se trata de un tipo de ataque que, para datos capturados de fuentes no seguras, y en los que no es posible obtener los datos de otra manera, existe el riesgo de que un atacante haya podido alterar el etiquetado de los datos en una parte del conjunto de datos de entrenamiento.
Aplicado a sistemas de alto riesgo, es importante considerar que debería tenerse en cuenta este concepto, incluso como ocurrido de manera natural o no malintencionada pero que el cualquier caso pudiera afectar al rendimiento del sistema. En ese escenario se deben aplicar técnicas para detectar el Re etiquetado de datos para mitigar este efecto.
Tal y como se describe en, https://www.researchgate.net/publication/323550082_Label_Sanitizati on_against_Label_Flipping_Poisoning_Attacks, el procedimiento utiliza k-NN para asignar la etiqueta a cada instancia del conjunto de entrenamiento. El objetivo es reforzar la homogeneidad de la etiqueta entre las instancias que están cerca, especialmente en las regiones que están lejos del límite de decisión

66
