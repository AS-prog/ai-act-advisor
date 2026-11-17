---
name: aesia-11-guia-ciberseguridad-08-reglamento-de-inteligencia-artificial-pa
description: "AESIA: aesia 11 guia ciberseguridad, sección «Reglamento de Inteligencia Artificial (parte 5)» (págs. 49-50). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-11-guia-ciberseguridad
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Reglamento de Inteligencia Artificial (parte 5)"
  paginas: 49-50
  origen: 2026-07-17-aesia-11-guia-ciberseguridad.pdf
  oficial: false
---
# Reglamento de Inteligencia Artificial (parte 5)

Vulnerabilidades

Controles de seguridad

Desajuste entre los entornos de desarrollo
/ pruebas / producción

Los sistemas entrenados en entornos de simulación pueden cometer errores en el mundo real debido a desajustes entre entornos de entrenamiento y de producción, o los entornos de simulación y producción. Ambos entornos deben estar definidos por descriptores de contenedores cuando sea posible o dispositivos hardware idénticos en los mismos entornos (IoT, edge computing).
En los escenarios de comercialización distintos al MLSaaS, las instrucciones deben ser claras (incluso con ejemplos de los contenedores software si es necesario) y las especificaciones hardware estarán basadas en estándares, para el caso de IoT o en los que se realice edge-computing.

Contratos con terceras partes que no tienen un nivel de seguridad adecuado

En ocasiones, una tercera parte puede desarrollar un elemento o sección del sistema de IA. Si el proveedor delega en una tercera parte la implementación completa del sistema, deberán tenerse en cuenta y cumplirse todas las medidas de seguridad descritas en esta guía.
Para el caso de un desarrollo parcial o específico del sistema de
IA (como modelos, preprocesado de datos o infraestructura de soporte), es fundamental integrar requisitos de seguridad en los contratos con terceros. Las recomendaciones de ISO 27001/2 o
NIST 800-53 incluyen integrar cláusulas específicas que establezcan controles de seguridad claros y verificables.
Ejemplos de estas cláusulas son:
-

Requisitos de auditorías periódicas: Obligar a la realización de auditorías de seguridad del desarrollo y los procesos del proveedor, con acceso a los resultados para el cliente.

-

Certificaciones de seguridad: Exigir que la tercera parte acredite el cumplimiento de estándares como ISO 27001,
ISO 27017 (para seguridad en la nube) o certificaciones equivalentes.

-

Revisión y gestión de vulnerabilidades: Incorporar la obligación de realizar pruebas de seguridad periódicas
(SAST/DAST), con la remediación de vulnerabilidades críticas en plazos específicos.

48

Vulnerabilidades

Controles de seguridad
-

Confidencialidad y protección de la información: Incluir políticas estrictas de protección de datos y propiedad intelectual en el desarrollo del sistema.

-

Planes de contingencia y respuesta a incidentes:
Establecer la obligación de contar con un plan de acción en caso de ciberincidentes que puedan afectar al sistema de IA.

Además, se recomienda monitorizar y revisar continuamente el cumplimiento de estos requisitos mediante indicadores de desempeño y revisiones periódicas de los servicios proporcionados.
Vulnerabilidades desconocidas como resultado de la configuración, integración o implementación.

Análisis continuado de los indicadores de ciberseguridad del cuadro de mando para el seguimiento de la operación del sistema de IA.
Análisis de las auditorías del sistema de IA realizadas. Se recomienda implementar herramientas de monitoreo en tiempo real basadas en IA que detecten patrones anómalos en el comportamiento del sistema. Adicionalmente, las auditorías periódicas deben incluir simulaciones de ataques adversarios para descubrir posibles defectos no documentados

Tabla 4 Vulnerabilidades y controles de seguridad para defectos de integración/configuración

Ejemplo – Sistema automático de concesión de ayudas
Este sistema se despliega en las instalaciones propias de la Administración Pública que hace uso de este, especialmente en las Comunidades Autónomas y Entidades Locales.
En ese proceso se ha identificado que puede existir un desajuste entre los entornos de desarrollo, pruebas y producción. Estos desajustes incluyen diferencias en las configuraciones del hardware, las versiones de las bibliotecas o frameworks utilizados, y las dependencias específicas del sistema.
Para mitigar este riesgo, y facilitar el trabajo del equipo de administración de sistemas y mantenimiento en la infraestructura de las CCAA y de las Entidades Locales, se encapsula el sistema de IA como un conjunto de servicios (entradas de datos, modelo, sistema de almacenamiento, etc.) a través de un sistema de mercado basado en descripción de contenedores (por ejemplo, Docker), de tal manera que, con el mismo mecanismo de descripción, se puede replicar el entorno en cualquier infraestructura, con las mismas condiciones y artefactos software.

49
