---
name: aesia-11-guia-ciberseguridad-13-referencias-estandares-y-normas
description: "AESIA: aesia 11 guia ciberseguridad, sección «Referencias, estándares y normas» (págs. 68-77). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-11-guia-ciberseguridad
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Referencias, estándares y normas"
  paginas: 68-77
  origen: 2026-07-17-aesia-11-guia-ciberseguridad.pdf
  oficial: false
---
# Referencias, estándares y normas

Término

Definición

Local Outlier Es un método que permite tanto detectar outlier naturales, es decir que
Factor puedan estar presentes de manera natural en una muestra (dada la medición, errores de almacenamiento etc.) como aquellos que pueden haberse insertado como intención de un ataque de envenenamiento. Se trata un método de detección de anomalías no supervisado que calcula la desviación de la densidad local de un punto de datos dado con respecto a sus vecinos. Considera como valores atípicos las muestras que tienen una densidad sustancialmente inferior a la de sus vecinos.
MITRE ATLAS Es una fuente de información de estado del arte de técnicas de ataque
(herramientas adversario, basada en sistemas que se encuentran en producción. Es
/fuentes)
una fuente de información muy relevante, que debe ser consultada tanto en fase de diseño, como desarrollo. Durante la fase de inferencia, el sistema podrá requerir actualizaciones en relación con casos de uso encontrados en otros sistemas que permitan ataques de transferencia.
Toda la información es accesible a través de la dirección https://atlas.mitre.org/
Model stacking

Stacking es un algoritmo de aprendizaje automático conjunto que combina de la mejor manera posible las predicciones de múltiples modelos de aprendizaje automático de buen rendimiento.
La ventaja de esta técnica es que puede aprovechar las capacidades de una serie de modelos de buen rendimiento en una tarea de clasificación o regresión y hacer predicciones que tienen mejor rendimiento que cualquier modelo individual del conjunto.
El siguiente enlace proporciona un ejemplo de cómo aplicar la técnica usando
Python https://machinelearningmastery.com/stackingensemble-for-deep-learning-neural-networks/

Neural
Dropout

El dropout es un método de regularización que aproxima el entrenamiento de un gran número de redes neuronales con diferentes arquitecturas en paralelo.
Durante el entrenamiento, un cierto número de salidas de las capas se ignoran o se "descartan" aleatoriamente. Esto tiene el efecto de hacer que la capa parezca y sea tratada como una capa con un número diferente de nodos y conectividad a la capa anterior. En efecto, cada actualización de una capa durante el entrenamiento se realiza con una
"vista" diferente de la capa configurada.
Esta técnica se implementa por capa en una red neuronal. Puede utilizarse con la mayoría de los tipos de capas, como las capas densas

67

Término

Definición totalmente conectadas, las capas convolucionales y las capas recurrentes, como la capa de red de memoria a corto plazo.
(ver https://arxiv.org/pdf/1806.01246v2.pdf)

OoD
Data Se trata de datos de entrada, recibidos por el sistema en fase de
(Out of inferencia una vez puesto el sistema de IA en producción, que no se
Domain Data) encuentran dentro del dominio establecido de entrenamiento y relacionado con la finalidad prevista del sistema. Se trata de un indicador de posible ataque adversarial, y pertenece a las técnicas de control de los parámetros de entrada. En el caso de datos estructurados y tabulados, o datos numéricos, series discretas etc., es relativamente sencillo detectar aquellos valores que no se encuentran dentro del dominio y restringir o prohibir su entrada al sistema de inteligencia artificial. En lo referente a sistemas basados en procesamiento del lenguaje natural, es especialmente importante detectar aquellos elementos que no son parte del dominio
(ver https://arxiv.org/pdf/1909.03862.pdf).
Privacidad
Diferencial

La privacidad diferencial busca proteger los valores de los datos personales mediante la incorporación de "ruido" estadístico al proceso de análisis. Los cálculos necesarios para formar ruido son complejos, pero el principio es bastante intuitivo: el ruido garantiza que las agregaciones de datos permanezcan estadísticamente coherentes con los valores de datos reales, lo que permite una variación aleatoria, pero dificulta trabajar con los valores individuales de los datos agregados.
Además, el ruido es diferente para cada análisis, por lo que los resultados son no deterministas; en otras palabras, dos análisis que realizan la misma agregación pueden generar resultados ligeramente diferentes.
https://becominghuman.ai/what-is-differential-privacy-1fd7bf507049 https://learn.microsoft.com/es-es/training/modules/exploredifferential-privacy/2-understand-differential-privacy

68

Término

Definición

RONI

La premisa de este tipo de mitigación en los ataques se centra en realizar una simulación del efecto de la inclusión de los datos de entrada de entrenamiento, antes de que estos se incorporen al proceso. Para ello el dato se rechaza en el caso de que su impacto sobre el modelo sea negativo (Reject On Negative Impact) RONI. Este tipo de defensas es especialmente interesante si el sistema tiene una fase de aprendizaje paralela a la inferencia con el sistema en producción, o si la fuente de datos de entrenamiento es muy extensa y difícil de controlar su estado
(por ejemplo, textos de email) y por tanto evitar que sean candidatos para envenenar el modelo.
Establece un umbral observando el impacto negativo medio de cada instancia en el conjunto de entrenamiento y marca una instancia cuando su impacto en el rendimiento supera el umbral. Se puede encontrar un trabajo detallando el proceso en https://people.eecs.berkeley.edu/~tygar/papers/SML/misleading.learn ers.pdf

STRIP

La técnica STRIP está destinada a poder mitigar los ataques de envenenamiento de datos que generan, o permiten la creación de una puerta trasera en una red neuronal profunda. Generalmente estos ataques disponen de un disparador en los datos que permite activar la respuesta del modelo con los que se ha envenenado éste y generar una clasificación errónea. STRIP es la abreviatura de STRong Intentional
Perturbation, esta técnica para detectar estas respuestas y está enfocada en sistemas de visión artificial. La técnica ha sido desarrollada en el siguiente paper que puede encontrase aquí https://arxiv.org/abs/1902.06531

Transferencia Esta vulnerabilidad representa la exposición del sistema de inteligencia de ataques artificial a recibir ataques adversarios para otros sistemas, dada la adversarios similitud que pueda tener con estos estos. Este tipo de ataque se puede realizar una vez que se ha identificado en mayor o menor medida el sistema atacado y puedan utilizarse ataques conocidos para el tipo o familia de modelo.
TRIM

Se trata de una técnica que, especialmente para aplicable al caso de regresiones. El método TRIM estima los parámetros de regresión de forma iterativa, utilizando una función de pérdida recortada (trimmed loss function) para eliminar los puntos con grandes residuos. Tras unas pocas iteraciones TRIM es capaz de aislar la mayoría de los puntos de envenenamiento y aprender un modelo de regresión robusto. Un mayor detalle se puede encontrar en

69

Término

Definición https://www.researchgate.net/figure/Several-iterations-of-the-TRIMalgorithm-Initial-poisoned-data-is-in-blue-in-top-left_fig2_324166859

tRONI

Si el ataque al que estamos expuestos es está dirigido, las instancias de datos envenenadas puede que no causen una caída significativa en el rendimiento. Esta variante aprovecha el conocimiento previo sobre una clasificación errónea en tiempo de prueba para determinar que instancias de entrenamiento podrían haberla causado. Mientras que
RONI estima el impacto negativo de una instancia en su conjunto, tRONI considera su efecto exclusivamente en la clasificación del objetivo. Los procedimientos aplicables para la realización de esta técnica se pueden encontrar en https://arxiv.org/pdf/1803.06975.pdf

Z-score

Es una técnica de normalización de los datos, o aplicado en la terminología de Inteligencia Artificial, se trata de un escalado de las características. En esta técnica, los valores se normalizan en función de la media y la desviación estándar de los datos. La esencia de esta técnica es la transformación de los datos mediante la conversión de los valores a una escala común en la que la media es igual a cero y la desviación estándar es uno.

70

8. Referencias, estándares y normas
Para la elaboración de la guía de ciberseguridad se ha utilizado diversas fuentes consultadas. Se recomienda especialmente a los proveedores y responsable del despliegue la lectura de dos informes elaborados por la Agencia Europea para la
Ciberseguridad, ENISA (European Union Agency for Cibersecurity) por sus siglas en inglés.
Dicha agencia europea, elabora documentos relevantes en el ámbito de la ciberseguridad y sin duda será un actor destacado en los aspectos de ciberseguridad en IA relacionados con el Reglamento Europeo

8.1 Estándares
Los siguientes estándares han sido consultados para reflejar en algunos casos los aspectos intermedios entre aspectos de seguridad genérica y aquellos específicos de IA. Se ha indicado en los puntos de la guía aquellas recomendaciones que podrían ser de aplicación.
- ISO/IEC 27001 Information technology — Security techniques — Information security

management systems — Requirements
- NIST 800-53 Security and Privacy Controls for Information Systems and

Organizations
- NISTIR 8269, A Taxonomy and Terminology of Adversarial Machine Learning.

8.2 ENISA
8.2.1 Artificial Intelligence cybersecurity challenges
Publicado en diciembre de 2020 este documento realiza un mapeo del ecosistema de ciberseguridad en IA y su entorno de amenazas. Ha sido realizada por el grupo de trabajo en ciberseguridad para la inteligencia artificial.
Puede consultarse completa en:
- https://www.enisa.europa.eu/publications/artificial-intelligence-cybersecuritychallenges

8.2.2 Securing Machine Learning
Publicado en diciembre de 2021, en este documento se ha realizado revisando de manera sistemática la literatura existente sobre machine learning. El documento hace presentación

71

especial de un análisis de amenazas para los sistemas de machine learning, proporcionando, como se ha indicado en esta guía, una relación con los controles de seguridad.
Puede consultarse completo en:
-

https://www.enisa.europa.eu/publications/securing-machine-learning-algorithms

8.2.3 Cybersecurity of AI and standardization
En este documento, publicado en marzo de 2023, se presentan los estándares (existentes, en desarrollo y planificados) relacionados con la ciberseguridad en inteligencia artificial.
Presenta sus alcances, y en sus conclusiones ofrece aquellos posibles huecos presentes en la estandarización planificada. Más allá del marco del sandbox de IA, el seguimiento de este tipo de esfuerzos de estandarización de ciberseguridad para IA es muy importante para el proveedor y responsable del despliegue de sistemas de inteligencia artificial de alto riesgo.
Puede consultarse completo en:
-

https://www.enisa.europa.eu/publications/cybersecurity-of-ai-and-standardisation

8.2.4 Multilayer Framework for Good Cybersecurity Practices for AI
Dicho texto actualiza y consolida el marco de amenazas y controles específicos de IA, así como menciona las futuras normas armonizadas del Reglamento de IA una vez sean publicadas en el DOUE.
Puede consultarse completo en:
-

https://www.enisa.europa.eu/publications/multilayer-framework-for-goodcybersecurity-practices-for-ai

8.3 Otras referencias
-
-
-
-

https://www.querypie.com/blog/machine-learning-data-poisoning-and-how-toprevent-it/ https://arxiv.org/abs/2009.07008 https://elie.net/blog/ai/attacks-against-machine-learning-an-overview/#toc-10 https://arxiv.org/pdf/1706.03691.pdf

Bagging or weight bagging

72

-
-

https://www.simplilearn.com/tutorials/machine-learning-tutorial/bagging-inmachine-learning https://www.projectpro.io/article/bagging-vs-boosting-in-machine-learning/579

Trim Algorithm
-
-

https://www.researchgate.net/figure/Several-iterations-of-the-TRIM-algorithmInitial-poisoned-data-is-in-blue-in-top-left_fig2_324166859 https://secml.github.io/class11/

Aumento de datos
-
-
-

https://arxiv.org/pdf/2010.01862.pdf https://research.aimultiple.com/data-augmentation-techniques/ https://research.aimultiple.com/data-augmentation/

Data sanitization
-
-

https://towardsdatascience.com/5-outlier-detection-methods-that-every-dataenthusiast-must-know-f917bf439210 https://towardsdatascience.com/poisoning-attacks-on-machine-learning1ff247c254db

STRIP
-

https://arxiv.org/abs/1902.06531

IMPROPER LABELING
-

https://www.researchgate.net/publication/323550082_Label_Sanitization_against_
Label_Flipping_Poisoning_Attacks

Adversarial Examples:
-

Estudio de ataques adversariales en medical machine learning: Adversarial attacks on medical machine learning — MIT Media Lab

Protección vulnerabilidades oráculo
-
-
-

-
-

Model Inversion Attacks that Exploit Confidence Information and Basic
Countermeasures https://dl.acm.org/doi/pdf/10.1145/2810103.2813677
Membership
Inference
Attacks against
Machine
Learning
Models https://arxiv.org/pdf/1610.05820.pdf.
Secure,
Robust and transparent application of
AI https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/KI/Secure_robust_and_t ransparent_application_of_AI.pdf
A
Taxonomy and
Terminology of
Adversarial
Machine
Learning https://csrc.nist.gov/publications/detail/nistir/8269/draft
SoK:
Security and privacy in machine learning https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8406613

Protección vulnerabilidades evasión

73

-

-
-
-

-
-
-
-
-
-
-

Adversarial attack and defence in reinforcement learning-from AI security view https://cybersecurity.springeropen.com/track/pdf/10.1186/s42400-019-0027x.pdf
On detecting Adversarial perturbation https://arxiv.org/pdf/1702.04267.pdf
Modelo más resiliente:
Algorithm stability on adversarial training https://proceedings.neurips.cc/paper/2021/file/df1f1d20ee86704251795841e6a9
405a-Paper.pdf
Input gradient regularisation https://towardsdatascience.com/the-many-uses-ofinput-gradient-regularization-e2af244e6950
Defensive distillation:
https://deepai.org/machine-learning-glossary-andterms/defensive-distillation
Generating
Adversarial
Examples with
Adversarial
Networks:
https://arxiv.org/pdf/1801.02610.pdf
Adversarial
Attacks and
Defenses in
Deep
Learning, https://www.sciencedirect.com/science/article/pii/S209580991930503X
Distillation as a defense to adversarial perturbations against DNN https://arxiv.org/pdf/1511.04508.pdf
Towards Deep Learning Models Resistant to Adversarial Attacks https://arxiv.org/pdf/1706.06083.pdf
Improving the Adversarial Robustness and Interpretability of Deep Neural Network by Regularizing their input Gradients https://arxiv.org/pdf/1711.09404.pdf

Differential privacy
-
-
-
-
-
-
-
-
-
-

Modelo
PATE
(paper https://arxiv.org/abs/1610.05755, explicación http://www.cleverhans.io/privacy/2018/04/29/privacy-and-machine-learning.html)
Modelo
PATE
(https://blog.openmined.org/build-pate-differential-privacy-inpytorch/)
Security and privacy in
ML https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8406613
Scalable Private Learning with Pate https://arxiv.org/pdf/1802.08908.pdf
Sustracción de datos confidenciales (membership inference attacks)
Artículo referenciado https://arxiv.org/pdf/1806.01246v2.pdf.
También https://www.cs.cmu.edu/~mfredrik/papers/fjr2015ccs.pdf.
Usar neural dropout y model stacking ayuda a mitigar el riesgo
Neural Dropout https://towardsdatascience.com/dropout-in-neural-networks47a162d621d9
Model stacking https://towardsdatascience.com/simple-model-stacking-explainedand-automated-1b54e4357916

CAT-Gen
-
-

https://arxiv.org/abs/2010.02338
Reinforcing Adversarial Robustness using Model Confidence Induced by
Adversarial Training - Xi Wu, Uyeong Jang, Jiefeng Chen, Lingjiao Chen, Somesh
Jha

74

-

Attribution-driven Causal Analysis for Detection of Adversarial Examples, Susmit
Jha, Sunny Raj, Steven Fernandes, Sumit Kumar Jha, Somesh Jha, Gunjan Verma,
Brian Jalaian, Ananthram Swami

75

76
