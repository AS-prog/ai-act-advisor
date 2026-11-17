---
name: aesia-07-guia-de-datos-y-gobernanza-de-datos-13-anexos-parte-3
description: "AESIA: aesia 07 guia de datos y gobernanza de datos, sección «Anexos (parte 3)» (págs. 63-70). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-07-guia-de-datos-y-gobernanza-de-datos
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Anexos (parte 3)"
  paginas: 63-70
  origen: 2026-07-17-aesia-07-guia-de-datos-y-gobernanza-de-datos.pdf
  oficial: false
---
# Anexos (parte 3)

1. Sistemas de clasificación: el sesgo en los sistemas de clasificación puede detectarse mediante mediciones de diferentes tipos de errores con respecto a varios grupos. El enfoque de dividir los datos en conjuntos de entrenamiento, validación y prueba se complementa subdividiendo cada uno de esos conjuntos en función de las características con respecto a las cuales se espera que el sistema sea justo. Si hay múltiples características relevantes para detectar posibles sesgos en un sistema en particular, entonces esas características podrían considerarse independientes o interseccionales. Por ejemplo, un sistema que es imparcial con respecto al género y la raza independientemente podría estar sesgado hacia una combinación específica de los dos.
Una vez que los datos se han dividido adecuadamente, se calculan métricas de sesgo en cada grupo y se realizan comparaciones entre grupos relacionados. Un sistema de clasificación podría ser "imparcial" con respecto a las características relevantes si las mediciones basadas en métricas entre grupos están dentro de un delta suficientemente pequeño.
2. Sistemas de aprendizaje por refuerzo: el sesgo en los sistemas de aprendizaje por refuerzo difiere del de los sistemas de clasificación. En este caso el sesgo se centra en la serie de acciones que va tomando el sistema. Si bien probar el sesgo de los sistemas de aprendizaje por refuerzo es una práctica menos desarrollada, están surgiendo algunos métodos. Los sistemas de aprendizaje por refuerzo generalmente se entrenan en función de una medición de utilidad siguiendo sus acciones. Las métricas de sesgo se pueden aplicar a esta medición de utilidad en todos los grupos.
Además de usar la utilidad como análogo a la precisión, el sesgo en los sistemas de aprendizaje continuo que utilizan el aprendizaje por refuerzo puede manifestarse como diferentes “path attractors” para diferentes grupos. Este podría ser particularmente el caso en los sistemas de aprendizaje por refuerzo que realizan recomendaciones de contenido.
En tales sistemas, el "ground truth" es un concepto menos definido. Si, por ejemplo, un asistente de IA para guiar a los estudiantes universitarios a lo largo de su curso de estudio condujo consistentemente a las mujeres hacia profesiones de cuidado y a los hombres hacia profesiones de ingeniería, entonces ese sistema está potencialmente sesgado independientemente de las métricas de utilidad.
3. Matriz de confusión: una matriz de confusión (figura 1) es un método utilizado para descubrir el sesgo de los clasificadores. Informa el número de falsos positivos, falsos negativos, verdaderos positivos y verdaderos negativos e incluye otros criterios de rendimiento derivados de estos valores. Dado que una matriz de confusión contiene y compara múltiples métricas, permite un análisis detallado del rendimiento de un clasificador y es útil para eludir o descubrir las debilidades de las métricas individuales. Por ejemplo, el uso de métricas individuales para medir el rendimiento de un clasificador daría lugar a resultados engañosos si los conjuntos de datos subyacentes estuvieran desequilibrados y, por lo tanto, no pueden proporcionar resultados confiables.

62

Figura 1 – Matriz de confusión y métricas de rendimiento de clasificación derivadas [17]

4. Igualdad de probabilidades: también conocida por su término en inglés “equalized odds” significa que las decisiones de un algoritmo son independientes de una categoría A dada una entrada Y. Un predictor Ŷ satisface las probabilidades igualadas con respecto a la categoría A y la salida Y, si Ŷ y A son independientes condicionales a Y:
𝑃(Ŷ = ŷ|𝑌 = 𝑦, 𝐴 = 𝑚) = 𝑃 (Ŷ = ŷ|𝑌 = 𝑦, 𝐴 = 𝑛), ∀ 𝑌, 𝑚, 𝑛 ∈ 𝐴
Esto implica que las tasas de verdaderos positivos (TPR) son iguales en todas las categorías demográficas y las tasas de falsos positivos (FPR) son iguales en todas las categorías demográficas.
Debemos considerar que esta definición permite que los modelos tengan en cuenta la información demográfica. TPR es igual a 1 - Tasa de falsos negativos (FNR), por lo que esto también fomenta tasas de falsos negativos iguales en todas las categorías demográficas.
Para ver las compensaciones entre falsos negativos y falsos positivos, comparar la tasa de falsos negativos y la tasa de falsos positivos podría ayudar.
5. Igualdad de oportunidades: también conocida por su término en inglés “equality of opportunity” significa que las decisiones de un algoritmo donde Ŷ=1 son independientes de una categoría A dada la entrada Y=1.
Un predictor binario Ŷ satisface la igualdad de oportunidades con respecto a A y Y si Ŷ=1 y
A son independientes condicionales a Y=1. Formalmente:
P (Ŷ=1|Y=1, A=m) = P (Ŷ=1|Y=1, A=n) , ∀ 𝑚, 𝑛 ∈ 𝐴
Esto implica tasas positivas verdaderas (TPR) iguales en todas las categorías demográficas.

63

6. Paridad: La paridad estadística significa que hay tasas de predicción iguales entre las categorías. La paridad demográfica dice que hay tasas de predicción iguales entre las categorías demográficas, como la raza. La paridad demográfica, que es un caso de paridad estadística, significa que una decisión, como aceptar o rechazar una solicitud de préstamo, debe ser independiente de un atributo demográfico. Formalmente, dada la variable demográfica A:
𝑃(Ŷ = ŷ|𝐴 = 𝑚) = 𝑃(Ŷ = ŷ|𝐴 = 𝑛), ∀ 𝑚, 𝑛 ∈ 𝐴
La paridad no captura los casos en los que la decisión de salida está correlacionada con uno de los grupos o atributos que se evalúan, y no hay garantía de que las predicciones realizadas sean igualmente buenas para cada categoría.
7. Igualdad predictiva: la igualdad predictiva implica tasas de falsos positivos (FPR)
iguales en todas las categorías demográficas. Formalmente:
𝑃(Ŷ = 1|𝑌 = 0, 𝐴 = 𝑚) = 𝑃(Ŷ = 1|𝑌 = 0, 𝐴 = 𝑛), ∀ 𝑚, 𝑛 ∈ 𝐴

8.3.3 ANEXO C.3 – Medidas de tratamiento del sesgo
En este Anexo detallamos algunas de las medidas de tratamiento del sesgo más comunes que pueden implementarse para mitigar el impacto de los posibles sesgos que hayamos identificado y afectar al funcionamiento deseado de nuestro sistema de IA. Las medidas detalladas a continuación van más allá del contexto de los datos, se trata de un enfoque que trata de abarcar el tratamiento de los sesgos en las diferentes etapas del ciclo de vida de un sistema de IA [4]:
1. Análisis del contexto y los requisitos del sistema
El análisis de los requisitos del sistema es una actividad importante para mitigar el sesgo.
Es la etapa donde se analizan los requisitos internos y externos, se determinan las partes interesadas del sistema y se evalúan los objetivos del sistema. Para este hito, se han identificado los riesgos planteados por el sistema, se ha evaluado el impacto para las partes interesadas identificadas y se han definido los niveles de participación de las partes interesadas.
1.1 Requisitos externos
La identificación de requisitos externos como parte de la actividad de análisis del sistema es una parte normal del ciclo de vida de desarrollo y adquisición de sistemas. Durante este proceso podría prestarse especial atención a los siguientes marcos reglamentarios:
-
-
-
-

Instrumentos internacionales de derechos humanos e igualdad.
Leyes y orientaciones específicas relacionadas con la provisión de soluciones técnicas.
La legislación sobre protección de datos y privacidad podría incluir disposiciones relativas a la toma de decisiones automatizada.
Derecho de la competencia y de los negocios.

A continuación, se presentan ejemplos de posibles tipos de obligaciones para la entidad responsable:

64

-
-

-
-
-

La necesidad de una evaluación de riesgos, que podría incluir las preocupaciones sociales desde la perspectiva de las partes interesadas afectadas.
Notificación a los usuarios de que están sujetos a una decisión automatizada, el requisito de obtener el consentimiento explícito y proporcionar una alternativa no automatizada cuando no se otorga el consentimiento.
Asegurar un cierto nivel de auditabilidad o explicabilidad en la solución, para apoyar el análisis de una decisión o evento en particular.
Actividades para cuantificar o mitigar los riesgos, como la recopilación de metadatos sobre fuentes de datos para comprender la procedencia y la calidad.
Provisión para la participación significativa de un ser humano en el proceso de toma de decisiones.

La provisión y el precio equivalentes de servicios para grupos de personas con ciertas características. Esto podría requerir la capacidad de demostrar que la igualdad se logra en la práctica.
1.2 Requisitos internos
Además de los requisitos reglamentarios, muchos otros factores podrían contribuir al deseo de una parte interesada de mitigar el sesgo, tales como:
-
-
-

Metas, estrategias y políticas internas de una organización.
Valores morales o culturales.
Evitar preocupaciones sociales o daños a la reputación.

El proceso de análisis puede prestar especial atención a cinco áreas específicas: inclusión de expertos transdisciplinarios; la identificación de las partes interesadas; la selección de fuentes de datos; cambio externo; y especificación de los criterios de aceptación, incluidos los niveles aceptables de sesgo.
1.3 Expertos transdisciplinarios
Si bien el sesgo no deseado es un tema relativamente nuevo en el contexto de la tecnología, es un tema bien entendido en las ciencias sociales. Como parte del proceso de análisis de requisitos (y, de hecho, de todo el ciclo de vida del sistema), es relevante considerar la experiencia que podría requerirse para mitigar completamente las preocupaciones sociales sobre el sesgo y tener en cuenta diversas perspectivas. Esto podría incluir:
-
-
-
-

Científicos sociales y especialistas en ética;
Científicos de datos y especialistas en calidad;
Expertos legales y de privacidad de datos;
Representantes de usuarios o grupos de partes interesadas externas.

Por ejemplo, los diseñadores de un sistema de reconocimiento facial podrían dar importancia a la característica de contorno facial en su diseño y pasar por alto el hecho de que el contorno podría estar (parcial / completamente) cubierto para personas con antecedentes culturales / religiosos particulares. Es más probable que un equipo suficientemente diverso identifique tales limitaciones con diseños, suposiciones y conjuntos de datos.

65

1.4 Identificación de las partes interesadas
El análisis tradicional de los requisitos incluye la identificación de las partes interesadas. Sin embargo, para cumplir con los aspectos de los marcos regulatorios antes mencionados y mitigar adecuadamente las preocupaciones sociales, podría ser necesario ampliar esta definición tradicional de parte interesada para incluir a aquellos directa e indirectamente afectados por el sistema implementado.
Según los tipos de datos que se utilizan para tomar decisiones automatizadas, podría ser necesario descomponer aún más las listas de partes interesadas en grupos de personas que podrían verse afectadas de manera diferente por el sesgo en el sistema, tener diferentes habilidades en el uso del sistema o tener diferentes niveles de conocimiento y acceso. Es importante considerar qué sesgos, experiencias negativas o resultados discriminatorios podrían ocurrir.
Estos pueden considerarse a través de una variedad de diseño participativo o métodos etnográficos, los cuales implican un alcance activo y una discusión con los grupos afectados. Por lo general, es insuficiente señalar quién podría verse afectado teóricamente sin el aporte directo de esos grupos. A menudo, tampoco es suficiente que un miembro del grupo afectado (que posiblemente también trabaje como parte del equipo de diseño)
evalúe cómo se ve afectado ese grupo. Los grupos no son monolitos, y una persona no siempre puede representar adecuadamente la gama de perspectivas posibles.
La identificación y el compromiso de las partes interesadas podrían incluirse en una descripción formal y documentación de las áreas de preocupación anticipadas y las posibles consecuencias para los grupos afectados, positivas y negativas. De estos, se pueden derivar requisitos más calificados y cuantitativos. Una evaluación de impacto humano realizada en fases posteriores puede revisar estas áreas de preocupación y evaluar si la preocupación se mitigó con éxito.
1.5 Selección y documentación de fuentes de datos
La selección de datos utilizados para formar reglas explícitas dentro de un sistema experto basado en reglas, o datos que se utilizan para entrenar modelos de ML, es una actividad esencial que tiene una influencia significativa en el sesgo.
En el caso del conocimiento explícito, es importante considerar los sesgos cognitivos humanos ya presentes en aquellos que especifican el conocimiento. El sesgo cognitivo humano podría estar presente en un juicio humano, que luego se codifica en un sistema basado en reglas, y luego se propaga durante toda la vida útil del sistema a una escala mayor. Si bien podría considerarse aceptable que tal sesgo cognitivo esté presente en una sola decisión humana, propagar ese sesgo a través de la toma de decisiones automatizada podría tener un impacto mucho mayor.
Los sistemas estadísticos de IA que aprenden de los datos sin que se especifique el conocimiento explícito sufren muchos riesgos. Se podría considerar la fuente de datos individual para determinar:
-

Integridad. Un origen de datos que excluye determinados registros porque no contienen las mismas características para todos los registros podría no proporcionar

66

-

-

-

-

una imagen completa y provocar defectos en el proceso de entrenamiento. Es poco probable que los datos disponibles públicamente (por ejemplo, de Internet) tengan una distribución equivalente entre grupos de personas.
Exactitud. Un origen de datos que contenga datos inexactos propagará esas imprecisiones en un modelo de aprendizaje automático. Esto podría dar lugar a problemas generales de precisión, pero estos problemas también podrían estar sesgados hacia ciertos grupos de personas, por ejemplo, aquellos con menos historial de crédito.
Procedimientos de recogida. Es importante comprender el linaje de los datos, cómo se recopilan, cómo se ingresan y si estos procesos afectan la integridad y la precisión. Se puede considerar la ubicación y el entorno del que se obtienen los datos.
Coherencia temporal. La frecuencia con la que se recopilan o actualizan los datos puede ser relevante para garantizar su exactitud. Por el contrario, la actualización puede requerir una nueva evaluación. Un sistema que pasa una auditoría puede quedar fuera de conformidad, especialmente si las actualizaciones provienen de un proceso diferente al de los datos iniciales.
Consistencia. La consistencia con la que se determinan los datos de entrada (o etiquetas) puede ser importante. Por ejemplo, si un humano está categorizando elementos que no tienen un límite claro entre categorías, diferentes categorías o etiquetas podrían resultar de los mismos datos.

1.6 Cambio externo
Tal vez sea necesario prestar atención a la forma en que podrían producirse cambios en la utilización del sistema desarrollado o adquirido, ya que ello podría requerir una reevaluación completa de un sistema.
Algunos ejemplos son:
-

-

El despliegue de un sistema existente en un entorno diferente, incluidos diferentes usuarios, mercados objetivo y fuentes de datos, puede cambiar los riesgos y requerir que se vuelva a evaluar un sistema.
Con el tiempo, la relación entre las entradas y salidas del sistema puede cambiar.
Por ejemplo, un sistema que utiliza un modelo de ML para tomar decisiones basadas en correlaciones establecidas durante el entrenamiento inicial del sistema podría sufrir si esas correlaciones cambian con el tiempo.

Los casos de uso para el sistema pueden desarrollarse, ya sea deliberada u orgánicamente, requiriendo una reevaluación de los riesgos.
-

Las normas sociales cambian con el tiempo (por ejemplo, las actitudes hacia las normas de comportamiento de género, la forma corporal ideal o el tabaquismo). Es posible que sea necesario reevaluar el sesgo en los sistemas de IA para considerar los cambios resultantes (como métricas, riesgos, partes interesadas o requisitos) y abordarse en consecuencia.

67

1.7 Criterios de aceptación
Los requisitos efectivos son comprobables, ya que cuando se evalúan es posible determinar si un sistema los cumple. A menudo, el rendimiento del sistema de IA se compara con el de los humanos. Aun así, es beneficioso poder especificar el rendimiento de manera estadística. Por ejemplo, las partes interesadas pueden especificar un límite para las decisiones falsas positivas o falsas negativas, además de una métrica de precisión general.
Establecer la aceptación en términos de características específicas del sistema y el grado de su cumplimiento por adelantado permite una evaluación y toma de decisiones efectivas.
Los criterios de falla pueden ser el límite inferior de aceptación, estableciendo límites claros para el rendimiento aceptable de un modelo. Sin que se establezcan y monitoreen estos criterios, un sistema de IA podría desviarse de tal manera que surjan sesgos no deseados sin ser notados o remediados. La forma en que un sistema falla también podría necesitar ser considerada cuidadosamente como parte del proceso de diseño para evitar que ocurran casos extremos de sesgo.
2. Diseño y desarrollo
Los modelos en sí mismos pueden estar sesgados si no se tiene cuidado para evitar esto.
Los sesgos humanos pueden codificarse en los sistemas de ML a través de suposiciones implícitas que se abren camino en el diseño. Por lo tanto, ayuda a identificar y hacer explícitas las suposiciones implícitas.
2.1 Representación y etiquetado de datos
Un paso clave en el desarrollo de un sistema de aprendizaje automático es decidir cómo representar mejor los datos de entrenamiento en características que el modelo pueda interpretar. Esto también se denomina ingeniería de características, y el Anexo C.1 describe algunos tipos de sesgo de datos que podrían afectar este proceso. Hay varios criterios a menudo implícitos que entran en este proceso, incluidos los criterios por los cuales los datos se consideran "buenos" o "malos" (por ejemplo, si una foto sobreexpuesta podría mantenerse en un conjunto de datos). Estos criterios sobre qué datos se incluyen en los datos de entrenamiento y qué características se seleccionan pueden hacerse explícitos. Es importante considerar cómo los datos se relacionan con el propósito de construir el sistema, el proceso por el cual se eligen las características y las personas que eligen las características y su justificación.
Es importante evaluar las características elegidas para cualquier dato y sesgo cognitivo humano, como valores de entidad faltantes, valores de características inesperadas o sesgo de datos. Cualquiera de estos podría indicar que ciertos grupos o características no están representados con precisión en los datos.
La falta de valores de entidad podría ser el resultado de sesgos implícitos en el proceso de recopilación de datos, que podrían necesitar ser modificados.
En los algoritmos de aprendizaje profundo donde las características se crean durante el entrenamiento, las etiquetas correctas son críticas. Las anotaciones realizadas por humanos para crear etiquetas para los datos pueden ser propensas a sesgos debido a sesgos

68

cognitivos humanos o errores humanos debido a dificultades en la tarea de etiquetado en sí. Es importante garantizar que las etiquetas sean correctas mediante la evaluación tanto de los etiquetadores como de los datos finales etiquetados.
Los anotadores de datos a menudo anotan y etiquetan los datos que se utilizarán para el entrenamiento de ML supervisado. Los errores consistentes o los sesgos cognitivos humanos que se manifiestan durante ese proceso se propagan en un modelo entrenado.
Cuando se utilizan anotadores de datos para el etiquetado de datos, podría ser útil comprender la diversidad y los objetivos de las personas que anotan los datos. Por ejemplo, podría considerarse cómo se ve el éxito para diferentes trabajadores, y las compensaciones entre el tiempo dedicado a la tarea y el disfrute de la tarea.
Los responsables del despliegue pueden desarrollar tareas que tengan en cuenta las diferencias humanas (y los sesgos cognitivos) en la anotación, por ejemplo, mediante el uso de preguntas de prueba de oro con respuestas conocidas u otras formas de preselección de participantes.
La claridad de las instrucciones, así como la obtención de comentarios de los trabajadores de la multitud sobre tareas potencialmente confusas, podrían ser importantes para reducir el sesgo no deseado. La variabilidad humana, incluida la accesibilidad, la memoria muscular y los sesgos cognitivos humanos en la anotación, podría explicarse mediante el uso de un conjunto estándar de preguntas con respuestas conocidas.
2.2 Herramientas de transparencia
Para aclarar los casos de uso previstos de los modelos de ML y minimizar su uso en contextos para los que no son adecuados, los modelos publicados pueden ir acompañados de documentación que detalle sus características de rendimiento. Las herramientas de transparencia del modelo podrían proporcionar un marco para la presentación de informes transparentes sobre la procedencia del modelo de ML, el uso y la evaluación basada en la imparcialidad. La documentación del modelo puede incluir:
-

Información cualitativa, como consideraciones éticas, usuarios objetivo y casos de uso;
- Información cuantitativa, que consiste en una evaluación desagregada del modelo
(dividida en los diferentes subgrupos objetivo) e interseccional (incluida la evaluación de múltiples subgrupos en combinación, por ejemplo, raza + género).
- Información de datos, si es posible, que podría formalizarse como una herramienta
de transparencia de datos.
La utilidad y precisión de una herramienta de transparencia depende de la integridad del creador o creadores de la propia herramienta y pueden almacenarse como documentación o metadatos asociados con cada modelo.

69
