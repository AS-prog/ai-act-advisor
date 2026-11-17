# Reglamento europeo de Inteligencia Artificial (AI Act): investigación sobre fuentes primarias para un plugin de detección de riesgos

- **Fecha de la investigación:** 17 de noviembre de 2026
- **Texto de referencia:** Reglamento (UE) 2024/1689 (RIA / AI Act), **versión consolidada a 27-07-2026**, que ya incorpora el Reglamento (UE) 2026/1744 ("Digital Omnibus on AI").
- **Alcance:** criterios comprobables por un ingeniero o por una herramienta. Esto no es asesoramiento jurídico.

> **Nota de método (importante).** El proxy de este entorno bloqueó la descarga directa (curl) de `eur-lex.europa.eu`, `aesia.digital.gob.es`, `boe.es` y `europa.eu`. El contenido se leyó con una herramienta de lectura web que **devuelve resúmenes y citas literales de 125 caracteres como máximo**, no el texto íntegro. Además, las páginas de EUR-Lex se cortaron por tamaño. Por eso:
> 1. Para el texto consolidado se usó sobre todo el **AI Act Explorer del AI Act Service Desk** de la Comisión Europea (`ai-act-service-desk.ec.europa.eu`). Es una fuente oficial de la Comisión que reproduce el consolidado de EUR-Lex "as at 27 July 2026" y marca con **NEW / AMENDED / DELETED** lo que cambió el Omnibus. Sus resúmenes no son jurídicamente vinculantes; aquí se citan los artículos, no esos resúmenes.
> 2. Para el Reglamento 2026/1744 se leyó en EUR-Lex (ES, HTML y PDF) hasta su art. 1 punto 10. Para el resto se usó el **texto final del Consejo y del Parlamento PE-CONS 30/1/26 REV 1**, leído hasta el art. 1 punto 32 (art. 75 bis). Lo que no se pudo leer en ninguno de los dos se contrastó solo con el Service Desk y se indica.
> 3. Las citas entre comillas en inglés son literales del texto inglés. Las traducciones al español son mías salvo que se indique lo contrario. Para un uso jurídico, contrástese con la versión española de EUR-Lex.

---

## Índice

1. [Resumen ejecutivo](#1-resumen-ejecutivo)
2. [Qué es el Reglamento (UE) 2026/1744 (Digital Omnibus on AI)](#2-qué-es-el-reglamento-ue-20261744-digital-omnibus-on-ai)
3. [Calendario de aplicación (art. 113) tras el Omnibus](#3-calendario-de-aplicación-art-113-tras-el-omnibus)
4. [Ámbito de aplicación (art. 2) y definiciones clave (art. 3)](#4-ámbito-de-aplicación-art-2-y-definiciones-clave-art-3)
5. [Categorías de riesgo y árbol de clasificación](#5-categorías-de-riesgo-y-árbol-de-clasificación)
6. [Prácticas prohibidas (art. 5)](#6-prácticas-prohibidas-art-5)
7. [Sistemas de alto riesgo: clasificación (art. 6, anexos I y III)](#7-sistemas-de-alto-riesgo-clasificación-art-6-anexos-i-y-iii)
8. [Obligaciones de alto riesgo (arts. 8-27, 43-49, 72-73)](#8-obligaciones-de-alto-riesgo)
9. [Transparencia (art. 50)](#9-transparencia-art-50)
10. [Modelos de IA de uso general (GPAI) (arts. 51-56, anexos XI-XIII)](#10-modelos-de-ia-de-uso-general-gpai)
11. [Alfabetización en IA (art. 4) y datos sensibles para sesgos (art. 4 bis)](#11-alfabetización-en-ia-art-4-y-datos-sensibles-para-sesgos-art-4-bis)
12. [Sandboxes y pruebas en condiciones reales (arts. 57-63)](#12-sandboxes-y-pruebas-en-condiciones-reales-arts-57-63)
13. [Supervisión y sanciones (arts. 75, 75 bis, 99-101)](#13-supervisión-y-sanciones)
14. [Cambios del Reglamento 2026/1744, artículo por artículo](#14-cambios-del-reglamento-20261744-artículo-por-artículo)
15. [AESIA: qué publica y cómo aprovecharlo](#15-aesia-qué-publica-y-cómo-aprovecharlo)
16. [Directrices y códigos oficiales de la Comisión](#16-directrices-y-códigos-oficiales-de-la-comisión)
17. [Herramientas y recursos existentes (lista awesome-eu-ai-act)](#17-herramientas-y-recursos-existentes-lista-awesome-eu-ai-act)
18. [Implicaciones para el plugin (INFERENCIA, no texto legal)](#18-implicaciones-para-el-plugin-inferencia-no-texto-legal)
19. [Fuentes consultadas](#19-fuentes-consultadas)
20. [Pendiente / no verificado](#20-pendiente--no-verificado)

**Abreviaturas de cita.** "art. X" se refiere al RIA consolidado y se ha leído en `https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-X` (los anexos, en `.../annex-N`). "Omnibus art. 1.N" es el punto N del art. 1 del Reglamento (UE) 2026/1744. "Cdo." es un considerando.

---

## 1. Resumen ejecutivo

- El **Reglamento (UE) 2026/1744**, de 8 de julio de 2026 ("Digital Omnibus on AI"), se publicó en el DOUE L el 24-07-2026 y **entró en vigor el 27-07-2026**: al tercer día de su publicación (Cdo. 46). Modifica el RIA y también los Reglamentos (UE) 2018/1139 (aviación) y 2023/1230 (máquinas).
- **Aplazamiento del alto riesgo:** los requisitos y obligaciones de los arts. 6-27 (capítulo III, secciones 1-3) se aplican a partir del **2-12-2027** para el anexo III (antes, 2-08-2026) y del **2-08-2028** para el anexo I, art. 6.1 (antes, 2-08-2027) (art. 113.c.i y c.ii).
- **Nuevas prohibiciones:** se prohíben los sistemas que generan *deepfakes* sexuales o íntimos no consentidos de personas identificables (art. 5.1.b bis) y material de abuso sexual infantil (art. 5.1.b ter). Se aplican a partir del **2-12-2026** (art. 113.a). Hoy todavía no se aplican; faltan 15 días.
- **Transparencia (art. 50)**: se aplica **desde el 2-08-2026**. Para los sistemas generativos ya comercializados antes de esa fecha, el marcado legible por máquina (art. 50.2) es exigible a partir del **2-12-2026** (art. 111.4, NEW).
- **Alfabetización en IA (art. 4)**: deja de ser una obligación de "garantizar" un nivel suficiente y pasa a ser una obligación de "tomar medidas para apoyar el desarrollo" de la alfabetización, sin exigir un nivel concreto (art. 4.1 AMENDED; Cdo. 8 del Omnibus).
- **Nuevo art. 4 bis**: base jurídica para tratar **categorías especiales de datos personales** con el fin de detectar y corregir sesgos, con 6 condiciones acumulativas. Se aplica a proveedores de alto riesgo y también a otros sistemas y modelos.
- **Pymes y small mid-caps (SMC)**: se definen las SMC (art. 3.14 ter). Las SMC obtienen la documentación técnica simplificada (art. 11.1), la proporcionalidad en el SGC (art. 17.2), el acceso prioritario al sandbox de la UE (art. 57.3 bis) y el tope de multa "el menor de" para las multas de los apartados 4 y 5 del art. 99 (art. 99.6 bis).
- **Registro**: los sistemas que el proveedor declara no de alto riesgo por el art. 6.3 **siguen debiendo registrarse** (art. 49.2), pero con un contenido reducido (anexo VIII, sección B: se suprimen los puntos 7 y 9).
- **Supervisión centralizada en la Oficina de IA**: tiene **competencia exclusiva** sobre los sistemas basados en un modelo GPAI del mismo proveedor y sobre los sistemas integrados en VLOP o VLOSE (art. 75.1), con poderes de autoridad de vigilancia del mercado (art. 75 bis, NEW).
- **GPAI**: las obligaciones se aplican desde el 2-08-2025. Los poderes sancionadores de la Comisión rigen desde el 2-08-2026 (art. 113; art. 101). Los modelos anteriores al 2-08-2025 deben cumplir antes del 2-08-2027 (art. 111.3). El umbral de riesgo sistémico sigue siendo **10^25 FLOP** (art. 51.2).
- **Multas**: hasta 35 M EUR o el 7 % del volumen de negocios por prácticas prohibidas; 15 M EUR o el 3 % por otras obligaciones, incluido el art. 50; 7,5 M EUR o el 1 % por información incorrecta (art. 99.3-5).
- **AESIA** publica 16 guías prácticas y un **compendio de checklists en Excel** (ZIP). Proceden del sandbox piloto español, tienen licencia CC BY 4.0 y AESIA anuncia que se actualizarán por el Omnibus. Son reutilizables como base del plugin (sección 15).

---

## 2. Qué es el Reglamento (UE) 2026/1744 (Digital Omnibus on AI)

| Dato | Valor | Fuente |
|---|---|---|
| Título | Reglamento (UE) 2026/1744 del Parlamento Europeo y del Consejo, de 8 de julio de 2026, por el que se modifican los Reglamentos (UE) 2024/1689, (UE) 2018/1139 y (UE) 2023/1230 en lo que respecta a la simplificación de la aplicación de normas armonizadas sobre inteligencia artificial ("Ómnibus Digital sobre IA") | EUR-Lex ES HTML CELEX 32026R1744 |
| Publicación | DO L, 2026/1744, 24-07-2026 | ídem |
| Entrada en vigor | Al tercer día de su publicación (Cdo. 46), es decir, el **27-07-2026**. Esa es también la fecha del consolidado (`/2026-07-27/`) | ídem; consolidado ELI |
| Procedimiento | 2025/0359(COD). Propuesta COM(2025) 836 | Ficha OEIL; texto PE-CONS 30/1/26 REV 1 |
| Dictamen | Dictamen conjunto SEPD-CEPD de 20-01-2026 (Cdo. 47) | EUR-Lex ES HTML |
| ELI | https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng | ídem |

Objetivos declarados por la Comisión (FAQ del Service Desk, categoría "Digital Omnibus"):

- vincular la aplicación del alto riesgo a la disponibilidad de normas armonizadas y herramientas;
- simplificar para pymes y SMC;
- reformular la alfabetización en IA;
- suprimir la plantilla armonizada del plan de vigilancia poscomercialización;
- reducir el registro de los sistemas en áreas de alto riesgo que no son de alto riesgo;
- centralizar en la Oficina de IA los sistemas basados en GPAI y los sistemas en VLOP y VLOSE;
- permitir el tratamiento de datos para sesgos;
- ampliar los sandboxes;
- aclarar la relación con otra legislación.

La FAQ estima que la extensión a SMC beneficia a "an additional 8,250 companies".

> **Ojo:** la FAQ del Service Desk describe en parte la **propuesta**: aplicación del alto riesgo "condicionada a la disponibilidad de estándares" con un máximo de 16 y 12 meses, y un periodo transitorio de "6 months" para el art. 50.2. El **texto final** del art. 113 fija **fechas fijas** (2-12-2027 y 2-08-2028), y el art. 111.4 fija el **2-12-2026** para el art. 50.2. En el plugin hay que usar las fechas del articulado.

---

## 3. Calendario de aplicación (art. 113) tras el Omnibus

### 3.1 Fechas antes y después

| Bloque | Fecha original (Reglamento 2024/1689) | Fecha vigente (tras 2026/1744) | Cita |
|---|---|---|---|
| Entrada en vigor del RIA | 1-08-2024 | sin cambio | art. 113, párr. 1; cronograma del Service Desk |
| Capítulos I y II (definiciones, alfabetización, prohibiciones a-h) | 2-02-2025 | sin cambio | art. 113.a |
| **Nuevas prohibiciones art. 5.1.b bis y b ter, y art. 5.1 bis y 1 ter** | no existían | **2-12-2026** | art. 113.a (AMENDED) |
| Cap. III secc. 4 (notificación y organismos notificados), cap. V (GPAI), cap. VII (gobernanza), cap. XII (sanciones, salvo art. 101) y art. 78 | 2-08-2025 | sin cambio | art. 113.b |
| Fecha general de aplicación, incluido el **art. 50** y el art. 101 (multas a GPAI) | 2-08-2026 | sin cambio | art. 113, párr. 2 |
| Arts. 102-110 (modificaciones de otros actos) | 2-08-2026 (según la regla general) | **27-07-2026** | art. 113.d (NEW) |
| Art. 50.2 para sistemas generativos comercializados antes del 2-08-2026 | 2-08-2026 | **2-12-2026** | art. 111.4 (NEW) |
| **Alto riesgo, anexo III (art. 6.2)**: cap. III secc. 1-3, salvo el art. 6.5 | **2-08-2026** | **2-12-2027** (+16 meses) | art. 113.c.i (AMENDED); FAQ: "maximum 16 months later than originally envisaged" |
| **Alto riesgo, anexo I (art. 6.1)** | **2-08-2027** | **2-08-2028** (+12 meses) | art. 113.c.ii (AMENDED); FAQ ("maximum delay of 12 months") |
| Sandbox nacional operativo (al menos 1 por Estado miembro) | 2-08-2026 | **2-08-2027** | art. 57.1 (AMENDED) |
| GPAI comercializados antes del 2-08-2025 | 2-08-2027 | sin cambio | art. 111.3 |
| Actos delegados sobre la limitación de requisitos para el anexo I, sección A | — | antes del 2-08-2027 | art. 2.13 (NEW) |
| Directrices sobre los arts. 8.2, 9.10 y 17.3 (anexo I, sección A) | — | antes del 1-08-2027 | art. 96.1.g (NEW) |
| Directrices y plantilla del plan de vigilancia poscomercialización | antes del 2-02-2026, como acto de ejecución | **antes del 2-09-2027**, como "guidance" | art. 72.3 (AMENDED) |
| Solicitud de designación de los organismos notificados del anexo I, sección A | — | antes del 28-01-2028 | art. 43.3 (AMENDED) |
| Sistemas de alto riesgo destinados a autoridades públicas ya comercializados | 2-08-2030 | 2-08-2030 | art. 111.2 |
| Componentes de sistemas TI de gran magnitud (anexo X) | 31-12-2030 | 31-12-2030 | art. 111.1 |

*Las fechas originales del alto riesgo (2-08-2026 y 2-08-2027) se infieren de la FAQ del Service Desk ("Other parts of the Act are set to apply on 2 August 2026 and 2 August 2027") y de los retrasos máximos de 16 y 12 meses que indica. Coinciden con el art. 113 original del DO L 12-07-2024, pero el texto original **no se pudo leer** en esta sesión (sección 20).*

### 3.2 Qué se aplica hoy (17-11-2026)

**En vigor y aplicable:**

- **Definiciones (art. 3) y alfabetización en IA** (art. 4, en su redacción nueva desde el 27-07-2026).
- **Prohibiciones del art. 5.1.a-h**, desde el 2-02-2025.
- **Obligaciones de los proveedores de GPAI** (arts. 53-55), desde el 2-08-2025. La Comisión puede multar desde el 2-08-2026 (art. 101; página "Guidelines for GPAI providers": "from 2 August 2026 onwards").
- **Transparencia del art. 50**, desde el 2-08-2026. La excepción es el art. 50.2 para sistemas ya comercializados antes de esa fecha, exigible a partir del 2-12-2026.
- Gobernanza, sanciones, sandboxes y las facultades de la Oficina de IA de los arts. 75 y 75 bis (aplicación general desde el 2-08-2026; el Omnibus entró en vigor el 27-07-2026).
- **Art. 4 bis** (datos sensibles para sesgos). Considerando 9 del Omnibus: "debe aplicarse desde la fecha en que empiece a aplicarse dicho Reglamento".

**Todavía no aplicable:**

- Las prohibiciones del art. 5.1.b bis y b ter, a partir del 2-12-2026.
- **Todos los requisitos de alto riesgo** de los arts. 6-27: a partir del 2-12-2027 (anexo III) y del 2-08-2028 (anexo I). Incluye la clasificación del art. 6 (sección 1 del capítulo III), la FRIA (art. 27) y las obligaciones de los responsables del despliegue (art. 26).

> Inferencia: el registro (art. 49, cap. III secc. 5) se aplica formalmente desde el 2-08-2026, pero solo tiene objeto cuando se aplica la clasificación de alto riesgo del art. 6. **No verificado** si la Comisión lo interpreta así.

---

## 4. Ámbito de aplicación (art. 2) y definiciones clave (art. 3)

### 4.1 Quién está sujeto (art. 2.1)

| Sujeto | Condición | Cita |
|---|---|---|
| Proveedores | Introducen en el mercado o ponen en servicio sistemas de IA en la UE, o introducen modelos GPAI en el mercado, **aunque estén establecidos fuera de la UE** | art. 2.1.a |
| Responsables del despliegue | Establecidos o ubicados en la UE | art. 2.1.b |
| Proveedores y responsables del despliegue de terceros países | Cuando **la salida del sistema se utiliza en la UE** | art. 2.1.c |
| Importadores y distribuidores | — | art. 2.1.d |
| Fabricantes de productos | Introducen el sistema junto con su producto y con su nombre o marca | art. 2.1.e |
| Representantes autorizados | De proveedores no establecidos en la UE | art. 2.1.f |
| Personas afectadas | Ubicadas en la UE | art. 2.1.g |

### 4.2 Exclusiones (art. 2)

| Exclusión | Límites | Cita |
|---|---|---|
| Uso **exclusivamente** militar, de defensa o de seguridad nacional | Con independencia del tipo de entidad | art. 2.3 |
| Autoridades de terceros países y organizaciones internacionales en cooperación policial o judicial | Solo con garantías adecuadas de derechos fundamentales | art. 2.4 |
| Sistemas o modelos desarrollados y puestos en servicio **con el único fin** de la investigación y el desarrollo científicos | "sole purpose" | art. 2.6 |
| Investigación, pruebas y desarrollo **antes** de la comercialización | **No** cubre las pruebas en condiciones reales | art. 2.8 |
| Personas físicas en actividad **puramente personal no profesional** | — | art. 2.10 |
| Licencias **libres y de código abierto** | **No** se aplica si el sistema es de alto riesgo, del art. 5 o del art. 50 | art. 2.12 |
| Productos del anexo I, sección B (vehículos, aviación, ferrocarril, etc.) | Solo se aplican el art. 6.1, el art. 60 bis y los arts. 102-112. Los arts. 57-59 solo se aplican si los requisitos se integran en la legislación sectorial | art. 2.2 (AMENDED) |
| Limitación de requisitos (arts. 9-15 y 17-25) para el anexo I, sección A | Si la legislación sectorial ofrece una protección equivalente o superior; mediante actos delegados antes del 2-08-2027 | art. 2.13 (NEW) |
| Protección de datos | El RGPD y demás normas se aplican sin perjuicio de los arts. 4 bis y 59 | art. 2.7 (AMENDED) |

### 4.3 Definiciones clave (art. 3)

| Término | Contenido clave | Cita |
|---|---|---|
| **Sistema de IA** | Sistema basado en máquinas, diseñado para funcionar con distintos niveles de autonomía, que puede mostrar adaptabilidad tras el despliegue y que, con objetivos explícitos o implícitos, **infiere** de la información de entrada cómo generar salidas (predicciones, contenidos, recomendaciones o decisiones) que pueden influir en entornos físicos o virtuales | art. 3.1 |
| Proveedor | Desarrolla un sistema o modelo GPAI, o lo encarga, y lo introduce en el mercado o lo pone en servicio **con su nombre o marca**, de forma onerosa o gratuita | art. 3.3 |
| Responsable del despliegue | Usa un sistema bajo su autoridad, salvo en una actividad personal no profesional | art. 3.4 |
| Importador | Establecido en la UE; comercializa un sistema con el nombre o la marca de una entidad de un tercer país | art. 3.6 |
| Distribuidor | Cualquier otro agente de la cadena que comercializa el sistema en la UE | art. 3.7 |
| Operador | Proveedor, fabricante del producto, responsable del despliegue, representante autorizado, importador o distribuidor | art. 3.8 |
| Finalidad prevista | El uso previsto por el proveedor, según las instrucciones de uso, el material promocional y la documentación técnica | art. 3.12 |
| Uso indebido razonablemente previsible | Uso no conforme con la finalidad que puede derivarse de un comportamiento humano previsible | art. 3.13 |
| **Componente de seguridad** (AMENDED) | Componente que cumple una **función de seguridad** o cuyo fallo pone en peligro la salud y la seguridad de personas o bienes. Cumple una función de seguridad si su finalidad es prevenir o mitigar esos riesgos | art. 3.14 |
| **Pyme** (NEW) | Según la Recomendación 2003/361/CE | art. 3.14 bis |
| **SMC** (NEW) | Pequeña empresa de mediana capitalización, según el punto 2 del anexo de la Recomendación (UE) 2025/1099 | art. 3.14 ter |
| Modificación sustancial | Cambio no previsto en la evaluación de conformidad inicial que afecta al cumplimiento de la secc. 2 o modifica la finalidad | art. 3.23 |
| Sistema de reconocimiento de emociones | Identifica o infiere emociones o intenciones **a partir de datos biométricos** | art. 3.39 |
| Categorización biométrica | Asigna a personas a categorías según sus datos biométricos, salvo que sea accesoria a otro servicio comercial y estrictamente necesaria | art. 3.40 |
| Identificación biométrica remota | Sin participación activa de la persona, normalmente a distancia, por comparación con una base de datos | art. 3.41; "en tiempo real": 3.42 |
| Incidente grave | Muerte o daño grave a la salud; alteración grave e irreversible de infraestructura crítica; infracción del Derecho de la UE sobre derechos fundamentales; daño grave a bienes o al medio ambiente | art. 3.49 (a-d) |
| **Ultrafalsificación (deepfake)** | Contenido de imagen, audio o vídeo generado o manipulado que se asemeja a personas, objetos, lugares, entidades o sucesos existentes y que parecería auténtico | art. 3.60 |
| **Modelo GPAI** | Modelo, también el entrenado con grandes volúmenes de datos mediante autosupervisión, que muestra una generalidad significativa y puede realizar con competencia una gran variedad de tareas. Excluye los modelos usados solo para I+D o prototipos antes de comercializarse | art. 3.63 |
| Capacidades de gran impacto | Igualan o superan las de los modelos más avanzados | art. 3.64 |
| Riesgo sistémico | Riesgo específico de las capacidades de gran impacto, con repercusión significativa por su alcance o sus efectos negativos, que puede propagarse a escala | art. 3.65 |
| Sistema GPAI | Sistema basado en un modelo GPAI que puede servir para diversos fines | art. 3.66 |

**Directrices de la Comisión sobre la definición de sistema de IA** (publicadas el 6-02-2025 y adoptadas el 29-07-2025 como C(2025) 5053 final; no vinculantes). Desglosan el art. 3.1 en **7 elementos**: basado en máquinas, autonomía, adaptabilidad (opcional), objetivos, **inferencia** (el criterio que separa la IA del software tradicional), salidas e influencia en el entorno (párr. 9-60). **Quedan fuera** (párr. 41-51):

- la **optimización matemática** que solo acelera o aproxima métodos clásicos (párr. 42-44);
- el **procesamiento básico de datos**: consultas a bases de datos, cuadros de mando sin recomendación (párr. 46-47);
- las **heurísticas clásicas**: minimax en ajedrez (párr. 48);
- los **sistemas de predicción simple**, cuyo rendimiento se consigue con una regla estadística básica (párr. 49-51).

### 4.4 Cuándo otro operador se convierte en proveedor (art. 25)

Un distribuidor, importador, responsable del despliegue u otro tercero pasa a ser proveedor (art. 25.1) si:

- pone su nombre o marca en un sistema de alto riesgo;
- lo modifica sustancialmente; o
- cambia la finalidad de un sistema, incluido un sistema GPAI, de modo que pase a ser de alto riesgo (art. 25.1.c).

El proveedor inicial debe cooperar con el nuevo: documentación técnica, limitaciones y modos de fallo conocidos, y acceso técnico para pruebas. No tiene que hacerlo si especificó claramente que su sistema no debía convertirse en uno de alto riesgo (art. 25.2, AMENDED).

Los proveedores de alto riesgo y quienes les suministran modelos, herramientas o componentes deben firmar un **acuerdo escrito** (art. 25.4, AMENDED). Quedan exentos los componentes libres y de código abierto, **salvo los modelos GPAI**.

---

## 5. Categorías de riesgo y árbol de clasificación

1. **¿Es un sistema de IA (art. 3.1)?** Si no infiere, sino que aplica reglas definidas por humanos, procesamiento básico o predicción simple, queda fuera (directrices de definición).
2. **¿Se aplica alguna exclusión del art. 2?** Por ejemplo: militar, solo I+D, uso personal u open source no prohibido, no de alto riesgo y no del art. 50.
3. **¿Es una práctica prohibida (art. 5)?** Si lo es, no puede usarse ni comercializarse.
4. **¿Es de alto riesgo?**
   - a) Por el **art. 6.1**: es un componente de seguridad de un producto del anexo I, o el propio producto, y ese producto requiere una evaluación de conformidad por terceros. Los apartados 1 bis a 1 ter, nuevos, delimitan qué es un componente de seguridad.
   - b) Por el **art. 6.2**: está en un caso de uso del **anexo III**, **salvo** la excepción del art. 6.3, que no se aplica si hay **perfilado**.
5. **¿Activa obligaciones de transparencia del art. 50?** Se acumulan con el alto riesgo (art. 50.6).
6. **¿Es un modelo GPAI?** Obligaciones de los arts. 53-55, que corresponden al proveedor del modelo, no al del sistema.
7. **Riesgo mínimo**: solo el art. 4 (alfabetización), los códigos voluntarios y el art. 4 bis si se tratan datos para sesgos.

---

## 6. Prácticas prohibidas (art. 5)

Aplicables desde el 2-02-2025, salvo b bis y b ter, que se aplican a partir del 2-12-2026 (art. 113.a). Multa: hasta 35 M EUR o el 7 % (art. 99.3).

| Letra | Práctica prohibida | Condiciones y excepciones | Cita |
|---|---|---|---|
| **a** | Técnicas **subliminales**, deliberadamente **manipuladoras** o **engañosas** | Que alteren de forma sustancial el comportamiento, mermando apreciablemente la toma de decisiones informada, y causen o puedan causar un perjuicio considerable | art. 5.1.a |
| **b** | **Explotación de vulnerabilidades** por edad, discapacidad o situación social o económica específica | Misma prueba de alteración sustancial y perjuicio considerable | art. 5.1.b |
| **b bis** (NEW) | Generar o manipular imágenes, vídeos o audios realistas de las **partes íntimas o de actividad sexual explícita** de una persona identificable | Sin "freely-given, specific, informed, unambiguous and explicit consent". Según el apdo. 1 bis, **en la comercialización** solo se prohíbe si esa es la **finalidad prevista** o si el diseño hace ese resultado "reasonably foreseeable and reproducible" **y** faltan "reasonable and adequate technical safety measures". **En el uso**, solo si el responsable del despliegue lo usa para ese fin. Según el apdo. 1 ter, no es manipulación la que no aumenta la exposición de las partes íntimas ni cambia la naturaleza de la actividad | art. 5.1.b bis, 5.1 bis, 5.1 ter; Cdos. 10-16 del Omnibus |
| **b ter** (NEW) | Generar o manipular **material de abuso sexual infantil**, en el sentido del art. 2.c y e de la Directiva 2011/93/UE | Salvo "where a 'without right' defence applies under national law". Mismo régimen del apdo. 1 bis | art. 5.1.b ter, 5.1 bis |
| **c** | **Puntuación social**: evaluar o clasificar a personas a lo largo del tiempo por su comportamiento social o sus características personales | Si conduce a un trato perjudicial en contextos no relacionados con el contexto original de los datos, o a un trato injustificado o desproporcionado | art. 5.1.c |
| **d** | Predecir el riesgo de que una persona cometa un delito **basándose únicamente** en perfilado o rasgos de personalidad | No se prohíbe el apoyo a una valoración humana basada en hechos objetivos y verificables vinculados a una actividad delictiva | art. 5.1.d |
| **e** | Crear o ampliar bases de datos de **reconocimiento facial** mediante la **extracción no selectiva** (*scraping*) de imágenes faciales de internet o de CCTV | — | art. 5.1.e |
| **f** | **Inferir emociones** en el **lugar de trabajo** y en **centros educativos** | Salvo por motivos **médicos o de seguridad** | art. 5.1.f |
| **g** | **Categorización biométrica** para deducir raza, opiniones políticas, afiliación sindical, convicciones religiosas o filosóficas, vida sexual u orientación sexual | Salvo el etiquetado o filtrado de conjuntos de datos biométricos lícitos y la categorización en el ámbito policial | art. 5.1.g |
| **h** | **Identificación biométrica remota "en tiempo real"** en espacios de acceso público **con fines policiales** | Salvo cuando sea estrictamente necesaria para: (i) buscar víctimas o personas desaparecidas; (ii) prevenir una amenaza concreta, sustancial e inminente o terrorista; (iii) localizar sospechosos de delitos del anexo II castigados con un máximo de al menos 4 años. Requiere FRIA (art. 27), registro (art. 49), autorización judicial o administrativa previa (urgencia: solicitud en 24 h), notificación a la autoridad de vigilancia del mercado y a la de protección de datos, y ley nacional habilitante | art. 5.1.h, 5.2-5.7 |

**Ejemplos de las directrices de la Comisión sobre prácticas prohibidas** (publicadas el 4-02-2025 y adoptadas el 29-07-2025 como C(2025) 5052 final; no vinculantes; lectura parcial):

- Para la letra **a**: mensajes subliminales o estímulos enmascarados (párr. 65), manipulación sensorial (párr. 68), persuasión personalizada sobre vulnerabilidades (párr. 68) y un chatbot que suplanta a un familiar para estafar (párr. 73).
- Las alucinaciones de la IA generativa no entran, si se informa a los usuarios y hay salvaguardias (párr. 73).
- El scoring crediticio y de seguros **no** es puntuación social *per se*: es alto riesgo (párr. 37).
- El reconocimiento de emociones fuera del trabajo y de la educación es alto riesgo, no práctica prohibida (párr. 37).
- Los proveedores de sistemas de propósito general deberían excluir en sus términos el uso prohibido en el trabajo (párr. 41).

---

## 7. Sistemas de alto riesgo: clasificación (art. 6, anexos I y III)

### 7.1 Art. 6.1: productos del anexo I

Es de alto riesgo si se cumplen **dos** condiciones (art. 6.1.a-b):

- **a)** es componente de seguridad de un producto del anexo I, o es el propio producto; y
- **b)** el producto requiere una evaluación de conformidad **por terceros**.

Novedades del Omnibus (Omnibus art. 1.8):

- **6.1 bis (NEW):** **no** son componentes de seguridad los sistemas usados **solo** para asistencia al usuario, optimización del rendimiento, eficiencia del servicio, automatización, comodidad o control de calidad.
- **6.1 ter (NEW):** a pesar de lo anterior, **sí** lo son si su fallo o mal funcionamiento pondría en peligro la salud y la seguridad.
- **6.1 quater (NEW):** si el producto requiere evaluación por terceros **solo** por riesgos ajenos a la salud y la seguridad (por ejemplo, el espectro radioeléctrico o las interferencias electromagnéticas), no se cumple la condición b).

**Anexo I (consolidado):**

- **Sección A** (marco legislativo nuevo): juguetes (2009/48/CE), embarcaciones de recreo (2013/53/UE), ascensores (2014/33/UE), ATEX (2014/34/UE), equipos radioeléctricos (2014/53/UE), equipos a presión (2014/68/UE), teleféricos (2016/424), EPI (2016/425), aparatos de gas (2016/426), **productos sanitarios (2017/745)** y **PSDIV (2017/746)**.
- **El punto 1 (máquinas, antes Directiva 2006/42/CE) aparece como DELETED en la sección A.**
- **Sección B**: seguridad de la aviación civil (300/2008), vehículos de dos o tres ruedas (168/2013), vehículos agrícolas (167/2013), equipos marinos (2014/90/UE), ferrocarril (2016/797), vehículos de motor (2018/858 y 2019/2144), aviación civil y drones (2018/1139) y **máquinas, Reglamento (UE) 2023/1230 (NEW, punto 21)**.

> **Consecuencia (inferencia a confirmar):** las máquinas pasan a la sección B. Según el art. 2.2, a la sección B solo se le aplican el art. 6.1, el art. 60 bis y los arts. 102-112. Los requisitos de IA de las máquinas se canalizarían a través del Reglamento de máquinas, que el Omnibus también modifica. **Verifíquese en el texto** de los arts. 2 y 3 del Reglamento 2026/1744, que no se pudieron leer (sección 20).

### 7.2 Art. 6.2: anexo III (todas las áreas)

| Área | Casos de alto riesgo | Exclusiones expresas | Cita |
|---|---|---|---|
| **1. Biometría** (si lo permite el Derecho) | a) identificación biométrica remota; b) categorización biométrica por atributos sensibles o protegidos; c) reconocimiento de emociones | La **verificación** biométrica cuyo único fin es confirmar la identidad (desbloqueo, acceso 1:1) | anexo III.1 |
| **2. Infraestructuras críticas** | Componentes de seguridad en la gestión y el funcionamiento de infraestructura digital crítica, tráfico rodado y suministro de agua, gas, calefacción o electricidad | — | anexo III.2 |
| **3. Educación y formación profesional** | a) acceso, admisión o asignación a centros; b) evaluación de resultados de aprendizaje; c) evaluación del nivel educativo adecuado; d) supervisión y detección de comportamientos prohibidos en exámenes | — | anexo III.3 |
| **4. Empleo y gestión de trabajadores** | a) contratación o selección: anuncios dirigidos, filtrado de candidaturas, evaluación de candidatos; b) decisiones sobre la relación laboral: promoción, despido, asignación de tareas según rasgos o comportamiento, seguimiento del rendimiento | — | anexo III.4 |
| **5. Servicios esenciales** | a) elegibilidad, concesión, reducción o revocación de prestaciones públicas, incluida la sanidad; b) **solvencia o calificación crediticia**; c) evaluación de riesgos y **precios en seguros de vida y salud**; d) clasificación de llamadas de emergencia, despacho y triaje | En la b), la **detección de fraude financiero** | anexo III.5 |
| **6. Garantía del cumplimiento del Derecho** | a) riesgo de ser víctima; b) polígrafos; c) fiabilidad de las pruebas; d) riesgo de delinquir o reincidir (no solo por perfilado); e) perfilado en investigaciones | — | anexo III.6 |
| **7. Migración, asilo y fronteras** | a) polígrafos; b) evaluación de riesgos de personas que entran; c) examen de solicitudes de asilo, visado o residencia; d) detección, reconocimiento o identificación de personas | La verificación de documentos de viaje | anexo III.7 |
| **8. Justicia y procesos democráticos** | a) asistencia a autoridades judiciales en la interpretación de hechos y Derecho, también en resolución alternativa de litigios; b) influir en elecciones, referendos o en el comportamiento electoral | Herramientas cuya salida no se expone directamente a las personas (logística de campañas) | anexo III.8 |

### 7.3 Excepción del art. 6.3 y contraexcepción por perfilado

Un sistema del anexo III **no** es de alto riesgo si no plantea un riesgo importante de daño, incluido el de influir sustancialmente en la toma de decisiones, **y** cumple alguna de estas condiciones (art. 6.3):

- **a)** tarea procedimental limitada;
- **b)** mejora del resultado de una actividad humana ya realizada;
- **c)** detección de patrones de decisión o de desviaciones, sin sustituir ni influir en la valoración humana sin revisión;
- **d)** tarea preparatoria de una evaluación.

**Contraexcepción**: "shall always be considered to be high-risk" si el sistema **realiza perfilado de personas físicas** (art. 6.3, último párrafo).

**Obligaciones si se usa la excepción:**

- documentar la evaluación **antes** de la comercialización (art. 6.4);
- **registrar** el sistema en la base de datos de la UE (arts. 6.4 y 49.2), con el contenido reducido de la sección B del anexo VIII;
- entregar la documentación a las autoridades si la piden (art. 6.4).

**Directrices del art. 6** (art. 6.5, plazo legal: 2-02-2026). Solo existe un **borrador** en consulta pública hasta el 23-07-2026, no adoptado (página del Service Desk "Guidelines on classification of high-risk AI systems"). Hay un "Guidelines Explorer" con ejemplos.

---

## 8. Obligaciones de alto riesgo

Aplicables a partir del 2-12-2027 (anexo III) o del 2-08-2028 (anexo I). Ninguno de los arts. 8-16 y 26 tiene marcas NEW o AMENDED en el Service Desk, salvo el art. 10.

### 8.1 Requisitos del sistema (arts. 8-15): comprobaciones técnicas

| Art. | Requisito | Puntos comprobables |
|---|---|---|
| **9** Gestión de riesgos | Proceso iterativo durante todo el ciclo de vida | Identificar y analizar riesgos conocidos y previsibles (9.2.a); estimarlos también ante usos indebidos previsibles (9.2.b); incorporar datos poscomercialización (9.2.c); medidas específicas (9.2.d); riesgo residual aceptable (9.5); pruebas **antes** de comercializar con "prior defined metrics and probabilistic thresholds" (9.8); impacto en **menores de 18** y grupos vulnerables (9.9) |
| **10** Datos | Para sistemas **que entrenan modelos** (10.1 AMENDED) | Prácticas de gobernanza (10.2.a-h): decisiones de diseño, origen y finalidad de los datos, preparación (etiquetado y limpieza), supuestos, disponibilidad, **examen de sesgos** (f), medidas contra sesgos (g) y lagunas (h). Datos pertinentes, representativos y, en la medida de lo posible, sin errores y completos (10.3). Contexto geográfico y funcional (10.4). **Se suprime el 10.5**: los datos sensibles pasan al nuevo art. 4 bis. Si no se entrena, solo se aplica a los **datos de prueba** (10.6 AMENDED) |
| **11** Documentación técnica | Elaborada **antes** de la comercialización y actualizada; contenido mínimo del anexo IV | **Pymes, start-ups y SMC** pueden presentarla de forma simplificada con un **formulario de la Comisión**, que los organismos notificados deben aceptar (11.1 AMENDED) |
| **12** Registros (logs) | Registro **automático** de eventos durante toda la vida útil | Los logs deben permitir detectar situaciones de riesgo o modificaciones sustanciales (12.2.a), la vigilancia poscomercialización (b) y el seguimiento por el responsable del despliegue (c). Para la identificación biométrica remota (anexo III.1.a): periodo de uso, base de datos de referencia, datos con coincidencia e identidad de los verificadores (12.3) |
| **13** Transparencia e instrucciones | Sistema interpretable por el responsable del despliegue, con instrucciones de uso | Instrucciones (13.3): proveedor; finalidad; precisión con métricas, solidez y ciberseguridad; riesgos previsibles; explicabilidad; rendimiento por grupos; especificaciones de los datos; cambios predeterminados; supervisión humana; recursos y vida útil; **mecanismos de logs** |
| **14** Supervisión humana | Diseño que permita una supervisión efectiva | El supervisor debe poder: entender capacidades y límites y detectar anomalías (14.4.a); ser consciente del **sesgo de automatización** (b); interpretar la salida (c); **no usar, ignorar o revertir** la salida (d); **intervenir o detener** el sistema con un "botón de parada" (e). Verificación por **2 personas** en la identificación biométrica remota (14.5) |
| **15** Precisión, solidez y ciberseguridad | Nivel adecuado y constante | Métricas declaradas en las instrucciones (15.3); resiliencia y planes de seguridad ante fallos (15.4); **bucles de retroalimentación** sesgados en sistemas que siguen aprendiendo (15.4); ataques: **envenenamiento de datos y de modelos, ejemplos adversarios o evasión, ataques a la confidencialidad, defectos del modelo** (15.5). Nuevo **art. 42.3**: los sistemas que cumplan el **Reglamento (UE) 2024/2847 (Ley de Ciberresiliencia)** se consideran conformes con los requisitos de ciberseguridad del art. 15 (Omnibus art. 1.18, PE-CONS; Cdo. 19) |

**Anexo IV, documentación técnica (resumen).** Incluye:

1. Descripción general: finalidad, versiones, interacción con otro hardware o software, formas de comercialización (API, descarga), hardware e interfaz.
2. Desarrollo:
   - métodos y uso de **componentes preentrenados de terceros**;
   - lógica y algoritmos, decisiones de diseño y compensaciones;
   - arquitectura y **recursos de cómputo**;
   - **datos**: origen, alcance, etiquetado y limpieza;
   - supervisión humana;
   - cambios predeterminados;
   - validación y pruebas con métricas, incluidos los impactos discriminatorios, y **registros de pruebas fechados y firmados**;
   - ciberseguridad.
3. Capacidades y limitaciones, precisión por grupos y riesgos previsibles.
4. Idoneidad de las métricas.
5. Sistema de gestión de riesgos.
6. Cambios a lo largo del ciclo de vida.
7. Normas armonizadas aplicadas.
8. Declaración UE de conformidad.
9. Plan de vigilancia poscomercialización.

(anexo IV, puntos 1-9.)

### 8.2 Obligaciones de los proveedores (arts. 16-17)

**Art. 16, letras a-l:**

- cumplir la secc. 2;
- indicar nombre y contacto;
- tener un **SGC** (art. 17);
- conservar la documentación (art. 18) y los logs bajo su control (art. 19);
- someterse a la **evaluación de conformidad** (art. 43) antes de comercializar;
- emitir la **declaración UE de conformidad** (art. 47);
- colocar el **marcado CE** (art. 48);
- **registrar** el sistema (art. 49.1);
- adoptar medidas correctoras (art. 20);
- demostrar la conformidad ante las autoridades;
- cumplir la **accesibilidad** (Directivas 2016/2102 y 2019/882).

**Art. 17, sistema de gestión de la calidad**, letras a-m: estrategia de cumplimiento, diseño, desarrollo y QA, pruebas, especificaciones o normas, gestión de datos, gestión de riesgos, vigilancia poscomercialización, notificación de incidentes, comunicación con autoridades, registros, recursos y rendición de cuentas.

- **17.2 (AMENDED)**: proporcionalidad según el tamaño, en particular para pymes, start-ups y **SMC**, manteniendo el rigor.
- **17.4**: las entidades financieras cumplen mediante su gobernanza sectorial, salvo las letras g, h e i.
- **Art. 63.1 (AMENDED)**: **SGC simplificado** para **pymes y start-ups**, con directrices de la Comisión, si no tienen empresas asociadas o vinculadas. No exime de los arts. 9-15, 72 y 73 (art. 63.2).

### 8.3 Responsables del despliegue (art. 26) y FRIA (art. 27)

**Art. 26:**

- usar el sistema según las instrucciones (26.1);
- asignar supervisión humana a personas competentes y con autoridad (26.2);
- datos de entrada pertinentes y representativos si están bajo su control (26.4);
- vigilar el funcionamiento; si hay riesgo, informar y **suspender**; si hay un incidente grave, informar al proveedor y a las autoridades (26.5);
- conservar los **logs al menos 6 meses** (26.6);
- **informar a los representantes de los trabajadores** antes de usarlo en el lugar de trabajo (26.7);
- registro, en el caso de autoridades públicas (26.8);
- usar la información del art. 13 para la **EIPD del art. 35 RGPD** (26.9);
- en la identificación biométrica remota diferida: autorización en un máximo de 48 h (26.10);
- **informar a las personas** sobre las que el sistema del anexo III decide o ayuda a decidir (26.11);
- cooperar con las autoridades (26.12).

> El FAQ del Omnibus indica que se mantienen las **obligaciones de formación** de los responsables del despliegue de alto riesgo, que encajan en el art. 26.2.

**Art. 27, FRIA (evaluación de impacto en los derechos fundamentales).**

- **Quién la hace**: organismos de Derecho público, entidades privadas que prestan servicios públicos y responsables del despliegue del anexo III.5.b (crédito) y 5.c (seguros de vida y salud). Excluye el anexo III.2.
- **Contenido** (27.1.a-f): procesos, periodo y frecuencia, categorías de personas afectadas, riesgos específicos, medidas de supervisión humana y medidas si el riesgo se materializa (gobernanza y reclamaciones).
- **Notificación** de los resultados a la autoridad de vigilancia del mercado (27.3).
- **Novedades:** puede remitirse a la **EIPD** o incorporar partes de ella (27.4 AMENDED). La Oficina de IA elaborará un **cuestionario modelo**, que puede incluir una **herramienta automatizada** (27.5 AMENDED).

### 8.4 Evaluación de conformidad, marcado CE y registro

**Art. 43:**

- **Anexo III.1 (biometría)**: control interno (anexo VI) si se aplican normas armonizadas o especificaciones comunes; si no, organismo notificado (anexo VII) (43.1).
- **Anexo III.2-8**: **control interno, sin organismo notificado** (43.2).
- **Anexo I, sección A**: procedimiento sectorial que integra la secc. 2 (43.3 AMENDED). Los organismos sectoriales deben solicitar su designación **antes del 28-01-2028**.
- Una **modificación sustancial** exige una nueva evaluación. Los cambios predeterminados y documentados (anexo IV.2.f) no lo son (43.4).

**Declaración UE de conformidad y marcado CE**: arts. 47 y 48 (citados en el art. 16.g-h; no se revisaron por separado).

**Registro en la base de datos de la UE** (arts. 49 y 71). El art. 49 no tiene marcas del Omnibus; los cambios están en el anexo VIII.

| Quién | Qué | Cita |
|---|---|---|
| Proveedor del anexo III (salvo el punto 2) | Se registra a sí mismo y registra el sistema **antes** de comercializarlo | art. 49.1; anexo VIII secc. A (13 datos) |
| Proveedor que aplica la excepción del art. 6.3 | Registro con **contenido reducido**: identificación, finalidad, **condición del 6.3 invocada** y estado. Se **suprimen** los puntos 7 y 9 | art. 49.2; anexo VIII secc. B (DELETED en 7 y 9) |
| Responsable del despliegue que es autoridad pública o institución de la UE | Se registra, selecciona el sistema y registra el uso, con resumen de la FRIA y de la EIPD | art. 49.3; anexo VIII secc. C |
| Anexo III.1, 6 y 7 (policía y migración) | Sección **segura y no pública** | art. 49.4 |
| Anexo III.2 (infraestructuras críticas) | Registro **nacional** | art. 49.5 |

### 8.5 Vigilancia poscomercialización e incidentes graves

- **Art. 72**: sistema de vigilancia proporcionado que recopile y analice datos de rendimiento durante toda la vida útil (72.1-2). El **plan forma parte de la documentación técnica**. La Comisión adoptará **orientaciones y una plantilla antes del 2-09-2027**, en lugar del acto de ejecución obligatorio (72.3 AMENDED; Omnibus art. 1.30).
- **Art. 73, plazos de notificación de incidentes graves:**
  - en general, inmediatamente y **como máximo en 15 días** (73.2);
  - **2 días** si hay una infracción generalizada o un incidente del art. 3.49.b (infraestructura crítica) (73.3);
  - **10 días** si hay muerte (73.4).
  - Se permite un informe inicial incompleto (73.5).
  - **No se debe alterar el sistema** antes de informar si eso afecta al análisis de las causas (73.6).
- **Art. 75.1 bis (NEW)**: si el sistema está bajo competencia de la Oficina de IA, los incidentes se notifican a la **Oficina de IA**.

### 8.6 Sistemas ya comercializados (art. 111.2)

Los sistemas de alto riesgo comercializados antes de la fecha de aplicación solo quedan sujetos si sufren **cambios significativos en su diseño**. Si se destinan a autoridades públicas, deben cumplir **antes del 2-08-2030**.

---

## 9. Transparencia (art. 50)

Aplicable **desde el 2-08-2026** (art. 113). Para los sistemas generativos comercializados antes de esa fecha, el art. 50.2 es exigible a partir del **2-12-2026** (art. 111.4, NEW). Multa: hasta 15 M EUR o el 3 % (art. 99.4.g). Solo el art. 50.7 está marcado AMENDED.

| Apdo. | Obligado | Obligación | Excepciones |
|---|---|---|---|
| **50.1** | **Proveedor** | Sistemas que **interactúan directamente** con personas (**chatbots, agentes, avatares, asistentes de voz**): deben estar diseñados para que la persona sepa que interactúa con una IA | Cuando sea **obvio** para una persona razonablemente informada (interpretación **restrictiva**; no se aplica si se exponen grupos vulnerables, directrices párr. 42-45). Uso policial autorizado por ley, salvo los sistemas públicos para denunciar delitos |
| **50.2** | **Proveedor**, también de sistemas GPAI | Contenido sintético de **audio, imagen, vídeo o texto**: **marcado legible por máquina** y **detectable** como generado o manipulado artificialmente. Soluciones eficaces, interoperables, sólidas y fiables en la medida técnicamente posible | Función de **asistencia a la edición estándar**; sistemas que no alteran sustancialmente la entrada ni su semántica; uso policial autorizado |
| **50.3** | **Responsable del despliegue** | **Reconocimiento de emociones o categorización biométrica**: informar a las personas expuestas y tratar los datos conforme al RGPD | Uso policial autorizado por ley |
| **50.4** | **Responsable del despliegue** | **Deepfakes**: revelar que el contenido es artificial. **Texto publicado para informar al público sobre asuntos de interés público**: revelarlo | Obras **evidentemente** artísticas, creativas, satíricas o de ficción: revelación atenuada que no estropee la obra. Texto con **revisión humana o control editorial** y responsabilidad editorial. Uso policial |
| **50.5** | Ambos | Información **clara y distinguible**, **como muy tarde en la primera interacción o exposición**, y accesible | — |
| **50.7** (AMENDED) | Comisión | Códigos de buenas prácticas sobre detección, marcado y etiquetado. **Acto de ejecución solo si el código se considera inadecuado** | — |

**Criterios operativos de las directrices del art. 50**, Comunicación C(2026) 7702 final, de 5-11-2026 (su contenido se aprobó el 20-07-2026 como C(2026) 5054, con la misma numeración de párrafos), no vinculantes:

- **Interacción directa**: hay 4 elementos (párr. 30). Las respuestas automáticas basadas en reglas, como un mensaje de ausencia, quedan fuera. Los **agentes de IA** deben revelar su naturaleza y **en nombre de quién actúan**, en cada interacción nueva y en los pasos clave (párr. 31).
- **Técnicas de aviso recomendadas** (párr. 37): etiquetas, banners, saludo en el primer turno, aviso sonoro en voz, iconos persistentes o el símbolo "AI".
- **Avisos insuficientes** (párr. 38): solo los términos y condiciones o una URL; marcas no perceptibles; etiquetas vagas como "assistant"; frases genéricas del tipo "este sitio usa IA"; "este sistema usa LLMs".
- **Recordatorios periódicos** en contextos de riesgo: personas vulnerables, asesoramiento financiero, sanitario o jurídico, y **AI companions**. También cuando el usuario pregunta (párr. 40).
- **Marcado (50.2)**: hacen falta **las dos cosas**, marcado legible por máquina **y** detectabilidad (párr. 69-70).
  - Técnicas: marcas de agua, metadatos, procedencia criptográfica, registro (logging) y huellas (fingerprints). Se admite combinarlas en varias capas (párr. 72-73; Cdo. 133).
  - El marcado puede hacerse a nivel de modelo, en la inferencia o a posteriori. El proveedor sigue siendo responsable aunque use una solución de terceros (párr. 74).
  - La detección debe estar disponible para las personas expuestas, preferiblemente con herramientas estándar públicas (párr. 75-76).
- **Fuera del marcado** (párr. 64-68):
  - salidas muy cortas: palabras sueltas, pies de foto, *alt-text*, etiquetas de interfaz;
  - **código fuente, SQL, JSON, YAML, esquemas y API**;
  - salidas máquina a máquina;
  - recomendadores que solo ordenan contenido existente;
  - salidas intermedias de un circuito cerrado de producción.
- **Edición estándar** (párr. 90-92): gramática, formato, traducción, transcripción y reducción de ruido están exentos. **Sí** hay que marcar los resúmenes generados, las reescrituras que cambian el sentido y la inserción o eliminación de personas u objetos en imágenes.
- **Ultrafalsificación o deepfake** (párr. 113-117):
  - cuatro criterios acumulativos (párr. 113): semejanza apreciable; con personas, objetos, lugares, entidades o sucesos; existentes; y que puede inducir a una persona a pensar erróneamente que son auténticos o verídicos. No hace falta intención de engañar (párr. 114).
  - Un avatar realista del CEO **sí** es un deepfake; una esfinge volando sobre la Torre Eiffel **no**.
  - El responsable del despliegue necesita una etiqueta **perceptible por humanos**. **No le basta** con el marcado técnico del proveedor.
- **Emociones y biometría** (párr. 99-108): avisar a **todas** las personas expuestas, incluidos los niños, en la primera exposición. Ejemplo: una ventana emergente antes de un juego que graba la cara.

**Código de buenas prácticas sobre transparencia del contenido generado por IA**: versión final del 10-06-2026. La Comisión y el Comité lo consideran **adecuado** para demostrar el cumplimiento, y hay iconos de la UE para etiquetar. La FAQ del art. 50 aclara que el contenido generado antes del 2-08-2026 **no** requiere etiquetado retroactivo.

---

## 10. Modelos de IA de uso general (GPAI)

Aplicable desde el 2-08-2025; la Comisión puede multar desde el 2-08-2026. Ninguno de los arts. 51-55 tiene marcas del Omnibus. El art. 56.6 está marcado AMENDED.

| Tema | Regla | Cita |
|---|---|---|
| ¿Es un modelo GPAI? | Generalidad significativa (art. 3.63). **Criterio indicativo** de la Comisión: cómputo de entrenamiento **> 10^23 FLOP** y capacidad de generar lenguaje (texto o audio), texto a imagen o texto a vídeo. No es un criterio absoluto | Directrices GPAI C(2025) 5045, párr. 17 y 20 |
| Obligaciones de **todos** los proveedores | a) documentación técnica (anexo XI) para la Oficina de IA y las autoridades; b) información para los proveedores *downstream* (anexo XII); c) **política de derechos de autor**, incluido el respeto de la reserva de derechos del art. 4.3 de la Directiva 2019/790 (*opt-out* de minería de textos y datos); d) **resumen público del contenido de entrenamiento** según la plantilla de la Oficina de IA | art. 53.1 |
| Excepción **open source** | Licencia libre que permita acceso, uso, modificación y distribución, con pesos, arquitectura e información de uso públicos. **Exime solo de las letras a y b** del art. 53.1 y del representante del art. 54. **No** exime de c y d, ni se aplica a modelos con riesgo sistémico | art. 53.2; art. 54.6 |
| Monetización (open source) | Descalifican para la excepción: las licencias no comerciales, los umbrales de usuarios, la doble licencia de pago, el soporte de pago obligatorio y el alojamiento exclusivo de pago | Directrices GPAI, párr. 83-89 |
| Modificador que pasa a ser proveedor | Criterio indicativo: la modificación usa **más de 1/3 del cómputo** de entrenamiento original. Si no se conoce, 1/3 de 10^25 o de 10^23 FLOP | Directrices GPAI, párr. 63-64 |
| Representante autorizado | Obligatorio para proveedores de fuera de la UE. Conserva el anexo XI **10 años** | art. 54 |
| **Riesgo sistémico** | Capacidades de gran impacto o designación de la Comisión según el anexo XIII. **Se presume si el cómputo acumulado de entrenamiento es > 10^25 FLOP** | art. 51.1-2 |
| Criterios del anexo XIII | Parámetros, datos (tokens), FLOP, modalidades, *benchmarks*, impacto en el mercado (**se presume con ≥ 10 000 usuarios profesionales registrados en la UE**) y número de usuarios finales | anexo XIII.a-g |
| Notificación | A la Comisión **sin demora y en un máximo de 2 semanas** desde que se alcanza o se prevé el umbral. Se pueden presentar argumentos para refutar el riesgo sistémico. La reevaluación puede pedirse a los 6 meses | art. 52.1-5. Canal: plataforma EU SEND (página "Guidelines for GPAI providers") |
| Obligaciones adicionales (riesgo sistémico) | a) evaluación con protocolos de vanguardia y **pruebas adversarias**; b) evaluar y mitigar los riesgos sistémicos; c) notificar incidentes graves a la Oficina de IA sin demora indebida; d) **ciberseguridad** del modelo y de su infraestructura | art. 55.1; anexo XI secc. 2 |
| Códigos de buenas prácticas | Sirven para demostrar el cumplimiento hasta que haya normas armonizadas. Quien no se adhiere debe demostrar medios alternativos. La Comisión evalúa y **publica** su valoración de adecuación (56.6 AMENDED) | arts. 53.4, 55.2, 56 |
| Modelos anteriores | Los comercializados antes del 2-08-2025 deben cumplir **antes del 2-08-2027** | art. 111.3 |
| Multas | Hasta **15 M EUR o el 3 %**, la cifra mayor | art. 101.1 |

**Anexo XI, secc. 1**: tareas previstas, política de uso aceptable, fecha y forma de distribución, arquitectura y **número de parámetros**, modalidades, licencia, diseño y proceso de entrenamiento, datos, **recursos de cómputo** y **consumo energético**. **Secc. 2** (riesgo sistémico): estrategias de evaluación, pruebas adversarias o *red teaming* y arquitectura.

**Anexo XII**: integra el contenido de la secc. 1 del anexo XI más el **tamaño máximo de entrada**, es decir, la **ventana de contexto**.

---

## 11. Alfabetización en IA (art. 4) y datos sensibles para sesgos (art. 4 bis)

**Art. 4 (AMENDED por Omnibus art. 1.5; Cdo. 8):**

- **4.1**: los proveedores y responsables del despliegue "shall take measures to support the development of AI literacy" de su personal y de las demás personas que operan sistemas en su nombre, según sus conocimientos, el contexto de uso y las personas afectadas. "This obligation does not require providers or deployers to guarantee any specific level of AI literacy of any individual."
- **4.2**: la Comisión y los Estados miembros apoyarán, con atención a las pymes. La Comisión publicará **ejemplos prácticos** en la plataforma única de información del art. 62.3.b.
- **4.3**: el Comité adoptará recomendaciones basadas en marcos europeos de competencias.
- **Antes**, la obligación era la de garantizar, "en la mayor medida posible", un nivel suficiente de alfabetización. Esto se deduce del Cdo. 8 del Omnibus; el texto original no se leyó de forma literal.
- Recurso de la Comisión: el *living repository* de prácticas de alfabetización (FAQ).

**Art. 4 bis (NEW; Omnibus art. 1.6).** Tratamiento de categorías especiales de datos personales para detectar y corregir sesgos.

- **Apdo. 1**: los proveedores de alto riesgo pueden hacerlo de forma excepcional, cuando sea estrictamente necesario para el art. 10.2.f-g, si se cumplen **todas** estas condiciones:
  - **a)** no es posible con otros datos, **incluidos los sintéticos o anonimizados**;
  - **b)** límites técnicos a la reutilización y medidas de vanguardia, incluida la **seudonimización**;
  - **c)** controles estrictos y **acceso documentado**, limitado a personas autorizadas con deber de confidencialidad;
  - **d)** **no** se transmiten a terceros;
  - **e)** se **suprimen** cuando se corrige el sesgo o vence el plazo de conservación;
  - **f)** el registro de actividades de tratamiento justifica la necesidad.
- **Apdo. 2**: se extiende a los proveedores y responsables del despliegue de **otros sistemas y modelos** y a los responsables del despliegue de alto riesgo, con las mismas condiciones. **No crea la obligación** de detectar sesgos.

---

## 12. Sandboxes y pruebas en condiciones reales (arts. 57-63)

- **Sandbox nacional** operativo **antes del 2-08-2027** (art. 57.1 AMENDED).
- **Sandbox a escala de la UE** de la Oficina de IA para los sistemas del art. 75.1, con **acceso prioritario para pymes, start-ups y SMC** (art. 57.3 bis, NEW). La FAQ habla de "from 2028"; el texto no da fecha.
- **Sin multas administrativas** si se sigue el plan del sandbox y las orientaciones de buena fe (art. 57.12). El **informe de salida** debe tenerse en cuenta en la evaluación de conformidad (57.7).
- **Art. 58.1 (AMENDED)**: actos de ejecución con reglas comunes, más una nueva letra d) sobre gobernanza. Esas reglas están en el **Reglamento de Ejecución (UE) 2026/2487, de 10-11-2026**, según la noticia de AESIA del 12-11-2026. No se ha leído en EUR-Lex.
- **Art. 59**: tratamiento ulterior de datos personales en el sandbox para sistemas de interés público sustancial, con salvaguardias.
- **Art. 60 (AMENDED 60.1-2)**: pruebas en condiciones reales fuera del sandbox para el anexo III y el anexo I.A, "at any time" antes de comercializar. Requisitos:
  - plan aprobado; silencio positivo a los 30 días;
  - registro;
  - un **máximo de 6 meses, prorrogables otros 6**;
  - consentimiento informado (art. 61);
  - reversibilidad;
  - supervisión.
- **Art. 60 bis (NEW)**: los Estados miembros pueden permitir pruebas reales para los productos del anexo I, sección B, mediante marcos nacionales notificados a la Comisión.
- **Art. 62**: apoyo a pymes y start-ups: acceso prioritario a sandboxes, formación, canales de consulta y **tasas reducidas** en la evaluación de conformidad.
- **Art. 70.8 (AMENDED)**: las autoridades nacionales pueden orientar a pymes, start-ups y SMC.

---

## 13. Supervisión y sanciones

**Oficina de IA:**

- **Competencia exclusiva** (art. 75.1 AMENDED):
  - a) sistemas basados en un **modelo GPAI cuando el modelo y el sistema son del mismo proveedor** o del mismo grupo. Excepciones: productos del anexo I, anexo III.2, policía, fronteras y entidades financieras (en la medida del art. 74.6) y anexo III.8;
  - b) sistemas que son o se integran en una **VLOP o VLOSE** designada según la DSA.
- Recibe los **incidentes graves** (75.1 bis) y gestiona la **evaluación de conformidad por terceros**, delegable en organismos notificados que el proveedor paga (75.1 sexies).
- **Art. 75 bis (NEW)**: poderes de autoridad de vigilancia del mercado. Puede pedir información e inspeccionar, también *in situ*, y **repercutir el coste total** de la supervisión al operador incumplidor.
- **Art. 77.1 bis-1 ter (NEW)**: las autoridades de derechos fundamentales obtienen acceso a la información a través de las autoridades de vigilancia del mercado.

**Multas (art. 99):**

| Infracción | Máximo | Cita |
|---|---|---|
| Prácticas prohibidas (art. 5) | **35 000 000 EUR o el 7 %** del volumen de negocios mundial anual, la cifra mayor | art. 99.3 |
| Obligaciones de proveedores (16), representantes (22), importadores (23), distribuidores (24), **cadena de valor (25.2 y 25.4, NEW, letra d bis)**, responsables del despliegue (26), organismos notificados y **transparencia (50)** | **15 000 000 EUR o el 3 %**, la cifra mayor | art. 99.4 |
| Información incorrecta, incompleta o engañosa a las autoridades o a los organismos notificados | **7 500 000 EUR o el 1 %**, la cifra mayor | art. 99.5 |
| **Pymes y start-ups** | Se aplica **la cifra menor** en todas las multas | art. 99.6 |
| **SMC** (NEW) | La **cifra menor** en las multas de los apdos. 4 y 5, **no en las del art. 5** | art. 99.6 bis |
| Instituciones de la UE (impone el SEPD) | 1 500 000 EUR (art. 5); 750 000 EUR (resto) | art. 100.2-3 |
| Proveedores de GPAI (impone la Comisión) | **15 000 000 EUR o el 3 %**, la cifra mayor, por dolo o negligencia | art. 101.1 |

---

## 14. Cambios del Reglamento 2026/1744, artículo por artículo

Leyenda de verificación:

- **[OJ]**: leído en EUR-Lex (DO).
- **[PC]**: leído en PE-CONS 30/1/26 REV 1 (texto final firmado).
- **[SD]**: marcado NEW, AMENDED o DELETED en el consolidado del Service Desk.

| N.º Omnibus art. 1 | Disposición del RIA | Cambio | Verif. |
|---|---|---|---|
| 1 | Art. 1.2.g | Las medidas de innovación mencionan expresamente las **SMC**, las pymes y las start-ups | OJ, PC |
| 2 | Art. 2.2 y 2.7 | Anexo I, sección B: solo los arts. 6.1, 60 bis y 102-112. Protección de datos sin perjuicio de los arts. 4 bis y 59 | OJ, PC, SD |
| 3 | Art. 2.13 (nuevo) | Limitación de los requisitos de los arts. 9-15 y 17-25 para el anexo I, sección A, si la protección sectorial es equivalente. Actos delegados antes del 2-08-2027 | OJ, PC, SD |
| 4 | Art. 3.14, 14 bis y 14 ter | Nueva definición de componente de seguridad ("función de seguridad"). Definiciones de **pyme** y **SMC** | OJ, PC, SD |
| 5 | Art. 4 | Alfabetización: pasa de garantizar a **tomar medidas de apoyo**. Ejemplos de la Comisión y recomendaciones del Comité | OJ, PC, SD |
| 6 | Art. 4 bis (nuevo) | Categorías especiales de datos para detectar y corregir sesgos, con 6 condiciones; también fuera del alto riesgo | OJ, PC, SD |
| 7 | Art. 5.1.b bis, b ter, 1 bis y 1 ter | Prohibición de deepfakes íntimos no consentidos y de material de abuso sexual infantil. Se aplica a partir del 2-12-2026 | OJ, PC, SD |
| 8 | Art. 6.1 bis, 1 ter y 1 quater | Qué es y qué no es un componente de seguridad; evaluación por terceros solo por riesgos no sanitarios | OJ, PC, SD |
| 9 | Art. 10.1, 10.5 y 10.6 | 10.1 reformulado; **10.5 suprimido**, pasa al art. 4 bis; 10.6 remite al art. 4 bis.1 | OJ, PC, SD |
| 10 | Art. 11.1, párr. 2 | Documentación técnica simplificada para **pymes, start-ups y SMC**, con un formulario de la Comisión obligatorio para ellas y aceptado por los organismos notificados | PC, SD |
| 11 | Art. 17.2 | SGC proporcional al tamaño, incluidas las SMC | PC, SD |
| 12 | Art. 25.2 y 25.4 | Cooperación del proveedor inicial y acuerdo escrito con los suministradores; exención open source salvo GPAI | PC, SD |
| 13 | Art. 27.4 y 27.5 | La FRIA puede remitirse a la EIPD; cuestionario o herramienta automatizada de la Oficina de IA | PC, SD |
| 14 | Art. 28.8 y 28.9 (nuevos) | Solicitud única y procedimiento unificado para los organismos notificados del anexo I.A | PC, SD |
| 15 | Art. 29.4 | Reutilización de documentos de designación; solicitud única | PC |
| 16 | Art. 30.2 | Notificación vinculada a los códigos del **anexo XIV**, modificable por acto delegado | PC |
| 17 | Art. 40.2 | Petición de normalización que apoye el cumplimiento conjunto con la legislación sectorial | PC |
| 18 | Art. 42.3 (nuevo) | Presunción de conformidad con la ciberseguridad del art. 15 si se cumple la **Ley de Ciberresiliencia, Reglamento 2024/2847** | PC (el SD advierte de que su texto del art. 42 no está actualizado) |
| 19 | Art. 43.3 | Nueva regla de evaluación de conformidad para el anexo I. Los organismos sectoriales deben solicitar la designación antes del 28-01-2028. Cdo. 18: plazo de 18 meses desde el 27-07-2026 | PC, SD |
| 20 | Art. 50.7 | Acto de ejecución sobre transparencia **solo si** el código es inadecuado | PC, SD |
| 21 | Art. 56.6 | Seguimiento de los códigos y publicación de la evaluación de adecuación | PC, SD |
| 22 | Art. 57 (1, 3, 3 bis, 4, 5, 9.e, 10 y 14) | Sandbox nacional antes del 2-08-2027; sandbox del SEPD; **sandbox de la UE** de la Oficina de IA con prioridad para pymes y SMC; papel de las autoridades de protección de datos | PC, SD |
| 23 | Art. 58.1 | Actos de ejecución "to avoid fragmentation" y nueva letra d) sobre gobernanza | PC, SD |
| 24 | Art. 60.1 y 60.2 | Pruebas reales para el anexo III y el anexo I.A "at any time" antes de comercializar | PC, SD |
| 25 | Art. 60 bis (nuevo) | Pruebas reales para el anexo I.B con marcos nacionales | PC, SD |
| 26 | Art. 63.1 | SGC simplificado para pymes y start-ups con directrices de la Comisión | PC, SD |
| 27 | Art. 64.3 (nuevo) | Recursos adecuados para la Oficina de IA | PC |
| 28 | Art. 69.2 | Tasas por el acceso de los Estados miembros a los expertos del grupo científico (simplificación, Cdo. 30) | PC (el SD no tiene el texto actualizado) |
| 29 | Art. 70.8 | Orientación a pymes, start-ups y SMC | PC |
| 30 | Art. 72.3 | Plan de vigilancia poscomercialización como parte de la documentación técnica; **orientaciones y plantilla antes del 2-09-2027**, sin acto de ejecución | PC, SD |
| 31 | Art. 75 | Competencia exclusiva de la Oficina de IA (GPAI del mismo proveedor, VLOP y VLOSE); apdos. 1 bis a 1 sexies y 2 bis; respuesta en un máximo de 4 meses | PC, SD |
| 32 | Art. 75 bis (nuevo) | Poderes de supervisión y ejecución de la Oficina de IA | PC (parcial), SD |
| ¿? | Art. 77.1, 1 bis y 1 ter | Acceso a la información de las autoridades de derechos fundamentales | SD |
| ¿? | Art. 96.1 (a-g) | Directrices: nueva letra g) sobre los arts. 8.2, 9.10 y 17.3 (antes del 1-08-2027); atención a las SMC | SD |
| ¿? | Art. 99.1, 99.4.d bis y 99.6 bis | Multas por el art. 25.2 y 25.4; tope "el menor de" para las SMC | SD |
| ¿? | Art. 111.2 y 111.4 | Ajuste de la referencia de fechas; **art. 50.2 a partir del 2-12-2026** para sistemas anteriores al 2-08-2026 | SD |
| ¿? | Art. 113.a, c y d | Nuevas fechas (sección 3) | SD |
| ¿? | Anexo I | Máquinas: el punto 1 de la sección A se suprime y se añade el punto 21 en la sección B, Reglamento 2023/1230 | SD |
| ¿? | Anexo VIII, secc. B | Se suprimen los puntos 7 y 9: registro reducido para el art. 6.3 | SD |
| ¿? | Anexo XIV | Códigos para la notificación de organismos (Omnibus punto 16); contenido no leído | PC (referencia) |
| Art. 2 y 3 del Omnibus | Reglamentos 2018/1139 y 2023/1230 | Modificaciones correlativas, incluido el anexo III del Reglamento de máquinas (Cdo. 45) | **No leído** |

**"¿?"**: el número de punto del art. 1 del Omnibus no se pudo leer, porque el PE-CONS se cortó en el punto 32. El cambio se verificó solo en el consolidado del Service Desk.

---

## 15. AESIA: qué publica y cómo aprovecharlo

AESIA es la Agencia Española de Supervisión de la Inteligencia Artificial (https://aesia.digital.gob.es/).

### 15.1 Guías prácticas (16), en https://aesia.digital.gob.es/es/guias

Proceden del **sandbox piloto español**, liderado por SEDIA con la Comisión Europea. Participaron **12 sistemas de alto riesgo de 6 sectores**: servicios esenciales, biometría, empleo, infraestructuras críticas, máquinas y productos sanitarios (noticia AESIA del 12-11-2026). La página de guías indica que "serán actualizadas de acuerdo al Ómnibus Digital". **Todavía reflejan el texto anterior al Omnibus.**

| N.º | Título | URL directa | Artículo |
|---|---|---|---|
| 01 | Guía introductoria al reglamento de IA | https://aesia.digital.gob.es/storage/media/01-guia-introductoria-al-reglamento-de-ia.pdf | General |
| 02 | Guía práctica y ejemplos para entender el Reglamento de IA | https://aesia.digital.gob.es/storage/media/02-guia-practica-y-ejemplos-para-entender-el-reglamento-de-ia.pdf | Ejemplos |
| 03 | Guía Evaluación de conformidad | https://aesia.digital.gob.es/storage/media/03-guia-evaluacion-de-conformidad.pdf | art. 43 |
| 04 | Guía del sistema de gestión de la calidad | https://aesia.digital.gob.es/storage/media/04-guia-del-sistema-de-gestion-de-la-calidad.pdf | art. 17 |
| 05 | Guía de gestión de riesgos | https://aesia.digital.gob.es/storage/media/05-guia-de-gestion-de-riesgos.pdf | art. 9 |
| 06 | Guía Vigilancia humana | https://aesia.digital.gob.es/storage/media/06-guia-vigilancia-humana.pdf | art. 14 |
| 07 | Guía de datos y gobernanza de datos | https://aesia.digital.gob.es/storage/media/07-guia-de-datos-y-gobernanza-de-datos.pdf | art. 10 |
| 08 | Guía Transparencia | https://aesia.digital.gob.es/storage/media/08-guia-transparencia.pdf | art. 13 |
| 09 | Guía de Precisión | https://aesia.digital.gob.es/storage/media/09-guia-de-precision.pdf | art. 15 |
| 10 | Guía Solidez | https://aesia.digital.gob.es/storage/media/10-guia-solidez.pdf | art. 15 |
| 11 | Guía Ciberseguridad | https://aesia.digital.gob.es/storage/media/11-guia-ciberseguridad.pdf | art. 15 |
| 12 | Guía de registros | https://aesia.digital.gob.es/storage/media/12-guia-de-registros.pdf | art. 12 |
| 13 | Guía Vigilancia poscomercialización | https://aesia.digital.gob.es/storage/media/13-guia-vigilancia-poscomercializacion.pdf | art. 72 |
| 14 | Guía Gestión de Incidentes | https://aesia.digital.gob.es/storage/media/14-guia-gestion-de-incidentes.pdf | art. 73 |
| 15 | Guía Documentación Técnica | https://aesia.digital.gob.es/storage/media/15-guia-documentacion-tecnica.pdf | art. 11 y anexo IV |
| 16 | Manual de checklist de guías de requisitos | https://aesia.digital.gob.es/storage/media/16-manual-de-checklist-de-guias-de-requisitos.pdf | Todos |
| — | **Compendio de checklists y ejemplos (ZIP)** | https://aesia.digital.gob.es/storage/Checklists%20y%20ejemplos.zip | Todos |

### 15.2 Estructura de los checklists (guía 16, v1.1 de 30-06-2026, CC BY 4.0)

- Hay **12 checklists**, uno por requisito: SGC, gestión de riesgos, supervisión humana, datos, transparencia, precisión, solidez, ciberseguridad, registros, documentación técnica, vigilancia poscomercialización e incidentes.
- Todos están en **un único Excel** con **9 pestañas**.
  - Informativas: Portada, Intro, Artículo RIA, Medidas Guías (MG) y Relación MG-Apartado.
  - Operativas: Autoeval MG, Medidas Adicionales (MA), Relación MA-Apartado y Autoeval MA.
- Datos que se rellenan:
  - **Dificultad percibida**: 00 Alto, 01 Medio, 02 Bajo.
  - **Nivel de madurez L1-L8**: L1 sin documentar ni implementar … L5 documentado e implementado; L6 implementado sin documentar; L8 no necesaria.
  - El **Plan de adaptación** se deriva de forma automática: "01 Documentar e implementar", "02 Implementar", "03 Adaptación completa", "04 Documentar" o "05 Ninguna adaptación requerida".
- **No hay una puntuación numérica.** El progreso se mide con el "Estado diagnóstico".

### 15.3 Otros recursos de AESIA

**Recursos** (https://aesia.digital.gob.es/es/recursos y su segunda página):

- FAQs sobre las directrices del art. 50: https://aesia.digital.gob.es/es/recursos/ria-articulo-50-faqs-directrices-sobre-transparencia
- FAQs sobre el código de buenas prácticas de transparencia: https://aesia.digital.gob.es/es/actualidad/recursos/ria-articulo-50-faqs-codigo-de-buenas-practicas
- Preguntas y respuestas sobre el art. 50: https://aesia.digital.gob.es/es/actualidad/recursos/ria-articulo-50
- Preguntas y respuestas sobre el art. 4 (alfabetización): https://aesia.digital.gob.es/es/actualidad/recursos/ria-articulo-4
- Alfabetización en IA: https://aesia.digital.gob.es/es/actualidad/recursos/20250821-alfabetizacion-en-ia
- Recursos útiles de alfabetización: https://aesia.digital.gob.es/es/actualidad/recursos/ria-recusos-utiles
- Directrices sobre GPAI (resumen en español): https://aesia.digital.gob.es/es/actualidad/recursos/20250608-directrices-sobre-modelos-de-ia-de-uso-general
- Sistemas de alto riesgo: https://aesia.digital.gob.es/es/actualidad/recursos/ria-sistemas-de-alto-riesgo. Trae ejemplos: un semáforo adaptativo, la vigilancia de exámenes, la corrección de la calidad del agua y un juguete de voz. Reparte la supervisión entre AESIA, AEPD, Banco de España, CGPJ y las autoridades sectoriales. Ojo: habla de autoevaluación por el "anexo VII", cuando el art. 43.2 remite al control interno del **anexo VI**; hay que contrastarlo.
- Sistemas prohibidos: https://aesia.digital.gob.es/es/actualidad/recursos/ria-sistemas-prohibidos
- Aproximación general al RIA: https://aesia.digital.gob.es/es/actualidad/recursos/ria-aproximacion-general

**Divulgación sobre transparencia** (https://aesia.digital.gob.es/es/divulgacion):

- "Tus derechos de transparencia"
- "Transparencia en la era de la IA"
- "Normas de transparencia"

**Otros:**

- **Laboratorio de ideas** (https://aesia.digital.gob.es/es/el-laboratorio): un comité asesor y grupos de trabajo sobre mujeres, desinformación, menores y mercado laboral. **No** es una herramienta técnica.
- La página "Publicaciones" estaba "En construcción" en la fecha de consulta.

### 15.4 Sandbox español

- **Real Decreto 817/2023, de 8 de noviembre** (BOE n.º 268, 9-11-2023; https://www.boe.es/buscar/act.php?id=BOE-A-2023-22767). Crea el entorno controlado de pruebas.
- Vigencia "máximo treinta y seis meses desde su entrada en vigor", que fue el 10-11-2023. También decae si antes se aplica el RIA.
- *Inferencia:* el plazo terminaría hacia el 10-11-2026. **No se ha verificado** si sigue operativo ni qué lo sustituye.
- El sandbox nacional obligatorio debe estar operativo antes del 2-08-2027 (art. 57.1). Las reglas comunes están en el Reglamento de Ejecución (UE) 2026/2487 (sección 12).

### 15.5 Cómo aprovecharlo en el plugin (inferencia)

- **Reutilizar el modelo de datos de los checklists**: requisito → apartado del artículo → medida guía → pregunta guía → madurez L1-L8 → plan de adaptación. La licencia CC BY 4.0 permite reutilizarlo citando a SEDIA y AESIA. Así el plugin genera un informe "compatible AESIA".
- Las guías 05, 07, 12 y 06 (riesgos, datos, logs y supervisión) se traducen mejor a **comprobaciones sobre código** y pipelines de ML. La 15 sirve como plantilla del anexo IV.
- **Advertencia**: hay que marcar en la herramienta lo que el Omnibus cambia respecto a las guías: 10.5 → 4 bis, documentación técnica simplificada para pymes y SMC, SGC simplificado, plan de vigilancia poscomercialización, fechas y alfabetización.

---

## 16. Directrices y códigos oficiales de la Comisión

| Documento | Fecha y estado | URL |
|---|---|---|
| Directrices sobre la definición de sistema de IA, C(2025) 5053 final | Publicadas el 6-02-2025; adoptadas el 29-07-2025; no vinculantes | PDF ES: https://ec.europa.eu/newsroom/dae/redirection/document/118640 · https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-ai-system-definition-facilitate-first-ai-acts-rules-application · PDF EN: https://ai-act-service-desk.ec.europa.eu/sites/default/files/2025-08/commission_guidelines_on_the_definition_of_an_artificial_intelligence_system_established_by_regulation_eu_20241689_ai_actenglish_nf2skcqfrtjdfggjavcodopcwz4_112455.PDF |
| Directrices sobre prácticas prohibidas, C(2025) 5052 final | Publicadas el 4-02-2025; adoptadas el 29-07-2025; no vinculantes | PDF ES: https://ec.europa.eu/newsroom/dae/redirection/document/118659 · https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-prohibited-artificial-intelligence-ai-practices-defined-ai-act · PDF EN: https://ai-act-service-desk.ec.europa.eu/sites/default/files/2025-08/guidelines_on_prohibited_artificial_intelligence_practices_established_by_regulation_eu_20241689_ai_act_english_ied3r5nwo50xggpcfmwckm3nuc_112367-1.PDF |
| Directrices sobre el alcance de las obligaciones GPAI, C(2025) 5045 | 18-07-2025, actualizadas el 20-04-2026 | https://digital-strategy.ec.europa.eu/en/library/guidelines-scope-obligations-providers-general-purpose-ai-models-under-ai-act · PDF: https://ai-act-service-desk.ec.europa.eu/sites/default/files/2025-07/guidelines_on_the_scope_of_the_obligations_for_generalpurpose_ai_models_established_by_regulation_1cx2atxgq79us4n3x8jfgyy1qlm_118340-3.pdf · FAQ: https://digital-strategy.ec.europa.eu/en/faqs/guidelines-obligations-general-purpose-ai-providers |
| Directrices del art. 50 (transparencia), C(2026) 7702 final | Adoptadas el 5-11-2026 (contenido aprobado el 20-07-2026 como C(2026) 5054); no vinculantes | PDF ES: https://ec.europa.eu/newsroom/dae/redirection/document/134794 · PDF EN de julio: https://ai-act-service-desk.ec.europa.eu/sites/default/files/2026-07/guidelines_on_the_implementation_of_the_transparency_obligations_for_certain_ai_systems_under_article_50_of_the_ai_act_bzptwqhk0ikg1dtlddap41psfy_131215.pdf · https://digital-strategy.ec.europa.eu/en/policies/guidelines-transparency-ai-generated-content · Q&A: https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act |
| Código de buenas prácticas sobre transparencia del contenido generado por IA | Final el 10-06-2026; declarado adecuado | https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content · PDF: https://ec.europa.eu/newsroom/dae/redirection/document/129555 · Iconos UE: https://digital-strategy.ec.europa.eu/en/policies/eu-icons-labelling-ai-generated-content |
| Directrices de clasificación de alto riesgo (art. 6) | **BORRADOR** publicado el 19-05-2026, consulta hasta el 23-07-2026; sin versión final a 17-11-2026 | https://ai-act-service-desk.ec.europa.eu/en/guidelines-classification-high-risk-ai-systems · https://digital-strategy.ec.europa.eu/en/library/draft-guidelines-high-risk · Explorer: https://ai-act-service-desk.ec.europa.eu/en/guideline-explorer |
| Código de buenas prácticas GPAI | Versión final de julio de 2025 (según la lista awesome; **no leído** en origen) | https://digital-strategy.ec.europa.eu/en/policies/ai-act-general-purpose-ai |
| AI Act Service Desk: Compliance Checker, Explorer y FAQ | Oficial (Comisión) | https://ai-act-service-desk.ec.europa.eu/en/eu-ai-act-compliance-checker · https://ai-act-service-desk.ec.europa.eu/en/ai-act-explorer · https://ai-act-service-desk.ec.europa.eu/en/faq |

---

## 17. Herramientas y recursos existentes (lista awesome-eu-ai-act)

> **Procedencia:** todo este apartado sale de la lista curada de la comunidad https://github.com/morganrcu/awesome-eu-ai-act (README de la rama `master`, consultado el 17-11-2026). **No es una fuente primaria.** Las descripciones son las de la lista. No se ha comprobado el funcionamiento de las herramientas, ni su licencia, ni su exactitud jurídica. Sirven como referencia o como competencia del plugin.

**Las más parecidas al plugin (análisis de código o del caso de uso):**

| Herramienta | Qué hace (según la lista) | Licencia (según la lista) |
|---|---|---|
| [Regula](https://github.com/kuzivaai/getregula) | CLI offline que **escanea código fuente** en busca de indicadores de riesgo del AI Act. Unos 419 patrones en 8 familias de lenguajes | Apache-2.0 / EUPL 1.2 |
| [AIR Blackbox](https://github.com/airblackbox/gateway) | CLI que comprueba **código Python de agentes** frente a los arts. 9-15 | OSS |
| [EU AI Act Risk Checker](https://github.com/tomdxb0004/eu-ai-act-risk-checker) | Triaje del nivel de riesgo en el cliente con cita del artículo; **actualizado para el Omnibus 2026/1744** | MIT |
| [AI Act Companion](https://github.com/JKasteele/ai-act-companion) | Clasificador local; genera EIPD, anexo IV y FRIA; cruces con NIST e ISO 42001 | MIT |
| [art50-ci](https://github.com/Rubiss/art50-ci) | GitHub Action y CLI para pruebas de regresión de los **avisos de IA y de C2PA** (art. 50) | OSS |
| [Inkog](https://github.com/inkog-io/inkog) | Escáner de seguridad de agentes (inyección de prompts, falta de supervisión humana). Mapea a los arts. 9, 14 y 15; salida SARIF y servidor MCP | OSS |
| [Human-AI Interaction Layer Reviewer](https://github.com/miguelferre/human-ai-governance) | Auditor de la capa humano-IA; mapea a los arts. 13, 14 y 86; CLI, MCP e Inspect | MIT |
| [GOPAL](https://github.com/Principled-Evolution/gopal) | Políticas OPA/Rego; 29 políticas sobre el AI Act | Apache-2.0 |
| [CorvinOS](https://github.com/CorvinLabs/CorvinOS) | Runtime de agentes con aviso de bot (art. 50) y logs encadenados por hash (art. 12) | Apache-2.0 |
| [Regulus](https://github.com/neul-labs/regulus) | Perfiles de cumplimiento en tiempo de ejecución para Google ADK (arts. 9, 10 y 50) | OSS |
| [Venturalitica SDK](https://github.com/Venturalitica/venturalitica-sdk) | Evidencias: OSCAL, CycloneDX ML-BOM, auditorías de sesgo y anexo IV | OSS |
| [COMPL-AI](https://github.com/compl-ai/compl-ai) | Evaluación de LLM con más de 29 benchmarks mapeados al AI Act (ETH Zúrich, INSAIT, LatticeFlow) | OSS |
| [VerifyWise](https://github.com/verifywise-ai/verifywise) | Plataforma de gobernanza autoalojada | OSS |
| [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit) | Políticas y *sandboxing* de agentes | MIT |

**Pruebas y evidencias (open source):**

- Pruebas, *red teaming* y monitorización: Giskard, DeepEval, PyRIT, Inspect AI y Evidently.
- Formatos de evidencias:
  - [CycloneDX ML-BOM](https://cyclonedx.org/capabilities/mlbom/) (anexo IV.2);
  - [Croissant](https://github.com/mlcommons/croissant) (datos, art. 10);
  - Model Card Toolkit;
  - OSCAL;
  - [AKF](https://github.com/HMAKT99/AKF).

**Normas armonizadas (CEN-CENELEC JTC 21), según la lista (no verificado en origen):**

- **EN 18286 (SGC)** está publicada desde julio de 2026, pero **no está citada en el DOUE**, así que todavía no da presunción de conformidad (art. 40).
- Están en curso:
  - prEN 18228 (riesgos, art. 9);
  - prEN 18282 (ciberseguridad, art. 15);
  - prEN 18229-1 (logging, art. 12);
  - prEN 18229-3 (supervisión humana, art. 14);
  - prEN 18283 (sesgo) y prEN 18284 (datos), ambas para el art. 10.

**Documentos oficiales descubiertos a través de la lista y verificados en origen en esta sesión:**

- las directrices de definición, de prácticas prohibidas y de GPAI;
- el código de transparencia;
- las guías de AESIA y el checklist;
- la URL ELI del Omnibus.

La lista también enlaza el **ALTAI** (autoevaluación de la Comisión, 2020) y recursos de la **AEPD**, que no se verificaron.

---

## 18. Implicaciones para el plugin (INFERENCIA, no texto legal)

> **Esto es inferencia propia, no texto legal.** Las señales siguientes son heurísticas para **sospechar** un riesgo y hacer preguntas. Ninguna determina por sí sola la calificación jurídica. Cada señal se vincula al artículo que la justifica. El plugin debería pedir siempre al usuario la **finalidad prevista** (art. 3.12) y el **rol** (proveedor o responsable del despliegue, art. 3.3-3.4), porque casi todas las obligaciones dependen de ellos.

### 18.1 Preguntas de triaje que el plugin debería hacer

1. ¿El componente **infiere** (ML, LLM, sistema de conocimiento) o aplica reglas fijas, consultas o estadística simple? (art. 3.1; directrices de definición, párr. 41-51)
2. ¿Vas a ponerlo en el mercado o en servicio con **tu nombre**, o lo usas internamente? ¿Modificas o cambias la finalidad de un sistema ajeno? (arts. 3.3, 3.4 y 25)
3. ¿La salida se usa en la UE o afecta a personas en la UE? (art. 2.1.c y g)
4. ¿Es solo I+D, uso militar o uso personal? ¿Es open source, no de alto riesgo y no del art. 50? (art. 2.3, 2.6, 2.8, 2.10 y 2.12)
5. ¿Toma o apoya **decisiones sobre personas** en alguna de las 8 áreas del anexo III? ¿Hace **perfilado**? (art. 6.2-6.3)
6. ¿Es un componente de seguridad de un producto regulado (anexo I) que requiere un organismo notificado? (art. 6.1-6.1 quater)
7. ¿Habla con personas o genera contenido (texto, imagen, audio o vídeo)? (art. 50)
8. ¿Entrenas o modificas un modelo general? ¿Cuánto cómputo empleas? (arts. 3.63, 51 y 53; directrices GPAI)
9. ¿Tu empresa es pyme o SMC? Eso cambia la documentación, el SGC y las multas (arts. 11.1, 17.2, 63 y 99.6-6 bis).

### 18.2 Señales en código, configuración o descripción del caso de uso

| Señal detectable (ejemplos de patrones) | Riesgo sospechado | Artículos | Severidad sugerida |
|---|---|---|---|
| `face_recognition`, `insightface`, `deepface`, `facenet`, búsqueda 1:N en una galería de embeddings faciales con cámaras o streams en espacios públicos | Identificación biométrica remota; en tiempo real y con fines policiales puede estar **prohibida** | art. 5.1.h; anexo III.1.a; art. 14.5; art. 12.3; art. 26.10 | Crítica o alta |
| Scrapers (`requests`, `scrapy`, `playwright`) que descargan imágenes de rostros de la web o de CCTV para construir o ampliar un índice facial | **Prohibido**: extracción no selectiva | art. 5.1.e | Crítica |
| Modelos de **emoción** o afecto (FER, `emotion`, `sentiment` sobre cara o voz) usados con empleados, en call centers sobre el agente o con estudiantes | **Prohibido** salvo motivos médicos o de seguridad. Fuera del trabajo y de la educación es alto riesgo más el aviso del art. 50.3 | art. 5.1.f; anexo III.1.c; art. 50.3; art. 3.39 (debe basarse en **datos biométricos**: el sentimiento de un texto no encaja en la definición, según el art. 3.39) | Crítica o alta |
| Inferir raza, religión, orientación sexual, afiliación política o sindical a partir de la cara, la voz o la marcha | **Prohibido** (categorización biométrica) | art. 5.1.g; anexo III.1.b | Crítica |
| Puntuaciones agregadas de "confianza" o "reputación" de ciudadanos o usuarios que se usan para limitar el acceso en otros contextos | Puntuación social **prohibida** | art. 5.1.c | Crítica |
| Puntuación de "riesgo de delinquir" basada solo en rasgos o perfil | **Prohibido** | art. 5.1.d; anexo III.6.d | Crítica |
| Patrones persuasivos personalizados según vulnerabilidad (edad, adicción, deuda), urgencia artificial o mensajes subliminales | Manipulación o explotación **prohibida** | art. 5.1.a-b | Alta (requiere valorar el perjuicio) |
| Generación de imágenes o vídeo de personas reales con funciones de "desnudar", *face-swap* sexual o sin filtros NSFW ni de identidad; prompts con nombres reales | **Prohibido a partir del 2-12-2026** si es la finalidad o un resultado previsible y reproducible **sin salvaguardias técnicas** | art. 5.1.b bis, 5.1 bis y 5.1 ter | Crítica |
| Generación sin clasificador o filtro de material de abuso sexual infantil | **Prohibido a partir del 2-12-2026** | art. 5.1.b ter | Crítica |
| Cribado de CV, ranking de candidatos, anuncios de empleo dirigidos, evaluación del rendimiento, asignación de turnos por comportamiento, monitorización de empleados | Alto riesgo (anexo III.4); posible FRIA; informar a los trabajadores | anexo III.4; arts. 26.7 y 26.11 | Alta (a partir del 2-12-2027) |
| *Credit scoring*, PD o *scorecards* de solvencia de personas físicas; *pricing* o riesgo en **seguros de vida y salud** | Alto riesgo; FRIA obligatoria | anexo III.5.b-c; art. 27 | Alta |
| Detección de **fraude** financiero | **Excluida** del anexo III.5.b. Normalmente no es alto riesgo por ese punto | anexo III.5.b | Informativa |
| Admisión, calificación automática de exámenes, *proctoring* o detección de copia | Alto riesgo | anexo III.3.a-d | Alta |
| Elegibilidad para prestaciones públicas o sanitarias; triaje de emergencias o del 112 | Alto riesgo | anexo III.5.a y 5.d | Alta |
| Control de red eléctrica, agua, gas, tráfico o infraestructura digital crítica como componente de seguridad | Alto riesgo; registro nacional | anexo III.2; art. 49.5 | Alta |
| Asistencia a jueces o en resolución alternativa de litigios; microsegmentación electoral o persuasión de voto | Alto riesgo | anexo III.8 | Alta |
| Uso policial, de fronteras o de asilo: polígrafo, evaluación de riesgo de personas, fiabilidad de pruebas | Alto riesgo; registro no público | anexo III.6-7; art. 49.4 | Alta |
| Indicios de perfilado: *features* de comportamiento individual que predicen preferencias, fiabilidad o rendimiento de una persona dentro de un caso del anexo III | **Anula la excepción del art. 6.3** | art. 6.3, último párrafo | Alta |
| Un producto sanitario, juguete, ascensor, EPI o radio con IA en una función de seguridad | Alto riesgo del anexo I (a partir del 2-08-2028); comprobar el art. 6.1 bis a 1 quater | art. 6.1; anexo I | Alta |
| Chatbot o agente (SDK de LLM, *widgets* de chat, voz o TTS, avatares) **sin** aviso visible de IA en la UI o en el primer turno | Incumplimiento del art. 50.1 (**ya aplicable**) | art. 50.1 y 50.5; directrices art. 50, párr. 30-40 | Alta |
| Agentes que envían correos, llaman o actúan ante terceros sin identificarse como IA ni decir en nombre de quién actúan | Art. 50.1 | directrices art. 50, párr. 31 | Alta |
| Generación de imagen, audio, vídeo o texto **sin** marca de agua, metadatos C2PA o IPTC, firma o *fingerprint* y sin forma de detectarla | Incumplimiento del art. 50.2 (**ya aplicable**; desde el 2-12-2026 para sistemas anteriores al 2-08-2026) | art. 50.2; art. 111.4; directrices, párr. 69-76 | Alta |
| Salidas que son código, JSON, SQL, etiquetas cortas o máquina a máquina | **Fuera** del marcado del art. 50.2 | directrices art. 50, párr. 64-68 | Informativa |
| *Pipeline* de *deepfakes*: clonación de voz, *face-swap* o avatar de persona real publicado sin etiqueta visible | Art. 50.4 (responsable del despliegue). El marcado técnico no basta | art. 50.4; directrices, párr. 113-117 | Alta |
| Publicación automática de noticias o textos de interés público generados sin revisión editorial | Art. 50.4, segundo párrafo | art. 50.4 | Media o alta |
| Reconocimiento de emociones o categorización biométrica **sin** aviso a las personas expuestas | Art. 50.3 | art. 50.3; directrices, párr. 99-108 | Alta |
| Entrenamiento o *fine-tuning* de modelos: estimar FLOP (≈ 6 · parámetros · tokens, heurística común **no oficial**). Más de 10^23 FLOP con capacidad generativa sugiere un modelo GPAI. Más de 10^25 FLOP hace presumir riesgo sistémico: **notificar en 2 semanas** | Obligaciones de los arts. 53-55 | art. 51.2; art. 52.1; directrices GPAI, párr. 17 y 63 | Alta o crítica |
| *Fine-tuning* de un modelo ajeno con más de 1/3 de su cómputo original | Pasas a ser proveedor del modelo GPAI | directrices GPAI, párr. 63-64 | Alta |
| Datos de entrenamiento obtenidos con *scraping* sin comprobar `robots.txt` o TDM *opt-out*; sin resumen público del contenido de entrenamiento | Política de derechos de autor y resumen (art. 53.1.c-d), **también para open source** | art. 53.1.c-d; art. 53.2 | Alta |
| Publicación de pesos con licencias "open" restringidas (no comercial, umbral de usuarios) | La excepción open source no se aplica | art. 53.2; directrices GPAI, párr. 83-86 | Media |
| En un sistema de alto riesgo: **ausencia de logging** automático de eventos, sin retención de al menos 6 meses | Arts. 12 y 26.6 | arts. 12 y 26.6 | Alta |
| Sin mecanismo de *override*, desactivación o parada, sin umbral de confianza ni revisión humana | Art. 14.4.d-e | art. 14 | Alta |
| Sin evaluación de sesgo por grupos ni métricas con umbrales predefinidos antes del lanzamiento | Arts. 9.8, 10.2.f-g y 15.3 | arts. 9, 10 y 15 | Alta |
| Uso de atributos sensibles (etnia, salud, etc.) para medir sesgos | Permitido solo con las 6 condiciones del art. 4 bis: seudonimización, acceso registrado, borrado y justificación | art. 4 bis | Media |
| Sin defensas frente a *prompt injection*, *data poisoning* o ataques adversarios | Art. 15.5. Posible presunción si se cumple la Ley de Ciberresiliencia (art. 42.3) | arts. 15.5 y 42.3 | Media o alta |
| Sin ficha o documentación del modelo (finalidad, datos, métricas, limitaciones) | Arts. 11 y 13; anexo IV. Una pyme o SMC puede usar el formulario simplificado | arts. 11 y 13; anexo IV | Media (alto riesgo) |
| Equipos que usan IA sin formación ni política interna | Art. 4: tomar medidas de apoyo a la alfabetización. **Ya aplicable**, pero en su versión menos exigente | art. 4 | Baja |

### 18.3 Lógica de fechas que el plugin debe incluir

- `hoy >= 2025-02-02`: art. 5.1.a-h.
- `>= 2025-08-02`: GPAI.
- `>= 2026-08-02`: art. 50 y multas a GPAI.
- `>= 2026-12-02`: art. 5.1.b bis y b ter, y art. 50.2 para sistemas anteriores al 2-08-2026.
- `>= 2027-12-02`: alto riesgo del anexo III.
- `>= 2028-08-02`: alto riesgo del anexo I.

El plugin debería mostrar **"aplicable ya"** o **"aplicable desde AAAA-MM-DD"** en cada hallazgo, según el art. 113 y el art. 111.

### 18.4 Recomendaciones de diseño (inferencia)

- Separar el **triaje de clasificación** (preguntas) del **escaneo técnico** (patrones de código). Muchas obligaciones dependen de la finalidad y no se pueden deducir solo del código.
- Generar la salida en el formato de los **checklists de AESIA**, con niveles L1-L8, y como **SARIF** para la integración continua, igual que hacen Inkog y Regula.
- Versionar la base normativa (consolidado del 27-07-2026) y marcar los criterios que proceden de **directrices no vinculantes** o de **borradores**, como las directrices del art. 6.

---

## 19. Fuentes consultadas

Todas se consultaron el **17-11-2026**.

**Fuentes primarias (texto legal):**

1. Reglamento (UE) 2024/1689, consolidado a 27-07-2026. ELI facilitado por el usuario: https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng. *Solo devolvió metadatos.*
2. AI Act Service Desk / AI Act Explorer (Comisión Europea), consolidado "as at 27 July 2026" con marcas NEW, AMENDED y DELETED: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-{2,3,4,4a,5,6,9,10,11,12,13,14,15,16,17,25,26,27,28,42,43,49,50,51,52,53,54,55,56,57,58,59,60,60a,62,63,69,72,73,74,75,75a,77,96,99,100,101,111,113}, y https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-{1,3,4,8,11,12,13}
3. Reglamento (UE) 2026/1744, EUR-Lex ES HTML: https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32026R1744. Se leyeron los considerandos 1-47 y el art. 1 hasta el punto 7, con el texto truncado.
4. Reglamento (UE) 2026/1744, EUR-Lex ES PDF: https://eur-lex.europa.eu/legal-content/ES/TXT/PDF/?uri=CELEX:32026R1744. Se leyó hasta el art. 1 punto 10.
5. PE-CONS 30/1/26 REV 1 (texto final del Parlamento y el Consejo): https://data.consilium.europa.eu/doc/document/PE-30-2026-REV-1/en/pdf. Se leyó hasta el art. 1 punto 32.
6. URL facilitada por el usuario https://eur-lex.europa.eu/legal-content/EN-ES/TXT/?uri=CELEX%3A32026R1744: **bloqueada** (robots). La versión EN HTML devolvió una página vacía del DOUE.
7. Real Decreto 817/2023 (BOE): https://www.boe.es/buscar/act.php?id=BOE-A-2023-22767

**Fuentes oficiales complementarias (Comisión):**

8. FAQ del AI Act Service Desk (Digital Omnibus): https://ai-act-service-desk.ec.europa.eu/en/faq
9. Cronograma: https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act
10. Las directrices y códigos de la sección 16, con sus URL.
11. Guidelines for GPAI providers (resumen): https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers

**AESIA:**

12. https://aesia.digital.gob.es/ · https://aesia.digital.gob.es/es/guias · https://aesia.digital.gob.es/es/recursos (y `?page=2`) · https://aesia.digital.gob.es/es/divulgacion · https://aesia.digital.gob.es/es/el-laboratorio · https://aesia.digital.gob.es/es/publicaciones (en construcción) · guía 16 (PDF) · noticia del 12-11-2026: https://aesia.digital.gob.es/es/actualidad/20261112-la-comision-europea-establece-normas-comunes-para-el-desarrollo-de-los-espacios-controlados · https://aesia.digital.gob.es/es/actualidad/recursos/ria-sistemas-de-alto-riesgo

**Lista de la comunidad (no primaria):**

13. awesome-eu-ai-act: https://github.com/morganrcu/awesome-eu-ai-act (README de `master`, descargado con curl desde raw.githubusercontent.com)

**Usadas solo para descubrir documentos (no se citan como fuente):** los resultados de búsqueda web de despachos y blogs sobre el Omnibus.

---

## 20. Pendiente / no verificado

> **Revisión del 17-11-2026 con los textos oficiales en español** (copias en `docs/documentos/fuentes/`, manifiesto en `docs/documentos/fuentes/README.md`). La lista de abajo se conserva como quedó al cerrar la investigación; esto es lo que ha cambiado:
>
> - **Puntos 2 y 3, resueltos.** Se leyó el consolidado en español (CELEX 02024R1689-20260727) y el texto original de 2024 (DO L de 12-07-2024). La terminología de este documento sigue ya la oficial; el art. 3.60 dice «ultrafalsificación».
> - **Punto 1, resuelto en lo que usa el plugin.** Los arts. 99, 111 y 113 y el anexo I se comprobaron en el consolidado, y el art. 4 del Reglamento 2026/1744 (entrada en vigor a los tres días de su publicación: 27-07-2026), en el Diario Oficial. El art. 3 del Reglamento 2026/1744 modifica los arts. 8, 20 y 47 del Reglamento 2023/1230; no se ha analizado más allá.
> - **Punto 5, resuelto.** En el consolidado, el art. 6.4 conserva la redacción original; el Omnibus solo añade los apartados 1 bis, 1 ter y 1 quater.
> - **Punto 7, sigue igual.** Las directrices del art. 6 siguen en borrador.
> - **Punto 8, resuelto en parte.** Las directrices de prácticas prohibidas se descargaron completas en español (C(2025) 5052 final); se comprobaron los términos y los ejemplos que usa `knowledge/`, no el resto de ejemplos de este documento.
> - **Punto 13, resuelto en parte.** Las guías 01-15 de AESIA (versión 2.0, de 17-07-2026, ya adaptadas al Reglamento 2026/1744), la guía 16 y el ZIP de checklists están descargados; no se han leído una a una.
> - **Punto 14.** El art. 43.2 del consolidado confirma el control interno del anexo VI.
>
> El estado al día de cada duda está en `docs/documentos/pendientes.md`.

1. **Texto íntegro del Reglamento 2026/1744 a partir del art. 1 punto 32 (art. 75 bis)**: arts. 77, 96, 99, 111 y 113, anexos VIII y XIV, y los **arts. 2 y 3 (modificaciones de los Reglamentos 2018/1139 y 2023/1230)**. Los cambios de los arts. 77-113 y de los anexos se verificaron **solo** con las marcas del Service Desk, y no se conoce el número de punto exacto. No se leyó el contenido de las modificaciones del Reglamento de máquinas, que es relevante para el traslado de las máquinas a la sección B del anexo I.
2. **Texto original de 2024 de los arts. 4 y 113**, para la columna "antes" del calendario. Se infiere de la FAQ del Service Desk y del considerando 8 del Omnibus. EUR-Lex y BOE se truncaron antes de llegar a los artículos.
3. **Consolidado en español**: no se pudo leer (el proxy bloqueó la descarga y el texto se truncó). Las traducciones son propias.
4. **Arts. 42 y 69 del Service Desk**: la propia página advierte de que su texto **no está actualizado**. El art. 42.3 (Ley de Ciberresiliencia) se verificó en el PE-CONS; el 69.2, solo en su descripción.
5. **Art. 6.4 y art. 49.2**: no se verificó si el Omnibus cambió también la redacción del art. 6.4. El Service Desk solo marca los apartados 1 bis a 1 quater del art. 6.
6. **Fecha del sandbox de la UE** ("from 2028", según la FAQ): no figura en el texto del art. 57.3 bis leído.
7. **Directrices de clasificación de alto riesgo (art. 6.5)**: solo hay un borrador. No se leyeron los ejemplos del Guidelines Explorer porque la página de resúmenes no los contenía.
8. **Directrices sobre prácticas prohibidas**: lectura parcial; la herramienta se cortó tras la sección 3. No se verificaron los ejemplos de las letras d), e), f) (call centers, análisis de sentimiento de texto), g) ni h).
9. **Código de buenas prácticas GPAI (julio de 2025)** y su contenido (capítulos de transparencia, derechos de autor y seguridad): no se leyó en origen.
10. **Reglamento de Ejecución (UE) 2026/2487** (sandboxes): solo se conoce por la noticia de AESIA; no se leyó en EUR-Lex.
11. **Estado actual del sandbox español** del RD 817/2023, cuya vigencia máxima de 36 meses terminaría hacia el 10-11-2026: no verificado.
12. **Normas armonizadas JTC 21** (EN 18286 y prEN): solo según la lista awesome. No se verificó en CEN-CENELEC ni en el DOUE si alguna está citada.
13. **Guías de AESIA 01-15 y ZIP de checklists**: no se abrieron una a una (solo se leyó la guía 16). La URL de la guía 01 difiere entre la lista awesome (`...-1770802981.pdf`) y la página de AESIA (`01-guia-introductoria-al-reglamento-de-ia.pdf`). Se usa la de AESIA.
14. **Discrepancia en la página de AESIA "Sistemas de alto riesgo"**: habla de autoevaluación por el "anexo VII", cuando el art. 43.2 dice control interno del anexo VI. Hay que contrastarlo.
15. **Heurística de FLOP ≈ 6·N·D**: es una convención técnica común, **no** procede de ninguna fuente oficial consultada.
16. **Herramientas de la sección 17**: no se han probado ni auditado.
