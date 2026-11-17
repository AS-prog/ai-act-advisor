---
name: aesia-13-guia-vigilancia-poscomercializacion-08-anexos
description: "AESIA: aesia 13 guia vigilancia poscomercializacion, sección «Anexos» (págs. 29-35). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-13-guia-vigilancia-poscomercializacion
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Anexos"
  paginas: 29-35
  origen: 2026-07-17-aesia-13-guia-vigilancia-poscomercializacion.pdf
  oficial: false
---
# Anexos

7. Anexos
7.1 Anexo A - Indicadores de vigilancia
La definición de indicador depende en gran medida del contexto de su aplicación. No obstante, en el ámbito de un sistema de vigilancia, un indicador se puede considerar como un dato dentro de una escala que permite medir su impacto respecto a una o varias consecuencias concretas. A modo de ejemplo, nuestro sistema inteligente responsable de administrar la insulina al usuario registra un dato del nivel actual de azúcar en sangre: 115 mg/dL. ¿Cómo se transforma dicho dato en un indicador? En este caso, para ser un indicador, se debe conocer:
1. La escala del dato: el nivel de azúcar mínimo (70 mg/dL) y máximo (99 mg/dL)
aceptable.
2. El impacto de dicho dato: evaluar qué implicaciones tiene la medición actual (115 mg/dL) en las consecuencias o escenarios que queremos controlar: a partir de 99 mg/dL el nivel de azúcar es inusualmente alto y se debe de realizar una evaluación del estado del usuario en profundidad.
Otro ejemplo relacionado con el mismo sistema sería el indicador de número de predicciones. El dato sería el número de predicciones generadas por el sistema durante el último minuto: 128 predicciones. Para transformarlo en indicador debemos de establecer:
1. La escala del dato: se espera un mínimo de 90 predicciones y un máximo de 180 predicciones por minuto.
2. El impacto de dicho dato: En este caso el dato se encuentra dentro del rango de actividad usual del sistema. Sin embargo, si fuera más alto de 180 podría alertarnos sobre potenciales errores del sistema no notificados o si por el contrario fuera más bajo de 90 podría alertarnos de una posible carga de trabajo del sistema inusualmente alta.
A continuación, se detalla un listado con diferentes ejemplos de indicadores que deberán de ser seleccionados en función de la evaluación de riesgos realizada (Véase sección 5 de la Guía de Gestión de Riesgos: “¿Qué elementos debo implantar y cómo debo hacerlo para desarrollar un adecuado sistema de gestión de riesgos?”) y transformados en registros
(Véase sección 5 de la Guía de Conservación de Registros: “¿Qué elementos debo implantar y cómo debo hacerlo para desarrollar un adecuado sistema de gestión de registros?”):
Algunas notas aclaratorias sobre los listados de indicadores propuestos:
-
-

No se trata de un listado exhaustivo sino de un listado mínimo sobre el que ampliar indicadores en función del sistema inteligente concreto.
En los casos en los que el indicador obtenga un dato promedio también se aconseja obtener el valor mínimo y máximo para registrar valores puntuales anómalos de los indicadores. Por ejemplo, si se obtiene el número de predicciones por minuto promedio también se aconseja obtener el mínimo de predicciones realizadas por
28

-

-

-

minuto y el máximo. En definitiva, se aconseja incluir todas las medidas estadísticas necesarias para una correcta vigilancia del indicador.
Resulta de especial importancia resaltar que los indicadores de ciberseguridad son un listado de ejemplos que debe de ser adaptado y ampliado por los responsables de seguridad del sistema inteligente en base a su contexto de aplicación. Por lo tanto, no se tratan de indicadores mínimos sino de ejemplos generales.
Los umbrales mínimos y máximos establecidos en la escala deben de ir acompañados de un sistema de envío de alertas para actuar en tiempo real ante cualquier tipo de contingencia. También se aconseja contar con un dashboard de vigilancia en tiempo real de las mediciones obtenidas del sistema.
En algunos casos contar solo con indicadores no es suficiente y se debe de considerar una revisión manual de los registros en función de la complejidad de estos. Por ejemplo, el número de orígenes de sesión diferentes para un usuario
(supongamos 15 inicios de sesión en lugares diferentes) no solo debe de ser evaluado a través de un indicador sino en muchos casos a través de una revisión manual o automatizada de dichos orígenes. El objetivo es que el indicador actúe como alerta o disparador para dicha revisión.

7.1.1 Anexo A.I - Indicadores sobre el sistema inteligente
INDICADOR

Predicciones realizadas por unidad de tiempo

DATO

ESCALA

Mínimo esperado de
Número de predicciones predicciones y número máximo realizadas.
Ejemplo:
1.567 de predicciones sin pérdida de predicciones en el último rendimiento. Ejemplo: mínimo minuto.
200 y máximo 22.000.

Tiempo entre la introducción de
Tiempo medio input en el sistema inteligente y de predicción su respuesta. Ejemplo: 0.65 segundos.

Tiempo mínimo esperado para una predicción y tiempo máximo aceptable. Ejemplo:
0.2 segundos / 2.5 segundos

Número de tareas en espera de
Rango aceptable de cola de
Cola de ser procesadas por el modelo procesamiento. Ejemplo: 0 - 50 procesamiento en tiempo real. Ejemplo: 10 tareas.
tareas en cola.
Porcentaje de predicciones
Tasa de errores incorrectas sobre el total de Rango de tolerancia para de predicción* predicciones realizadas. errores. Ejemplo: 0% - 10%
Ejemplo: 3%

29

Precisión modelo*

Porcentaje de predicciones del correctas sobre el total de Rango de precisión deseado.
predicciones realizadas. Ejemplo: 85% - 100%
Ejemplo: 97%

Porcentaje de verdaderos positivos sobre el total de casos positivos reales (verdaderos
Recall
Rango aceptable de Recall.
positivos y falsos negativos).
(Exhaustividad)*
Ejemplo: 80% - 100%
Especialmente importante en el caso de problemas desbalanceados. Ejemplo: 90%
F1 Score modelo*

del Media armónica de precisión y Rango aceptable de F1 Score.
exhaustividad. Ejemplo: 0.85
Ejemplo: 0.7 - 1.0

Depende del input en particular, pero conceptualmente se trata del registro de mediciones estadísticas como la media,
Variación en las mediana y desviación típica de medidas los valores de entrada para estadísticas de detectar variaciones los inputs considerables en tiempo real.
Ejemplo para un sistema que recibe un texto como input:
Media de 6.8 tokens /
Desviación típica de 2.1

El rango aceptable de las medidas estadísticas seleccionadas para el input en concreto. Ejemplo: Media de mínimo 1 y máximo 100.

* En muchos casos las medidas relacionadas con errores de predicción del sistema no se pueden obtener en tiempo real por lo que no podrán aplicarse en la vigilancia continua sino en la vigilancia periódica descrita en la sección 4.2 de la presente guía “Vigilancia periódica”. A modo de ejemplo, no podemos saber a tiempo real si el sistema de promoción de empleados ha cometido un error en la asignación de un nuevo puesto hasta no comprobar los resultados y KPIs obtenidos por el trabajador con el tiempo. En este caso no tiene sentido obtener indicadores de tasa de error del sistema de forma continuada sino realizar evaluaciones periódicas del mismo.

30

7.1.2 Anexo A.II - Indicadores sobre la infraestructura
INDICADOR

Uso de CPU

DATO

ESCALA

Porcentaje de utilización de la
Rango aceptable de uso de
CPU en el sistema. Ejemplo:
CPU. Ejemplo: 20% - 90%
60%

Número medio de procesos en
Media de
Rango aceptable de procesos el sistema por unidad de procesos en el activos de media. Ejemplo: 53 tiempo. Ejemplo: 433 procesos sistema
2500 procesos / minuto.
de media / minuto.
Porcentaje de utilización de la
Uso de
Rango aceptable de uso de memoria en el sistema.
memoria RAM memoria. Ejemplo: 30% - 95%
Ejemplo: 70%
Uso de GPU y
Porcentaje de utilización de la Rango aceptable de uso de sistemas
GPU. Ejemplo: 55%
GPU. Ejemplo: 20% - 85% similares
Uso de Porcentaje de utilización de Rango aceptable de uso de almacenamient almacenamiento en el sistema. almacenamiento.
Ejemplo:
o
Ejemplo: 80%
10% - 90%

Tiempo actividad

Porcentaje de tiempo que el
Rango deseado de tiempo de de sistema permanece operativo actividad. Ejemplo: Máximo de sin interrupciones. Ejemplo: 26
72 horas.
horas.

Capacidad de la red para Rango deseado de ancho de
Ancho de transmitir datos por segundo. banda de red. Ejemplo: 100 banda de red
Ejemplo: 1.62 Gbps
Mbps - 10 Gbps

Temperatura del sistema

Temperatura promedio sistema. Ejemplo: 22°C

del

Rango aceptable de temperatura ambiente.
Ejemplo: 15°C - 30°C

31

7.1.3 Anexo A.III - Indicadores sobre las acciones de los usuarios
Los indicadores relacionados con las acciones de usuarios se pueden aplicar tanto de forma general para todos los usuarios como a nivel de usuario en función de las necesidades de vigilancia y riesgos del sistema inteligente. Por ejemplo, el número de inicios de sesión se puede aplicar como una métrica para todos los usuarios del sistema y también se puede aplicar para cada uno de los usuarios de este.

INDICADOR

DATO

ESCALA

Número de inicios de sesión
Rango aceptable de inicios de
Inicios de sesión realizados por los usuarios en sesión. Ejemplo: 100 - 1.000 un periodo dado. Ejemplo: 500 diarios.
inicios de sesión diarios.
Número de interacciones por usuario por unidad de tiempo

Cantidad promedio de predicciones solicitadas por Rango aceptable de cada usuario en un periodo interacciones por usuario.
dado. Ejemplo: 50 predicciones Ejemplo: 0 - 1000 al día.
por usuario al día.

Duración promedio de las
Tiempo
Rango deseado de tiempo sesiones de usuario en la promedio entre promedio en la plataforma.
plataforma.
Ejemplo:
15 interacciones
Ejemplo: 5 - 60 minutos.
minutos

Interacciones con la interfaz

Número de interacciones realizadas por los usuarios con Rango deseado de la interfaz en un periodo dado. interacciones con la interfaz.
Ejemplo: 2.000 interacciones Ejemplo: 500 - 5.000 diarias.
diarias

Mismos datos que “Variación en
Medidas las medidas estadísticas de los estadísticas de inputs” de la tabla de los inputs indicadores sobre el sistema introducidos inteligente, pero asociando por usuario dichas métricas con un usuario en particular.

Misma escala que “Variación en las medidas estadísticas de los inputs” de la tabla de indicadores sobre el sistema inteligente, pero asociando dichas métricas con un usuario en particular.

32

Número orígenes sesión diferentes

En algunos casos resulta de fundamental controlar la
Rango aceptable de orígenes de dispersión de inicios de sesión diferentes de inicios de sesión tanto bajo la perspectiva técnica por usuario. Ejemplo: 1 - 20.
como de ciberseguridad.
Ejemplo: 3 orígenes diferentes.

7.1.4 Anexo A.IV - Indicadores de seguridad
Los siguientes indicadores de ciberseguridad son algunos ejemplos que pueden ser ampliados por los responsables de seguridad del sistema inteligente en base a su contexto de aplicación siguiendo las recomendaciones de la guía de ciberseguridad. Además, los indicadores pueden combinarse con análisis manuales de los registros obtenidos para una comprensión completa de cada escenario.

INDICADOR

DATO

ESCALA

Número de intentos fallidos de
Intentos de inicio de sesión en un periodo Rango aceptable de intentos inicio de sesión dado. Ejemplo: 50 fallidos fallidos. Ejemplo: 0 - 100 diarios fallidos diarios.
Número de modificaciones no
Cambios no autorizadas en archivos del Importancia alta a partir de un solo autorizados en sistema en un periodo dado. cambio.
archivos
Ejemplo: 1 cambio detectado.
Número de Número de usuarios logueados
Rango aceptable de usuarios usuarios activos en el sistema en un momento logueados. Ejemplo: 2 - 3 usuarios.
en el sistema dado. Ejemplo: 10 usuarios.
Volumen de
Cantidad de datos transferida Rango aceptable de cantidad de datos por unidad de tiempo en la red. datos. Ejemplo: 10 - 750 MB / transferidos en
Ejemplo: 103.2 MB / segundo.
segundo.
la red
Número de
Rango aceptable de conexiones.
Cantidad de conexiones de red comunicaciones
Ejemplo: 200 - 20.000 conexiones / establecidas por unidad de abiertas hora.

33

tiempo.
Ejemplo:
conexiones / hora.

2.498

Este listado solo representa un ejemplo con diferentes indicadores y debe de ser completado en función de las características del sistema inteligente y el análisis de riesgos realizado.

34
