---
title: Pendientes y dudas
description: Lista de dudas normativas sin confirmar, decisiones de diseño abiertas y datos ya verificados del plugin ai-act-advisor, para retomarlos sin más contexto.
date: 2026-11-17
status: vivo
---

# Pendientes y dudas

Lista de trabajo del plugin `ai-act-advisor`. Tres partes: dudas normativas que siguen abiertas (P), decisiones de diseño abiertas (D) y lo ya verificado (V), con su fuente, para no repetirlo. Las rutas son relativas a la raíz del repo; `knowledge/` es `plugins/ai-act-advisor/knowledge/` y `skills/` es `plugins/ai-act-advisor/skills/`.

## Cómo se hizo la revisión

Hubo dos pasadas el 2026-11-17.

- **Primera**: con el consolidado en inglés del AI Act Service Desk y, para el RGPD, una copia no oficial. Dejó doce dudas, P01 a P12.
- **Segunda**: con los textos oficiales, en español cuando existe. Los documentos están en `docs/fuentes/` y su manifiesto (título oficial, identificador, versión, URL de origen y sha256) en `docs/fuentes/README.md`. Cada dato de la tabla de verificado se buscó en el original; las conversiones a Markdown de `docs/fuentes/md/` solo sirvieron para localizar el pasaje.

Resultado de la segunda pasada: P01, P02, P03, P05, P06, P07, P08 y P12 están cerradas y pasan a la tabla de verificado; P09 era una decisión de diseño y ahora es D17. Siguen abiertas P04, P10 y P11, que dependen de documentos que aún no existen en versión final o de una lectura que no se ha hecho. Los identificadores no se renumeran.

## Dudas normativas que siguen abiertas

### P04 · Directrices de clasificación de alto riesgo (art. 6.5): siguen en borrador

- **Qué se afirma**: que son un borrador sin adoptar.
- **Dónde**: `knowledge/ai-act-classification.md` (final de «Excepción del art. 6.3») y `skills/ai-act-classify/SKILL.md` (límites).
- **Estado a 2026-11-17**: comprobado. Solo existe el borrador publicado el 19-05-2026 para consulta hasta el 23-07-2026, en tres PDF en inglés sin número de documento («[…](2026) XXX draft»), guardados como `docs/fuentes/2026-05-19-directrices-art6-alto-riesgo-borrador-parte{1,2,3}-en.pdf`. Ni el Service Desk ni la biblioteca de la Comisión listan una versión final.
- **Por qué sigue abierta**: el plazo legal venció el 2-02-2026 y la consulta se cerró en julio; la adopción puede llegar en cualquier momento. El borrador (167 páginas) no se ha comparado con la tabla del anexo III de `knowledge/`, porque un borrador no debe fijar criterio.
- **Qué hacer**: vigilar la adopción en cada `/regulatory-update`. Cuando se adopten, revisar con ellas la tabla del anexo III y la excepción del art. 6.3.

### P10 · Publicaciones recientes: leídas por encima, sin comparación a fondo

- **Qué se hizo**: se descargaron y se repasaron los documentos que quedaron apuntados en la primera pasada.
  - AEPD, «Sistemas algorítmicos en el ámbito laboral» (7-10-2026): llevó a añadir el Real Decreto 723/2026 a `knowledge/ai-act-classification.md` (V43).
  - AEPD, «Asistentes y agentes de IA» (27-10-2026) y «Exactitud, idoneidad y calidad de los datos» (21-07-2026): no contradicen la base; no se han incorporado.
  - CEPD, Guidelines 02/2026 (anonimización) y 03/2026 (*web scraping* en IA generativa): son la versión 1.0 para consulta pública, en inglés. `knowledge/masking-techniques.md` menciona la primera como borrador.
  - AESIA: las guías 01 a 15 ya están en su versión 2.0, de 17-07-2026, adaptadas al Reglamento 2026/1744.
- **Por qué sigue abierta**: las dos directrices del CEPD no tienen versión final y pueden cambiar; las guías de AESIA (16 PDF y un ZIP de checklists) no se han leído una a una ni se han comparado con las skills; el decálogo de agentes de la AEPD podría dar criterios para `skills/ai-transparency/SKILL.md` que no se han extraído.
- **Qué hacer**: en el próximo `/regulatory-update`, comprobar si el CEPD ha adoptado las directrices y revisar `masking-techniques.md` con la de anonimización; decidir si las guías de AESIA entran en la base (D19).

### P11 · Listados de la AEPD y del CEPD, leídos a medias

- **Estado**: de la página de guías de la AEPD solo se ha visto la primera de 14 páginas; la URL del CEPD de `knowledge/sources.yaml` muestra sobre todo consultas públicas. Por eso `aepd` y `edpb` siguen con `last_checked: null`. El resto de fuentes, incluidas las tres nuevas (`rgpd`, `lopdgdd`, `ai-act-service-desk`), están a 2026-11-17.
- **Por qué sigue abierta**: sin recorrer los listados enteros no se puede afirmar que no haya otra guía reciente que afecte a la base.
- **Qué hacer**: en el próximo `/regulatory-update`, recorrer las 14 páginas de la AEPD, comprobar que la URL del CEPD lista también las directrices adoptadas y valorar una URL de la AEPD filtrada por IA.

## Decisiones de diseño abiertas

### D01 · Q5: cuánto ruido es aceptable

- **Estado**: el hook avisa de cuatro hallazgos por fichero como máximo, una vez por sesión, y calla lo que está en la línea base (`plugins/ai-act-advisor/scripts/aiact/hooks.py`).
- **Qué decidir**: si ese límite vale tras probarlo en proyectos reales y si la búsqueda por términos, que es la parte ruidosa, sigue activa cuando el repo ya tiene reglas.

### D02 · MCP de documentación normativa (versión madura)

- **Qué decidir**: dónde corre (local o servicio), qué modelo de embeddings usa y cómo se reparte el índice con el plugin. Está como pendiente en `docs/diseno/propuesta-prototipo.md`.
- **Dato nuevo**: EUR-Lex no responde a peticiones automáticas y las herramientas de lectura cortan los textos largos. Los originales íntegros y sus conversiones a Markdown están ya en `docs/fuentes/` y `docs/fuentes/md/`, y pueden ser la materia prima del índice.

### D03 · Ruta del resumen de riesgos

- **Estado**: `skills/risk-summary/SKILL.md` guarda el resumen en `.ai-act/risk-summary.md`, solo si el PM lo pide, y lo sobrescribe. La ruta la eligió la skill; no estaba en el diseño.
- **Qué decidir**: si la ruta es esa, si conviene un resumen fechado en `.ai-act/audits/` y si el resumen debe escribirse siempre.

### D04 · Skills solo manuales

- **Estado**: las siete skills se pueden cargar solas, también `project-init`, `risk-summary` y `regulatory-update`, que en el diseño se lanzan a mano.
- **Qué decidir**: si esas tres llevan `disable-model-invocation: true`. Ahorra contexto en cada turno; a cambio, el hook `SessionStart` ya no puede hacer que Claude las cargue, solo sugerir el comando al usuario.

### D05 · Clave multi-repo del perfil

- **Estado**: `skills/project-init/SKILL.md` pide listar los repos del proyecto, pero `plugins/ai-act-advisor/examples/profile.yaml` no tiene esa clave y ningún script la lee. `risk-summary` lee «la que haya».
- **Qué decidir**: nombre y forma (por ejemplo `repos:` con `name`, `path` o `url`, y cuál es el de gestión), y añadirla al ejemplo.

### D06 · Un solo `ai_act_level` en el perfil

- **Estado**: el alto riesgo y el art. 50 se acumulan (art. 50.6), pero el perfil guarda un nivel. `ai-act-classify` escribe el más grave y deja la transparencia en el aviso.
- **Qué decidir**: si el perfil pasa a una lista o añade un campo `transparency: true`, y cómo lo enseña el hook `SessionStart`.

### D07 · Señal para proxies

- **Estado**: `knowledge/signals.yaml` no tiene términos de proxy; la skill los busca leyendo el esquema.
- **Qué decidir**: si se añade una lista `proxy_terms` (código postal, nacionalidad, bajas…) y con qué severidad, sabiendo que `codigo_postal` y `postal_code` ya están en `pii_terms`. La duda P08 ya está cerrada (V40): el criterio del TJUE es amplio, así que la lista sería larga.

### D08 · `scoring-model` en el hook

- **Estado**: el hallazgo solo lo emite la auditoría completa (`core.audit`); el hook `PostToolUse` no lo comprueba, así que un modelo nuevo no avisa hasta relanzar `/project-init`.
- **Qué decidir**: si el hook debe comprobar ML más términos de scoring en el fichero editado.

### D09 · Tarea semanal sin programar

- **Estado**: el diseño (Q13) pide una tarea semanal que abra una PR; el plugin no la trae. La alerta de 90 días del `SessionStart` sí existe.
- **Qué decidir**: dónde se programa (tarea programada de Claude Code o CI del repo) y con qué permisos para abrir la PR.

### D10 · Quién decide y cuándo, en la línea base

- **Estado**: `.ai-act/baseline.json` guarda `status` y `justification` en texto libre, sin autor ni fecha de la decisión.
- **Qué decidir**: si se añaden `decided_by` y `decided_on`, y que `merge_baseline` de `core.py` los conserve.

### D11 · Fechas y artículos escritos fuera de `knowledge/`

- **Estado**: el campo `aplica` de los hallazgos está escrito en `core.py` («ya (desde 2026-08-02)», «desde 2027-12-02») y `skills/project-init/SKILL.md` repite tres fechas. `AGENTS.md` pide que una fecha se cambie solo en `knowledge/`.
- **Además**: el hallazgo `llm-sdk` dice que el art. 50 aplica ya, sin distinguir el marcado del 50.2 para sistemas anteriores al 2026-08-02, exigible desde 2026-12-02.
- **Qué decidir**: si `core.py` calcula `aplica` con `dates.yaml` y la fecha del día.

### D12 · Cuándo se sube `ultima_revision`

- **Estado**: `skills/regulatory-update/SKILL.md` solo la sube si se leyeron todas las fuentes. EUR-Lex suele devolver textos cortados, así que la alerta de 90 días podría no apagarse nunca.
- **Qué decidir**: si basta con leer el índice de cada fuente. `knowledge/sources.yaml` incluye ya el AI Act Service Desk y la dirección de la Oficina de Publicaciones (`publications.europa.eu/resource/celex/<CELEX>`), que sí devuelve el texto íntegro.

### D13 · Fuentes que el plugin cita y no vigila

- **Estado**: resuelto en parte. `knowledge/sources.yaml` incluye ya el RGPD, la LOPDGDD y el AI Act Service Desk, y el agente `regulatory-watcher` acepta `publications.europa.eu`, `curia.europa.eu` y `commission.europa.eu`.
- **Qué decidir**: si el vigilante debe seguir también la jurisprudencia del TJUE (hoy se cita una sentencia, C-184/20) y con qué URL.

### D14 · Datos penales dentro de «categorías especiales»

- **Estado**: `special_category_terms` incluye `antecedentes_penales` y `criminal_record`, y el hallazgo cita solo el art. 9 RGPD. Esos datos van por el art. 10 RGPD y el art. 10 LOPDGDD.
- **Qué decidir**: si se separan en un hallazgo propio o si el hallazgo cita los dos artículos.

### D15 · Adaptadores por stack

- **Estado**: `plugins/ai-act-advisor/adapters/` solo tiene un README que dice «Pendiente Q16», mientras la tabla de decisiones da Q16 por cerrada (sin stack fijo). Las skills usan `knowledge/masking-techniques.md` para los ejemplos por stack.
- **Qué decidir**: si los adaptadores siguen en el diseño o se retira la carpeta.

### D16 · Redacción de «nunca bloquea»

- **Estado**: las cinco skills nuevas lo dicen en positivo («explica, propone y deja la decisión»); `project-init` y `pii-masking` conservan «Nunca bloquea».
- **Qué decidir**: si se unifican.

### D17 · Alcance resumido en `dates.yaml`

- **Estado**: las fechas son correctas (V02 a V08), pero el alcance está resumido: pone «arts. 51-55» desde 2025-08-02 y «arts. 6-27» desde 2027-12-02. El art. 113.b habla del capítulo V entero (arts. 51-56) y también del capítulo III sección 4, el capítulo VII, el capítulo XII salvo el art. 101 y el art. 78; el art. 113.c excluye el art. 6.5 del aplazamiento. Antes era la duda P09; el texto literal del art. 113 está comprobado.
- **Qué decidir**: si `dates.yaml` refleja el alcance completo. Si se cambia, revisar el hook `SessionStart` y las skills que lo leen.

### D18 · Normas nacionales fuera del AI Act y del RGPD

- **Estado**: `knowledge/ai-act-classification.md` menciona el Real Decreto 723/2026 (información a la persona trabajadora sobre sistemas algorítmicos) como nota del área de empleo. Ninguna señal ni hallazgo lo usa, y `knowledge/sources.yaml` no vigila normas laborales.
- **Qué decidir**: si el plugin cubre normas nacionales sectoriales (laboral, consumo, seguros) o se queda en el AI Act, el RGPD y la LOPDGDD, con notas sueltas como esta.

### D19 · Mantenimiento de `docs/fuentes/`

- **Estado**: la carpeta guarda 37 documentos oficiales (38 MB) y cinco derivadas, con manifiesto. `skills/regulatory-update/SKILL.md` no dice nada de ella.
- **Qué decidir**: si cada `/regulatory-update` añade a `docs/fuentes/` los documentos que lee y actualiza el manifiesto; si las versiones antiguas se conservan; y si las guías de AESIA, que hoy solo están archivadas, pasan a ser referencia de alguna skill.

## Verificado

Todo comprobado el 2026-11-17 en el documento oficial que se indica. Los ficheros están en `docs/fuentes/`; la columna de fuente da el identificador y, la primera vez que aparece, el nombre del fichero. Abreviaturas:

- **AIA**: AI Act consolidado en español, CELEX 02024R1689-20260727, `2026-07-27-ai-act-2024-1689-consolidado-es.xhtml`.
- **OMN**: Reglamento (UE) 2026/1744, CELEX 32026R1744, `2026-07-24-omnibus-2026-1744-es.xhtml`.
- **RGPD**: consolidado en español, CELEX 02016R0679-20160504, `2016-05-04-rgpd-2016-679-consolidado-es.xhtml`.
- **LOPDGDD**: texto consolidado del BOE, BOE-A-2018-16673, última modificación BOE-A-2025-26698 (27-12-2025), `2025-12-27-lopdgdd-3-2018-consolidado-boe.pdf`.
- **D50**: Directrices del art. 50, C(2026) 7702 final, de 5-11-2026, `2026-11-05-directrices-art50-transparencia-c2026-7702-es.pdf`.
- **DPP**: Directrices de prácticas prohibidas, C(2025) 5052 final, de 29-07-2025, `2025-07-29-directrices-practicas-prohibidas-c2025-5052-es.pdf`.
- **DDEF**: Directrices de definición de sistema de IA, C(2025) 5053 final, de 29-07-2025, `2025-07-29-directrices-definicion-sistema-ia-c2025-5053-es.pdf`.

| Id | Qué | Dónde está en el repo | Fuente |
|---|---|---|---|
| V01 | Consolidado de 27-07-2026 (versión 001.001, incorpora el Reglamento 2026/1744); el 2026/1744 es de 8-07-2026, publicado en el DO L el 24-07-2026, y modifica los Reglamentos 2024/1689, 2018/1139 y 2023/1230 | `knowledge/VERSION` | AIA; OMN |
| V02 | Capítulos I y II (art. 4 y art. 5.1.a-h) desde 2025-02-02 | `knowledge/dates.yaml`, `skills/project-init` | AIA art. 113.a |
| V03 | Capítulo V (GPAI) desde 2025-08-02 | `knowledge/dates.yaml` | AIA art. 113.b |
| V04 | Fecha general 2026-08-02, que incluye el art. 50 y el art. 101 | `knowledge/dates.yaml`, `core.py` (`llm-sdk`), `skills/project-init` | AIA art. 113 |
| V05 | Art. 5.1.b bis, 5.1.b ter, 5.1 bis y 5.1 ter desde 2026-12-02 | `knowledge/dates.yaml` | AIA art. 113.a |
| V06 | Art. 50.2 exigible desde 2026-12-02 a sistemas comercializados antes del 2026-08-02 | `knowledge/dates.yaml`, `knowledge/transparency-art50.md`, `skills/ai-transparency` | AIA art. 111.4 |
| V07 | Alto riesgo del anexo III (cap. III, secc. 1-3) desde 2027-12-02 | `knowledge/dates.yaml`, `core.py` (`scoring-model`), `skills/project-init` | AIA art. 113.c.i |
| V08 | Alto riesgo del anexo I (art. 6.1) desde 2028-08-02 | `knowledge/dates.yaml` | AIA art. 113.c.ii |
| V09 | Ámbito y exclusiones: art. 2.1.c, 2.1.g, 2.3, 2.6, 2.8 y 2.10 | `knowledge/ai-act-classification.md` | AIA art. 2 |
| V10 | Definiciones: art. 3.1, 3.3, 3.4, 3.12, 3.39 (exige datos biométricos), 3.40, 3.52, 3.60 y 3.63 | `knowledge/ai-act-classification.md`, `skills/ai-act-classify` | AIA art. 3 |
| V11 | Art. 4: medidas de apoyo a la alfabetización, sin nivel garantizado | `knowledge/ai-act-classification.md` | AIA art. 4 |
| V12 | Art. 4 bis: seis condiciones (a-f), alcance del apartado 2 y ausencia de obligación de detectar sesgos | `knowledge/special-categories.md`, `skills/special-categories` | AIA art. 4 bis |
| V13 | Art. 5.1, letras a, b, b bis, b ter, c, d, e, f, g y h, con sus excepciones; 5.1 bis y 5.1 ter; 5.2-5.7 | `knowledge/ai-act-classification.md` | AIA art. 5 |
| V14 | Art. 6.1, 6.1 bis-quater, 6.2, 6.3 (cuatro condiciones y elaboración de perfiles), 6.4 con el registro del 49.2, y 6.5. El art. 6.4 conserva su redacción de 2024 | `knowledge/ai-act-classification.md`, `skills/ai-act-classify` | AIA arts. 6 y 49 |
| V15 | Anexo III: las ocho áreas, sus letras y las exclusiones expresas | `knowledge/ai-act-classification.md` | AIA anexo III |
| V16 | Mapa de 17 sectores a puntos del anexo III | `knowledge/sectors.yaml` | AIA anexo III |
| V17 | Art. 25.1 (a-c), 25.2 y 25.4 | `knowledge/ai-act-classification.md` | AIA art. 25 |
| V18 | Art. 26.1, 26.2, 26.6 (seis meses como mínimo), 26.7, 26.9 y 26.11 | `knowledge/ai-act-classification.md` | AIA art. 26 |
| V19 | Art. 27: quién hace la FRIA, exclusión del anexo III.2, 27.4 y 27.5 | `knowledge/ai-act-classification.md` | AIA art. 27 |
| V20 | Art. 50.1 a 50.7: obligado, obligación y excepciones, con la redacción oficial | `knowledge/transparency-art50.md`, `skills/ai-transparency`, `core.py` | AIA art. 50 |
| V21 | Multas: art. 99.3 (35 M EUR o 7 %), 99.4 (15 M EUR o 3 %; el art. 50 es la letra g), 99.5, 99.6 y 99.6 bis | `knowledge/ai-act-classification.md`, `knowledge/transparency-art50.md` | AIA art. 99 |
| V22 | Art. 101.1: multas de la Comisión a proveedores de modelos GPAI | `knowledge/dates.yaml` | AIA art. 101 |
| V23 | Art. 111.2: sistemas ya comercializados, solo con cambios significativos de diseño | `knowledge/ai-act-classification.md` | AIA art. 111 |
| V24 | Las obligaciones del art. 53 son del proveedor del modelo GPAI | `skills/ai-transparency` (límites) | AIA art. 53 |
| V25 | Directrices del art. 50: párr. 30, 31, 37, 38, 40, 42-45, 64-68, 69-70, 72-76, 90-92, 99-108 y 113-117, con los ejemplos literales del párr. 38 | `knowledge/transparency-art50.md` | D50 |
| V26 | Código de buenas prácticas sobre transparencia del contenido generado por IA: versión final de 10-06-2026, declarado herramienta voluntaria adecuada | `knowledge/transparency-art50.md` | Página de la Comisión sobre el código (primera pasada; no hay copia en `docs/fuentes/`) |
| V27 | El contenido generado antes del 2026-08-02 no necesita etiquetado retroactivo | `knowledge/transparency-art50.md` | FAQ de la Comisión sobre el art. 50 (primera pasada; no hay copia en `docs/fuentes/`) |
| V28 | El scoring crediticio y de seguros es alto riesgo si no cumple las condiciones de la puntuación ciudadana (párr. 37) | `knowledge/ai-act-classification.md` | DPP |
| V29 | Quedan fuera de la definición: optimización matemática (párr. 42-45), procesamiento básico (46-47), heurísticas clásicas (48) y predicción simple (49-51) | `knowledge/ai-act-classification.md` | DDEF |
| V30 | RGPD considerando 26 (el dato seudonimizado sigue siendo personal) y considerando 51 (se suman las condiciones generales de licitud) | `knowledge/masking-techniques.md`, `knowledge/special-categories.md` | RGPD |
| V31 | LOPDGDD art. 9.1, 9.2 y 10.1 | `knowledge/special-categories.md` | LOPDGDD |
| V32 | RGPD arts. 4.5, 5.1.c, 5.1.e, 9.1, 9.2 (letras a-j), 10, 17, 22.4, 25, 28, 30, 32, 35.3.b, 44-49 y 89. Cierra P01 | `knowledge/special-categories.md`, `knowledge/masking-techniques.md`, `skills/pii-masking`, `skills/special-categories`, `core.py` | RGPD |
| V33 | Campos `norma`, `articulos` y `aplica` de los diez tipos de hallazgo | `plugins/ai-act-advisor/scripts/aiact/core.py` | Los de V04, V07, V20 y V32; salvedad en D11 |
| V34 | Las URL de las fuentes cargan; AESIA lista 16 guías y el compendio de checklists | `knowledge/sources.yaml` | Las propias páginas; salvedades en P11 |
| V35 | Numeración en español: «artículo 4 bis», «b bis)», «b ter)», «1 bis», «1 ter», «1 quater» y «6 bis» (art. 99). Términos oficiales: «responsable del despliegue», «ultrafalsificación» (art. 3.60), «puntuación ciudadana» (art. 5.1.c), «elaboración de perfiles» (art. 3.52), «Consejo de IA». Cierra P02 | `knowledge/` y las skills | AIA |
| V36 | Las directrices del art. 50 se adoptaron formalmente como Comunicación C(2026) 7702 final el 5-11-2026, en español; el documento de 20-07-2026, C(2026) 5054, aprobaba su contenido y tiene la misma numeración de párrafos. El párr. 5 dice que no son vinculantes. Cierra P03 | `knowledge/transparency-art50.md`, `skills/ai-transparency` (límites) | D50; C(2026) 5054 final, `2026-07-20-directrices-art50-transparencia-c2026-5054-en.pdf` |
| V37 | El Reglamento 2026/1744 entró en vigor a los tres días de su publicación en el DO (24-07-2026): el 27-07-2026. Cierra P05 | `knowledge/VERSION`, `docs/investigacion/ai-act-investigacion.md` | OMN art. 4 y considerando 46 |
| V38 | Requisitos de los sistemas de alto riesgo en los arts. 8-15; obligaciones del proveedor en los arts. 16-17; la evaluación de la conformidad es el art. 43, al que remite el art. 16.f. Cierra P06 | `knowledge/ai-act-classification.md` | AIA arts. 8-17 y 43 |
| V39 | Los Reglamentos 2017/745 y 2017/746 (productos sanitarios) están en la sección A del anexo I; la maquinaria (Reglamento 2023/1230) pasa a la sección B. Cierra P07 | `knowledge/sectors.yaml` (`healthcare`), `knowledge/dates.yaml` | AIA anexo I |
| V40 | Tratar datos que pueden desvelar indirectamente una categoría especial, por deducción o cruce, es tratar categorías especiales. La tabla de variables proxy sigue siendo heurística del plugin. Cierra P08 | `knowledge/special-categories.md`, `skills/special-categories` | TJUE, sentencia de 1-8-2022, C-184/20, apdos. 123-128 y fallo 2; CELEX 62020CJ0184, `2022-08-01-tjue-c-184-20-sentencia-es.xhtml` |
| V41 | Fechas de las directrices de 2025: las de prácticas prohibidas se publicaron el 4-02-2025 y las de definición el 6-02-2025; las dos se adoptaron el 29-07-2025. Cierra P12 | `docs/investigacion/ai-act-investigacion.md` (secciones 4.3, 6 y 16), `knowledge/ai-act-classification.md` | DPP; DDEF |
| V42 | Las directrices del art. 6 siguen en borrador a 2026-11-17 (ver P04) | `knowledge/ai-act-classification.md`, `skills/ai-act-classify` | Borrador de 19-05-2026, `2026-05-19-directrices-art6-alto-riesgo-borrador-parte1-en.pdf` y partes 2 y 3 |
| V43 | Real Decreto 723/2026, art. 3.2.k: la empresa informa por escrito de los sistemas algorítmicos o automatizados de toma de decisiones; publicado el 15-09-2026 y en vigor a los veinte días, el 5-10-2026 | `knowledge/ai-act-classification.md` | BOE-A-2026-19200, `2026-09-15-rd-723-2026-consolidado-boe.pdf` (disposición final cuarta) |

## Corregido

### Segunda pasada, con los textos oficiales

| Qué | Antes | Después | Fuente |
|---|---|---|---|
| Referencia de las directrices del art. 50, `knowledge/transparency-art50.md` e investigación | C(2026) 5054, de 20-07-2026 | Comunicación C(2026) 7702 final, de 5-11-2026; no vinculantes (párr. 5) | D50 |
| Término del art. 3.60, `knowledge/transparency-art50.md` e investigación (sección 4.2) | «Deepfake» a secas; «ultrasuplantación» en la investigación | «Ultrafalsificación»; deepfake queda como nombre de oficio | AIA art. 3.60 |
| Criterios de la ultrafalsificación, investigación (sección 9) | Tres criterios | Cuatro criterios acumulativos | D50 párr. 113 |
| Excepción del art. 50.1, `knowledge/transparency-art50.md` | «Obvio para una persona razonablemente informada»; «no vale si hay grupos vulnerables» | «Evidente para una persona razonablemente informada, atenta y perspicaz»; se tiene en cuenta a los grupos vulnerables | AIA art. 50.1; D50 párr. 42-45 |
| Excepción del art. 50.4, mismo fichero | «Obras evidentemente artísticas, satíricas o de ficción» | «Manifiestamente creativas, satíricas, artísticas o de ficción»; se hace pública la existencia del contenido sin dificultar el disfrute de la obra | AIA art. 50.4 |
| Ejemplos de aviso insuficiente, mismo fichero | «este sitio usa IA», «este sistema usa LLM» | Las frases del texto español: «Los servicios en este sitio web utilizan la IA», «este sistema utiliza grandes modelos de lenguaje» | D50 párr. 38 |
| Recordatorios, mismo fichero | Incluía «siempre que el usuario pregunte» | Lo que dice el párrafo: asesoramiento financiero, de seguros, jurídico o sanitario, acompañantes de IA y control sobre un agente | D50 párr. 40 |
| Obligaciones del proveedor, `knowledge/ai-act-classification.md` | «Arts. 8-17», con la evaluación de conformidad dentro | Requisitos (arts. 8-15) y obligaciones (arts. 16-17), con el art. 43 citado aparte | AIA arts. 8-17 y 43 |
| Términos, mismo fichero | «Tarea procedimental limitada»; «perfila» | «Tarea de procedimiento limitada»; «elaboración de perfiles»; nota con «puntuación ciudadana» | AIA arts. 6.3, 3.52 y 5.1.c |
| Directrices del art. 6, mismo fichero | «Borrador, sin adoptar» | Borrador de 19-05-2026, sin versión final a 2026-11-17 | Borrador (ver P04) |
| Empleo en España, mismo fichero | Nada | Nota sobre el Real Decreto 723/2026, art. 3.2.k | BOE-A-2026-19200 |
| Definición de proxy, `knowledge/special-categories.md` y `skills/special-categories/SKILL.md` | Heurística propia: «se trata como» categoría especial si se usa para inferirla | Criterio del Tribunal de Justicia: basta con que el dato pueda desvelarla indirectamente | TJUE C-184/20 |
| Condiciones b y e del art. 4 bis, `knowledge/special-categories.md` | «Medidas de vanguardia»; «supresión» | «Medidas punteras de seguridad y protección de la intimidad»; «eliminación […] lo que ocurra antes» | AIA art. 4 bis.1 |
| Seudonimización, `knowledge/masking-techniques.md` | Solo el considerando 26 | Añade el art. 4.5 y avisa de las Guidelines 02/2026 del CEPD, en consulta | RGPD art. 4.5; CEPD 02/2026 v1.0 |
| Fechas de las directrices de 2025, investigación (secciones 4.3, 6 y 16) | «6-02-2025» y «4-02-2025, actualizadas el 31-07-2025» | Publicación en febrero y adopción el 29-07-2025, con su número C(2025) | DPP; DDEF |
| Pendientes de la investigación (sección 20) | Daba por no leído el consolidado en español | Nota con lo resuelto el 2026-11-17 | AIA; OMN |
| Fuentes, `knowledge/sources.yaml` | Cinco fuentes; `ai-office` sin revisar | Ocho: se añaden `rgpd`, `lopdgdd` y `ai-act-service-desk`, el consolidado del AI Act y la dirección de la Oficina de Publicaciones | Las propias páginas |
| Dominios del vigilante, `agents/regulatory-watcher.md` | Ocho dominios | Añade `publications.europa.eu`, `curia.europa.eu` y `commission.europa.eu` | — |

### Primera pasada

| Qué | Antes | Después | Fuente |
|---|---|---|---|
| Criterios del deepfake, `knowledge/transparency-art50.md` | Tres criterios | Cuatro criterios acumulativos | Directrices del art. 50, párr. 113 |
| Excepciones del art. 5.1.h, `knowledge/ai-act-classification.md` | «Salvo las excepciones tasadas del art. 5.2-5.7» | Las tres excepciones están en el propio 5.1.h; los apartados 2 a 7 ponen las condiciones | AIA art. 5 |
| Excepción del art. 5.1.g, mismo fichero | Solo etiquetado o filtrado de conjuntos de datos | Añade la categorización de datos biométricos en el ámbito policial | AIA art. 5 |
| Art. 2.10, mismo fichero | «Uso personal no profesional» | Persona física en actividad puramente personal, no profesional | AIA art. 2 |
| Art. 9.2 y art. 6 RGPD, `knowledge/special-categories.md` | «además de una base del art. 6», sin fuente | La misma idea, apoyada en el considerando 51 | RGPD considerando 51 |
| Arts. 22.4 y 35 RGPD, mismo fichero | Citas genéricas | 22.4: solo con el 9.2.a o el 9.2.g y con garantías; 35.3.b: gran escala, también datos penales | RGPD |
| Alcance del art. 4 bis.2, mismo fichero | «También fuera del alto riesgo» | A quién se extiende y con qué condición de necesidad | AIA art. 4 bis |
| LOPDGDD, mismo fichero | Solo el art. 9.1 | Añade el 9.2 (norma con rango de ley) y el 10.1 (datos penales) | LOPDGDD |
| URL del Reglamento 2026/1744, `knowledge/sources.yaml` | `…/ES/TXT/?uri=CELEX:32026R1744`, que devuelve el índice del DO | `…/ES/TXT/HTML/?uri=CELEX:32026R1744`, que devuelve el acto | La propia página |
