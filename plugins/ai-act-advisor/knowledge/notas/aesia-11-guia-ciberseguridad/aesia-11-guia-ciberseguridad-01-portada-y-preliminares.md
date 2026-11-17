---
name: aesia-11-guia-ciberseguridad-01-portada-y-preliminares
description: "AESIA: aesia 11 guia ciberseguridad, sección «Portada y preliminares» (págs. 1-8). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-11-guia-ciberseguridad
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Portada y preliminares"
  paginas: 1-8
  origen: 2026-07-17-aesia-11-guia-ciberseguridad.pdf
  oficial: false
---
# Portada y preliminares

11

Empresas desarrollando cumplimiento de requisitos

Esta guía ha sido desarrollada en el marco del desarrollo del piloto español de sandbox regulatorio de IA, en colaboración entre los participantes, asistencias técnicas, potenciales autoridades nacionales competentes y el grupo asesor de expertos del sandbox.
La guía tiene como objetivo servir de apoyo introductorio a la normativa europea de Inteligencia Artificial y sus obligaciones aplicables. Si bien no tiene carácter vinculante ni sustituye ni desarrolla la normativa aplicable, proporciona recomendaciones prácticas alineadas con los requisitos regulatorios a la espera de que se aprueben las normas armonizadas de aplicación para todos los estados miembros.
El presente documento está sujeto a un proceso permanente de evaluación y revisión, con actualizaciones periódicas conforme al desarrollo de los estándares y las distintas directrices publicadas desde la Comisión Europea. La guía ha sido actualizada conforme al Ómnibus digital que modifica el Reglamento de
Inteligencia Artificial.
Entre las referencias técnicas relevantes actualmente aplicables, destacan las normas ISO/IEC 27001:2022 “Information security, cybersecurity and privacy protection — Information security management systems — Requirements” e
ISO/IEC 27017:2015 “Information technology — Security techniques — Code of practice for information security controls based on ISO/IEC 27002 for cloud services”, que servirán de base para garantizar la seguridad de la información y la protección de los servicios en la nube en el desarrollo y despliegue de sistemas de inteligencia artificial en el contexto del cumplimiento del Reglamento Europeo de
Inteligencia Artificial.

Guía 11. Ciberseguridad © 2026 por el Ministerio para la Transformación Digital y de la
Función
Pública está bajo una licencia
Creative Commons Atribución 4.0 Internacional.
NIPO: 230260144
Fecha de revisión: 17 de julio de 2026

1

-

Control de versiones del documento:

Versión

Fecha de versión

Cambios principales

1.0.

10/12/2025

Publicación de la primera versión

17/07/2026

Adaptación de acuerdo con los cambios introducidos por el Ómnibus Digital y cambios menores de forma

2.0.

2

Contenido general
1.

Preámbulo ............................................................................................................................................ 6

2.

Introducción ......................................................................................................................................... 9

3.

Reglamento de Inteligencia Artificial .............................................................................................. 14

4.

¿Cómo abordar los requisitos? ........................................................................................................ 17

5.

Documentación técnica .................................................................................................................... 48

6.

Cuestionario de autoevaluación ...................................................................................................... 50

7.

Anexos ................................................................................................................................................ 51

8.

Referencias, estándares y normas ................................................................................................... 65

3

Índice detallado
1.

Preámbulo ............................................................................................................................................ 6

1.1 Objetivo del documento ...................................................................................................................... 6
1.2 ¿Cómo leer esta guía? .......................................................................................................................... 6
1.3 ¿A quién está dirigido? ......................................................................................................................... 7
1.4 Casos de uso utilizados en la guía ....................................................................................................... 7
2.

Introducción ......................................................................................................................................... 9

2.1 ¿Qué es la ciberseguridad para IA? .................................................................................................... 9
2.2 ¿Cuáles son las principales amenazas? ............................................................................................. 10
3.

Reglamento de Inteligencia Artificial .............................................................................................. 14

3.1 Análisis previo y relación de los artículos ......................................................................................... 14
3.2 Requisitos del Reglamento de IA ...................................................................................................... 15
3.3 Correspondencia del artículo con los apartados de la guía ........................................................... 16
4.

¿Cómo podemos abordar los requisitos? ...................................................................................... 17

4.1 Nivel de ciberseguridad y consistencia .......................................................................................... 17
4.1.1 Medidas aplicables .......................................................................................................................... 18
4.2 Sistemas resistentes a alteraciones de uso ..................................................................................... 22
4.2.1 Medidas aplicables .......................................................................................................................... 24
4.3 Vulnerabilidades y controles de seguridad para datos ................................................................ 26
4.3.1 Medidas aplicables .......................................................................................................................... 27
4.4 Protección frente a ataques adversarios ......................................................................................... 30
4.4.1 Medidas aplicables .......................................................................................................................... 32
4.5 Ataques a los defectos del sistema de IA ....................................................................................... 41
4.5.1 Medidas aplicables .......................................................................................................................... 41
5.

Documentación técnica .................................................................................................................... 52

6.

Cuestionario de autoevaluación ...................................................................................................... 54

7.

Anexos ................................................................................................................................................ 55

7.1 Anexo I: Políticas de acceso. Una aproximación a sistemas de inteligencia artificial de alto riesgo .......................................................................................................................................................... 55
7.1.1 Para el proveedor ............................................................................................................................. 55
7.1.2 Para el responsable del despliegue ............................................................................................... 57
7.2 Anexo II: Formación en ciberseguridad y sistemas de inteligencia artificial de alto riesgo ..... 58
7.2.1 Para el proveedor ............................................................................................................................. 58
7.2.2 Para el responsable del despliegue ............................................................................................... 60
7.3 Glosario orientativo ........................................................................................................................... 61
8.

Referencias, estándares y normas ................................................................................................... 71

8.1 Estándares ............................................................................................................................................ 71

4

8.2 ENISA .................................................................................................................................................... 71
8.2.1 Artificial Intelligence cybersecurity challenges ............................................................................. 71
8.2.2 Securing Machine Learning............................................................................................................. 71
8.2.3 Cybersecurity of AI and standardization ........................................................................................ 72
8.2.4 Multilayer Framework for Good Cybersecurity Practices for AI .................................................. 72
8.3 Otras referencias ................................................................................................................................. 72

5

1. Preámbulo
1.1 Objetivo del documento
Esta guía está destinada a desarrollar el cumplimiento de las medidas necesarias en materia de ciberseguridad para sistemas de IA, específicamente en los aspectos relativos a inteligencia artificial, de manera que esta se integre en un esquema de ciberseguridad más amplio. El objetivo principal de esta guía es proporcionar a las empresas los conocimientos y pasos necesarios para implementar los requisitos de ciberseguridad en sistemas de IA, conforme a lo establecido en el artículo 15 del
Reglamento Europeo. Su aplicación es responsabilidad tanto del proveedor como del responsable del despliegue del sistema.

1.2 ¿Cómo leer esta guía?
En el apartado introductorio, a título ilustrativo y no vinculante, se abordan lo que entendemos por ciberseguridad para sistemas de IA de alto riesgo, en relación con el
Reglamento Europeo de IA. Este apartado, a modo de ejemplo, sienta las bases conceptuales de la guía.
En el segundo apartado, a título orientativo, se establecen cómo podrían interpretarse a modo de recomendación los requisitos establecidos en el Artículo 15: precisión, solidez y ciberseguridad, del Reglamento Europeo de IA. Es importante aclarar que esta guía se centra exclusivamente en los aspectos de ciberseguridad, y no en los requisitos de precisión o solidez, los cuales se tratan de manera específica en otras guías. A lo largo de esta guía, se recomienda que el lector (proveedor o, dependiendo de su alcance, el responsable del despliegue) aborde el apartado con el enfoque siguiente:
-
-
-
-
-

Identificar los activos y actores de su sistema de IA, en relación con el ciclo de vida.
Asociar activos y actores para poder establecer sus relaciones.
Identificar las vulnerabilidades a las que están expuestos los activos del sistema de
IA.
Definir y poner en marcha los controles de seguridad para proteger al sistema.
Revisar periódicamente la efectividad de esos controles.

En el apartado 3 se revisa el articulado relevante del Reglamento Europeo de IA, así como los requisitos que exige.
En el apartado 4 se discute cómo abordar los requisitos enumerados en el apartado 3. En el apartado 5 se establecen las bases de qué puede ser documentado en relación con la ciberseguridad, en línea con el proceso descrito para el apartado 4.

6

En el siguiente, apartado 6, se establecen una serie de cuestiones genéricas de autoevaluación para el cumplimiento de los requisitos exigidos por el Reglamento Europeo de IA.
En el apartado 7, se plantean las recomendaciones sobre formación y sobre políticas de acceso, que se mencionan a lo largo de las otras secciones de la guía. Además, este apartado incluye el subapartado 7.3 que es la relación de todos los términos y aspectos técnicos indicados a lo largo de la guía.
La guía se cierra con el apartado 8, donde se reúnen las fuentes consultadas para la elaboración de la guía, y otras referencias para profundizar en aquellos aspectos más específicos y propios del sistema de IA y su finalidad prevista. Específicamente en el apartado 8.1, se proporciona una relación de estándares, que pueden ayudar a la organización de un esquema de ciberseguridad más amplio, y que se encuentra fuera del alcance y objetivo de esta guía, centrada en la ciberseguridad para IA, en el marco del
Reglamento Europeo de IA.

1.3 ¿A quién está dirigido?
Es responsabilidad del proveedor del sistema de inteligencia artificial de alto riesgo tomar las medidas adecuadas (tanto organizativas como técnicas) para garantizar con el cumplimiento de los requerimientos de protección en el aspecto de ciberseguridad para la IA. Igualmente, dentro de su ámbito de aplicación, el responsable del despliegue del sistema también tiene responsabilidades que se materializarán en medidas concretas (de nuevo organizativas y técnicas).
Esta guía está dirigida a sistemas de IA de alto riesgo en fases avanzadas de desarrollo (a partir del nivel de madurez tecnológica TRL 6) y a sistemas que ya están en operación. Por tanto, aplica tanto a sistemas que están próximos a su puesta en servicio como a aquellos que requieren medidas de ajuste o refuerzo durante su funcionamiento.
A lo largo de la guía, a modo orientativo, se detallan los pasos y recomendaciones para implementar los requisitos de ciberseguridad específicos establecidos en el Reglamento, tanto por parte del proveedor como del responsable del despliegue del sistema de IA. Es importante señalar que esta guía no aborda todas las medidas generales de ciberseguridad, sino aquellas más destacadas o específicas para sistemas de IA de alto riesgo.
Para temas complementarios, como gestión de riesgos, transparencia, documentación técnica o gestión de calidad, se recomienda consultar las guías correspondientes.

1.4 Casos de uso utilizados en la guía
A lo largo de la guía se utilizarán dos casos de uso a modo de ejemplo de cómo elaborar la documentación técnica. Los ejemplos estarán centrados en el proveedor del sistema de
IA, quien es el responsable de generar y conservar la documentación. Sin embargo, es

7
