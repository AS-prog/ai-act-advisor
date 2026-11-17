---
name: aesia-10-guia-solidez-03-introduccion
description: "AESIA: aesia 10 guia solidez, sección «Introducción» (págs. 11-14). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-10-guia-solidez
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Introducción"
  paginas: 11-14
  origen: 2026-07-17-aesia-10-guia-solidez.pdf
  oficial: false
---
# Introducción

2. Introducción
2.1 ¿Qué es la solidez para IA?
La solidez se puede expresar a partir de una serie de propiedades asociadas al sistema de
IA que permitirán definir y establecer claramente diferentes aristas del sistema de IA.
Las palabras y descripciones destacadas se corresponden con términos que son desarrollados en el glosario (ver 7.3 Glosario).
Podemos decir que la relación entre estas propiedades, la solidez y el sistema de IA no pueda entenderse los unos, sin las otras. Estas propiedades que hemos considerado deseables son:
- Fiabilidad: Se refiere a la consistencia entre los valores inicialmente estimados y los
valores estimados subsecuentes, o la coherencia general de una medida en estadística. La solidez suele considerarse una subcaracterística de la fiabilidad
[ISO/IEC 25059:2023]. En el marco del método SQuaRE [75], la fiabilidad y la solidez se integran en la evaluación de la calidad de los sistemas de software, lo que permite una medición sistemática y alineada con estándares de calidad [ISO/IEC 25010].
- Estabilidad: En sistemas de inteligencia artificial, la estabilidad expresa el grado en
que se permite que la salida del sistema cambie de forma controlada cuando sus entradas varían dentro de un dominio específico. Esta propiedad es crucial en aplicaciones que requieren consistencia en las respuestas ante pequeñas fluctuaciones en los datos de entrada, como ocurre en tareas de clasificación, identificación o toma de decisiones automatizada. La estabilidad se basa en la disponibilidad de información previa sobre la salida esperada del sistema, ya sea conocida por el usuario, derivada de simulaciones o definida mediante sistemas de optimización. Esta característica es relevante en redes neuronales, donde ayuda a asegurar que las variaciones en las entradas no conduzcan a salidas drásticamente diferentes. Sin embargo, también es aplicable a otros modelos de IA, como sistemas de reglas, árboles de decisión o métodos de aprendizaje estadístico, siempre que se espere que el sistema mantenga una respuesta predecible y coherente dentro de un rango de variabilidad de las entradas.
- Sensibilidad: En sistemas de inteligencia artificial, la sensibilidad expresa el grado
en que se permite que la salida del sistema varíe cuando sus entradas experimentan cambios. Similar a la estabilidad, el análisis de sensibilidad requiere verificar que el sistema esté restringido dentro de ciertos límites de respuesta y es particularmente relevante en aplicaciones que exigen coherencia en condiciones específicas de entrada, como en tareas de interpolación o regresión. Este criterio se establece normalmente en términos cuantificables (como un umbral de variación permitido dentro de un rango específico de entradas), lo cual facilita la comparación entre distintas arquitecturas o enfoques de IA. La sensibilidad es crucial en sistemas que requieren precisión directa con respecto a un valor de referencia conocido (ground
10

truth), como los sistemas de IA que controlan dispositivos médicos. Por ejemplo, en el caso de una bomba de insulina controlada por IA, la sensibilidad del sistema es un factor determinante para su seguridad y fiabilidad, ya que la administración de insulina debe mantenerse dentro de los límites de las dosis recomendadas por el fabricante, sin exceder esos parámetros.
- Relevancia: Expresa la magnitud del impacto que las distintas entradas tienen sobre
las salidas en un sistema de inteligencia artificial. Dado que diferentes modelos de
IA, incluidas las redes neuronales, pueden arrojar criterios de relevancia distintos y, aun así, ser ambos válidos, cualquier protocolo de comparación entre modelos debe incluir un mecanismo para resolver posibles discrepancias (por ejemplo, mediante un sistema de votación). Este criterio es especialmente útil en aplicaciones donde la IA realiza una tarea que un humano podría realizar, y por lo tanto debe ser capaz de entender y verificar las salidas. Evaluar la relevancia es esencial para confirmar que la precisión del sistema está sustentada en los factores correctos, y este proceso de verificación puede ser realizado tanto por un operador humano como de forma automática mediante referencias previamente validadas.
- Alcanzabilidad: Esta propiedad se refiere a la precisión multi-paso de un sistema de
IA en interacción con su entorno de operación. Aplica a sistemas que funcionan bajo el paradigma de agentes, donde existe un ciclo de percepción-acción-entorno en el cual el agente percibe el estado del entorno, ejecuta acciones, y evalúa el impacto de estas hasta lograr ciertos objetivos. La propiedad de alcanzabilidad evalúa si el sistema, al aplicar un modelo de IA (como una red neuronal u otro tipo de algoritmo), puede alcanzar un conjunto de estados definidos, ya sean objetivos a lograr o estados de fallo a evitar, en función de sus decisiones. Esta propiedad es útil en diversos enfoques de IA, proporcionando una métrica de precisión y rendimiento en sistemas de bucle cerrado, es decir, aquellos donde el sistema responde de manera continua a las condiciones del entorno en tiempo real.

Ejemplo – Detención de denuncias falsas
En el análisis de riesgos para el sistema de denuncias falsas se establece que el sistema debe ser capaz de mantener una respuesta uniforme para pequeñas variaciones en los textos de la denuncia, para evitar que determinados datos o palabras clave puedan disparar la categoría de una denuncia, causando que se clasifique incorrectamente. Esta clasificación incorrecta es especialmente grave, en el caso de una clasificación de una denuncia verdadera como falsa, causando que no se trate adecuadamente.
Por ello se considera especialmente relevante la sensibilidad del sistema. Para verificar la sensibilidad del sistema de IA, respecto a variaciones de entradas, se establece su valoración local, considerada que su valoración local, para medir la variación alrededor de denuncias de los conjuntos de datos, modificadas en su entorno, pero no muy alejadas entre sí.
La evaluación local del sistema se va a realizar sobre el conjunto de datos verificación, y posteriormente extender al proceso de validación (ver apartado 4.1.3).
11

El procedimiento seguido para esta verificación consiste en los siguientes pasos:
-
-
-

-

En el conjunto de verificación se selecciona el mismo número de denuncias etiquetadas como falsas y verdaderas.
Se utiliza una bolsa de palabras genérica, suficientemente amplia, del castellano.
Para cada denuncia con la bolsa de palabras se generan nuevas denuncias, con cambios de palabras aleatorios del 5%, es decir se crean denuncias, próximas
(locales) a las seleccionadas.
Se establece que, durante la fase de verificación, se estudiará la sensibilidad del sistema frente a estas denuncias generadas y aquellas que se han seleccionado originalmente como base para estas

Las propiedades de solidez pueden ser locales o globales. Es más común verificar la solidez local que global, pues la primera es más fácil de especificar. Con local nos referimos a verificar las propiedades de solidez dentro de los dominios de entrada y salida del sistema, y siempre en relación con su finalidad prevista. Por ejemplo, un clasificador de imágenes predice correctamente “un coche”. La propiedad de solidez local puede especificar que todas las imágenes generadas rotando la imagen original 5 grados deben ser calificadas como un coche.
Un inconveniente de verificar propiedades de solidez local es que las garantías son locales a la muestra testeada y no se extienden a otras muestras en la base de datos, este inconveniente se puede soslayar, aumentando y consolidando las pruebas de solidez local para ser lo más extensas posible, y cubrir variaciones, dentro del dominio esperado. Esto permitirá encontrar puntos del dominio de entrada que son mucho menos robustos que sus vecinos, o encontrar zonas de frontera de dominio en las que el sistema es menos robusto y abordar a lo largo del proceso de diseño e implementación su mejora paulatina.
Por otro lado, las propiedades de solidez global definen garantías que se cumplen de manera determinista sobre todas las posibles entradas (éstas deben especificarse definiendo un rango válido para características de entrada, lo cual es más difícil en configuraciones donde las características individuales no tienen significado semántico).
Ambos entornos de solidez (globales y locales) tienen igual importancia para un sistema de IA de alto riesgo y acorde al estado del arte del tipo de modelo, la finalidad prevista y los riesgos para la salud, los derechos y libertades fundamentales, ambas se recomiendan verificar. La solidez local, por permitir encontrar y actuar sobre puntos menos robustos y mejorar el sistema de IA en el proceso de su diseño, prueba y validación. La global por ofrecer garantías del comportamiento del modelo en los rangos de entrada del dominio esperado. Especial interés tiene (tal y como se detalla en la guía de documentación)
considerar dentro de las propiedades de solidez, los usos indebidos razonablemente previsibles del sistema de IA, para que sean consideradas en el análisis global y local de la misma.
Propiedades deseables al diseñar sistemas de IA incluyen la solidez, resiliencia, fiabilidad, precisión, seguridad, protección, privacidad, etc. Puesto que la solidez es una propiedad crucial que supone nuevos desafíos en el contexto de sistemas de IA: la calidad de los

12

datos, la degradación del modelo, la estabilidad de las características de entrada, Precisión frente a Recall y perturbaciones en los datos de entrada.
La compresión de los riesgos especialmente relacionados con la solidez del sistema de IA es esencial para su adopción, por lo que se recomienda evaluar los riesgos especialmente ligados a la solidez de los sistemas de IA en su relación con aquellos localizados en el plan de riesgos, especialmente aquellos relacionados con los daños a la salud y los derechos y libertades de las personas físicas.
Dado que la verificación de software es un elemento esencial en cualquier proceso industrial, la necesidad de garantizar la seguridad y la precisión del sistema la convierte en un componente fundamental de su certificación. En este contexto, las técnicas de inteligencia artificial también pueden someterse a procesos de validación. No obstante, dado que no todos los métodos tradicionales son aplicables a sistemas de IA, especialmente en el caso de modelos como las redes neuronales, resulta necesario desarrollar enfoques específicos para su verificación, que serán abordados en esta guía desde la perspectiva de la solidez.
Los cambios que conlleva la transformación digital a nivel de organización podrán contemplar procesos de gestión del cambio de cultura para alcanzar los principios de IA confiable. Un ejemplo de metodologías de la teoría de juegos que puede inspirar tales cambios incluye la teoría de diseño de mecanismos (mechanism design)1 [113].
Además, una manera orientativa, resumida y visual de ver los cambios asociados al cumplimiento de los requisitos de solidez es:

1

merecedora del Nobel de Economía en 2007, en que el objetivo es obtener resultados deseados de acuerdo con un concepto de solución específico, cuando nos dan una función objetivo y desconocemos el mecanismo.

13
