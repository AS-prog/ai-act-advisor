---
name: aesia-checklist-05-01-ejemplo-ilustrativo-del-desarrollo-05-5-respuesta-al-riesgo
description: "AESIA, checklist «05.01 Ejemplo ilustrativo del desarrollo de un sistema de gestión de riesgos v6», hoja «5.Respuesta al riesgo» (11 filas). Hoja del Excel de autoevaluación de las guías de requisitos, 2026-07-30."
metadata:
  type: reference
  documento: "aesia-checklist-05-01-ejemplo-ilustrativo-del-desarrollo"
  emisor: "AESIA"
  fecha: "2026-07-30"
  idioma: "es"
  hoja: "5.Respuesta al riesgo"
  filas: "11"
  origen: "2026-07-30-aesia-checklists-y-ejemplos.zip/05.01 Ejemplo ilustrativo del desarrollo de un sistema de gestión de riesgos v6.xlsx"
  oficial: false
---
# 5.Respuesta al riesgo

| Sistema | Componente del sistema | Amenaza | Impacto | Probabilidad | Riesgo inherente | Apetito al riesgo | Control | Descripción | Mitigación | Riesgo residual |
|---|---|---|---|---|---|---|---|---|---|---|
| Sistema de IA para la promoción de empleados | Datos de entrenamiento | Ataques de inserción en conjuntos de datos de entrenamiento | 4 | 3 | 12 | 4 | Monitorización de la seguridad | La IA es un campo que evoluciona rápidamente, especialmente en lo que respecta a su ciberseguridad. La comprobación periódica de los nuevos ataques y defensas debe integrarse en los procesos de mantenimiento del nivel de seguridad de las aplicaciones. Por lo tanto, el nivel de seguridad también debe evaluarse periódicamente para evitar ataques e intrusiones de terceros. | 0.7 | 3.6000000000000014 |
|  | Datos etiquetados | Elaboración de perfiles | 5 | 2 | 10 | 4 | Instaurar el aprendizaje federado | El aprendizaje federado son un conjunto de técnicas de entrenamiento que se desarrollan en varios servidores descentralizados que contienen muestras de datos locales, sin intercambiar sus muestras de datos. Esto evita la necesidad de transferir los datos y/o confiarlos a un tercero que no es de confianza y, por lo tanto, ayuda a preservar la privacidad de los datos. | 0.8 | 2 |
|  | Parámetros de entrenamiento | Sesgos en los datos | 4 | 3 | 12 | 4 | Análisis y limpieza de los datos de entrenamiento | Analizar los conjuntos de datos de entrenamiento y tratar las muestras sospechosas, puede ayudar a identificar sesgos en dichos datos así como también identificar posibles ataques de envenenamiento. | 0.7 | 3.6000000000000014 |
|  | Propietario de datos | Revelación de datos | 5 | 2 | 10 | 4 | Implantación de un modelo RBAC | Define la administración de derechos de acceso usando un modelo RBAC (Role Based Access Control) respetando el principio de menor privilegio. Esto debería cubrir todos los componentes del sistema de IA y permitir la protección de recursos como los parámetros y los datos usados. | 0.8 | 2 |
|  | Científicos de datos | Configuración errónea del sistema de IA | 3 | 1 | 3 | 4 | No requerido | N/A | 0 | 3 |
| Gestión de enfermedades crónicas - Bomba de insulina inteligente | Parámetros del sistema de IA | Manipulación de la integridad del sistema de IA | 4 | 3 | 12 | 5 | Monitorización del comportamiento del sistema de IA | Definir paneles de indicadores clave que integren indicadores de seguridad (picos de cambio en el comportamiento del modelo, etc.) para hacer un seguimiento del correcto funcionamiento del modelo, en particular para permitir la identificación rápida de anomalías. | 0.7 | 3.6000000000000014 |
|  | Datos de entrenamiento | Sobrecarga mediante un conjunto de datos etiquetados | 4 | 3 | 12 | 5 | Implantar herramientas de identificación de datos adversos | Las herramientas de detección de datos adversos pueden resultar muy útiles a la hora de identificar si un atacante ha modificado o no una entrada determinada. | 0.8 | 2.3999999999999986 |
|  | Propietario del sistema | Procesos no reproducibles del sistema de IA | 3 | 1 | 3 | 5 | No requerido | N/A | 0 | 3 |
|  | Herramientas de exploración de datos | Lógica desconocida del sistema de IA | 4 | 3 | 12 | 5 | Implantar herramientas para el análisis de la explicabilidad | Las herramientas de análisis de la explicabilidad de los sistemas de IA permiten generalmente adquirir una visión más precisa del funcionamiento y el proceso de toma de decisiones que está siguiendo el sistema de IA. | 0.8 | 2.3999999999999986 |
|  | Propietario de datos | Revelación de datos | 4 | 1 | 4 | 5 | No requerido | N/A | 0 | 4 |
|  | Científicos de datos | Configuración errónea del sistema de IA | 3 | 1 | 3 | 5 | No requerido | N/A | 0 | 3 |
