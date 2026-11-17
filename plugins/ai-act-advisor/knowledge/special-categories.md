# Categorías especiales: referencia

Referencia de la skill `special-categories`. El art. 4 bis del AI Act sale de `docs/investigacion/ai-act-investigacion.md` (sección 11). La investigación del repo cubre el AI Act y no el articulado del RGPD: lo que aquí viene del RGPD y de la LOPDGDD está resumido del texto legal y **pendiente de contrastar** por el DPO o en la próxima revisión normativa (ver el final).

## Qué es categoría especial (RGPD art. 9.1)

Datos que revelan el origen étnico o racial, las opiniones políticas, las convicciones religiosas o filosóficas o la afiliación sindical; datos genéticos; datos biométricos dirigidos a identificar de manera unívoca a una persona; datos relativos a la salud; datos relativos a la vida sexual o a la orientación sexual.

Los datos de condenas e infracciones penales van aparte, por el art. 10 RGPD. El plugin los detecta con los mismos términos (`antecedentes_penales`, `criminal_record`) y se escalan igual.

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

La regla es que su tratamiento está vetado salvo que se cumpla una de las excepciones del art. 9.2 **además** de una base del art. 6. Las que aparecen en proyectos de datos:

| Letra | Excepción | Típica en |
|---|---|---|
| 9.2.a | Consentimiento explícito para fines concretos | Programas de salud voluntarios, encuestas |
| 9.2.b | Obligaciones de Derecho laboral y de seguridad social | Nóminas, bajas, prevención de riesgos |
| 9.2.g | Interés público esencial con base en una ley | Sector público |
| 9.2.h | Medicina preventiva o laboral, asistencia sanitaria, bajo secreto profesional | Sanidad, mutuas |
| 9.2.i | Salud pública | Sanidad |
| 9.2.j | Archivo, investigación científica o estadística, con las garantías del art. 89 | Estudios, analítica agregada |

En España, el consentimiento por sí solo no levanta el veto cuando la finalidad principal es identificar la ideología, la afiliación sindical, la religión, la orientación sexual, las creencias o el origen racial o étnico (LOPDGDD art. 9.1).

Otras obligaciones que suelen acompañar: evaluación de impacto (EIPD, RGPD art. 35) cuando el tratamiento es a gran escala, y límites a las decisiones automatizadas basadas en estas categorías (RGPD art. 22.4). La base jurídica la fija el responsable del tratamiento, que suele ser el cliente, con su DPO.

## Medir sesgos con categorías especiales (AI Act art. 4 bis)

El art. 4 bis permite tratar categorías especiales para detectar y corregir sesgos de un sistema o modelo de IA. Alcanza a proveedores y responsables del despliegue, también fuera del alto riesgo (4 bis.2), y no crea la obligación de detectar sesgos. Exige **las seis** condiciones:

| Letra | Condición | Cómo se ve en un repo |
|---|---|---|
| a | No es posible con otros datos, incluidos sintéticos o anonimizados | Nota de por qué no bastan |
| b | Límites técnicos a la reutilización y medidas de vanguardia, incluida la seudonimización | Tabla aparte, seudonimizada, sin unirse al conjunto de entrenamiento productivo |
| c | Controles estrictos y acceso documentado, limitado a personas autorizadas con deber de confidencialidad | Permisos propios y registro de accesos |
| d | Sin transmisión a terceros | Fuera de exportaciones y de entornos compartidos |
| e | Supresión cuando se corrige el sesgo o vence el plazo de conservación | Fecha o tarea de borrado |
| f | El registro de actividades de tratamiento justifica la necesidad | Entrada en el registro del responsable |

Cubre medir y corregir el sesgo; usar la categoría como variable del modelo en producción queda fuera de este artículo y vuelve al art. 9.2.

## Pendiente de verificar

- RGPD arts. 9.1, 9.2, 10, 22.4 y 35, y LOPDGDD art. 9.1: resumidos del texto legal, sin contrastar en `docs/investigacion/`.
- La tabla de proxies es heurística propia del plugin, sin fuente normativa.
