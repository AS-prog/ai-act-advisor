---
name: aesia-08-guia-transparencia-08-medidas-aplicables-para-conseguir-transp
description: "AESIA: aesia 08 guia transparencia, sección «Medidas aplicables para conseguir Transparencia (parte 2)» (págs. 37-44). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-08-guia-transparencia
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Medidas aplicables para conseguir Transparencia (parte 2)"
  paginas: 37-44
  origen: 2026-07-17-aesia-08-guia-transparencia.pdf
  oficial: false
---
# Medidas aplicables para conseguir Transparencia (parte 2)

Ejemplo – Bomba de insulina
El sistema deberá ofrecer mecanismos que permitan a la entidad responsable del despliegue conocer:
- El criterio global seguido para la decisión de la dosis a administrar (detallado en el
ejemplo de la medida Atender al dominio de la funcionalidad).
- Composición de las dosis administradas, sobre un conjunto de pacientes con
características médicas similares (por ejemplo, sexo, edad, estado físico, patologías adicionales, etc.), permitiendo que los facultativos puedan comprobar que las decisiones son homogéneas en dicho conjunto en un orden de magnitud lógico desde un punto de vista médico.
- Decisiones tomadas sobre un paciente concreto, en base al criterio global de
funcionamiento del sistema.

5.6.

Adaptar el lenguaje

Como medida de carácter orientativo, puede resultar conveniente diseñar el sistema de IA de forma que pueda proporcionar información a todos los perfiles que interaccionan con él y así asegurar de manera transparente su completo entendimiento.
Son muchos los tipos de perfiles que pueden interaccionar con el sistema de IA a lo largo de todo su ciclo de vida. Por tanto, se pueden habilitar mecanismos técnicos que permitan mostrar dicha información de manera transparente y entendible por todos ellos, adecuando el tipo de lenguaje a su nivel de interlocución:
-

-

-

Los responsables del despliegue del sistema de IA necesitan entender mediante lenguaje natural, que las predicciones y decisiones que está proporcionando el sistema son homogéneas en usuarios finales con características similares, etc., con un enfoque orientado al objetivo de negocio del sistema.
Los técnicos del proveedor, cuyo lenguaje es técnico, cuando están construyendo el sistema de IA, necesitan poder explicar a los usuarios de la entidad responsable del despliegue, el razonamiento de sus modelos mediante un lenguaje entendible por éstos, y así asegurar entre ambos que el sistema cumple con el Reglamento Europeo de la IA y las políticas de la empresa. Y en toda la vida del sistema de IA deben conocer con un lenguaje técnico el razonamiento que está siguiendo dicho sistema para asegurar su correcto funcionamiento e incluso mejorar su precisión,
Las personas físicas o jurídicas afectadas por el funcionamiento del sistema de IA, que en muchas ocasiones no tiene porqué disponer de un lenguaje técnico de cualquier tipo, necesitan poder conocer, p.ej., los motivos por los cuales no se les ha concedido un producto o servicio y saber en qué condiciones se les concedería aplicadas a su realidad.

Para ello, además de los mecanismos técnicos necesarios para la implementación del sistema por parte de los especialistas, se propone para el resto de los perfiles, proporcionar una
36

interfaz de usuario que facilite la información de manera comprensible, ya sea visualmente, textualmente en lenguaje natural o por otros medios. En definitiva, un diseño de interfaz persona-sistema de IA de calidad para reforzar la transparencia de los sistemas de IA por parte de los responsables del despliegue y afectados sin conocimientos técnicos especializados.
A quién aplica
- El proveedor podrá proporcionar a los responsables del despliegue los
mecanismos técnicos e interfaces de usuario que faciliten esta necesidad y así asegurar el completo control y entendimiento del sistema bajo un lenguaje entendible por todos los actores que interactúan con él a lo largo de todo su ciclo de vida.
- El responsable del despliegue podrá usar estos elementos para cubrir las
necesidades de transparencia para su solución particular de negocio.
A qué apartados aplica esta medida
-
-

Apartado 1. Diseño y desarrollo
Apartado 3d. Vigilancia humana

Ejemplo - Concesión de ayudas
El sistema proporcionará una interfaz de usuario, alineada con el nivel de interlocución de cada uno de los perfiles que interactúa con él, y que facilite la siguiente información de manera entendible, visual y textualmente en lenguaje natural, sobre todo a aquellos perfiles no técnicos:
- Los gestores de la concesión de las ayudas deben recibir información del sistema, en
lenguaje natural, que les permita asegurar que está cumpliendo las políticas de concesión de ayudas, el grado de precisión que está teniendo a la hora de predecir las exclusiones sociales que finalmente se producen y que dan lugar a las ayudas, como la homogeneidad de las predicciones que está proporcionando en familias con características similares, detalles acerca de todas las predicciones y decisiones tomadas por el sistema de IA. Asimismo, los responsables de la concesión de ayudas dispondrán de cuadros de mando que les permita obtener estadísticas de los resultados.
- Los técnicos que implementan el sistema y se encargan de su monitorización mientras
está en funcionamiento, deben conocer la misma información anterior, pero desde una perspectiva técnica.
- A las familias solicitantes, el sistema deberá poder explicarles en lenguaje natural los
motivos por los cuales se les ha concedido un determinado importe y no otro, porqué se les ha denegado la solicitud y en qué condiciones aplicada a su realidad se le aceptaría, etc.

37

Ejemplo – Bomba de insulina
El sistema proporcionará una interfaz de usuario, alineada con el nivel de interlocución de cada uno de los perfiles que interactúa con el mismo, y que facilite la siguiente información de manera fácilmente entendible, visual y textualmente en lenguaje natural, sobre todo a aquellos perfiles no técnicos:
- Los facultativos responsables de la administración de las dosis sobre sus pacientes
deben recibir información del sistema, en lenguaje natural con el detalle técnico necesario desde un punto de vista médico, que les permita asegurar que las dosis suministradas están surtiendo el efecto correcto desde un punto de vista médico, atendiendo a los niveles de precisión deseados. También podrán disponer de cuadros de mando que les permita conocer la evolución del funcionamiento del sistema, así como la de los propios pacientes.
- Los técnicos de software que implementan el sistema y se encargan de su
monitorización mientras está en funcionamiento deben conocer la misma información anterior, pero desde una perspectiva técnica.
- A los pacientes, el sistema deberá poder explicarles en lenguaje natural las dosis que
están recibiendo, su efecto, etc., de la misma manera que se lo explicaría el facultativo en una de sus revisiones.

5.7.

Gestionar la complejidad

Entender el funcionamiento de sistemas de IA para así facilitar su transparencia puede implicar el análisis de cantidades ingentes de variables y operaciones matemáticas. Por tanto, un buen diseño del sistema entendido desde la simplicidad de este, puede ser clave para lograr una mayor transparencia, ya que en ocasiones se tiende a aumentar la complejidad del sistema de
IA para buscar más precisión, lo cual puede implicar la pérdida de transparencia acerca de su funcionamiento. Por tanto, es necesario medir el retorno de inversión de complicar el modelo por obtener un poco más de precisión a costa de posiblemente perder transparencia.
Es recomendable decidir en fase de diseño el modelo más sencillo que cumpla con los objetivos de negocio, simplificando así la transparencia y el entendimiento de su funcionamiento. Así es más fácil identificar qué factores afectan al sistema y poder explicarlo.
Además, esta simplicidad en el sistema redunda en un menor consumo energético, algo muy importante en estos sistemas de IA, cuya necesidad de computación implica un alto impacto medioambiental.
El siguiente gráfico representa la relación entre la complejidad técnica de algunos tipos de modelos inteligentes vs la sencillez para conseguir transparencia en los mismos.

38

La particularidad de los modelos de caja negra/caja blanca
A los sistemas de "caja blanca" se les suele llamar "transparentes", y son aquellos en los que es más sencillo entender su comportamiento. Ejemplos de este tipo de modelos son las regresiones lineales y los árboles de decisión. Por el contrario, los modelos de "caja negra” son aquellos en los que se conoce la entrada y salida, pero su funcionamiento interno es difícilmente comprensible incluso en ocasiones para los técnicos que la implementan.
Ejemplos de sistemas de “caja negra" son los bosques de decisión y las redes neuronales.
Los modelos de caja negra ofrecen una gran precisión y pueden solucionar casos de uso complejos, pero su transparencia puede ser limitada dada su complicada construcción. Su falta de transparencia puede implicar tener que descartarlos para recurrir a modelos de caja blanca, directamente interpretables. Esta decisión de diseño por parte del proveedor es especialmente relevante en aplicaciones de alto riesgo donde hay que asegurar que su funcionamiento no se degenera y donde la transparencia es una necesidad ineludible.
La transparencia en sistemas de caja negra es un reto sobre el que se está investigando.
Actualmente, una de las posibles soluciones para facilitar su transparencia (no al 100%) pasa por algoritmos (por ejemplo, profweight) que sondean el sistema analizando las entradas y salidas correspondientes que producen. Una vez analizados estos datos, se genera un sistema directamente interpretable equivalente que sirve para detallar el funcionamiento de la caja negra.
A quién aplica
-
-

Esta decisión de diseño aplica al proveedor del sistema de IA.
El responsable del despliegue podrá identificar si la complejidad del sistema que va a soportar su caso de uso puede llegar a ser bloqueante para las necesidades de transparencia sobre el sistema.

A qué apartados aplica esta medida
-
-
-

Apartado 1. Diseño y desarrollo
Apartado 3b.ii. Nivel de precisión
Apartado 3d. Vigilancia humana

39

Ejemplo – Concesión de ayudas y bomba de insulina
Se utilizarán árboles de decisión y regresiones lineales. Se descarta el uso de modelos probabilísticos bayesianos o redes neuronales, ya que la mejora de precisión con estos últimos podría no ser relevante, por ejemplo, en un caso de uso con alto factor probabilístico como el de la concesión de ayudas, mientras que por otro lado complicarían el objetivo de trasparencia del sistema.

5.8.

Utilizar métricas integradas en el ciclo de vida del sistema

Las métricas permiten monitorizar el nivel de precisión, solidez y ciberseguridad (referidas en las guías que detallan el Artículo 15 del reglamento). Dichas métricas pueden aplicar a datos y sistema. Desde el punto de vista formal las métricas empleadas en datos y modelo aparecen desarrolladas en el estándar [ISO/IEC 23053]. Su uso es necesario porque los sistemas de IA degradan su rendimiento con el tiempo debido, por ejemplo, a los nuevos datos de entrada recibidos por el sistema (data drift), o bien incluso debido a cambios en el mismo (model drift).
Por tanto, puede ser necesario:
-
-
-

Definir las métricas específicas a utilizar sobre los datos, el modelo, la calidad de los resultados y el rendimiento.
Validar dichas métricas en las pruebas finales antes de poner el sistema en funcionamiento.
Monitorizar el valor de dichas métricas durante su funcionamiento, especificando los valores mínimos aceptables a partir de los cuales es necesario, por ejemplo, reentrenar el sistema (cuando la degradación es por datos) o bien incluso parar su ejecución (por el motivo anterior y/o cuando la degradación es por un error de sistema).

Estas métricas deben estar asociadas a un sistema de integración continúa sobre el sistema y sus datos (MLOps), permitiendo el análisis de dichas métricas cada vez que se produce un cambio en el sistema y/o sus datos y así identificar el nivel de las métricas definidas para cada versión. Para ello es necesario atenerse al ciclo de vida del sistema definidos en los estándares
[ISO/IEC 22989] e [ISO/IEC 5338] (ver en Glosario la definición de Ciclo de Vida de un sistema de IA).
A quién aplica
-

-
-

El proveedor podrá proporcionar las herramientas necesarias para definir y monitorizar dichas métricas, tal y como se detalla en las guías que abarcan el Artículo 15 del reglamento.
El proveedor podrá incluir un sistema de integración continúa (MLOps) que permita identificar cómo afectan los cambios en las diferentes versiones del sistema.
El usuario, como responsable final del sistema en su explotación, podrá monitorizar dichas métricas siguiendo las recomendaciones proporcionadas en las guías que detallan el Artículo 15 del reglamento.

A qué apartados aplica esta medida
40

-
-
-
-
-

Apartado 1. Diseño y desarrollo
Apartado 3b.ii. Nivel de precisión
Apartado 3c. Cambios
Apartado 3d. Vigilancia humana
Apartado 3e. Recursos HW/SW y mantenimiento

Ejemplo – Bomba de insulina
Se utilizarán métricas de precisión que permitan, por ejemplo, comparar las reacciones de pacientes ante determinadas dosis.
Relacionado con la integración continúa, dichas métricas deberán ser especialmente monitorizadas, por ejemplo, al desplegar una nueva versión del sistema que incluya, por ejemplo, un nuevo medicamento o una nueva composición de este, o que incluya la medicación de grupos de personas con determinadas patologías adicionales anteriormente no contempladas. De esta manera, a partir de las mencionadas métricas, se garantizará de manera transparente que el sistema funciona conforme a las especificaciones esperadas.

Ejemplo – Concesión de ayudas
Se utilizarán métricas de precisión (especificadas en la guía de precisión, artículo 15) que permitan, por ejemplo, comparar las predicciones realizadas por el sistema sobre familias en riesgo de exclusión social que finalmente hayan derivado en dicha situación.
Relacionado con la integración continúa, dichas métricas deberán ser especialmente monitorizadas, por ejemplo, al desplegar una nueva versión del sistema que incluya a una nueva región geográfica (release de datos), o que incluya la ponderación de personas dependientes o con discapacidad dentro de la familia a la hora de predecir exclusiones sociales o conceder la ayuda (release de modelo). De esta manera, a partir de las mencionadas métricas, se garantizará de manera transparente que el sistema no realiza discriminación positiva o negativa por estos nuevos conceptos incluidos en dichas releases.

5.9.

Aplicar prudencia

La información proporcionada debería ser pertinente. Esto implica que, a modo orientativo, dicha información tiene que ser prudente, identificando los escenarios en los que la información proporcionada pueda no ser apropiada, al menos de manera pública si, por ejemplo:
-
-

Deriva en mayor confusión para los usuarios.
Puede ser aprovechadas por agentes externos para vulnerar la seguridad del sistema y/o degenerar su funcionamiento, sus procesos de aprendizaje y razonamiento. Esto es algo particular en los sistemas de IA respecto de los sistemas tradicionales, y es conocido como “ataques de envenenamiento”, concepto descrito con detalle en la guía correspondiente de ciberseguridad del artículo 15 del Reglamento Europeo de la IA.

41

-

Revelan información privada y confidencial, o bien sujeta a GDPR, que pueda ser apropiada por terceros de manera indebida.

A quién aplica
-

-

El responsable del despliegue, como propietario de la información, podrá identificar la información sensible que no deba ser proporcionada ya sea porque, por ejemplo, es información confidencial de sus clientes, o bien porque incluso revele información sensible del proceso de negocio soportado.
El proveedor podrá implementar los filtros pertinentes para que la información no sea revelada.

Ejemplo – Concesión de ayudas
El sistema proporciona a las familias una respuesta de aceptación/denegación de la ayuda a través del canal web online, con argumentos que la soportan. Dichos argumentos no deben incluir, por ejemplo, información económica detallada de toda la familia, ya que parte de dicha información puede ser privada de manera individual.

Ejemplo – Bomba de insulina
El sistema proporciona a los pacientes un seguimiento de las dosis pasadas e inmediatas a través de una app móvil. En caso de variación en la dosis, se le explicará al paciente de manera sencilla para asegurar su entendimiento, estando dicha información segurizada para evitar accesos a información confidencial por parte de terceros.

A qué apartados aplica esta medida
-
-

Apartado 1. Diseño y desarrollo
Apartado 3d. Vigilancia humana

5.10.

Usar causalidad, minimizar correlaciones

La correlación no implica causalidad, ya que dos variables pueden tener una alta correlación, pero pueden no ser a causa de la otra. Un sencillo ejemplo de estos conceptos es usar directamente la estatura y no la edad para predecir si es seguro físicamente para un niño subirse a una montaña rusa. Con la estatura estaríamos utilizando una causalidad directa, mientras que con la edad estaríamos utilizando una correlación teórica que, de no cumplirse, podría producir accidentes.
La correlación puede complicar la transparencia del sistema de IA y su nivel de precisión, ya que hay que tener en cuenta la gran cantidad de variables que manejan estos sistemas, y las muchas relaciones explícitas e implícitas que pueden existir entre las mismas. El análisis de los datos puede ayudar a identificar dichas correlaciones, tal y como se detalla en la medida para la transparencia de los datos reflejada en el presente documento.

42

Además, la correlación puede depender de la subjetividad de quien diseña e implementa las reglas de correlación que considere además de no contemplar posibles escenarios no habituales pero relevantes en el sistema de IA. Es por tanto una potencial fuente de sesgo, y como consecuencia un riesgo en la correcta aplicación del principio de equidad.
A quién aplica
-

-

Al definir los requisitos, el responsable del despliegue podrá identificar las correlaciones válidas, así como las explícitamente no deseadas, ya que es el conocedor de la información gestionada por el sistema de IA desde una perspectiva de negocio.
El proveedor podrá tener identificado con detalle el modo en el que se han implementado las correlaciones, así como su impacto en la precisión del sistema.

Ejemplo – Concesión de ayudas
Se analizarán los datos de las fuentes disponibles tal y como se indica en la medida transparencia sobre los datos utilizados de este documento, ya que la asignación considera muchas variables y existen relaciones entre las mismas.
Por ejemplo, para la asignación de la ayuda, una de las variables utilizadas es el número de miembros de la unidad familiar. Erróneamente se puede establecer una correlación directa entre el número de miembros de la familia y la necesidad y/o el importe de la ayuda. Habrá que tener en cuenta que dicha variable deberá ser ponderada con otras variables de dichos miembros como, por ejemplo, su edad (por ejemplo, los menores de edad no tienen capacidad para aportar ingresos a la familia), o la posible pertenencia de alguno de ellos a grupos de personas dependientes (por ejemplo, una familia con un solo hijo siendo este dependiente puede tener mayor necesidad que otra familia con tres hijos sin dicha dependencia).

Ejemplo – Bomba de insulina
En el diseño del sistema será necesario analizar los datos de las fuentes disponibles tal y como se indica en la medida transparencia sobre los datos utilizados de este documento, dado que la decisión acerca de la dosis a aplicar puede tener muchas variables a considerar y existen relaciones entre las mismas.
Por ejemplo, una de las variables utilizadas es la edad del paciente. Erróneamente se puede establecer una correlación directa entre el nivel de azúcar en sangre y el volumen de la dosis. En el diseño de la solución y su documentación asociada habrá que tener en cuenta que dicha variable deberá ser ponderada con otras variables como la edad, el sexo, su actividad física, etc.

A qué apartados aplica esta medida
-
-
-

Apartado 1. Diseño y desarrollo
Apartado 3b.ii. Nivel de precisión
Apartado 3d. Vigilancia humana

43
