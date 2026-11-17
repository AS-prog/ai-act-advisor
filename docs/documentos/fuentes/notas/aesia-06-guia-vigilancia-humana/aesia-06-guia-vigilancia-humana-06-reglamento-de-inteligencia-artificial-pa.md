---
name: aesia-06-guia-vigilancia-humana-06-reglamento-de-inteligencia-artificial-pa
description: "AESIA: aesia 06 guia vigilancia humana, sección «Reglamento de Inteligencia Artificial (parte 3)» (págs. 28-30). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-06-guia-vigilancia-humana
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Reglamento de Inteligencia Artificial (parte 3)"
  paginas: 28-30
  origen: 2026-07-17-aesia-06-guia-vigilancia-humana.pdf
  oficial: false
---
# Reglamento de Inteligencia Artificial (parte 3)

Ejemplo - Bomba de insulina
Uno de los errores en este modo de error forzado consistirá, por ejemplo, en que el sistema proponga al médico una dosis no adecuada a uno de sus pacientes en función de valores anormales en sangre identificados igualmente por el sistema sobre el mismo. El médico deberá identificar dicha situación, marcarla como errónea, e indicar la dosis correcta para que el sistema se lo comunique al paciente, demostrando así que su vigilancia sobre las propuestas de decisión tomadas por el sistema es correcta.

Ejemplo - Concesión de ayudas
Uno de los errores en este modo de error forzado consistirá, por ejemplo, en que el sistema proponga al responsable de las concesiones una horquilla de importe de ayuda no alineada con los ingresos económicos y necesidades de la familia. Dicho responsable deberá identificar dicha situación, marcarla como errónea, e indicar la horquilla correcta, demostrando así que su vigilancia sobre las propuestas de decisión tomadas por el sistema es correcta.

A qué apartados aplica esta medida
-

Apartado 4b. Sesgo de automatización

4.2.5 Gobernanza. Human in/on the loop
Una de las decisiones que se ha de tomar en el diseño del sistema de IA es el nivel de autonomía que se le concede al mismo. Dicho nivel de autonomía se enmarca en los aspectos procedimentales a definir en el modelo de gobernanza del sistema de IA. Existen tres niveles:
-

-

-

El primero, y más global, que ha de tenerse siempre en cuenta ya que refuerza el concepto de Supervisión Humana, es el de Human in Command (HIC), y se refiere a cómo un ser humano es el responsable último y toma las decisiones críticas en el funcionamiento de un sistema de IA. Este concepto profundiza en la idea de una posición de responsabilidad última de las personas en el funcionamiento del sistema de IA y de las decisiones críticas que se toman en su funcionamiento para garantizar decisiones finales y el logro de los objetivos deseados de manera segura y confiable.
Human-in-the-loop (HITL) se refiere a la intervención humana en cada acción del sistema, lo que en muchos casos no es posible dado el alto volumen de acciones que gestiona. La supervisión humana en este caso se denomina ex ante, e implica que la acción está parcialmente automatizada. En los casos de uso de alto riesgo (los que nos ocupan en el Reglamento), donde suele ser necesario que una persona valide cada una de las acciones, aunque el volumen de acciones sea alto, este es el nivel que suele ser el recomendado.
Human-on-the-loop (HOTL) se refiere a una intervención humana de vigilancia sobre las acciones que es realizada a posteriori. La supervisión humana en este caso se denomina ex post, e implica que la acción está totalmente automatizada, aunque se
27

deba habilitar posteriormente la posibilidad de que una intervención humana permita revertirla. Este nivel de autonomía no es especialmente recomendado en los casos de alto riesgo que nos ocupan, debido al riesgo de impacto difícilmente reversible sobre los derechos fundamentales de las personas, uno de los objetivos principales del
Reglamento.
Independientemente del nivel de autonomía aportado por ambos niveles, el sistema puede disponer de un mecanismo que permita la desactivación inmediata del mismo, sin perjuicio de la existencia de un Plan de continuidad de negocio que permita que el proceso soportado por el sistema pueda recuperar y restaurar sus funciones.
El nivel utilizado determinará el nivel de supervisión humana que se ejerza sobre el sistema de IA, y tendrá impacto en los procedimientos de gobernanza asociados al sistema cuando esté en uso.
En ambos casos el sistema registrará las dos acciones: la propuesta o incluso ejecutada por el sistema, y la ejecutada finalmente por el responsable del mismo, siguiendo las medidas indicadas en la guía del artículo 12 (Registros).
A quién aplica
-

-

Es el responsable del despliegue quien tiene que determinar el nivel de autonomía que se proporciona al sistema en función del caso de uso que soporte dentro de su negocio, así como el procedimiento de gobernanza asociado a dicho nivel cuando el sistema esté en uso.
El proveedor tiene que implementar los mecanismos técnicos que permitan cada uno de los mencionados niveles.

Ejemplo - Bomba de insulina
Este es un caso donde, debido a que la aplicación inmediata de la decisión pudiera poner en riesgo un derecho fundamental de las personas (la salud), el sistema debe ser diseñado con un enfoque Human-in-the-loop (HITL). Por tanto, cuando el sistema proponga la siguiente dosis a un paciente, su médico responsable deberá validarla o ajustarla en base a los parámetros en sangre del paciente recabados por el sistema, momento en el cual el paciente podrá recargar la bomba de insulina con la cantidad indicada por el sistema y administrársela.

Ejemplo – Concesión de ayudas
Este es igualmente un caso de uso que requiere de un nivel Human-in-the-loop (HITL), tanto por la naturaleza funcional “propositiva” del sistema que no requiere inmediatez como, principalmente, por el impacto de la decisión finalmente adoptada. El sistema analiza las peticiones de ayuda realizadas por las familias, y el gestor publico responsable de las mismas podrá analizarlas una a una, estableciendo la cuantía finalmente asignada. Por tanto, cuando el sistema, por ejemplo, proponga la cuantía asignada a una familia, el responsable público deberá validarla en base a la información económico-social recabada de la misma.

A qué apartados aplica esta medida
28

-
-

Apartado 4e. Autonomía para decidir
Apartado 4e. Interrupción

4.3 Resumen ejecutivo. Relación Apartado-medidas aplicables

Apartados
1. Diseño y desarrollo para una vigilancia efectiva
2. Riesgos sobre derechos fundamentales, salud y seguridad
3. Tipos de medidas
4. Entendimiento y Autonomía
4a. Entender capacidades y limitaciones
4b. Sesgo de automatización
4c. Interpretar la información de salida
4d. Autonomía para decidir
4e. Interrupción
5. Identificación biométrica

edidas
MV4 MV5 MV6 MV7

X

X

X
X

X
X

X

MV1
MV2
MV3
MV4
MV5
MV6
MV7

Medidas
MV1 MV2 MV3 MV4 MV5 MV6 MV7
X
X
X
X
X
X
X
X
X
X
X
X
X

X
X
X
X

X

Medidas de diseño y desarrollo para una vigilancia efectiva
Habilitar una interfaz humano-máquina
Modelo de gobernanza
Concienciación. Error forzado
Gobernanza. Human in/on the loop
Artículo 09. Sistema de gestión de riesgos
Artículo 13. Transparencia

X
X
X

29

MV1
MV2
MV3
MV4
MV5
MV6
MV7

Med
Habi
Mod
Conc
Gobe
Artíc
Artíc
