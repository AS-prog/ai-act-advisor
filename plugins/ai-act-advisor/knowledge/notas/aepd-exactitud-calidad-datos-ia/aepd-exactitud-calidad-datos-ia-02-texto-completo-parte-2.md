---
name: aepd-exactitud-calidad-datos-ia-02-texto-completo-parte-2
description: "AEPD: aepd exactitud calidad datos ia, sección «Texto completo (parte 2)» (págs. 9-16). Documento de 2026-07-21, idioma es."
metadata:
  type: reference
  documento: aepd-exactitud-calidad-datos-ia
  emisor: AEPD
  fecha: 2026-07-21
  idioma: es
  seccion: "Texto completo (parte 2)"
  paginas: 9-16
  origen: 2026-07-21-aepd-exactitud-calidad-datos-ia.pdf
  oficial: false
---
# Texto completo (parte 2)

Otros casos podrían ser tratamientos de análisis de tendencias, de correlaciones, optimizaciones, asignación de recursos, desarrollo de modelos, toma de decisiones en políticas públicas o análisis de riesgos en ámbitos como la logística, la educación, las finanzas, la energía, la movilidad, la sanidad, la ciencia, etc.
En estos casos, en la medida que el conjunto de datos contenga datos personales, el principio de exactitud-RGPD debe tener en cuenta características tan importantes como que los datos, tomados en su conjunto, no contengan sesgos que comprometan la finalidad del tratamiento.
Así pues, en sistemas de inteligencia artificial, la calidad del dato debe evaluarse también al nivel del conjunto de datos (“dataset”), pues resulta esencial para garantizar el correcto funcionamiento del sistema y, por lo tanto, cumplir con la finalidad del tratamiento que supone su desarrollo. Ello sin perjuicio de la calidad del dato individual, por cuanto produzca efectos sobre las personas.
El responsable del tratamiento, bajo el principio de exactitud y de responsabilidad proactiva, deberá garantizar y documentar la trazabilidad del conjunto de datos utilizado, incluyendo el origen de los datos, las transformaciones aplicadas y los criterios de selección y exclusión.

F. CALIDAD DE LOS DATOS VS VERACIDAD Y ACTUALIDAD
La calidad del conjunto de datos para una finalidad específica, en cuanto a datos personales, puede estar relacionada con la veracidad y actualidad de estos. No obstante, el RGPD es incluso explícito en que la actualidad del dato personal es un requisito de exactitud-RGPD sólo cuando sea necesario para cumplir con la finalidad del tratamiento.
La aplicación sobre un conjunto de datos personales de técnicas para la eliminación de sesgos, de técnicas de anonimización (no solo para anonimizar, sino para minimizar datos), de técnicas de privacidad diferencial o la generación de datos sintéticos puede implicar que algunos valores no reflejen directamente la realidad de un individuo o no cumplan determinados criterios técnicos de exactitud-ISO. Sin embargo, el conjunto de datos resultante puede tener la calidad suficiente como para ser utilizada como entrada en todas o algunas de las fases de desarrollo de un sistema de IA basado en ML. Es decir, el conjunto de datos puede considerarse que cumple con el principio de exactitud-RGPD en la medida en que resulte adecuado para la finalidad del tratamiento, sin que ello suponga prescindir de las exigencias de veracidad cuando estas sean relevantes.
Es más, existen técnicas para incrementar la calidad del conjunto de datos que pueden implicar la utilización de valores que no reflejen directamente la realidad individual. Así, por ejemplo, puede considerarse un conjunto de datos formado por registros con múltiples campos en el que algunos de ellos están vacíos o incompletos (problemas de completitud). Una técnica para aumentar la calidad del conjunto de datos es estimar el posible valor de los campos vacíos extrapolándolo de medidas estadísticas obtenidas del resto de registros. Esta es una técnica adecuada, pero introduce valores formalmente falsos e inexactos, sacrificando la exactitud-ISO por la completitud-ISO.
CO NJ U NT O DE DAT O S O R IG INAL
ID
ID 1
ID 2
ID 3
ID 4
ID 5
ID 6
ID 7
ID 8

P R O VINCIA
MAD
VAL
GR
VAL
B CN
VAL
VAL
B CN

S U E L DO
57400
90000
36900
7600
45000

EXP.
Medio
B ajo
Alto
B ajo
Medio
Alto
B ajo
B ajo

CO M P L E T ADO CO N L A M E DIA
P R O VINCIA S U E L DO
MAD
57400
VAL
65150
GR
90000
VAL
36900
B CN
65150
VAL
7600
VAL
65150
B CN
45000

EXP.
Medio
B ajo
Alto
B ajo
Medio
Alto
B ajo
B ajo

CO M P L E T ADO CO N M E DIA P O R P R O VINCIA
P R O VINCIA S U E L DO
MAD
57400
VAL
22250
GR
90000
VAL
36900
B CN
45000
VAL
7600
VAL
22250
B CN
45000

EXP.
Medio
B ajo
Alto
B ajo
Medio
Alto
B ajo
B ajo

Figura 5 En la tabla de la izquierda existen campos que no estaban completados en origen. Se puede completar la tabla de datos con distintas estrategias. En la tabla del centro se ha elegido introducir la media de los sueldos de toda la tabla. En la derecha se han utilizado las medias de los sueldos de la misma provincia.
Página: 9 de 23

Los conjuntos de datos personales que tienen campos “inventados” pueden mantener un nivel adecuado de calidad desde una perspectiva técnica. La característica de exactitud-ISO no se estaría cumpliendo para determinados registros individuales, pero eso no sería relevante para un tratamiento específico. Además, no se faltaría al principio de exactitud-RGPD si el conjunto de datos es adecuado para conseguir la finalidad del tratamiento.
De igual forma, una técnica de corrección de sesgos consiste en aplicar correcciones para normalizar por grupo, calculando el sesgo grupal y eliminando la diferencia sistemática:
TABLA ORIGINAL

TABLA CON SESGO ELIMINADO
Historial
Código
Historial
ID
Edad Ingresos (€) Código Postal
Edad Ingresos (€)
Crédito
Postal
Crédito
1
45
60000
28001
0,80
45
60000
28001
0,80
2
25
28000
28003
0,70
25
28000
28003
0,90
3
50
72000
28002
0,85
50
72000
28002
0,85
4
38
58000
28001
0,90
38
58000
28001
0,90
5
29
30000
28003
0,60
29
30000
28003
0,80
6
41
65000
28002
0,85
41
65000
28002
0,85
7
33
32000
28003
0,65
33
32000
28003
0,85
8
41
65000
28002
0,95
41
65000
28002
0,95
9
36
70000
28001
0,75
36
70000
28001
0,75
Figura 6 En la tabla original hay un sesgo en la evaluación del historial de crédito con relación a las personas que viven en el código postal 28003. La media de los otros códigos postales es de 0,85, mientras que la media en las personas con código 28003 es de 0,65. El sesgo toma un valor de 0,2, que se puede corregir normalizando los valores.

Así pues, la calidad entendida como idoneidad para una finalidad, no se identifica automáticamente con la veracidad en sentido absoluto. La relevancia de la veracidad del dato varía en función del tipo de tratamiento. Así, en tratamientos agregados o estadísticos, pueden admitirse mayores niveles de abstracción o transformación del dato, mientras que en tratamientos que produzcan efectos sobre personas concretas, la exigencia de veracidad y actualidad, al menos en el resultado del mismo, debe ser más estricta. Ello sin perjuicio de que se debe garantizar que no se genere una representación incorrecta o distorsionada de la persona interesada, o que se generen efectos adversos sobre sus derechos e intereses. En definitiva, el uso de datos que no reflejen la realidad debe analizarse en función de su impacto en la toma de decisiones, la generación de perfiles, o cualquier otro efecto significativo sobre la persona física, y ha de estar justificado y documentado.

G. ALINEACIÓN DE EXACTITUD-RGPD CON CALIDAD DE LOS DATOS
El concepto de exactitud-RGPD se alinea con las definiciones de calidad de los datos de los estándares de la economía del dato en la medida en que ambos están vinculados con el principio de finalidad. Sin embargo, ambos términos no son intercambiables. Calidad de los datos se aplica tanto a datos personales como no personales en el marco de la industria, mientras que exactitudRGPD se aplica a datos personales en el ámbito de competencia del RGPD14.
Por otro lado, el nivel de calidad de los datos puede venir determinado por requisitos técnicos o funcionales que no se derivan de la normativa de protección de datos, por ejemplo, el cumplimiento de obligaciones de otras normativas, cumplimiento de estándares, compromisos contractuales y políticas internas de una entidad. En consecuencia, dichos requisitos no tienen por qué coincidir con las exigencias del principio exactitud-RGPD, que deben valorarse en función de la finalidad del tratamiento y de sus efectos sobre las personas.

14 Como se ha señalado anteriormente, la referencia al RGPD empleada en el texto incluye a la L.O. 7/2021.

Página: 10 de 23

En ambos casos, los términos calidad de los datos y exactitud-RGPD no se configuran en términos absolutos, sino en relación con la finalidad del tratamiento. Por ello, unos datos que resultan adecuados o exactos, y que por tanto que cumplen con la calidad para una finalidad, pueden no tener la calidad necesaria para otra finalidad distinta. De igual forma, los datos no veraces o no actuales, en la medida que permitan cumplir con la finalidad de un tratamiento específico, serían lo suficientemente exactos-RGPD o tendrían la necesaria calidad para dicho tratamiento.

III.

TRATAMIENTOS DE DATOS PERSONALES E IA

Un proceso es un conjunto de actividades mutuamente relacionadas, o que interactúan, las cuales transforman elementos de entrada en resultados de salida15. Todo proceso tiene un propósito o finalidad, y su implementación será eficaz cuando sea capaz de cumplir dicho propósito. Asimismo, para asegurar que dichos resultados cumplen unos requisitos mínimos de eficacia, deberán obtenerse evidencias mediante la definición de métricas específicas para cada tipo de proceso que permitan verificar si se alcanzan esos niveles.
En la medida en que el proceso implica datos personales nos encontramos ante un tratamientoRGPD, que para cumplir el principio de finalidad ha de poder alcanzar su propósito, es decir, ser idóneo16 .

Figura 7 El resultado del tratamiento ha de ser idóneo respecto a su finalidad, lo que dependerá de su diseño, el rendimiento de las operaciones que lo forman, de las salvaguardas desplegadas y de los datos de entrada al tratamiento.

El cumplimiento de los requisitos de idoneidad dependerá, fundamentalmente, de los siguientes factores:
- El diseño del tratamiento como un conjunto de operaciones de distinta naturaleza17 y la
relación entre ellas.
- La calidad de los datos de entrada al tratamiento, inclusive la calidad de los datos no
personales.
- La calidad de los datos que sean resultados de cada una de las operaciones que conforman
el tratamiento, que generarán datos intermedios.

15 ISO 9001:2015
16 STC 14/2003, de 28 de enero, juicio de idoneidad: evaluar si la medida es susceptible de conseguir el objetivo propuesto.
17 Operaciones ejecutadas por personas, por sistemas digitales, por sistemas de IA, por el responsable, por un encargado, en la nube,

automatizadas, etc.
Página: 11 de 23

-

Las salvaguardas desplegadas en el tratamiento (p.ej. preprocesado de los datos, supervisión humana, supervisión con algoritmos, evaluación de convergencia, filtrado de acuerdo a políticas, alertas, gestión de quejas e incidencias, …), que podrían aplicarse para corregir problemas de calidad de los datos de entrada, problemas de calidad en los datos intermedios generados por cada uno de los sistemas que implementan las operaciones de tratamiento y, también, las salvaguardas que corrigen el resultado de salida del tratamiento.

Estos factores son interdependientes, y han de estar adecuadamente balanceados para conseguir el grado de idoneidad deseado en el resultado del tratamiento.

A. TIPOS DE TRATAMIENTOS DE DATOS PERSONALES
El resultado del tratamiento de datos, tanto personales como no personales, puede ser una acción, una decisión, incluyendo una decisión sobre una persona física, un perfil sobre dicha persona o un dato personal en general. También puede dar como resultado (incluso simultáneamente) datos no personales, como una decisión estratégica, un valor estadístico, la definición de una política o un modelo de IA que no contenga datos personales.

Figura 8 Tres casos de tratamientos de datos personales clasificados con el criterio de si los datos de entrada al tratamiento son personales o no, y si el resultado de salida es un dato personal o no.

Un tratamiento (caso 1) podrá, en función de datos personales y no personales (estos últimos podría ser, por ejemplo, baremos, estadísticas, presupuestos u otros) obtener un resultado de salida que podría determinar si un ciudadano va a recibir una beca o una ayuda, evaluar su fiabilidad financiera, calificarlo para un trabajo, determinar su productividad, darle acceso a un servicio o local, etc. Es decir, tomar una decisión, perfilarlo o inferir otros datos. Este resultado de salida, que suponen datos vinculados a una persona física, ha de ser lo suficientemente exactosRGPD (y mínimos-RGPD) para que la finalidad del tratamiento se cumpla de forma idónea. A su vez, los datos personales de entrada al tratamiento tendrán que ser exactos-RGPD (y mínimos-RGPD).
También, el conjunto de todos los datos de entrada al tratamiento, incluyendo los no personales, tendrá que tener la calidad de los datos suficiente para que la finalidad se pueda alcanzar tal y como está diseñado e implementado el tratamiento.
Un tratamiento (caso 2) puede utilizar datos personales (y no personales) para definir una política pública, como la distribución de recursos educativos en función del perfil y rendimiento de los alumnos, analizar una situación económica de una región, etc. En este caso el resultado de salida de dicho tratamiento no sería un dato personal. Sin embargo, el resultado de salida deberá
Página: 12 de 23

tener la calidad suficiente para que la finalidad se pueda cumplir y el tratamiento de los datos personales utilizados sea leal y legítimo. A su vez, los datos de entrada al tratamiento tendrían que cumplir las condiciones descritas en el caso anterior.
Un tratamiento (caso 3) que sin recibir de entrada ningún dato personal tome una decisión sobre una persona física, perfile o infiera datos que se vinculen a una persona física es más difícil de plantear. Podría ser el caso de un sorteo de plazas, la generación de números en una lotería, o cualquier otro caso en el que se aplique una regla ajena al individuo pero que finalmente se asocie a él o le afecte significativamente. En la medida que el resultado sean datos personales tendrá que cumplir las mismas condiciones que en los casos anteriores.

B. CALIDAD DE LOS DATOS EN TRATAMIENTOS DE DATOS PERSONALES QUE INCLUYEN SISTEMAS DE IA
Las distintas operaciones de un tratamiento concreto se pueden implementar de diferentes formas: con personas y/o con sistemas y/o, en particular, con uno o más sistemas de IA. Si nos enfocamos en el sistema de IA, este ha de producir resultados con la calidad suficiente para cumplir la finalidad del tratamiento.

Figura 9 Aspectos de calidad de datos para tener en cuenta cuando se despliega uno o más sistemas/modelos de IA en un tratamiento. En la figura se han representado deliberadamente dos, para evidenciar que no hay una correspondencia directa entre sistema de IA y tratamiento

El sistema de IA podría ser tan simple como un modelo de IA con los mínimos interfaces o, por el contrario, un complejo servicio SaaS de IA generativa, o agéntica, que ya incorpora numerosas operaciones y salvaguardas18 tanto a la entrada como a la salida del sistema.
Los resultados de salida de un sistema de IA (ya se denominen inferencias 19, predicciones, contenidos, recomendaciones o decisiones, entre otros) que forma parte de un tratamiento podrán ser una entrada para operaciones posteriores del mismo tratamiento. Entre ellas, y sería
18 Firewalls, limitadores de interacción, balanceo de carga, circuit breakers, detectores de información personal, clasificadores de texto y

contenido, higienizadores, modelos de embedding, rerankers, memorias, RAGs y su gestión, generador del prompt, selectores de modelos, escaldo, autorecuperación, reformateo, detector de alucinaciones, de copyright, gestor de referencias y citas, filtros de toxicidad, aplicación de políticas de servicio, llamadas a herramientas, APIs, clientes MCP, etc.
19 El RIA, en el considerando 12, habla de "capacidad de inferencia" como la capacidad de obtener los resultados de salida enumerados a continuación.
Página: 13 de 23

lo más recomendable, operaciones que implementen salvaguardas adicionales y supervisión humana. Por ello, el nivel mínimo de calidad de los datos y/o exactitud-RGPD exigible a los resultados de salida del sistema IA dependerá de varios factores:
- Los requisitos de calidad de datos y/o exactitud-RGPD definidos para garantizar el
cumplimiento de la finalidad del tratamiento de forma idónea.
- El respeto a los derechos y libertades de las personas físicas identificadas o identificables
cuando dichos resultados sean relativos a ellas.
- El conjunto de operaciones posteriores al sistema IA dentro del tratamiento que modifiquen
o corrijan los resultados generados por dicho sistema de IA (un sistema IA podría generar salidas para otro sistema IA dentro del mismo tratamiento, como en los sistemas multiagente).
- En particular, de las salvaguardas internas incluidas en el diseño del tratamiento destinadas
a corregir los errores conocidos del sistema de IA.
La capacidad del sistema de IA de proporcionar la calidad exigible una vez desplegado en el tratamiento no dependerá únicamente de éste, sino de varios factores de diseño del tratamiento y de su contexto, por ejemplo:
- De la calidad de los datos de entrada al sistema IA, que podrán haber sido resultados de
otras operaciones que se realizan en el marco del tratamiento, como recogida de datos de sensores, bases de datos o interacción con un humano.
- De las salvaguardas desplegadas durante el diseño del tratamiento que se apliquen a dichos
datos de entrada, como las que impiden una degradación en la dinámica de la operación sobre el sistema IA desplegado (bucle de retroalimentación20).
- De la adecuación del sistema IA, diseñado para unos propósitos más o menos concretos, con
relación a la finalidad del tratamiento donde se ha desplegado.
Los requisitos de calidad de los datos de entrada al tratamiento podrán definirse cuando se conozcan las condiciones de idoneidad del tratamiento. Estas, a su vez, se podrán determinar teniendo en cuenta, entre otros, los requisitos de exactitud-RGPD del resultado y el impacto a los derechos de las personas físicas. El diseño del tratamiento, incluyendo las salvaguardas que se planifiquen, podrán matizar dichos requisitos de calidad de los datos de entrada.

Figura 10 Definir los requisitos de calidad de los datos de entrada no es posible si no se conocen los requisitos de idoneidad de los tratamientos probables.

Los hechos demuestran que el sistema perfecto es una ilusión, ya sea sistema IA o no-IA. La adecuación de un sistema IA dependerá de cómo el diseño del tratamiento, donde se despliega, aproveche sus bondades y gestione adecuadamente sus defectos en el marco de un contexto y una finalidad específica. Un sistema o modelo de IA puede tener muy distinto rendimiento dependiendo de las condiciones de despliegue en un entorno determinado. Por lo tanto, no sería exigible un sistema IA perfecto, sino un sistema IA adecuado al diseño del tratamiento, teniendo en cuenta los efectos del sistema sobre las decisiones o evaluaciones sobre las personas
20 Considerando 67 del RIA. En el caso de despliegue sin reentrenamiento, porque se alimenten RAGs, prompts o memoria de forma

dinámica.
Página: 14 de 23

afectadas. Debe destacarse que el rendimiento agregado del sistema de IA puede ocultar errores o inexactitudes en inferencias individuales, especialmente cuando se evalúa mediante métricas globales. Ello exige la adopción de mecanismos adicionales de control cuando los resultados del sistema puedan afectar a personas concretas.

C. EXIGIBILIDAD DE CALIDAD EN LOS DATOS NO PERSONALES DENTRO DE TRATAMIENTOS DE DATOS
PERSONALES

En muchos casos, en un tratamiento de datos personales también estarán involucrados datos no personales, tanto entradas al tratamiento como formando parte del diseño del mismo21. La calidad de los datos no personales también puede ser crítica para conseguir la idoneidad del tratamiento y/o con relación al impacto a los derechos y libertades de personas físicas identificadas o identificables. En esa medida, se deben establecer los requisitos de calidad de los datos no personales y medidas adecuadas para garantizar el cumplimiento del tratamiento.

Figura 11 Ejemplo de cómo un dato no personal de entrada puede influir en el resultado del tratamiento y afectar a una persona. Un error (una falta de calidad) en el dato no personal de entrada puede generar un resultado de salida no exacto-RGPD, aunque el dato personal de entrada sea exacto-RGPD.

D. DESARROLLO DE IA COMO TRATAMIENTO
Un caso específico de tratamiento de datos personales (ver caso 2 definido en el apartado A de este capítulo) involucra el desarrollo o evolución de un modelo o sistema de IA con aprendizaje automático basado en datos. Dicho desarrollo será un tratamiento distinto del tratamiento en el que el sistema de IA es utilizado en fase de explotación o despliegue para tratar datos personales.
La finalidad del tratamiento de desarrollo podría ser crear un sistema que realice una tarea concreta, y ya en el marco del tratamiento decidir que la naturaleza de dicho sistema será una IA.
O bien la finalidad podría ser el desarrollo de una IA en sí misma, por ejemplo, en el caso de proyectos cuya financiación o subvención requiera el diseño específicamente de un modelo de IA.
El ciclo de vida de dicho tratamiento se podría representar utilizando las fases de desarrollo y evolución definidas en el estándar ISO 5338.

21 Pueden tomar la forma de bases de datos, ficheros, tablas y ciertos parámetros de configuración de los sistemas empleados en la

implementación del tratamiento.
Página: 15 de 23

Figura 12 Fases del ciclo de vida de desarrollo de sistemas IA acorde al estándar ISO 5338 destacando los procesos de datos y una clasificación con carácter general de las fases del ciclo de vida que formarían parte de operaciones de un tratamiento de desarrollo y de aquella que formarían parte de un tratamiento de explotación cuando suponga tratamiento de datos personales.

El rendimiento del sistema o modelo IA resultante, con relación a la calidad de los resultados que ofrezca, dependerá, entre otros, de:
- La calidad de los conjuntos de datos de desarrollo (entrenamiento, prueba, validación,
evolución).
- La modificación de la calidad de los datos a lo largo de los procesos de datos del ciclo de
vida.
- La metodología de desarrollo empleada.
- Las decisiones de diseño.
- Los contextos y finalidades previstas.
- Los factores de implementación en el despliegue (p.ej. cuantización del modelo).
- La evolución del contexto en el tiempo (p.ej. casos de context-drift y data-drift)
- En el caso de evolución del modelo de IA, por ejemplo, sesgos generados por bucles de
realimentación.

E. DETERMINACIÓN DE LOS REQUISITOS DE CALIDAD DE LOS DATOS EN EL DESARROLLO DE SISTEMAS DE
IA
La gestión de la calidad de los datos aplicable a un tratamiento destinado al desarrollo de un sistema de IA, tal y como se ha señalado en el apartado B de este capítulo, solo podrá definirse una vez que se conozcan las condiciones de idoneidad de los procesos o tratamientos en los que se prevé desplegar el sistema, puesto que dichas condiciones determinan los requisitos de calidad exigibles a los datos.

Página: 16 de 23
