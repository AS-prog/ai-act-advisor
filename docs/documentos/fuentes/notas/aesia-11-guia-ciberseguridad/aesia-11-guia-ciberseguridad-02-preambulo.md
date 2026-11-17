---
name: aesia-11-guia-ciberseguridad-02-preambulo
description: "AESIA: aesia 11 guia ciberseguridad, sección «Preámbulo» (págs. 9-11). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-11-guia-ciberseguridad
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Preámbulo"
  paginas: 9-11
  origen: 2026-07-17-aesia-11-guia-ciberseguridad.pdf
  oficial: false
---
# Preámbulo

importante destacar que la obligación de cumplir con los requisitos de ciberseguridad no solo recae en las empresas que desarrollan la IA, sino también en aquellas que la comercializan, implementan o despliegan.
La descripción detallada de los casos de uso utilizados podrá encontrarse en Guía práctica y ejemplos para entender el Reglamento de IA
Siempre que se ponga un ejemplo, se hará de manera ilustrativa. Tanto proveedores como responsables del despliegue del sistema pueden aplicar las medidas y controles indicados en esta guía.
Los casos de uso se han seleccionado atendiendo a dos motivos:
-

La capacidad para explicar la información y procedimientos detallados en la guía, para establecer los criterios necesarios, en el entendimiento de aplicación de los requisitos establecidos en el artículo 15 de precisión, solidez y ciberseguridad.

-

La relevancia de ambos casos de uso en cuanto al impacto en sufrir un ataque que pueda generar consecuencias graves en los derechos de las personas físicas incluyendo personas con riesgo de exclusión social o minorías.

Los casos seleccionados han sido, con las consideraciones indicadas:
-

Sistema automático de concesión de ayudas.

-

Asistencia al trabajo.

8

2. Introducción
2.1 ¿Qué es la ciberseguridad para IA?
La ciberseguridad en sistemas de Inteligencia Artificial de alto riesgo no es una opción, y todos los sistemas se encuentran expuestos a amenazas específicas que requieren medidas de protección rigurosas y adaptadas a su contexto. Estas amenazas incluyen la manipulación de los datos de entrenamiento, que puede comprometer la integridad de los modelos; los ataques diseñados para forzar errores en los resultados, como los ejemplos adversarios; o aquellos dirigidos a obtener información privada de los datos utilizados durante el entrenamiento del sistema. Además, defectos propios del modelo o errores en su integración pueden ser aprovechados por terceros para alterar su funcionamiento o rendimiento. Como se explicará más adelante, siempre se deberá estar vigilante ante la aparición de nuevas amenazas que puedan aparecer de las categorías, mencionadas, o de otras nuevas y en ningún caso se debe considerar esta guía contiene un catálogo cerrado de amenazas y vulnerabilidades.
Vivimos inmersos en un contexto tecnológico en el que las ciberamenazas a los sistemas de la información son variadas, y los riesgos que estas contemplan son amplios. Las organizaciones de toda índole tienen en su más profundo carácter interiorizado el concepto de ciberamenaza, y lo que es más relevante, de ciberseguridad. Todos hemos visto alguna noticia que hace referencia a un ciberataque recibido por alguna empresa, o institución que, en el mejor de los casos, detiene el servicio prestado desde unas horas a algunos días. En el peor de los casos, la pérdida de datos, los riesgos para las personas y sus derechos son irreparables.
El ámbito de los sistemas de inteligencia artificial de alto riesgo no escapa a las amenazas de ciberseguridad generales, que no son objetivo de esta guía y que deberán ser tenidas en cuenta, de la manera adecuada. Estos sistemas de inteligencia artificial además suman y agravan, por su naturaleza, una serie de ciberamenazas propias que exponen sus vulnerabilidades y que son vectores de ataques específicos de los sistemas de inteligencia artificial, especialmente en el contexto de los sistemas de alto riesgo. No tener en consideración estas amenazas, y por tanto estar expuesto a ellas, supone un grave riesgo para cualquier sistema y, sin lugar a duda, una acción inadmisible en el contexto de los sistemas de alto riesgo.
Los daños potenciales que pueden causar los sistemas de alto riesgo para la seguridad y salud de las personas, daños materiales, de privacidad, limitaciones de derechos, discriminación, acceso al empleo y un largo etc., son de una gran magnitud, dado el contexto de consideración de alto riesgo que estos tienen.
Las medidas orientativas de ciberseguridad para sistemas de IA presentadas en esta guía tienen como objetivo mitigar los riesgos que amenazan los derechos y libertades de las personas físicas y de la sociedad en general. Estos se pueden ver seriamente amenazados

9

por la existencia de puertas traseras en los modelos, posibilidad de ataques de exfiltración o vulnerabilidad a ataques adversarios.
Es por ello importante que esta guía se aborde con la consideración de riesgos identificados que amenazan los derechos y libertades de las personas físicas y de la sociedad en general, identificados en el plan de riesgos (ver guía de gestión de riesgos)
para el sistema de IA, y exista un proceso que comience en los riesgos identificados, se asocie a las vulnerabilidades presentes en esta guía y pueda demostrarse la aplicación de los controles de seguridad aplicables. Todo ello siempre dentro del ciclo de vida del sistema de IA: concepción, diseño, implementación, validación/verificación y puesta en marcha.
La ciberseguridad desempeña un papel crucial a la hora de garantizar que los sistemas de
IA sean resistentes a los intentos de alterar su uso, comportamiento y rendimiento o de comprometer sus propiedades de seguridad por parte de terceros malintencionados que exploten las vulnerabilidades del sistema. Los ciberataques contra los sistemas de IA pueden aprovechar los activos específicos de la IA, como los conjuntos de datos de entrenamiento (por ejemplo, envenenamiento de datos) o los modelos entrenados (por ejemplo, ataques de adversarios), o explotar las vulnerabilidades de los activos digitales del sistema de IA o de la infraestructura de TIC subyacente. Por lo tanto, para garantizar un nivel de ciberseguridad adecuado a los riesgos, los proveedores de sistemas de IA de alto riesgo deben adoptar medidas adecuadas, teniendo en cuenta también, según proceda, la infraestructura de TIC subyacente.
Igualmente, el Reglamento Europeo de IA en su artículo 15, indica que la ciberseguridad
(orientada a Inteligencia Artificial) deberá ser adecuada y consistente a lo largo del ciclo de vida del sistema, lo que exige de las organizaciones (especialmente del proveedor, pero también del responsable del despliegue) un dimensionamiento adecuado de los esfuerzos en costes y personal. Del mismo modo, considerar la necesidad de vigilar adecuadamente las nuevas formas de ataque a los sistemas de inteligencia artificial, es un campo fuertemente cambiante.
De forma complementaria, el Reglamento de Ciberresiliencia será aplicable en aquellos productos con elementos digitales clasificados como un sistema de IA de alto riesgo.
Tendrá que tenerse en cuenta los requisitos de este reglamento cuando entre en aplicación, el 11 de diciembre de 2027.

2.2 ¿Cuáles son las principales amenazas?
Generalmente agrupadas bajo el concepto de ataques adversarios, a modo orientativo, algunas de estas amenazas a las que se encuentra expuesto un sistema de inteligencia artificial son:
-

Ataques de envenenamiento: buscan manipular el sistema de IA durante su fase de entrenamiento o actualización para comprometer su comportamiento. Estos ataques pueden clasificarse en dos tipos principales:

10
