---
name: aesia-08-guia-transparencia-09-medidas-aplicables-para-conseguir-transp
description: "AESIA: aesia 08 guia transparencia, sección «Medidas aplicables para conseguir Transparencia (parte 3)» (págs. 45-47). Documento de 2026-07-17, idioma es."
metadata:
  type: reference
  documento: aesia-08-guia-transparencia
  emisor: AESIA
  fecha: 2026-07-17
  idioma: es
  seccion: "Medidas aplicables para conseguir Transparencia (parte 3)"
  paginas: 45-47
  origen: 2026-07-17-aesia-08-guia-transparencia.pdf
  oficial: false
---
# Medidas aplicables para conseguir Transparencia (parte 3)

5.11.

Utilizar contrafactualidad

En el proceso de transparencia puede resultar útil utilizar comparaciones. Es decir, a parte de detallar el porqué de una acción (predicción o decisión), añadir también el porqué, dicha acción fue una en vez de otra (concepto de contrafactualidad). O también en qué circunstancias dicha acción podría haber sido otra si se modificaran algunas de las informaciones tenidas en cuenta. Esto es especialmente relevante para las personas objeto de las decisiones del sistema de IA, que tienen el derecho de saber en base a qué criterios e información se ha hecho una determinada predicción o tomado una decisión, y en qué circunstancias particulares dicha acción sería otra.

A quién aplica
-

-

El responsable del despliegue, como conocedor de la información gestionada por el sistema de IA, podrá identificar las contrafactualidades necesarias para el caso de uso que soporte dicho sistema y tenerlas en cuenta en la definición funcional del sistema de IA.
El proveedor podrá diseñar e implementar el sistema de IA aportando herramientas que faciliten la implementación de esta medida.

Ejemplo – Concesión de ayudas
Como resultado de esta medida, la familia solicitante podrá conocer a través del canal web los motivos por los cuales no les ha sido concedida la ayuda, y en qué condiciones particulares a su caso si les fuera concedida (por ejemplo, si incluyen los datos de una persona dependiente que el sistema ha detectado en la familia, pero que no fue aportada en la solicitud).

A qué apartados aplica esta medida
-
-
-
-

5.12.

Apartado 1. Diseño y desarrollo
Apartado 3b.vii. Información de salida
Apartado 3d. Vigilancia humana
Apartado 3b.v. Impacto en personas

Habilitar un canal con la información de uso del sistema

Adicionalmente a las medidas a tener en cuenta en el diseño y desarrollo del sistema para que él mismo pueda proporcionar información acerca de su funcionamiento de manera transparente, puede resultar conveniente habilitar un medio externo al propio sistema
(web/wiki/doc page) que recopile la información de dicho sistema que está orientada a facilitar la transparencia sobre el funcionamiento del mismo.
Atendiendo a la información específica reflejada en el apartado tercero de este artículo, la estructura de dicho canal podría ser la siguiente:
44

-
-
-
-
-

Información de contacto del proveedor.
Descripción de la finalidad del sistema.
Casos de uso para los que está destinada.
Casos de uso potenciales no recomendados, y el riesgo asociado en caso de ser utilizado para dichos fines.
Información de su funcionamiento:
o
Rendimiento y precisión del sistema.
o
Sesgos potenciales.
o
Posibles ataques.
o
Descripción de los datos utilizados.
o
Archivos de registro, para poder analizar las acciones realizadas.
o
Ciclo de vida del sistema y procedimientos de actualización, incluyendo
Change log de versiones

A quién aplica
-
-

Al proveedor, como creador del sistema.
Al responsable del despliegue, ya que será quien consuma la información proporcionada por el proveedor y podrá desplegarla en su organización entre las personas que tengan algún nivel de responsabilidad sobre el sistema.

Ejemplo – Concesión de ayudas y Bomba de insulina
El contenido de dicho canal (web/wiki/doc page) puede ser equivalente a la desarrollada en cada uno de los ejemplos de las medidas del presente documento.

A qué apartados aplica esta medida
-

Apartado 2. Instrucciones de uso

5.13.

Resumen ejecutivo. Relación Apartado-medidas aplicables

Apartados
1. Diseño y desarrollo
2. Instrucciones de uso
3. Información específica
3a. Contacto
3b. Características, capacidades y limitaciones
3b.i. Finalidad
3b.ii. Nivel de precisión
3b.iii. Riesgos por usos no previstos
3b.iv. Explicación de sus resultados de salida
3b.v. Impacto en personas y colectivos
3b.vi. Datos de entrada
3b.vii. Información de salida
3c. Cambios
3d. Vigilancia humana
3e. Recursos HW/SW y mantenimiento
3f. Archivos de registro

Medidas
MT1 MT2 MT3 MT4 MT5 MT6 MT7 MT8 MT9 MT10 MT11 MT12 MT13 MT14 MT15 MT16
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

45

MT1 Proporcionar contacto con el proveedor
MT2 Atender al dominio de negocio
MT3 Asegurar el objetivo funcional del sistema
MT4 Transparencia sobre los datos utilizados
MT5 Detallar de lo más global a lo más particular
MT6 Adaptar el lenguaje
MT7 Gestionar la complejidad
MT8 Utilizar métricas integradas en el ciclo de vida del sistema
MT9 Aplicar prudencia
MT10 Usar causalidad, minimizar correlaciones
MT11 Utilizar contrafactualidad
MT12 Habilitar un canal con la información de uso del sistema
MT13 Artículo 09. Sistema de gestión de riesgos
MT14 Artículo 14. Supervisión humana
MT15 Artículo 15. Precisión, solidez y ciberseguridad

46
