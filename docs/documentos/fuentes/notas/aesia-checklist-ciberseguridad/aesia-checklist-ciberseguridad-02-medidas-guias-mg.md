---
name: aesia-checklist-ciberseguridad-02-medidas-guias-mg
description: "AESIA, checklist «Ciberseguridad», hoja «Medidas guías (MG)» (12 filas). Hoja del Excel de autoevaluación de las guías de requisitos, 2026-07-30."
metadata:
  type: reference
  documento: "aesia-checklist-ciberseguridad"
  emisor: "AESIA"
  fecha: "2026-07-30"
  idioma: "es"
  hoja: "Medidas guías (MG)"
  filas: "12"
  origen: "2026-07-30-aesia-checklists-y-ejemplos.zip/Ciberseguridad_Checklist.xlsx"
  oficial: false
---
# Medidas guías (MG)

| Esta es una pestaña INFORMATIVA que expone las medidas explicadas con detalle en su correspondiente guía (recordamos que este es otro de los materiales proporcionados a las entidades). Recordamos que dichas medidas: • Han sido recogidas de buenas prácticas de la industria del software, y han sido validadas por entidades nacionales y europeas. • Son de mayor detalle que el de los estándares que se espera sean liberados en febrero de 2026 por la CE, ya que éstos recogen el QUE hay que hacer para cumplir el RIA, y estas medidas pueden llegar a recoger el CÓMO. • No todas tienen porque aplicar en cualquier sistema atendiendo a las características del mismo. • En base a la experiencia particular de cada sistema participante en el sandbox pueden existir medidas adicionales que sean igualmente válidas. Por eso en la pestaña "Medidas Adicionales (MA)" podrán ser agregadas. Adicionalmente, para cada medida existen unas cuestiones orientativas para contextualizarla, ya que incluyen los grandes “titulares” de cada una. La respuesta a las mismas puede dar una idea de si el sistema cumple o no la medida. |  |  |  |
|---|---|---|---|
| Tipo Medida | IDMedida | Descripción | Cuestiones orientativas para contextualizar las medidas |
| Medida Guía | MG01 | Nivel de ciberseguridad y consistencia adecuados | *¿Se han evaluado globalmente los riesgos de ciberseguridad en base a las amenazas actuales y emergentes? *¿Existen procedimientos establecidos para mantener la consistencia de las configuraciones de seguridad a lo largo del tiempo? |
| Medida Guía | MG02 | Sistemas resistentes a alteraciones de uso | *¿El diseño del sistema incorpora mecanismos para detectar y responder a usos no autorizados o anómalos? *¿Se dispone de controles de integridad que eviten la modificación indebida de la configuración o comportamiento del sistema? |
| Medida Guía | MG03 | Prevenir y controlar la manipulación del conjunto de datos | *¿Se han establecido protocolos y medidas técnicas para detectar, reportar y remediar anomalías o inconsistencias en el conjunto de datos? *¿Se han mapeado las fuentes de obtención de datos, qué controles de seguridad se establecen y quiénes son los responsables de vigilar dicha integridad? |
| Medida Guía | MG04 | Protección frente a ataques adversarios | *¿Se han identificado y evaluado los riesgos de ataques adversarios en cada fase del desarrollo del sistema? *¿El sistema incorpora técnicas de detección y mitigación específicas para neutralizar posibles ataques adversarios en producción? *¿Se llevan a cabo ejercicios de ataques adversarios de forma periódica para validar la resiliencia ante dichos ataques? |
| Medida Guía | MG05 | Protección frente a los defectos del sistema | *¿Se ha evaluado si el propio sistema inteligente puede tener riesgos de ciberseguridad específicos? |
| Medida Guía | MG06 | Protección frente a ataques de inversión y/o robo de modelo | *¿Se han adoptado técnicas de ofuscación, cifrado o separación de componentes para dificultar la extracción o copia del modelo? *¿Se dispone de controles de acceso y autenticación robustos para prevenir el acceso no autorizado al modelo? *¿Se han establecido protocolos de respuesta ante incidentes específicos de robo o manipulación del modelo? *¿Existen sistemas de monitorización y control de sesiones para evitar la ingeniería inversa del modelo a través de requests? |
| Medida Guía | MG07 | Protección frente a ataques de evasión | *¿El sistema incorpora mecanismos que permitan detectar intentos de evasión en la entrada o manipulación de datos como por ejemplo detección de datos fuera de dominio? *¿Se han implementado técnicas de preprocesamiento o similares para evitar que se produzcan este tipo de ataques? |
| Medida Guía | MG08 | Protección frente a ataques jailbreak | *¿Se han desarrollado y documentado controles específicos para prevenir el jailbreak como un firewall de requests a los sistemas? *¿El sistema dispone de mecanismos de verificación que bloqueen intentos de bypass a las restricciones o retorno del contenido del prompt del sistema? *¿Se ha probado la efectividad de estas medidas mediante simulacros o ejercicios de red team? |
| Medida Guía | MG09 | Protección frente a ataques de inferencia de pertenencia | *¿Se han evaluado las vulnerabilidades relacionadas con la posibilidad de inferir la participación de datos en el conjunto de entrenamiento? *¿Se han implementado técnicas de protección de la privacidad, como el uso de differential privacy, para minimizar estos riesgos? |
| Medida Guía | MG10 | Protección frente a ataque de canal lateral | *¿Se han mapeado todas las funciones o herramientas que el sistema inteligente acciona y que podrían ser de utilidad para un atacante? Ejemplo: consola de Python3, gestión de procesos, búsquedas online, etc. *¿El sistema depende de librerías no controladas por el equipo de desarrollo? |
| Medida Guía | MG11 | Protección frente a ataques de ingeniería social | *¿En la labor de supervisión humana o vigilancia poscomercialización el sistema inteligente puede verse afectado por algún tipo de acción relacionada con la ingeniería social? *¿Cómo se va a asegurar la comunicación segura y confiable entre los clientes y los responsables de vigilancia? |
