---
title: Demo de ai-act-advisor de punta a punta
description: Guion para probar el plugin entero en una hora con un proyecto ficticio, paso a paso por rol (PM, DE y AE), con qué pedirle a Claude, qué debe pasar y qué apuntar.
date: 2026-11-17
status: vigente
---

# Demo de ai-act-advisor de punta a punta

Guion para probar el plugin entero con un proyecto ficticio: catorce pasos repartidos entre PM, data engineer (DE) y analytics engineer (AE), que ejercitan las siete skills, el agente, los dos hooks y la línea base. Cada paso dice qué pedirle a Claude, qué debe pasar y qué decidir.

## En corto

- **Duración**: una hora, o 45 minutos sin el paso 14 (necesita internet y tarda).
- **Quién**: una persona puede hacer los tres roles. Al cambiar de rol se cierra Claude Code y se vuelve a abrir, para que empiece una sesión nueva.
- **Qué hace falta**: Claude Code, Python 3 y git. Nada más: el plugin no tiene dependencias.
- **Datos**: ninguno. El proyecto es ficticio y no trae ficheros de datos; el plugin solo lee código y configuración.
- **Antes, sin Claude**: `python3 examples/demo/ensayo.py` recorre el guion con la auditoría y los hooks reales y comprueba que cada aviso sale donde debe (27 comprobaciones, un par de segundos).

## El escenario

*Electrodomésticos Ejemplo, S.L.* (inventada) vende en tiendas y online. La consultora le construye una medallion de clientes y ventas, y le entrega cada semana un fichero de audiencias a un socio de medios. Es el proyecto de `examples/medallion-demo`, hecho para que salga lo que vimos en proyectos reales.

La demo tiene dos fases. En la primera el proyecto solo mueve y agrega datos: el riesgo es de RGPD y el proyecto queda fuera del AI Act. En la segunda el cliente pide tres cosas nuevas, y con ellas llega el AI Act:

1. Un **modelo de impago** que decide en la web quién puede pagar a plazos. Puntúa la solvencia de personas físicas: candidato a alto riesgo (anexo III, punto 5.b), aunque el sector del cliente no tenga punto propio.
2. Un **asistente para el chat de la web** que responde con un modelo de lenguaje: transparencia del art. 50.
3. Una **encuesta de accesibilidad** que marketing quiere cruzar con clientes: datos de salud, categoría especial del art. 9 del RGPD.

<figure class="figwrap">
  <svg viewBox="0 0 720 372" role="img" aria-labelledby="esc-title esc-desc">
  <title id="esc-title">El proyecto ficticio de la demo y dónde salta cada aviso</title>
  <desc id="esc-desc">Fase 1: el CRM en PostgreSQL y un libro de SharePoint entran en Bronze, pasan a Silver y a Gold, y Gold entrega un fichero a un socio de medios en Google Cloud Storage. Fase 2: el cliente añade solicitudes de pago a plazos, dependencias de ML y de LLM, una encuesta de accesibilidad, un modelo de impago y un asistente para la web. Cada elemento lleva el número del paso del guion en el que avisa el plugin.</desc>
  <defs><marker id="esc-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon class="d-bar" points="0 0, 8 3, 0 6"/></marker></defs>
  <rect class="d-wash-1" x="8" y="8" width="704" height="186"/>
  <rect class="d-wash-2" x="8" y="206" width="704" height="158"/>
  <text class="d-tm" x="20" y="28">FASE 1 · MEDALLION DE CLIENTES</text>
  <text class="d-tm" x="20" y="226">FASE 2 · EL CLIENTE PIDE IA</text>
  <line class="d-line" x1="166" y1="70" x2="196" y2="98" marker-end="url(#esc-arrow)"/>
  <line class="d-line" x1="166" y1="146" x2="196" y2="118" marker-end="url(#esc-arrow)"/>
  <line class="d-line" x1="340" y1="108" x2="372" y2="108" marker-end="url(#esc-arrow)"/>
  <line class="d-line" x1="516" y1="100" x2="548" y2="76" marker-end="url(#esc-arrow)"/>
  <line class="d-line" x1="624" y1="96" x2="624" y2="132" marker-end="url(#esc-arrow)"/>
  <rect class="d-box" x="24" y="48" width="142" height="44"/>
  <text class="d-t d-mid" x="95" y="67">CRM PostgreSQL</text>
  <text class="d-tm d-mid" x="95" y="84">subscriptions</text>
  <rect class="d-box" x="24" y="124" width="142" height="44"/>
  <text class="d-t d-mid" x="95" y="143">SharePoint</text>
  <text class="d-tm d-mid" x="95" y="160">campaign_contacts</text>
  <rect class="d-box" x="200" y="86" width="140" height="44"/>
  <text class="d-t d-mid" x="270" y="105">Bronze</text>
  <text class="d-tm d-mid" x="270" y="122">Delta, solo añade</text>
  <rect class="d-box" x="376" y="86" width="140" height="44"/>
  <text class="d-t d-mid" x="446" y="105">Silver</text>
  <text class="d-tm d-mid" x="446" y="122">build_customers</text>
  <rect class="d-box" x="552" y="52" width="144" height="44"/>
  <text class="d-t d-mid" x="624" y="71">Gold</text>
  <text class="d-tm d-mid" x="624" y="88">customers_by_age</text>
  <rect class="d-box" x="552" y="136" width="144" height="44"/>
  <text class="d-t d-mid" x="624" y="155">Socio de medios</text>
  <text class="d-tm d-mid" x="624" y="172">exporta a GCS</text>
  <circle class="d-fill" cx="166" cy="48" r="11"/>
  <text class="d-tm d-mid" x="166" y="52">2</text>
  <circle class="d-fill" cx="166" cy="124" r="11"/>
  <text class="d-tm d-mid" x="166" y="128">5</text>
  <circle class="d-fill" cx="340" cy="86" r="11"/>
  <text class="d-tm d-mid" x="340" y="90">2</text>
  <circle class="d-fill" cx="516" cy="86" r="11"/>
  <text class="d-tm d-mid" x="516" y="90">4</text>
  <circle class="d-fill" cx="696" cy="52" r="11"/>
  <text class="d-tm d-mid" x="696" y="56">6</text>
  <circle class="d-fill" cx="696" cy="136" r="11"/>
  <text class="d-tm d-mid" x="696" y="140">3</text>
  <rect class="d-box" x="24" y="246" width="142" height="44" stroke-dasharray="5 4"/>
  <text class="d-t d-mid" x="95" y="265">Solicitudes a plazos</text>
  <text class="d-tm d-mid" x="95" y="282">crm · finance</text>
  <rect class="d-box" x="200" y="246" width="140" height="44" stroke-dasharray="5 4"/>
  <text class="d-t d-mid" x="270" y="265">Dependencias</text>
  <text class="d-tm d-mid" x="270" y="282">pyproject.toml</text>
  <rect class="d-box" x="376" y="246" width="140" height="44" stroke-dasharray="5 4"/>
  <text class="d-t d-mid" x="446" y="265">Encuesta</text>
  <text class="d-tm d-mid" x="446" y="282">discapacidad</text>
  <rect class="d-box" x="552" y="240" width="144" height="44" stroke-dasharray="5 4"/>
  <text class="d-t d-mid" x="624" y="259">Modelo de impago</text>
  <text class="d-tm d-mid" x="624" y="276">scikit-learn</text>
  <rect class="d-box" x="552" y="302" width="144" height="44" stroke-dasharray="5 4"/>
  <text class="d-t d-mid" x="624" y="321">Asistente web</text>
  <text class="d-tm d-mid" x="624" y="338">anthropic</text>
  <circle class="d-fill" cx="166" cy="246" r="11"/>
  <text class="d-tm d-mid" x="166" y="250">9</text>
  <circle class="d-fill" cx="340" cy="246" r="11"/>
  <text class="d-tm d-mid" x="340" y="250">8</text>
  <circle class="d-fill" cx="516" cy="246" r="11"/>
  <text class="d-tm d-mid" x="516" y="250">11</text>
  <circle class="d-fill" cx="696" cy="240" r="11"/>
  <text class="d-tm d-mid" x="696" y="244">12</text>
  <circle class="d-fill" cx="696" cy="302" r="11"/>
  <text class="d-tm d-mid" x="696" y="306">10</text>
  </svg>
  <figcaption>El proyecto de la demo. Cada número es el paso del guion en el que el plugin avisa de ese elemento. Lo de la fase 2 (en trazo discontinuo) lo añade <code>preparar.py --fase 2</code>.</figcaption>
</figure>

## Qué ejercita cada paso

<figure class="figwrap">
  <svg viewBox="0 0 720 364" role="img" aria-labelledby="cob-title cob-desc">
  <title id="cob-title">Qué parte del plugin ejercita cada paso del guion</title>
  <desc id="cob-desc">Matriz de catorce pasos por once piezas del plugin. Los pasos 1 a 7 son la fase 1, los 8 a 13 la fase 2 y el 14 el mantenimiento. Las siete skills, el agente, los dos hooks y la línea base salen al menos una vez. En el paso 4 el hook debe callar porque el riesgo ya está en la línea base.</desc>
  <rect class="d-wash-1" x="196" y="8" width="252" height="348"/>
  <rect class="d-wash-2" x="448" y="8" width="216" height="348"/>
  <rect class="d-wash-1" x="664" y="8" width="36" height="348"/>
  <text class="d-tm d-mid" x="322" y="26">FASE 1</text>
  <text class="d-tm d-mid" x="556" y="26">FASE 2</text>
  <text class="d-tm d-mid" x="682" y="26">MANT.</text>
  <text class="d-t d-mid" x="214" y="52">1</text>
  <text class="d-tm d-mid" x="214" y="72">PM</text>
  <text class="d-t d-mid" x="250" y="52">2</text>
  <text class="d-tm d-mid" x="250" y="72">PM</text>
  <text class="d-t d-mid" x="286" y="52">3</text>
  <text class="d-tm d-mid" x="286" y="72">PM</text>
  <text class="d-t d-mid" x="322" y="52">4</text>
  <text class="d-tm d-mid" x="322" y="72">DE</text>
  <text class="d-t d-mid" x="358" y="52">5</text>
  <text class="d-tm d-mid" x="358" y="72">DE</text>
  <text class="d-t d-mid" x="394" y="52">6</text>
  <text class="d-tm d-mid" x="394" y="72">AE</text>
  <text class="d-t d-mid" x="430" y="52">7</text>
  <text class="d-tm d-mid" x="430" y="72">PM</text>
  <text class="d-t d-mid" x="466" y="52">8</text>
  <text class="d-tm d-mid" x="466" y="72">DE</text>
  <text class="d-t d-mid" x="502" y="52">9</text>
  <text class="d-tm d-mid" x="502" y="72">DE</text>
  <text class="d-t d-mid" x="538" y="52">10</text>
  <text class="d-tm d-mid" x="538" y="72">DE</text>
  <text class="d-t d-mid" x="574" y="52">11</text>
  <text class="d-tm d-mid" x="574" y="72">AE</text>
  <text class="d-t d-mid" x="610" y="52">12</text>
  <text class="d-tm d-mid" x="610" y="72">PM</text>
  <text class="d-t d-mid" x="646" y="52">13</text>
  <text class="d-tm d-mid" x="646" y="72">PM</text>
  <text class="d-t d-mid" x="682" y="52">14</text>
  <text class="d-tm d-mid" x="682" y="72">MT</text>
  <line class="d-dash" x1="16" y1="92" x2="700" y2="92"/>
  <text class="d-tm" x="16" y="108">SessionStart</text>
  <line class="d-dash" x1="16" y1="116" x2="700" y2="116"/>
  <text class="d-tm" x="16" y="132">PostToolUse</text>
  <line class="d-dash" x1="16" y1="140" x2="700" y2="140"/>
  <text class="d-tm" x="16" y="156">línea base</text>
  <line class="d-dash" x1="16" y1="164" x2="700" y2="164"/>
  <text class="d-tm" x="16" y="180">project-init</text>
  <line class="d-dash" x1="16" y1="188" x2="700" y2="188"/>
  <text class="d-tm" x="16" y="204">pii-masking</text>
  <line class="d-dash" x1="16" y1="212" x2="700" y2="212"/>
  <text class="d-tm" x="16" y="228">special-categories</text>
  <line class="d-dash" x1="16" y1="236" x2="700" y2="236"/>
  <text class="d-tm" x="16" y="252">ai-transparency</text>
  <line class="d-dash" x1="16" y1="260" x2="700" y2="260"/>
  <text class="d-tm" x="16" y="276">ai-act-classify</text>
  <line class="d-dash" x1="16" y1="284" x2="700" y2="284"/>
  <text class="d-tm" x="16" y="300">risk-summary</text>
  <line class="d-dash" x1="16" y1="308" x2="700" y2="308"/>
  <text class="d-tm" x="16" y="324">regulatory-update</text>
  <line class="d-dash" x1="16" y1="332" x2="700" y2="332"/>
  <text class="d-tm" x="16" y="348">regulatory-watcher</text>
  <circle class="d-bar" cx="214" cy="104" r="6"/>
  <circle class="d-bar" cx="250" cy="176" r="6"/>
  <circle class="d-bar" cx="250" cy="152" r="6"/>
  <circle class="d-bar" cx="286" cy="152" r="6"/>
  <circle class="d-bar" cx="322" cy="104" r="6"/>
  <circle class="d-box" cx="322" cy="128" r="6"/>
  <circle class="d-bar" cx="358" cy="128" r="6"/>
  <circle class="d-bar" cx="358" cy="200" r="6"/>
  <circle class="d-bar" cx="394" cy="128" r="6"/>
  <circle class="d-bar" cx="394" cy="200" r="6"/>
  <circle class="d-bar" cx="430" cy="296" r="6"/>
  <circle class="d-bar" cx="466" cy="128" r="6"/>
  <circle class="d-bar" cx="502" cy="128" r="6"/>
  <circle class="d-bar" cx="502" cy="200" r="6"/>
  <circle class="d-bar" cx="538" cy="128" r="6"/>
  <circle class="d-bar" cx="538" cy="248" r="6"/>
  <circle class="d-bar" cx="574" cy="128" r="6"/>
  <circle class="d-bar" cx="574" cy="224" r="6"/>
  <circle class="d-bar" cx="610" cy="128" r="6"/>
  <circle class="d-bar" cx="610" cy="272" r="6"/>
  <circle class="d-bar" cx="610" cy="152" r="6"/>
  <circle class="d-bar" cx="646" cy="176" r="6"/>
  <circle class="d-bar" cx="646" cy="296" r="6"/>
  <circle class="d-bar" cx="646" cy="152" r="6"/>
  <circle class="d-bar" cx="682" cy="104" r="6"/>
  <circle class="d-bar" cx="682" cy="320" r="6"/>
  <circle class="d-bar" cx="682" cy="344" r="6"/>
  </svg>
  <figcaption>Cada punto es una pieza del plugin que entra en juego en ese paso. El círculo hueco del paso 4 es una comprobación al revés: el hook debe <strong>callar</strong>, porque el riesgo ya está en la línea base. MT es mantenimiento.</figcaption>
</figure>

## Antes de empezar

**1. Clona el repo del plugin** y sitúate en la rama que quieras probar.

**2. Ensaya sin Claude.** Si algo falla aquí, fallará en vivo:

```text
python3 examples/demo/ensayo.py
```

**3. Prepara la carpeta de trabajo.** Copia el proyecto ficticio fuera del repo del plugin y hace `git init`:

```text
python3 examples/demo/preparar.py --dest ~/ai-act-demo
```

**4. Abre Claude Code** en esa carpeta con el plugin de tu rama:

```text
cd ~/ai-act-demo
claude --plugin-dir <ruta-del-clon>/plugins/ai-act-advisor
```

> [!IMPORTANT]
> Si ya tienes instalado `ai-act-advisor` desde el marketplace, desactívalo durante la demo (`/plugin`, pestaña de instalados), para que no avisen dos copias a la vez.

En Windows usa `python` si no tienes `python3`, y en PowerShell la variable del paso 14 se pone con `$env:AI_ACT_KNOWLEDGE="…"` antes de lanzar `claude`. Los hooks se lanzan con `sh`, que Claude Code trae con Git Bash.

## Fase 1 · Medallion de clientes

### Paso 1 · PM · Abrir el repo sin configurar

**Abre** Claude Code (ya lo hiciste en «Antes de empezar») y escribe:

> Hola, soy el PM de este proyecto. ¿Qué es este repo?

**Qué debe pasar**

- Claude resume el repo y te sugiere **una vez** lanzar `/project-init`, porque no hay perfil (`.ai-act/profile.yaml`).
- No insiste si sigues con otra cosa.

### Paso 2 · PM · Configurar el proyecto: /project-init

> /project-init

**Qué debe pasar**

1. Detecta que es un proyecto **encaminado** (hay código) y lanza la auditoría en modo consulta, que no escribe nada.
2. Te enseña los entornos (Delta Lake, DuckDB, PostgreSQL, SharePoint, Google Cloud Storage), las reglas del repo (clave de PII `pii_columns`, fuentes en `config/sources/`, escritura en Bronze, exportación) y los hallazgos: 7, de ellos 2 altos.
3. Te pregunta el perfil en pocas tandas.

Contesta con esto:

| Pregunta | Respuesta |
|---|---|
| Cliente y sector | Electrodomésticos Ejemplo, S.L. · `retail-marketing` |
| Finalidad | Medallion de clientes y ventas; entrega de audiencias a un socio de medios. No infiere |
| Rol de la consultora | Responsable del despliegue (no hay sistema de IA todavía) |
| Datos personales | Contacto e historial de compras |
| Stack | El que propone la auditoría |
| Contactos | DPO `dpo@cliente.example`, legal `legal@consultora.example`, PM `pm@consultora.example` |
| Repos | Solo este |

Confirma los hallazgos sin corregir nada. Después:

- Escribe `.ai-act/profile.yaml`, `.ai-act/rules.json`, `.ai-act/baseline.json` y `.ai-act/audits/AAAA-MM-DD.md`.
- Cierra con un resumen de cinco líneas: clasificación inicial **fuera de alcance** del AI Act (siguen los avisos del RGPD), hallazgos por severidad y los dos que mirar primero (`pii_columns` que nadie aplica y la exportación al socio), con su skill.

El perfil esperado está en `examples/demo/perfil.yaml`, por si quieres compararlo.

### Paso 3 · PM · Registrar una decisión

> Marca la exportación al socio de medios como aceptada en la línea base: hay contrato de encargado firmado y el bucket está en la UE. Lo decido yo, el PM.

**Qué debe pasar**

- Claude cambia en `.ai-act/baseline.json` el hallazgo `external-export:…` a `aceptado`, con esa justificación.
- No toca el código.

### Paso 4 · DE · Abrir sesión y leer código ya revisado

Cierra Claude Code (`/exit`) y vuelve a abrirlo con el mismo comando. Ahora eres DE.

> Soy DE. Explícame qué hace transform/silver/build_customers.py.

**Qué debe pasar**

- Al abrir, Claude conoce el perfil (sector, fuera de alcance, datos de contacto) y sabe que hay hallazgos altos abiertos, pero **no** los repite si no trabajas en ellos.
- Al leer el fichero **no hay aviso**: las columnas `email`, `phone` y `birth_date` ya están en la línea base desde el paso 2. Este paso comprueba que el plugin calla lo ya visto.

### Paso 5 · DE · Añadir una fuente sin declarar la PII

> Añade a config/sources/sharepoint.yaml un objeto newsletter_signups de la biblioteca Marketing, hoja altas_newsletter, activo.

**Qué debe pasar**

- Claude hace el cambio y te avisa en pocas líneas: objeto `newsletter_signups` sin `pii_columns`, RGPD art. 5.1.c, 25 y 30, aplica ya, skill `pii-masking`, con la fecha de la base normativa y «no es asesoramiento legal».
- No repite `campaign_contacts`, que ya estaba en la línea base, y no bloquea nada.

Pide el detalle:

> ¿Qué hago con esto?

- Claude carga `pii-masking`: explica el riesgo, propone revisar el esquema de origen y declarar `pii_columns`, y debería notar el comentario del fichero (el registro de SharePoint no admite `pii_columns`).
- **Decide** tú: declararlo, dejarlo pendiente o anotarlo como aceptado con justificación.

### Paso 6 · AE · Crear un modelo en Gold con un dato personal

Cierra y vuelve a abrir Claude Code. Ahora eres AE.

> Soy AE. Crea transform/gold/customers_by_age.sql que cuente clientes por ciudad y edad a partir de silver_customers.

**Qué debe pasar**

- Al escribir el fichero, aviso de **dato personal** (`birth_date`) con la skill `pii-masking`.

> ¿Cómo lo dejo sin dato personal en Gold?

- `pii-masking` propone generalizar (tramos de edad, calcularla en Silver y no llevar `birth_date` a Gold) y agregar con un mínimo de personas por grupo, adaptado a DuckDB.
- **Decide** si aplicas el cambio.

### Paso 7 · PM · Ver el estado: /risk-summary

Cierra y vuelve a abrir Claude Code como PM.

> /risk-summary

**Qué debe pasar**

Una página con la cabecera (proyecto, `retail-marketing`, fuera de alcance), el hallazgo alto abierto (`pii_columns` que nadie aplica), la tabla de los de severidad media, los **nuevos sin registrar** de los pasos 5 y 6, la exportación **aceptada** con su justificación, qué escalar al DPO (aplicar `pii_columns`, supresión y retención) y qué aplica ya (todo el RGPD).

## Fase 2 · El cliente pide IA

En un terminal aparte, aplica la fase 2 sobre la misma carpeta:

```text
python3 examples/demo/preparar.py --fase 2 --dest ~/ai-act-demo
```

Añade cuatro ficheros: la fuente nueva en `config/sources/crm_postgres.yaml`, el modelo `ml/instalment_scoring.py`, el asistente `assistant/support_bot.py` y la encuesta `accessibility_survey.sql` en Silver. Las dependencias no se copian: las pides tú en el paso 8.

> [!IMPORTANT]
> En esta fase, **no relances `/project-init` hasta el paso 13**, aunque Claude lo sugiera en el paso 8. La auditoría mete en la línea base todo lo que encuentra y los hooks callan lo que está en la línea base, así que los avisos de los pasos 9 a 12 ya no saldrían. Está apuntado como D20 en los pendientes.

### Paso 8 · DE · Añadir dependencias de ML y LLM

Abre Claude Code como DE.

> Añade scikit-learn y anthropic a las dependencias de pyproject.toml.

**Qué debe pasar**

- Al editar, aviso de **entornos nuevos** que la auditoría no tenía: «SDK de LLM» y «Librerías de ML». Sugiere al PM relanzar `/project-init` (déjalo para el paso 13).

### Paso 9 · DE · Revisar la fuente de las solicitudes a plazos

> Revisa config/sources/crm_postgres.yaml: hay un objeto nuevo para el modelo de impago.

**Qué debe pasar**

- Aviso de `instalment_applications` sin `pii_columns`, con `pii-masking`. Son datos financieros de personas: el DE debería declararlos antes de llevarlos a Bronze.

### Paso 10 · DE · Revisar el asistente de la web

> Revisa assistant/support_bot.py: es el chat de atención al cliente de la web.

**Qué debe pasar**

- Aviso **alto**: uso de un modelo de lenguaje, AI Act art. 50, aplica ya (desde 2026-08-02), escalar al PM, skill `ai-transparency`.

> ¿Qué tenemos que hacer para cumplir el art. 50?

- `ai-transparency` sitúa el chat en el 50.1 (interactúa con personas), dice que la obligación es del proveedor, explica si aplica o no el marcado del 50.2 a sus respuestas y propone un aviso al empezar la conversación («Soy un asistente automático…»).
- **Decide** si lo implementas y regístralo.

### Paso 11 · AE · Revisar la encuesta de accesibilidad

Cierra y vuelve a abrir Claude Code como AE.

> Revisa transform/silver/accessibility_survey.sql: marketing quiere cruzarla con clientes para campañas de productos adaptados.

**Qué debe pasar**

- Aviso **alto** de posibles categorías especiales (`discapacidad`), RGPD art. 9, escalar al DPO, skill `special-categories`, y uno medio por `postal_code`.

> /special-categories

- Clasifica `discapacidad` como dato de salud y debería ver también `movilidad_reducida` y `necesita_ayuda_en_tienda`, aunque la señal no los nombre.
- Explica que cruzarla con clientes para campañas necesita una excepción del art. 9.2 (en la práctica, consentimiento explícito), propone alternativas (agregar por tienda, no cruzar con clientes, quitar columnas) y termina **siempre** en el DPO.

### Paso 12 · DE y PM · Revisar y clasificar el modelo de impago

Como DE, en la misma sesión o en una nueva:

> Revisa ml/instalment_scoring.py.

**Qué debe pasar**

- Aviso **alto**: modelo que puntúa o clasifica, posiblemente sobre personas, AI Act art. 6 y anexo III, aplica desde 2027-12-02, escalar al PM, skill `ai-act-classify`.

Cierra y vuelve a abrir como PM:

> /ai-act-classify para el modelo de impago de ml/instalment_scoring.py

- Recorre el árbol: no es práctica prohibida (art. 5); el sector `retail-marketing` no tiene punto propio, pero la finalidad (decidir quién paga a plazos) evalúa la solvencia de personas físicas, así que es **candidato a alto riesgo por el punto 5.b**; la excepción del art. 6.3 no salva un sistema que elabora perfiles.
- Pregunta por el rol: proveedor es quien lo pone en servicio con su nombre (probablemente el cliente); la consultora lo desarrolla.
- Dice desde cuándo aplica (2027-12-02) y menciona la evaluación de impacto (FRIA, art. 27) para el responsable del despliegue de un sistema del 5.b.
- Te pide confirmación. **Confirma**: cambia `classification.ai_act_level` a `high-risk-candidate` en el perfil y registra el hallazgo `scoring-model` en la línea base con su justificación.

### Paso 13 · PM · Relanzar la auditoría y ver el estado

> /project-init

- Como ya hay perfil, no vuelve a preguntarlo todo: enseña el perfil, pregunta qué ha cambiado (ahora infiere: ML y LLM) y relanza la auditoría.
- Los hallazgos nuevos desde la fase 1: modelo que puntúa, SDK de LLM, categorías especiales, `postal_code` en la encuesta e `instalment_applications`.

> /risk-summary y guárdalo

- Cabecera con clasificación **candidato a alto riesgo**.
- Altos abiertos: categorías especiales (DPO), asistente con LLM (PM) y `pii_columns` sin aplicar (DPO).
- Aceptados con justificación: exportación y modelo de impago.
- Qué aplica ya (RGPD, art. 50 desde 2026-08-02) y qué después (anexo III desde 2027-12-02).
- Lo guarda en `.ai-act/risk-summary.md` porque se lo pediste.

## Mantenimiento

### Paso 14 · Base normativa antigua y /regulatory-update

Prepara una copia de la base normativa con la revisión de hace 120 días (se crea junto a la carpeta de trabajo, no dentro):

```text
python3 examples/demo/preparar.py --base-antigua --dest ~/ai-act-demo
cd ~/ai-act-demo
AI_ACT_KNOWLEDGE=~/ai-act-demo-base-antigua claude --plugin-dir <ruta-del-clon>/plugins/ai-act-advisor
```

**Qué debe pasar**

- Al abrir, Claude sabe que la base tiene 120 días y sugiere `/regulatory-update`.

Después, en el **clon del plugin** (no en la carpeta de la demo), con internet:

> /regulatory-update. Solo quiero el informe: no abras rama ni PR.

- Lanza el agente `regulatory-watcher`, que lee las fuentes de `knowledge/sources.yaml` en solo lectura.
- Devuelve las fuentes leídas y no leídas, los cambios confirmados (con URL y cita literal), los que quedan por verificar y las novedades sin efecto. Sin tu permiso no crea la rama `regulatory/AAAA-MM-DD`.

## Qué apuntar durante la demo

La demo sirve para afinar el plugin. Apunta en cada paso:

| Qué mirar | Por qué importa |
|---|---|
| ¿Salió el aviso? ¿Y en el momento justo? | Si no sale, es un fallo; si sale tarde, Claude ya no lo encaja con lo que haces |
| ¿Claude lo contó en pocas líneas y siguió con tu tarea? | El plugin nunca debe estorbar (D01, ruido) |
| ¿Hubo avisos que sobraban o falsos positivos? | Van a `exclusions` o a ajustar señales |
| ¿La skill propuso opciones del stack del proyecto (Delta, DuckDB, PostgreSQL)? | Las opciones genéricas no ayudan al DE |
| ¿Citó norma, artículo, fecha de aplicación y fecha de la base? | Es la regla de todos los avisos |
| ¿Te dejó decidir? | Ningún paso debe imponer un cambio de código |

## Si algo no sale

- **No hay ningún aviso**: comprueba que el plugin está cargado (`/plugin` lo lista) y que Python 3 está en el `PATH`. `python3 examples/demo/ensayo.py` dice si el fallo es del plugin o de la sesión.
- **Avisa dos veces de lo mismo**: hay dos copias del plugin activas (la del marketplace y la de `--plugin-dir`).
- **En la fase 2 no salen los avisos**: se relanzó `/project-init` antes de tiempo. Empieza de cero con `preparar.py --force` o borra la línea base (`.ai-act/baseline.json`) y vuelve al paso 2.
- **Claude no carga la skill**: pídesela por su nombre (`/pii-masking`, `/special-categories`…).

## Limpiar

Borra la carpeta de trabajo (`~/ai-act-demo`) y, si hiciste el paso 14, `~/ai-act-demo-base-antigua`. El repo del plugin no cambia.

## Más información

- [Cómo se usa](como-se-usa.html): la guía de uso, aviso a aviso.
- [Cómo funciona el prototipo en uso](../tecnica/uso-del-prototipo.html): qué hay por dentro.
- [Pendientes y dudas](../pendientes.html): D01 (ruido), D08 (scoring en el hook) y D20 (relanzar la auditoría).
