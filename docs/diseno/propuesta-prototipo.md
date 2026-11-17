---
title: Propuesta del prototipo del plugin AI Act
description: Qué lleva el primer prototipo en cada componente de un plugin de Claude Code para que PM, DE y AE reciban avisos preventivos del AI Act y del RGPD.
date: 2026-11-17
status: borrador
---

# Propuesta del prototipo del plugin AI Act

Qué lleva el primer prototipo en cada componente de un plugin de Claude Code para que PM, DE y AE reciban avisos preventivos del AI Act y del RGPD, sin que nada se bloquee.

## Conclusión

Propongo un plugin de Claude Code que acompaña a PM, DE y AE en
proyectos de datos: avisa de los riesgos del AI Act y del RGPD en el
momento en que aparecen, sugiere cómo mitigarlos y deja la decisión a
quien trabaja. El prototipo lleva un perfil del proyecto, siete skills,
dos hooks que solo añaden contexto, un agente para vigilar la normativa
y una base de conocimiento con fecha. No lleva MCP ni LSP.

## Contexto

Los proyectos de ingeniería y analítica de datos para clientes de
consultoras como Merkle rara vez son de alto riesgo por la técnica: el
riesgo lo pone el sector del cliente y la finalidad. Y casi siempre hay
datos personales, que son terreno del RGPD. Por eso el AI Act pone el
marco y el plugin baja hasta cada tabla.

<figure class="figwrap">
  <svg viewBox="0 0 720 264" role="img" aria-labelledby="marco-title marco-desc">
    <title id="marco-title">Del AI Act al RGPD</title>
    <desc id="marco-desc">Tres capas: la clasificación AI Act del proyecto la hace el PM en el kickoff, las obligaciones de cada caso las comparten PM y DE, y los avisos RGPD sobre tablas y columnas llegan a DE y AE siempre, haya IA o no.</desc>
    <defs>
      <marker id="marco-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon class="d-bar" points="0 0, 8 3, 0 6"/></marker>
    </defs>
    <line class="d-line" x1="276" y1="72" x2="276" y2="104" marker-end="url(#marco-arrow)"/>
    <line class="d-line" x1="276" y1="160" x2="276" y2="192" marker-end="url(#marco-arrow)"/>
    <rect class="d-box" x="16" y="16" width="520" height="56"/>
    <text class="d-t" x="32" y="40">AI Act · clasificación del proyecto</text>
    <text class="d-sm" x="32" y="60">prohibido, alto riesgo, transparencia, mínimo o fuera del AI Act</text>
    <rect class="d-box" x="16" y="104" width="520" height="56"/>
    <text class="d-t" x="32" y="128">AI Act · obligaciones del caso</text>
    <text class="d-sm" x="32" y="148">anexo III según el sector del cliente, art. 50, art. 4 bis</text>
    <rect class="d-fill" x="16" y="192" width="520" height="56"/>
    <text class="d-t" x="32" y="216">RGPD · cada tabla y cada columna</text>
    <text class="d-sm" x="32" y="236">PII, categorías especiales, minimización. Aplica siempre</text>
    <text class="d-tm" x="560" y="48">PM · KICKOFF</text>
    <text class="d-tm" x="560" y="136">PM Y DE</text>
    <text class="d-tm" x="560" y="224">DE Y AE · DIARIO</text>
  </svg>
  <figcaption>El AI Act pone el marco y el RGPD llega a cada tabla. Un proyecto <strong>fuera del AI Act</strong> sigue recibiendo la capa de abajo.</figcaption>
</figure>

Tres reglas acordadas en la entrevista:

1.  **Avisa y sugiere, nunca bloquea.** Ningún hook deniega una acción.
    El aviso dice cuándo una decisión no le corresponde al ingeniero y a
    quién escalarla.
2.  **Cada aviso dice su norma.** Artículo, si aplica ya o desde qué
    fecha, y la fecha de la base normativa. Un proyecto sin IA recibe
    una línea de «fuera del AI Act» y sigue con los avisos del RGPD.
3.  **La base normativa se actualiza con revisión humana** y el plugin
    recuerda que no es asesoramiento legal.

## Propuesta

Las piezas se relacionan a través del perfil del proyecto y de la base
de conocimiento, que leen todas las demás.

<figure class="figwrap">
  <svg viewBox="0 0 720 328" role="img" aria-labelledby="piezas-title piezas-desc">
    <title id="piezas-title">Cómo se relacionan las piezas</title>
    <desc id="piezas-desc">El PM escribe el perfil en el kickoff. Hooks y skills leen el perfil y la base de conocimiento. El trabajo de DE y AE dispara los hooks, que sugieren skills; las skills avisan, el ingeniero decide y sus decisiones alimentan el resumen del PM.</desc>
    <defs>
      <marker id="piezas-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon class="d-bar" points="0 0, 8 3, 0 6"/></marker>
    </defs>
    <rect class="d-wash-1" x="264" y="16" width="448" height="88"/>
    <text class="d-tm" x="276" y="32">CONTEXTO QUE LEEN TODOS</text>
    <line class="d-line" x1="184" y1="64" x2="280" y2="64" marker-end="url(#piezas-arrow)"/>
    <rect class="d-mask" x="200" y="42" width="56" height="14"/>
    <text class="d-tm d-mid" x="228" y="53">ESCRIBE</text>
    <line class="d-line" x1="368" y1="104" x2="368" y2="152" marker-end="url(#piezas-arrow)"/>
    <rect class="d-mask" x="376" y="121" width="36" height="14"/>
    <text class="d-tm" x="380" y="132">LEEN</text>
    <line class="d-line" x1="608" y1="104" x2="608" y2="152" marker-end="url(#piezas-arrow)"/>
    <line class="d-line" x1="184" y1="176" x2="280" y2="176" marker-end="url(#piezas-arrow)"/>
    <rect class="d-mask" x="210" y="152" width="44" height="14"/>
    <text class="d-tm d-mid" x="232" y="163">EDITA</text>
    <line class="d-line" x1="456" y1="176" x2="520" y2="176" marker-end="url(#piezas-arrow)"/>
    <rect class="d-mask" x="459" y="152" width="58" height="14"/>
    <text class="d-tm d-mid" x="488" y="163">SUGIERE</text>
    <line class="d-line" x1="608" y1="200" x2="608" y2="264" marker-end="url(#piezas-arrow)"/>
    <rect class="d-mask" x="616" y="225" width="44" height="14"/>
    <text class="d-tm" x="620" y="236">AVISA</text>
    <line class="d-dash" x1="520" y1="288" x2="184" y2="288" marker-end="url(#piezas-arrow)"/>
    <rect class="d-mask" x="310" y="264" width="88" height="14"/>
    <text class="d-tm d-mid" x="354" y="275">REGISTRO · Q5</text>
    <rect class="d-box" x="24" y="40" width="160" height="48"/>
    <text class="d-t d-mid" x="104" y="61">Kickoff del PM</text>
    <text class="d-tm d-mid" x="104" y="78">/project-init</text>
    <rect class="d-fill" x="280" y="40" width="176" height="48"/>
    <text class="d-t d-mid" x="368" y="61">Perfil del proyecto</text>
    <text class="d-tm d-mid" x="368" y="78">.ai-act/profile.yaml</text>
    <rect class="d-box" x="520" y="40" width="176" height="48"/>
    <text class="d-t d-mid" x="608" y="61">Base de conocimiento</text>
    <text class="d-tm d-mid" x="608" y="78">knowledge/</text>
    <rect class="d-box" x="24" y="152" width="160" height="48"/>
    <text class="d-t d-mid" x="104" y="173">Trabajo de DE y AE</text>
    <text class="d-tm d-mid" x="104" y="190">.sql .py dbt</text>
    <rect class="d-box" x="280" y="152" width="176" height="48"/>
    <text class="d-t d-mid" x="368" y="173">Hooks</text>
    <text class="d-sm d-mid" x="368" y="190">solo añaden contexto</text>
    <rect class="d-box" x="520" y="152" width="176" height="48"/>
    <text class="d-t d-mid" x="608" y="173">Skills de riesgo</text>
    <text class="d-sm d-mid" x="608" y="190">se cargan solas</text>
    <rect class="d-fill" x="520" y="264" width="176" height="48"/>
    <text class="d-t d-mid" x="608" y="285">El ingeniero decide</text>
    <text class="d-sm d-mid" x="608" y="302">mitiga, acepta o escala</text>
    <rect class="d-box" x="24" y="264" width="160" height="48"/>
    <text class="d-t d-mid" x="104" y="285">Resumen del PM</text>
    <text class="d-tm d-mid" x="104" y="302">/risk-summary</text>
  </svg>
  <figcaption>El perfil es la pieza focal: sin él, hooks y skills no saben el sector ni el rol. La línea discontinua depende de <strong>Q5</strong>.</figcaption>
</figure>

| Componente           | Qué lleva el prototipo                                          | Para quién                |
|----------------------|-----------------------------------------------------------------|---------------------------|
| Manifiesto           | Nombre, versión y fecha de la base normativa                    | Todos                     |
| Perfil del proyecto  | Un fichero en el repo del proyecto que leen todas las piezas    | PM lo crea, todos lo usan |
| Skills               | 7: 2 del PM, 4 de riesgo y 1 de actualización                   | PM, DE, AE                |
| Hooks                | 2: inicio de sesión y detección de señales tras leer o escribir | DE, AE                    |
| Agentes              | 1: vigilante normativo para la actualización                    | Mantenimiento             |
| Base de conocimiento | Señales, fechas, sectores, técnicas y fuentes, en ficheros      | Todas las piezas          |
| MCP                  | Ninguno en el prototipo                                         | —                         |
| LSP                  | Ninguno                                                         | —                         |
| Marketplace          | Repo propio en GitHub                                           | Distribución              |

### Perfil del proyecto

Lo crea el PM en el kickoff con `/project-init` y queda versionado en el
repo del proyecto. Si cambia el alcance (nuevo modelo, nuevo uso del
dato, nuevo sector), el PM lo vuelve a lanzar.

.ai-act/profile.yaml

    client:
      name: Aseguradora Ejemplo
      sector: insurance-life-health   # decide los puntos del anexo III que aplican
    project:
      purpose: Modelo de propensión a la baja para campañas de retención
      deliverable_infers: true        # ML, LLM o scoring; false = pipeline o dashboard
      ai_type: [ml]                   # ml | llm | rules
      role: provider                  # provider | deployer | both (rol de la consultora)
      eu_affected: true
    personal_data: [contact, financial, health]
    stack: [dbt, bigquery]            # activa los adaptadores
    escalation:
      dpo: dpo@cliente.example
      legal: legal@consultora.example
      pm: pm@consultora.example
    classification:
      ai_act_level: high-risk-candidate   # prohibited | high-risk-candidate | transparency | minimal | out-of-scope
      reviewed: 2026-11-17

### Manifiesto

`.claude-plugin/plugin.json` con nombre, versión, descripción y autor.
La versión de la base normativa va aparte, en `knowledge/VERSION`, con
la fecha del consolidado que usa: hoy, AI Act consolidado de 2026-07-27,
con el Reglamento 2026/1744. Nombre propuesto: `ai-act-advisor`.

### Skills

Las de riesgo se cargan solas cuando Claude ve que encajan, o porque un
hook se lo sugiere. Las del PM se lanzan a mano.

| Skill                | Cómo se lanza          | Qué hace                                                                                                                                                                                                                                           |
|----------------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `project-init`       | `/project-init` (PM)   | Entrevista corta al PM. Si le pasas la propuesta o el SOW, rellena lo que encuentre. Escribe el perfil y una primera clasificación AI Act con sus fechas.                                                                                          |
| `risk-summary`       | `/risk-summary` (PM)   | Resumen de riesgos del proyecto en una página: clasificación, riesgos detectados, qué aplica ya y qué aplica después, y qué está pendiente de decidir y por quién.                                                                                 |
| `pii-masking`        | Automática (DE, AE)    | Ante PII: riesgo de no enmascarar, técnicas posibles y cuándo conviene cada una (seudonimización, hashing con sal, tokenización, generalización, masking dinámico del stack).                                                                      |
| `special-categories` | Automática             | Ante datos de salud, origen étnico, religión, etc., o variables que los aproximan (art. 9 RGPD). Explica también el art. 4 bis del AI Act cuando se usan para medir sesgos.                                                                        |
| `ai-act-classify`    | Automática             | Ante un modelo de scoring o propensión sobre personas: cruza la finalidad con el sector del perfil para ver si cae en el anexo III, revisa la excepción del art. 6.3 y el perfilado, y da las fechas (alto riesgo del anexo III desde 2027-12-02). |
| `ai-transparency`    | Automática             | Ante chatbots, agentes o contenido generado: comprueba el aviso de IA y el marcado (art. 50, aplicable desde 2026-08-02; marcado de sistemas anteriores desde 2026-12-02).                                                                         |
| `regulatory-update`  | Tarea semanal o a mano | Revisa las fuentes, compara con la base del plugin y prepara un PR con los cambios. Usa el agente `regulatory-watcher`.                                                                                                                            |

Todos los avisos de las skills de riesgo tienen la misma forma:

Ejemplo de aviso

    Riesgo: PII sin enmascarar en stg_customers (email, dni, fecha_nacimiento)
    Norma: RGPD art. 5.1.c (minimización) y art. 25 (protección desde el diseño) · aplica ya
    Qué puede pasar: exposición de datos personales en capas que no los necesitan
    Opciones: 1) seudonimizar dni con hash con sal  2) generalizar fecha_nacimiento a rango
              3) masking dinámico en BigQuery con policy tags  4) mantener y justificarlo
    Escalar a: no hace falta salvo que se exporte fuera de la UE (DPO)
    Base normativa 2026-07-27 · No es asesoramiento legal

### Hooks

Viven en `hooks/hooks.json` y solo añaden contexto.

- **`SessionStart`**: sin perfil, sugiere `/project-init`; con perfil,
  añade un resumen de tres líneas (sector, clasificación, datos
  personales); si la base normativa tiene más de 90 días, lo avisa.
- **`PostToolUse`** sobre `Read`, `Edit` y `Write` de `.sql`, `.py`,
  `.ipynb` y `.yml` de dbt: busca las señales del núcleo genérico y de
  los adaptadores del perfil, y si encuentra una nueva añade la señal,
  el fichero y la skill que conviene cargar.

<figure class="figwrap">
  <svg viewBox="0 0 760 328" role="img" aria-labelledby="aviso-title aviso-desc">
    <title id="aviso-title">Recorrido de un aviso</title>
    <desc id="aviso-desc">Un DE abre un fichero; el hook PostToolUse busca señales; si la señal es nueva en la sesión, Claude carga la skill, muestra el aviso con norma y opciones y el ingeniero decide. Si no, sigue sin aviso.</desc>
    <defs>
      <marker id="aviso-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon class="d-bar" points="0 0, 8 3, 0 6"/></marker>
    </defs>
    <line class="d-line" x1="168" y1="64" x2="208" y2="64" marker-end="url(#aviso-arrow)"/>
    <line class="d-line" x1="360" y1="64" x2="400" y2="64" marker-end="url(#aviso-arrow)"/>
    <line class="d-line" x1="552" y1="64" x2="592" y2="64" marker-end="url(#aviso-arrow)"/>
    <rect class="d-mask" x="562" y="42" width="20" height="14"/>
    <text class="d-tm d-mid" x="572" y="53">SÍ</text>
    <line class="d-dash" x1="476" y1="88" x2="476" y2="160" marker-end="url(#aviso-arrow)"/>
    <rect class="d-mask" x="484" y="117" width="24" height="14"/>
    <text class="d-tm" x="486" y="128">NO</text>
    <line class="d-line" x1="668" y1="88" x2="668" y2="160" marker-end="url(#aviso-arrow)"/>
    <line class="d-line" x1="668" y1="208" x2="668" y2="264" marker-end="url(#aviso-arrow)"/>
    <rect class="d-box" x="16" y="40" width="152" height="48"/>
    <text class="d-t d-mid" x="92" y="61">DE abre una tabla</text>
    <text class="d-tm d-mid" x="92" y="78">stg_customers.sql</text>
    <rect class="d-box" x="208" y="40" width="152" height="48"/>
    <text class="d-t d-mid" x="284" y="61">Busca señales</text>
    <text class="d-tm d-mid" x="284" y="78">PostToolUse</text>
    <g class="g-warn">
      <rect class="d-box" x="400" y="40" width="152" height="48"/>
      <text class="d-t d-mid" x="476" y="61">¿Señal nueva?</text>
      <text class="d-sm d-mid" x="476" y="78">1 vez por sesión</text>
    </g>
    <rect class="d-box" x="592" y="40" width="152" height="48"/>
    <text class="d-t d-mid" x="668" y="61">Carga la skill</text>
    <text class="d-tm d-mid" x="668" y="78">pii-masking</text>
    <rect class="d-box" x="400" y="160" width="152" height="48"/>
    <text class="d-t d-mid" x="476" y="189">Sigue sin aviso</text>
    <rect class="d-box" x="592" y="160" width="152" height="48"/>
    <text class="d-t d-mid" x="668" y="181">Aviso al usuario</text>
    <text class="d-sm d-mid" x="668" y="198">norma y opciones</text>
    <g class="g-ok">
      <rect class="d-fill" x="592" y="264" width="152" height="48"/>
      <text class="d-t d-mid" x="668" y="293">Decide el DE o AE</text>
    </g>
  </svg>
  <figcaption>Ningún paso bloquea: el hook solo añade contexto y <strong>la decisión es del ingeniero</strong>.</figcaption>
</figure>

### Agentes

Uno: `regulatory-watcher`. Lee las cinco fuentes (EUR-Lex, Oficina de IA
de la Comisión, AESIA, AEPD y CEPD) y devuelve solo los cambios
relevantes. Va aparte para que la lectura de muchas páginas no llene el
contexto de la sesión.

### Base de conocimiento

Ficheros que leen a la vez los scripts de los hooks y las skills, para
que haya una sola fuente. `signals.yaml` parte de la sección 18 de la
investigación, filtrada a los cuatro riesgos del prototipo.

| Fichero                           | Contenido                                                               |
|-----------------------------------|-------------------------------------------------------------------------|
| `knowledge/VERSION`               | Fecha del consolidado y de la última revisión                           |
| `knowledge/dates.yaml`            | Fechas de aplicación por artículo (art. 113 y 111)                      |
| `knowledge/signals.yaml`          | Núcleo genérico: patrón → riesgo → norma → artículo → severidad → skill |
| `knowledge/sectors.yaml`          | Sector del cliente → puntos del anexo III que pueden aplicar            |
| `knowledge/masking-techniques.md` | Técnicas de enmascaramiento, ventajas, límites y cuándo usar cada una   |
| `knowledge/sources.yaml`          | Las cinco fuentes con su URL y la fecha de la última comprobación       |
| `adapters/<stack>/`               | Señales y ejemplos de mitigación propios de cada stack                  |

### Actualización de la base normativa

<figure class="figwrap">
  <svg viewBox="0 0 760 352" role="img" aria-labelledby="update-title update-desc">
    <title id="update-title">Ciclo de actualización normativa</title>
    <desc id="update-desc">Cada semana el vigilante normativo revisa cinco fuentes; si hay cambios abre un PR que Andrés revisa y fusiona, la base de conocimiento se actualiza y los avisos salen con la fecha nueva. Si no hay cambios, espera a la semana siguiente. Si la base supera 90 días, SessionStart lo avisa.</desc>
    <defs>
      <marker id="update-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon class="d-bar" points="0 0, 8 3, 0 6"/></marker>
    </defs>
    <line class="d-line" x1="168" y1="80" x2="208" y2="80" marker-end="url(#update-arrow)"/>
    <line class="d-line" x1="360" y1="80" x2="400" y2="80" marker-end="url(#update-arrow)"/>
    <line class="d-line" x1="552" y1="80" x2="592" y2="80" marker-end="url(#update-arrow)"/>
    <rect class="d-mask" x="562" y="58" width="20" height="14"/>
    <text class="d-tm d-mid" x="572" y="69">SÍ</text>
    <path class="d-dash" d="M476 56 V36 a8 8 0 0 0 -8 -8 H100 a8 8 0 0 0 -8 8 V56" marker-end="url(#update-arrow)"/>
    <rect class="d-mask" x="248" y="8" width="72" height="14"/>
    <text class="d-tm d-mid" x="284" y="19">NO · ESPERA</text>
    <line class="d-line" x1="668" y1="104" x2="668" y2="176" marker-end="url(#update-arrow)"/>
    <line class="d-line" x1="592" y1="200" x2="552" y2="200" marker-end="url(#update-arrow)"/>
    <line class="d-line" x1="400" y1="200" x2="360" y2="200" marker-end="url(#update-arrow)"/>
    <line class="d-dash" x1="476" y1="224" x2="476" y2="288" marker-end="url(#update-arrow)"/>
    <rect class="d-mask" x="484" y="249" width="64" height="14"/>
    <text class="d-tm" x="488" y="260">RED SEGURA</text>
    <rect class="d-box" x="16" y="56" width="152" height="48"/>
    <text class="d-t d-mid" x="92" y="77">Tarea semanal</text>
    <text class="d-tm d-mid" x="92" y="94">regulatory-update</text>
    <rect class="d-box" x="208" y="56" width="152" height="48"/>
    <text class="d-t d-mid" x="284" y="77">Vigilante normativo</text>
    <text class="d-sm d-mid" x="284" y="94">5 fuentes</text>
    <g class="g-warn">
      <rect class="d-box" x="400" y="56" width="152" height="48"/>
      <text class="d-t d-mid" x="476" y="85">¿Hay cambios?</text>
    </g>
    <rect class="d-box" x="592" y="56" width="152" height="48"/>
    <text class="d-t d-mid" x="668" y="77">PR con el resumen</text>
    <text class="d-tm d-mid" x="668" y="94">knowledge/</text>
    <g class="g-ok">
      <rect class="d-fill" x="592" y="176" width="152" height="48"/>
      <text class="d-t d-mid" x="668" y="197">Andrés revisa</text>
      <text class="d-sm d-mid" x="668" y="214">y fusiona</text>
    </g>
    <rect class="d-box" x="400" y="176" width="152" height="48"/>
    <text class="d-t d-mid" x="476" y="197">Base actualizada</text>
    <text class="d-tm d-mid" x="476" y="214">knowledge/VERSION</text>
    <rect class="d-box" x="208" y="176" width="152" height="48"/>
    <text class="d-t d-mid" x="284" y="205">Avisos al día</text>
    <rect class="d-box" x="400" y="288" width="152" height="48"/>
    <text class="d-t d-mid" x="476" y="309">Alerta a 90 días</text>
    <text class="d-tm d-mid" x="476" y="326">SessionStart</text>
  </svg>
  <figcaption>Nada entra en la base sin <strong>revisión humana</strong>. La alerta de 90 días cubre el caso de que la tarea deje de funcionar.</figcaption>
</figure>

### MCP, LSP y distribución

- **MCP**: ninguno en el prototipo. Después, Jira o Confluence para leer
  el SOW y dejar el resumen de riesgos, y el catálogo del data warehouse
  para leer esquemas y etiquetas de columnas.
- **LSP**: no aporta nada a este plugin.
- **Distribución**: por ahora en el repo personal
  `AS-prog/ai-act-advisor`, todo en español. Si va a un marketplace
  propio se decide después del prototipo.

### Versión madura: MCP de documentación normativa

Cuando el prototipo funcione, un servidor MCP con toda la documentación
normativa indexada con embeddings, para contrastar cada aviso con el texto
original en lugar de fiarse solo de los resúmenes de `knowledge/`.

- **Qué indexa**: el AI Act consolidado y los reglamentos que lo
  modifican, las directrices y códigos de la Comisión, las guías y
  checklists de AESIA y las guías de AEPD y CEPD. Cada fragmento con su
  fuente, artículo o apartado y fecha.
- **Para qué**: que las skills citen el pasaje exacto en cada aviso, que
  el PM pueda preguntar en lenguaje natural («¿un modelo de propensión
  para una aseguradora es anexo III?») y que el vigilante normativo
  compare versiones de un mismo texto.
- **Herramientas previstas**: buscar pasajes por pregunta, traer un
  artículo por su número y contrastar una afirmación con los pasajes que
  la apoyan o la contradicen.
- **Actualización**: el índice se regenera con el mismo ciclo semanal y
  por el mismo PR que `knowledge/`.

> [!PENDING] versión madura
> Dónde corre el MCP (local o servicio), qué modelo de embeddings usa y
> cómo se reparte el índice con el plugin.

## Alternativas

- **Bloquear acciones de riesgo.** Descartado: la decisión es del
  ingeniero; el plugin informa.
- **Cubrir solo el AI Act.** Descartado: en proyectos de datos el riesgo
  más frecuente es RGPD y el plugin callaría casi siempre.
- **Checklist completo de AESIA en todos los proyectos.** Aplazado:
  entra solo cuando un proyecto salga candidato a alto riesgo.
- **Solo skills, sin hooks.** Descartado: una skill depende de que
  Claude decida cargarla; el hook garantiza que la señal se vea.
- **Actualizar la base sin revisión.** Descartado: una fecha mal leída
  haría avisar mal en todos los proyectos a la vez.

## Decisiones

| Pregunta | Decisión |
|---|---|
| Q1 | Para consultoras como Merkle, no solo Merkle |
| Q2 | AI Act como marco, bajando al RGPD |
| Q3 | Hooks para detectar, skills para explicar |
| Q4 | Varios stacks, elegidos al iniciar el proyecto |
| Q6 | El PM hace el triaje y ve el resumen de riesgos |
| Q7 | Un perfil por proyecto, versionado en el repo |
| Q8 | Sin IA, siguen los avisos del RGPD |
| Q9 | Núcleo genérico más adaptadores por stack |
| Q10 | Los avisos de riesgo alto dicen a quién escalar |
| Q11 | Base normativa con fecha y búsqueda proactiva de cambios |
| Q12 | Todo en español |
| Q13 | Tarea semanal que abre un PR y alerta a 90 días |
| Q14 | EUR-Lex, Oficina de IA, AESIA, AEPD y CEPD |
| Q15 | Prototipo con PII, categorías especiales, scoring por sector y art. 50 |
| Q16 | Sin stack fijo: `project-init` audita el repo, detecta los entornos y el PM confirma |
| Q17 | Nombre `ai-act-advisor` |
| Q18 | Repo personal hasta después del prototipo |
| Q20 | Hooks y auditoría en Python sin dependencias |
| Q22 | Licencia MIT |
| — | Versión madura con un MCP de documentación normativa y embeddings |

## Pendiente

> [!PENDING] Q5
> Cuánto ruido es aceptable y si las decisiones del ingeniero quedan en un
> registro del repo. Se decide al probar el prototipo.

> [!PENDING] Q19
> Primer corte del prototipo. La auditoría de un repo real apunta a la PII
> en la ingesta.
