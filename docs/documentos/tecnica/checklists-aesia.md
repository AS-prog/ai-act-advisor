---
title: Cómo funcionan los checklists Excel de AESIA
description: Qué hoja rellena la persona, qué calcula solo el libro y qué produce cada uno de los 12 checklists de AESIA y el ejemplo 05.01, con sus errores y una recomendación para usarlos en el plugin.
date: 2026-11-20
status: borrador
---

# Cómo funcionan los checklists Excel de AESIA

Qué hoja rellena la persona, qué calcula solo el libro y qué produce cada
uno de los 12 checklists de AESIA y el ejemplo 05.01, con sus errores y
una recomendación para usarlos en el plugin. Responde al issue #13.

## En una frase

Cada checklist es una **autoevaluación de brecha** para un proveedor de
un sistema de alto riesgo: cruza los apartados de un artículo del RIA con
las medidas de su guía, la persona marca dificultad y madurez de cada
cruce, y el libro deduce qué falta hacer (el **Plan de Adaptación**, PDA).
No hay macros ni informes: todo son fórmulas, desplegables y hojas
ocultas.

## Fuentes

- `docs/documentos/fuentes/2026-07-30-aesia-checklists-y-ejemplos.zip`:
  12 checklists `*_Checklist.xlsx` (versión 1.0, 10-12-2025) y el
  ejemplo `05.01 Ejemplo ilustrativo del desarrollo de un sistema de
  gestión de riesgos v6.xlsx`.
- `docs/documentos/fuentes/2026-06-30-aesia-16-manual-de-checklist-de-guias-de-requisitos.pdf`
  (guía 16, versión 1.1).
- Las notas de `knowledge/notas/aesia-checklist-*` (PR #12).

El análisis abrió los Excel con openpyxl (fórmulas, estados de hoja,
validaciones) y leyó a mano el XML de cada libro para lo que openpyxl
pierde: los desplegables `x14:dataValidation`, los cuadros de texto y
las imágenes.

## El flujo

El manual lo sitúa en la **fase de diagnóstico** del sandbox español. La
entidad hace dos cosas: medir la brecha entre su sistema y el artículo, y
diseñar el PDA que ejecutará después. La hoja `Intro` es solo una imagen
con tres pasos:

1. Recorrer los apartados del artículo y autoevaluar la madurez de las
   **medidas guía** (MG) que proponen las guías.
2. Aportar **medidas adicionales** (MA) propias. La SEDIA las evalúa y,
   si valen, las incorpora a las guías.
3. Indicar a qué apartados aplica cada MA y su madurez.

En todos los pasos la entidad tiene un mentor del sandbox. Fuera del
sandbox el paso 2 no tiene quien evalúe.

## Las hojas

Todos los checklists tienen la misma estructura: 14 hojas, de las que 10
se ven y 4 están ocultas como `veryHidden` (solo se muestran desde VBA o
editando el XML). El manual habla de 9 pestañas: no cuenta `Control de
Versiones` ni las ocultas.

| Hoja | Tipo | Qué rellena la persona | Qué calcula el libro |
|---|---|---|---|
| `Portada` | informativa | nada | nada; aviso de confidencialidad del sandbox |
| `Control de Versiones` | informativa | nada | nada; versión 1.0 del 10-12-2025 |
| `Intro` | informativa | nada | nada; es una imagen con los tres pasos |
| `Artículo RIA` | informativa | nada | nada; un apartado por fila: `IDArt`, apartado, texto literal y descripción resumida |
| `Medidas guías (MG)` | informativa | nada | nada; `MGnn`, descripción y «cuestiones orientativas» |
| `Relación MG-Apart.` | informativa | nada | matriz apartado × medida con una `X` en cada cruce; los rótulos se leen de las dos hojas anteriores |
| `Autoeval MG` | operativa | dificultad y madurez de cada cruce; filas extra al final si una MG aplica a otro apartado | despliega una fila por cada `X`; rellena «Estado diagnóstico» y «Plan de adaptación» |
| `Medidas Adicionales (MA)` | operativa | descripción de cada MA y fichero donde se detalla | numera `MA01`, `MA02`…; marca si está documentada |
| `Relación MA-Apart.` | operativa | una `X` en cada cruce apartado × MA | pone los `MAnn` como cabecera |
| `Autoeval MA` | operativa | dificultad, madurez y evidencia de cada cruce | despliega una fila por cada `X`; mismos cálculos que `Autoeval MG` |
| `TO_DO` | oculta | — | lista de tareas de quienes construyeron el libro |
| `helper_flat_table` | oculta | — | despliega la matriz MG en filas (apartado, medida, `X`) |
| `helper_flat_table_MA` | oculta | — | lo mismo para la matriz MA |
| `Tablas Aux` | oculta | — | catálogos de los desplegables y tabla madurez → plan |

Las columnas que la SEDIA rellena en `Medidas Adicionales (MA)`
(«Evaluación SEDIA. Estado» y «Comentarios») y en `Autoeval MA`
(evaluación de la evidencia) solo tienen sentido dentro del sandbox.

## Las fórmulas

Son fórmulas de Excel 365: `LET`, `SEQUENCE`, `FILTER`, `HSTACK`,
`XLOOKUP`, `TEXTBEFORE` y `TEXTAFTER`, con matrices desbordadas. En Excel
2019 o LibreOffice antiguos no calculan. **No hay macros**: los libros son
`.xlsx` sin `vbaProject.bin`, sin tablas dinámicas, sin gráficos y sin
conexiones externas.

La cadena es esta:

1. `helper_flat_table!A2` toma la matriz de `Relación MG-Apart.` y la
   despliega en filas, una por cada celda con `X`:
   `FILTER(HSTACK(fila, col, val), val="X")`.
2. `Autoeval MG` lee esa tabla. `C5` y `D5` parten el texto «13.1. Diseño
   y desarrollo» en apartado y descripción (`TEXTBEFORE`/`TEXTAFTER`);
   `F5` copia el `MGnn`; `B5`, `E5` y `G5` buscan con `XLOOKUP` el
   `IDArt`, el tipo y la descripción de la medida.
3. En cada fila, dos fórmulas reaccionan a la madurez (columna I):
   - «Estado diagnóstico»:
     `=IF(I5="", '00. Pdte diagnóstico', '01. Ya diagnosticada')`.
   - «Plan de adaptación»:
     `=IF(I5<>"", VLOOKUP(I5, 'Tablas Aux'!B23:C31, 2), '00. Pdte diagnóstico')`.
4. Para las MA, `C5` numera con
   `"MA" & TEXT(COUNTIF($D$5:D5,"<>"),"00")`, `Relación MA-Apart.` pone
   esos ids como cabecera con `TRANSPOSE(FILTER(...))` y
   `helper_flat_table_MA` repite el paso 1.

La dificultad percibida (columna H) no entra en ninguna fórmula: solo se
guarda para priorizar el PDA.

### Los desplegables

openpyxl solo ve uno, la validación del formato `MAnn`. Los demás son
`x14:dataValidation` dentro de `extLst`, que openpyxl descarta al leer.
Están en el XML:

| Columna | Lista | Valores |
|---|---|---|
| Dificultad percibida | `Tablas Aux!B51:B53` | `00. Alto`, `01. Medio`, `03. Bajo` |
| Nivel de madurez | `Tablas Aux!B23:B31` | L1 a L9, abajo |
| Estado diagnóstico | `Tablas Aux!B38:B39` | `00. Pdte diagnóstico`, `01. Ya diagnosticada` |
| Evaluación SEDIA | `Tablas Aux!B46:B48` | Pendiente, OK, NO_OK |
| MA documentada | `Tablas Aux!B42:B43` | `00. Pendiente de aportar`, `01. Ya aportada` |

### Madurez y plan de adaptación

Es el corazón del libro. La tabla de `Tablas Aux` tiene **nueve** niveles;
el manual describe ocho, con otra numeración, porque no tiene «No
documentada e implementación en curso». Mando lo que dice el Excel:

| Nivel de madurez | Plan de adaptación |
|---|---|
| L1. No documentada ni implementada | 01. Documentar e implementar |
| L2. Documentación en curso y no implementada | 01. Documentar e implementar |
| L3. No documentada e implementación en curso | 01. Documentar e implementar |
| L4. Documentada y no implementada | 02. Implementar |
| L5. Documentada e implementación en curso | 02. Implementar |
| L6. Documentada e implementada | 03. Adaptación completa |
| L7. No documentada e implementada | 04. Documentar |
| L8. Documentación en curso e implementada | 04. Documentar |
| L9. Medida no necesaria en mi sistema | 05. Ninguna adaptación requerida |

La regla se reduce a dos preguntas: ¿está documentada? y ¿está
implementada? Lo que falte de las dos es el plan.

## Qué produce

Solo la propia hoja rellenada. No hay hoja de indicadores, ni de PDA, ni
botón de exportar. La hoja oculta `TO_DO` lo confirma: entre sus tareas
pendientes están «Probar la exportación a indicadores», «Probar la
exportación a PDA» e «Informe de seguimiento en base a indicadores».

- **PDA** es el **Plan de Adaptación** del manual (apartado 1.1): el plan
  de trabajo que la entidad ejecuta después para cumplir el RIA. En el
  libro es la columna «Plan de adaptación»; plazos y esfuerzos se añadían
  fuera, en la fase siguiente del sandbox.
- **Indicadores** son el «grado de avance» del diagnóstico: cuántas filas
  están en `01. Ya diagnosticada` y cómo se reparten por plan. Se
  calculaban fuera del libro, con los «automatismos desarrollados por
  Pablo» que la `TO_DO` pide integrar y que no vienen en el ZIP.

## Los 12 checklists

| Checklist | Guía | Artículo | Apartados | MG | Cruces |
|---|---|---|---|---|---|
| Gestión de calidad | 04 | 17 | 17 | 16 | 21 |
| Gestión de riesgos | 05 | 9 | 17 | 14 | 98 |
| Supervisión humana | 06 | 14 | 12 | 8 | 28 |
| Gobernanza del dato | 07 | 10 | 20 | 21 | 65 |
| Transparencia | 08 | 13 | 16 | 16 | 53 |
| Precisión | 09 | 15 | 3 | 14 | 28 |
| Solidez | 10 | 15 | 2 | 16 | 16 |
| Ciberseguridad | 11 | 15 | 2 | 11 | 11 |
| Registros | 12 | 12 y 19 | 10 | 14 | 37 |
| Vigilancia poscomercialización | 13 | 72 | 2 | 13 | 14 |
| Gestión de incidentes | 14 | 73 | 11 | 5 | 40 |
| Documentación técnica | 15 | 11, 18 y anexo IV | 36 | 45 | 99 |
| **Total** | | | **148** | **193** | **510** |

«Cruces» son las `X` de `Relación MG-Apart.`, es decir, las filas que
aparecen en `Autoeval MG`. Algunas MG remiten a otro checklist en vez de
describir una medida: en Transparencia, MG13 a MG16 son «Artículo 09»,
«Artículo 14», «Artículo 15» y «Artículo 12»; en Gestión de calidad,
MG04 y MG09 a MG12 remiten a los artículos 15, 10, 9, 72 y 73. Forman un
grafo entre checklists.

## El ejemplo 05.01

No es un checklist. Es el anexo de la guía 05 (sistema de gestión de
riesgos, art. 9): recorre los pasos de su sección 2 con dos casos de uso,
un sistema de promoción de empleados y una bomba de insulina inteligente.
Cada hoja lleva un cuadro de texto con la explicación.

| Hoja | Qué contiene |
|---|---|
| `Leyenda` | escalas de impacto (1-5, con columnas de seguridad, derechos fundamentales y salud) y de probabilidad (1-5, con frecuencia esperada) |
| `0.Sistemas IA en análisis` | los dos casos de uso |
| `1.Definición apetito al riesgo` | solo texto: apetito de 4 sobre 15 |
| `2.Contexto de la organización` | elementos de salud, seguridad y derechos fundamentales por sistema |
| `3.Identificación de riesgos` | componente, categoría (datos, actores, entornos), amenaza y riesgo |
| `4.Análisis y eval. de riesgos` | impacto, probabilidad, `riesgo inherente = impacto × probabilidad`, apetito y conclusión |
| `5.Respuesta al riesgo` | control, mitigación (0 a 0,8) y `riesgo residual = inherente − inherente × mitigación` |

Hay tres hojas ocultas: versiones anteriores de las hojas 2 y 3 y un
control de cambios (V1 de 2022-12-28, V2 de 2023-03-28). Las únicas
fórmulas son las dos multiplicaciones; la conclusión de la hoja 4
(«R.Inherente > Apetito») está escrita a mano.

Lo útil para el plugin: el patrón **componente de datos → amenaza →
riesgo → control** está pensado para quien construye el sistema. Varias
amenazas son de ingeniería de datos: envenenamiento de los datos de
entrenamiento, perfilado por el etiquetado, sesgo en los datos, revelación
de datos y procesos no reproducibles.

## Errores e incoherencias

Ninguno impide usar el contenido, pero hay que saberlos antes de
reutilizarlo:

1. **El art. 10.5 ya no existe.** El checklist de Gobernanza del dato
   evalúa los apartados 10.5.a a 10.5.f (categorías especiales para
   corregir sesgos). El Reglamento 2026/1744 suprimió el art. 10.5 y lo
   llevó al nuevo **art. 4 bis**; el nuevo 10.6 remite a él. Los
   checklists son de 2025-12-10 y el manual avisa de que se actualizarán
   tras el Omnibus. También cambian, sin invalidar las medidas, el art. 11
   (documentación simplificada para pymes y pequeñas mid-caps), el 17.2
   (proporcionalidad) y el 72.3 (modelo de plan de la Comisión).
2. **Manual y Excel no coinciden** en la escala de madurez (8 niveles
   frente a 9) ni en la dificultad (`02. Bajo` frente a `03. Bajo`).
3. **Cabeceras rotas en `Autoeval MA`.** Las columnas L a P muestran
   `#REF!`: apuntan a una columna borrada de `Autoeval MG`. Por los
   desplegables, son el fichero de evidencia, si está aportada y la
   evaluación de la SEDIA.
4. **`IDArt` mal en Vigilancia poscomercialización**: pone `AR73` para
   los apartados 72.2 y 72.3.
5. **Apartado repetido en Registros**: «12.3» aparece dos veces.
6. **`VLOOKUP` sin coincidencia exacta** en el plan de adaptación.
   Funciona porque L1…L9 están ordenados; con un L10 fallaría.
7. **El ejemplo 05.01 contradice su escala.** El texto habla de impacto
   1-5, probabilidad 1-3 y apetito 4 sobre 15; la `Leyenda` usa 1-5 para
   las dos, y el apetito de la bomba de insulina es 5.
8. **Enlace privado.** La plantilla para documentar una MA apunta al
   SharePoint del sandbox (`DIGITAL-SANDBOXIA`), al que no se puede
   acceder.

## Qué recuperan las notas y qué pierden

Las notas de la PR #12 guardan el valor calculado que Excel dejó en
caché, no la fórmula. Para las hojas informativas basta. En las demás:

- `Autoeval MG` sí trae sus filas, porque la caché tiene la matriz
  desbordada. En Documentación técnica faltan 2 de 99 cruces (anexo IV.8
  con MG44 y IV.9 con MG45) y `IDArt` sale vacío.
- `Autoeval MA` y `Relación MA-Apart.` salen casi vacías porque el libro
  llega sin MA: son filas con los valores por defecto
  («00. Pdte diagnóstico», «00. Pendiente de aportar»).
- Las hojas `helper_*` no tienen nota, y no hace falta: repiten
  `Relación MG-Apart.` en filas.
- Se pierden las listas de los desplegables y la regla madurez → plan,
  aunque `Tablas Aux` conserva la tabla.

## Recomendación

Los checklists están hechos para **proveedores de sistemas de alto
riesgo** que preparan una evaluación de conformidad, con plazos de
2027-12-02 (anexo III) y 2028-08-02 (anexo I). La mayoría de proyectos de
un DE o un AE no lo son. Por eso propongo usarlos como **catálogo de
medidas**, no como formulario:

1. **Las notas bastan para citar.** `cite-regulation` y el buscador ya
   encuentran una medida y sus cuestiones orientativas. No hace falta
   rehacerlas; solo marcar en su front matter que el art. 10.5 es ahora
   el art. 4 bis.
2. **Un catálogo estructurado para sugerir.** Un script stdlib que lea
   los 12 Excel y escriba `knowledge/aesia-measures.yaml` con, por
   checklist: artículo, apartados, medidas (`id`, descripción,
   cuestiones orientativas), cruces apartado → medidas y remisiones entre
   checklists. Con eso una skill puede pasar de una señal a medidas
   concretas sin buscar. Ejemplo: una columna de categoría especial
   (`special_category_terms`) → art. 10.2.f-g y art. 4 bis → MG14 a MG16
   (sesgo) y MG19 a MG21 (anonimización, seudonimización, garantías RGPD)
   de Gobernanza del dato. El mapa señal → medida se cura a mano, como
   `citas.yaml`.
3. **Las cuestiones orientativas como preguntas, no como examen.** Encajan
   con el enfoque del plugin: la skill las propone, explica el riesgo de
   no tenerlas y la decisión es de la persona. Nunca bloquean.
4. **La escala de madurez, opcional.** Si alguien quiere el diagnóstico
   completo, una skill puede preguntar por documentada/implementada y
   devolver el plan con la regla de arriba, en Markdown o CSV. No vale la
   pena generar el Excel: depende de Excel 365 y de una SEDIA que evalúe
   las MA.
5. **El patrón del ejemplo 05.01** sirve para `risk-summary`: componente
   de datos → amenaza → control, con las escalas de su `Leyenda`.

El primer paso concreto sería el punto 2 limitado a **Gobernanza del
dato** y **Registros**, que son los dos checklists más cercanos al
trabajo de un DE o un AE (calidad, linaje, sesgo, retención y logs).

## Decisiones que quedan abiertas

Cada una tiene su issue:

- Si se genera `knowledge/aesia-measures.yaml` y con qué esquema.
- Cómo se mapean las señales del plugin a las medidas, empezando por
  Gobernanza del dato y Registros.
- Si el plugin ofrece una autoevaluación guiada con la escala de madurez
  y el plan de adaptación.

## Cómo se comprueba

Los números de este documento salen de leer los Excel del ZIP con
`openpyxl` y del XML de cada libro. Para repetirlo: descomprimir el ZIP,
abrir cada `*_Checklist.xlsx` con `openpyxl.load_workbook(...)` (sin
`data_only`) y contar las `X` de `Relación MG-Apart.`; los desplegables
están en `xl/worksheets/sheetN.xml`, bajo `x14:dataValidations`.

*No es asesoramiento legal. Base normativa: consolidado del AI Act de
2026-07-27.*
