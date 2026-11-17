---
name: aesia-11-guia-ciberseguridad-07-reglamento-de-inteligencia-artificial-pa
description: "AESIA: aesia 11 guia ciberseguridad, sección «Reglamento de Inteligencia Artificial (parte 4)» (págs. 41-48). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-11-guia-ciberseguridad
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Reglamento de Inteligencia Artificial (parte 4)"
  paginas: 41-48
  origen: 2026-07-17-aesia-11-guia-ciberseguridad.pdf
  oficial: false
---
# Reglamento de Inteligencia Artificial (parte 4)

Tabla 2 Ataques adversarios al modelo: vulnerabilidades y controles de seguridad

Ejemplo – Sistema automático de concesión de ayudas
Durante el desarrollo de del sistema de IA, el proveedor ha establecido un equipo de desarrollo del sistema y otro destinado a ponerlo a prueba, un proceso basado en equipo azul/equipo rojo, de tal manera que cada iteración del modelo (equipo azul) es puesta a prueba (equipo rojo).
Para ello el equipo rojo ha diseñado, herramientas específicas que permiten automatizar las pruebas de seguridad, una serie de pruebas al sistema de IA que son verificadas cada vez que el equipo azul realiza un cambio en el modelo. Estas pruebas automatizadas replican los ataques a vulnerabilidades conocidas y se deben actualizar continuamente cuando se vayan conociendo nuevas vulnerabilidades que potencialmente podrían ser explotadas.
Se ha puesto el foco también en el control de datos de entrada, dado que son los solicitantes los que introducen los datos en el sistema. Se dispone en la recepción de los datos de un mecanismo de control OoD (Out of Domain data). Se ha seleccionado este procedimiento debido a que los datos introducidos se encuentran dentro de secuencias de valores estructurados y tabulados, con valores numéricos o series discretas y permiten establecer controles sobre entradas sospechosas.
Dado que el sistema se ha entrenado con datos proporcionados por la Administración
General del Estado, sobre históricos de datos anonimizados los últimos 10 años, se ha identificado la vulnerabilidad de ataques de inferencia de pertenencia como un riesgo relevante a pesar de la anonimización. Para proteger al sistema se ha recurrido a técnicas de privacidad diferencial. El conjunto de datos inicial ha sido ampliado utilizando herramientas que permiten aumentar los datos de inyectando ruido en los mismos. Se seleccionan estas herramientas, por ser adecuadas cuando se trata de evitar el riesgo de ataques de inversión.
Considerando la vulnerabilidad clasificación errónea origen/objetivo, que permitiría conseguir que un solicitante pudiera obtener la ayuda con un patrón malicioso de entrada, se ha aplicado la técnica Feature Denoising a los datos de entrada. El modelo además ha sido entrenado con ejemplos adversarios.
Responsable del despliegue
En este ámbito de ataques el modelo de comercialización del sistema de inteligencia artificial de alto riesgo determina el alcance de las acciones relativas a ciberseguridad que debe realizar el responsable del despliegue.
En cualquier caso, y según el modelo de comercialización del sistema de IA se recomienda que estas estén claramente definidas en el manual de instrucciones. Organizativamente el responsable del despliegue deberá conocer y analizar las vulnerabilidades y los controles que puedan ser de su responsabilidad y asignar recursos humanos y técnicos para cubrirlas.

40

4.5 Ataques a los defectos del sistema de IA
En el párrafo 5, artículo 15 relativo a precisión solidez y ciberseguridad, del Reglamento
Europeo de IA, se pone de manifiesto que los defectos del modelo deben ser tenidos en cuenta a la hora de considerar:

Art.15.5 – Precisión, solidez y ciberseguridad
… prevenir, detectar, combatir, resolver y controlar los ataques que traten de manipular [...] la información de entrada diseñada para hacer que el modelo de IA cometa un error («ejemplos adversarios» o «evasión de modelos») los ataques a la confidencialidad o los defectos en el modelo.

Los ataques dirigidos a descubrir y explotar defectos del sistema de IA aprovechan vulnerabilidades presentes en dos niveles: los defectos propios del modelo utilizado, y, los defectos derivados de su integración en el entorno software que lo rodea y como ha sido configurado.
-

-

Defectos propios del modelo: Son vulnerabilidades intrínsecas al diseño, entrenamiento o arquitectura del modelo de IA. Pueden surgir debido a errores en el diseño del modelo, datos de entrenamiento incompletos o sesgados, o configuraciones inapropiadas de los hiperparámetros. Estos defectos permiten a un atacante manipular las predicciones del modelo, generar resultados controlados o forzar errores sistemáticos.
Defectos en la integración del modelo: Surgen cuando el modelo se incorpora al ecosistema software o hardware en el que opera, debido a configuraciones incorrectas, dependencias inseguras, o fallos en la implementación y despliegue.
Estos defectos pueden ser explotados para alterar la funcionalidad del sistema, provocar fugas de información o facilitar otros tipos de ataques, como los de evasión y extracción

Estos defectos pueden detectarse y explotarse mediante ataques de oráculo, que consisten en interactuar con el sistema para inferir su funcionamiento interno y descubrir sus vulnerabilidades. Los ataques de oráculo, a su vez, pueden servir como punto de partida para variantes más específicas, como los ataques adversarios (evasión, extracción o inversión) ya descritos en esta guía.

4.5.1 Medidas aplicables
Proveedor
En lo referente a la explotación de defectos de modelo, el proveedor es responsable de identificar y mitigar las vulnerabilidades que el modelo pueda tener, y en su integración

41

con el ecosistema tecnológico. A modo de ejemplo, este proceso podría debe abarcar todo el ciclo de vida del sistema, desde su diseño y desarrollo hasta su implementación y operación, asegurando una revisión continua de posibles defectos. El conjunto de medidas aplicadas no solo podría contribuir a fortalecer la seguridad, sino que podría ayudar al cumplimiento los requisitos del artículo 15 del Reglamento.
A continuación, presentamos una lista de las vulnerabilidades que a modo orientativo pueden presentarse en este ámbito.
- Defectos intrínsecos del modelo.
- Existencia de sesgos en el modelo o en los datos.
- Compromiso del framework utilizado para el modelo del sistema de IA. Se entiende
este como el conjunto de librerías, elementos o artefactos software definidos en conjunto y mantenidos por un tercero, destinados a la implementación de sistemas de IA.
- Existencia de puertas traseras en el modelo.
- Exposición y acceso al código del modelo.
- Vulnerabilidades desconocidas en relación con potenciales defectos del modelo.
Las vulnerabilidades específicas y asociadas a los ataques de adversarios son propias del modelo, pero dada su naturaleza, se han tratado con detalle en los apartados anteriores.
En la siguiente tabla podemos ver a modo de ejemplo los controles de seguridad aplicables a las anteriores vulnerabilidades.
Vulnerabilidades

Controles de seguridad

Defectos intrínsecos del modelo

Cuando se seleccione un modelo para el sistema de IA, el proveedor debe conocer e investigar sus defectos intrínsecos tanto aquellos específicos dentro de la familia a la que pertenece el modelo (CNN, Randomforest, KNN, etc.) como aquellos aplicables a la finalidad prevista.
Estos defectos deberán estar inventariados en el modelo de amenaza y documentada la medida aplicada para mitigar su explotación como vulnerabilidades. La información recogida dependerá del modelo utilizado y sus defectos conocidos.

Existencia de sesgos en el modelo, o en los datos

Si bien la existencia de sesgos, puede ser un defecto explotable por el atacante, no es el objetivo de esta guía, y se describen en otras guías con más detalle (guía de datos y precisión).

Compromiso del framework del modelo

Los modelos se encuentran dentro de frameworks (marcos de trabajo) utilizados para el desarrollo y la implementación de sistemas de IA. Para mitigar el riesgo de compromiso, es fundamental que los frameworks utilizados estén actualizados y que se conozcan y monitoricen las vulnerabilidades publicadas,

42

Vulnerabilidades

Controles de seguridad como las registradas en CVE (Common Vulnerabilities and
Exposures) o CWE (Common Weakness Enumeration).
Además, se recomienda integrar procesos automatizados de revisión y análisis de vulnerabilidades en el ciclo de desarrollo del sistema, utilizando herramientas especializadas como:
-

OWASP Dependency-check: herramienta open-source que permite detectar vulnerabilidades conocidas en dependencias y librerías utilizadas en el sistema.

-

Dependency-Track: solución que facilita el análisis continuo de componentes y la gestión del riesgo asociado a dependencias de terceros.

Estas herramientas permiten identificar y alertar de manera proactiva sobre dependencias vulnerables, automatizando la monitorización y facilitando la actualización o sustitución de componentes inseguros. De esta forma, se refuerza la seguridad del framework y se reduce significativamente el riesgo de explotación.
Existencia de puertas traseras en el modelo

Para mitigar el riesgo de puertas traseras en los modelos de IA, se deben realizar pruebas periódicas y análisis de seguridad utilizando técnicas específicas:
-

-

-

Análisis periódicos de código tipo SAST (Static
Application Security Testing). Para identificar en las librerías y herramientas utilizadas vulnerabilidades que pudieran ser un vector de ataque para cualquiera de las vulnerabilidades descritas en esta guía. Además, permitirá identificar un modelo vulnerable o un framework de IA desactualizado o comprometido.
Análisis periódicos de código tipo DAST (Dynamic
Application Security Testing). El enfoque de un análisis tipo DAST centrado en inteligencia artificial, debe tener especial consideración los escenarios de acceso al modelo, control de los datos de entrada y el riesgo de escalado de privilegios en las políticas de seguridad que permitan la manipulación o la intervención en los datos de entrada.
Realización de prueba de penetración orientado a
Inteligencia Artificial y Machine Learning. En este caso, las pruebas deberán estar orientadas a realizar ataques de tipo adversario: evasión, inversión y extracción. Para facilitar la ejecución de estas pruebas, se recomienda el uso de frameworks específicos para seguridad en IA, como:

43

Vulnerabilidades

Controles de seguridad o

MLSecTools: herramienta diseñada para realizar pruebas de penetración y evaluar la robustez de modelos de Machine Learning frente a ataques adversarios.

o

Adversarial Robustness Toolbox (ART): framework open-source de IBM que proporciona un conjunto de herramientas para realizar pruebas de robustez y ataques adversaries en modelos de IA.

La integración de estas herramientas en el proceso de desarrollo y evaluación garantiza una detección más eficaz de vulnerabilidades relacionadas con puertas traseras y otros vectores de ataque, mejorando la resiliencia del modelo frente a manipulaciones maliciosas.
Exposición y acceso al código del modelo

La protección del código del modelo con políticas de acceso es fundamental para evitar manipulaciones errónea o malintencionadas, y las medidas de seguridad aplicables en este ámbito son las mismas que deben implementarse en cualquier sistema informático. Estos riesgos no son exclusivos de sistemas de IA, pero adquieren especial relevancia dada la sensibilidad y complejidad de los modelos utilizados.
Las políticas de acceso deben restringir el acceso al código únicamente al personal autorizado y cualificado. Esto incluye la implementación de controles de identidad y autenticación robustos, uso de MFA, certificados, etc. (autenticación multifactor), y el seguimiento de todas las interacciones mediante registro detallados (logs).
Los equipos del personal que participa en el desarrollo del sistema de IA deben estar adecuadamente protegidos frente a exfiltraciones, por ejemplo, no permitiendo utilizar los medios extraíbles (USB, disco externo…), o acceso a redes públicas.
En aquellos escenarios de trabajo con el repositorio central, el canal de comunicación securizado y cifrado (como VPN, etc.). El tránsito se tiene que realizar cifrado, para evitar la posibilidad de una manipulación del modelo en tránsito a través de ataques
Man-In-The-Middle.
Estas medidas aseguran la integridad del código y deben aplicarse de manera coherente tanto a sistemas tradicionales como a aquellos que implementan inteligencia artificial, garantizando la seguridad del entorno completo en el que opera el sistema.

44

Vulnerabilidades
Vulnerabilidades desconocidas en relación con potenciales defectos del modelo

Controles de seguridad
Análisis continuado de los indicadores de ciberseguridad del cuadro de mando para el seguimiento de la operación del sistema de IA.
Análisis de las auditorías del sistema de IA realizadas.

Tabla 3 Vulnerabilidades y controles de seguridad para defectos intrínsecos

Ejemplo – Asistencia al trabajo
En el análisis de riesgos realizado se ha identificado que el riesgo de poder falsear una identificación para el sistema de asistencia al trabajo, haciendo así sería posible que se generasen registros de asistencia que realmente no se han producido. Las vulnerabilidades de clasificación errónea y clasificación errónea aleatoria se han considerado defectos intrínsecos al modelo y relacionadas directamente con este riesgo.
Un atacante podría utilizar patrones adversarios, por ejemplo, en una camiseta, que pudiera causar una identificación errónea tanto de otro usuario como no localizar al usuario en su base de datos
(ver por ejemplo al respecto https://arxiv.org/pdf/2211.07383.pdf).
Como control de seguridad al desarrollar el modelo, para mitigar esta vulnerabilidad, el equipo de diseño utiliza el framework Highly Confident Near Neighbor (HCNN) en combinación con un Attribution-driven Causal Analysis.
Además, el framework del modelo utilizado y todas las librerías de ML asociadas siguen escaneos periódicos tipo SAST para localizar vulnerabilidades en el perímetro del sistema de IA que sirviesen de puerta de entrada.
En el entorno productivo, se somete de manera periódica a un análisis de tipo DAST centrado en una escalada de privilegios y acceso sobre el modelo. En este entorno y de manera periódica también, se realizan test de penetración orientados a IA, realizando ataques adversarios al sistema.

Para los defectos que pueden aparecer en el sistema de inteligencia artificial, como resultado de la configuración, integración o implementación se pueden identificar a modo de ejemplo las siguientes vulnerabilidades:
- El sistema de inteligencia artificial permite extraer información privada.
- Demasiada información proporcionada en el modelo en la información de salida.
- Demasiada información disponible de forma pública sobre el modelo.

45

- No se han considerado los ataques a los que el sistema de inteligencia de IA puede
estar expuesto.
- No existe un proceso de seguridad que mantenga el nivel de seguridad de los
componentes del sistema de IA.
- Uso de componentes vulnerables.
- Desajuste entre los entornos de desarrollo/pruebas/producción.
- No se han definido indicadores del correcto funcionamiento del sistema, haciendo
complejo identificar el compromiso del sistema.
- Malas prácticas por falta de concienciación en ciberseguridad.
- Contratos con terceras partes que no tienen un nivel de seguridad adecuado.
- Vulnerabilidades desconocidas como resultado de la configuración, integración o
implementación.

Vulnerabilidades

Controles de seguridad

Gestión de derechos de acceso inadecuada

Unos accesos inadecuados o no controlados pueden desembocar en la introducción de defectos por personal no cualificado.

El sistema de inteligencia artificial permite extraer información privada

El sistema de IA dispone de un mecanismo de privacidad diferencial; el diseño del modelo se ha realizado utilizando PATE
(Private Aggregation of Teacher Ensembles).

Uso de componentes vulnerables

En este caso ISO27001/2 y NIST 800-53 recomiendan:

Las técnicas utilizadas para proteger frente ataques de inversión son aplicables en la misma medida como controles de seguridad para esta vulnerabilidad.

-

Disponer de un inventario de los componentes utilizados y realizar un seguimiento constante de los mismos y sus versiones para estar al tanto de las vulnerabilidades encontradas en ellos utilizando las bases de datos de referencia para ellas (de tipo CVE, https://cve.mitre.org/ o de tipo CWE, https://cwe.mitre.org/).

Se pueden utilizar herramientas automáticas, como OWASP
Dependency-check, para comprobar los componentes utilizados

46

Vulnerabilidades

Controles de seguridad y realizar las comprobaciones en las bases de datos de referencia.
-

No se han definido indicadores del correcto funcionamiento del sistema, haciendo complejo identificar el compromiso del sistema.

Gestionar aquellos componentes obsoletos y planificar su eliminación de la cadena de producción. Sin ser de aplicación específica para IA, realizar análisis frecuentes de vulnerabilidades en todos los sistemas que rodean al sistema de IA.

El sistema de IA debe disponer de una serie de indicadores definidos y asociados a su naturaleza y finalidad prevista. Estos indicadores deben presentarse en la interfaz del sistema de IA, mediante un dahsboard o panel de información accesible, donde el responsable del despliegue pueda visualizar y conocer en tiempo real el estado de desempeño del sistema y detectar la posible existencia de fallos o posible situación de compromiso.
Para cumplir su propósito, estos indicadores deben incluir umbrales claramente definidos que permitan alertar sobre anomalías en el comportamiento del sistema. Un umbral fuera de rango puede ser indicativo de un fallo, un intento de ataque o una degradación del rendimiento, facilitando la respuesta temprana y mitigación de riesgo.
Los indicadores deben referirse, al menos, a las siguientes métricas:
-

Métricas de precisión y solidez del sistema de IA, para evaluar su desempeño en condiciones esperadas y adversas.

-

Indicadores distintivos de las bases de datos de entrenamiento utilizadas, tales como la distribución de los datos o la detección de sesgos, para orientar el correcto uso del sistema y alertar de posibles desviaciones.

La combinación de indicadores con umbrales definidos garantiza que el sistema pueda monitorearse proactivamente, facilitando la identificación de problemas en tiempo real y mejorando la resiliencia frente a situaciones inesperadas.

47
