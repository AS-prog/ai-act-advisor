---
name: aesia-02-guia-practica-y-ejemplos-para-entender-el-reglamento-de-ia-01-texto-completo-parte-1
description: "AESIA: aesia 02 guia practica y ejemplos para entender el reglamento de ia, sección «Texto completo (parte 1)» (págs. 1-8). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-02-guia-practica-y-ejemplos-para-entender-el-reglamento-de-ia
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Texto completo (parte 1)"
  paginas: 1-8
  origen: 2026-07-17-aesia-02-guia-practica-y-ejemplos-para-entender-el-reglamento-de-ia.pdf
  oficial: false
---
# Texto completo (parte 1)

2

Empresas que empiezan a conocer el Reglamento

0

Esta guía ha sido desarrollada en el marco del desarrollo del piloto español de sandbox regulatorio de IA, en colaboración entre los participantes, asistencias técnicas, potenciales autoridades nacionales competentes y el grupo asesor de expertos del sandbox.
La guía tiene como objetivo servir de apoyo introductorio a la normativa europea de Inteligencia Artificial y sus obligaciones aplicables. Si bien no tiene carácter vinculante ni sustituye ni desarrolla la normativa aplicable, proporciona recomendaciones prácticas alineadas con los requisitos regulatorios a la espera de que se aprueben las normas armonizadas de aplicación para todos los estados miembros.
El presente documento está sujeto a un proceso permanente de evaluación y revisión, con actualizaciones periódicas conforme al desarrollo de los estándares y las distintas directrices publicadas desde la Comisión Europea. La guía ha sido actualizada conforme al Ómnibus digital que modifica el Reglamento de Inteligencia Artificial.
Guía 2. Guía práctica y ejemplos para entender el Reglamento de
Inteligencia Artificial © 2026 por el Ministerio para la Transformación
Digital y de la Función Pública está bajo una licencia
Creative Commons Atribución 4.0 Internacional.
NIPO:230260246

Fecha de versión: 17 de julio de 2026

1

-

Control de versiones del documento:

Versión

Fecha de versión

Cambios principales

1.0.

10/12/2025

2.0.

17/07/2026

Publicación de la primera versión
Adaptación de acuerdo con los cambios introducidos por el Ómnibus Digital y cambios menores de forma

2

Índice detallado
1. Preámbulo .............................................................................................................................. 5
1.1 Objetivo del documento ................................................................................................ 5
1.2 ¿Cómo leer esta guía? ................................................................................................... 5
1.3 ¿A quién está dirigido? .................................................................................................. 5
2. Ejemplos de Sistemas de IA ................................................................................................. 6
2.1 Sistema de IA de identificación biométrica en el trabajo .......................................... 6
2.2 Sistema de IA en la gestión de personal – Promoción............................................... 6
2.3 Sistema de IA para la predicción de riesgo de exclusión social y valoración de acceso a ayudas/subvenciones ............................................................................................... 7
2.4 Sistema de IA para la gestión de enfermedades crónicas - Bomba de insulina inteligente .................................................................................................................................. 8
2.5 Sistema de IA para la detección de denuncias falsas ................................................ 8
3. Definiciones con ejemplos ................................................................................................... 9
3.1 Sistema de inteligencia artificial (sistema de IA) ........................................................ 9
3.2 Introducción en el mercado ........................................................................................ 10
3.3 Comercialización .......................................................................................................... 10
3.4 Finalidad prevista ......................................................................................................... 10
3.5 Componente de seguridad ........................................................................................ 11
3.6 Modificación sustancial ............................................................................................... 11
3.7 Sistema de vigilancia poscomercialización ............................................................... 11
3.8 Especificación común .................................................................................................. 12
3.9 Datos de entrenamiento ............................................................................................. 13
3.10 Datos de validación ................................................................................................... 13
3.11 Datos de prueba ........................................................................................................ 13
3.12 Datos de entrada ....................................................................................................... 13
3.13 Identificación biométrica........................................................................................... 14
3.14 Verificación biométrica.............................................................................................. 14
3.15 Sistema de categorización biométrica .................................................................... 14
3.16 Sistema de identificación biométrica remota ......................................................... 15
3.17 Incidente grave........................................................................................................... 15
3.18. Infracción generalizada ............................................................................................ 15
3

3.19 Prueba en condiciones reales .................................................................................. 16
3.20 Plan de prueba en condiciones reales .................................................................... 16
3.21 Ultrafalsificación (Deep fake) .................................................................................... 16
3.22 Modelo de IA de uso general (GPAI) ....................................................................... 16
3.23 Riesgo sistémico de modelos de IA de uso general ............................................. 17
3.24 Ciclo de vida de un sistema IA ................................................................................. 17
4. Introducción a las Guías Técnicas ..................................................................................... 18
4.1 El piloto de Sandbox IA español ................................................................................ 18
4.2 Contexto de publicación de las guías técnicas ........................................................ 20

4

1. Preámbulo
1.1 Objetivo del documento
El objetivo de esta guía es facilitar la comprensión del Reglamento de IA desde un enfoque práctico. Con este objetivo, se proporciona un contexto de introducción de las guías técnicas, así como ejemplos hipotéticos de sistemas e IA de alto riesgo que se utilizan a lo largo de las guías con un objetivo didáctico que ayude a mejorar su comprensión.
La presente guía toma como referencia el Reglamento 2024/1689 del Parlamento Europeo y del Consejo, de 13 de junio de 2024 (Reglamento Europeo de Inteligencia Artificial).

1.2 ¿Cómo leer esta guía?
Esta guía debe leerse de manera complementaria a la Guía 1. Introducción al Reglamento
IA, de cara a introducir las guías técnicas y contribuir a aclarar algunas de las dudas más habituales que han surgido durante la participación en el piloto de Sandbox IA español.
El primer apartado que contiene el preámbulo, donde se presenta el propósito general de la guía.
El segundo apartado proporciona resúmenes de los ejemplos de los casos de uso que se utilizan a modo de ejemplo a lo largo de las guías técnicas para ilustrar su aplicación práctica.
El tercer apartado contiene un glosario de algunos de los términos y conceptos generales
(extraídos del Artículo 3 del RIA) más relevantes para facilitar la comprensión práctica del
Reglamento, acompañados de ejemplos vinculados a los casos de uso mencionados.
En el cuarto apartado proporciona un contexto sobre el desarrollo del piloto de Sandbox
IA español, en el que surgen las guías técnicas, así como una relación entre las guías y las obligaciones de los sistemas de alto riesgo, de cara a facilitar su consulta.

1.3 ¿A quién está dirigido?
A empresas y personas que deseen mejorar su comprensión del Reglamento de IA y prevean utilizar o consultar las guías técnicas.

5

2. Ejemplos de Sistemas de IA
En esta sección se presentan una serie de ejemplos de sistemas de IA, a modo de patrones, que han sido seleccionados por su representatividad. A lo largo de todas las guías y documentación proporcionada durante el sandbox, estos casos de uso serán utilizados como ejemplo transversal, para facilitar la explicación y compresión de los diferentes apartados. Todos los casos de uso presentados en esta sección son de alto riesgo.

2.1 Sistema de IA de identificación biométrica en el trabajo
Título

Asistencia al trabajo

Descripción

Sistema de Inteligencia Artificial de reconocimiento biométrico para registrar el tiempo y la asistencia al trabajo. Dispone de cámaras (o sensores biométricos) que registran la entrada, y cámaras (o sensores biométricos) que registran la salida, sin participación activa del empleado. El sistema asociado a cada cámara registra los tiempos de entrada/salida. El uso previsto es controlar el tiempo trabajado y no únicamente la identificación biométrica, por lo que, en este caso, la identificación no es la única finalidad del sistema
Cualquier empresa, para controlar y monitorizar la asistencia al trabajo de sus empleados.

Responsables del despliegue potenciales
RIA Anexo
Apartado
Subapartado

Anexo III
1 - Biometría.
a - Sistemas de identificación biométrica remota.

2.2 Sistema de IA en la gestión de personal – Promoción
Título

Gestión de personal - Promoción

Descripción

Este sistema de inteligencia artificial evalúa la posible promoción de los empleados. El sistema recoge una serie de parámetros para evaluar a los empleados de una organización y determinar si deben ser o no promocionados a un nuevo puesto. La propuesta de promoción que facilita el sistema de IA influye como uno de los factores determinantes, y no meramente accesorios, en el establecimiento de las retribuciones del nuevo puesto.

Responsables del Empresas para la gestión de promociones de sus empleados, si se despliegue subcontrata el servicio o la gestión de personal, puede tener potenciales responsables del despliegue anidados.
RIA Anexo

Anexo III

Apartado

4 - Empleo, gestión de los trabajadores y autoempleo.
6

Subapartado

b - Sistemas de IA destinados a ser utilizados para tomar decisiones que afecten a las condiciones de las relaciones de índole laboral o a la promoción o rescisión de relaciones contractuales de índole laboral, para la asignación de tareas a partir de comportamientos individuales o rasgos o características personales o para supervisar y evaluar el rendimiento y el comportamiento de las personas en el marco de dichas relaciones.

2.3 Sistema de IA para la predicción de riesgo de exclusión social y valoración de acceso a ayudas/subvenciones
Título

Predicción de riesgo de exclusión social y valoración de acceso a ayuda

Descripción

Este sistema de inteligencia artificial recogerá datos específicos de la unidad familiar, así como generales de la ayuda solicitada. El sistema de inteligencia artificial establece el acceso a la ayuda en función de los parámetros específicos de la misma, así como de aquellos generales que predicen el riesgo de exclusión social a corto plazo. Dentro de la ayuda además del acceso, el sistema establece una horquilla del importe asignado. El acceso a la ayuda viene determinado directamente por la indicación del sistema, el importe se asigna dentro de la horquilla que el sistema establece.

Responsables del Administraciones públicas para establecer el acceso y establecimiento despliegue de cuantía a ayudas.
potenciales
RIA Anexo

Anexo III

Apartado

5 - Acceso y disfrute de servicios públicos y privados esenciales y sus beneficios.

Subapartado

a - Sistemas de IA destinados a ser utilizados por las autoridades públicas o en su nombre para evaluar la admisibilidad de las personas físicas para beneficiarse de servicios y prestaciones esenciales de asistencia pública, incluidos los servicios de asistencia sanitaria, así como para conceder, reducir o retirar dichos servicios y prestaciones o reclamar su devolución.

7
