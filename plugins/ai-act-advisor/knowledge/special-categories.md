# Categorías especiales: referencia

Referencia de la skill `special-categories`. El art. 4 bis del AI Act sale de `docs/investigacion/ai-act-investigacion.md` (sección 11) y se contrastó con el consolidado del AI Act Service Desk. La parte del RGPD y de la LOPDGDD se contrastó el 2026-11-17; el detalle de con qué fuente está al final y en `docs/pendientes.md`.

## Qué es categoría especial (RGPD art. 9.1)

Datos que revelan el origen étnico o racial, las opiniones políticas, las convicciones religiosas o filosóficas o la afiliación sindical; datos genéticos; datos biométricos dirigidos a identificar de manera unívoca a una persona; datos relativos a la salud; datos relativos a la vida sexual o a la orientación sexual.

Los datos de condenas e infracciones penales van aparte, por el art. 10 RGPD. En España, tratarlos para fines distintos de la prevención o persecución de delitos necesita el amparo de una norma de Derecho de la Unión o con rango de ley (LOPDGDD art. 10.1). El plugin los detecta con los mismos términos (`antecedentes_penales`, `criminal_record`) y se escalan igual.

## Proxies

Un **proxy** es una variable que no es categoría especial pero permite inferirla. Si se usa para inferir o decidir sobre la categoría, se trata como tal. Heurísticas para preguntar, no pruebas:

| Variable | Qué puede revelar |
|---|---|
| Código postal, barrio, sección censal | Origen étnico, nivel socioeconómico |
| Nombre, apellidos, nacionalidad, país de nacimiento, idioma | Origen étnico o racial |
| Bajas médicas, absentismo por enfermedad, compras de farmacia, primas o siniestros de salud, grado de discapacidad | Salud |
| Cuota sindical en nómina, horas sindicales | Afiliación sindical |
| Dieta o menú, festivos solicitados, donativos, asignación tributaria | Convicciones religiosas |
| Estado civil, sexo de la pareja o del beneficiario | Vida u orientación sexual |
| Donaciones a partidos, suscripciones a medios, afiliaciones | Opiniones políticas |
| Fotografía, voz, huella | Biometría, y a través de ella origen étnico o salud |

En un modelo, el riesgo crece cuando el proxy entra como variable predictora: el modelo puede discriminar por la categoría sin que nadie la haya cargado.

## Cuándo se pueden tratar (RGPD art. 9.2)

La regla es que su tratamiento está vetado salvo que se cumpla una de las excepciones del art. 9.2. La excepción se suma a las condiciones generales de licitud, es decir, a una base del art. 6 (considerando 51). Las que aparecen en proyectos de datos:

| Letra | Excepción | Típica en |
|---|---|---|
| 9.2.a | Consentimiento explícito para fines concretos | Programas de salud voluntarios, encuestas |
| 9.2.b | Obligaciones de Derecho laboral y de seguridad social | Nóminas, bajas, prevención de riesgos |
| 9.2.g | Interés público esencial con base en una ley | Sector público |
| 9.2.h | Medicina preventiva o laboral, asistencia sanitaria, bajo secreto profesional | Sanidad, mutuas |
| 9.2.i | Salud pública | Sanidad |
| 9.2.j | Archivo, investigación científica o estadística, con las garantías del art. 89 | Estudios, analítica agregada |

En España, el consentimiento por sí solo no levanta el veto cuando la finalidad principal es identificar la ideología, la afiliación sindical, la religión, la orientación sexual, las creencias o el origen racial o étnico (LOPDGDD art. 9.1). Y los tratamientos de las letras g, h e i que se apoyen en Derecho español necesitan una norma con rango de ley (LOPDGDD art. 9.2).

Otras obligaciones que suelen acompañar: evaluación de impacto (EIPD) cuando el tratamiento de estas categorías o de datos penales es a gran escala (RGPD art. 35.3.b), y decisiones automatizadas basadas en estas categorías solo con la excepción del 9.2.a o del 9.2.g y con garantías (RGPD art. 22.4). La base jurídica la fija el responsable del tratamiento, que suele ser el cliente, con su DPO.

## Medir sesgos con categorías especiales (AI Act art. 4 bis)

El art. 4 bis permite tratar categorías especiales para detectar y corregir sesgos de un sistema o modelo de IA. El apartado 1 habla de los proveedores de sistemas de alto riesgo; el apartado 2 lo extiende a proveedores y responsables del despliegue de otros sistemas y modelos, y a los responsables del despliegue de alto riesgo, cuando sea estrictamente necesario para sesgos que puedan afectar a la salud, la seguridad o los derechos fundamentales, o llevar a una discriminación prohibida. No crea la obligación de detectar sesgos. Exige **las seis** condiciones:

| Letra | Condición | Cómo se ve en un repo |
|---|---|---|
| a | No es posible con otros datos, incluidos sintéticos o anonimizados | Nota de por qué no bastan |
| b | Límites técnicos a la reutilización y medidas de vanguardia, incluida la seudonimización | Tabla aparte, seudonimizada, sin unirse al conjunto de entrenamiento productivo |
| c | Controles estrictos y acceso documentado, limitado a personas autorizadas con deber de confidencialidad | Permisos propios y registro de accesos |
| d | Sin transmisión a terceros | Fuera de exportaciones y de entornos compartidos |
| e | Supresión cuando se corrige el sesgo o vence el plazo de conservación | Fecha o tarea de borrado |
| f | El registro de actividades de tratamiento justifica la necesidad | Entrada en el registro del responsable |

Cubre medir y corregir el sesgo; usar la categoría como variable del modelo en producción queda fuera de este artículo y vuelve al art. 9.2.

## Estado de la verificación

- RGPD arts. 9.1, 9.2, 22.4 y 35.3.b, y los títulos de los arts. 10 y 89: contrastados el 2026-11-17 con una copia no oficial del texto (gdpr-info.eu), porque EUR-Lex y el BOE devolvieron el Reglamento cortado en los considerandos. Los considerandos 26 y 51 sí se leyeron en EUR-Lex. Falta la lectura en la fuente oficial (`docs/pendientes.md`, P01).
- LOPDGDD arts. 9.1, 9.2 y 10.1: contrastados el 2026-11-17 en el texto consolidado del BOE.
- AI Act art. 4 bis: contrastado el 2026-11-17 en el consolidado del AI Act Service Desk, en inglés.
- La tabla de proxies es heurística propia del plugin, sin fuente normativa.
