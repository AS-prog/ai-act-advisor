---
name: aesia-16-manual-de-checklist-de-guias-de-requisitos-04-estructura-de-la-herramie-nta-de-checkli
description: "AESIA: aesia 16 manual de checklist de guias de requisitos, sección «Estructura de la herramie nta de checklist» (págs. 9-15). Documento de 2026-06-30, idioma es."
metadata:
  type: reference
  documento: aesia-16-manual-de-checklist-de-guias-de-requisitos
  emisor: AESIA
  fecha: 2026-06-30
  idioma: es
  seccion: "Estructura de la herramie nta de checklist"
  paginas: 9-15
  origen: 2026-06-30-aesia-16-manual-de-checklist-de-guias-de-requisitos.pdf
  oficial: false
---
# Estructura de la herramie nta de checklist

3. Estructura de la herramienta de checklist
Dicha herramienta es un documento Excel que tiene la misma estructura para todos los requisitos.
Se compone de 9 pestañas, 5 de ellas informativas con instrucciones de uso e información de contexto, y otras 4 pestañas operativas en las que se completa la información requerida. Para que su uso esté alineado con el procedimiento operativo de esta fase, se recomienda abordar las pestañas en el orden en el que aparecen en la propia herramienta.

A continuación, se describe la información y funcionalidad de cada una de las pestañas, indicando entre corchetes la naturaleza de la misma (informativa u operativa).

3.1 Portada [Informativa]
Contiene el recordatorio de confidencialidad obligatorio para la SEDIA (Secretaría de Estado de
Digitalización e Inteligencia Artificial) y todas las entidades participantes en el sandbox, que incluye el uso y distribución de esta checklist.

E JEMPLO DE PORTADA DE LA CHECKLIST DEL REQUISITO DE T RANSPARENCIA

3.2 Intro [Informativa]
Describe de manera resumida los pasos y lo que permite realizar la herramienta.

8

3.3 Artículo RIA [Informativa]
Muestra los apartados del artículo sobre los cuales la entidad va a hacer el autodiagnóstico. El campo “Descripción resumida” es un resumen de cada apartado para facilitar su contextualización en pestañas posteriores.

E JEMPLO DE LA CHECKLIST DE T RANSPARENCIA
( EL CONTENIDO DE LA IMAGEN ES PARTE DE LA EXISTENTE EN LA HERRAMIENTA )

3.4 Medidas Guías (MG) [Informativa]
Expone las medidas orientativas explicadas con detalle, recogidas en la correspondiente guía, las cuales:
- Han sido recogidas de buenas prácticas de la industria del software, y han sido validadas
por entidades nacionales y europeas.
- Se espera que sean de mayor detalle que los estándares que se espera que sean
liberados por la CE, ya que estos estarán más encaminados a describir QUÉ hay que hacer para cumplir el RIA, mientras que las medidas descritas en las guías (y en las checklists) dan pautas sobre CÓMO llegar al cumplimiento de cada requisito (o artículo). Estas pautas no son de obligado cumplimiento
9

-
-

No todas tienen por qué aplicar en cualquier sistema atendiendo a las características del mismo.
En base a la experiencia, se ha detectado que pueden existir medidas adicionales que las empresas ya están utilizando en sus sistemas y que sean igualmente válidas para el cumplimiento del RIA. Por eso en la pestaña "Medidas Adicionales (MA)", descrita más adelante en este documento, podrán ser agregadas.

Adicionalmente, para cada medida se han definido unas cuestiones orientativas con el fin de contextualizarla, de manera que la respuesta a las mismas pueda dar una idea de si el sistema ya cumple o no la medida en cuestión.

E JEMPLO DE LA CHECKLIST DE T RANSPARENCIA
( EL CONTENIDO DE LA IMAGEN ES PARTE DE LA EXISTENTE EN LA HERRAMIENTA )

3.5 Relación MG-Apart. [Informativa]
Resume de manera ejecutiva la potencial aplicación de las medidas expuestas en la pestaña anterior (Medidas guías (MG)) a cada uno de los apartados del artículo. Se trata de un resumen visual de la relación entre las medidas propuestas y todos los apartados del artículo.

E JEMPLO DE LA CHECKLIST DE T RANSPARENCIA

10

3.6 Autoeval MG. [Operativa]
Esta es la primera pestaña operativa de la herramienta, que permitirá identificar tanto el nivel de madurez de implantación de la medida propuesta en el sistema, como el nivel de dificultad percibido para llevarla a cabo. De la cumplimentación de esta pestaña va a surgir el diseño del
Plan de Adaptación mencionado anteriormente, que será completado con plazos y esfuerzos, y que constituirá la herramienta de planificación para la fase posterior.
Esta pestaña aparece pre-informada con una fila por cada una de las relaciones descritas entre medidas y subapartados del artículo.

E JEMPLO DE LA CHECKLIST DE T RANSPARENCIA
( EL CONTENIDO DE LA IMAGEN ES PARTE DE LA EXISTENTE EN LA HERRAMIENTA )

Si además la entidad considera que alguna medida puede servir para ser aplicada a algún apartado adicional, podrá indicarlo al final de las filas pre-informadas. Para cada relación se han de cumplimentar únicamente dos columnas:
-

-

Nivel de dificultad percibido, indicando cuál es la dificultad que la entidad entiende que la aplicación de dicha medida tendría en su sistema para ese apartado, en base a los siguientes valores cualitativos:
o 00. Alto o 01. Medio o 02. Bajo
Nivel de madurez, indicando cuál es el nivel de madurez de dicha medida en su sistema para el apartado indicado, utilizando los siguientes valores en función del estado de su documentación e implementación en el sistema:
o L1. No documentada ni implementada o L2. Documentación en curso y no implementada o L3. Documentada y no implementada o L4. Documentada e Implementación en curso o L5. Documentada e Implementada o L6. No documentada e Implementada o L7. Documentación en curso e Implementada o L8. Medida no necesaria, en caso de que la medida propuesta se considera que no es necesaria para el cumplimiento del apartado ya que, como se ha indicado anteriormente, no todas las medidas pueden tener que aplicar a todos los tipos de sistemas inteligentes.
Al seleccionar cualquiera de los anteriores valores del Nivel de madurez, automáticamente:

11

o

o

La columna Estado Diagnóstico se actualiza con el valor 01. Ya diagnosticada (por defecto, dicha columna aparece con el valor 00. Pdte diagnóstico), lo que permitirá conocer el grado de avance del diagnóstico.
La columna Plan de Adaptación se actualiza con un valor que servirá para diseñar el Plan de Adaptación de cada sistema, en base a la siguiente relación:
Nivel de madurez
L1. No documentada ni implementada
L2. Documentación en curso y no implementada
L3. Documentada y no implementada
L4. Documentada e Implementación en curso

L5. Documentada e Implementada
L6. No documentada e Implementada
L7. Documentación en curso e Implementada
L8. Medida no necesaria en mi sistema

Plan de adaptación
01. Documentar e implementar
01. Documentar e implementar
02. Implementar
02. Implementar
03. Adaptación completa
04. Documentar
04. Documentar
05. Ninguna adaptación requerida

R ELACIÓN ENTRE LOS NIVELES DE MADUREZ Y EL P LAN DE A DAPTACIÓN A REALIZAR

3.7 Medidas Adicionales (MA). [Operativa]
A partir de esta pestaña, junto a las dos siguientes, el autodiagnóstico consiste en la información de las entidades acerca de medidas que ellas mismas proponen como posibles para el cumplimiento del RIA y de las que la SEDIA evalúa su idoneidad.
Esta pestaña aparece sin informar, con el objetivo de que la entidad indique las medidas que, en su experiencia, permiten el cumplimiento de apartados del artículo.
Para ello deberá agregar una fila por cada una de dichas medidas, indicando la siguiente información:
-
-

Descripción breve: una descripción identificativa de la medida. Se recomienda utilizar la misma concreción que la utilizada en las Medias Guías (MG).
Nombre del archivo: donde dicha medida será detallada por la entidad. Cuando este campo se informe, la columna “Medida adicional documentada” automáticamente se actualizará con el valor “01. Ya aportada” (por defecto, al estar el campo en blanco aparecerá con el valor “00. Pendiente de aportar”)

Las medidas adicionales deben ser validadas por la institución correspondiente (la SEDIA en el caso del sandbox), que informará las siguientes columnas:
-

Evaluación SEDIA. Estado, que incluye los siguientes valores:
o 00. Evaluación Medida Adicional SEDIA. Pendiente, para cuando la medida esté pendiente de valorar por la SEDIA.
o 01. Evaluación Medida Adicional SEDIA. OK., cuando la SEDIA haya dado su OK a la medida. Esto supondrá un éxito para la entidad, ya que habrá aportado una medida hasta el momento no identificada que permitirá su aplicación en España y Europa.
o 02. Evaluación Medida Adicional SEDIA. NO_OK, para cuando la SEDIA rechace la medida tras, además de utilizar el criterio de sus expertos internos, haya recurrido a expertos y entidades externas para su evaluación.
12

-

Evaluación SEDIA. Comentarios, donde la SEDIA incluye comentarios adicionales a cualquiera de los tres estados mencionados anteriormente.

M EDIDAS A DICIONALES DE PRUEBA

3.8 Relación MA-Apart. [Operativa]
Permite resumir de manera ejecutiva la potencial aplicación de las medidas informadas en la pestaña anterior a cada uno de los apartados del artículo.
Los identificadores de las medidas aportadas en dicha pestaña anterior aparecen automáticamente en las columnas superiores.
Únicamente es necesario marcar con una X (mayúscula) a qué apartado del artículo aplica cada medida.

R ELACIÓN DE PRUEBA DE LAS M EDIDAS A DICIONALES APORTADAS EN LA PESTAÑA ANTERIOR CON LOS APARTADOS

3.9 Autoeval MA. [Operativa]
Este es el último paso. La pestaña aparece automáticamente pre-informada con una fila por cada una de las relaciones descritas en la pestaña anterior. Al igual que en la pestaña “Autoeval MG”, para cada relación se han de informar únicamente dos columnas: "Nivel de dificultad percibido" y “Nivel de madurez”. Las columnas “Estado Diagnóstico”, y “Plan de adaptación” se actualizan automáticamente al informar las dos anteriores columnas de igual manera que en la pestaña
“Autoeval MG" descrita anteriormente.

13

A UTOEVALUACIÓN DE PRUEBA DE LAS M EDIDAS A DICIONALES APORTADAS EN LA PESTAÑA ANTERIOR CON LOS APARTADOS

14
