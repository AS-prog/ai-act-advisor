---
title: Cómo funciona el prototipo en uso
description: Recorrido paso a paso de una sesión con el prototipo sobre el proyecto de ejemplo, con las salidas reales, y por qué el plugin avisa o calla en cada momento.
date: 2026-11-17
code: ai-act-advisor@2d551c3
design: docs/documentos/diseno/propuesta-prototipo.md
decisions: Q5, Q16, Q19, Q20, Q21, Q23
---

# Cómo funciona el prototipo en uso

Recorrido paso a paso de una sesión con el prototipo sobre el proyecto de ejemplo `examples/medallion-demo`, con las salidas reales que recibe Claude, y por qué el plugin avisa o calla en cada momento.

## En una frase {#en-una-frase}

El prototipo audita un repo de datos en solo lectura, deduce sus propias reglas (dónde declara las fuentes, con qué clave marca la PII, qué escribe en Bronze y qué exporta) y, mientras se trabaja, añade al contexto de Claude un aviso de RGPD solo cuando aparece un riesgo nuevo. No bloquea, no edita el código del proyecto, no abre datos ni secretos, y del AI Act solo detecta señales (SDK de LLM, scoring) para derivar a la skill que toca.

## Mapa general {#mapa}

<figure class="figwrap">
  <svg viewBox="0 0 720 260" role="img" aria-labelledby="mapa-title mapa-desc">
    <title id="mapa-title">Qué lee y qué escribe el prototipo</title>
    <desc id="mapa-desc">Los scripts del plugin leen el código y la configuración del repo y escriben su estado en la carpeta .ai-act. Añaden contexto a la sesión de Claude, que carga las skills. Datos, secretos y warehouses no se abren.</desc>
    <defs>
      <marker id="mapa-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon class="d-bar" points="0 0, 8 3, 0 6"/></marker>
    </defs>
    <rect class="d-wash-1" x="16" y="16" width="200" height="232"/>
    <text class="d-tm" x="28" y="32">PLUGIN</text>
    <rect class="d-wash-1" x="280" y="16" width="200" height="232"/>
    <text class="d-tm" x="292" y="32">REPO DEL PROYECTO</text>
    <line class="d-line" x1="116" y1="92" x2="116" y2="106" marker-end="url(#mapa-arrow)"/>
    <line class="d-line" x1="200" y1="120" x2="248" y2="120"/>
    <line class="d-line" x1="248" y1="120" x2="248" y2="68"/>
    <line class="d-line" x1="248" y1="68" x2="294" y2="68" marker-end="url(#mapa-arrow)"/>
    <rect class="d-mask" x="230" y="87" width="36" height="14"/>
    <text class="d-tm d-mid" x="248" y="98">LEE</text>
    <line class="d-line" x1="200" y1="144" x2="248" y2="144"/>
    <line class="d-line" x1="248" y1="144" x2="248" y2="196"/>
    <line class="d-line" x1="248" y1="196" x2="294" y2="196" marker-end="url(#mapa-arrow)"/>
    <rect class="d-mask" x="220" y="163" width="56" height="14"/>
    <text class="d-tm d-mid" x="248" y="174">ESCRIBE</text>
    <line class="d-line" x1="200" y1="132" x2="542" y2="132" marker-end="url(#mapa-arrow)"/>
    <rect class="d-mask" x="320" y="125" width="120" height="14"/>
    <text class="d-tm d-mid" x="380" y="136">AÑADE CONTEXTO</text>
    <line class="d-dash" x1="464" y1="68" x2="542" y2="68"/>
    <rect class="d-mask" x="487" y="61" width="32" height="14"/>
    <text class="d-tm d-mid" x="503" y="72">NO</text>
    <line class="d-line" x1="624" y1="156" x2="624" y2="236"/>
    <line class="d-line" x1="624" y1="236" x2="116" y2="236"/>
    <line class="d-line" x1="116" y1="236" x2="116" y2="222" marker-end="url(#mapa-arrow)"/>
    <rect class="d-mask" x="510" y="229" width="84" height="14"/>
    <text class="d-tm d-mid" x="552" y="240">CARGA SKILL</text>
    <rect class="d-box" x="32" y="44" width="168" height="48"/>
    <text class="d-t d-mid" x="116" y="65">Base de conocimiento</text>
    <text class="d-tm d-mid" x="116" y="82">knowledge/</text>
    <rect class="d-box" x="32" y="108" width="168" height="48"/>
    <text class="d-t d-mid" x="116" y="129">Auditoría y hooks</text>
    <text class="d-tm d-mid" x="116" y="146">audit.py · hook.py</text>
    <rect class="d-box" x="32" y="172" width="168" height="48"/>
    <text class="d-t d-mid" x="116" y="193">Skills</text>
    <text class="d-tm d-mid" x="116" y="210">skills/</text>
    <rect class="d-box" x="296" y="44" width="168" height="48"/>
    <text class="d-t d-mid" x="380" y="65">Código y configuración</text>
    <text class="d-tm d-mid" x="380" y="82">.py .sql .yaml .toml</text>
    <rect class="d-fill" x="296" y="172" width="168" height="48"/>
    <text class="d-t d-mid" x="380" y="193">Estado del plugin</text>
    <text class="d-tm d-mid" x="380" y="210">.ai-act/</text>
    <rect class="d-box" x="544" y="44" width="160" height="48"/>
    <text class="d-t d-mid" x="624" y="65">Datos y secretos</text>
    <text class="d-sm d-mid" x="624" y="82">nunca se abren</text>
    <rect class="d-box" x="544" y="108" width="160" height="48"/>
    <text class="d-t d-mid" x="624" y="129">Sesión de Claude</text>
    <text class="d-sm d-mid" x="624" y="146">contexto añadido</text>
  </svg>
  <figcaption>Lo único que escribe el plugin en el repo es <code>.ai-act/</code>. Los hooks leen de ahí las reglas y la línea base en cada aviso.</figcaption>
</figure>

## Vocabulario {#vocabulario}

Perfil
: `.ai-act/profile.yaml`. Sector, finalidad, rol de la consultora, datos personales, stack y contactos de escalado. Lo escribe `/project-init` con el PM.

Reglas del repo
: `.ai-act/rules.json`. Lo que la auditoría deduce del propio repo: la clave con la que marca la PII (`pii_key`), las configuraciones de fuentes, los escritores de Bronze, las exportaciones, los entornos y las exclusiones de palabras.

Hallazgo
: Un riesgo concreto con su evidencia (rutas), norma, artículos, desde cuándo aplica, opción sugerida, a quién escalar y skill que ayuda. Tiene un id estable, por ejemplo `source-without-pii:70fdf1a3eb`.

Línea base
: `.ai-act/baseline.json`. Los hallazgos conocidos con su estado: `abierto`, `mitigado`, `aceptado` o `no detectado`.

Aviso
: El texto que un hook añade al contexto de Claude (`additionalContext`). Claude decide cuándo contárselo al usuario; el hook nunca decide nada.

## Cómo funciona {#como-funciona}

El recorrido usa el proyecto ficticio `examples/medallion-demo`: ingesta desde PostgreSQL y SharePoint, Bronze en Delta Lake, Silver con DuckDB y una exportación de Gold a un bucket de Google Cloud Storage de un socio. Las salidas son las que devuelve hoy el código, copiadas tal cual.

### 1. Antes de configurar: el plugin solo orienta

Al abrir Claude Code en un repo sin `.ai-act/`, el hook `SessionStart` añade una sola sugerencia:

```text
ai-act-advisor: este repo no tiene perfil AI Act/RGPD (.ai-act/profile.yaml). Si el usuario
trabaja con datos personales o modelos, sugiere una vez lanzar /project-init (configura el
proyecto y, si ya está encaminado, hace una auditoría de riesgos de solo lectura).
```

Sin reglas del repo, `PostToolUse` cae a la búsqueda de términos por palabra completa, con `_` como separador. Al leer `transform/silver/build_customers.py`:

```text
ai-act-advisor: señales de riesgo en `transform/silver/build_customers.py` (no están en la
línea base del proyecto). Cuéntaselo al usuario en pocas líneas cuando encaje con lo que está
haciendo; no bloquees su trabajo: la decisión es suya. Si quiere detalle, carga la skill indicada.
- [media] Columnas o campos con aspecto de dato personal (Términos: birth_date, email, phone)
  · RGPD art. 5.1.c, art. 25, art. 32 · aplica ya · skill pii-masking · id pii-terms:793ba1509f
  Opción sugerida: Comprueba si son datos personales reales y, si lo son, decide dónde se
  enmascaran o seudonimizan (skill pii-masking).
Base normativa 2026-07-27 (revisada 2026-11-17). No es asesoramiento legal.
El repo no tiene reglas propias (.ai-act/rules.json): sugiere una vez /project-init.
```

Palabras como `planificadas`, `predicate` o `schema_hash` no casan: `nif` tiene que ser un identificador completo (`cliente_nif` sí casa) y hay una lista de exclusiones en `knowledge/signals.yaml`.

### 2. /project-init: auditar, confirmar y escribir

<figure class="figwrap">
  <svg viewBox="0 0 720 112" role="img" aria-labelledby="init-title init-desc">
    <title id="init-title">Los tres pasos de /project-init en un proyecto encaminado</title>
    <desc id="init-desc">La auditoría en modo consulta no escribe nada. El PM confirma o corrige entornos, reglas y falsos positivos. Después se escriben reglas, línea base e informe.</desc>
    <defs>
      <marker id="init-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon class="d-bar" points="0 0, 8 3, 0 6"/></marker>
    </defs>
    <line class="d-line" x1="216" y1="52" x2="258" y2="52" marker-end="url(#init-arrow)"/>
    <line class="d-line" x1="456" y1="52" x2="498" y2="52" marker-end="url(#init-arrow)"/>
    <rect class="d-box" x="24" y="24" width="192" height="56"/>
    <text class="d-t d-mid" x="120" y="47">Auditoría en consulta</text>
    <text class="d-tm d-mid" x="120" y="65">audit.py scan</text>
    <rect class="d-box" x="264" y="24" width="192" height="56"/>
    <text class="d-t d-mid" x="360" y="47">El PM confirma</text>
    <text class="d-sm d-mid" x="360" y="65">entornos, reglas, falsos positivos</text>
    <rect class="d-fill" x="504" y="24" width="192" height="56"/>
    <text class="d-t d-mid" x="600" y="47">Estado escrito</text>
    <text class="d-tm d-mid" x="600" y="65">audit.py write</text>
    <text class="d-sm" x="24" y="100">no escribe nada</text>
    <text class="d-sm" x="504" y="100">solo dentro de .ai-act/</text>
  </svg>
  <figcaption>En un proyecto nuevo, sin código, solo hay entrevista y perfil, y el stack queda como <code>declarado</code> hasta que haya algo que auditar.</figcaption>
</figure>

La skill primero pregunta lo que falta del perfil (sector, finalidad, rol, datos personales, stack, contactos) rellenando antes con el README y `docs/`. Después ejecuta la auditoría en modo consulta. Sobre el ejemplo detecta cinco entornos y estas reglas:

| Regla | Valor deducido |
|---|---|
| Clave de PII | `pii_columns` (aparece en la configuración y en el código) |
| Configuración de fuentes | `config/sources/crm_postgres.yaml`, `config/sources/sharepoint.yaml` |
| Escritura en Bronze | `ingestion/bronze/writer.py` |
| Salidas fuera de la plataforma | `transform/gold/exports/partner_upload.py` |
| Dónde se lee la clave | `ingestion/common/registry.py` (solo la valida) |
| Entornos | Delta Lake, DuckDB, PostgreSQL, SharePoint, Google Cloud Storage |

Y siete hallazgos:

| Severidad | Hallazgo | Evidencia | Norma |
|---|---|---|---|
| alta | Entrega de datos fuera de la plataforma o a un tercero | `transform/gold/exports/partner_upload.py` | RGPD art. 28, arts. 44-49 |
| alta | «pii_columns» se declara pero ningún código lo aplica | `ingestion/common/registry.py` | RGPD art. 25, art. 32 |
| media | Bronze acepta columnas nuevas del origen sin revisión | `ingestion/bronze/writer.py` | RGPD art. 25, art. 5.1.c |
| media | Sin mecanismo de supresión ni de retención | `ingestion/bronze/writer.py` | RGPD art. 17, art. 5.1.e |
| media | Columnas con aspecto de dato personal | `transform/silver/build_customers.py` | RGPD art. 5.1.c, art. 25, art. 32 |
| media | Objeto «subscriptions» sin «pii_columns» | `config/sources/crm_postgres.yaml` | RGPD art. 5.1.c, art. 25, art. 30 |
| media | Objeto «campaign_contacts» sin «pii_columns» | `config/sources/sharepoint.yaml` | RGPD art. 5.1.c, art. 25, art. 30 |

El PM corrige lo que haga falta (un entorno que no es suyo, una palabra que en su repo no es PII y pasa a `exclusions`) y la skill escribe el estado con `audit.py write`: `.ai-act/rules.json`, `.ai-act/baseline.json` y `.ai-act/audits/2026-11-17.md`. Con el perfil escrito, la siguiente sesión arranca con un resumen en lugar de la sugerencia:

```text
ai-act-advisor: perfil del proyecto · sector insurance-life-health · clasificación AI Act
high-risk-candidate · datos personales contact, financial, health.
Línea base: 2 hallazgos de severidad alta abiertos (ver .ai-act/audits/). No los repitas salvo
que el usuario trabaje en ellos.
```

### 3. El trabajo diario: avisar solo de lo nuevo

<figure class="figwrap">
  <svg viewBox="0 0 720 244" role="img" aria-labelledby="hook-title hook-desc">
    <title id="hook-title">Qué decide PostToolUse antes de avisar</title>
    <desc id="hook-desc">Tras cada Read, Edit o Write, el hook comprueba que el fichero es del repo y de un tipo vigilado, aplica las comprobaciones con las reglas del repo, quita lo que está en la línea base y lo ya avisado en la sesión, y solo entonces añade un aviso.</desc>
    <defs>
      <marker id="hook-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon class="d-bar" points="0 0, 8 3, 0 6"/></marker>
    </defs>
    <line class="d-line" x1="216" y1="52" x2="258" y2="52" marker-end="url(#hook-arrow)"/>
    <line class="d-line" x1="456" y1="52" x2="498" y2="52" marker-end="url(#hook-arrow)"/>
    <rect class="d-mask" x="462" y="30" width="32" height="14"/>
    <text class="d-tm d-mid" x="478" y="41">SÍ</text>
    <line class="d-line" x1="600" y1="80" x2="600" y2="116"/>
    <line class="d-line" x1="600" y1="116" x2="120" y2="116"/>
    <line class="d-line" x1="120" y1="116" x2="120" y2="146" marker-end="url(#hook-arrow)"/>
    <line class="d-line" x1="216" y1="180" x2="258" y2="180" marker-end="url(#hook-arrow)"/>
    <line class="d-line" x1="456" y1="180" x2="498" y2="180" marker-end="url(#hook-arrow)"/>
    <rect class="d-mask" x="222" y="158" width="32" height="14"/>
    <text class="d-tm d-mid" x="238" y="169">NO</text>
    <rect class="d-mask" x="462" y="158" width="32" height="14"/>
    <text class="d-tm d-mid" x="478" y="169">NO</text>
    <rect class="d-box" x="24" y="24" width="192" height="56"/>
    <text class="d-t d-mid" x="120" y="47">Claude usa una herramienta</text>
    <text class="d-tm d-mid" x="120" y="65">Read · Edit · Write</text>
    <rect class="d-box" x="264" y="24" width="192" height="56"/>
    <text class="d-t d-mid" x="360" y="47">¿Fichero vigilado?</text>
    <text class="d-sm d-mid" x="360" y="65">del repo, sin secretos ni datos</text>
    <rect class="d-box" x="504" y="24" width="192" height="56"/>
    <text class="d-t d-mid" x="600" y="47">Comprobaciones</text>
    <text class="d-sm d-mid" x="600" y="65">con las reglas del repo</text>
    <text class="d-sm" x="264" y="98">no → silencio</text>
    <rect class="d-box" x="24" y="152" width="192" height="56"/>
    <text class="d-t d-mid" x="120" y="175">¿En la línea base?</text>
    <text class="d-tm d-mid" x="120" y="193">baseline.json</text>
    <rect class="d-box" x="264" y="152" width="192" height="56"/>
    <text class="d-t d-mid" x="360" y="175">¿Ya avisado?</text>
    <text class="d-sm d-mid" x="360" y="193">en esta sesión</text>
    <rect class="d-fill" x="504" y="152" width="192" height="56"/>
    <text class="d-t d-mid" x="600" y="175">Aviso en el contexto</text>
    <text class="d-sm d-mid" x="600" y="193">norma · fecha · skill</text>
    <text class="d-sm" x="24" y="228">sí → silencio</text>
    <text class="d-sm" x="264" y="228">sí → silencio</text>
  </svg>
  <figcaption>Tres filtros antes de hablar: tipo de fichero, línea base y memoria de la sesión. El ruido (Q5) se ajusta aquí.</figcaption>
</figure>

Con la línea base escrita, estas son las respuestas del hook a cuatro situaciones del ejemplo:

| Qué hace el ingeniero | Qué recibe Claude | Por qué |
|---|---|---|
| Edita `transform/gold/exports/partner_upload.py` | Nada | La exportación ya está en la línea base |
| Añade la tabla `complaints` a `crm_postgres.yaml` sin `pii_columns` | Un aviso, abajo | Es un objeto nuevo: su id no está en la línea base |
| Vuelve a editar el mismo fichero | Nada | Ese id ya se avisó en esta sesión |
| Añade `openai>=1.40` a `pyproject.toml` | Sugerencia de relanzar `/project-init` | Aparece un entorno (SDK de LLM) que la auditoría no tenía |

El aviso de la tabla nueva:

```text
ai-act-advisor: señales de riesgo en `config/sources/crm_postgres.yaml` (no están en la línea
base del proyecto). Cuéntaselo al usuario en pocas líneas cuando encaje con lo que está
haciendo; no bloquees su trabajo: la decisión es suya. Si quiere detalle, carga la skill indicada.
- [media] Objeto «complaints» sin «pii_columns» declarado · RGPD art. 5.1.c, art. 25, art. 30
  · aplica ya · skill pii-masking · id source-without-pii:70fdf1a3eb
  Opción sugerida: Revisa el esquema de origen de «complaints» antes de llevarlo a Bronze y
  declara «pii_columns» (aunque sea una lista vacía) para que conste que se revisó.
Base normativa 2026-07-27 (revisada 2026-11-17). No es asesoramiento legal.
```

Y el de la dependencia nueva:

```text
ai-act-advisor: en `pyproject.toml` aparecen entornos que la auditoría no tenía (SDK de LLM).
Sugiere al PM relanzar /project-init para actualizar las reglas.
```

Si el ingeniero pide detalle, Claude carga `pii-masking`, que explica el riesgo, propone dos o tres técnicas de `knowledge/masking-techniques.md` según el stack y la capa (por ejemplo, aplicar `pii_columns` en el escritor de Bronze o seudonimizar con HMAC en la frontera Bronze → Silver) y deja la decisión al ingeniero.

### 4. Decidir sobre un hallazgo

<figure class="figwrap">
  <svg viewBox="0 0 720 200" role="img" aria-labelledby="estados-title estados-desc">
    <title id="estados-title">Estados de un hallazgo en la línea base</title>
    <desc id="estados-desc">La auditoría crea los hallazgos como abiertos. Un abierto pasa a mitigado cuando se resuelve, a aceptado cuando se asume con justificación, o a no detectado cuando desaparece del código.</desc>
    <defs>
      <marker id="estados-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon class="d-bar" points="0 0, 8 3, 0 6"/></marker>
    </defs>
    <line class="d-line" x1="160" y1="100" x2="220" y2="100" marker-end="url(#estados-arrow)"/>
    <line class="d-line" x1="360" y1="100" x2="516" y2="44" marker-end="url(#estados-arrow)"/>
    <line class="d-line" x1="360" y1="100" x2="516" y2="100" marker-end="url(#estados-arrow)"/>
    <line class="d-line" x1="360" y1="100" x2="516" y2="156" marker-end="url(#estados-arrow)"/>
    <rect class="d-mask" x="394" y="58" width="92" height="14"/>
    <text class="d-tm d-mid" x="440" y="69">LO RESUELVE</text>
    <rect class="d-mask" x="400" y="93" width="80" height="14"/>
    <text class="d-tm d-mid" x="440" y="104">LO ASUME</text>
    <rect class="d-mask" x="394" y="128" width="92" height="14"/>
    <text class="d-tm d-mid" x="440" y="139">YA NO SALE</text>
    <rect class="d-box" x="24" y="76" width="136" height="48"/>
    <text class="d-t d-mid" x="92" y="97">Auditoría</text>
    <text class="d-tm d-mid" x="92" y="114">hallazgo nuevo</text>
    <rect class="d-fill" x="224" y="76" width="136" height="48"/>
    <text class="d-t d-mid" x="292" y="97">abierto</text>
    <text class="d-sm d-mid" x="292" y="114">cuenta en el resumen</text>
    <rect class="d-box" x="520" y="20" width="176" height="48"/>
    <text class="d-t d-mid" x="608" y="41">mitigado</text>
    <text class="d-sm d-mid" x="608" y="58">lo marca el equipo</text>
    <rect class="d-box" x="520" y="76" width="176" height="48"/>
    <text class="d-t d-mid" x="608" y="97">aceptado</text>
    <text class="d-sm d-mid" x="608" y="114">con justificación</text>
    <rect class="d-box" x="520" y="132" width="176" height="48"/>
    <text class="d-t d-mid" x="608" y="153">no detectado</text>
    <text class="d-sm d-mid" x="608" y="170">lo pone la auditoría</text>
  </svg>
  <figcaption>Los hooks callan en los cuatro estados: solo avisan de ids que no están en la línea base. Relanzar la auditoría conserva estado y justificación.</figcaption>
</figure>

Si el PM asume la exportación porque hay contrato de encargado y el bucket está en la UE, cambia su estado en `.ai-act/baseline.json`. Tras relanzar la auditoría queda así:

```json
"external-export:98e308bed7": {
  "status": "aceptado",
  "justification": "Contrato de encargado firmado; bucket en UE",
  "first_seen": "2026-11-17",
  "last_seen": "2026-11-17",
  "rule": "external-export",
  "severity": "alta",
  "title": "Entrega de datos fuera de la plataforma o a un tercero",
  "evidence": ["transform/gold/exports/partner_upload.py"]
}
```

La tabla `complaints` que se añadió en el paso 3 entra en la línea base como `abierto`, y el resumen de la siguiente sesión ya cuenta un solo hallazgo alto abierto.

### 5. Por qué funciona así: lo que enseñaron dos repos reales

Antes de escribir el código se lanzaron dos auditorías de solo lectura en el ordenador de trabajo, contra dos repos reales de cliente: uno de gestión (diseño y decisiones, sin código) y su repo de código (pipeline medallion en Microsoft Fabric con PySpark y Delta, ingesta desde PostgreSQL y SharePoint). No se copió nada del cliente: el ejemplo de este repo es ficticio y reproduce solo los patrones.

| Qué se vio | Qué cambió en el diseño |
|---|---|
| La única señal real era la PII: una clave por objeto para marcarla, opcional, validada pero nunca aplicada | El primer corte es la PII en la ingesta (Q19) y las reglas salen de la propia configuración del repo |
| Todo llegaba a Bronze en claro, con cambio de esquema automático y sin supresión | Hallazgos `bronze-schema-merge` y `no-erasure`, y la guía de proteger en la frontera Bronze → Silver |
| Una exportación de Gold al bucket de un tercero | Hallazgo `external-export` (art. 28 y 44-49) |
| La búsqueda por palabras daba falsos positivos: «predicado», «planificadas», «traza», «perfil», `client_id` | Palabras completas con `_` como separador, lista de exclusiones y, sobre todo, reglas estructuradas en lugar de palabras |
| El repo de gestión solo tenía documentación | La auditoría también detecta entornos desde `.md`, marcados como «documentación» |
| Ninguna señal del AI Act (sin LLM, scoring ni perfilado) | El AI Act queda como segundo nivel: el hook solo detecta SDK de LLM y scoring y deriva a su skill |

## Qué deja {#que-deja}

| Fichero | Quién lo escribe | Qué contiene |
|---|---|---|
| `.ai-act/profile.yaml` | `/project-init`, con el PM | Sector, finalidad, rol, datos personales, stack, contactos y clasificación inicial |
| `.ai-act/rules.json` | `audit.py write` | Reglas del repo, entornos, exclusiones y huella de la auditoría |
| `.ai-act/baseline.json` | `audit.py write`; el equipo edita estados | Hallazgos por id con estado, justificación y fechas |
| `.ai-act/audits/AAAA-MM-DD.md` | `audit.py write` | Informe fechado: entornos, reglas, hallazgos con norma, fecha y opción |
| `<tmp>/ai-act-advisor/<sesión>.json` | Hook `PostToolUse` | Ids ya avisados en la sesión; fuera del repo y se puede borrar |

`.ai-act/` se versiona con el repo: la línea base y las justificaciones son el registro de decisiones del proyecto.

## Despliegue {#despliegue}

<figure class="figwrap">
  <svg viewBox="0 0 720 104" role="img" aria-labelledby="dep-title dep-desc">
    <title id="dep-title">Cómo llega un evento de Claude Code al código del plugin</title>
    <desc id="dep-desc">Claude Code lanza el evento, hooks.json lo pasa a run.sh con un límite de diez segundos, run.sh elige python3 o python y hook.py ejecuta el código, que siempre sale con cero.</desc>
    <defs>
      <marker id="dep-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon class="d-bar" points="0 0, 8 3, 0 6"/></marker>
    </defs>
    <line class="d-line" x1="168" y1="52" x2="190" y2="52" marker-end="url(#dep-arrow)"/>
    <line class="d-line" x1="344" y1="52" x2="366" y2="52" marker-end="url(#dep-arrow)"/>
    <line class="d-line" x1="520" y1="52" x2="542" y2="52" marker-end="url(#dep-arrow)"/>
    <rect class="d-box" x="16" y="24" width="152" height="56"/>
    <text class="d-t d-mid" x="92" y="47">Claude Code</text>
    <text class="d-sm d-mid" x="92" y="65">lanza el evento</text>
    <rect class="d-box" x="192" y="24" width="152" height="56"/>
    <text class="d-t d-mid" x="268" y="47">hooks.json</text>
    <text class="d-sm d-mid" x="268" y="65">límite de 10 s</text>
    <rect class="d-box" x="368" y="24" width="152" height="56"/>
    <text class="d-t d-mid" x="444" y="47">run.sh</text>
    <text class="d-sm d-mid" x="444" y="65">python3 o python</text>
    <rect class="d-fill" x="544" y="24" width="152" height="56"/>
    <text class="d-t d-mid" x="620" y="47">hook.py</text>
    <text class="d-sm d-mid" x="620" y="65">sale siempre con 0</text>
  </svg>
  <figcaption>Si no hay Python, <code>run.sh</code> sale sin hacer nada. Cualquier error del hook se traga: el trabajo nunca se interrumpe.</figcaption>
</figure>

El plugin se instala desde el marketplace del propio repo:

```text
/plugin marketplace add AS-prog/ai-act-advisor
/plugin install ai-act-advisor@ai-act-advisor
```

Lo que protege el trabajo del ingeniero: los hooks solo devuelven `additionalContext` (nunca `decision` ni `permissionDecision`), Python sin dependencias (Q20), y la auditoría no abre `.env*`, claves, credenciales ni ficheros de datos, y de `profiles.yml` solo lee las líneas `type:`.

## Cómo se opera {#como-se-opera}

```sh
# Auditoría en consulta, en JSON (no escribe)
python3 plugins/ai-act-advisor/scripts/audit.py scan --root RUTA_DEL_REPO

# Informe en Markdown por pantalla
python3 plugins/ai-act-advisor/scripts/audit.py report --root RUTA_DEL_REPO

# Escribir reglas, línea base e informe en RUTA_DEL_REPO/.ai-act/
python3 plugins/ai-act-advisor/scripts/audit.py write --root RUTA_DEL_REPO

# Tests del prototipo
python3 -m unittest discover -s tests
```

| Síntoma | Qué pasa | Qué hacer |
|---|---|---|
| Cada sesión sugiere `/project-init` | No hay `.ai-act/profile.yaml` | Lanzar `/project-init` o ignorarlo si el repo no trata datos personales |
| Un aviso se repite en sesiones nuevas | El hallazgo no está en la línea base | Relanzar `audit.py write` y marcar su estado |
| Avisa de una palabra que no es PII | Falso positivo de la búsqueda de términos | Añadirla a `exclusions` en `.ai-act/rules.json` |
| No avisa de una fuente nueva | La configuración no está en `source_configs` ni usa la clave de PII | Relanzar `/project-init` para que la auditoría la reconozca |
| Hay que volver a oír un aviso en la misma sesión | Está en la memoria de la sesión | Borrar `<tmp>/ai-act-advisor/<sesión>.json` |

## Límites conocidos {#limites}

> [!WARNING]
> La búsqueda de términos es el respaldo cuando no hay reglas, y es la parte más ruidosa. En repos con nombres de columna en otro idioma o abreviados puede no ver PII real o marcar de más.

> [!WARNING]
> «PII declarada que no se aplica» es una heurística: busca código que use la clave más allá de validarla. Si el enmascaramiento ocurre fuera del repo (en el warehouse o en otro repo), saldrá como hallazgo y hay que marcarlo `mitigado` con su justificación.

> [!PENDING] Q5
> Cuánto ruido es aceptable. El límite actual es cuatro hallazgos por aviso, una vez por sesión y nada de lo que está en la línea base. Se ajusta con el uso.

- Solo entiende configuración en YAML, código Python y SQL. Los notebooks `.ipynb` se leen por celdas. Scala y R solo entran en la auditoría, con la búsqueda de términos; los hooks no los vigilan.
- Categorías especiales, scoring y transparencia (art. 50) tienen skill propia, y el hook del día a día ya emite `scoring-model` (ML y términos de scoring en el mismo fichero, D08), pero los proxies de categorías especiales no tienen señal en `signals.yaml`.
- El informe HTML con el sistema de diseño solo se ofrece si el repo tiene `docs/site/site.toml`.

## Dónde está en el código {#donde-esta}

| Parte | Fichero |
|---|---|
| Auditoría: entornos, reglas, comprobaciones, línea base, informe | `ai-act-advisor:plugins/ai-act-advisor/scripts/aiact/core.py` |
| Hooks `SessionStart` y `PostToolUse` | `ai-act-advisor:plugins/ai-act-advisor/scripts/aiact/hooks.py` |
| Lector de YAML sin dependencias | `ai-act-advisor:plugins/ai-act-advisor/scripts/aiact/miniyaml.py` |
| Línea de comandos de la auditoría | `ai-act-advisor:plugins/ai-act-advisor/scripts/audit.py` |
| Entrada de los hooks y lanzador | `ai-act-advisor:plugins/ai-act-advisor/scripts/hook.py`, `run.sh`, `hooks/hooks.json` |
| Señales, exclusiones y paquetes | `ai-act-advisor:plugins/ai-act-advisor/knowledge/signals.yaml` |
| Skills | `ai-act-advisor:plugins/ai-act-advisor/skills/project-init/SKILL.md`, `skills/pii-masking/SKILL.md` |
| Proyecto de ejemplo | `ai-act-advisor:examples/medallion-demo/` |
| Tests | `ai-act-advisor:tests/test_prototype.py` |

## Historial {#historial}

| Fecha | Cambio | Qué cambió |
|---|---|---|
| 2026-11-17 | Skills y agente | `risk-summary`, `special-categories`, `ai-act-classify`, `ai-transparency`, `regulatory-update` y el agente `regulatory-watcher` con contenido real, más tres referencias en `knowledge/` |
| 2026-11-17 | PR #2 | Primer prototipo: auditoría, hooks con línea base, skills `project-init` y `pii-masking`, ejemplo medallion. Detección de SDK de LLM y librerías de ML también en los ficheros de dependencias |
