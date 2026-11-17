---
name: aesia-05-guia-de-gestion-de-riesgos-05-reglamento-de-inteligencia-artificial-pa
description: "AESIA: aesia 05 guia de gestion de riesgos, sección «Reglamento de Inteligencia Artificial (parte 2)» (págs. 21-28). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-05-guia-de-gestion-de-riesgos
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Reglamento de Inteligencia Artificial (parte 2)"
  paginas: 21-28
  origen: 2026-07-17-aesia-05-guia-de-gestion-de-riesgos.pdf
  oficial: false
---
# Reglamento de Inteligencia Artificial (parte 2)

Ejemplo
En nuestro ejemplo, identificamos como elementos del contexto la necesidad del cumplimiento con el derecho fundamental a la no discriminación y el cumplimiento con el derecho fundamental relacionado con la protección de datos de carácter personal.
Tal y como indicábamos en la sección anterior, el contexto es la base para la identificación de amenazas y en consiguiente, los riesgos. Así, en este ejemplo, vamos a identificar cada uno de los elementos del contexto mencionados con un componente del sistema de IA y con un riesgo asociado:

Sistema

Sistema de promoción de empleados

Componente

Datos de entramiento

Propietario de los datos

Amenaza

Riesgo

Sobrerrepresentación
Discriminación de o subrepresentación unos empleados de un conjunto en la frente a otros en la base de datos de promoción entrenamiento
Filtración de datos
Revelación de intencionada o no datos personales intencionada por de los empleados parte del propietario

Es importante destacar, una vez más, que el Reglamento Europeo de la IA hace especial énfasis en los riesgos que puedan afectar a la salud, la seguridad y los derechos fundamentales de las personas. En este sentido, se deberá poner especial atención a la identificación de cualquier riesgo que pueda afectar a los elementos mencionados. Por ejemplo, en un sistema de IA encargado de administrar de forma automática insulina a un paciente diabético, el riesgo asociado a un fallo en la lectura de los parámetros que permiten determinar la cantidad de insulina que el paciente necesita en un momento dado, tiene un impacto directo sobre la salud y la vida de dicho paciente. En cambio, un riesgo de ese mismo sistema asociado a un fallo a la hora de enviar un reporte mensual de las dosis administradas a lo largo del mes a la aplicación del móvil del paciente no tiene un impacto directo tan representativo como el anterior sobre la salud o la vida del paciente.
Adicionalmente, para obtener más detalle de cómo se aborda este ejercicio y dónde y cómo queda reflejado, se aconseja consultar el documento Excel señalado en la sección
1.4.
¿Por qué es importante?
La identificación de riesgos es importante dado que sólo los riesgos identificados pueden evaluarse y recibir la respuesta adecuada. Cuando una organización no logra identificar el riesgo adecuadamente, éste queda completamente fuera del sistema de gestión de riesgos.

20

4.4 Análisis y evaluación de riesgos
¿Qué es?
Es el proceso de análisis y evaluación de los riesgos identificados en la etapa predecesora mediante la determinación, para cada uno de ellos, de la probabilidad de la materialización de la amenaza y la magnitud del impacto en el componente.
¿Cómo puedo abordarlo?
El objetivo de esta fase es determinar el impacto y la probabilidad de ocurrencia de cada riesgo identificado en la fase anterior. Por ello, se recomienda tomar nuestro documento donde estamos registrando el proceso de gestión de riesgos e incorporar dos nuevos atributos, el impacto y la probabilidad (se recomienda consultar y seguir el ejemplo desarrollado de forma detallada en el documento Excel señalado en la sección 1.4).

Ejemplo
En los apartados anteriores, hemos utilizado como ejemplo el sistema de IA de promoción y ascenso de los empleados y hemos identificado como posibles riesgos la discriminación de unos empleados frente a otros en la promoción y la revelación de datos personales de los empleados.
Lo que tenemos que hacer ahora, es decidir qué magnitud de impacto le damos a este riesgo, para ello determinaremos una escala de forma similar a cómo lo hicimos en la sección 4.1 cuando definimos el apetito al riesgo. Y haremos lo mismo con la probabilidad.

Llegados a este punto, es probable que nos surjan dudas como, ¿bajo qué criterio decido yo el nivel de impacto que tiene un riesgo?, ¿cómo puedo determinar la probabilidad que existe de que se materialice?, ¿cómo estableceré el valor del riesgo final?, ¿cómo se relaciona con la probabilidad y el impacto?, ¿y con el apetito al riesgo? A continuación, trataremos de dar respuesta a estas cuestiones.
Hay que recordar que la evaluación del riesgo es un ejercicio cualitativo y subjetivo, que debe facilitar conocer los sistemas de IA que se tienen y los principales riesgos que podrían afectarles y, por tanto, a la salud, la seguridad y los derechos fundamentales de las personas.
El valor o nivel de riesgo lo calcularemos como el producto del impacto en el componente por la probabilidad de que la amenaza suceda. No se trata de cuantificar el impacto y la probabilidad de que se materialice una amenaza con precisión numérica, sino valorarlos en una escala conceptual, y ser coherente en su aplicación a todos los casos. Así, por ejemplo, podemos definir una escala del 1 al 5 para categorizar los riesgos en 5 niveles de impacto (en orden ascendente, muy bajo o inexistente, bajo, medio, alto, muy alto o crítico)
y una escala del 1 al 3 para categorizar la probabilidad de que éstos sucedan (en orden ascendente, improbable, probable, muy probable). Dicho esto, el máximo nivel de riesgo que me podría encontrar sería igual a 15. Debemos considerar que esta escala debe ser la

21

misma que la definida para el apetito al riesgo, y lo que haremos a continuación es compararlos.
Una vez establecidos los niveles de impacto y probabilidad y calculado el valor final del riesgo, podemos compararlo con el apetito al riesgo determinado inicialmente.

Ejemplo
Supongamos que, para el riesgo relacionado con revelación de datos personales de los empleados, hemos determinado que tiene una probabilidad de suceder de 3 en la escala del 1 al 3 definida. ¿Por qué 3?, por ejemplo, porque no tenemos ningún control de acceso a la base de datos que contiene el conjunto de datos de entrenamiento ni controles de ciberseguridad que la protejan de agentes maliciosos externos.
En caso de suceder, determinamos que éste tendría un impacto grave sobre los empleados, ya que atentaría contra uno de los derechos fundamentales, la protección de datos de carácter personal. Digamos, entonces, que un impacto 4 en la escala definida del 1 al 5.
El resultado del análisis de este riesgo sería igual a 12 (producto de 3 por 4). Si habíamos definido un apetito al riesgo igual a 4, estaríamos por encima del umbral y por ende no estaríamos dispuestos a asumir este riesgo.

¿Qué podemos hacer ahora?, decidir qué tipo de respuesta al riesgo es la que mejor se ajusta a este escenario (evitar, transferir, mitigar, aceptar). Por ejemplo, mitigarlo estableciendo medidas (como controles de acceso o ciberseguridad) que lo reduzcan hasta que baje por debajo del umbral de apetito definido. En la sección 4.5 ahondaremos en las diferentes medidas y tratamientos del riesgo que podemos abordar.
Adicionalmente, para obtener más detalle de cómo se aborda este ejercicio y dónde y cómo queda reflejado, se aconseja consultar el documento Excel señalado en la sección
1.4.
¿Por qué es importante?
El análisis y evaluación de riesgos permite cuantificar el nivel de riesgo para nuestro sistema y, por consiguiente, a la salud, la seguridad y los derechos fundamentales de las personas, los riesgos identificados en la etapa anterior.
Sin este proceso de evaluación de los riesgos no tendríamos la capacidad de determinar, cuantitativamente si los aceptamos o, por el contrario, necesitásemos definir e implementar medidas de tratamiento para gestionarlos adecuadamente.

22

4.5 Respuesta al riesgo
¿Qué es?
Es el proceso de selección e implementación de medidas para abordar los riesgos identificados y analizados en las etapas anteriores.
¿Cómo debo abordarlo?
En esta fase se aconseja definir las medidas de respuesta al riesgo que podemos incorporar en nuestro documento donde estamos registrando el proceso de gestión de riesgos. Para ello seguiremos un procedimiento como el descrito a continuación (se incluyen breves ejemplos en cada etapa descrita, si bien, como se indica al final del apartado, el ejercicio completo se dispone en el Excel indicado en la sección 1.4):

1. Primero podemos determinar qué tipo de medidas de tratamiento de riesgos seleccionaremos para abordar cada uno de los riesgos identificados y analizados.
Las opciones principales son las que indicamos a continuación:
a. Implementar medidas de control para mitigar el riesgo:
Normalmente la primera opción que nos podemos plantear a la hora de tratar un riesgo cuyo valor supera nuestro apetito al riesgo será implementar controles adicionales para mitigar su probabilidad o impacto. En el Anexo D se disponen algunos ejemplos de controles específicos del ámbito de la IA.

Ejemplo
Siguiendo con nuestro ejemplo del sistema de IA para la promoción de empleados y el riesgo identificado asociado con la revelación de datos personales de los empleados, una medida que mitigaría este riesgo es la implementación de un sistema RBAC (Role Based Access Control) o sistema de control de accesos y administración de los derechos sobre los datos.
Con este control conseguiremos reducir la probabilidad de que suceda el riesgo. En el ejemplo más detallado de la sección 1.4 veremos cómo se reduce el valor del riesgo mediante la implementación de estos controles, pero supongamos por ahora que dicho valor se reduce del valor original 12 a un valor igual a 4, en la misma escala del 1 al 15.

b. Asumir el riesgo, aceptando las consecuencias que éste tendría en caso de suceder.

23

Ejemplo
En el apartado anterior veíamos como, tras implementar una medida de mitigación del riesgo, éste se reducía de un valor 12 a un valor 4. Inicialmente habíamos definido un apetito al riesgo igual a 4, ahora nos encontramos por debajo de dicho umbral.
En este escenario, podríamos implementar más medidas de control para seguir reduciendo el riesgo. Pero también podríamos determinar que, dado que el valor del riesgo actual ya está por debajo de nuestro apetito al riesgo, no implementar medidas de control adicionales y aceptar el nivel de riesgo actual.
En el ejemplo más detallado de la sección 1.4 veremos casos representando este escenario y cómo se releja en el documento que recoge nuestro sistema de gestión de riesgos.

c. Evitar el riesgo mediante la decisión de no iniciar o descontinuar la actividad que genera el riesgo.

Ejemplo
Siguiendo con nuestro ejemplo, tras analizar los riesgos asociados a nuestro sistema de IA para la promoción de empleados, podemos encontrarnos en un escenario donde el número de riesgos, su probabilidad de suceder y sus respectivos impactos sobre la salud, la seguridad y los derechos fundamentales de las personas sean tan elevados, que nos hagan plantearnos que quizá no nos interese seguir utilizando el sistema o descontinuarlo.

d. Transferir el riesgo, por ejemplo, a través de contratos, como la compra de seguros.

Ejemplo
En el contexto del Reglamento de la IA, cabe destacar que la gestión del riesgo, como ya hemos comentado a lo largo de la guía, se centra en la gestión aquellos riesgos que puedan afectar a la salud, la seguridad y los derechos fundamentales de las personas.
La transferencia del riesgo es una medida, por su naturaleza, aplicable en un contexto de gestión de riesgos para la organización. Por ejemplo, supongamos que el riesgo asociado a la una posible pérdida de información de la organización es tan elevado que decidimos contratar los servicios de una compañía externa que velará por garantizar que nuestros datos no son manipulados y que llegamos a un acuerdo con dicha compañía según el cual en caso de que éstos sufran una manipulación indeseada la compañía nos compensará con una cuantía económica acordada.
24

2. En segundo lugar, y una vez definidas las medidas de tratamiento del riesgo podemos establecer una planificación para su implementación. Para ello, por ejemplo, podemos establecer mediante un diagrama de Gantt la secuencia de implementación de las medidas definidas en función la prioridad y las fechas de compromiso para implementarlas.
La priorización de la implementación de las medidas se puede establecer, por ejemplo, en función de su impacto de mitigación, dando especial prioridad a aquellas que mitiguen los riesgos más relevantes.
3. En tercer lugar, se recomienda documentar e informar los riesgos residuales. Es aconsejable informar en la documentación asociada a nuestro sistema aquellos riesgos identificados y analizados. Para la adecuada elaboración de esta documentación se deberá consultar la guía de transparencia y provisión de información a los usuarios dispuesta para ello, tal y como se indica en el
Reglamento, en el apartado 5c del artículo:” Sistema de gestión de riesgos”).
4. Finalmente, podemos establecer periodos de revisión y seguimiento del sistema de gestión de riesgos (se recomienda incorporar todos aquellos nuevos riesgos que se identifiquen, así como evaluar y definir las medidas de tratamiento oportunas).
También deberemos comunicar los resultados y actividades de la gestión del riesgo, así como las actualizaciones derivadas a lo largo de la organización
(especialmente a las partes interesadas y/o impactadas).
Adicionalmente, para obtener más detalle de cómo se aborda este ejercicio y dónde y cómo queda reflejado, se aconseja consultar el documento Excel señalado en la sección
1.4.
¿Por qué es importante?
Es la fase donde, tras identificar, analizar y evaluar los riesgos que amenazan a nuestro sistema de IA, establecemos las medias oportunas para gestionarlos.
Sin implementar medidas de respuesta al riesgo, el sistema de gestión de riesgos se quedaría en una fase de conocimiento de los riesgos amenazantes y, en el peor de los casos, de conocimiento de que estos superan el nivel de riesgo que estamos dispuestos a asumir. Esta fase es la que nos permite, una vez determinado todo ello, enfrentarnos a los riesgos y tratar de reducir o mitigar su impacto, en definitiva, darles una respuesta.

4.6 Documentación técnica del sistema de gestión de riesgos
Para la adecuada documentación del sistema de gestión de riesgos, se recomienda seguir los pasos descritos en la sección 4 y reflejarlos en un documento igual o similar al facilitado como ejemplo en la sección 1.4. Adicionalmente, poner especial atención a la documentación de los riesgos residuales, tal y como se explica en la sección 4.5 apartado
3.

25

Para más detalle, ver sección 6.

4.7 Comunicación y consulta
Los actores involucrados en el diseño, desarrollo y comercialización del sistema de IA deben conocer el sistema de gestión de riesgos del sistema de IA y deberán colaborar en su completitud y actualizaciones.
La comunicación busca promover la toma de conciencia y la comprensión del riesgo.
La consulta implica obtener retroalimentación e información para apoyar la toma de decisiones.
Es recomendable que la comunicación y consulta con las partes interesadas apropiadas, tanto externas como internas, se realice en todas las etapas del proceso de la gestión del riesgo.
Se recomienda a las organizaciones que desarrollan o utilizan sistemas de IA identificar qué partes de la organización están involucradas. La organización debe ser consciente de que la aplicación de las tecnologías de IA puede tener un mayor impacto que la aplicación de otras tecnologías y prestar especial atención a aquellos impactos sobre la salud, la seguridad y los derechos fundamentales de las personas.

4.8 Seguimiento y mejora continua
Su finalidad es asegurar y mejorar la calidad y la eficacia del sistema de gestión de riesgos.
Es imprescindible desarrollar un seguimiento y establecer unos periodos determinados de revisión y actualización del sistema de gestión de riesgos. De este modo, conviene revisar el inventario de riesgos e incorporar todos aquellos adicionales que puedan identificarse.
También se podrá abordar y revisar el análisis y evaluación de los nuevos riesgos y de los ya existentes. Por último, las medidas de mitigación oportunas también podrán revisarse y actualizarse en consecuencia.
Como comentábamos al inicio de la guía, es favorable abordar el proceso de gestión de riesgos en todas las etapas del ciclo de vida del sistema de IA, desde el diseño y desarrollo hasta su comercialización y poscomercialización. Por tanto, conviene realizar el seguimiento y actualización de los riesgos en cada etapa.

4.9 Liderazgo y compromiso
La gestión de riesgos es el proceso por el cual la dirección de una organización: supervisa, lidera, se compromete con el desarrollo del sistema de gestión de riesgos y garantiza la integración de los diferentes sistemas de gestión de riesgos de la organización (por ejemplo, el de la gestión de riesgos de los sistemas de IA con el resto).

26

Formalizar el liderazgo y compromiso con la gestión de riesgos es otro de los pilares fundamentales en el desarrollo de un sistema de gestión de riesgos.
La alta dirección y los órganos de supervisión, siempre que apliquen, deberán asegurar que la gestión del riesgo del ciclo de vida de los sistemas de IA está integrada con la gestión del riesgo del resto de la organización. Esto lo pueden llevar a cabo mediante, por ejemplo:
a) La publicación de una declaración o política que establezca un enfoque, plan o línea de acción para la gestión del riesgo descrita en el ANEXO G.
b) El aseguramiento que existen recursos suficientes asignados a la gestión del riesgo.
c) La asignación de autoridad, responsabilidad y rendición de cuentas en los niveles apropiados dentro de la organización.

27
