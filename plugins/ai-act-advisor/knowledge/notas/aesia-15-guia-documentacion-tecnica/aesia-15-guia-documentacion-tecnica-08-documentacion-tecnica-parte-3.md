---
name: aesia-15-guia-documentacion-tecnica-08-documentacion-tecnica-parte-3
description: "AESIA: aesia 15 guia documentacion tecnica, sección «Documentación técnica (parte 3)» (págs. 41-48). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-15-guia-documentacion-tecnica
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Documentación técnica (parte 3)"
  paginas: 41-48
  origen: 2026-07-17-aesia-15-guia-documentacion-tecnica.pdf
  oficial: false
---
# Documentación técnica (parte 3)

la citada arquitectura hardware, detallar y explicar cómo arquitectura de contenedores se relaciona con la arquitectura física.
✓ Descripción utilizando esa arquitectura de los entornos de desarrollo, integración y producción. Se indicará si estos sistemas están aislados entre sí, y los mecanismos de arquitectura relacionados con MLOPS.
✓ En cualquiera de los niveles en los que se describa la arquitectura hardware, se recomienda relacionar con lo reflejado en la sección (e) del apartado 5.1.
✓ Si se trata de un sistema de IA embebido o que es en sí mismo un producto o que es componente de seguridad de un producto cubierto por Anexo I A, conviene describir los recursos informáticos de emulación del entorno final del sistema.
Una referencia de normativa para la descripción de la arquitectura del sistema donde se desarrollan conceptualmente aspectos propios de esta y que puede ser consultada para su aplicación, ISO/IEC 5392 Information Technology — Artificial Intelligence — Reference
Architecture of Knowledge Engineering. 6.3.1 Functional architecture of KE.

AI Act
Anexo IV.2 – Documentación técnica a que se refiere el artículo 11, apartado 1
(d.1) cuando proceda, los requisitos en materia de datos, en forma de fichas técnicas que describan las metodologías y técnicas de entrenamiento, así como los conjuntos de datos de entrenamiento utilizados, e incluyan una descripción general de dichos conjuntos de datos e información acerca de su procedencia, su alcance y sus características principales;

La información solicitada en el apartado es bastante autodescriptiva. Los datos utilizados para el entrenamiento, prueba y validación tienen que estar claramente descritos, siguiendo las directrices de la guía de datos y gobierno del dato, que da cobertura al artículo 10, datos y gobernanza de datos, del Reglamento Europeo de IA.
Los conjuntos de datos se distinguirán entre sí por referirse a dominios diferentes de aplicación según la finalidad prevista. Cada conjunto de datos debería tener una ficha descriptiva donde se detalle:
-

La metodología planteada, como ejemplo, utilizada para la formación de los datos.
- Descripción general de los mismos. Aclarando las etiquetas internas de
representación de los datos y asociándolas a su significado real (por ejemplo, las columnas etiquetadas como EDAD podría responder a la edad de un paciente, o a la edad en la que se contrae una enfermedad.
- Identificar si se han utilizado técnicas de ampliación o técnicas de añadido de ruido,
en ese caso cuáles. Indicar como es la representación interna de los datos faltantes, para poderlos identificar e interpretar correctamente los datos faltantes.

40

-

El dominio de los datos conviene ser descrito adecuadamente, identificando los intervalos de pertenencia y rangos para los datos. Aquellos datos discretos o pertenecientes a categorías, establecer y describir las categorías de estos.

AI Act
Anexo IV.2 – Documentación técnica a que se refiere el artículo 11, apartado 1
(d.2) […] la manera en que se obtuvieron y seleccionaron los datos; los procedimientos de etiquetado (p. ej., para el aprendizaje supervisado) y las metodologías de depuración de datos (p. ej., la detección de anomalías);

Para completar la información detallada sobre los datos, se deben añadir en la ficha de la documentación:
✓ La procedencia de los datos debe registrarse indicando si estos se han obtenido de fuentes públicas, de acuerdos con terceros, o recogidos por los sistemas de la propia empresa. Si esos datos siguieron respecto de la fuente original un proceso de selección, deberá indicarse como se ha realizado y si este afecta a categorías o al dominio que los datos pudieran tener.
✓ Para los aprendizajes supervisados, se debe describir la técnica utilizada para su etiquetado y categorización, identificando el proceso que se ha seguido para etiquetar los datos y relacionarlo con las categorías descritas previamente en la documentación técnica.
✓ En los casos en los que los datos son preprocesados para aumentar distribución y hacer el entrenamiento del modelo más robusto, se debe detallar en la ficha el procedimiento de aumentado de los datos y su relación con la finalidad prevista y con las especificaciones de diseño del sistema de IA.
✓ Especificar y describir con detalle todas las hipótesis que se han realizado para poder pretratar y depurar los datos antes del análisis y comparar las características de los datos originales con las de los datos preprocesados.
✓ En lo relativo a al preprocesamiento de los datos es necesario cubrir como mínimo, en los casos en los que se realice:
o Tratamiento de datos faltantes.
o Impacto del tratamiento de los datos faltantes en la distribución de los datos de entrada o Identificación, diagnóstico y tratamiento de valores atípicos.
o Transformación de variables y variables derivadas.
✓ En los casos en los que los datos puedan contener valores atípicos, el procedimiento para cada uno de los conjuntos de datos de eliminación utilizado tiene que estar detallado y explicado, indicando la razón de su eliminación del conjunto de datos y presentando un ejemplar de muestra de los datos eliminados.

41

En la guía de gobierno del dato, relativa al artículo 10, datos y gobernanza de datos, se hace referencia a maneras adicionales de documentar los datos y su categorización, debe completarse la información en esta sección, con lo descrito en dicha guía.

AI Act
Anexo IV.2 – Documentación técnica a que se refiere el artículo 11, apartado 1
(e) una evaluación de las medidas de supervisión humana necesarias de conformidad con el artículo 14, incluida una evaluación de las medidas técnicas necesarias para facilitar la interpretación de los resultados de salida de los sistemas de IA por parte de los responsables del despliegue, con arreglo al artículo 13, apartado 3, letra d);

En la guía de supervisión humana (artículo 14, supervisión humana) y la guía de transparencia
(artículo 13, transparencia y comunicación de información a los responsables del despliegue)
de este sandbox, se han dado una serie de medidas técnicas orientativas para alcanzar los requisitos solicitados por el Reglamento Europeo de IA. La documentación de las medidas técnicas generada en el cumplimiento de dichas guías podrá incluirse en esta sección.
La documentación presentada deberá indicar, al menos:
✓ Descripción de las medidas técnicas de manera funcional.
✓ Un detalle de la experiencia de usuario, indicando como esta informa de los resultados.
✓ Los mecanismos visuales, sonoros, de avisos o cualquier otra naturaleza que puedan ayudar a interpretar los resultados proporcionados por dicha interfaz y sus rangos de funcionamiento.
✓ Las medidas técnicas dispuestas en la interfaz del sistema, y en su operativa, destinadas a cumplir los requerimientos de transparencia.
Los aspectos aquí descritos relativos a la documentación de la supervisión humana son exclusivamente técnicos (dado el alcance de la presente guía) y no representan el total de medidas aplicables que en su caso estarán descritos en la guía de supervisión humana correspondiente y deberán ser aplicados en el alcance descrito, para cubrir los requisitos del
Reglamento Europeo de IA.

AI Act
Anexo IV.2 – Documentación técnica a que se refiere el artículo 11, apartado 1
(f) en su caso, una descripción detallada de los cambios predeterminados en el sistema de IA y su funcionamiento, junto con toda la información pertinente relativa a las soluciones técnicas adoptadas con el objetivo de garantizar la
42

conformidad permanente del sistema de IA con los requisitos pertinentes establecidos en el capítulo III, sección 2;

A lo largo del ciclo de vida, el sistema de IA tendrá actualizaciones programadas destinadas a proporcionar mejoras, a actualizar recursos o a solventar problemas que hayan podido producirse. En cualquiera de los casos, esas mejoras conviene reflejarlas en la documentación.
Es importante tener en cuenta que cada una de las mejoras, debe replicar, en aquellos apartados de la documentación técnica que le sean de aplicación, lo explicado en esta guía para todo el sistema de IA.
La información debería contener, mínimo:
✓ Una fecha del cambio y de su entrada en operación del sistema.
✓ La identificación de la versión del sistema.
✓ Una descripción de la motivación del cambio o cambios implementados, a modo de registro de cambios evolutivo.
✓ Registro de los cambios sobre el sistema de IA realizados en la actualización
✓ Se recomienda que la documentación de actualización sea autocontenida con relación a toda la documentación del sistema, referenciando en los ámbitos en los que sea aplicable, los apartados aquí descritos en esta guía.
✓ Descripción de los resultados de las pruebas de validación y su comparación pre-post cambio/actualización, no solo en términos de precisión de los modelos, sino también en términos de costes de computación o volúmenes de datos.

43

Ejemplo – Sistema de promoción de empleados
Durante el uso del sistema, dos grandes compañías (seguros y banca), usuarios del sistema de IA, han indicado que es necesario mejorar el tiempo que tarda el sistema de IA en analizar los datos, dado que ambas tienen un gran volumen de empleados y varios periodos de promoción a lo largo del año, por lo que los tiempos de respuesta son esenciales.
Para ello se elaboran unas nuevas especificaciones de tiempo de respuesta, que son remitidas al equipo de diseño e implementación del sistema de IA.
La actuación supone una mejora en los tiempos de respuesta del sistema que ha requerido diversas actuaciones en diferentes partes del sistema; Se elabora una ficha de la actualización cubriendo los puntos descritos en este apartado (f). La ficha contiene la siguiente información:
-
-

-

-

La fecha en la que el cambio se ha realizado, cuando entra en efecto, así como la versión del sistema de IA que la incluye.
Se recoge la información proporcionada por los usuarios de sistema sobre la necesidad de la mejora, con sus comentarios y la necesidad de que este tiempo sea más corto para agilizar sus procesos de evaluación.
Se recoge un registro de todos los cambios realizados para alcanzar los objetivos descritos en el punto anterior. Es este caso se recogen los siguientes cambios.
- Actualización de librerías específicas, a versiones que permiten el cómputo
en paralelo.
- Ajustes en la arquitectura de componentes para soportar el cálculo en
paralelo de manera adecuada.
- Modificaciones en la interfaz donde se indica el tiempo de procesado de un
empleado individual.
La documentación técnica se ha adaptado también para reflejar dichos cambios, por lo que en esta ficha de actualización indica los apartados de la documentación modificados y un resumen del motivo de su modificación:
- En la descripción general (ver 5.1) se ha modificado el apartado (c) para
indicar las nuevas librerías utilizadas.
- En las especificaciones generales (ver 5.1) en el apartado (g), se han
modificado las instrucciones de uso, para reflejar la información del cambio en la interfaz.
- En la descripción detallada (ver 5.2) apartado (c) se actualiza el diagrama de
interacción de componentes para reflejar la adaptación al procesado en paralelo.
- En la descripción detallada (ver 5.2) apartado (g) los procesos de validación
y prueba se han ajustado para incluir la verificación del tiempo de procesado, así como utilizar como un parámetro adicional de solidez el tiempo de procesado.

Es importante tener en cuenta que este tipo de cambios obligan a mantener una relación entre la versión del sistema de IA y la propia documentación, como se ha indicado en el apartado 5.1.
44

AI Act
Anexo IV.2 – Documentación técnica a que se refiere el artículo 11, apartado 1
(g.1) los procedimientos de validación y prueba utilizados, incluida la información acerca de los datos de validación y prueba empleados y sus características principales;

Se deberá describir los procedimientos de validación utilizados durante el diseño del sistema, para considerar que este alcanza en el proceso la finalidad prevista. No se deben confundir los ensayos (pruebas), únicamente con la evaluación del modelo en relación con otros parámetros propios (por ejemplo, solidez, precisión o ciberseguridad).
La documentación debe dejar constancia de la metodología de pruebas considerando el sistema de IA como artefacto software:
✓ Descripción del alcance de las pruebas unitarias, tanto del modelo propiamente dicho como de los elementos relacionados con éste y que formen parte integrante del sistema de inteligencia artificial y puedan afectar a su finalidad prevista, su precisión y solidez; independientemente de que seas piezas de IA/ML, por ejemplo: si existe un proceso de preprocesado de los datos antes de ser introducidos al sistema las pruebas unitarias del mismo, indicando el porcentaje de cobertura de código.
✓ Las pruebas de integración realizadas entre los diferentes componentes que conforman el sistema de IA, incluyendo el modelo y la interacción de éste con las partes.
✓ Metodología utilizada para las pruebas sobre la interfaz del sistema destinada a la supervisión y/o interfaces de configuración que el sistema pueda tener.
Respecto a los datos de validación y ensayo utilizados para evaluar el modelo la documentación puede reflejar:
✓ La naturaleza de los datos y sus variables implicadas. Por ejemplo, si se trata de datos tabulados, las diferentes variables consideradas; si se tratase de datos en forma de imágenes o audios una descripción de sus características o duración.
✓ Indicación de las dimensiones del conjunto total de datos y del reparto de prueba, validación y ensayo.
✓ Registro de los cambios en el conjunto de datos desde su creación y a lo largo de la vida del sistema de IA, cuando éstos se modifiquen. Por ejemplo, se puede utilizar para los datos textuales una herramienta de control de versiones tipo Git.
✓ Las relaciones entre los ensayos y los cambios en el modelo que esto pudieran causar, y el valor obtenido en cada prueba de las métricas de precisión.
En algunos estándares que actualmente se encuentran en fase de desarrollo, se abordan estos aspectos desde un punto de vista formal y normativo, como puede ser ISO/IEC 17847
Information technology — Artificial intelligence — Verification and validation analysis of AI systems. Igualmente existen otros estándares ya consolidados, que podrían servir a modo de guía en la fase de Testing de un sistema basado en IA, como por ejemplo ISO/IEC TR 2911945

11:2020(en) Software and systems engineering — Software testing — Part 11: Guidelines on the testing of AI-based systems
(https://www.iso.org/standard/79016.html)

AI Act
Anexo IV.2 – Documentación técnica a que se refiere el artículo 11, apartado 1
(g.2) […] los parámetros utilizados para medir la precisión, la solidez y el cumplimiento de otros requisitos pertinentes establecidos en el capítulo III, sección 2
(h) las medidas de ciberseguridad adoptadas

En las guías correspondientes al artículo 15, relativo a precisión y solidez se definen una serie de métricas que permiten definir los rangos de trabajo del sistema y su comportamiento, dentro de la finalidad prevista. Las métricas seleccionadas, sus rangos establecidos y la motivación de estas debe estar reflejada en esta sección de la documentación, acompañados de la documentación generada indicada en aquellas guías.
La guía de ciberseguridad, también relativa al artículo 15, precisión, solidez y ciberseguridad, establece una serie de controles para mitigar los riesgos de un sistema de IA. En lo relativo a este aspecto, se debe reflejar en la documentación:
✓ El plan de ciberseguridad para IA establecido.
✓ Los activos y actores identificados.
✓ Las vulnerabilidades identificadas y los controles aplicados sobre los datos para los ataques de envenenamiento.
✓ Las vulnerabilidades identificadas y los controles aplicados para la protección frente a ataques adversarios.
✓ Vulnerabilidades y controles para la protección de ataques que utilicen los defectos del modelo.
El resto de las guías que acompañan el sandbox también establecen una serie de requisitos y definen métricas para asegurar su cumplimiento. En esta sección se recomienda reflejar dichas métricas. Con relación al resto de guías siempre que haya una medida técnica que disponga de una métrica para su seguimiento, podrá estar reflejado en esta sección.

46

AI Act
Anexo IV.2 – Documentación técnica a que se refiere el artículo 11, apartado 1
(g.3) […] así como los efectos potencialmente discriminatorios

En la guía de gobierno del dato se ha establecido que en el procesamiento de datos se debe realizar un examen "atendiendo a posibles sesgos que puedan afectar a la salud y la seguridad de personas o que conduzcan a una discriminación prohibida por el Derecho de la Unión". Al respecto, la documentación técnica debería contar con el resultado del análisis realizado, indicando especialmente las repercusiones discriminatorias que puedan aparecer, relacionadas con la finalidad prevista, indicando la métrica seleccionada. De acuerdo con la guía de Datos dichas métricas podrán ser:
✓
✓
✓
✓
✓
✓

Diferencias de paridad.
Impacto desigual.
Disparidad en los resultados.
Diferencia de rasgos indicadores en los valores predichos.
Diferencia de igualdad de oportunidades.
Diferencia de probabilidades media.

Acompañado de un análisis previo de los datos de entrenamiento a partir de los cuáles se construye el modelo, para poder poner en contexto los puntos indicados. Para este análisis de discriminación se recomienda valorar que tipos de datos recoger y si dicha recogida es viable en el marco de la finalidad prevista.
Igualmente, en la guía de precisión se indica que es necesario realizar ensayos para detectar posibles tipos de sesgos que pueda sufrir el sistema afectando a la precisión para categorías de datos que puedan resultar ser discriminadas, y cómo las mismas métricas provistas a nivel global de modelos para medir la precisión, no presentan impacto desigual o disparatado
(disparate impact) para diferentes grupos pertenecientes a variables sensibles. Este análisis desde el punto de vista de precisión del modelo, en relación con las repercusiones potencialmente discriminatorias, puede estar documentado en esta sección.
En cuanto al análisis de posibles sesgos y limpieza del algoritmo se recomienda los estándares normativos siguientes:
-
-

ISO/IEC TR 24027:2021, Information technology — Artificial intelligence (AI) — Bias in AI systems and AI aided decision making.
Y actualmente en desarrollo el relativo al tratamiento de sesgos no deseados
ISO/IEC AWI TS 12791 - Information technology — Artificial intelligence —
Treatment of unwanted bias in classification and regression machine learning tasks.

47
