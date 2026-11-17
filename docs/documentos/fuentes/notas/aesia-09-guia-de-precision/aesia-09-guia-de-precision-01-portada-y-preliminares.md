---
name: aesia-09-guia-de-precision-01-portada-y-preliminares
description: "AESIA: aesia 09 guia de precision, sección «Portada y preliminares» (págs. 1-6). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-09-guia-de-precision
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Portada y preliminares"
  paginas: 1-6
  origen: 2026-07-17-aesia-09-guia-de-precision.pdf
  oficial: false
---
# Portada y preliminares

9

Empresas desarrollando

0

Esta guía ha sido desarrollada en el marco del desarrollo del piloto español de sandbox regulatorio de IA, en colaboración entre los participantes, asistencias técnicas, potenciales autoridades nacionales competentes y el grupo asesor de expertos del sandbox.
La guía tiene como objetivo servir de apoyo introductorio a la normativa europea de Inteligencia Artificial y sus obligaciones aplicables. Si bien no tiene carácter vinculante ni sustituye ni desarrolla la normativa aplicable, proporciona recomendaciones prácticas alineadas con los requisitos regulatorios, a la espera de que se aprueben las normas armonizadas de aplicación para todos los Estados miembros.
El presente documento está sujeto a un proceso permanente de evaluación y revisión, con actualizaciones periódicas conforme al desarrollo de los estándares y las distintas directrices publicadas desde la
Comisión Europea. La guía ha sido actualizada conforme al Ómnibus digital que modifica el Reglamento de Inteligencia Artificial.
Entre las referencias técnicas relevantes actualmente en desarrollo, destaca el prEN 18229-2 “AI Trustworthiness Framework — Part 2:
Accuracy and Robustness”, que servirá de base para la evaluación de la precisión y la solidez de los sistemas de IA una vez sea adoptado como norma armonizada en el contexto del cumplimiento del Reglamento
Europeo de Inteligencia Artificial.

Guía 9. Precisión © 2026 por el Ministerio para la Transformación Digital y de la
Función
Pública está bajo una licencia
Creative Commons Atribución 4.0 Internacional.
NIPO: 230260170

Fecha de versión: 17 de julio de 2026

1

-

Control de versiones del documento:

Versión

Fecha de versión

Cambios principales

1.0.

10/12/2025

Publicación de la primera versión

2.0

17/07/2026

Adaptación de acuerdo con los cambios introducidos por el Ómnibus Digital y cambios menores de forma

2

Contenido general
1.

Preámbulo ................................................................................................................................................... 6

2.

Introducción ................................................................................................................................................ 8

3.

Reglamento de Inteligencia Artificial ...................................................................................................... 11

4.

¿Cómo puedo abordar los requisitos? ................................................................................................... 15

5.

Documentación técnica ........................................................................................................................... 32

6.

Cuestionario de autoevaluación ............................................................................................................. 37

7.

Anexos ....................................................................................................................................................... 38

8.

Referencias, estándares y normas ........................................................................................................... 57

3

Índice detallado
1.

Preámbulo ................................................................................................................................................... 6
1.1 Objetivo del documento ........................................................................................................................ 6
1.2 ¿Cómo leer esta guía? ............................................................................................................................ 6
1.3 ¿A quién está dirigido? .......................................................................................................................... 6
1.4 Casos de uso utilizados en la guía ........................................................................................................ 7

2.

Introducción ................................................................................................................................................ 8
2.1 ¿Qué es la precisión para IA? ................................................................................................................ 8

3.

Reglamento de Inteligencia Artificial ...................................................................................................... 11
3.1 Análisis previo y relación de los artículos ........................................................................................... 11
3.2 Contenido de los artículos en el Reglamento de IA ......................................................................... 12
3.3 Correspondencia del articulado con los apartados de la guía ........................................................ 13

4.

¿Cómo puedo abordar los requisitos? ................................................................................................... 15
4.1 Precisión y ciclo de vida ....................................................................................................................... 15
4.1.1 Preprocesamiento de los datos .................................................................................................... 15
4.1.2 Sobreaprendizaje (Overfitting) ..................................................................................................... 16
4.1.3 Uso de modelos apropiados ......................................................................................................... 19
4.1.4 Incertidumbre y precisión ............................................................................................................. 21
4.2 Evaluando la precisión ......................................................................................................................... 21
4.2.1 Selección de métricas de precisión .............................................................................................. 23
4.2.2 Selección de la función objetivo ................................................................................................... 24
4.2.3 Dimensiones complementarias a la precisión............................................................................. 24
4.3 Garantizando la precisión .................................................................................................................... 27
4.3.1 Medidas técnicas ............................................................................................................................ 28
4.3.2 Evaluaciones de significancia estadística .................................................................................... 29
4.3.3 Benchmarks de bases de datos y modelos ................................................................................. 30

5.

Documentación técnica ........................................................................................................................... 32
5.1 Tarjeta del Modelo ............................................................................................................................ 33
5.2 Tarjeta de base de datos .................................................................................................................. 35

6.

Cuestionario de autoevaluación ............................................................................................................. 37

7.

Anexos ....................................................................................................................................................... 38
7.1 Métricas de precisión ........................................................................................................................... 38
7.2 Funciones Objetivo............................................................................................................................... 39
7.2.1 Funciones objetivo regresión, clasificación o ranking ............................................................... 39
7.2.2 Funciones objetivo en otros tipos de modelo ............................................................................ 40
7.3 Precisión, sesgos e imparcialidad ....................................................................................................... 40

4

7.3.1 Sesgos y precisión .......................................................................................................................... 41
7.3.2 La imparcialidad para mitigar sesgos .......................................................................................... 42
7.4 Glosario .................................................................................................................................................. 43
8.

Referencias, estándares y normas ........................................................................................................... 57
8.1 Referencias ............................................................................................................................................ 57
8.1.1 Referencias generales .................................................................................................................... 57
8.1.2 Referencias del Glosario ................................................................................................................ 63
8.2 Estándares ............................................................................................................................................. 66

5
