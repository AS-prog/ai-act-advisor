---
name: aesia-09-guia-de-precision-03-introduccion
description: "AESIA: aesia 09 guia de precision, sección «Introducción» (págs. 9-11). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-09-guia-de-precision
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Introducción"
  paginas: 9-11
  origen: 2026-07-17-aesia-09-guia-de-precision.pdf
  oficial: false
---
# Introducción

2. Introducción
2.1 ¿Qué es la precisión para IA?
En el contexto del Reglamento Europeo de IA, se indica, en su considerando (66) que la precisión está entre los requisitos fundamentales para la mitigación de los riesgos asociados al sistema de IA:

AI Act
(66)
Deben aplicarse a los sistemas de IA de alto riesgo requisitos referentes a la gestión de riesgos, la calidad y la pertinencia de los conjuntos de datos utilizados, la documentación técnica y la conservación de registros, la transparencia y la comunicación de información a los responsables del despliegue, la supervisión humana, la solidez, la precisión y la ciberseguridad. Dichos requisitos son necesarios para mitigar de forma efectiva los riesgos para la salud, la seguridad y los derechos fundamentales […].

Aclaración sobre la nomenclatura del inglés: En esta guía se ha traducido el término en inglés accuracy, genéricamente, por precisión, siguiendo la traducción aportada por el
Reglamento Europeo en español. Sin embargo, se han mantenido excepciones cuando el término accuracy forma parte de un término compuesto (ejemplo, balanced accuracy) en cuyo caso se hace referencia al término compuesto en inglés para evitar confusión y mantener así una única nomenclatura internacional como aquella usada en la mayoría de los métodos y herramientas y librerías. Es importante notar que, en ocasiones, cuando se habla del término de accuracy para referirse a la noción de performance, como medida de calidad del modelo más genérico, en inglés, en IA, se suele sobreentender nos referimos a accuracy, precisión, recall, etc. o la métrica asociada en particular al problema a resolver. En estos casos se ha mantenido la traducción usual en español para no causar confusión. En definitiva: accuracy se tradujo por exactitud, precisión por precisión, y performance (aunque se suele traducir por rendimiento o eficiencia fuera de campos de la IA como high performance computing o ingeniería del software), en esta guía se ha traducido por precisión.
Siempre que se ponga un ejemplo, se hará de manera ilustrativa. Proveedor y responsable
Podemos considerar que la precisión, entendida indicado en la nota previa, nos del despliegue han de considerar la aplicación decomo todashemos las medidas indicadas en esta guía.
permite acotar, delimitar y conocer el comportamiento del sistema de IA acorde a su finalidad prevista, los conjuntos de datos con los que va a trabajar, y la relación de la precisión con el resto de los requisitos, entre otros: ciberseguridad, solidez, transparencia, gobierno del dato,
8

supervisión. Además, la precisión es una métrica fundamental dentro del sistema de gestión de calidad que rodea al sistema de IA de alto riesgo.
El Reglamento Europeo de IA indica también, en su considerando (74) la necesidad que el nivel de precisión esté al día de los avances y estado del arte del campo y que este nivel sea mantenido durante todo el ciclo de vida del sistema de IA, desde su puesta en el mercado hasta su retirada.

AI Act
(74)
Los sistemas de IA de alto riesgo deben funcionar de manera uniforme durante todo su ciclo de vida y presentar un nivel adecuado de precisión, solidez y ciberseguridad, a la luz de su finalidad prevista y con arreglo al estado actual de la técnica generalmente reconocido. Se anima a la Comisión y las organizaciones y partes interesadas pertinentes a que tengan debidamente en cuenta la mitigación de los riesgos y las repercusiones negativas del sistema de IA. El nivel previsto de los parámetros de funcionamiento debe declararse en las instrucciones de uso que acompañen a los sistemas de IA. Se insta a los proveedores a que comuniquen dicha información a los responsables del despliegue de manera clara y fácilmente comprensible, sin malentendidos ni afirmaciones engañosas.

Cómo podemos comprobar en el considerando anterior, el Reglamento Europeo de IA se puede entender una clara relación entre la precisión y la transparencia, al relacionar ambas con la información al responsable del despliegue.
Por otro lado, la precisión se encuentra muy presente a lo largo del Anexo IV del Reglamento
Europeo de IA, que explica cómo debe abordarse la documentación técnica. Sirva de ejemplo el siguiente extracto del párrafo 3 del Anexo IV, relativo a la relación entre documentación técnica y precisión.

AI Act
Anexo IV.3 – Documentación técnica a que se refiere el artículo 11, apartado 1
Información detallada acerca de la supervisión, el funcionamiento y el control del sistema de IA, en particular con respecto a sus capacidades y limitaciones de funcionamiento, incluidos los niveles de precisión para las personas o colectivos de personas específicos en relación con los que está previsto que se utilice el sistema y el nivel general de precisión esperado en relación con su finalidad prevista; […].

9

El proceso para alcanzar la precisión puede ser visualizado como:

10
