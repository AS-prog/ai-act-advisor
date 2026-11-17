---
name: aesia-11-guia-ciberseguridad-06-reglamento-de-inteligencia-artificial-pa
description: "AESIA: aesia 11 guia ciberseguridad, sección «Reglamento de Inteligencia Artificial (parte 3)» (págs. 33-40). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-11-guia-ciberseguridad
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Reglamento de Inteligencia Artificial (parte 3)"
  paginas: 33-40
  origen: 2026-07-17-aesia-11-guia-ciberseguridad.pdf
  oficial: false
---
# Reglamento de Inteligencia Artificial (parte 3)

Art.15.5 – Precisión, solidez y ciberseguridad
Medidas para prevenir, detectar, combatir, resolver y controlar los ataques que traten de manipular [...] la información de entrada diseñada para hacer que el modelo de IA cometa un error («ejemplos adversarios» o «evasión de modelos») […]

Para ello se deben establecer los controles de seguridad necesarios para evitar que la introducción de determinados datos de entrada haga cometer un error al modelo o permita extraer información de este. Se trata de ataques adversarios de tipo oráculo, extracción, inversión o ataques de evasión en el sistema de inteligencia artificial de alto riesgo.

4.4.1 Medidas aplicables
Proveedor
Se recomienda que el proveedor identifique las vulnerabilidades relacionadas con la manipulación de los datos de entrada, las cuales pueden hacer que el modelo cometa errores o permitir la inferencia de los datos usados en el entrenamiento a través de consultas al modelo. Se puede evaluar y priorizar la lista de vulnerabilidades en función de la finalidad prevista del sistema de IA. A continuación, se presenta una lista de vulnerabilidades a modo ilustrativo:
- Transferencia de ataques adversarios.
- Gestión inadecuada de los derechos de acceso al modelo
- Falta de consideración de los posibles ataques a los que el sistema de IA puede
estar expuesto.
- Ausencia de un proceso de seguridad que mantenga el nivel de protección de los
componentes del sistema de IA.
- Mecanismo débil de control de accesos a los componentes del sistema de IA.
- Falta de detección de entradas de datos anómalos, aumentando la exposición a los
ataques de pertenencia para inferir datos o ataques de inversión.
- No considerar en el diseño e implementación del modelo la posibilidad de ataques
de evasión.
- No considerar en el diseño e implementación del modelo la posibilidad de ataques
adversarios, por ejemplo: clasificación errónea, clasificación errónea origen/objetivo, clasificación errónea aleatoria y reducción de confianza.
- Uso de modelos ampliamente conocidos en el sistema de IA, lo que permite la
réplica total o parcial y, por tanto, facilita la transferencia de ataques adversarios.
- Entrada de datos totalmente controlada por el atacante (sin preprocesamiento o
por vulneración del mecanismo de entrada), lo que permite crear pares de datos de entrada y salida. Exposición a ataques de inversión, tanto ataques de inferencia de

32

pertenencia (Membership Inference Attack), que permitan saber si unos datos de entrada han formado parte o no del set de datos de entrenamiento, como ataques de inferencia de propiedades (Property Inference) que busca conocer los datos usados en el modelo. Este riesgo afecta a la privacidad de los datos personales utilizados en el entrenamiento y, por tanto, debe tenerse en cuenta como riesgo de ciberseguridad, según establece la norma ISO7IEC 27001. Ambos ataques pueden preceder o ir dirigidos a conseguir la reconstrucción del conjunto completo de datos de entrenamiento.
- Exceso de información disponible en el modelo. Exceso de información sobre el
modelo en sus salidas.
- Falta de consideración de la posibilidad de ataques de extracción.
- Robo o compromiso del modelo.
En el manual de uso del sistema se recomienda que el proveedor enumere las vulnerabilidades asociadas a la manipulación de los datos en los que el sistema se encuentra expuesto. Aquellas medidas que han sido puestas en marcha durante el entrenamiento del modelo se recomiendan que estén indicadas. Si el sistema no se ofrece como un MLSaaS, o por su naturaleza pudiera encontrase físicamente en las instalaciones del responsable del despliegue, el manual de instrucciones y su documentación podrían hacer referencia a las vulnerabilidades de aplicación y a la forma de aplicar aquellos controles de seguridad que puedan ser de su responsabilidad.
Las medidas técnicas aplicables en este caso son los controles de seguridad que impiden o mitigan la explotación de las vulnerabilidades. Si algunas de las medidas deben ser realizadas en el proceso de instalación y utilización del sistema por parte del responsable del despliegue, se recomienda indicarlo en el manual de instrucciones.
A continuación, se muestra una lista detallada de vulnerabilidades a modo orientativo y no vinculante:
Vulnerabilidades

Controles de seguridad

Transferencia de ataques adversarios

En la medida de lo posible, se debe evitar utilizar modelos en el sistema de IA que sean de amplio uso y conocimiento, ya que estos pueden contener vulnerabilidades conocidas que faciliten ataques de transferencia. También es recomendable evitar partir de modelos de base o frameworks de trabajo en versiones ya comprometidas, que permitan identificar el ataque y explotar esta vulnerabilidad.

Todas las familias de modelos y sistemas de IA tienen vulnerabilidades conocidas o aspectos en los que son más susceptibles a ciertos tipos de ataques adversarios. Por ello,

33

Vulnerabilidades

Controles de seguridad es fundamental conocer, identificar y proteger el sistema de
IA desde la fase de diseño, implementación, verificación y validación hasta su fase de puesta en marcha y funcionamiento.
Además, para reducir el riesgo asociado al uso de modelos ampliamente conocidos:
-

Se recomienda aplicar técnicas de ofuscación o enmascaramiento que dificulten la identificación y explotación del modelo por parte de un atacante.

-

Evaluar de manera proactiva la robustez del sistema frente a ataques transferidos mediante pruebas específicas y metodologías de evaluación continua.

Gestión inadecuada de los derechos de acceso al modelo

Políticas de acceso, ver apartado 7 Anexos

Falta de consideración de los posibles ataques a los que el sistema de
IA puede estar expuesto

Integrar las especificidades de seguridad para sistemas de
IA en la estrategia de sensibilización y asegurarse que todas las partes implicadas lo reciben (ver Anexo II: Formación en ciberseguridad y sistemas de inteligencia artificial de alto riesgo).

7.1 Anexo I: Políticas de acceso. Una aproximación a sistemas de inteligencia artificial de alto riesgo.

Seguimiento del estado del arte de los ataques adversarios:
https://csrc.nist.gov/publications/detail/nistir/8269/draft
Ausencia de un proceso de seguridad que mantenga el nivel de protección de los componentes del sistema de IA

ISO27001/2 - NIST 800-53: Realizar auditorías periódicas y regulares sobre el modelo en base a las medidas detalladas en esta guía, y realizar planes de acción tras cada caso.

Falta de detección de entradas de datos anómalos

Implementar herramientas específicas para detectar si un valor de entrada puede ser un ejemplo adversario. Una estrategia efectiva es añadir al sistema subredes de detección de adversarios, que funcionan de manera separada al modelo principal. Estas subredes se entrenan específicamente para identificar patrones asociados a

Realizar una aproximación equipo azul /equipo rojo; el equipo azul desarrolla el modelo y el equipo rojo lo pone a prueba con diversos formatos de ataque de tipo adversario al mismo (caja blanca, gris, negra).

34

Vulnerabilidades

Controles de seguridad ataques adversarios, analizando características particulares de las entradas sospechosas y alertando sobre posibles intentos de manipulación.
Además, se deben implementar métricas de confianza y análisis de distribución para robustecer el modelo. Esto incluye establecer umbrales que generen alertas ante resultados con alta incertidumbre o valores alejados del comportamiento esperado, lo cual permite identificar posibles ataques adversarios o anomalías.
Complementariamente, es vital integrar:
-

Mecanismos de detección Out-of-Domain (OoD).
Estos permiten identificar datos que se sitúan en las fronteras de clasificación o fuera del espacio de solución previsto. En sistemas no basados en clasificación, este enfoque se centra en localizar outliers y analizar su relación con otras variables críticas del sistema.

-

Control de orígenes de llamadas al sistema:
Monitorizar y detectar solicitudes sospechosas que intenten explorar o manipular el espacio de solución del modelo. Los accesos provenientes de estos orígenes deben ser bloqueados temporal o permanentemente, o ralentizados mediante el aumento de los tiempos de respuesta.

-

Niveles de confianza y mecanismos de alerta:
Establecer un mecanismo que asocie cada resultado del modelo a un nivel de confianza. Los valores bajos de confianza deben activar alertas automáticas para advertir de entradas potencialmente anómalas.

En la interfaz del sistema, se debe incluir:

-

Registros de entradas anormales: Un sistema de trazabilidad que permita registrar y analizar las entradas sospechosas.

35

Vulnerabilidades

Controles de seguridad
-

Alertas visuales y avisos al usuario: Facilitar que los usuarios sean advertidos de posibles entradas anómalas en tiempo real.

Para facilitar la implementación, se pueden integrar herramientas open-source o comerciales especializadas en la detección de entradas anómalas y ejemplos adversarios.
Se listan a continuación algunos ejemplos de herramientas open-source:
-

Adversarial Robustness Toolbox (ART) de IBM: Un framework open-source que proporciona métodos para evaluar y mejorar la robustez de los modelos frente a ejemplos adversarios.

-

Foolbox: Herramienta open-source para pruebas de robustez y generación de ejemplos adversarios en modelos de aprendizaje automático.

-

TensorFlow Privacy y PyTorch-based libraries:
Soluciones que ayudan a aplicar técnicas de detección y mitigación, como análisis de confianza y monitoreo de outliers.

No considerar en el diseño e implementación del modelo la posibilidad de ataques de evasión

Diseñar un modelo resiliente contra ataques de evasión mediante aleatorización de entradas, regularización del gradiente de entrada y destilación defensiva (defensive distillation) Utilizar recursos de referencia para el estado del arte de los ataques de adversarios de referencia de las que existen diferentes formatos, muchas de ellas de código abierto. Estos conjuntos de herramientas proporcionan conjuntos de técnicas adecuadas para verificar el modelo adecuadamente frente a ataques adversarios.

No considerar en el diseño e implementación del modelo la posibilidad de ataques de evasión

MITRE ATLAS (https://atlas.mitre.org/) es una extensa base de conocimiento con información actualizada sobre las amenazas y casos de estudio basado en observaciones de mundo real y de sistemas de inteligencia artificial operativos.

36

Vulnerabilidades

Controles de seguridad

Clasificación errónea y clasificación errónea aleatoria

Los atacantes generan una muestra que no está en la clase de entrada del clasificador objetivo pero que es clasificada por el modelo como esa clase de entrada particular. En la variante aleatoria el resultado puede ser cualquiera diferente de la clasificación correcta.
Para mitigar estos riesgos, se proponen dos estrategias:
- Framework Highly Confident Near Neighbor (HCNN):
Utilizado para validar si la clasificación de una muestra es coherente con sus "vecinos" más cercanos en el espacio de características, filtrando aquellas que generan una confianza artificialmente alta pero errónea.
- Attribution-driven Causal Analysis: Un análisis de
causalidad basado en atribuciones que permite explicar decisiones individuales.

Clasificación errónea dirigida

El objetivo del ataque es obtener un resultado específico (o clasificación) para una entrada dada. Para mitigarlo:
Eliminación de características: Feature Denoising
Una técnica que mitiga especialmente este tipo de ataques es incluir en el set de entrenamiento ejemplos adversarios conocidos de manera que el sistema se entrene con ejemplos adversarios construidos para tal fin.
Compresión o exprimido de las características (feature squeezing).

Reducción de confianza

Este tipo de ataque está destinado a reducir la confianza del sistema en una clasificación correcta, para que de esta manera se influya en la percepción que actúa en el proceso de supervisión.
Puede mitigarse mediante el control de las entradas, con la disminución de entradas admitidas al sistema en un formato específico o procedentes de una dirección IP, origen o demarcación sospechosa. Estas entradas podrán bloquearse en caso de riesgo.

Uso de modelos ampliamente conocidos en el sistema

Utilizar modelos con menos riesgo de transferencia.
Durante el proceso de elección del modelo, conocer y analizar los riesgos de transferencia o, en caso general, su

37

Vulnerabilidades

Controles de seguridad

de IA facilitando la transferencia de ataques adversarios

popularidad y uso generalizado, para seleccionar aquel que tenga un riesgo menor de transferencia.

Uso de modelos ampliamente conocidos en el sistema de IA facilitando la transferencia de ataques adversarios

No reutilizar modelos directamente desde internet, sin su comprobación y validación. En la medida de lo posible y equilibrando la finalidad prevista y protección, seleccionar modelos en los que la exposición de ataques de adversarios, siendo conocido, tenga controles de seguridad establecidos.

Datos de entrada total o parcialmente controlados por el atacante

Aplicar modificaciones a los datos de entrada, realizando operaciones de preprocesado: en la medida que no comprometa la exactitud del sistema, realizar una normalización de los datos, eliminación de ruido de los datos. La eliminación de valores fuera de los rangos esperados puede mitigar el control de los datos de entrada por parte del atacante.
Los sistemas NLP, pueden ser muy vulnerables frente a la introducción de modificaciones en los datos de entrada. La generación de textos adversarios durante el entrenamiento utilizando, por ejemplo, CAT-Gen.
Mantener un histórico de datos de entrada que permita detectar datos de entrada extremadamente cercanos, y levantar una alarma en el sistema por niveles (registro, notificación y bloqueo).
Si los datos se introducen de manera directa al modelo por parte del posible atacante, esta introducción de datos debe estar controlada por políticas de acceso adecuadas (ver
Anexos
7.1 Anexo I: Políticas de acceso. Una aproximación a sistemas de inteligencia artificial de alto riesgo). El acceso a introducir datos directamente al modelo no debe ser público salvo que sea estrictamente necesario, y en ese caso, deberán controlarse como se ha indicado.

Vulnerabilidad a ataques de inferencia

La investigación y artículos publicados en este ámbito indican que la utilización de técnicas de privacidad

38

Vulnerabilidades

Controles de seguridad

de pertenencia
(Membership Attacks)

diferencial supone una mitigación efectiva a estos tipos de ataques.
También es posible crear conjuntos de datos privados, diferencialmente derivados de datos desprotegidos. Para ello se pueden utilizar herramientas que permitan estas acciones.
La utilización de Neural dropout o Model stacking puede incrementar la resiliencia del sistema de IA frente a este ataque.

Ataques de Inferencia de Propiedades
(Property Inference)

Establecer un límite por origen (IP, usuario, dispositivo) y disponer de mecanismos de alarma y bloqueo de orígenes.

No considerar la existencia de posibilidad de ataques de extracción

Al igual que los ataques de transferencia, se debe controlar la información que retorna el sistema, así como los orígenes con demasiadas consultas, pues es un vector de ataque para los ataques de extracción.

Todas las entradas de los datos al modelo accesibles deben tener un mecanismo de validación.

Existen herramientas que, dentro de sus capacidades, permiten generar defensas modificando la salida del modelo haciendo redondeos o añadiendo ruido estadístico, para dificultar así al atacante el conocimiento del razonamiento del modelo. Se recomienda la utilización de estas herramientas para este tipo de control de seguridad.

Robo del modelo

Control de versiones del modelo, para evitar que se pueda modificar de manera malintencionada el modelo en cualquier punto del ciclo de vida desde la concepción y el diseño, entrenamiento y validación como en producción.
Como se ha indicado en el caso de ataques de transferencia, es conveniente que la exposición del modelo
(incluso, la publicación de su código fuente) no suponga una vulnerabilidad en sí misma. Esto se consigue aplicando los criterios de protección frente a otras vulnerabilidades a lo largo del sistema, de tal manera que incluso en un nivel de exposición del modelo no suponga una vulnerabilidad.

39
