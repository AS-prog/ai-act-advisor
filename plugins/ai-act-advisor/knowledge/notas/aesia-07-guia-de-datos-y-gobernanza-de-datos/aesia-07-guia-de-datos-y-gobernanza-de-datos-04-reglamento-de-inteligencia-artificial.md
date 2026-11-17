---
name: aesia-07-guia-de-datos-y-gobernanza-de-datos-04-reglamento-de-inteligencia-artificial
description: "AESIA: aesia 07 guia de datos y gobernanza de datos, sección «Reglamento de Inteligencia Artificial» (págs. 10-13). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-07-guia-de-datos-y-gobernanza-de-datos
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Reglamento de Inteligencia Artificial"
  paginas: 10-13
  origen: 2026-07-17-aesia-07-guia-de-datos-y-gobernanza-de-datos.pdf
  oficial: false
---
# Reglamento de Inteligencia Artificial

3. Reglamento
Artificial

de

Inteligencia

La puesta en servicio o la utilización de sistemas de IA de alto riesgo debe supeditarse al cumplimiento de determinados requisitos obligatorios, entre los cuales está el de datos y gobernanza de datos. Estos requisitos tienen como objetivo garantizar que los sistemas de IA de alto riesgo disponibles en la Unión o cuyos resultados de salida se utilicen en la Unión no representen riesgos inaceptables para intereses públicos importantes o derechos individuales reconocidos y protegidos por el Derecho de la Unión.
En este apartado se incluyen los artículos referentes a la gobernanza de datos del
Reglamento 2024/1689 del Parlamento Europeo y del Consejo, de 13 de junio de 2024
(Reglamento Europeo de Inteligencia Artificial) y se detalla en que secciones de esta guía se abordan los diferentes elementos de dichos artículos.

3.1 Análisis previo y relación de los artículos
Con el objetivo de facilitar la implantación de las medidas propuestas para dar cumplimiento a los requisitos que establece el artículo, se ha reestructurado el contenido de este de manera que algunos puntos que parecen más genéricos (como el 2.h y el 3) se encuentren imbricados en otros más específicos (por ejemplo, el punto 2.e) que es donde tendrían una aplicación más concreta:
1. Los conjuntos de datos de entrenamiento, validación y prueba se someterán a las siguientes prácticas de gobernanza y gestión de datos:
a) Elección de un diseño adecuado.
b) Procesos de recopilación de datos.
c) Operaciones de tratamiento para la preparación de los datos (la anotación, el etiquetado, la depuración, el enriquecimiento y la agregación).
d) Formulación de los supuestos pertinentes con respecto a la información que los datos miden y representan.
e) Evaluación previa de la disponibilidad, la cantidad y la adecuación de los conjuntos de datos necesarios:
i. Serán pertinentes y representativos.
ii. Estarán completos.
iii. Tendrán las propiedades estadísticas adecuadas.
iv. Tendrán en cuenta, en función de su finalidad prevista, las características o elementos particulares del contexto geográfico, conductual o funcional en el que se pretende utilizar el HRAIS.
f) Análisis de sesgos (atendiendo aquellos que puedan afectar a la salud y la seguridad de las personas o dar lugar a algún tipo de discriminación prohibida por el Derecho de la Unión).
g) Detección y remediación de lagunas o deficiencias en los datos:

9

i. Carecerán de errores.
2. En el caso de que los datos de salida vayan a ser datos de entrada de otro modelo, deberían ser sometidos a las prácticas de gobernanza y gestión de datos mencionadas.
3. En la medida en que sea estrictamente necesario para garantizar la vigilancia, la detección y la corrección de los sesgos, se podrán tratar las categorías especiales de datos personales, ofreciendo siempre las salvaguardias adecuadas para los derechos y las libertades fundamentales de las personas.
A partir de este análisis, en la sección 4 plantearemos un enfoque orientativo para poder abordar cada una de estas tareas de forma adecuada.

3.2 Contenido de los artículos en el Reglamento de IA

AI Act
Art.10 – Datos y gobernanza de datos
1. Los sistemas de IA de alto riesgo que utilizan técnicas que implican el entrenamiento de modelos de IA con datos se desarrollarán a partir de conjuntos de datos de entrenamiento, validación y prueba que cumplan los criterios de calidad a que se refieren los apartados 2, 3 y 4 del presente artículo y el artículo 4 bis, apartado 1, siempre que se utilicen dichos conjuntos de datos.
2. Los conjuntos de datos de entrenamiento, validación y prueba se someterán a prácticas de gobernanza y gestión de datos adecuadas para la finalidad prevista del sistema de IA de alto riesgo. Dichas prácticas se centrarán, en particular, en lo siguiente:
a) las decisiones pertinentes relativas al diseño;
b) los procesos de recogida de datos y el origen de los datos y, en el caso de los datos personales, la finalidad original de la recogida de datos;
c) las operaciones de tratamiento oportunas para la preparación de los datos, como la anotación, el etiquetado, la depuración, la actualización, el enriquecimiento y la agregación;
d) la formulación de supuestos, en particular en lo que respecta a la información que se supone que miden y representan los datos;
e) una evaluación de la disponibilidad, la cantidad y la adecuación de los conjuntos de datos necesarios;
f) el examen atendiendo a posibles sesgos que puedan afectar a la salud y la seguridad de las personas, afectar negativamente a los derechos fundamentales o dar lugar a algún tipo de discriminación prohibida por el Derecho de la Unión, especialmente cuando las

10

salidas de datos influyan en las informaciones de entrada de futuras operaciones;
g) medidas adecuadas para detectar, prevenir y mitigar posibles sesgos detectados con arreglo a la letra f);
h) la detección de lagunas o deficiencias pertinentes en los datos que impidan el cumplimiento del presente Reglamento, y la forma de subsanarlas.
3. Los conjuntos de datos de entrenamiento, validación y prueba serán pertinentes, suficientemente representativos y, en la mayor medida posible, carecerán de errores y estarán completos en vista de su finalidad prevista.
Asimismo, tendrán las propiedades estadísticas adecuadas, por ejemplo, cuando proceda, en lo que respecta a las personas o los colectivos de personas en relación con los cuales está previsto que se utilice el sistema de
IA de alto riesgo. Los conjuntos de datos podrán reunir esas características para cada conjunto de datos individualmente o para una combinación de estos.
4. Los conjuntos de datos tendrán en cuenta, en la medida necesaria para la finalidad prevista, las características o elementos particulares del entorno geográfico, contextual, conductual o funcional específico en el que está previsto que se utilice el sistema de IA de alto riesgo.
5. (Apartado suprimido por el Ómnibus Digital).
6. Para el desarrollo de sistemas de IA de alto riesgo que no emplean técnicas que implican el entrenamiento de modelos de IA, los apartados 2, 3 y 4 del presente artículo y el artículo 4 bis, apartado 1, se aplicarán únicamente a los conjuntos de datos de prueba.

3.3 Correspondencia del articulado con los apartados de la guía
En la tabla dispuesta a continuación se detalle en que secciones de esta guía se abordan los diferentes elementos de dicho artículo:
Artículo
Reglamento

Requerimiento Reglamento

Sección guía

10.2.a

¿Qué elementos puedo implantar y cómo puedo hacerlo para desarrollar un adecuado gobierno del dato?

Apartado 2.2

10.2.b

Recopilación de los datos

Apartado 4.2

10.2.c

Preparación de los datos

Apartado 4.3

11

10.2.d

Requisitos de información

Apartado 4.1

10.2.e

Medición y mejora de la calidad de los datos

Apartado 4.3.1

10.2.f

Análisis de sesgos en los datos

Apartado 4.3.8

10.2.g

Medición y mejora de la calidad de los datos

Apartado 4.3.1

Medición y mejora de la calidad de los datos

Apartado 4.3.1

Tratamiento de las categorías especiales de datos personales

Apartado 5.1

10.2.h
10.4
4 bis

12
