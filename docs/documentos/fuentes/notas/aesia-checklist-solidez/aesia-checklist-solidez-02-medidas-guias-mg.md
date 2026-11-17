---
name: aesia-checklist-solidez-02-medidas-guias-mg
description: "AESIA, checklist «Solidez», hoja «Medidas guías (MG)» (17 filas). Hoja del Excel de autoevaluación de las guías de requisitos, 2026-07-30."
metadata:
  type: reference
  documento: "aesia-checklist-solidez"
  emisor: "AESIA"
  fecha: "2026-07-30"
  idioma: "es"
  hoja: "Medidas guías (MG)"
  filas: "17"
  origen: "2026-07-30-aesia-checklists-y-ejemplos.zip/Solidez_Checklist.xlsx"
  oficial: false
---
# Medidas guías (MG)

| Esta es una pestaña INFORMATIVA que expone las medidas explicadas con detalle en su correspondiente guía (recordamos que este es otro de los materiales proporcionados a las entidades). Recordamos que dichas medidas: • Han sido recogidas de buenas prácticas de la industria del software, y han sido validadas por entidades nacionales y europeas. • Son de mayor detalle que el de los estándares que se espera sean liberados en febrero de 2026 por la CE, ya que éstos recogen el QUE hay que hacer para cumplir el RIA, y estas medidas pueden llegar a recoger el CÓMO. • No todas tienen porque aplicar en cualquier sistema atendiendo a las características del mismo. • En base a la experiencia particular de cada sistema participante en el sandbox pueden existir medidas adicionales que sean igualmente válidas. Por eso en la pestaña "Medidas Adicionales (MA)" podrán ser agregadas. Adicionalmente, para cada medida existen unas cuestiones orientativas para contextualizarla, ya que incluyen los grandes “titulares” de cada una. La respuesta a las mismas puede dar una idea de si el sistema cumple o no la medida. |  |  |  |
|---|---|---|---|
| Tipo Medida | IDMedida | Descripción | Cuestiones orientativas para contextualizar las medidas |
| Medida Guía | MG01 | Adquirir conocimientos básicos sobre solidez | *¿Se ha asegurado una formación adecuada del personal involucrado en el desarrollo e implementación en aspectos clave de solidez del sistema de IA? |
| Medida Guía | MG02 | Establecer objetivos claros de solidez, definir métricas asociadas | *¿Se han establecido las propiedades y métricas de solidez del sistema y los requisitos que deben cumplir acorde a la finalidad prevista y al análisis de riesgos realizado, con evidencias? |
| Medida Guía | MG03 | Identificar las características críticas del sistema | *¿Durante el diseño del sistema se han identificado las características reconocidas para la medición de solidez y se han identificado su separabilidad (posibilidad de ser medidas por separado)? |
| Medida Guía | MG04 | Uniformización de entornos de validación y producción | *¿Los diferentes entornos por los que evoluciona el sistema en su ciclo de vida (desarrollo, integración, preproducción y producción) tienen características equivalentes acorde a los objetivos de solidez definidos? |
| Medida Guía | MG05 | Validación en entornos hardware que repliquen las capacidades finales del sistema | *¿La verificación y validación de las métricas escogidas se ha realizado en entornos hardware que replican exactamente las capacidades finales a las que tendrá acceso el sistema de IA? |
| Medida Guía | MG06 | Medición de rendimiento y complejidad computacional | *¿Se han definido varias métricas de solidez relativas al rendimiento (FLOPS, eficiencia, FLOPY, Latencia etc.) del sistema en el hardware establecido para su funcionamiento? |
| Medida Guía | MG07 | Diseñar experimentos para evaluar la solidez | *¿Existe un plan de experimentos para demostrar la solidez del sistema basados al menos en uno de los siguientes métodos: estadísticos, formales, empíricos o pruebas prácticas? |
| Medida Guía | MG08 | Realizar experimento con datos reales, analizar e interpretar sus resultados | *¿Existen evidencias de dichos experimentos realizados, su análisis e interpretación y su impacto en los parámetros de solidez del sistema de IA? |
| Medida Guía | MG09 | Implementar capacidades para observar, supervisar y reportar degradaciones | *¿Se han definido procedimientos y medidas técnicas que permitan monitorizar la solidez, como por ejemplo interfaces de sistema mostrando las métricas de solidez seleccionadas de manera agregada y en históricos y registros de operaciones? |
| Medida Guía | MG10 | Configurar técnicas de alerta y protocolos de fallo seguro | *¿Existen mecanismos de alerta cuando la solidez del sistema no se encuentre dentro de los parámetros establecidos? |
| Medida Guía | MG11 | Establecer comités de evaluación para prever incoherencias o fallos | *¿Se han establecido comités o equipos específicos encargados de evaluar proactivamente incoherencias o posibles fallos en la solidez del sistema? |
| Medida Guía | MG12 | Implementar mecanismos automáticos para la recuperación en caso de fallo | *¿Existen mecanismos automáticos diseñados e implementados para garantizar la recuperación del sistema en caso de fallo? |
| Medida Guía | MG13 | Implementar herramientas para garantizar la redundancia geográfica, el versionado y la escalabilidad | *¿Se han implementado herramientas o procedimientos específicos para garantizar la redundancia geográfica, la gestión adecuada del versionado y la escalabilidad del sistema? |
| Medida Guía | MG14 | Para sistemas que siguen aprendiendo: Asegurar que no se degrade la solidez, precisión y rendimiento del sistema | *¿Se monitoriza para sistemas que continúan aprendiendo todas las métricas establecidas (relativas también a precisión y ciberseguridad) y que permitan conocer si el sistema sigue dentro de los parámetros de diseño? |
|  | MG15 | Para sistemas que siguen aprendiendo: Adoptar estrategias de mitigación que minimicen la desviación del modelo y prevengan la acumulación de sesgos | *¿Se han establecido planes de seguimiento y control, con sus medidas de acción para la degradación del modelo en base a model deviation, concept drift, data drift etc.? |
|  | MG16 | Para sistemas que siguen aprendiendo: Registrar formalmente los casos de interacción e interoperabilidad con otros sistemas o humanos, junto con la retroalimentación recibida | *¿Se registran formalmente las interacciones, interoperabilidad y retroalimentación recibida durante el ciclo de vida del sistema, especialmente en sistemas que continúan aprendiendo, para asegurar la trazabilidad y mejorar la solidez? |
