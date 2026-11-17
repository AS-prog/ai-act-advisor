---
title: Cómo se usa ai-act-advisor
description: Guía de uso del plugin para PM, data engineers y analytics engineers: instalarlo, configurar un proyecto, qué hacer con cada aviso, cómo registrar decisiones, ver el estado y mantener al día la base normativa.
date: 2026-11-17
status: vigente
---

# Cómo se usa ai-act-advisor

Guía de uso del plugin para PM, data engineers (DE) y analytics engineers (AE): cómo se instala, cómo se configura un proyecto, qué hacer con cada aviso, cómo se registran las decisiones, cómo se ve el estado y cómo se mantiene al día la base normativa.

## En corto

1. El PM lanza `/project-init` al empezar el proyecto, o cuando ya está en marcha, y deja configurado el repo en `.ai-act/`.
2. DE y AE trabajan como siempre. Cuando Claude lee o edita algo con riesgo nuevo de RGPD o del AI Act, recibe un aviso y te lo cuenta en pocas líneas.
3. Si quieres detalle, pides la skill que indica el aviso. Te explica el riesgo, te propone opciones y la decisión es tuya.
4. La decisión se apunta en la línea base (`.ai-act/baseline.json`), y ese aviso no vuelve a salir.
5. El PM lanza `/risk-summary` cuando quiere ver el estado y qué escalar.
6. Quien mantiene el plugin lanza `/regulatory-update` para revisar las fuentes oficiales y proponer los cambios en una PR.

El plugin no bloquea nada, no edita tu código salvo que se lo pidas, no abre ficheros de datos ni secretos y no se conecta a bases de datos. No es asesoramiento legal: cada aviso dice de qué norma viene y desde cuándo aplica.

## El flujo de un proyecto

<figure class="figwrap">
  <svg viewBox="0 0 720 304" role="img" aria-labelledby="flujo-title flujo-desc">
    <title id="flujo-title">Quién hace qué con el plugin a lo largo de un proyecto</title>
    <desc id="flujo-desc">El PM configura el proyecto con project-init. DE y AE trabajan, reciben avisos y deciden con la ayuda de una skill; si hay un modelo o un LLM, el PM clasifica con ai-act-classify. Las decisiones van a la línea base, que el PM consulta con risk-summary. En mantenimiento, regulatory-update lanza el vigilante y deja una PR revisada que mantiene al día la base normativa.</desc>
    <defs>
      <marker id="flujo-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon class="d-bar" points="0 0, 8 3, 0 6"/></marker>
    </defs>
    <rect class="d-wash-1" x="16" y="16" width="688" height="80"/>
    <rect class="d-wash-1" x="16" y="208" width="688" height="80"/>
    <text class="d-tm" x="24" y="60">PM</text>
    <text class="d-tm" x="24" y="156">DE Y AE</text>
    <text class="d-tm" x="24" y="252">MANTENIMIENTO</text>
    <line class="d-line" x1="216" y1="80" x2="216" y2="124" marker-end="url(#flujo-arrow)"/>
    <rect class="d-mask" x="176" y="95" width="80" height="14"/>
    <text class="d-tm d-mid" x="216" y="106">CONFIGURA</text>
    <line class="d-line" x1="296" y1="152" x2="332" y2="152" marker-end="url(#flujo-arrow)"/>
    <line class="d-line" x1="496" y1="152" x2="532" y2="152" marker-end="url(#flujo-arrow)"/>
    <line class="d-dash" x1="416" y1="128" x2="416" y2="84" marker-end="url(#flujo-arrow)"/>
    <rect class="d-mask" x="366" y="99" width="100" height="14"/>
    <text class="d-tm d-mid" x="416" y="110">MODELO O LLM</text>
    <line class="d-line" x1="616" y1="128" x2="616" y2="84" marker-end="url(#flujo-arrow)"/>
    <rect class="d-mask" x="572" y="99" width="88" height="14"/>
    <text class="d-tm d-mid" x="616" y="110">LÍNEA BASE</text>
    <line class="d-line" x1="296" y1="248" x2="332" y2="248" marker-end="url(#flujo-arrow)"/>
    <line class="d-line" x1="496" y1="248" x2="532" y2="248" marker-end="url(#flujo-arrow)"/>
    <line class="d-dash" x1="616" y1="224" x2="616" y2="180" marker-end="url(#flujo-arrow)"/>
    <rect class="d-mask" x="572" y="195" width="88" height="14"/>
    <text class="d-tm d-mid" x="616" y="206">BASE AL DÍA</text>
    <rect class="d-fill" x="136" y="32" width="160" height="48"/>
    <text class="d-t d-mid" x="216" y="53">Configura</text>
    <text class="d-tm d-mid" x="216" y="70">/project-init</text>
    <rect class="d-box" x="336" y="32" width="160" height="48"/>
    <text class="d-t d-mid" x="416" y="53">Clasifica</text>
    <text class="d-tm d-mid" x="416" y="70">/ai-act-classify</text>
    <rect class="d-box" x="536" y="32" width="160" height="48"/>
    <text class="d-t d-mid" x="616" y="53">Ve el estado</text>
    <text class="d-tm d-mid" x="616" y="70">/risk-summary</text>
    <rect class="d-box" x="136" y="128" width="160" height="48"/>
    <text class="d-t d-mid" x="216" y="149">Trabaja</text>
    <text class="d-sm d-mid" x="216" y="166">lee y edita código</text>
    <rect class="d-box" x="336" y="128" width="160" height="48"/>
    <text class="d-t d-mid" x="416" y="149">Recibe un aviso</text>
    <text class="d-sm d-mid" x="416" y="166">solo si es nuevo</text>
    <rect class="d-fill" x="536" y="128" width="160" height="48"/>
    <text class="d-t d-mid" x="616" y="149">Decide</text>
    <text class="d-sm d-mid" x="616" y="166">con la skill indicada</text>
    <rect class="d-box" x="136" y="224" width="160" height="48"/>
    <text class="d-t d-mid" x="216" y="245">Revisa normativa</text>
    <text class="d-tm d-mid" x="216" y="262">/regulatory-update</text>
    <rect class="d-box" x="336" y="224" width="160" height="48"/>
    <text class="d-t d-mid" x="416" y="245">Lee las fuentes</text>
    <text class="d-tm d-mid" x="416" y="262">regulatory-watcher</text>
    <rect class="d-box" x="536" y="224" width="160" height="48"/>
    <text class="d-t d-mid" x="616" y="245">PR revisada</text>
    <text class="d-sm d-mid" x="616" y="262">nunca se fusiona sola</text>
  </svg>
  <figcaption>Hay dos momentos manuales del PM (configurar y ver el estado). El día a día de DE y AE es automático: solo habla el plugin cuando aparece algo nuevo.</figcaption>
</figure>

| Rol | Qué lanza | Cuándo | Qué obtiene |
|---|---|---|---|
| PM | `/project-init` | Al empezar, y cuando cambian el alcance, el stack o aparece un entorno nuevo | Perfil del proyecto, reglas del repo, línea base e informe fechado |
| PM | `/ai-act-classify` | Cuando hay un modelo que puntúa o decide sobre personas, un LLM, o cambia la finalidad | Clasificación AI Act razonada y rol de proveedor o responsable del despliegue |
| PM | `/risk-summary` | Antes de un comité, una entrega o cuando quiere saber qué escalar | Resumen de una página por severidad y estado, y qué escalar a quién |
| DE y AE | Nada: los avisos llegan solos | Al leer o editar código y configuración | Aviso corto con norma, fecha, opción y skill |
| DE y AE | `pii-masking`, `special-categories`, `ai-transparency` | Cuando quieren detalle de un aviso | Riesgo explicado, opciones según su stack y a quién escalar |
| Mantenimiento | `/regulatory-update` | Semanalmente, o cuando el aviso dice que la base tiene más de 90 días | PR con los cambios normativos, cada uno con su cita |

## Instalar

En Claude Code:

```text
/plugin marketplace add AS-prog/ai-act-advisor
/plugin install ai-act-advisor@ai-act-advisor
```

Hace falta Python 3 en la máquina (sin dependencias). Si no lo hay, los hooks no hacen nada y no interrumpen. Desde ese momento, al abrir un repo, el plugin te dice si ya está configurado.

## 1. Configurar el proyecto: /project-init

Lo lanza el PM. Primero averigua si el repo tiene código:

- **Proyecto nuevo, sin código**: entrevista corta y perfil. El stack queda como `declarado`, y el plugin sugerirá auditar cuando haya código.
- **Proyecto en marcha**: además del perfil, una auditoría de riesgos de solo lectura.

Preguntas del perfil, en pocas tandas, rellenando antes con lo que ya diga el README o la propuesta:

1. Cliente y sector.
2. Finalidad del entregable y si infiere (modelo, scoring, LLM) o solo mueve y agrega datos.
3. Rol de la consultora: proveedor, responsable del despliegue o ambos.
4. Datos personales que se tratan.
5. Stack (si hay código, lo propone la auditoría y el PM lo corrige).
6. Contactos de escalado: DPO, legal, PM.
7. Si el proyecto ocupa varios repos, cuáles son.

En un proyecto en marcha, la skill enseña los entornos que toca el repo, las reglas que deduce (dónde se declaran las fuentes, con qué clave se marca la PII, qué se escribe en Bronze, qué se exporta) y los hallazgos con su evidencia. El PM confirma o corrige: un entorno que sobra, un falso positivo que pasa a `exclusions`. Después la skill escribe el estado en `.ai-act/`.

> [!IMPORTANT]
> La auditoría solo lee código y configuración del repo. No abre `.env`, claves, credenciales ni ficheros de datos, no se conecta a warehouses y no copia nada fuera del repo.

Vuelve a lanzarlo cuando cambie el alcance o el stack, o cuando un aviso diga que aparece un entorno que la auditoría no tenía (por ejemplo, una dependencia de `openai` nueva).

## 2. Trabajar: qué hacer con un aviso

DE y AE no lanzan nada. Al abrir una sesión, el plugin le da a Claude un resumen del perfil. Cuando Claude lee o edita un fichero con un riesgo que no está en la línea base, recibe un aviso con esta forma:

```text
[media] Objeto «complaints» sin «pii_columns» declarado · RGPD art. 5.1.c, art. 25, art. 30
· aplica ya · skill pii-masking
Opción sugerida: Revisa el esquema de origen de «complaints» antes de llevarlo a Bronze y
declara «pii_columns» (aunque sea una lista vacía) para que conste que se revisó.
Base normativa 2026-07-27 (revisada 2026-11-17). No es asesoramiento legal.
```

Claude te lo cuenta cuando encaja con lo que estás haciendo. Tienes tres opciones:

- **Seguir**: el aviso no se repite en la sesión. Si no lo registras, volverá en otra sesión.
- **Pedir detalle**: «explícame este riesgo» o «cómo lo enmascaro». Claude carga la skill del aviso.
- **Decidir y registrar** (paso 3).

| Si el aviso habla de… | La skill que ayuda | Qué te da |
|---|---|---|
| Columnas con aspecto de dato personal, fuente sin clave de PII, PII declarada que no se aplica, Bronze sin revisión, exportación, supresión | `pii-masking` | Técnicas según capa y stack (suprimir, seudonimizar con HMAC, tokenizar, generalizar, masking dinámico) y su límite |
| Salud, origen, religión, ideología, sindicato, biometría, orientación sexual, antecedentes, o un proxy de ellas | `special-categories` | Si está permitido y bajo qué condición del art. 9.2; siempre escala al DPO |
| SDK de LLM, chatbot, contenido generado, ultrafalsificaciones | `ai-transparency` | Qué aviso o marcado pide el art. 50 y desde cuándo |
| Modelo que puntúa o clasifica a personas | `ai-act-classify` | Si es candidato a alto riesgo según sector y finalidad, y el rol |

## 3. Decidir y registrar

La decisión es de quien trabaja (o del PM, el DPO o legal cuando el aviso dice a quién escalar). Se apunta en `.ai-act/baseline.json`, sobre el id del hallazgo:

| Estado | Cuándo | Qué hay que escribir |
|---|---|---|
| `abierto` | Lo pone la auditoría al encontrarlo | Nada |
| `mitigado` | Ya se ha resuelto | `justification`: qué se hizo y dónde |
| `aceptado` | Se asume el riesgo | `justification`: por qué, y quién lo decidió |
| `no detectado` | Lo pone la auditoría cuando el hallazgo desaparece del código | Nada |

```json
"external-export:98e308bed7": {
  "status": "aceptado",
  "justification": "Contrato de encargado firmado; bucket en UE"
}
```

Puedes pedírselo a Claude: «marca la exportación como aceptada, hay contrato de encargado». Relanzar la auditoría conserva el estado y la justificación, y los hooks no vuelven a avisar de ningún id que esté en la línea base. Si una palabra salta y no es dato personal en tu repo, añádela a `exclusions` en `.ai-act/rules.json`.

## 4. Ver el estado: /risk-summary

Lo lanza el PM. Une la línea base con una auditoría de consulta y devuelve una página con:

1. Cabecera: proyecto, sector, rol, clasificación y repos leídos.
2. Abiertos de severidad alta, uno por uno, y de media en tabla.
3. Nuevos sin registrar (aparecen en el código pero no en la línea base).
4. Aceptados con su justificación (señala los que no la tienen).
5. Mitigados y no detectados.
6. Qué escalar y a quién, con los contactos del perfil.
7. Qué aplica ya y qué después, por fecha.
8. Qué falta por decidir y de quién es.

Si el proyecto ocupa varios repos, lee los que estén clonados en la máquina, y el consolidado vive en el repo de gestión. La página se enseña en la conversación y solo se guarda en `.ai-act/risk-summary.md` si el PM lo pide.

## 5. Clasificar frente al AI Act: /ai-act-classify

Cuando el proyecto entrena o usa un modelo sobre personas, o un LLM, el PM (con el DE o AE que lo conoce) recorre el árbol: práctica prohibida (art. 5), candidato a alto riesgo (anexo III según sector y finalidad), transparencia (art. 50), mínimo o fuera de alcance, y el rol de la consultora. La skill propone y razona. El perfil solo cambia cuando el PM lo confirma.

## Mantener al día la base normativa

Cada aviso lleva la fecha de la base normativa. Cuando tiene más de 90 días, la sesión lo dice al arrancar. Quien mantiene el plugin lanza `/regulatory-update` en un clon del repo del plugin:

1. El agente `regulatory-watcher` lee las fuentes oficiales (EUR-Lex, BOE, Comisión, AESIA, AEPD, CEPD) en solo lectura y devuelve los cambios con cita.
2. La skill separa lo confirmado de lo que está por verificar.
3. Deja los cambios en una rama `regulatory/AAAA-MM-DD` con su PR. Una persona la revisa y la fusiona; nunca se fusiona sola.

Los textos oficiales de referencia están en `docs/documentos/fuentes/` del repo del plugin, con su versión y su huella en el manifiesto.

## Qué deja en tu repo

| Fichero | Para qué |
|---|---|
| `.ai-act/profile.yaml` | Perfil del proyecto: sector, finalidad, rol, datos personales, stack, contactos, clasificación |
| `.ai-act/rules.json` | Reglas del repo que usan los avisos, y `exclusions` para los falsos positivos |
| `.ai-act/baseline.json` | Hallazgos con estado y justificación: el registro de decisiones |
| `.ai-act/audits/AAAA-MM-DD.md` | Informe fechado de cada auditoría |
| `.ai-act/risk-summary.md` | Último resumen, solo si el PM pidió guardarlo |

Conviene versionar `.ai-act/` con el repo: así las decisiones quedan en el historial.

## Preguntas frecuentes

¿Me puede impedir hacer algo?
: No. Los avisos solo añaden contexto a Claude; la decisión es siempre tuya.

¿Manda datos o código a algún sitio?
: No. Todo se ejecuta en local con Python, solo lee código y configuración del repo, y no abre datos ni secretos.

Me avisa demasiado.
: Registra en la línea base lo que ya has decidido y añade a `exclusions` los términos que no son datos personales en tu repo. Cada aviso sale una vez por sesión y como mucho con cuatro hallazgos.

¿Y si el proyecto no usa IA?
: Los avisos del RGPD siguen siendo útiles. La clasificación AI Act queda como «fuera de alcance».

¿Es asesoramiento legal?
: No. Señala riesgos con su norma y su fecha para que el equipo decida y, cuando toca, escale al DPO o a legal.

## Más información

- [Cómo funciona el prototipo en uso](../tecnica/uso-del-prototipo.html): qué hay por dentro, con las salidas reales.
- [Propuesta del prototipo](../diseno/propuesta-prototipo.html): el diseño y las decisiones.
- [Pendientes y dudas](../pendientes.html): lo que queda por decidir o confirmar.
