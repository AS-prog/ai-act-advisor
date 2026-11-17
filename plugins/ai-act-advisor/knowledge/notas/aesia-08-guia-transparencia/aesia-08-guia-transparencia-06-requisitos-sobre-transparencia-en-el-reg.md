---
name: aesia-08-guia-transparencia-06-requisitos-sobre-transparencia-en-el-reg
description: "AESIA: aesia 08 guia transparencia, sección «Requisitos sobre transparencia en el Reglamento (parte 2)» (págs. 24-28). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-08-guia-transparencia
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Requisitos sobre transparencia en el Reglamento (parte 2)"
  paginas: 24-28
  origen: 2026-07-17-aesia-08-guia-transparencia.pdf
  oficial: false
---
# Requisitos sobre transparencia en el Reglamento (parte 2)

Qué entendemos
Garantizar que no haya acciones injustas cuando las acciones del sistema (predicciones, decisiones) estén orientados a personas.
Posibles medidas para contribuir a su cumplimiento
-
-
-

Analizar los datos, asegurando la equidad del sistema respecto del grupo de personas en el que pueda tener influencia el sistema de IA.
Proporcionar mecanismos que permitan analizar de lo más global a lo más particular, asegurando así el análisis sobre grupos de personas y personas concretas.
Utilizar contrafactualidad para poder detallar las razones tomadas sobre personas y grupos de personas.
4.3.2.6.

Apartado 3b.vi. Datos de entrada

AI Act
Art.13.3b.vi - Transparencia y comunicación información a los responsables del despliegue

de

cuando proceda, especificaciones relativas a los datos de entrada, o cualquier otra información pertinente en relación con los conjuntos de datos de entrenamiento, validación y prueba usados, teniendo en cuenta la finalidad prevista del sistema de IA de alto riesgo.

Qué entendemos
Pretende dar visibilidad de la naturaleza de los datos utilizados, para que el usuario pueda entender y evaluar si la muestra de datos es justa y representativa para el objetivo del sistema.
Posibles medidas para contribuir a su cumplimiento
-

Transparencia sobre los datos utilizados
4.3.2.7.

Apartado 3b.vii. Información de salida

AI Act
Art.13.3b.vii - Transparencia y comunicación de información a los responsables del despliegue en su caso, información que permita a los responsables del despliegue interpretar los resultados de salida del sistema de IA de alto riesgo y utilizarla adecuadamente;

23

Qué entendemos
Asegurar el entendimiento de la información de salida del sistema.
Posibles medidas para contribuir a su cumplimiento
-
-
-
-

Medidas de Trasparencia sobre los datos utilizados, teniendo en cuenta cual será la salida del sistema.
Detallar de lo más global a lo más particular que pueda producirse en dicha salida.
Aplicar prudencia y no revelar información sensible en la salida del sistema.
Utilizar contrafactualidad para detallar en la salida qué el porqué de dicha acción o en qué circunstancias dicha acción podría haber sido otra si se modificaran algunas de las informaciones tenidas en cuenta.

4.3.3. Apartado 3c. Cambios

AI Act
Art.13.3c - Transparencia y comunicación información a los responsables del despliegue

de

los cambios en el sistema de IA de alto riesgo y su funcionamiento predeterminados por el proveedor en el momento de efectuar la evaluación de la conformidad inicial, en su caso;

Qué entendemos
Asegurar que la entidad usuaria es informada de los cambios realizados en el sistema por el proveedor, con las implicaciones que esto pudiera tener en su comportamiento y/o precisión.
Esto es especialmente importante, ya que la evaluación inicial de conformidad establece un
OK antes de poner en funcionamiento el sistema, que debe mantenerse durante el funcionamiento y evolución del mismo. Además, se da la circunstancia de que los sistemas de
IA pueden degradar su rendimiento con el tiempo debido, por ejemplo, a los nuevos datos de entrada recibidos por el sistema (data drift), o bien incluso debido a cambios en el mismo
(model drift).
Posibles medidas para contribuir a su cumplimiento
-
-

Utilizar métricas integradas en el ciclo de vida del sistema
Para comunicar dichos cambios será necesario habilitar un canal de comunicación entre entidad proveedora y usuaria.

24

4.3.4. Apartado 3d. Vigilancia humana

AI Act
Art.13.3d - Transparencia y comunicación información a los responsables del despliegue

de

las medidas de supervisión humana a que se hace referencia en el artículo 14, incluidas las medidas técnicas establecidas para facilitar la interpretación de los resultados de salida de los sistemas de IA de alto riesgo por parte de los responsables del despliegue;

Qué entendemos
Aplicar medidas de transparencia sobre el sistema de IA permite entender su funcionamiento e interpretar sus resultados. Como consecuencia, y de manera bidireccional, la transparencia y la supervisión humana (desarrollada en el artículo 14 del reglamento) están completamente relacionadas, ya que para que el sistema pueda ser supervisado por personas es fundamental que el sistema sea transparente. Por tanto, todas las medidas aplicables a la transparencia y a la supervisión humana son las que resuelven este artículo.
Posibles medidas para contribuir a su cumplimiento
Todas las medidas técnicas reflejadas en el presente documento, ya que todas ellas permiten facilitar la interpretación de la información de salida del sistema de IA:
o Atender al dominio de funcionalidad o Asegurar el objetivo funcional del sistema o Trasparencia sobre los datos utilizados o Detallar de lo más global a lo más particular o Adaptar el lenguaje o Gestionar la complejidad o Utilizar métricas integradas en el ciclo de vida del sistema o Aplicar prudencia o Usar causalidad y minimizar correlaciones o Utilizar contrafactualidad
Adicionalmente, las indicadas en la guía del artículo 14 (Supervisión humana).

25

4.3.5. Apartado 3e. Recursos HW/SW y mantenimiento

AI Act
Art.13.3e - Transparencia y comunicación información a los responsables del despliegue

de

los recursos informáticos y de hardware necesarios, la vida útil prevista del sistema de IA de alto riesgo y las medidas de mantenimiento y cuidado necesarias (incluida su frecuencia) para garantizar el correcto funcionamiento de dicho sistema, también en lo que respecta a las actualizaciones del software;

Qué entendemos
Este apartado está en parte relacionado con el 13.3.c, que pretende igualmente que la entidad usuaria sea informada de los cambios realizados en el sistema como parte de su mantenimiento y evolución por el proveedor, con las implicaciones que esto pudiera tener en su comportamiento y/o precisión y así garantizar su correcto funcionamiento ante los mismos.

Posibles medidas para contribuir a su cumplimiento
-

Utilizar un sistema de integración continúa sobre el sistema de IA y su utilización
(incluyendo los datos procesados por el usuario), aplicando métricas integradas en el ciclo de vida del sistema que permitan medir la utilización, el rendimiento y el impacto de las actualizaciones en el mismo.

4.3.6. Apartado 3f. Archivos de registro

AI Act
Art.13.3f - Transparencia y comunicación información a los responsables del despliegue

de

cuando proceda, una descripción de los mecanismos incluidos en el sistema de
IA de alto riesgo que permita a los responsables del despliegue recabar, almacenar e interpretar correctamente los archivos de registro de conformidad con el artículo 12.

26

Qué entendemos
En la línea de facilitar el entendimiento y uso apropiado de los sistemas por parte de los usuarios, se trata de describir e implantar los mecanismos contenidos dentro del propio sistema de IA de alto riesgo para permitir que los usuarios del propio sistema puedan recoger, guardar e interpretar correctamente los logs, siempre que estos sean considerados relevantes. Pretende definir el alcance de lo que una IA transparente debería ser.
Concretamente, menciona que los usuarios del sistema deberían poder recoger, guardar e interpretar los logs del sistema siempre que estos sean relevantes.
Posibles medidas para contribuir a su cumplimiento
- Las indicadas en la guía del artículo 12 del Reglamento Europeo de la IA (Registros).

27
