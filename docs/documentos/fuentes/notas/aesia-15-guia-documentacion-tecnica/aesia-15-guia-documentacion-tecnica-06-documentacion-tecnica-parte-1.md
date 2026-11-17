---
name: aesia-15-guia-documentacion-tecnica-06-documentacion-tecnica-parte-1
description: "AESIA: aesia 15 guia documentacion tecnica, sección «Documentación técnica (parte 1)» (págs. 25-32). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-15-guia-documentacion-tecnica
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Documentación técnica (parte 1)"
  paginas: 25-32
  origen: 2026-07-17-aesia-15-guia-documentacion-tecnica.pdf
  oficial: false
---
# Documentación técnica (parte 1)

5.

Documentación técnica

El Artículo 11, documentación técnica, establece que el Anexo IV define el contenido mínimo que deberá tener la documentación técnica. Este comienza indicando que:

AI Act
Anexo IV – Documentación técnica referida al artículo
11, apartado 1
La documentación técnica a que se refiere el artículo 11, apartado 1, incluirá como mínimo la siguiente información, aplicable al sistema de IA pertinente:

Para ofrecer un contexto amplio al lector de la guía, se ha dispuesto el texto completo de dicho Anexo en el apartado 3.2. Documentación Técnica a que se refiere el artículo 11,
Apartado 1: Anexo IV del Reglamento Europeo de la IA, en los propios anexos que acompaña esta guía para que pueda ser consultado de manera íntegra y con todas sus partes en contexto.
Este apartado se presenta como ejemplo de la estructura que deberá tener la documentación técnica, para el sistema de IA al completo. En cada apartado vamos a indicar qué elementos se van cubriendo del Anexo IV y la documentación necesaria a aplicar para cumplir con dichos elementos. De esta manera, esta sección de la guía sirve de ejemplo para la construcción de la documentación. En el artículo 11, documentación técnica, párrafo 1 y referido a las pymes, incluidas las empresas emergentes, y pequeñas empresas de mediana capitalización, indica:

AI Act
Art.11.1– Documentación técnica
“[…] Las pymes, incluidas las empresas emergentes, y pequeñas empresas de mediana capitalización, podrán facilitar los elementos de la documentación técnica especificada en el anexo IV de manera simplificada. A tal fin, la Comisión establecerá un formulario simplificado de documentación técnica orientado a las necesidades de las pequeñas empresas y las microempresas. Cuando una pyme, incluidas las empresas emergentes, y pequeñas empresas de mediana capitalización, opte por facilitar la información exigida en el anexo IV de manera simplificada, utilizará el formulario a que se refiere el presente apartado. Los organismos notificados aceptarán dicho formulario a efectos de la evaluación de la conformidad.

24

El artículo establece que puede ser elaborada una documentación equivalente simplificada, que cumpla los mismos objetivos, haciendo uso del formulario simplificado que establecerá la Comisión.

El Anexo IV es extenso y detallado, y tiene el objetivo de indicar qué debe contener la documentación técnica del sistema de IA. En este apartado, para poder abordar el nivel de granularidad requerido, se ha dividido el anexo en apartados. Dentro de cada apartado se fragmenta el texto del anexo para ayudar a completar la documentación técnica exigida, explicando cada aspecto.

Ejemplo - Sistema automático de concesión de ayudas
El proveedor ha estructurado la documentación del sistema de IA acorde a los once diferentes apartados que se detallan en esta sección de la guía. De esta manera ha definido un documento maestro donde se estructura una información inicial de la sección y su ubicación, asociado a una estructura de carpetas y/o documentos por cada uno de los apartados.
Del mismo modo, basado en estos apartados ha establecido el responsable de cada uno de ellos. Por ejemplo, el apartado 5.2 ha sido asignado dentro del equipo de expertos en
IA y desarrollo del modelo. Igualmente, el apartado 5.4, ha sido asignado al departamento de gestión de riesgos.
Finalmente, como guía de cada uno de los documentos específicos por apartado
(referenciados en el documento maestro), se utiliza la estructura para ese apartado descrita en esta guía, alineada con el contenido del Anexo IV.

5.1 Descripción general del sistema de IA
Este apartado tendrá que contener la descripción general del sistema, cubriendo la información que se indica en el párrafo 1 del Anexo IV del Reglamento Europeo de la IA establece que los contenidos que una descripción general del sistema de IA debe tener.

AI Act
Anexo IV.1 – Documentación técnica referida al artículo
11, apartado 1
(a) su finalidad prevista, el nombre del proveedor y la versión del sistema de tal manera que se refleje su relación con versiones anteriores;

La finalidad prevista que debe indicar de manera clara y concisa:
25

✓ Descripción del uso para el que ha sido diseñado y desarrollado el sistema de inteligencia artificial.
✓ El contexto de utilización de dicho sistema de inteligencia artificial.
✓ Las condiciones de uso del sistema.
El nombre del proveedor (y del representante autorizado si procede) y la documentación contendrá la razón o denominación social de la empresa. Se recuerda aquí que se debe incluir también como parte de la documentación los recursos utilizados para el desarrollo del sistema, debiendo de estar incluidos como mínimo en el sistema de gestión de calidad. Debiendo indicar:
✓ El rol o roles de la persona en el contexto de la concepción, implementación y ciclo de vida del sistema de IA. Tomando como referencia al menos los siguientes ámbitos:
o Actores sobre datos: perfiles que actúen sobre los datos que alimentan el aprendizaje del sistema de IA (Analistas de datos, Científicos de datos,
Ingenieros informáticos, Expertos en IA, etc.);
o Actores sobre la configuración y operación del sistema de IA (Expertos en AI,
Ingenieros informáticos, Administradores del sistema de IA, Analistas de sistemas, Expertos en ML, etc.);
o Desarrolladores de integración y/o interacción con el sistema de IA (Incluido
MLOps, en su caso) (Ingenieros informáticos, Desarrolladores, etc.);
o Actores de administración de sistemas que hospedan y operan el sistema de IA
(Administradores del sistema de IA, Analistas de sistemas, etc.);
o Actores sobre la concepción, diseño, implementación y mantenimiento del software que materializa el sistema de IA en sí mismo (Investigadores en IA,
Ingenieros informáticos, Desarrolladores, Analistas, Expertos en IA, etc.);
o Actores sobre la arquitectura, administración y mantenimiento del sistema de
IA en su ciclo de vida, tanto durante el desarrollo como una vez puesto en marcha (Investigadores en IA, Ingenieros informáticos, Expertos en AI,
Administradores del sistema de IA, Expertos en ML, etc.)
✓ La cualificación o cualificaciones específicas en materia de IA y en el campo de la ingeniería informática en general, con especial mención de los conocimientos técnicos sobre tecnologías de inteligencia artificial, datos y computación de datos.
Opcionalmente a la cualificación podrá recogerse la experiencia, especialmente en el caso de investigadores.
✓ Expertos en el dominio de aplicación del sistema de AI, que hayan participado en el diseño y desarrollo.
✓ Perfiles relacionados con los servicios del proveedor a los responsables del despliegue del sistema de IA (implementación, explotación, mantenimiento y soporte del Sistema de IA por parte de los responsables del despliegue del sistema de IA.)
Versión del sistema
✓ En el proceso de desarrollo del sistema, para soportar el versionado adecuado y fiable del sistema, el proveedor deberá establecer técnicamente el control de versiones y detallarlo en esta sección.
✓ El sistema de versionado debe estar correctamente definido, incluyendo en la información o los metadatos de la versión la fecha correspondiente y su relación con versiones anteriores.

26

✓ Tanto la versión como la de la fecha deberán ser aquellos correspondientes a la más reciente del sistema de IA; es decir, que la documentación presentada sea aquella correspondiente a la versión referida y no a otra. Los cambios se documentarán en el apartado 0 Descripción detallada del sistema de gestión de riesgos.

AI Act
Anexo IV.1 – Documentación técnica referida al artículo
11, apartado 1
(b) la manera en que el sistema de IA interactúa o puede utilizarse para interactuar con hardware o software, también con otros sistemas de IA, que no formen parte del propio sistema de IA, cuando proceda;

Interacción con soportes físicos (hardware)
✓ Tecnología de la interoperabilidad con el elemento físico (Driver, API, acceso directo a elementos del dispositivo, etc.) Si se trata de una interacción basada en actuadores, relés o mecanismos que permitan la interacción del sistema de IA con el exterior, por ejemplo, el sistema de IA activa una alarma sonora y visual de aviso de emergencia dentro de un rango de salidas establecidas. En ese caso indicar, en su caso, los parámetros técnicos adicionales que permitan especificar dicha interacción.
✓ Descripción de la información intercambiada con dicho sistema. Como mínimo sobre el formato de intercambio (llamadas, formato personalizado, embebido en la programación, etc.) y el conjunto de informaciones y tipos de datos intercambiados
(por ejemplo, binaria, alfanumérica, comunicación directa por GPIO, o cualquier otro formato de comunicación hardware/software.)
✓ Información sobre el tipo de conexión entre los sistemas;
✓ Descripción del mecanismo de interconexión del sistema de IA con el hardware; por ejemplo, si es cableado directo paralelo, Cableado directo USB, Cableado directo coaxial, a través de internet, comunicación inalámbrica Wifi, Comunicación inalámbrica
5G, VPN, …
✓ En el caso de sistemas de entrada, debe proveerse de una identificación única del sistema (sensor, máquina dedicada, ordenador dedicado, etc.) que quede asociada como fuente a los datos que en su caso se almacenen o registren como parte del funcionamiento del sistema de IA.
Interacción con el software
✓ Formato de integración con el sistema: el software en cuestión recibe la salida del sistema de IA o proporciona el input del sistema de IA.
✓ Información de interoperabilidad: En particular sobre el mecanismo de interacción
(API, directo dentro del entorno de ejecución, etc.) y el formato de la información intercambiada por los sistemas. Como mínimo sobre el formato de intercambio (XML, formato personalizado, etc.) y el conjunto de informaciones y tipos de datos intercambiados (binaria, alfanumérica, etc.).
27

✓ Descripción del canal de comunicación del sistema IA con el software. Por ejemplo, en la misma máquina, en otra máquina de una red local física, en otra máquina de modo inalámbrico, en otra máquina vía VPN, etc.
✓ Ubicación del elemento del software en relación con el sistema de IA (ejecución en el mismo contexto computacional, servicio externo, microservicio externo).
✓ Indicación de si se trata de un servicio propio gestionado por el proveedor, o por el entorno de ejecución del sistema de IA, o es un servicio externo propiedad de un tercero al que el sistema de IA accede en calidad de Software as a service.
✓ En el caso de software que genere datos que sean entradas del sistema de IA, debe proveerse de una identificación única del software que quede asociada como fuente a los datos que en su caso se almacenen o registren como parte del funcionamiento del sistema de IA.

AI Act
Anexo IV.1 – Documentación técnica referida al artículo
11, apartado 1
(c) las versiones de software o firmware pertinentes y todo requisito relacionado con la actualización de versiones

La documentación técnica deberá contener un listado tanto de software como de firmware, que integra el sistema de IA. Esto incluye la información de las versiones de librerías, componentes software, o elementos de terceros ya sean en formato código abierto (en cualquiera de sus versiones de licenciamiento) o como elementos comerciales que hayan podido incorporarse para el desarrollo del sistema de IA y formen parte de éste. Para cada uno de estos elementos conviene incluir:
✓ Identificación del software; su nombre identificativo, o nombre comercial en su caso, tipo de software y nivel de protección de datos que incorpora.
✓ Versión del elemento del componente.
✓ Fecha incorporación y fecha de actualización.
✓ En el caso de componentes firmware (microprogramas) el componente hardware con el que pudieran estar relacionados.
Durante el ciclo de vida de un sistema de IA, pueden realizarse actualizaciones de sus componentes software y/o firmware, sin que estos puedan afectar a la finalidad prevista del mismo. La información anteriormente descrita deberá mantenerse siempre actualizado acorde a estas actualizaciones y manteniendo un histórico de versiones del sistema de IA y su relación con versiones de componentes de manera clara, por ejemplo, en una tabla.
El proveedor puede facilitar un esquema que recoja la totalidad de los componentes software y hardware relacionados con el sistema de IA, e indicará para cada uno de ellos si es de naturaleza totalmente algorítmica (no IA) o bien si tiene naturaleza de IA en el sentido del
Artículo 3.1 del Reglamento Europeo de la IA:

28

✓ Componentes software que integran el sistema de IA.
✓ Elementos software que interoperan con el sistema de IA pero que no forman parte del sistema de IA.
✓ Elementos hardware que interoperan con el sistema de IA pero que no forman parte del sistema de IA.

AI Act
Anexo IV.1 – Documentación técnica a que se refiere el artículo 11, apartado 1
(d) la descripción de todas las formas en que el sistema de IA se introduce en el mercado o se pone en servicio, como paquetes de software integrados en el hardware, descargas o API;

Por cada forma de comercialización que tenga el sistema de inteligencia artificial conviene proporcionar, al menos, la siguiente información:
✓ Indicar la modalidad de comercialización en términos de sistemas: Software instalado en los sistemas propios del responsable del despliegue (on-premise); Software en sistema instalado en modalidad Infraestructura como servicio (IaaS), Software instalado en la nube del responsable del despliegue, Software instalado en la nube del proveedor o de terceros (distribuidores, etc.), otras modalidades de tipo Software como Servicio (SaaS), o en otros formatos como edge-computing.
✓ Informar de la duración de la licencia, en caso de que esta exista y de su formato.
✓ Si el sistema de IA está integrado en un hardware, indicar como se comercializa dicho hardware.
✓ En caso de un sistema del Anexo I A, indicar los formatos de comercialización del producto que pueda ser el sistema de IA o del que pueda formar parte.
Cada una de estas categorías requiere añadir información adicional.
Para los formatos de comercialización tipo SaaS
✓ Indicar la tecnología de interoperabilidad de acceso al sistema SaaS: API, interfaz directa, interconexión con los sistemas del cliente.
✓ Los diferentes niveles comerciales de uso del sistema de IA: sus características asociadas: Peticiones máximas diarias, por segundo o cualquier formato de medida que se haya seleccionado para caracterizar y limitar el acceso.
✓ Indicar si el sistema de IA comparte hardware para varios responsables del despliegue, o se instancia de manera individual para cada responsable del despliegue en sistemas hardware específicos y aislados.
Formatos de comercialización instalables
✓ Información sobre el formato, la periodicidad y política de las actualizaciones, indicando si están incluidas en el producto o no.
29

✓ Formato de acceso al propio sistema para su instalación en los sistemas del responsable del despliegue: descarga, distribución directa etc.
✓ Si el sistema de IA cuenta con un soporte para el proceso de instalación por parte del proveedor.
✓ Si la comercialización incluye un servicio en el que el proveedor se encarga de gestionar e instalar el sistema en las instalaciones del responsable del despliegue de manera total o parcial.
Elemento de seguridad de un producto anexo I A del Reglamento Europeo de IA, o como producto anexo I A en sí mismo
✓ Información del formato de adquisición del producto.
✓ Información del servicio, si existe, de mantenimiento del producto, en particular, aplicable al sistema de IA.
✓ Al tratarse de un producto, indicar si el sistema de IA se encuentra directamente integrado en el mismo, o el producto se interopera de manera remota con el sistema de IA.

AI Act
Anexo IV.1 – Documentación técnica a que se refiere el artículo 11, apartado 1
(e) la descripción del hardware en el que está previsto que se ejecute el sistema de IA;

La descripción del soporte físico (hardware) debería contener al menos:
✓ Los requisitos y recomendaciones de recursos netos para el funcionamiento del sistema de IA en términos de capacidad de computación (procesadores y/o máquinas y características) y almacenamiento (memoria RAM, memoria caché, memoria secundaria y su tipo). Se recomienda establecer al menos los mínimos, y se podrán indicar los recomendados para diferentes configuraciones de uso. En su caso con la indicación del rol en la arquitectura del sistema de IA de la máquina o máquinas que van a ser utilizadas para su ejecución, así como sus características físicas y de sistemas operativos.
✓ La máquina o máquinas que van a ser utilizadas para su ejecución y las características de estas.
✓ En su caso se pueden indicar las características de la red necesaria para el funcionamiento del sistema (ancho de banda, disponibilidad, latencia etc.), tanto a nivel mínimo como recomendado.
✓ Se recomienda especificar las características de los recursos de almacenamiento secundario para la operación del sistema de IA: tamaño, velocidad, disponibilidad, tolerancia a fallos etc. En el caso de existir algún requisito de tecnología de manejo de
30

ficheros o gestión de bases de datos se puede indicar tecnología, y en su caso producto y versión.
✓ Se recomienda describir el hardware necesario recomendado para diferentes configuraciones de uso, en particular en relación con los volúmenes e intensidades esperadas de entrada de datos al sistema y con los tiempos establecidos de respuesta en su diseño, debiendo indicarse dichos tiempos.
o Si el sistema de inteligencia artificial forma parte o se encuentra embebido dentro de un hardware específico en el que es distribuido (es decir, incluido dentro de un equipamiento). Se pueden proporcionar los elementos de diseño y la descripción de los componentes utilizados. En estos casos, este tipo de nivel de detalle de descripción podrá ya estar cubierto por los requerimientos de evaluación de conformidad ya aplicables al producto, dentro de la legislación armonizada que le sea de aplicación de acuerdo con el Anexo I A.

AI Act
Anexo IV.1 – Documentación técnica a que se refiere el artículo 11, apartado 1
(f) en el caso de que el sistema de IA sea un componente de un producto, fotografías o ilustraciones de las características exteriores, el marcado y la configuración interna de dicho producto;

El apartado es claramente prescriptivo en lo requerido. En estas fotografías o imágenes
(diseños del producto) deben de quedar referido que:
✓ Para las características externas las imágenes deben mostrar todo el producto.
✓ La ubicación del marcado se deberá resaltar claramente.
✓ En la disposición interna se indicará aquellas partes o componentes que corresponden al sistema de inteligencia artificial, para distinguirlo de otros elementos accesorios al sistema.

AI Act
Anexo IV.1 – Documentación técnica a que se refiere el artículo 11, apartado 1
(g) una descripción básica de la interfaz de usuario facilitada al responsable del despliegue;
(h) instrucciones de uso para el responsable del despliegue y una descripción básica de la interfaz de usuario facilitada al responsable del despliegue, cuando proceda.

31
