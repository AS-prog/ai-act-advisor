---
title: Pendientes y dudas
description: Lista de dudas normativas sin confirmar, decisiones de diseño abiertas y datos ya verificados del plugin ai-act-advisor, para retomarlos sin más contexto.
date: 2026-11-17
status: vivo
---

# Pendientes y dudas

Lista de trabajo del plugin `ai-act-advisor` tras la revisión de datos normativos del 2026-11-17. Tres partes: dudas normativas sin confirmar (P), decisiones de diseño abiertas (D) y lo ya verificado (V), con su fuente y fecha, para no repetirlo. Las rutas son relativas a la raíz del repo; `knowledge/` es `plugins/ai-act-advisor/knowledge/` y `skills/` es `plugins/ai-act-advisor/skills/`.

## Cómo se hizo la revisión

- Fecha de consulta de todas las fuentes: 2026-11-17.
- El AI Act se contrastó con el consolidado «as at 27 July 2026» del AI Act Service Desk de la Comisión (`https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-N` y `/annex-N`), **en inglés**. Es la única copia del consolidado que se deja leer entera desde aquí.
- La herramienta de lectura devuelve resúmenes con citas de 125 caracteres como máximo. Sirve para comprobar artículo, apartado, fecha y contenido, y no para copiar texto literal largo. Las bases de conocimiento no contienen citas literales largas; las pocas frases entrecomilladas están en `docs/investigacion/ai-act-investigacion.md`, que no se revisó entera.
- EUR-Lex (HTML) y el BOE (PDF del DOUE) devolvieron el RGPD cortado en los considerandos, sin el articulado. Por eso los artículos del RGPD se contrastaron con una copia no oficial (P01).

## Dudas normativas sin confirmar

### P01 · Artículos del RGPD, sin leer en fuente oficial

- **Qué se afirma**: el contenido de los arts. 4.5, 5.1.c, 5.1.e, 9.1, 9.2 (letras a, b, g, h, i, j), 10, 17, 22.4, 25, 28, 30, 32, 35.3.b, 44-49 y 89.
- **Dónde**: `knowledge/special-categories.md`, `knowledge/masking-techniques.md`, `skills/pii-masking/SKILL.md`, `skills/special-categories/SKILL.md` y los campos `articulos` de `plugins/ai-act-advisor/scripts/aiact/core.py`.
- **Estado**: coinciden con la copia no oficial `gdpr-info.eu` (arts. 5, 9, 22 y 35 leídos; del resto, solo el título). Los considerandos 26 y 51 sí se leyeron en EUR-Lex.
- **Qué falta**: leer el articulado en EUR-Lex o en el BOE. `https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32016R0679` y `https://www.boe.es/doue/2016/119/L00001-00088.pdf` se cortan antes del art. 1 (157 796 y 106 474 caracteres).
- **Qué hacer**: abrir el PDF oficial a mano o con otra herramienta y repasar esos artículos; si todo coincide, pasar esta entrada a la tabla de verificado.

### P02 · Términos y numeración del AI Act en español

- **Qué se afirma**: la numeración «art. 4 bis», «art. 5.1.b bis», «5.1.b ter», «5.1 bis», «5.1 ter», «6.1 bis a quater» y términos como «responsable del despliegue» o «ultrasuplantación».
- **Dónde**: `knowledge/dates.yaml`, `knowledge/ai-act-classification.md`, `knowledge/special-categories.md`, `knowledge/transparency-art50.md` y las skills.
- **Estado**: el contenido está verificado en inglés (allí son 4a, 5(1)(ba), 5(1)(bb), 5(1a), 5(1b), 6(1a)-(1c)). La forma española es la conversión habitual, sin leer el consolidado en español.
- **Qué falta**: el consolidado en español de EUR-Lex (`https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/spa` o equivalente); en la investigación ya consta que no se pudo leer.
- **Qué hacer**: confirmar la numeración y los términos en la versión española y corregir si difieren.

### P03 · Estado formal de las directrices del art. 50

- **Qué se afirma**: que las directrices C(2026) 5054, de 20-07-2026, «no son vinculantes».
- **Dónde**: `knowledge/transparency-art50.md` (cabecera) y `skills/ai-transparency/SKILL.md` (límites).
- **Estado**: referencia, fecha y párrafos verificados (V25). El PDF se presenta como anexo de una Comunicación que «aprueba el proyecto de directrices»; en lo leído no aparece la frase sobre su carácter no vinculante, y la FAQ de la Comisión tampoco la dice.
- **Qué falta**: la parte introductoria del PDF y saber si hubo adopción formal posterior en todas las lenguas.
- **Qué hacer**: leer la introducción del PDF y la página `https://digital-strategy.ec.europa.eu/en/policies/guidelines-transparency-ai-generated-content`; ajustar la frase si procede.

### P04 · Directrices de clasificación de alto riesgo (art. 6.5): ¿siguen en borrador?

- **Qué se afirma**: que son un borrador sin adoptar.
- **Dónde**: `knowledge/ai-act-classification.md` (final de «Excepción del art. 6.3») y `skills/ai-act-classify/SKILL.md` (límites).
- **Estado**: la página del Service Desk sigue hablando de borrador en consulta hasta el 23-07-2026. Han pasado casi cuatro meses y la página puede estar sin actualizar.
- **Qué hacer**: buscar la adopción en `https://digital-strategy.ec.europa.eu/en/library` y en el Service Desk. Si están adoptadas, revisar con ellas la tabla del anexo III y la excepción del 6.3.

### P05 · Entrada en vigor del Reglamento 2026/1744

- **Qué se afirma**: que entró en vigor el 27-07-2026, al tercer día de su publicación.
- **Dónde**: `knowledge/VERSION` (fecha del consolidado) y `docs/investigacion/ai-act-investigacion.md` (secciones 1 y 2).
- **Estado**: la fecha 27-07-2026 está confirmada de forma indirecta (consolidado del Service Desk «as at 27 July 2026»; la página de la Oficina de IA dice que las enmiendas entraron en vigor el 27 de julio). El artículo final del Reglamento, con la regla del tercer día, no se pudo leer: EUR-Lex corta el texto a los 100 000 caracteres.
- **Qué hacer**: leer el último artículo del Reglamento 2026/1744 en el PDF del DO.

### P06 · Resumen de obligaciones de alto riesgo

- **Qué se afirma**: la lista corta de obligaciones del proveedor («arts. 8-17»: gestión de riesgos, gobernanza de datos, documentación técnica, registros, supervisión humana, precisión y ciberseguridad, evaluación de conformidad).
- **Dónde**: `knowledge/ai-act-classification.md`, sección «Qué trae ser candidato a alto riesgo».
- **Estado**: sale de la sección 8 de la investigación; en esta revisión solo se leyeron los arts. 25, 26 y 27. La evaluación de conformidad es el art. 43, fuera del rango citado.
- **Qué hacer**: leer los arts. 8 a 17 y 43 en el Service Desk y ajustar el rango o la lista.

### P07 · Anexo I y productos sanitarios

- **Qué se afirma**: que un producto sanitario con IA va por el anexo I (art. 6.1) y no por el anexo III.
- **Dónde**: `knowledge/sectors.yaml` (nota de `healthcare`) y `knowledge/dates.yaml` (fila de 2028-08-02).
- **Estado**: el art. 6.1 y su fecha están verificados; la lista del anexo I no se releyó.
- **Qué hacer**: leer `https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-1` y confirmar que los Reglamentos 2017/745 y 2017/746 siguen en la sección A.

### P08 · Proxies: cuándo un dato que permite inferir una categoría especial lo es

- **Qué se afirma**: que un proxy «se trata como» categoría especial si se usa para inferirla o decidir sobre ella, y una tabla de variables proxy.
- **Dónde**: `knowledge/special-categories.md` (sección «Proxies») y `skills/special-categories/SKILL.md` (paso 1).
- **Estado**: heurística propia, sin fuente. Hay jurisprudencia del TJUE que podría ir más lejos (datos que revelan indirectamente una categoría especial; asunto C-184/20, de 2022, citado de memoria y sin comprobar).
- **Qué hacer**: leer esa sentencia en `curia.europa.eu` y lo que digan la AEPD y el CEPD sobre datos inferidos; reescribir la definición de proxy con esa base o marcarla como criterio prudente del plugin.

### P09 · Precisiones menores en `dates.yaml`

- **Qué se afirma**: «arts. 51-55» desde 2025-08-02 y «arts. 6-27» desde 2027-12-02.
- **Estado**: el art. 113.b habla del capítulo V entero (arts. 51-56) y también del capítulo III sección 4, el capítulo VII, el capítulo XII salvo el art. 101 y el art. 78. El art. 113.c excluye el art. 6.5 del aplazamiento. Las fechas son correctas; el alcance está resumido.
- **Qué hacer**: decidir si `dates.yaml` debe reflejar el alcance completo. Si se cambia, revisar el hook `SessionStart` y las skills que lo leen.

### P10 · Publicaciones vistas y sin analizar

- **Qué son**: novedades que aparecieron al abrir las fuentes y que no se compararon con la base.
  - AEPD: «Asistentes y agentes de IA: Que la IA actúe por ti, no sin ti» (27-10-2026); «Sistemas algorítmicos en el ámbito laboral. Transparencia y garantías de protección de datos» (07-10-2026); «Exactitud, idoneidad y calidad de los datos en tratamientos de datos personales con Inteligencia Artificial» (21-07-2026).
  - CEPD: Guidelines 02/2026 sobre anonimización y Guidelines 03/2026 sobre *web scraping* en IA generativa, en consulta hasta el 30-10-2026.
  - AESIA: anuncia que actualizará sus 16 guías por el Ómnibus; sin fecha.
  - Oficina de IA: enlace a «próximas directrices», sin fecha.
- **A qué pueden afectar**: `knowledge/masking-techniques.md` (anonimización), `knowledge/transparency-art50.md` (agentes), `knowledge/ai-act-classification.md` (área 4, empleo).
- **Qué hacer**: lanzar `/regulatory-update` y dejar que el vigilante las compare.

### P11 · Fuentes de `sources.yaml` leídas a medias

- **Estado**: las siete URL cargan. De la AEPD solo se ve la primera de 14 páginas; la URL del CEPD muestra sobre todo consultas públicas; `ai-office`, `aepd` y `edpb` siguen con `last_checked: null` porque esta revisión no fue una vigilancia completa.
- **Qué hacer**: en el próximo `/regulatory-update`, comprobar que la URL del CEPD lista también las directrices adoptadas y valorar una URL de la AEPD filtrada por IA.

### P12 · Errores vistos en la investigación, sin corregir

- **Dónde**: `docs/investigacion/ai-act-investigacion.md`. No se tocó porque quedaba fuera del encargo.
- **Qué**:
  - Sección 9: dice que el deepfake tiene «tres criterios»; las directrices del art. 50 dan cuatro (párr. 113). En `knowledge/` ya está corregido.
  - Secciones 4.3, 6 y 16: fecha las directrices de definición en «6-02-2025» y las de prácticas prohibidas en «4-02-2025, actualizadas el 31-07-2025». Los PDF dicen C(2025) 5053 final y C(2025) 5052 final, ambos de 29-07-2025. Puede que las fechas de febrero sean las de publicación del borrador aprobado; sin comprobar.
- **Qué hacer**: corregir la sección 9 y aclarar las fechas de la sección 16.

## Decisiones de diseño abiertas

### D01 · Q5: cuánto ruido es aceptable

- **Estado**: el hook avisa de cuatro hallazgos por fichero como máximo, una vez por sesión, y calla lo que está en la línea base (`plugins/ai-act-advisor/scripts/aiact/hooks.py`).
- **Qué decidir**: si ese límite vale tras probarlo en proyectos reales y si la búsqueda por términos, que es la parte ruidosa, sigue activa cuando el repo ya tiene reglas.

### D02 · MCP de documentación normativa (versión madura)

- **Qué decidir**: dónde corre (local o servicio), qué modelo de embeddings usa y cómo se reparte el índice con el plugin. Está como pendiente en `docs/diseno/propuesta-prototipo.md`.
- **Dato nuevo**: EUR-Lex y el BOE cortan los textos largos al leerlos desde un agente (P01, P05); un índice propio del texto íntegro resolvería también eso.

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
- **Qué decidir**: si se añade una lista `proxy_terms` (código postal, nacionalidad, bajas…) y con qué severidad, sabiendo que `codigo_postal` y `postal_code` ya están en `pii_terms`. Depende de P08.

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
- **Qué decidir**: si basta con leer el índice de cada fuente, o si se añade a `sources.yaml` el AI Act Service Desk como copia legible del consolidado.

### D13 · Fuentes que el plugin cita y no vigila

- **Estado**: `knowledge/sources.yaml` no incluye el RGPD en EUR-Lex, la LOPDGDD en el BOE ni el AI Act Service Desk, y las tres se usan en `knowledge/`.
- **Qué decidir**: si se añaden, y que el agente `regulatory-watcher` acepte `curia.europa.eu` si P08 acaba citando jurisprudencia.

### D14 · Datos penales dentro de «categorías especiales»

- **Estado**: `special_category_terms` incluye `antecedentes_penales` y `criminal_record`, y el hallazgo cita solo el art. 9 RGPD. Esos datos van por el art. 10 RGPD y el art. 10 LOPDGDD.
- **Qué decidir**: si se separan en un hallazgo propio o si el hallazgo cita los dos artículos.

### D15 · Adaptadores por stack

- **Estado**: `plugins/ai-act-advisor/adapters/` solo tiene un README que dice «Pendiente Q16», mientras la tabla de decisiones da Q16 por cerrada (sin stack fijo). Las skills usan `knowledge/masking-techniques.md` para los ejemplos por stack.
- **Qué decidir**: si los adaptadores siguen en el diseño o se retira la carpeta.

### D16 · Redacción de «nunca bloquea»

- **Estado**: las cinco skills nuevas lo dicen en positivo («explica, propone y deja la decisión»); `project-init` y `pii-masking` conservan «Nunca bloquea».
- **Qué decidir**: si se unifican.

## Verificado

Todo consultado el 2026-11-17. «SD» es el consolidado del AI Act Service Desk (inglés, «as at 27 July 2026»).

| Id | Qué | Dónde está en el repo | Fuente |
|---|---|---|---|
| V01 | Consolidado de 27-07-2026; Reglamentos 2024/1689 y 2026/1744; el 2026/1744 es de 8-07-2026, publicado en el DO L el 24-07-2026, y modifica los Reglamentos 2024/1689, 2018/1139 y 2023/1230 | `knowledge/VERSION` | SD; EUR-Lex CELEX 32026R1744 (HTML ES); página de la Oficina de IA |
| V02 | Capítulos I y II (art. 4 y art. 5.1.a-h) desde 2025-02-02 | `knowledge/dates.yaml`, `skills/project-init` | SD art. 113.a |
| V03 | Capítulo V (GPAI) desde 2025-08-02 | `knowledge/dates.yaml` | SD art. 113.b |
| V04 | Fecha general 2026-08-02, que incluye el art. 50 y el art. 101 | `knowledge/dates.yaml`, `core.py` (`llm-sdk`), `skills/project-init` | SD art. 113; FAQ de la Comisión sobre el art. 50 |
| V05 | Art. 5.1.b bis, 5.1.b ter, 5.1 bis y 5.1 ter desde 2026-12-02 | `knowledge/dates.yaml` | SD art. 113.a |
| V06 | Art. 50.2 exigible desde 2026-12-02 a sistemas comercializados antes del 2026-08-02 | `knowledge/dates.yaml`, `knowledge/transparency-art50.md`, `skills/ai-transparency` | SD art. 111.4; FAQ del art. 50 |
| V07 | Alto riesgo del anexo III (cap. III, secc. 1-3) desde 2027-12-02 | `knowledge/dates.yaml`, `core.py` (`scoring-model`), `skills/project-init` | SD art. 113.c.i |
| V08 | Alto riesgo del anexo I (art. 6.1) desde 2028-08-02 | `knowledge/dates.yaml` | SD art. 113.c.ii |
| V09 | Ámbito y exclusiones: art. 2.1.c, 2.1.g, 2.3, 2.6, 2.8 y 2.10 | `knowledge/ai-act-classification.md` | SD art. 2 |
| V10 | Definiciones: art. 3.1, 3.3, 3.4, 3.12, 3.39 (exige datos biométricos), 3.40, 3.60 y 3.63 | `knowledge/ai-act-classification.md`, `skills/ai-act-classify` | SD art. 3 |
| V11 | Art. 4: medidas de apoyo a la alfabetización, sin nivel garantizado | `knowledge/ai-act-classification.md` | SD art. 4 |
| V12 | Art. 4 bis: seis condiciones (a-f), alcance del apartado 2 y ausencia de obligación de detectar sesgos | `knowledge/special-categories.md`, `skills/special-categories` | SD art. 4a |
| V13 | Art. 5.1, letras a, b, b bis, b ter, c, d, e, f, g y h, con sus excepciones; 5.1 bis y 5.1 ter; 5.2-5.7 | `knowledge/ai-act-classification.md` | SD art. 5 |
| V14 | Art. 6.1, 6.1 bis-quater, 6.2, 6.3 (cuatro condiciones y perfilado), 6.4 con el registro del 49.2, y 6.5 | `knowledge/ai-act-classification.md`, `skills/ai-act-classify` | SD arts. 6 y 49 |
| V15 | Anexo III: las ocho áreas, sus letras y las exclusiones expresas | `knowledge/ai-act-classification.md` | SD annex-3 |
| V16 | Mapa de 17 sectores a puntos del anexo III | `knowledge/sectors.yaml` | SD annex-3 |
| V17 | Art. 25.1 (a-c), 25.2 y 25.4 | `knowledge/ai-act-classification.md` | SD art. 25 |
| V18 | Art. 26.1, 26.2, 26.6 (seis meses como mínimo), 26.7, 26.9 y 26.11 | `knowledge/ai-act-classification.md` | SD art. 26 |
| V19 | Art. 27: quién hace la FRIA, exclusión del anexo III.2, 27.4 y 27.5 | `knowledge/ai-act-classification.md` | SD art. 27 |
| V20 | Art. 50.1 a 50.7: obligado, obligación y excepciones | `knowledge/transparency-art50.md`, `skills/ai-transparency`, `core.py` | SD art. 50 |
| V21 | Multas: art. 99.3 (35 M EUR o 7 %), 99.4 (15 M EUR o 3 %; el art. 50 es la letra g), 99.5, 99.6 y 99.6 bis | `knowledge/ai-act-classification.md`, `knowledge/transparency-art50.md` | SD art. 99 |
| V22 | Art. 101.1: multas de la Comisión a proveedores de modelos GPAI | `knowledge/dates.yaml` | SD art. 101 |
| V23 | Art. 111.2: sistemas ya comercializados, solo con cambios significativos de diseño | `knowledge/ai-act-classification.md` | SD art. 111 |
| V24 | Las obligaciones del art. 53 son del proveedor del modelo GPAI | `skills/ai-transparency` (límites) | SD art. 53 |
| V25 | Directrices del art. 50, C(2026) 5054 final, 20-07-2026: párr. 30, 31, 37, 38, 40, 42-45, 64-68, 69-70, 72-73, 74, 90-92, 99-108 y 113-117 | `knowledge/transparency-art50.md` | PDF de las directrices en el Service Desk |
| V26 | Código de buenas prácticas sobre transparencia del contenido generado por IA: versión final de 10-06-2026, declarado herramienta voluntaria adecuada | `knowledge/transparency-art50.md` | Página de la Comisión sobre el código |
| V27 | El contenido generado antes del 2026-08-02 no necesita etiquetado retroactivo | `knowledge/transparency-art50.md` | FAQ de la Comisión sobre el art. 50 |
| V28 | El scoring crediticio y de seguros es alto riesgo si no cumple las condiciones de la puntuación social (párr. 37) | `knowledge/ai-act-classification.md` | Directrices de prácticas prohibidas, C(2025) 5052 final |
| V29 | Quedan fuera de la definición: optimización matemática (párr. 42-45), procesamiento básico (46-47), heurísticas clásicas (48) y predicción simple (49-51) | `knowledge/ai-act-classification.md` | Directrices de definición, C(2025) 5053 final |
| V30 | RGPD considerando 26 (el dato seudonimizado sigue siendo personal) y considerando 51 (se suman las condiciones generales de licitud) | `knowledge/masking-techniques.md`, `knowledge/special-categories.md` | EUR-Lex CELEX 32016R0679 (HTML ES) |
| V31 | LOPDGDD art. 9.1, 9.2 y 10.1 | `knowledge/special-categories.md` | BOE, texto consolidado BOE-A-2018-16673 |
| V32 | RGPD arts. 5.1.c, 5.1.e, 9.1, 9.2, 22.4 y 35.3.b; títulos de los arts. 10, 17, 25, 28, 30, 32 y 89 y del capítulo V | `knowledge/special-categories.md`, `knowledge/masking-techniques.md`, `skills/pii-masking`, `core.py` | Copia no oficial `gdpr-info.eu`. Falta la fuente oficial: P01 |
| V33 | Campos `norma`, `articulos` y `aplica` de los diez tipos de hallazgo | `plugins/ai-act-advisor/scripts/aiact/core.py` | Los de V04, V07, V20 y V32; salvedad en D11 |
| V34 | Las siete URL de las fuentes cargan; AESIA lista 16 guías y el compendio de checklists | `knowledge/sources.yaml` | Las propias páginas; salvedades en P11 |

## Corregido en esta revisión

| Qué | Antes | Después | Fuente |
|---|---|---|---|
| Criterios del deepfake, `knowledge/transparency-art50.md` | Tres criterios | Cuatro criterios acumulativos | Directrices del art. 50, párr. 113 |
| Excepciones del art. 5.1.h, `knowledge/ai-act-classification.md` | «Salvo las excepciones tasadas del art. 5.2-5.7» | Las tres excepciones están en el propio 5.1.h; los apartados 2 a 7 ponen las condiciones | SD art. 5 |
| Excepción del art. 5.1.g, mismo fichero | Solo etiquetado o filtrado de conjuntos de datos | Añade la categorización de datos biométricos en el ámbito policial | SD art. 5 |
| Art. 2.10, mismo fichero | «Uso personal no profesional» | Persona física en actividad puramente personal, no profesional | SD art. 2 |
| Art. 9.2 y art. 6 RGPD, `knowledge/special-categories.md` | «además de una base del art. 6», sin fuente | La misma idea, apoyada en el considerando 51 | EUR-Lex, RGPD considerando 51 |
| Arts. 22.4 y 35 RGPD, mismo fichero | Citas genéricas | 22.4: solo con el 9.2.a o el 9.2.g y con garantías; 35.3.b: gran escala, también datos penales | `gdpr-info.eu` (P01) |
| Alcance del art. 4 bis.2, mismo fichero | «También fuera del alto riesgo» | A quién se extiende y con qué condición de necesidad | SD art. 4a |
| LOPDGDD, mismo fichero | Solo el art. 9.1 | Añade el 9.2 (norma con rango de ley) y el 10.1 (datos penales) | BOE-A-2018-16673 |
| URL del Reglamento 2026/1744, `knowledge/sources.yaml` | `…/ES/TXT/?uri=CELEX:32026R1744`, que devuelve el índice del DO | `…/ES/TXT/HTML/?uri=CELEX:32026R1744`, que devuelve el acto | La propia página |
