---
name: aesia-10-guia-solidez-02-preambulo
description: "AESIA: aesia 10 guia solidez, sección «Preámbulo» (págs. 7-10). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-10-guia-solidez
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Preámbulo"
  paginas: 7-10
  origen: 2026-07-17-aesia-10-guia-solidez.pdf
  oficial: false
---
# Preámbulo

1. Preámbulo
1.1 Objetivo del documento
Un sistema de IA de alto riesgo tiene que estar preparado para minimizar y prevenir los comportamientos perjudiciales e indeseables y ser capaz de detectar cuando su funcionamiento tenga lugar fuera de aquel dominio de entrada y ejecución establecido por su finalidad prevista. De igual modo tiene que estar diseñado e implementado para evitar la adopción de decisiones equivocadas o generar una información de salida errónea. Todo ello para evitar consecuencias negativas para la seguridad y los derechos fundamentales.
Es objetivo de esta guía establecer las medidas necesarias que, a título orientativo y no vinculante se relacionan con los requerimientos del Reglamento Europeo de la IA, en lo relativo a la solidez del sistema de alto riesgo.
El Reglamento Europeo de la IA considera el concepto de solidez técnica como un mecanismo clave para los sistemas de IA de alto riesgo. Así lo desarrolla a través de su considerando (75), donde establece que:

AI Act
Considerando (75)
La solidez técnica es un requisito clave para los sistemas de IA de alto riesgo, que deben ser resilientes en relación con los comportamientos perjudiciales o indeseables por otros motivos que puedan derivarse de limitaciones en los sistemas o del entorno en el que estos funcionan (p. ej., errores, fallos, incoherencias o situaciones inesperadas).

En las medidas propuestas en esta guía se establece que el sistema de IA deberá considerar en su diseño, desarrollo y validación, las soluciones técnicas y organizativas para prevenir dichas situaciones, incluso, con la posibilidad de que cuando, dicha solidez técnica no opere dentro de parámetros seguros, el sistema pueda interrumpir su funcionamiento. Tal es así que lo establece en el mismo considerando (75):

6

AI Act
Considerando (75)
[…] los sistemas de IA de alto riesgo, por ejemplo mediante el diseño y desarrollo de soluciones técnicas adecuadas para prevenir o reducir al mínimo ese comportamiento perjudicial o indeseable. Estas soluciones técnicas pueden incluir, por ejemplo, mecanismos que permitan al sistema interrumpir de forma segura su funcionamiento (planes de prevención contra fallos) en presencia de determinadas anomalías o cuando el funcionamiento tenga lugar fuera de determinados límites predeterminados. […]

Dicho de otro modo, la solidez del sistema de IA es tan relevante que en aquellos casos en los que no pueda garantizarse adecuadamente, el sistema debe estar preparado para interrumpir su funcionamiento de manera controlada.
Es responsabilidad del proveedor del sistema de inteligencia artificial de alto riesgo tomar las medidas adecuadas (tanto organizativas como técnicas) para garantizar que se cumple con los requerimientos de solidez del sistema. Igualmente, dentro de su ámbito de aplicación, el responsable del despliegue del sistema también tiene responsabilidades que se materializarán en medidas concretas (de nuevo organizativas y técnicas).
Desarrollaremos a lo largo de la guía una serie de medidas organizativas y técnicas orientativas destinadas primero a validar el sistema de inteligencia artificial y, a continuación, a aplicar los controles de calidad del modelo que ayudan a verificar y validar las razones que llevan a seleccionar tales métricas.
En cuanto a aspectos complementarios que son clave para poder implantar el sistema con el objetivo de ejecutar su finalidad prevista, estas métricas van más allá del resultado inmediato del modelo para un baremo de pruebas, y pueden tener implicaciones de discriminación, sesgo o imprecisión.
A lo largo de la guía abordaremos la relación con estos aspectos complementarios, y su inclusión en el concepto de solidez.

1.2 ¿Cómo leer esta guía?
Esta guía está estrechamente relacionada con las guías relativas al artículo 15 de precisión, solidez y ciberseguridad.
La solidez del sistema de IA tiene, entre otros objetivos, la conservación de la precisión obtenida durante el entrenamiento, prueba y validación del sistema a lo largo del ciclo de vida de este; especialmente en aquellas entradas que no se encuentran en el conjunto de entrenamiento y validación, pero que se encuentran dentro del dominio del sistema de IA.
La relación con la ciberseguridad es también estrecha. Por un lado, la ciberseguridad contribuye a la solidez del sistema al protegerlo frente a ataques adversarios, que podrían
7

alterar su respuesta (y por ende su precisión). Por otro lado, los mecanismos de solidez deben garantizar que las medidas de ciberseguridad se mantienen en el tiempo.
Para una correcta aplicación de esta guía, se ha estructurado siguiendo el artículo del
Reglamento Europeo de la IA, y a la vez proporcionando una serie de medidas que permitan cubrir los requisitos establecidos en el artículo 15 previamente analizado, en relación con la solidez.
La guía aborda en primer lugar en el apartado 4, como establecer unas métricas de solidez para el sistema, su validación y verificación. Es un apartado de peso importante en relación con las responsabilidades del proveedor del sistema de IA, porque establece las bases para definir la solidez de su sistema de IA. Se acompaña un detalle ampliado en el 7.1
Anexo I: Métricas y pruebas para sistemas de IA que puede ser consultado para ampliar la base teórica de lo que se pretende explicar en el citado apartado. En este apartado, la solidez se relaciona con eficiencia, rendimiento y monitorización para ofrecer una visión completa.
Siguiendo las recomendaciones del Reglamento Europeo de la IA en el artículo 15, se presentan en el apartado 4.1 medidas para conservar la solidez establecida cuando el sistema está expuesto a errores.
En el apartado 4, se establece que la solidez, una vez definida y protegida frente a fallos, pueda estar garantizada gracias a una serie de medidas destinadas a establecer su continuidad en el tiempo.
Para aquellos sistemas que continúan aprendiendo con el tiempo, ya sea porque lo hacen de manera automática, o de manera programada a través de recolección de datos (o retroalimentación de usuarios) y progresivas actualizaciones, en el apartado 5 se proporcionan medidas técnicas específicas.
El proveedor debe considerar que esta guía ofrece unas recomendaciones sobre la cobertura de los requisitos establecidos en el artículo 15 del Reglamento Europeo de la IA, pero que no es un compendio exhaustivo ni vinculante, y que puede que, en algunos casos, tenga necesariamente, que considerar adaptar los detalles específicos
(especialmente lo referido en los Anexos) a la naturaleza y la finalidad prevista del sistema y los riesgos para la salud y los derechos y libertades de las personas físicas.
Las instrucciones sobre cómo obtener la solidez asociada al sistema, cómo usarla e interpretarla, sus umbrales y métricas asociadas a ella deben documentarse según la guía de Documentación técnica. A continuación, a lo largo de la guía detallaremos dimensiones a tener en cuenta para ello.

1.3 ¿A quién está dirigido?
Dar cabida a todas las cuestiones detalladas en esta guía es responsabilidad del proveedor del sistema de inteligencia artificial de alto riesgo tomando las medidas adecuadas aquí propuestas, tanto organizativas como técnicas. Todo ello con el objetivo de garantizar que se cumple con los requisitos de precisión del sistema.

8

Dentro de su ámbito de aplicación, el responsable del despliegue del sistema también tiene responsabilidades que se materializarán en medidas concretas, de nuevo organizativas y técnicas. La guía indicará, en cada caso, cuales le son de aplicación y el alcance de estas.

1.4 Casos de uso utilizados en la guía
A lo largo de la guía se utilizarán dos casos de uso a modo de ejemplo de cómo elaborar la documentación técnica. Los ejemplos estarán centrados únicamente en el proveedor que es el responsable de generar y conservar la documentación. La descripción detallada de los casos de uso utilizados podrá encontrarse en la Guía práctica y ejemplos para entender el Reglamento de IA.
Nota: Siempre que se ponga un ejemplo, se hará de manera ilustrativa. Proveedor y responsable del despliegue han de considerar la aplicación orientativa de las medidas indicadas en esta guía.
Los casos de uso se han seleccionado atendiendo a su capacidad para explicar la información y procedimientos detallados en esta guía, por continuidad con la guía de precisión, se han seleccionado los mismos casos.
Los casos seleccionados en este caso para la elaboración de la guía son:
- Detección de denuncias falsas
- Sistema de promoción de empleados.

9
