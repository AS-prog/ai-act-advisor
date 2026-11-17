# Clasificación AI Act: referencia

Referencia de la skill `ai-act-classify`. Los artículos salen de `docs/investigacion/ai-act-investigacion.md` (secciones 4 a 7); las fechas de aplicación viven en `dates.yaml` y aquí no se repiten. Los criterios marcados «directrices» vienen de documentos no vinculantes de la Comisión.

## Árbol de clasificación

Se recorre en orden y se para en la primera respuesta que fija el nivel. La transparencia (paso 5) se comprueba siempre, porque se acumula con el alto riesgo (art. 50.6).

| Paso | Pregunta | Si la respuesta es sí | Nivel en el perfil |
|---|---|---|---|
| 1 | ¿El entregable **infiere** (art. 3.1)? | Sigue. Si solo aplica reglas escritas por personas, consultas, cuadros de mando sin recomendación, optimización clásica o una regla estadística básica, queda fuera (directrices de definición, párr. 41-51) | `out-of-scope` si no infiere |
| 2 | ¿Aplica una exclusión del art. 2? | Fuera: uso exclusivamente militar o de seguridad nacional (2.3), único fin de I+D científica (2.6), desarrollo y pruebas antes de comercializar, sin pruebas en condiciones reales (2.8), uso personal no profesional (2.10) | `out-of-scope` |
| 3 | ¿Es una práctica del art. 5? | Práctica prohibida | `prohibited` |
| 4 | ¿Su finalidad cae en un caso del anexo III (art. 6.2) o es componente de seguridad de un producto del anexo I (art. 6.1)? | Candidato a alto riesgo, salvo la excepción del art. 6.3 | `high-risk-candidate` |
| 5 | ¿Habla con personas o genera contenido (art. 50)? | Obligaciones de transparencia: skill `ai-transparency` | `transparency` |
| 6 | Nada de lo anterior | Riesgo mínimo: solo el art. 4 (medidas de apoyo a la alfabetización en IA) | `minimal` |

El AI Act alcanza al proyecto si la salida del sistema se usa en la UE o afecta a personas en la UE, aunque el cliente esté fuera (art. 2.1.c y g).

## Prácticas prohibidas (art. 5)

| Letra | Práctica | Condiciones y excepciones |
|---|---|---|
| 5.1.a | Técnicas subliminales, manipuladoras o engañosas | Que alteren de forma sustancial el comportamiento y causen o puedan causar un perjuicio considerable |
| 5.1.b | Explotar vulnerabilidades por edad, discapacidad o situación social o económica | Misma prueba de alteración sustancial y perjuicio considerable |
| 5.1.b bis | Generar o manipular imágenes, vídeo o audio realistas de las partes íntimas o de actividad sexual explícita de una persona identificable sin su consentimiento | En la comercialización, si esa es la finalidad prevista o un resultado previsible y reproducible sin medidas técnicas de seguridad adecuadas (5.1 bis) |
| 5.1.b ter | Generar o manipular material de abuso sexual infantil | Mismo régimen del 5.1 bis |
| 5.1.c | Puntuación social: evaluar o clasificar a personas a lo largo del tiempo por su comportamiento social o sus características | Si lleva a un trato perjudicial en contextos ajenos al de los datos, o desproporcionado |
| 5.1.d | Predecir el riesgo de que una persona delinca basándose únicamente en perfilado o rasgos de personalidad | Se permite apoyar una valoración humana basada en hechos objetivos y verificables |
| 5.1.e | Crear o ampliar bases de reconocimiento facial con extracción no selectiva de imágenes de internet o CCTV | — |
| 5.1.f | Inferir emociones en el lugar de trabajo y en centros educativos | Salvo motivos médicos o de seguridad. Debe basarse en datos biométricos (art. 3.39): el sentimiento de un texto no encaja en la definición |
| 5.1.g | Categorización biométrica para deducir raza, opiniones políticas, afiliación sindical, convicciones religiosas, vida u orientación sexual | Salvo etiquetado o filtrado de conjuntos de datos biométricos lícitos |
| 5.1.h | Identificación biométrica remota en tiempo real en espacios públicos con fines policiales | Salvo las excepciones tasadas del art. 5.2-5.7 |

El scoring crediticio y el de seguros **no** son puntuación social por sí mismos: son alto riesgo (directrices de prácticas prohibidas, párr. 37). Multa: hasta 35 M EUR o el 7 % del volumen de negocios (art. 99.3).

## Anexo III (art. 6.2)

| Área | Casos de alto riesgo | Exclusiones expresas |
|---|---|---|
| 1. Biometría | a) identificación biométrica remota; b) categorización biométrica por atributos sensibles; c) reconocimiento de emociones | Verificación biométrica 1:1 cuyo único fin es confirmar la identidad |
| 2. Infraestructuras críticas | Componentes de seguridad en la gestión de infraestructura digital crítica, tráfico rodado y suministro de agua, gas, calefacción o electricidad | — |
| 3. Educación y formación | a) acceso, admisión o asignación; b) evaluación de resultados de aprendizaje; c) evaluación del nivel educativo adecuado; d) vigilancia de exámenes | — |
| 4. Empleo y gestión de trabajadores | a) contratación o selección: anuncios dirigidos, filtrado de candidaturas, evaluación de candidatos; b) decisiones sobre la relación laboral: promoción, despido, asignación de tareas según rasgos o comportamiento, seguimiento del rendimiento | — |
| 5. Servicios esenciales | a) elegibilidad, concesión, reducción o revocación de prestaciones públicas, incluida la sanidad; b) solvencia o calificación crediticia; c) evaluación de riesgos y precios en seguros de vida y salud; d) clasificación de llamadas de emergencia, despacho y triaje | En la b), la detección de fraude financiero |
| 6. Garantía del cumplimiento del Derecho | a) riesgo de ser víctima; b) polígrafos; c) fiabilidad de las pruebas; d) riesgo de delinquir o reincidir; e) perfilado en investigaciones | — |
| 7. Migración, asilo y fronteras | a) polígrafos; b) evaluación de riesgos de personas que entran; c) examen de solicitudes de asilo, visado o residencia; d) detección o identificación de personas | Verificación de documentos de viaje |
| 8. Justicia y procesos democráticos | a) asistencia a autoridades judiciales, también en resolución alternativa de litigios; b) influir en elecciones, referendos o en el comportamiento electoral | Herramientas cuya salida no se expone directamente a las personas (logística de campañas) |

Ejemplos frecuentes en proyectos de datos: un modelo de propensión a la baja o de *next best action* para marketing no tiene punto propio; un *scorecard* de impago de personas físicas es 5.b; un modelo de precio para una póliza de salud es 5.c; un ranking de candidatos o una medida del rendimiento de empleados es 4.a o 4.b.

## Excepción del art. 6.3 y perfilado

Un sistema del anexo III deja de ser de alto riesgo si no plantea un riesgo importante de daño ni influye sustancialmente en la decisión **y** cumple una de estas condiciones:

- a) tarea procedimental limitada;
- b) mejora del resultado de una actividad humana ya realizada;
- c) detecta patrones de decisión o desviaciones, sin sustituir la valoración humana ni influir en ella sin revisión;
- d) tarea preparatoria de una evaluación.

**Perfilado**: si el sistema perfila a personas físicas, es siempre de alto riesgo (art. 6.3, último párrafo). Indicio en un repo: variables de comportamiento individual que predicen preferencias, fiabilidad o rendimiento de una persona.

Quien usa la excepción documenta la evaluación antes de comercializar y registra el sistema en la base de datos de la UE (arts. 6.4 y 49.2).

Las directrices de la Comisión sobre el art. 6 son un borrador, sin adoptar (investigación, sección 7.3): un criterio que venga de ellas se marca como tal en el aviso.

## Qué trae ser candidato a alto riesgo

Para orientar al PM, no para auditar: el detalle está en la investigación, sección 8.

- **Proveedor** (arts. 8-17): gestión de riesgos, gobernanza de datos, documentación técnica, registros, supervisión humana, precisión y ciberseguridad, evaluación de conformidad.
- **Responsable del despliegue** (art. 26): usar según instrucciones, supervisión humana, conservar los registros al menos 6 meses, informar a los trabajadores (26.7) y a las personas sobre las que se decide (26.11).
- **FRIA** (art. 27): la hacen los organismos públicos, las entidades privadas que prestan servicios públicos y los responsables del despliegue de los puntos 5.b y 5.c. Puede apoyarse en la EIPD del RGPD (27.4).
- Los sistemas ya comercializados antes de la fecha de aplicación solo quedan sujetos si cambian de forma significativa (art. 111.2).

## Rol de la consultora

| Rol | Cuándo | Artículo |
|---|---|---|
| Proveedor (`provider`) | Desarrolla el sistema, o lo encarga, y lo pone en el mercado o en servicio con su nombre o marca, cobre o no | art. 3.3 |
| Responsable del despliegue (`deployer`) | Usa el sistema bajo su autoridad | art. 3.4 |
| Pasa a ser proveedor | Pone su nombre o marca en un sistema de alto riesgo, lo modifica sustancialmente o cambia su finalidad de modo que pase a ser de alto riesgo | art. 25.1 |

Caso habitual de consultora: construye el sistema y el cliente lo pone en servicio con su nombre. El proveedor es entonces el cliente y la consultora es su suministradora, con acuerdo escrito si el sistema es de alto riesgo (art. 25.4). El contrato decide; si no lo dice, es una pregunta para legal.
