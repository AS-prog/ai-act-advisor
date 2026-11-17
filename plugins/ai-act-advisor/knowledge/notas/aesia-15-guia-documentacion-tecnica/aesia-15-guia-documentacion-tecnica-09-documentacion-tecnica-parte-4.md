---
name: aesia-15-guia-documentacion-tecnica-09-documentacion-tecnica-parte-4
description: "AESIA: aesia 15 guia documentacion tecnica, sección «Documentación técnica (parte 4)» (págs. 49-56). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-15-guia-documentacion-tecnica
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Documentación técnica (parte 4)"
  paginas: 49-56
  origen: 2026-07-17-aesia-15-guia-documentacion-tecnica.pdf
  oficial: false
---
# Documentación técnica (parte 4)

AI Act
Anexo IV.2 – Documentación técnica a que se refiere el artículo 11, apartado 1
(g.4) […] requisitos pertinentes establecidos en el capítulo III, sección 2, así como los efectos potencialmente discriminatorios; los archivos de registro de las pruebas y todos los informes de las pruebas fechados y firmados por las personas responsables, también en lo que respecta a los cambios predeterminados a que se refiere la letra f)

A lo largo de este apartado (g) del Anexo IV se ha hablado de los ensayos que se han realizado para la validación del modelo, la documentación deberá disponer registros de la información sobre la realización de los ensayos. Dicha información contendrá al menos:
✓
✓
✓
✓
✓

La fecha de realización del ensayo.
La versión de los datos relacionada.
La versión del sistema de IA.
Los resultados del ensayo.
La firma de las personas responsables.

En el caso de que se hayan realizado cambios predeterminados, o actualizaciones, los ensayos realizados deberán incorporarse y contener la misma información.

5.3 Seguimiento del funcionamiento y control del sistema de IA
El Anexo IV en su párrafo 3, indica al proveedor que la documentación técnica deberá contener información del seguimiento y control del sistema.

AI Act
Anexo IV.3 – Documentación técnica a que se refiere el artículo 11, apartado 1
Información detallada acerca de la supervisión, el funcionamiento y el control del sistema de IA, en particular con respecto a sus capacidades y limitaciones de funcionamiento, incluidos los niveles de precisión para las personas o colectivos de personas específicos en relación con los que está previsto que se utilice el sistema y el nivel general de precisión esperado en relación con su finalidad prevista;

48

Como se establece en la guía de solidez del sistema de IA la documentación debe incluir los rangos posibles de los parámetros configurables del modelo, rangos de datos de entrada y salida, así como las medidas de latencia y eficiencia estimadas para obtener la solidez establecida. Conviene que la documentación indique el procedimiento utilizado para monitorizar adecuadamente estos rangos definidos. La documentación puede reflejar las medidas técnicas realizadas para registrar (ver guía de registros) la información recogida de monitorización.
La documentación adicionalmente debería contener:
✓ Los valores mínimos aceptables para las métricas de solidez y precisión aplicables que deben reflejar y ser una señal de la calidad del sistema.
✓ En el momento que éstas no se puedan garantizar, la documentación reflejará los mecanismos de notificación de una posible interrupción/apagado del sistema.
✓ Debe explicar el funcionamiento del sistema en cuanto a desafíos de compromiso tomados más comunes. Por ejemplo, indicando garantías mínimas que provee el sistema para conocidos compromisos: entre imparcialidad global de grupo y privacidad individual (demostrado).
✓ La documentación deberá establecer las mínimas garantías esperadas, así como aquellos compromisos que han probado no poder garantizarse y que afectan al resultado de la finalidad prevista, tanto en el dominio de entrada como en los valores esperados.

5.4 Resultados no deseados y fuentes de riesgo
El foco de este apartado está centrado en la aparición de resultados no deseados previsibles y fuentes de riesgo. Se presentan de forma conjunta en el párrafo 3 del Anexo IV, pero su conceptualización es diferente.

AI Act
Anexo IV.3 – Documentación técnica a que se refiere el artículo 11, apartado 1
[…] los resultados no deseados previsibles y las fuentes de riesgo para la salud y la seguridad, los derechos fundamentales y la discriminación en vista de la finalidad prevista del sistema de IA;

Resultados no deseados, previsibles: Es este un aspecto que, a lo largo del Reglamento
Europeo de IA, se menciona específicamente en este apartado de documentación.
Este tipo de resultados se refiere a respuestas del sistema que dada su finalidad prevista son no deseados, pero que dado su diseño y características puedan ser previsibles, es decir, un resultado que no debe producirse en ningún caso, pero que cuando el sistema realiza la inferencia éste puede aparecer. Por ejemplo, en un sistema de concesión de ayudas, denegar las mismas a un grupo familiar (siendo beneficiarios), por encontrarse sus parámetros
49

incompletos o fuera del dominio de entrenamiento y el sistema no estar preparado para analizarlos; es un resultado previsible, dentro del ejemplo, pero no deseado.
En la guía del sistema de gestión de riesgos, que da cobertura al artículo 9, sistema de gestión de riesgos, del Reglamento Europeo de IA, se detalla como inventariar, gestionar y documentar los riesgos asociados a los conceptos de salud, derechos fundamentales y discriminación. La documentación técnica debería incluir un resumen que cubra todos los riesgos identificados en dicho proceso para los aspectos indicados.

5.5 Medidas de supervisión humana
El párrafo 3 del Anexo IV también indica que se deben documentar las medidas técnicas de supervisión humana.

AI Act
Anexo IV.3 – Documentación técnica a que se refiere el artículo 11, apartado 1
[…] las medidas de supervisión humana necesarias de conformidad con el artículo 14, incluidas las medidas técnicas establecidas para facilitar la interpretación de los resultados de salida de los sistemas de IA por parte de los responsables del despliegue;

En la guía de supervisión humana, se establecen que para que el responsable del despliegue pueda interpretar la información de salida se recomienda documentar:
✓ La descripción de su precisión, sus fallos típicos, sus causas y el intervalo de confianza de los resultados.
✓ Qué elementos se toman en cuenta para la toma de decisiones.
✓ Unas guías simplificadas para la supervisión humana a modo de prospecto que incluyan: que permite hacer el sistema, cuáles son sus usos adecuados, que es lo que no se puede hacer y cuáles son los usos inadecuados previsibles.
✓ La documentación debe contener ejemplos en los que el sistema puede tomar decisiones dispares y muestras de casos en los que se falla o acierta más.
✓ Información sobre el sesgo de automatización y como evitarlo.
✓ En la citada guía también se propone la elaboración de un video explicativo para el proceso de supervisión humana que pueda cubrir además de los citados elementos, un detalle de la operativa de la interfaz humano-máquina (si existiera)
de supervisión humana. La documentación debe incluir un enlace o referencia a dicho vídeo.

50

5.6 Especificación sobre los datos de entrada
El párrafo 3 finaliza indicando que deben proporcionarse las especificaciones de los datos de entrada.

AI Act
Anexo IV.3 – Documentación técnica a que se refiere el artículo 11, apartado 1
[…] las especificaciones de los datos de entrada, según proceda.

Descripción técnica sobre las especificaciones que se esperan en los datos de entrada, para contar con información de qué se espera que reciba el sistema cómo input. Esta descripción técnica puede contener:
-
-
-

-

El formato esperado de los datos de entrada, indicando si se trata de texto, imágenes, sonidos, series temporales, datos tabulados o cualquier otro tipo.
La frecuencia de recepción de estos para la que está diseñado el sistema, manteniendo las especificaciones de solidez y tiempo de respuesta.
Las validaciones realizadas sobre dichos datos que llevan a que se descarten y no sean introducidos en el sistema ya sea por motivos de seguridad (ataques de inversión o extracción) o valores fuera de dominio.
La manera en la que dichos datos de entrada quedan registrados en el sistema, tanto aceptados como no, y en relación con el sistema de mantenimiento de registros.

5.7 Descripción de la idoneidad de los parámetros de rendimiento
Como indica el párrafo 4 del Anexo IV, la documentación técnica debe incluir:

AI Act
Anexo IV.4 – Documentación técnica a que se refiere el artículo 11, apartado 1
Una descripción de la idoneidad de los parámetros de rendimiento para el sistema de IA concreto;
De acuerdo con lo detallado en la guía de solidez, se puede identificar cuáles son los parámetros allí detallados con una mayor relevancia para el sistema de IA en concreto e incluir una descripción de la idoneidad de éstos en la documentación técnica.

51

5.8 Descripción detallada del sistema de gestión de riesgos
Como indica el párrafo 5 del Anexo IV, la documentación técnica debe incluir:

AI Act
Anexo IV.5 – Documentación técnica a que se refiere el artículo 11, apartado 1
Una descripción detallada del sistema de gestión de riesgos con arreglo al artículo 9;

De acuerdo con lo detallado en la guía de gestión de riesgos, se debe incluir en la documentación técnica el informe resultante de su aplicación y la documentación asociada de controles y medidas aplicadas, como parte integrante de la documentación técnica.

5.9 Control de cambios realizados

AI Act
Anexo IV.6 – Documentación técnica a que se refiere el artículo 11, apartado 1
Una descripción de los cambios pertinentes realizados por el proveedor en el sistema a lo largo de su ciclo de vida.

En este párrafo 6, se establecen aspectos equivalentes al apartado correspondiente relacionado con las actualizaciones descritas en el apartado 2(f) del Anexo IV y ya previamente descrito en el apartado 5.2, y debe replicarse la misma información indicada en dicho apartado.
La documentación de cada cambio realizado sobre el sistema de IA debería indicar los apartados de la documentación técnica que han sido adaptados para reflejar la actualización realizada en el sistema y seguir manteniendo el requisito de completitud y actualización en aquellos casos en los que el cambio afecte a alguno de los apartados. Es decir, además de los cambios sufridos por el sistema de IA la documentación de estos deberá referir los apartados adaptados de la documentación para adecuarse a dichos cambios. Por ello la documentación técnica deberá relacionar, fecha versión de sistema de IA y versión de documentación, tal como se ha indicado en el apartado 5.1.
Los aspectos descritos en el apartado 5.2 son aplicables para los cambios pertinentes a la hora de reflejar su documentación.

52

5.10 Normas armonizadas o documentación equivalente
En el párrafo 7 del Anexo IV, se establece la necesidad que la documentación técnica contenga una lista de normas armonizadas utilizadas.

AI Act
Anexo IV.7 – Documentación técnica a que se refiere el artículo 11, apartado 1
Una lista de las normas armonizadas, aplicadas total o parcialmente, cuyas referencias se hayan publicado en el Diario Oficial de la Unión Europea;

Todas las normas armonizadas utilizadas en la planificación, organización, gobierno, diseño, implementación y puesta en marcha deberán inventariarse indicando el ámbito de aplicación.
Necesariamente sus referencias estarán publicadas en el Diario Oficial de la Unión Europea.
Cuando se encuentren disponibles, estarán emitidas por el organismo CEN-CENELEC https://www.cencenelec.eu/

AI Act
Anexo IV.7 – Documentación técnica a que se refiere el artículo 11, apartado 1
[…] cuando no se hayan aplicado normas armonizadas, una descripción detallada de las soluciones adoptadas para cumplir los requisitos establecidos en el capítulo III, sección 2, incluida una lista de otras normas y especificaciones técnicas pertinentes que se hayan aplicado.

En el ámbito del sandbox de IA en el que se enmarcan estas guías, dichas normas armonizadas no se encuentran publicadas, y otros estándares referencia ISO o NIST están en proceso de desarrollo. Si se diera el caso que para la cobertura de alguno de los apartados descritos en las guías del sandbox de IA se hubiera publicado alguno de dichos estándares
(ISO o NIST) se podría indicar a cuál apartado corresponde y su aplicación.
En el Anexo que acompaña esta guía se referencian aquellos estándares que se han consultado (así como su relación con los apartados), para la elaboración de la documentación. Por otro lado, cada una de las guías compañeras de esta de documentación, y relativo a los aspectos que en ellas se cubren, realizan una recopilación de los estándares
(en curso o aplicables) que le son también de aplicación.
Para el caso en el que durante la duración del sandbox dichas normas armonizadas, u otras especificaciones técnicas, no se encuentren publicadas, se deberá incluir en la documentación
53

las acciones y medidas que cada una de las guías proporcionadas indican para los aspectos cubiertos por el capítulo III sección 2 del Reglamento Europeo de IA.

5.11 Declaración de conformidad
El párrafo 8 del Anexo IV establece que se debe incorporar en la documentación técnica una copia de la declaración de conformidad de la UE.
En el periodo de realización del sandbox, dicho procedimiento de conformidad no estará establecido, al no estar definidos los organismos notificados, entre otros condicionantes. No obstante, el sandbox se acompaña de una guía dedicada a la evaluación de conformidad, en la que se establece qué es necesario realizar para obtener dicha conformidad.
La documentación técnica deberá incluir esta declaración de conformidad de la UE, en el momento que esta se encuentre disponible.
A continuación, indicamos el contenido que la declaración de conformidad debería contener, cuando el proceso de evaluación de conformidad se encuentre disponible, de acuerdo con el
Reglamento Europeo de IA.
El Reglamento Europeo de IA establece en el artículo 47 Declaración UE de conformidad, en su párrafo 1.

AI Act
Art.47.1 – Declaración UE de la conformidad
El proveedor redactará una declaración UE de conformidad por escrito en un formato legible por máquina, con firma electrónica o manuscrita, para cada sistema de IA de alto riesgo y la mantendrá a disposición de las autoridades nacionales competentes durante un período de diez años a contar desde la introducción del sistema de IA de alto riesgo en el mercado o su puesta en servicio. En la declaración UE de conformidad se especificará el sistema de IA de alto riesgo para el que ha sido redactada.

El contenido de esta declaración de conformidad se indica que debe estar referido al Anexo
V del Reglamento Europeo de IA, así se indica en el párrafo 2 del citado artículo.

54

AI Act
Art.47.2 – Declaración UE de la conformidad
En la declaración UE de conformidad constará que el sistema de IA de alto riesgo de que se trate cumple los requisitos establecidos en la sección 2. La declaración UE de conformidad contendrá la información indicada en el anexo
V.

Adicionalmente, el párrafo 3 del artículo 47, de aplicación para sistemas de IA del Anexo I, al estar sujetos dichos sistemas de IA a otra legislación de armonización de la Unión Europea se establecerá una única declaración y esta contendrá toda la información necesaria para identificar la legislación de armonización aplicable a la declaración de conformidad.
Acorde al Anexo V del Reglamento Europeo de IA, la declaración de conformidad deberá contener:
1.
Nombre y tipo del sistema de IA, y toda información que permita identificar y trazar de manera inequívoca el sistema de IA.
2.
Nombre y dirección del proveedor. Si el proveedor tiene un representante autorizado, esta información debe añadirse también.
3.
El proveedor debe indicar un párrafo afirmando que esta evaluación de conformidad se emite bajo su exclusiva responsabilidad.
4.
Igualmente deberá afirmar que el sistema de IA es conforme al Reglamento
Europeo de IA. Para ello, el proceso de evaluación de conformidad ha debido ser superado, el detalle de dicho proceso se establece en la guía de evaluación de conformidad que se ha proporcionado en el presente sandbox.
5.
Referencia a las normas armonizadas y/o especificaciones comunes respecto a las que se ha declarado conformidad. Este apartado dentro de la declaración de conformidad es equivalente a las indicaciones descritas en esta misma guía en el apartado 5.10.
6.
Como se puede consultar en la guía de evaluación de conformidad en detalle, el proceso de evaluación de conformidad puede incluir la participación de un organismo notificado, en esos casos, deberá identificarse adecuadamente el nombre y la identificación de dicho organismo. Es importante tener en consideración que durante la realización del sandbox de IA dicho organismo notificado no estará establecido.
7.
Lugar, fecha de emisión de la declaración con el nombre y cargo de la persona firmante.

55
