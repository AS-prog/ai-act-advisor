---
name: aesia-05-guia-de-gestion-de-riesgos-11-anexos-parte-3
description: "AESIA: aesia 05 guia de gestion de riesgos, sección «Anexos (parte 3)» (págs. 52-59). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-05-guia-de-gestion-de-riesgos
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Anexos (parte 3)"
  paginas: 52-59
  origen: 2026-07-17-aesia-05-guia-de-gestion-de-riesgos.pdf
  oficial: false
---
# Anexos (parte 3)

diferentes capacidades de hardware de los sistemas en términos de potencia de procesamiento, memoria y la disponibilidad de aceleradores de hardware de IA dedicados.
En un ejemplo como el de la promoción de los empleados, quizá una limitación de hardware y un retraso en el proceso de decisión del sistema por la indisponibilidad derivada, no supone un riesgo alto, pero en cambio, en un sistema de IA encargado de administrar de forma automática insulina a un paciente diabético, un fallo en el hardware podría suponer un riesgo crítico para la vida del paciente.
6. Problemas del ciclo de vida del sistema:
Los métodos, procesos y también el uso inadecuado o insuficiente de un sistema de IA a lo largo de su ciclo de vida pueden generar riesgos. Por ejemplo, un proceso de diseño defectuoso puede no anticipar los contextos en los que se utilizará el sistema de IA, lo que hace que falle inesperadamente cuando se usa en estos contextos.
En el ejemplo del sistema de administración automática de insulina, deberemos analizar y anticipar los contextos en los que se utilizará el sistema a lo largo de su ciclo de vida. Definir los ciclos de actualización y revisión a los que deberá someterse para mitigar posibles fallos en su funcionamiento.
7. Preparación tecnológica:
La preparación tecnológica indica cuán madura es una tecnología dada en un contexto de aplicación determinado.
Las tecnologías menos maduras utilizadas en el desarrollo y la aplicación de sistemas de IA pueden añadir riesgos desconocidos para la organización o difíciles de evaluar.
Para las tecnologías maduras, se puede disponer de una mayor variedad de datos de experiencia, lo que facilita la identificación y la evaluación de los riesgos. Por ejemplo, en el sistema de promoción de empleados un riesgo asociado a la preparación tecnológica podría ser el relacionado con la falta de experiencia en el funcionamiento de estos sistemas que podría derivar en retrasos y aumento de los costes si en un momento dado se requiere actualizar o modificar los parámetros del sistema y no se dispone del conocimiento necesario.
8. Complejidad del entorno:
La complejidad del entorno de un sistema de IA determina la gama de situaciones que un sistema de IA puede soportar en su contexto operativo. Uno de los riesgos más relevantes, por ejemplo, es el relacionado con el grado de comprensión del entorno del sistema de
IA.
Una comprensión parcial del entorno dará lugar a un nivel de incertidumbre que es una fuente de riesgo especialmente relevante en la fase del diseño de los sistemas de IA.
En el ejemplo del sistema de promoción de empleados, deberemos analizar la complejidad del entorno y las diferentes situaciones en las que se utilizará el sistema para identificar adecuadamente los posibles riesgos derivados y mitigar en la mayor medida posibles fallos en su funcionamiento.

51

9. Otras potenciales fuentes de riesgos:
a. Dificultad en la identificación de responsabilidades y rendición de cuentas.
b. Uso inadecuado, incorrecto o fraudulento del sistema de IA.
c. Exceso de confianza en las decisiones del sistema de IA (automatización de las decisiones sin ningún tipo de supervisión).
d. Amenazas de seguridad y ciberseguridad (se recomienda especialmente en este punto consultar la guía de ciberseguridad que incorpora un inventario adicional de riesgos y amenazas de los sistemas de IA en el contexto de la ciberseguridad).
e. Posibles amenazas a la privacidad de las personas si no se desarrolla un adecuado gobierno de los datos (se recomienda consultar la guía de gobierno de datos).
f. Posibles perturbaciones o manipulaciones en los datos no deseadas (se recomienda consultar la guía de gobierno de datos y la guía de ciberseguridad).
g. Otros usos inadecuados derivados de una especificación deficiente del sistema de IA.
h. Los posibles sesgos en los datos también pueden suponer una amenaza para el adecuado uso del sistema de IA (se recomienda consultar la guía de gobierno de datos).

52

8.4 ANEXO D - Ejemplos de controles en el ámbito de la IA
Nota importante: Este anexo, tal y como se indica en la sección 4.5 de la guía, pretende incorporar un listado de algunos ejemplos de posibles controles para que sirva como orientación y referencia al lector cuando se enfrente al proceso de definición de medidas de control [2]. En este sentido, no se espera que el lector implemente todas las medidas de control listadas o que se limite únicamente a éstas, este proceso dependerá del contexto y de los riesgos identificados, analizados y evaluados a lo largo del desarrollo del sistema de gestión de riesgos.
1. Medidas de gobierno:
a. Establecer y definir las normas profesionales y éticas en el ámbito de las tecnologías de la información para desarrollar sistemas de IA siguiendo los estándares de referencia.
b. Facilitar documentación para los responsables del despliegue que incluye el contexto apropiado y las limitaciones conocidas de los sistemas de IA.
c. Definir mecanismos de reparación si las personas se ven afectadas negativamente por las decisiones del sistema de IA.
2. Medidas de inclusión:
a. Incorporar en todo el ciclo de vida de los sistemas de IA la contribución de expertos en tecnologías de la información, con conocimientos técnicos que incluyan un conocimiento profundo de las tecnologías de inteligencia artificial, datos y computación de datos.
b. Incluir a los usuarios y partes interesadas, en la medida de lo posible, en el proceso de desarrollo del sistema de IA (revisión de las especificaciones, participación en las pruebas, etc.).
c. Recoger, analizar e incorporar las opiniones y el feedback de los usuarios y las partes interesadas (por ejemplo, a través de encuestas).
d. Consolidar, en la medida de lo posible, equipos de desarrollo y mantenimiento con diversidad de opiniones, orígenes y pensamientos.
e. Evaluar el sesgo de la interacción tras la retroalimentación recogida de todas las partes interesadas.
3. Transparencia y explicabilidad:
a. Implementar técnicas de aproximación de los modelos incorporados en el sistema de IA (como la técnica de explicación diagnóstica del modelo local interpretable).
b. Implementar métodos de diagnóstico de modelos (como el análisis de componentes principales).
c. Implementar métodos de imitación de modelos o destilación (por ejemplo, transferencia de conocimientos de redes neuronales a árboles de decisión).
4. Capacidad de control:
a. Establecer puntos de control en el ciclo de vida de desarrollo del sistema de
IA (normalmente cuantos más puntos de control mejor, pero este es un factor por evaluar en cada contexto y escenario y depende de factores como nivel de riesgo a gestionar, recursos disponibles, necesidades a cubrir, etc.)
y un mecanismo de transferencia del conocimiento.
b. Instaurar mecanismos de para que los usuarios informen de cualquier tipo de incidencia del sistema de IA.
53

5.

6.

7.

8.

c. Implementar mecanismos para que los usuarios, en la medida de lo posible, ajusten el sistema decisión del sistema de IA.
Controles de seguridad y ciberseguridad:
a. Implementar mecanismos para la detección de posibles ataques de fuzzing
(técnica de testeo automatizado mediante la que se introducen datos inválidos, aleatorios o inesperados a un sistema informático) o manipulación de entrada a voz, video y gestos.
b. Desarrollar mecanismos para la oportuna identificación de datos de entrenamiento maliciosos (por ejemplo, sistemas de detección de cambios no autorizados, sistemas de detección de intrusiones o sistemas de monitorización del comportamiento del sistema de IA).
c. Identificar a los usuarios que actúan de forma anómala (de manera coordinada y diferente a la ordinaria), pues éstos pueden ser una potencial fuente de ataque malicioso.
d. Implantar instalaciones de auditoría o rastreo de eventos para examinar los estados de decisión, entrenamiento o detección de los sistemas de IA.
Controles de privacidad de los datos a. Implementar mecanismos para garantizar el adecuado uso y tratamiento de datos sensibles.
b. Facilitar formación a los usuarios que trabajen con datos sensibles para garantizar que lo hacen de forma adecuada, con discreción y precaución para evitar, por ejemplo, revelar información crítica del sistema de IA a conocidos o familiares.
c. Obtener el consentimiento de individuos o grupos de individuos para el tratamiento de sus datos en el sistema de IA.
d. Capacitar a los sistemas de IA para identificar sesgos o desviaciones indeseadas.
Controles y medidas sobre los datos a. Seleccionar adecuadamente los conjuntos de datos de entrenamiento y prueba del sistema de IA para que sean coherentes con el entorno que pretenden representar.
b. Identificar los atributos confidenciales que se requieren para el comportamiento adecuado del sistema de IA.
c. Implementar medidas de control y validación de conjuntos de datos (por ejemplo, métodos de retención de datos, K-fold cross validation, leave-oneout of cross validation (LOO), remuestreo jackknife, muestreo estratificado, etc.).
Rendimiento del diseño y la implementación del modelo a. Desarrollar una especificación detallada del diseño, funcionalidades e implementación del sistema de IA.
b. Detallar las técnicas de "feature engineering" utilizadas, como la selección, extracción y/o regulación de las características (features).
c. Especificar el modelo, algoritmos, hiperparámetros y la topología por escenario utilizados.
d. Desarrollar una API para verificar las métricas de rendimiento del sistema de
IA.

54

e. Desarrollar un análisis contrafactual para comprender mejor el comportamiento del sistema y evitar resultados no deseados.
9. Robustez, fiabilidad y resiliencia a. Implementar técnicas de entrenamiento adversario, como inyectar ejemplos contradictorios (generados por diferentes estrategias de ataque) en los datos de entrenamiento).
b. Implementar mecanismos para reconstruir entradas dañadas, es decir, eliminar ruido (por ejemplo, denoising autoencoder).
c. Agregar un sistema crítico para detectar cuándo el sistema de IA tiene demasiada confianza a pesar de una entrada ruidosa.
d. Desarrollar pruebas en entornos simulados y/o pruebas de campo y hacerlo periódicamente incluso después del despliegue del sistema de IA.

8.5 ANEXO E – Ejemplos de indicadores de efectividad
8.5.1 ANEXO E.I – En relación con las medidas de gestión de riesgos
Medidas a evaluar

Indicadores de efectividad

Análisis y definición del contexto interno y externo.

-

Número de factores evaluados y considerados en el desarrollo del sistema de gestión de riesgos

Definición y actualización del apetito al riesgo.

-
-

Elementos considerados en la definición
Frecuencia de actualización definida

Inventariado de componentes del sistema de IA.

-

Número de componentes del sistema de
IA identificados e inventariados

Identificación de las fuentes de riesgo principales.

-

Número de identificadas

Evaluación de las fuentes de riesgo.

-

Número de fuentes de riesgos evaluadas

Identificación y análisis del impacto de los efectos y su probabilidad de ocurrencia.

-

% de riesgos categorizados en función de su impacto y probabilidad de ocurrencia

Reporting de los resultados.

-

Nivel de madurez de la metodología de reporting de resultados definida

-

Metodología implementada de recabado de información poscomercialización
Frecuencia definida de análisis de la información recabada

Análisis de datos poscomercialización.

recogidos

-
Identificación de nuevos posibles riesgos.

-
-

fuentes

de

riesgo

Número de riesgos identificados en el proceso de poscomercialización
% de estos riesgos incorporado al sistema de gestión de riesgos (con los correspondientes análisis, evaluación e implementación de controles)
55

Definición y selección de las opciones para el tratamiento del riesgo.

-
-

Planificar e implementar el tratamiento del riesgo.

-
-

Número de opciones de tratamiento valoradas y evaluadas
Distribución de las medidas de tratamiento aplicadas en función del tipo de opción
Nivel de madurez del plan de tratamiento definido
Número de partes interesadas consultadas para su elaboración

Evaluar la eficacia de cada tratamiento.

-

% de riesgos que quedan como aceptables (riesgo por debajo del apetito definido) tras la aplicación de los tratamientos

Determinar si el riesgo residual es aceptable.

-

% de riesgos que han necesitado medidas adicionales
Número de medidas adicionales que han requerido cada uno de estos riesgos

-
Documentar residuales.

e

informar

los

riesgos

-
-

% de riesgos que quedan como residuales
% de riesgos residuales que han sido adecuadamente documentados e informados

8.5.2 ANEXO E.II – Con relación a los controles del Anexo D
1. Medidas de gobierno
Control / medida técnica

Indicador efectividad

Establecer y definir las normas profesionales y éticas para el uso de la IA siguiendo los estándares de referencia.

-

Número de normas o estándares profesionales establecidos y aplicados

Facilitar documentación para los usuarios que incluye el contexto apropiado y las limitaciones conocidas de los sistemas de
IA.

-

% de usuarios que han leído y aplicado la documentación

Definir mecanismos de reparación si las personas se ven afectadas negativamente por las decisiones del sistema de IA.

-

Número de mecanismos definidos y establecidos

56

2. Medidas de inclusión
Control / medida técnica

Indicador efectividad

Incorporar la contribución de diferentes expertos en el campo de la IA para el desarrollo de los sistemas de IA y a lo largo de todo el ciclo de vida.

-

Número de expertos involucrados

Incluir a los responsables del despliegue y partes interesadas, en la medida de lo posible, en el proceso de desarrollo del sistema de IA (revisión de las especificaciones, participación en las pruebas, etc.).

-

Número de responsables del despliegue e interesados involucrados en las pruebas

Recoger, analizar e incorporar las opiniones y el feedback de los usuarios y las partes interesadas (por ejemplo, a través de encuestas).

-

Número de opiniones de los interesados recabadas

Consolidar, en la medida de lo posible, equipos de desarrollo y mantenimiento con diversidad de opiniones, orígenes y pensamientos

-

Diversidad de opiniones incorporadas en la consolidación de los equipos

Evaluar el sesgo de la interacción tras la retroalimentación recogida de todas las partes interesadas.

-

Número de identificados

elementos

de

sesgo

3. Transparencia y explicabilidad
Control / medida técnica

Indicador efectividad

Implementar técnicas de aproximación de los modelos incorporados en el sistema de IA (como la técnica de explicación diagnóstica del modelo local interpretable).

-

Implementar métodos de diagnóstico de modelos
(como el análisis de componentes principales).

-

Número de métodos de diagnóstico implementados

Implementar métodos de imitación de modelos o destilación (por ejemplo, transferencia de conocimientos de redes neuronales a árboles de decisión).

-

Precisión del modelo de imitación implementado
Número de técnicas diferentes implementadas

-

-

Precisión del modelo de explicación implementado
Número de técnicas diferentes implementadas

57

4. Capacidad de control
Control / medida técnica

Indicador efectividad

Establecer puntos de control en el ciclo de vida de desarrollo del sistema de IA y un mecanismo de transferencia del conocimiento.

-

Número de puntos implementados.

Instaurar mecanismos de comunicación
(por ejemplo, habilitando una dirección de correo electrónico) para que los responsables del despliegue informen de cualquier tipo de incidencia del sistema de IA.

-

Número de reacciones de los responsables del despliegue informadas

Implementar mecanismos para que los responsables del despliegue, en la medida de lo posible, ajusten el sistema decisión del sistema de IA.

-

Número de ajustes abordados por los responsables del despliegue

de

control

5. Controles de seguridad y ciberseguridad
Control / medida técnica

Indicador efectividad

Implementar mecanismos para la detección de posibles ataques de fuzzing
(técnica de testeo automatizado mediante la que se introducen datos inválidos, aleatorios o inesperados a un sistema informático) o manipulación de entrada a voz, video y gestos.

-

Número de ataques de fuzzing detectados en las diferentes entradas.

Desarrollar mecanismos para la oportuna identificación de datos de entrenamiento maliciosos (por ejemplo, sistemas de detección de cambios no autorizados, sistemas de detección de intrusiones o sistemas de monitorización del comportamiento del sistema de IA).

-

Número de detecciones de datos de entrenamiento maliciosos.

Identificar a los usuarios que actúan de forma anómala (de manera coordinada y diferente a la ordinaria), pues éstos pueden ser una potencial fuente de ataque malicioso.

-

Número de detectados

Implantar instalaciones de auditoría o rastreo de eventos para examinar los estados de decisión, entrenamiento o detección de los sistemas de IA.

-

Número de instalaciones de auditoría o rastreo de eventos implantados

usuarios

maliciosos

58
