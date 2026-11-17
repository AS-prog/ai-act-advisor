---
name: aesia-07-guia-de-datos-y-gobernanza-de-datos-11-anexos-parte-1
description: "AESIA: aesia 07 guia de datos y gobernanza de datos, sección «Anexos (parte 1)» (págs. 47-54). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-07-guia-de-datos-y-gobernanza-de-datos
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Anexos (parte 1)"
  paginas: 47-54
  origen: 2026-07-17-aesia-07-guia-de-datos-y-gobernanza-de-datos.pdf
  oficial: false
---
# Anexos (parte 1)

8. Anexos
8.1 ANEXO A – Métodos de recopilación de datos
Los datos existen en muchas formas y podemos crearlos o recopilarlos diferentes maneras.
En esta sección detallamos algunos de los métodos de recopilación de datos más comunes que podemos abordar [1][3].
-

-

Herramientas de recopilación automatizada de datos: en este caso la recopilación de datos se logra utilizando aplicaciones dentro de la organización
(por ejemplo, el correo electrónico) o externamente a través de un sitio web, una aplicación móvil o una aplicación similar. Consiste en utilizar programas informáticos para recopilar automáticamente datos de fuentes de datos en línea.
Algunos métodos para automatizar la recogida de datos son: Web-scraping, web crawling, uso de API, etc.
Transacciones desde otros sistemas: la recopilación o actualización de datos realizada en otros sistemas puede fluir hacia el sistema de la organización a través del intercambio electrónico de datos u otros procesos de interconexión.

-

Sensores: cada vez se introducen más datos en la organización a través de sistemas mecánicos como los sensores. Los sensores abarcan una amplia gama de dispositivos de adquisición de datos, como registros de sitios web, fuentes de medios sociales y dispositivos de Internet de las cosas, que incluyen dispositivos cotidianos, desde simples sensores de temperatura hasta televisores, coches, semáforos y edificios. Los datos de los sensores también pueden incluir señales potencialmente urgentes, como alertas y alarmas.

-

Nuevos contextos: los datos de diferentes reportes pueden combinarse con otros datos para proporcionar información adicional, que a su vez se retroalimenta con los datos de la organización. En muchos casos, estos datos adicionales aportan un nuevo contexto a los datos originales y puede ser necesario tratarlos de forma diferente. Los nuevos datos contextuales pueden proceder de decisiones que den relevancia o valor a los datos existentes.

-

Suscripción: los datos pueden estar disponibles para la organización a través de una suscripción a una fuente de datos o a almacenes de datos virtuales.

-

Crowdsourcing público: consiste en recopilar datos mediante la ayuda o aportación de personas independientes. Por ejemplo, si necesitamos recopilar imágenes de las calles para entrenar un sistema de reconocimiento de señales de tráfico podríamos obtenerlas a través del crowdsourcing público creando una plataforma para ello y proporcionando ciertas instrucciones a los participantes. Este método es habitualmente utilizado para el etiquetado de datos.
Crowdsourcing privado: es un método similar al crowdsourcing público, la diferencia está en que las aportaciones en este caso las harán grupos de especialistas privados que se contratarán para llevar a cabo esta tarea.

-

46

8.2 ANEXO B – Calidad del dato
8.2.1 ANEXO B.1 – Dimensiones de la calidad de los datos
Las dimensiones y controles de calidad de los datos se utilizan para especificar y evaluar la calidad de los datos. Generalmente, se dispone de más de un control de calidad del dato para evaluar la calidad asociada a cada dimensión. En este Anexo detallamos las principales dimensiones de la calidad en torno a los datos [6]. En el Anexo B.2 se disponen algunos ejemplos de controles de calidad de los datos para cada una de estas dimensiones.
1. Accesibilidad: se refiere al grado en que se puede acceder a los datos en un contexto específico de uso, particularmente por parte de personas que necesitan tecnología de apoyo o configuración especial debido a alguna discapacidad.
2. Auditabilidad: se refiere al grado en que todo o parte del conjunto de datos ha sido sometido a una revisión de auditoría o, en su defecto, a la disponibilidad de todo o parte del conjunto de datos para ser sometido a una revisión de auditoría.
Por ejemplo, supongamos que un conjunto de datos utilizado para entrenar un sistema de
IA de reconocimiento de imagen ha sido etiquetado por un especialista externo contratado. En esta situación, para garantizar el correcto etiquetado, podríamos contratar un tercero independiente para auditar un subconjunto de las imágenes etiquetadas.
3. Identificabilidad: se refiere la capacidad de identificar un principal de información de identificación personal (PII) directa o indirectamente sobre la base de un conjunto dado de
PII. Es importante comprender si cualquier PII en un conjunto de datos se puede usar para identificar un principal de PII, ya que los requisitos legales en algunas jurisdicciones pueden restringir dicha actividad. Los procesos de desidentificación o anonimización se pueden aplicar a los datos de entrenamiento, validación y prueba para reducir la posibilidad de identificación.
Por ejemplo, supongamos que disponemos de un sistema de IA desarrollado para mostrar publicidad específica a cada usuario, entrenado mediante consultas de motores de búsqueda. El conjunto de datos incluye la dirección IP del usuario, que se considera PII en algunas jurisdicciones, entre ellas la española por doctrina del TS y del TJUE. La anonimización se aplica al conjunto de datos para eliminar la dirección IP antes de que el conjunto de datos se divida en conjuntos de datos de entrenamiento, validación y prueba, tratando, de esta manera, de reducir la posibilidad de identificación.
4. Portabilidad: se refiere a la capacidad de mover datos de un sistema a otro, dentro de un contexto específico, preservando su calidad.
Por ejemplo, supongamos que para el desarrollo de nuestro sistema de IA necesitamos procesar los datos en múltiples plataformas o sistemas. Necesitamos mantener la calidad de los datos cuando los transfiramos de una plataforma o sistema a otro.
5. Comprensibilidad: se refiere a la facilidad con la que los datos puedan ser interpretados por la organización. Los sistemas de IA parten de modelos y construcciones matemáticas cuyo lenguaje principal se basa en números y algoritmos. Si éstos no pudieran

47

ser interpretados por los usuarios, podrían llegar a perder su función y por ello es una dimensión de la calidad relevante.
6. Coherencia temporal: se refiere a la alineación de los datos con la realidad que representan actualmente en términos de su antigüedad.
Por ejemplo, los datos sobre las personas pueden estar incompletos para las poblaciones subrepresentadas antes de los cambios en las regulaciones y normas sociales. Por otro lado, los sistemas de IA basados en datos económicos recopilados durante varias décadas pueden ser incorrectos si los datos no se corrigen por inflación, tipos de cambio y otros factores que varían con el tiempo.
7. Eficacia: se refiere a la medida en la que el conjunto de datos cumple con una serie de requisitos para su uso en el desarrollo del sistema de IA en específico:
-

-

-

Para un sistema de visión computacional, la eficacia del conjunto de datos puede ser la proporción aceptable más baja en la que la cantidad de imágenes con brillo o resolución sea inferior a un umbral requerido sobre todas las muestras del conjunto de datos.
Para un sistema de clasificación de imágenes, la eficacia del conjunto de datos puede referirse a la proporción aceptable más baja de la cantidad de imágenes que pertenecen a una clase sobre la cantidad total de muestras en el conjunto de datos.
Para un sistema de detección de objetos, la eficacia del conjunto de datos puede referirse a la proporción aceptable más baja en la que la cantidad de imágenes con números o áreas de cuadros delimitadores es inferior a un umbral requerido en todas las muestras del conjunto de datos.

8. Eficiencia: se refiere al grado en que los datos tienen atributos que pueden procesarse y proporcionar los niveles esperados de rendimiento mediante el uso de las cantidades y tipos apropiados de recursos en un contexto específico de uso.
9. Precisión: se refiere al grado en que cada dato del conjunto de datos tiene el valor correcto. Dicho de otra forma, es el grado en que los datos tienen atributos que representan correctamente el verdadero valor de los atributos previstos. Podemos diferenciar, principalmente, dos tipos de precisión:
-
-

Precisión sintáctica que considera la proximidad de los datos a un conjunto de datos sintácticamente correctos en un dominio relevante
Precisión semántica que considera la proximidad de los datos a un conjunto de datos semánticamente correctos en un dominio relevante

Un elemento de datos es sintácticamente correcto si su valor de datos tiene el mismo tipo que su tipo de datos explícito y semánticamente correcto si su valor de datos tiene un valor esperado correspondiente a la tarea ML (Machine Learning - Aprendizaje automático). Los modelos ML son construcciones matemáticas, lo que significa que la baja precisión sintáctica o semántica de los datos en conjuntos de datos de entrenamiento, validación o prueba puede hacer que el modelo en sí sea incorrecto o que las inferencias realizadas por el modelo puedan ser incorrectas.

48

Para un sistema de clasificación de aprendizaje supervisado, la corrección de las etiquetas puede afectar la precisión de inferencia de un modelo entrenado a partir de datos. Los factores que deben considerarse para medir la precisión del etiquetado incluyen:
-
-

Corrección de las etiquetas de categoría
Corrección de los cuadros delimitadores etiquetados

10. Completitud: se refiere al grado en el que los datos presentan valores para todas las características. La incompletitud de los conjuntos de datos puede tener un grave impacto en el desarrollo del sistema de IA.
La completitud de los datos etiquetados en un conjunto de datos es relativa. En diferentes escenarios, el significado de completitud puede ser diferente y debe considerarse con contextos de uso específicos. Los factores que deben considerarse para su medida incluyen:
-

-

La completitud de un conjunto de datos que se utiliza para una clasificación de imágenes basada en ML debe comprobar las muestras no etiquetadas en un conjunto de datos, que no se pueden usar directamente en ML supervisado.
La completitud de un conjunto de datos que se utiliza para una detección de objetos basada en ML debe comprobar la incompletitud de los cuadros delimitadores etiquetados en los objetos.

En particular, es común en la vida real que una muestra tenga múltiples objetos en varias categorías, ya que es difícil capturar una escena con un solo objeto aislado que ocupa todo el espacio de visión. En este caso, para medir la completitud del conjunto de datos para un reconocimiento de imágenes basado en ML, debe considerar si:
-
-
-

Existe cualquier objeto de destino en una muestra
Todos los objetos de destino están categorizados
Todos los objetos de destino detectados se etiquetan con cuadros delimitadores u otros métodos

11. Cumplimiento normativo: se refiere al grado de cumplimiento con las regulaciones, estándares, normativas u otras reglas de cumplimiento en torno a los datos. Por ejemplo, los datos personales utilizados para el desarrollo de sistemas de IA pueden estar sujetos a requisitos legales y reglamentarios.
12. Credibilidad: se refiere al grado en que los datos tienen atributos que los usuarios consideran verdaderos y creíbles en un contexto específico de uso. La credibilidad es aplicable para datos individuales, para datos relacionados en un registro de datos y para todo el conjunto de datos. El contexto en el que se utilizan los datos puede afectar su veracidad y credibilidad percibidas. Los datos pueden ser perturbados durante el procesamiento por partes autorizadas y no autorizadas.
Una preocupación emergente para ML es que las partes no autorizadas perturban los datos de entrenamiento, validación, prueba y producción para hacer deliberadamente que los modelos entrenados sean inutilizables o para manipular las inferencias hechas por un modelo entrenado.

49

Los procesos utilizados en la preparación de datos pueden cambiar los datos sin cambiar su significado (por ejemplo, normalización, imputación, segmentación o combinación de características). En estos casos los datos mantienen su credibilidad.
13. Equilibrio: se refiere a la distribución de las muestras para todos los aspectos del conjunto de datos. Por ejemplo, si el conjunto de datos representa X número de categorías de elementos, el número de muestras por categoría debe distribuirse uniformemente para que este conjunto de datos se equilibre. Para un conjunto de datos de imagen, estos aspectos pueden incluir etiquetas de categoría significativas para la lógica empresarial, resolución de figuras, brillo de figuras, la relación anchura/altura de los cuadros delimitadores etiquetados, el tamaño de los cuadros delimitadores etiquetados y cualquier otro que pueda influir en el rendimiento del modelo de aprendizaje automático.
El equilibrio de un conjunto de datos puede afectar a una parte del rendimiento general de un modelo de aprendizaje automático. Para un sistema de visión artificial basado en ML, se debe considerar el equilibrio del conjunto de datos.
-

-

-

Cuando existen diferencias considerables de brillo o resolución entre las muestras de un conjunto de datos de entrenamiento y los datos del mundo real, los modelos de ML pueden fallar debido a datos ruidosos introducidos por debilidad o vaguedad.
En un sistema de clasificación basado en ML, la presencia de una categoría desequilibrada de población de muestra puede dar lugar al fracaso del descubrimiento y la clasificación de instancias raras. Tales casos pueden incluso clasificarse erróneamente o identificarse como datos ruidosos.
En un sistema de detección de objetos basado en ML, las diferencias significativas en la relación anchura/altura o el tamaño de los cuadros delimitadores pueden dar lugar a la incoherencia de tamaño sobre los objetos que se van a detectar, dado un tamaño fijo de campo receptivo. En consecuencia, esto también puede causar una pérdida de generalización, si no se aplican enfoques adicionales de verificación o ajuste de objetos multi tamaño.

14. Consistencia: se refiere al grado en que los mismos datos representados en diferentes fuentes y datos diferentes que guarden una relación significativa no presenten contradicciones o incoherencias. La consistencia es un aspecto clave de los datos utilizados para el desarrollo de sistemas de IA, ya que las características utilizadas en los datos de entrenamiento deben proporcionar en conjunto un modelo que permita inferencias correctas en los datos de producción. Además, ML puede ser literal en su interpretación de los datos. Los registros duplicados pueden causar una sobre ponderación de ciertas características. Las contradicciones entre las características de los datos de entrenamiento pueden hacer que un modelo entrenado funcione por debajo de los requisitos.
La distribución de los datos para cada característica puede considerarse una medida de consistencia. En algunos casos, los modelos de ML requieren datos con una distribución normal para cumplir con los requisitos de rendimiento.
15. Diversidad: se refiere a la diferencia entre muestras en términos de los datos objetivo.
En un conjunto de datos utilizado para un sistema de IA, es importante una diferencia adecuada entre las muestras. Si todos o la mayoría de los registros de un conjunto de datos

50

son iguales, un modelo de aprendizaje automático entrenado a partir de ese conjunto de datos puede tener el riesgo de sobre ajustarse y, en consecuencia, ser menos generalizable. La diversidad de un conjunto de datos representa un grado de cómo el conjunto de datos contiene varios dominios de valor, etiquetas, clústeres y distribuciones entre datos individuales. La mejora de datos mediante modelos generativos de aprendizaje automático puede mejorar la diversidad de datos, pero estos enfoques pueden fallar si la diversidad del conjunto de datos original es limitada. La diversidad está estrechamente relacionada con la representatividad y el equilibrio. Es una característica de calidad de datos que se puede utilizar para evaluar la fidelidad de un conjunto de datos.
La medición de la diversidad se puede realizar en el contexto de los datos objetivoespecíficos, según lo determinado por los requisitos de la tarea ML.
16. Relevancia: se refiere al grado en que un conjunto de datos es adecuado para un contexto dado.
Para un sistema de IA, la relevancia puede significar que las características seleccionadas en los datos de entrenamiento y sus valores son buenos predictores para la variable objetivo. Por ejemplo, supongamos que se utiliza un sistema de IA para determinar la solvencia de las personas. Los datos de entrenamiento son representativos de la muestra de la población que se espera que aparezca en los datos de producción. Los datos de capacitación incluyen características relevantes como el historial crediticio previo, los ingresos, la permanencia en el trabajo y el patrimonio neto, que son buenos predictores de solvencia. Los datos de entrenamiento también incluyen la altura y el peso de cada persona. Las pruebas estadísticas no muestran correlación de altura y peso con el historial crediticio anterior y se consideran malos predictores del desempeño crediticio futuro. Para mejorar la relevancia general del conjunto de datos, se eliminan las características de altura y peso.
17. Representatividad: se refiere al grado en que una muestra refleja la población objetivo que se está estudiando. Para el ML supervisado, el conjunto de datos de entrenamiento puede considerarse como la muestra y los datos de producción como la población en estudio. Cuando los datos de entrenamiento no representan suficientemente los datos de producción, el sistema de IA entrenado puede no funcionar según lo requerido.
La representatividad de los datos está relacionada con la relevancia en el sentido de que es poco probable que un conjunto de datos que no represente a la población en estudio proporcione buenos predictores para la variable objetivo. Por ejemplo, para una aplicación de reconocimiento facial, es poco probable que un conjunto de datos de entrenamiento que no contenga imágenes de personas con piel oscura dé como resultado un sistema de IA entrenado que funcione correctamente en datos de producción que incluyan imágenes de personas con piel oscura.
18. Similitud: se refiere al grado de similitud entre muestras en términos de características interesadas. Esto es relevante para las tareas de clasificación que normalmente se implementan mediante aprendizaje supervisado. Esto también es relevante para las tareas de agrupación que normalmente se implementan mediante aprendizaje no supervisado.

51

Tanto las tareas de clasificación como las de agrupación requieren un nivel adecuado de diferencia entre las muestras para funcionar con éxito.
Un sistema de IA entrenado en un conjunto de datos que contiene imágenes bastante similares (por ejemplo, que se generan mediante un ligero desplazamiento de píxeles basado en unas pocas imágenes semilla) puede tener el riesgo de sobreajuste y, en consecuencia, menos generalización. En este caso, es posible considerar la aplicación de enfoques de mejora de datos, como la rotación y el desplazamiento. que puede mejorar la generalización del sistema de IA. Estos enfoques no pueden funcionar si el número de imágenes semilla es limitado. En este caso, debe comprobarse la proporción de muestras similares. Otro enfoque es considerar algoritmos de agrupación con métodos de mitigación de deriva de temas.
Otras medidas identifican la similitud de datos a través del enfoque geométrico: es decir, un conjunto de datos de N registros y M características, se pueden representar como N vectores en un M-espacio dimensional, para que pueda ser analizado y comparado utilizando las herramientas de la geometría. En particular, la similitud puede asociarse a la posición mutua de los vectores en el espacio.

8.2.2 ANEXO B.2 – Controles de calidad de los datos
En este Anexo se disponen algunos ejemplos de controles de calidad de los datos para cada una de las dimensiones de calidad descritas [6].
1. Accesibilidad
-

-

Accesibilidad del usuario: grado en que los usuarios consideran accesibles los valores de los datos.
o X = A/B, donde:
o A=número de datos relevantes para la tarea del usuario que son fácilmente accesibles.
o B=número de datos relevantes para la tarea del usuario cuyo acceso es necesario.
Accesibilidad al formato de datos: grado en que un dispositivo específico permite la accesibilidad.
o X =1- A/B, donde:
o A=número de datos que no son accesibles debido a su formato.
o B=número de datos para los que se puede definir un formato accesible.

2. Auditabilidad:
-

-

Registros auditados: Proporción de registros en el conjunto de datos que han sido auditados.
o X =A/B, donde:
o A=número de registros auditados.
o B=número de registros total del conjunto de datos.
Registros auditables: Proporción de los registros del conjunto de datos que están disponibles para ser auditados.
o X =A/B, donde:

52

o o

A=número de registros disponibles para ser auditados.
B=número de registros total del conjunto de datos.

3. Identificabilidad:
-

Índice de identificabilidad: Proporción de registros en el conjunto de datos que se pueden usar para la identificación.
o X =A/B, donde:
o A=número de registros que contienen datos que se pueden utilizar para la identificación.
o B= número de registros total del conjunto de datos.

4. Portabilidad:
-

Ratio de portabilidad de datos: Proporción de datos que preservan su calidad tras la portabilidad.
o X =A/B, donde:
o A=número de datos que preservan su calidad tras la portabilidad.
o B=número de datos que han sido portados.

5. Comprensibilidad:
-

-

-

-

Comprensibilidad de los símbolos: Grado en el que son usados símbolos comprensibles.
o X =A/B, donde:
o A=número de datos representados por símbolos conocidos.
o B=número de datos para los cuales es necesario comprender los símbolos.
Comprensibilidad semántica: Proporción de términos definidos en el diccionario de datos.
o X =A/B, donde:
o A=número de datos definidos en el diccionario de datos utilizando un lenguaje comprendido por los usuarios.
o B=número de datos definidos en el diccionario de datos.
Comprensibilidad de los valores de datos: Grado en el que los valores de los datos son comprendidos por los usuarios.
o X =A/B, donde:
o A=número de datos fácilmente comprensibles para los usuarios.
o B=número de datos que los usuarios necesitan comprender en un contexto concreto.
Comprensibilidad de la representación de datos: Grado en que los datos son representados de forma comprensible para los usuarios en un sistema específico.
o X =A/B, donde:
o A=número de datos considerados comprensibles en un modelo de datos.
o B=número de datos en el modelo de datos.

6. Coherencia temporal:
-

Coherencia temporal de las características: Proporción de datos para una característica del conjunto de datos que se encuentran dentro del rango temporal requerido.

53
