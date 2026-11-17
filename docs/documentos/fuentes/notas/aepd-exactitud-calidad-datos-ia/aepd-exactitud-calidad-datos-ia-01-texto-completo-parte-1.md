---
name: aepd-exactitud-calidad-datos-ia-01-texto-completo-parte-1
description: "AEPD: aepd exactitud calidad datos ia, sección «Texto completo (parte 1)» (págs. 1-8). Documento de 2026-07-21, idioma es."
metadata:
  type: reference
  documento: aepd-exactitud-calidad-datos-ia
  emisor: AEPD
  fecha: 2026-07-21
  idioma: es
  seccion: "Texto completo (parte 1)"
  paginas: 1-8
  origen: 2026-07-21-aepd-exactitud-calidad-datos-ia.pdf
  oficial: false
---
# Texto completo (parte 1)

Exactitud, idoneidad y calidad de los datos en tratamientos de datos personales con
Inteligencia Artificial

Página: 1 de 23

RESUMEN EJECUTIVO
Este documento formula una serie de reflexiones acerca de la relación entre la calidad de los datos y el principio de exactitud previsto en el Reglamento General de Protección de Datos (RGPD)
en el marco de los tratamientos de datos personales, poniendo de manifiesto que ambos conceptos deben interpretarse en función de la finalidad perseguida y de la idoneidad del tratamiento. Aunque estrechamente relacionados, los requisitos de calidad de los datos y el principio de exactitud del RGPD no son conceptos equivalentes. La calidad de los datos constituye un concepto más amplio, aplicable tanto a datos personales como no personales y debe dar respuesta a requisitos más allá del RGPD.
La interpretación del principio de exactitud del RGPD no debería limitarse exclusivamente a la veracidad o a la actualización de los datos. Dependiendo de la finalidad del tratamiento, la adecuación de los datos puede requerir también otras propiedades, tales como la precisión, el nivel de granularidad, la frecuencia de actualización o cualquier otra característica cuya ausencia pueda comprometer el cumplimiento de la finalidad perseguida. La veracidad y la actualidad de los datos deben exigirse cuando resulten necesarias para dicha finalidad, especialmente cuando su falta pueda incidir en los derechos y libertades de las personas físicas, sin que ello implique que constituyan requisitos exigibles para todo tratamiento.
Asimismo, cuando un tratamiento de datos personales incorpore datos no personales, estos también deberán satisfacer los requisitos de calidad que resulten adecuados para la finalidad perseguida, en la medida en que puedan influir en la idoneidad del tratamiento o en aquellos resultados susceptibles de producir efectos sobre los derechos y libertades de las personas físicas.
La evaluación de la calidad no puede limitarse a los datos de entrada. Resulta igualmente necesario establecer métricas objetivas sobre la calidad de los resultados generados por el tratamiento, ya que, sin ellas, no es posible verificar ni demostrar que la finalidad perseguida se alcanza de forma eficaz y que el tratamiento mantiene las condiciones de idoneidad exigibles.
Esta relación entre calidad e idoneidad adquiere una relevancia especial en los tratamientos destinados al desarrollo o evolución de sistemas y modelos de inteligencia artificial. Los conjuntos de datos que no reúnen los requisitos de calidad para dicho desarrollo no pueden considerarse necesarios para el tratamiento. En consecuencia, el acceso a tales conjuntos de datos únicamente podría justificarse en la medida estrictamente necesaria para evaluar objetivamente su calidad y determinar su eventual aptitud para la finalidad prevista.
Los mecanismos de gobierno y los procesos de gestión de datos han de coordinar tanto las obligaciones derivadas de los tratamientos de datos personales como las exigencias propias del desarrollo, adquisición, despliegue y evolución de sistemas de inteligencia artificial, garantizando la coherencia de los criterios de calidad y de cumplimiento normativo a lo largo de todo el ciclo de vida.
Finalmente, la definición, evaluación y revisión de los requisitos de calidad de los datos exige un enfoque multidisciplinar. Para ello resulta esencial contar, al menos, con la participación conjunta de especialistas en ciencia de datos y en protección de datos, que se guíen por criterios objetivos y evidencia verificable durante todo el ciclo de vida de los tratamientos.
Palabras clave: inteligencia artificial, exactitud, minimización, finalidad, idoneidad, calidad de datos, conjuntos de datos, gobernanza.

Página: 2 de 23

CONTENIDO
I.

INTRODUCCIÓN

4

II.

CALIDAD DE LOS DATOS Y EXACTITUD-RGPD

4

A.
B.
C.
D.
E.
F.
G.

Calidad de los datos
Exactitud y minimización en el RGPD
Características de calidad de los datos en los estándares
Características de calidad de los datos más allá del estándar
Calidad del dato individual vs calidad del conjunto de datos
Calidad de los datos vs veracidad y actualidad
Alineación de exactitud-RGPD con calidad de los datos

4
5
6
7
8
9
10

III. TRATAMIENTOS DE DATOS PERSONALES E IA

11

A.
B.
C.
D.
E.
F.
G.

12
13
15
15
16
17
18

Tipos de tratamientos de datos personales
Calidad de los datos en tratamientos de datos personales que incluyen sistemas de IA
Exigibilidad de calidad en los datos no personales dentro de tratamientos de datos personales
Desarrollo de IA como tratamiento
Determinación de los requisitos de calidad de los datos en el desarrollo de sistemas de IA
Análisis de calidad de las fuentes de datos para IA
Requisitos de calidad inadecuados

IV. REFLEXIONES FINALES
V.

18

ANEXO: EVOLUCIÓN DEL CONCEPTO DE EXACTITUD EN LA NORMATIVA ESPAÑOLA 21

Página: 3 de 23

I.

INTRODUCCIÓN

El concepto de calidad de los datos es esencial para la economía del dato cuando productos o servicios dependen, para su desarrollo, del acceso a conjuntos de datos. Además, tales conjuntos de datos precisan tener la calidad adecuada para alcanzar la finalidad prevista, y cumplir con distintos requisitos, en un contexto específico1. Estos conjuntos deben contener datos representativos que ofrezcan la cantidad de información necesaria para garantizar el éxito de los procesos basados en datos, ya sean datos personales o no. Un caso particular sería el desarrollo de modelos y sistemas de IA2 basados en técnicas de aprendizaje automático y/o que precisen conjuntos de datos para verificación, validación y prueba.
Por otro lado, los tratamientos de datos personales, que pueden incluir en sus operaciones uno o más sistemas de inteligencia artificial, deben ser conformes al RGPD3 4, en particular con relación a los principios de exactitud y de minimización con relación a los datos personales. Asimismo, el resultado de un tratamiento de datos personales ha de cumplir la condición de idoneidad para cumplir su finalidad, y en cuanto el resultado sea relativo a personas identificadas o identificables, se ha de garantizar que se protegen sus derechos y libertades, en particular en el respeto de ambos principios. Un caso específico de tratamiento de datos personales es aquel en el que conjuntos de datos personales (y no personales) son necesarios para el desarrollo de modelos y sistemas de IA.
La presente nota técnica trata sobre la aplicación de dichos conceptos (exactitud, minimización, idoneidad y calidad de datos) en el marco de tratamientos a los que aplica el RGPD.
Está orientada a responsables, encargados y DPD’s, así como para aquellos implicados en el desarrollo, prueba y mantenimiento de productos o servicios que precisen de acceso a conjuntos de datos personales, como pueden ser muchos tipos de modelos y sistemas de IA.

II.

CALIDAD DE LOS DATOS Y EXACTITUD-RGPD

A. CALIDAD DE LOS DATOS
La calidad de los datos se define en distintos estándares (por ejemplo, UNE 0079, ISO 25012, ISO
5259, ISO 8000) con relación a cualquier tipo de datos, ya sean datos personales o no, como el grado en que las características de los datos deben satisfacer necesidades declaradas e implícitas cuando se utilizan en condiciones específicas. La norma ISO 229895, con relación a sistemas de IA, define el proceso de comprobación de la calidad del dato como aquel "en el que los datos son examinados para determinar su completitud, sesgo y otros factores que afecten a su utilidad para un sistema de IA". Estas definiciones sirven de orientación técnica, y no sustituyen ni modifican las exigencias jurídicas derivadas del RGPD.
Tales definiciones vinculan el concepto de calidad de los datos a la adecuación de estos para cumplir una finalidad ("satisfacen necesidades declaradas e implícitas" o "utilidad para un sistema
IA") en un contexto6 determinado. Las "necesidades declaradas e implícitas" también podrían incluir el cumplimiento de obligaciones de distintas normativas, cumplimiento de estándares, compromisos contractuales y políticas internas de una entidad.

1 Así es como se expresa en el RIA para los modelos y sistemas de su competencia en el considerando 12
2 El término sistema o modelo de IA se utiliza en este texto con un significado más amplio que el utilizado en el RIA y en las guías de la

Comisión Europea sobre la definición de sistema de IA, pudiendo incluir otras técnicas basadas en ciencia de datos, como las regresiones logísticas, optimizaciones matemáticas, métodos estadísticos, etc.
3 Deben garantizar y poder demostrar que son conformes, según el art.24 del RGPD
4 Aunque se utilice únicamente el término RGPD, se extiende a la competencia establecida en la Ley Orgánica 7/2021, de 26 de mayo, de protección de datos personales tratados para fines de prevención, detección, investigación y enjuiciamiento de infracciones penales y de ejecución de sanciones penales.
5 ISO 22989 Artificial intelligence concepts and terminology
6 En el RIA, se define en el considerando 12 el contexto en el que funciona el sistema IA
Página: 4 de 23

Estas necesidades específicas se representan a través de los llamados requisitos de calidad de los datos.

B. EXACTITUD Y MINIMIZACIÓN EN EL RGPD
Pese a que la calidad de los datos puede considerarse un principio clásico en el ámbito de la privacidad, lo cierto es que el RGPD no hace referencia al término “calidad de los datos”7, aunque sí establece dos principios especialmente relacionados con él, como son el de minimización y el de exactitud en el artículo 5 apartado 1, letras c) y d):
“1. Los datos personales serán:
c) adecuados, pertinentes y limitados a lo necesario en relación con los fines para los que son tratados («minimización de datos»);
d) exactos y, si fuera necesario, actualizados; se adoptarán todas las medidas razonables para que se supriman o rectifiquen sin dilación los datos personales que sean inexactos con respecto a los fines para los que se tratan («exactitud»);”.
Si bien los requisitos de calidad de los datos no constituyen un principio del RGPD, su función sí es instrumental para facilitar la aplicación práctica de dichos principios. Ambos actúan de forma complementaria, coherente y autónoma para establecer la banda de calidad que han de tener los datos, exigiendo que sean correctos con relación a la finalidad y limitando el conjunto de datos a los necesarios. Tanto para los datos de entrada al tratamiento, como con relación a los resultados de salida del tratamiento.

Figura 1 Hay que encontrar el necesario balance entre exactitud y minimización para cumplir los fines del tratamiento

El cumplimiento de los principios de minimización de datos y de exactitud está vinculado al de finalidad del tratamiento8. En cuanto vinculado al cumplimiento de la finalidad, el significado del principio de exactitud de los datos en el RGPD (en adelante "exactitud-RGPD”9) tiene una extensión distinta, y no estrictamente vinculada a, por ejemplo, la veracidad y actualidad de cada uno de los datos. El término “exactitud-RGPD” está vinculado a que los datos sean adecuados para alcanzar la finalidad del tratamiento, es decir, conseguir que el tratamiento sea idóneo. Esto implica que los datos de entrada han de ser lo suficientemente exactos-RGPD para que el tratamiento consiga su finalidad y, si el resultado del tratamiento son datos personales, incluidas decisiones y

7 Excepto en el art.47 “Normas corporativas vinculantes” en el apartado 2 letra d) “Las normas corporativas vinculantes mencionadas en

el apartado 1 especificarán, como mínimo, los siguientes elementos:…d) la aplicación de los principios generales en materia de protección de datos, en particular la limitación de la finalidad, la minimización de los datos, los periodos de conservación limitados, la calidad de los datos, la protección de los datos desde el diseño y por defecto, …”.
8 En este caso, habría que considerar también el cumplimiento de principios como el de lealtad, sobre el que se podría fundamentar el tratamiento de datos para evitar, por ejemplo, sesgos, sin perjuicio de los establecido en el artículo 9 del RGPD y el RIA.
9 El término exactitud con relación a los datos tiene un ámbito semántico distinto al del utilizado en los estándares antes mostrados y en otras normativas. No es el único caso. Términos que aparecen en el RGPD, como transparencia, interesado, tratamiento, consentimiento, responsable o riesgo entre otros, son empleados en otros contextos normativos con un significado muy distinto. Cuando se emplean en contextos en los que aplican distintos marcos regulatorios es importante añadir a los términos un "apellido" para determinar con precisión su significado.
Página: 5 de 23

perfilados, estos resultados han de respetar los derechos y libertades de las personas físicas, en particular, con relación a la exigencia de que los datos sean veraces.
El cumplimiento del principio de exactitud-RGPD puede implicar el satisfacer distintos requisitos “técnicos”, tales como una adecuada precisión, suficiente granularidad, una frecuencia de recogida adecuada, ausencia de sesgos, completitud de atributos, etc. Una interpretación extensiva del principio de exactitud-RGPD que fuera más allá del cumplimiento de la finalidad podría afectar a los derechos de los interesados, en la medida que habilitaría un tratamiento de datos que podrían ir más allá de las necesidades estrictas, contradiciendo el principio de minimización-RGPD.
Asimismo, dicha interpretación extensiva podría generar cargas desproporcionadas para los responsables y encargados y, en particular, para los desarrolladores/evolucionadores de sistemas de IA, al exigirles acceder y gestionar conjuntos de datos con unos niveles de, por ejemplo, veracidad, actualidad, precisión, etc., que podrían no ser necesarios. Incluso, esto podría ir en contra de la posibilidad de conseguir conjuntos de datos de calidad suficiente para desarrollar sistemas adecuados y, además, exigir a los responsables la atención de unos derechos más allá de lo establecido en el RGPD10. En todo caso, quedará a salvo la posibilidad de corrección de datos personales que sean inexactos en relación con la persona afectada en coherencia con el derecho de rectificación (artículo 16 RGPD).

C. CARACTERÍSTICAS DE CALIDAD DE LOS DATOS EN LOS ESTÁNDARES
Existen criterios para evaluar la calidad de los datos. Por ejemplo, en el estándar ISO 25012 se enumeran una serie de características para tener en cuenta: exactitud, completitud, consistencia, credibilidad, actualidad, accesibilidad, conformidad, confidencialidad, eficiencia, precisión, trazabilidad, comprensibilidad, disponibilidad, portabilidad y recuperabilidad. El estándar establece que su evaluación ha de realizarse en función del contexto de uso específico, por lo que no se trata de características absolutas sino relativas a dicho contexto.
Aunque en el listado de características del estándar se puede leer el término "exactitud", sería un error emparejar este término con el término exactitud-RGPD. Exactitud-ISO es el grado en el que los datos representan correctamente el verdadero valor de un atributo, de un concepto o de un evento en un contexto de uso específico. La exactitud-ISO podría ser una de las condiciones necesarias para alcanzar la exactitud-RGPD, es decir, para cumplir con la finalidad del tratamiento, pero no necesariamente. Además, para alcanzar la exactitud-RGPD podrían ser necesarias otras características del estándar, como la precisión, así como características que no se encuentran enumeradas en el estándar, como la ausencia de un sesgo.
Como todo estándar, el conjunto de características de calidad de los datos recoge la experiencia pasada y permite establecer un marco de referencia común que facilite la comparación de las evaluaciones obtenidas por distintos actores. Sin embargo, no resulta exigible el cumplimiento de todas las características, ni estas agotan los requisitos necesarios para garantizar la idoneidad respecto de cualquier finalidad. Por ello, no hay que cometer los siguientes errores al utilizar estos estándares:
- Aplicar “calidad de checkbox”, entendida como un repaso en abstracto del conjunto de
datos sin tener en cuenta el contexto y la finalidad específicos, ni realizar un análisis basado en evidencias.
- Establecer que todas las características son igual de relevantes. Para un contexto y finalidad
determinados, algunas de ellas podrían ser irrelevantes y, por tanto, no exigibles.

10 El art.16 del RGPD también vincula la rectificación a la finalidad del tratamiento.

Página: 6 de 23

-

Suponer que las características a evaluar se agotan en la lista del estándar. El estándar no es exhaustivo, sino un valioso punto de partida que hay que adaptar a las circunstancias concretas de cada tratamiento.

Para no caer en estos errores, es necesario extraer la lista de características y sus requisitos para en función de los contextos y finalidades previstos del tratamiento.

D. CARACTERÍSTICAS DE CALIDAD DE LOS DATOS MÁS ALLÁ DEL ESTÁNDAR
Con relación al apartado anterior, y para el caso de desarrollo de modelos y sistemas de IA, puede ser necesario considerar más características con relación a la calidad de los datos, como por ejemplo11:
- La eliminación de sesgos que comprometan la finalidad del tratamiento12.
- Las propiedades estadísticas adecuadas para determinadas finalidades previstas.
- La representatividad del contexto con relación a las finalidades previstas.
- Que se reflejen los rasgos, características o elementos particulares del entorno geográfico,
contextual, conductual o funcional específico en el que esté previsto que se utilice el sistema de IA.
- La frecuencia de recogida de datos, que puede ser relevante cuando se están realizando
tratamientos basados en la geolocalización, en el consumo de energía, en la actividad en
Internet, etc.
- El poder predictivo de las variables seleccionadas. Estas son aquellas con la capacidad de
anticipar con precisión el valor de las variables resultado, al estar fuertemente relacionadas con ellas, permiten separar claramente entre clases y reducen la incertidumbre del resultado.
- La relevancia de muestras para el proceso de aprendizaje. Las muestras relevantes son
aquellas que aportan información significativa y útil para adaptar el modelo en cada iteración de entrenamiento. Las técnicas de “active-learning” en aprendizaje automático están orientadas a seleccionar muestras relevantes, que dependerán del diseño del modelo, así como del grado de preentrenamiento que ya posee.

Figura 2 En un ejemplo, sencillo y evidente, de clasificación con machine learning en el que dos clases se han de dividir de forma lineal. El gráfico de la izquierda utiliza un conjunto de datos en el que la mayoría de las muestras no son relevantes para realizar una clasificación adecuada, mientras que el de la derecha es un conjunto de datos muy relevantes para obtener dicha clasificación lineal.

11 Están enumeradas en el considerando 67 y artículo 10 del RIA en los apartados del 1 al 4.
12 Los sesgos no son en todos los casos negativos, sino que, en algunos de ellos, tanto los sesgos en los conjuntos de datos utilizados

en aprendizaje automático pueden ser necesarios en casos como el desarrollo de sistemas de detección del fraude, como los sesgos en el resultado de salida de un tratamiento pueden ser necesarios para la medicina de precisión.
Página: 7 de 23

Las técnicas de “active-learning”, la representatividad, la relevancia y el poder predictivo no solo tienen ventajas para el desarrollo y el rendimiento de un modelo o sistema de IA, sino que también pueden ser una herramienta muy útil para aplicar el principio de minimización de datos.

E. CALIDAD DEL DATO INDIVIDUAL VS CALIDAD DEL CONJUNTO DE DATOS
Aunque se ha abordado de forma indirecta, conviene hacer explícita la distinción entre la calidad del dato, considerado individualmente, y la calidad del conjunto de datos13. Este último concepto adquiere especial relevancia en el caso del desarrollo de sistemas de IA basados en aprendizaje automático.
Por ejemplo, sea el caso de la siguiente tabla:
CONJUNTO DE DATOS
ID
ID1
ID2
ID3
ID4
ID5
ID6
ID7
ID8

GENERO PROVINCIA
H
MAD
H
MAD
H
MAD
H
VAL
H
MAD
H
MAD
H
MAD
M
MAD

SUELDO
57400
67000
90000
36900
55000
76000
30000
45000

EXP.
Medio
Bajo
Alto
Bajo
Medio
Alto
Bajo
Bajo

Figura 3 Conjunto de datos con posible cumplimiento el estándar ISO, interpretado a nivel de registro, pero claramente sesgado con relación al género.

La tabla anterior podría obtener un alto grado de calidad según el estándar ISO, interpretado a nivel de registro, pero el conjunto de datos está claramente sesgado con relación al género. Si la finalidad del tratamiento es tener estimaciones o tomar decisiones que afecten a todos los géneros, el conjunto de datos mostrado no sería adecuado para cumplir con la finalidad de forma idónea.
El tratamiento de datos personales que tiene como objetivo el desarrollo de sistemas de IA mediante aprendizaje automático es uno de entre muchos tratamientos en los que la consecución de la finalidad no depende tanto de la calidad del dato tomado individualmente, o del registro específico de un usuario, sino de la calidad del conjunto de datos.
IS O

O tras caracterísitcas

Dato o reg istro
Conjunto de datos
Dato o reg istro
Conjunto de datos
E xactitud
Consistencia
R elevancia
S esgo
Completitud
A ccesibilidad
P ropiedades estadísticas
Credibilidad
Disponibilidad
F recuencia
A ctualidad
P ortabilidad
R epresentatividad
Cumplimiento
R ecuperabilidad
E ntorno geográfico
Confidencialidad
E ntorno contextual
E ficiencia
E ntorno funcional
P recisión
E ntorno conductual
T razabilidad
P oder predictivo
Comprensibilidad
Figura 4 Características específicas del dato o registro, y aquellas que dependen del conjunto de datos, y no las muestras evaluadas individualmente.

13 El empleo del término inglés "data quality", puede ser interpretado tanto en singular como en plural, y puede llevar a equívocos.

Página: 8 de 23
