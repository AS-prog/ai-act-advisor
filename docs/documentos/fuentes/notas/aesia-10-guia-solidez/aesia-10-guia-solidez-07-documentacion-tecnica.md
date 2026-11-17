---
name: aesia-10-guia-solidez-07-documentacion-tecnica
description: "AESIA: aesia 10 guia solidez, sección «Documentación técnica» (págs. 39-41). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-10-guia-solidez
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Documentación técnica"
  paginas: 39-41
  origen: 2026-07-17-aesia-10-guia-solidez.pdf
  oficial: false
---
# Documentación técnica

5. Documentación técnica
Tan importante como la propia solidez, sus métricas asociadas y los mecanismos necesarios para garantizarla, es la documentación de la misma. La documentación técnica, tal y como se detalla en la guía correspondiente, se recomienda que contenga la siguiente información, al menos, en relación con la solidez:
- Las instrucciones sobre cómo obtener e interpretar las medidas y métricas de solidez,
incluyendo su explicación y monitorización, se pueden documentarse según la guía de Documentación para todos los posibles usuarios del sistema que deban monitorizar, desarrollar o intervenir en el sistema.
- Para que la solidez reportada sea accionable, tal documentación puede incluir los
rangos posibles de los parámetros configurables del modelo, rangos de datos de entrada y salida, así como las medidas de latencia y eficiencia estimadas para obtener la solidez establecida.
- Los valores mínimos aceptables para las métricas de solidez aplicables (y
garantizadas por el proveedor en la documentación) podrían reflejar y ser una señal de la calidad del sistema. Cuando éstas no se puedan garantizar, el proveedor facilitará mecanismos al responsable del despliegue para notificar al humano (según guía de supervisión humana) y/o posible interrupción/apagado del sistema.
- Dado que la solidez debe mantenerse a lo largo de todo el ciclo de vida del sistema,
la documentación se recomienda que se actualice tras cada modificación relevante del modelo, reentrenamiento o cambio de contexto operativo, reflejando las evidencias y resultados de las nuevas evaluaciones realizadas.
- Además, la documentación de la solidez se recomienda que explique a los diferentes
responsables del despliegue el funcionamiento del sistema en cuanto a desafíos comunes entre los principios de IA responsable. Por ejemplo, indicando garantías mínimas que provee el sistema para conocidos compromisos: entre imparcialidad global de grupo y privacidad individual (ya demostrado), el potencial compromiso entre solidez y privacidad. Puesto que estos compromisos entre requisitos han demostrado la posibilidad de estar en conflicto, la tarjeta del modelo de IA podrá afirmar las mínimas garantías esperadas, así como aquellos compromisos que se hayan probado pueden o no garantizarse.
- Para testear el modelo como caso sandbox se recomiendan metodologías con las
que el usuario deberá familiarizarse, especialmente si éste se convierte en proveedor reusando y modificando el producto: como la implantación canaria (donde el modelo se pone en producción para un pequeño segmento de usuarios, siendo monitorizado y controlado ante posibles problemas señalados por pruebas de integración y regresión).
- Se recomienda reportar junto con las fichas del conjunto de datos y cartas del
modelo, la Responsible AI scorecard como base aglutinadora de los principios de IA responsable que afectan la solidez del sistema.
En cualquier caso, la citada guía de documentación establece a modo orientativo cómo organizar dicha documentación y cómo relacionarla con las medidas descritas en esta guía.
Para disponer de un escenario completo y por tanto un marco de trabajo correcto, se
38

recomienda consultar ambas en conjunto para establecer cómo documentar la solidez del sistema.

5.1 Certificación de la solidez de modelos
Previamente a la puesta en operación y tras la implantación del modelo, se podrá certificar la solidez del modelo. Dada finalidad prevista del sistema de IA y tipo de datos que usa, se recomienda ver tipo de ataques y defensas (en ese particular, la guía de ciberseguridad realiza una revisión de los escenarios aplicables).
En términos de metodologías, y que por tanto pueden ayudar al proveedor a documentar adecuadamente la solidez del sistema de IA, se pueden establecer mecanismos para establecer ciertas garantías de solidez. Para ello, se pueden considerar las nuevas licencias y aquellas bajo preparación:
- Hippocratic License https://firstdonoharm.dev/
- RAIL (https://www.licenses.ai)
- Ethicas foundation (certificación/sello)
Ejemplos:
- Para estabilizar la solidez de modelos que procesan imagen contra distorsiones como
compresión, re-escalado o corte (cropping) se puede usar entrenamiento de estabilidad (Stability Training [79]).
- Para evaluar y robustecer modelos de procesamiento de lenguaje natural, se puede
usar aumento de datos y entrenamiento adversarial con TextAttack [12] [13].
- Para funciones objetivo-suaves como la population loss, se puede usar entrenamiento
adversarial por principios, por ejemplo, considerando una formulación de penalti
Lagrange perturbando la distribución de los datos en una bola Wasserstein.
Según el momento del ciclo de vida, la certificación de la solidez requiere de diferentes medidas organizativas.

1 Operación y monitoreo. Es fundamental evaluar la solidez de los sistemas de inteligencia artificial (IA) en su ámbito operativo y supervisar su evolución. Cuando no se alcanza el nivel de robustez requerido, se recomienda implementar acciones correctivas, como alertar al operador o activar modos de seguridad para prevenir fallos.
Los métodos formales pueden aplicarse en este contexto; sin embargo, suelen demandar mayores recursos de procesamiento, memoria y energía en comparación con otros enfoques.
o

Para hacer las explicaciones en el tiempo más robustas se puede usar aumento de datos contrafactual para entrenar el modelo con muestras de datos y sus contras fácticas y así evitar eventos contrafactuales desafortunados (unfortunate counterfactual events: UCEs [82]) o usar contra

39

o

fácticos plausibles [85, 86], los cuales no solo proveen mejor solidez que explicaciones contra fácticas más cercanas al ejemplo a explicar, pero también suponen una mayor imparcialidad individual [85].
Para explicar la deriva de los datos de entrada en el sentido de diferenciales de datos, se pueden usar ontologías e inducción de conceptos sobre conocimiento de fondo [87].

2 Reevaluación: El monitoreo de las pruebas de validación y verificación de los principios éticos de la UE podrían hacerse a través de los requisitos establecidos por licencias actualizadas regularmente.

40
