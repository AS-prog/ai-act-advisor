---
name: aesia-15-guia-documentacion-tecnica-07-documentacion-tecnica-parte-2
description: "AESIA: aesia 15 guia documentacion tecnica, sección «Documentación técnica (parte 2)» (págs. 33-40). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-15-guia-documentacion-tecnica
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Documentación técnica (parte 2)"
  paginas: 33-40
  origen: 2026-07-17-aesia-15-guia-documentacion-tecnica.pdf
  oficial: false
---
# Documentación técnica (parte 2)

Instrucciones de uso generales, están dirigidas al responsable del despliegue del sistema.
En cada guía proporcionada acompañando a ésta, relativas a los requisitos para cumplir con los requisitos del capítulo III sección 2, se indica detallada y puntualmente como generar las instrucciones. Es importante que, aunque en este apartado puede parecer que es redundante con otros de la propia documentación técnica, aquí nos referimos a las instrucciones del sistema de IA para el responsable del despliegue es importante recordar en este punto que el Reglamento Europeo de la IA el responsable del despliegue es considerado la empresa o institución que lo utiliza y no el usuario final u operador, por ello las instrucciones del sistema tienen que tener en consideración este aspecto de alto nivel y abordándolo de manera vertical, para que desde el responsable del despliegue (según el Reglamento Europeo de la
IA) hasta el usuario final u operador, tengan el alcance necesario en las instrucciones.
Considerando que se deben indicar las instrucciones de cada guía para su ámbito de aplicación, estas instrucciones deben contener al menos:
✓ La clara indicación de que se trata de un sistema de inteligencia artificial.
✓ Información de cómo interpretar los resultados, acompañadas con ejemplos de usos y resultados.
✓ Una descripción del nivel de supervisión humana del sistema, y de cómo se espera que ésta se realice, acorde a lo descrito en la guía de supervisión. Las instrucciones incluirán todos los aspectos relacionados con este aspecto de aplicación al responsable del despliegue en el uso del sistema de IA.
✓ Dependiendo del nivel de supervisión humana del que disponga el sistema, explicación del mecanismo de anulación de la decisión del sistema o de la intervención de este.
✓ Información adecuada para el responsable del despliegue, acorde a las métricas descritas en la guía de precisión.
✓ Relativo a transparencia del sistema de IA, debe contener información de los casos de uso acorde a la finalidad prevista, y aquellos casos de uso potenciales no recomendados indicando usos indebidos razonablemente previsibles. En cuanto a su funcionamiento, deberá incluir: rendimiento y precisión del sistema, sesgos, la posibilidad de ataques al sistema de IA y una descripción de los datos utilizados.
✓ Relativo a transparencia del sistema de IA, debe contener información sobre la configuración de los datos de entrenamiento del sistema cuando los haya, así como de los datos de validación. Si el sistema está basado en conocimiento, aportar información sobre las hipótesis de aplicabilidad.
✓ Información sobre cómo interpretar los archivos de registro y eventos del sistema de
IA.
✓ Información de aplicación al responsable del despliegue sobre el análisis de riesgos en lo relativo a los potenciales daños y beneficios, especialmente aplicable a ciertos grupos demográficos, si entran dentro del dominio de aplicación.
✓ Información acerca de los posibles sesgos en el sistema y sus riesgos.
✓ En cualquier escenario la documentación debe estar versionada y actualizada respecto de la versión propia del sistema de IA al que haga referencia.
Si el sistema tiene una interfaz de usuario se debe añadir a las instrucciones generales:

32

✓ La descripción de cómo se interactúa con el sistema, con una descripción de los elementos de la interfaz y con sus funcionalidades. Si aplica, una descripción de cómo gestionar los papeles/niveles de usuario y como estos actúan sobre el sistema.
✓ Relación entre los elementos de la interfaz y la finalidad prevista del sistema, con una clara interpretación de la información.
✓ Indicar en cuantos idiomas se encuentra disponible la interfaz y el número de idiomas con los que puede operar el sistema.
✓ Indicar, si así se ha implementado, el nivel de accesibilidad del sistema de tal manera que la interfaz, si así lo requiere, sea inclusivo con minorías con diversidad funcional.
✓ Descripción detallada sobre cómo obtener desde la propia interfaz de usuario las ayudas necesarias para poder interactuar correcta y satisfactoriamente con el sistema.
Instrucciones de uso para productos cubiertos por el Anexo I apartado A. Dado que dichos productos ya disponen de sus legislaciones armonizadas específicas (indicadas en el Anexo I
A) las instrucciones de uso ya establecidas deben ampliar para añadir e incluir los aspectos generales descritos.
Instrucciones de instalación; aplicable a los sistemas de inteligencia artificial dependiendo de su forma de comercialización, instalable y/o configurables por el responsable del despliegue en sus sistemas (on-premise, in-house, in-cloud o edge-computing, por ejemplo)
✓ Las indicaciones del sistema hardware requerido para la ejecución del sistema en relación con sus volumetrías, tal y como se ha descrito para el apartado (e) de esta misma sección.
✓ Las indicaciones de los componentes software requeridos para la ejecución del sistema.
✓ En el caso de disponer de entornos de producción, desarrollo y/o pruebas del sistema de IA, la especificación de configuración de dichos entornos.
✓ Las indicaciones paso a paso de los procesos y mecanismos de instalación.
✓ Aquellas medidas de ciberseguridad relativas a IA aplicables al sistema, tal y como se ha descrito en la guía de ciberseguridad, a considerar en el proceso de instalación, aplicable al responsable del despliegue.
✓ Información sobre la implementación y mecanismo de configuración de registros del sistema tal y como se ha indicado en la guía de registros, requerida en el proceso de instalación.
✓ Información de aplicación al responsable del despliegue, para la gestión de guardado de registros en relación con las indicaciones de la guía de registros).

Ejemplo - Sistema automático de concesión de ayudas
El proveedor ha destinado un área específica de la Wiki del sistema de IA de tal manera que las instrucciones para el usuario final se encuentran integradas en ella. Para que estas instrucciones tengan más efecto, ha decidido involucrar al departamento de UX user experience, para facilitar la compresión y manejo de éstas. Fruto de esa colaboración, deciden añadir un proceso guiado paso a paso para facilitar la instalación. Para las instrucciones de la parte de interfaz, se ha añadido una serie de vídeos explicativos.

33

5.2 Descripción detallada de los elementos y procesos del sistema de
IA
El párrafo 2 del Anexo IV proporciona una lista de aspectos que deben ser cubiertos en detalle.
Este apartado de la documentación técnica requiere un detalle más amplio que la sección anterior. En este apartado la relación con el contenido ya descrito en otras guías es más directo, y será en esta sección donde se recomienda incluir la documentación que cada guía ha definido.

AI Act
Anexo IV.2 – Documentación técnica a que se refiere el artículo 11, apartado 1
(a) los métodos y las medidas adoptados para el desarrollo del sistema de IA, incluido, en su caso, el recurso a sistemas o herramientas previamente entrenados facilitados por terceros y la manera en que han sido utilizados, integrados o modificados por el proveedor;

Metodología en el proceso de desarrollo.
Existe amplia literatura para las metodologías existentes en el campo del desarrollo de sistema de inteligencia artificial (por ejemplo, Machine Learning, representación lógica y conocimiento, modelos estadísticos, etc. recogidos en el artículo 3.1 del Reglamento Europeo de la IA). Conviene que la documentación recoja la adecuación de la metodología seleccionada a la finalidad prevista del sistema de IA y su naturaleza.
La documentación técnica deberá contener, al menos:
✓ Una descripción del proceso de selección de la aproximación de IA o selección del modelo, y en su caso el formato de aprendizaje utilizado, por ejemplo, supervisado o no supervisado.
✓ La descripción detallada de la arquitectura empleada en el modelo seleccionado para el sistema de IA, con todos los elementos necesarios para su descripción y detalle, que depende de los diferentes tipos de modelo posibles.
✓ Una descripción detallada de los pasos realizados durante el desarrollo del software que implementa el sistema de IA, comenzando por la decisión del modelo tecnológico (desarrollo sobre plataformas existentes, MLOps, desarrollo propio…) indicando las etapas de diseño, los procesos de selección y la metodología general de desarrollo utilizada (iterativo/secuencial; y, si procede, el marco aplicado) con el objetivo de validar los controles aplicados durante el desarrollo.
✓ Una descripción detallada de como el modelo va a ser entrenado para alcanzar las métricas de solidez y precisión establecidas; en el caso de los sistemas de IA basados en ML, describir
34

las condiciones de entrenamiento del sistema y cómo se garantizan las métricas establecidas.
✓ Detalle del proceso de refinamiento de modelo, y su relación con los experimentos realizados.
✓ Una enumeración de los experimentos realizados, y los criterios de validación de dichos experimentos y su impacto en la elección del modelo. En este apartado se detallará la relación de ensayos y metodología, pues el detalle de las pruebas se realizará en la sección (d) más adelante en este apartado.
✓ Una descripción de cómo se establecen los criterios de versionado de los modelos, para su control y seguimiento.
✓ Relativo a los datos, añadir en la documentación técnica, una descripción resumida de la configuración de los datos originales y de los datos ya tratados y preparados para el análisis, la descripción de los mecanismos de tratamiento de los datos dentro del proceso de desarrollo. Así se debe establecer un mecanismo de versionado de los datos y éste se debe reflejar en la documentación técnica.
✓ Igualmente, relativo a los datos, una descripción de la tipología y forma de construcción de los datos de entrenamiento, y las consideraciones de diseño que estén relacionadas con los datos utilizados para el entrenamiento del sistema.
Sistemas pre-entrenados por terceros. Para reflejar como se han utilizado e integrado por parte del proveedor, la documentación técnica debe contener:
✓ Si el sistema de IA utiliza modelo(s) pre-entrenado(s); la motivación de la selección de dichos modelos, las ventajas que aportan estos en el proceso de desarrollo y las medidas tomadas para mitigar sus inconvenientes o riesgos. Esto se aplicará independientemente del nivel de preentrenamiento de dichos modelos.
✓ Si el sistema de IA utiliza un modelo sin pre-entrenar, pero cuya tecnología base es desarrollada por un tercero, se aplicará el mismo criterio que el punto anterior.
✓ En ambos casos se debe indicar la versión del sistema pre-entrenado, una referencia a la documentación de este y la indicación de si el proveedor de dicho sistema lo ha desarrollado siguiendo las directrices de un sistema de IA alto riesgo, o con la posibilidad de ser utilizado para implementar un sistema de IA de alto riesgo.
✓ Cualquier modificación o adaptación deberá detallarse, indicando su motivación en relación con la finalidad prevista del sistema de IA.

AI Act
Anexo IV.2 – Documentación técnica a que se refiere el artículo 11, apartado 1
(b.1) las especificaciones de diseño del sistema, a saber, la lógica general del sistema de IA y de los algoritmos; las decisiones clave de diseño, incluidos la lógica y los supuestos de los que se ha partido, también con respecto a las personas o colectivos de personas en relación con los que está previsto que se utilice el sistema;

35

Especificaciones de diseño del sistema. La documentación técnica en este apartado debería relacionar la finalidad prevista del sistema de IA, descrita previamente, con las especificaciones de diseño, de tal manera que la finalidad, sirva de motivación para el establecimiento de las especificaciones. Se recomienda detallar como mínimo:
✓ Relacionar las especificaciones del sistema con la finalidad prevista.
✓ Indicar la selección de métricas, tal y como se establece en las guías de precisión y solidez utilizadas para establecer las especificaciones del sistema, indicando su motivación y los rangos asociados.
✓ El tiempo de procesado esperado en el diseño del sistema, y si este procesa en tiempo real, en un intervalo de tiempo definido como tiempo de respuesta, o si el sistema realiza un post procesado de los datos.
Fundamentos y suposiciones en relación con las personas o grupos de personas. En este apartado se recomienda reflejar al menos:
✓ Suposiciones sobre el dominio de los datos de entrada y la relación de dichas hipótesis con las decisiones de diseño del sistema. Por ejemplo, en el caso de uso de sistema de promoción de empleados, en los datos de entrada no cuantitativos, se establece la hipótesis de un análisis de bag of words que incluye una lista de palabras positivas
(bien, correcto, eficiente etc.), con sus frecuencias estadísticas, para asignarles valores que serán utilizados después en el proceso.
✓ Si los datos que va a utilizar como datos de entrada el sistema de IA, son de personas físicas, detallar las suposiciones relacionadas a dichos grupos, y explicar su relación con la finalidad prevista.
✓ En lo relacionado a la supervisión humana. Se detallarán aquellas suposiciones consideradas en el diseño de la operación del sistema, de su interfaz de supervisión humana y de la interacción sistema IA / Humano.

AI Act
Anexo IV.2 – Documentación técnica a que se refiere el artículo 11, apartado 1
(b.2) […] las principales decisiones de clasificación;

✓ Para los sistemas que clasifican en categorías discretas, una descripción detallada de las diferentes categorías de clasificación y su relación con la finalidad prevista.
✓ En caso de que el sistema propiamente no establezca una clasificación, si no que realice una interpolación, estimación o cualquier otra operación sobre una variable continua, el rango de los valores de entrada y salida del sistema, y su relación con la finalidad prevista.
✓ Si el sistema no se encuentra en ninguno de los dos casos anteriores, conviene indicarlo en esta sección de la documentación técnica. Detallando el dominio y contexto esperado de respuesta de éste. Por ejemplo, en un sistema conversacional destinado a guiar en la adaptación curricular de la formación de un alumno de secundaria, indicar
36

que éste ha sido entrenado para las materias de matemáticas y ciencias, pero no para las correspondientes a lengua e historia, por lo que se espera que las respuestas en esas áreas o no sean precisas o no se puedan proporcionar.

37

AI Act
Anexo IV – Documentación técnica a que se refiere el artículo 11, apartado 1
(b.3) […] aquello que el sistema está diseñado para optimizar y la pertinencia de los diversos parámetros;
En aquellos casos en los que el sistema realice una optimización, en este apartado recomienda relacionar la finalidad prevista ya descrita con el objetivo de la optimización. Conviene considerar para establecer la relación, por tanto, entre:
✓ El tipo de modelo utilizado (ML, estadístico, etc.), con un detalle de bajo nivel de la arquitectura asociada del modelo utilizado en el sistema de IA.
✓ La variante del modelo utilizado (por ejemplo, en ML supervisado vs. no supervisado, u otras posibilidades como aprendizaje reforzado, aprendizaje profundo…), desarrollando un diagrama que indique como interacciona este con todas las entradas y salidas y demás elementos del propio sistema de IA en su conjunto.
✓ Todos los parámetros del sistema, en relación con el modelo utilizado. Para cada parámetro se debería describir su importancia y la relación de éste con el objetivo de optimización.
Por ejemplo, en un sistema de IA que controla una bomba de insulina para establecer el valor óptimo para proporcionar al paciente, indicar que se ha utilizado un modelo supervisado, basado en una RNN para predecir tendencias temporales, y que se han seleccionado los parámetros de tensión arterial, pulso y azúcar en sangre por ser los más significativos respecto a las necesidades inmediatas del paciente, descartando saturación de oxígeno en sangre por su dificultad de medición e imprecisión.

AI Act
Anexo IV – Documentación técnica a que se refiere el artículo 11, apartado 1
(b.4) […] la descripción de los resultados de salida esperados del sistema y la calidad de dichos resultados; las decisiones adoptadas acerca de cualquier posible concesión con respecto a las soluciones técnicas adoptadas para dar cumplimiento a los requisitos establecidos en el capítulo III, sección 2;

El Reglamento Europeo de IA establece en el capítulo III sección 2 una serie de requisitos que requieren la aplicación de unas medidas técnicas específicas, descritas y explicadas a lo largo de todas las guías de este sandbox.
En ocasiones, la implementación de una solución técnica puede implicar establecer una compensación (o trade-off) entre posibles aproximaciones, por la imposibilidad de satisfacer
38

de manera absoluta todas las posibilidades. En el caso de que durante el diseño del sistema se haya tomado alguna decisión de compensación entre algunos de los aspectos descritos en el capítulo III, dicha compensación se documentará indicando:
✓ Aspectos implicados en la compensación, relacionados con los artículos implicados, y estas guías.
✓ Motivo de la necesidad de realizar compensación.
✓ Descripción funcional de la compensación.
✓ Descripción técnica de la compensación.
✓ Consecuencias de aplicar la compensación y su relación con la finalidad prevista.

Ejemplo - Sistema automático de concesión de ayudas
Por ejemplo, en este sistema de IA el proveedor ha indicado en el análisis de riesgos del sistema, el riesgo de excluir una unidad familiar de las ayudas por un falso negativo (en definitiva, por error), y las consecuencias que para la familia tendría. Para mitigar ese riesgo, en la fase de diseño del sistema de IA, y durante la definición de las métricas de precisión, se decide que el sistema aumente ligeramente su tasa de falsos positivos, para excluir el citado riesgo. El proveedor documenta dicho ajuste (o trade-off), acorde a los puntos anteriormente indicados y lo refleja en la documentación técnica.

AI Act
Anexo IV.2 – Documentación técnica a que se refiere el artículo 11, apartado 1
(c) la arquitectura del sistema, con una explicación de la manera en que los componentes del software se utilizan o enriquecen mutuamente y de la manera en que se integran en el procesamiento general; los recursos informáticos utilizados para desarrollar, entrenar, probar y validar el sistema de IA;

Para la descripción de la arquitectura del sistema a nivel de componentes, el diseño de la aplicación y por tanto su arquitectura de componentes software, se puede documentar utilizando:
✓ En sistema de modelado de componentes por capas de complejidad, por ejemplo, se propone la utilización del sistema C4, donde los componentes se describen de alto a bajo nivel de manera progresiva identificando artefactos, sistemas y actores.
✓ Utilizar el diseño y modelado UML para el último nivel de arquitectura de componentes, en el que se describan a bajo nivel los componentes software y sus secuencias de interacción.
Para la arquitectura del sistema a nivel de recursos informáticos se puede detallar:
✓ La arquitectura de servidores/equipos implicada, las bases de datos y la interconexión de red entre los mismos. Si existe una arquitectura de contenedores desplegada sobre
39
