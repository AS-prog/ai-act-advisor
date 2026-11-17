---
name: aesia-05-guia-de-gestion-de-riesgos-12-anexos-parte-4
description: "AESIA: aesia 05 guia de gestion de riesgos, sección «Anexos (parte 4)» (págs. 60-63). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-05-guia-de-gestion-de-riesgos
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Anexos (parte 4)"
  paginas: 60-63
  origen: 2026-07-17-aesia-05-guia-de-gestion-de-riesgos.pdf
  oficial: false
---
# Anexos (parte 4)

6. Controles de privacidad de los datos
Control / medida técnica

Indicador efectividad

Implementar mecanismos para garantizar el adecuado uso y tratamiento de datos sensibles.

-

Número de atributos sensibles identificados y medidas implementadas.

Facilitar formación a los usuarios que trabajen con datos sensibles para garantizar que lo hacen de forma adecuada, con discreción y precaución para evitar, por ejemplo, revelar información crítica del sistema de IA a conocidos o familiares.

-

% de trabajadores conocedores de los requisitos de discreción y precaución establecidos

Obtener el consentimiento de individuos o grupos de individuos para el tratamiento de sus datos en el sistema de IA.

-

% de tratamientos de consentimiento aprobado

datos

Capacitar a los sistemas de IA para identificar sesgos o desviaciones indeseadas.

-

Número de identificadas

de

fuentes

con

sesgo

7. Controles y medidas sobre los datos
Control / medida técnica

Indicador efectividad

Seleccionar adecuadamente los conjuntos de datos de entrenamiento y prueba del sistema de IA para que sean coherentes con el entorno que pretenden representar.

-

Observación cualitativa de que los datos representan el entorno y realidad que pretender reproducir

Identificar los atributos confidenciales que se requieren para el comportamiento adecuado del sistema de IA.

-

Número de identificados

Implementar medidas de control y validación de conjuntos de datos (por ejemplo, métodos de retención de datos,
K-fold cross validation, leave-one-out of cross validation (LOO), remuestreo jackknife, muestreo estratificado, etc.).

-

Observación cualitativa de cada una de las medidas de validación de datos

atributos

confidenciales

8. Rendimiento del diseño y la implementación del modelo
Control / medida técnica
Desarrollar una especificación detallada del diseño, funcionalidades e implementación del sistema de IA.

Indicador efectividad
-

Grado de comprensión y conocimiento del diseño, funcionalidades y

59

funcionamiento por parte responsables del despliegue.

de

los

Detallar las técnicas de "feature engineering" utilizadas, como la selección, extracción y/o regulación de las características (features).

-

Número de técnicas documentadas

Especificar el modelo, algoritmos, hiperparámetros y la topología por escenario utilizados.

-

Nivel de madurez de la documentación del modelo, algoritmos, hiperparámetros y la topología por escenario utilizados.

Desarrollar una API para verificar las métricas de rendimiento del sistema de
IA.

-

% de responsables del despliegue que conoce y utiliza las herramientas para verificar el rendimiento

Desarrollar un análisis contrafactual para comprender mejor el comportamiento del sistema y evitar resultados no deseados.

-

Número de errores futuros predichos y corregidos

implementadas

9. Robustez, fiabilidad y resiliencia
Control / medida técnica

Indicador efectividad

Implementar técnicas de entrenamiento adversario, como inyectar ejemplos contradictorios (generados por diferentes estrategias de ataque) en los datos de entrenamiento).

-
-

Número de técnicas implementadas
Análisis cualitativo de la suficiencia de las medidas implementadas para garantizar la robustez, fiabilidad y resiliencia del modelo

Implementar mecanismos para reconstruir entradas dañadas, es decir, eliminar ruido
(por ejemplo, denoising autoencoder).

-

Número de reconstruidas

Agregar un sistema crítico para detectar cuándo el sistema de IA tiene demasiada confianza a pesar de una entrada ruidosa.

-

Número de detecciones de exceso de confianza del sistema identificadas

Desarrollar pruebas en entornos simulados y/o pruebas de campo y hacerlo periódicamente incluso después del despliegue del sistema de IA.

-

Número de pruebas implementadas

entradas

dañadas

60

8.6 ANEXO F – Glosario de términos
Esta guía se ha desarrollado con un enfoque que trata de explicar cada concepto presente en la guía cuando se expone, no obstante, se han recogido ciertos términos específicos en esta sección como aclaración adicional:
1. Amenaza: peligros a los que está expuesto el sistema que pueden terminar materializándose en un riesgo. Las amenazas de un sistema provienen principalmente de ataques externos (como un ciberataque), de no cumplir las políticas de seguridad (conectar dispositivos no autorizados a la red o utilizar contraseñas débiles) y de sucesos inesperados (como incendios o robos físicos, por ejemplo).
2. Vulnerabilidad: debilidad propia de un sistema que permite ser atacado y recibir un daño. Las vulnerabilidades se producen de forma habitual por una baja protección contra ataques externos.
3. Riesgo: posibilidad de que un sistema sufra un incidente y que una amenaza se materialice causando daños. El riesgo es, por lo tanto, la probabilidad de que la amenaza se materialice aprovechando una vulnerabilidad existente.
4. Medidas de control: en el contexto de la gestión de riesgos, son las medidas que deben tomarse para proteger el sistema de las amenazas, haciéndolo menos vulnerable y reduciendo la probabilidad de que el riesgo se materialice o en su lugar reduciendo el impacto que éste tendría en mi sistema.
5. Apetito al riesgo: es el volumen de riesgo que nuestra organización está dispuesta a aceptar en la búsqueda de lograr su misión.
6. Riesgo inherente: es el riesgo intrínseco de cada actividad, sin tener en cuenta las medidas de control que puedan implantarse.
7. Riesgo residual: es aquel riesgo que subsiste, después de haber implementado controles.
8. Ataque de fuzzing: técnica de testeo automatizado mediante la que se introducen datos inválidos, aleatorios o inesperados a un sistema informático.
9. HRAIS: los sistemas de alto riesgo basados en Inteligencia Artificial son aquellos con un impacto significativo en la vida de las personas y en sus derechos fundamentales.
Estos sistemas se utilizan en áreas críticas como la biometría, la educación, el empleo, la aplicación de la ley, la gestión de infraestructuras críticas, y otros sectores donde su mal uso podría causar daños considerables.
El reglamento en el artículo 6 y el Anexo III establecen los requisitos para el desarrollo, implementación y supervisión para garantizar su seguridad y fiabilidad.

8.7 ANEXO G – Política de Gestión de riesgos de IA
Este anexo, tal y como se indica en la sección 4.9, tiene como finalidad presentar una propuesta de

Política de Gestión de Riesgos en Inteligencia Artificial (IA) que sirva como referencia práctica para las organizaciones en el proceso de definición y desarrollo de su propio marco de gestión de riesgos. En este sentido, el contenido aquí descrito busca ofrecer una orientación general sobre los elementos y principios que debería contemplar una política de esta naturaleza.
61

No se espera que esta política sea adoptada de forma literal o completa por el lector, sino que actúe como un ejemplo de estructura y contenido que pueda adaptarse al contexto, naturaleza y nivel de madurez de cada organización. Su aplicación deberá ajustarse a los riesgos específicos identificados, analizados y evaluados a lo largo del proceso de gestión de riesgos en sistemas de IA, de acuerdo con las necesidades y particularidades de cada caso.
1. Resumen
Esta política establece un marco integral para la gestión de riesgos y gobernanza de los sistemas de Inteligencia Artificial (IA) en la organización, alineado con el Reglamento
Europeo de IA (UE 2024/1689) y las recomendaciones de la ISO/IEC 23894. Su propósito es proporcionar a la organización una guía clara para manejar de forma ética, segura y responsable los sistemas de IA, especialmente aquellos considerados de alto riesgo. La política define los objetivos y metas que orientan la identificación, evaluación, mitigación y seguimiento de riesgos, asegurando que las decisiones sobre IA se tomen de manera transparente y consistente.
Se establece la audiencia a la que aplica, incluyendo todo el personal que interviene en cualquier fase del ciclo de vida de los sistemas de IA, así como proveedores y colaboradores externos que puedan influir en su desempeño o cumplimiento normativo.
Se incluyen también los conceptos clave, ofreciendo un lenguaje común sobre sistemas de alto riesgo, riesgos operativos, éticos y legales, cumplimiento normativo y ciclo de vida de los sistemas.
La política asigna roles y responsabilidades específicas a cada área, asegurando que todos los actores conozcan su papel en la gestión de riesgos y supervisión de los sistemas de IA.
Se define la estrategia de riesgo, que abarca la evaluación de riesgos internos y de terceros, la identificación de riesgos residuales y la supervisión continua, consolidando un marco de gobernanza robusto, coherente y alineado con la normativa europea.
2. Política de uso de IA
La política de uso de IA complementa la gestión de riesgos, proporcionando directrices prácticas para el uso responsable de los sistemas de Inteligencia Artificial en la organización. Establece programas de entrenamiento y concienciación para todo el personal involucrado con sistemas de IA, asegurando que comprendan los riesgos operativos, legales y éticos, y fomentando un uso informado y responsable de la tecnología.
Se definen guías internas de uso, que indican los usos aceptables de la IA y las restricciones necesarias para proteger la seguridad, la privacidad y los derechos fundamentales.
Además, se incluyen procesos de preaprobación, de manera que cualquier nuevo sistema o modificación significativa pase por una revisión formal de riesgos antes de su implementación. Por último, la política establece un inventario de sistemas de IA, manteniendo un registro actualizado de todos los sistemas utilizados, sus responsables, nivel de riesgo y estado de cumplimiento, garantizando trazabilidad, control y supervisión continua en toda la organización.

62
