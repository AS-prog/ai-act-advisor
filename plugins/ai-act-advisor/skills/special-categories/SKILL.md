---
name: special-categories
description: "Categorías especiales de datos (RGPD art. 9) y variables proxy que las revelan: explica el riesgo, propone opciones y escala siempre al DPO. Úsala cuando aparezcan columnas de salud, origen étnico, religión, ideología, afiliación sindical, biometría, orientación sexual o antecedentes penales, cuando un aviso hable de «posibles categorías especiales», cuando un modelo use un proxy (código postal, nacionalidad, bajas médicas) o cuando pidan «medir sesgos» con datos sensibles."
---

# special-categories

Rol: DE y AE. Explica, propone y deja la decisión a quien trabaja. La base jurídica de una categoría especial la decide el responsable del tratamiento con su DPO: por eso este aviso **siempre** termina en el DPO.

Referencia: `${CLAUDE_PLUGIN_ROOT}/knowledge/special-categories.md` (lista del art. 9.1, tabla de proxies, excepciones del art. 9.2 y condiciones del art. 4 bis). Léela antes del paso 1.

## 1. Clasifica cada columna señalada

Trabaja con el código, la configuración y los esquemas; los ficheros de datos se quedan cerrados. Parte del hallazgo `special-category-terms` (su detalle lista los términos) o de lo que el ingeniero tenga abierto, y pon cada columna en uno de tres grupos:

- **Categoría especial**: el dato revela directamente algo del art. 9.1 (o condenas penales, art. 10).
- **Proxy**: no nombra la categoría, pero permite deducirla. Pesa más cuando el proyecto lo usa para segmentar, puntuar o decidir.
- **Falso positivo**: el término habla de otra cosa (`health_check` de un servicio, `salud` de un pipeline).

Hecho cuando cada columna señalada tiene grupo y ruta. Si todas son falsos positivos, salta al paso 5.

## 2. Sitúa el uso

El uso decide el aviso. Elige la rama que encaja:

- **Tránsito**: la columna pasa por la ingesta o las capas sin que nadie la consuma. El riesgo es de minimización y de seguridad.
- **Analítica o modelo**: alimenta un informe, una segmentación o las variables de un modelo. Si puntúa o decide sobre personas, añade la skill `ai-act-classify`: un proxy como variable predictora puede discriminar sin que nadie haya cargado la categoría.
- **Medir sesgos**: se quiere la categoría para comprobar o corregir el sesgo de un modelo. Es el único uso que cubre el art. 4 bis del AI Act, con sus seis condiciones.

## 3. Da el aviso

Con la forma de abajo. Para rellenarlo:

- **Norma**: RGPD art. 9 siempre, y aplica ya. Añade el art. 10 para condenas penales y el art. 4 bis del AI Act en la rama de sesgos (su fecha, de `${CLAUDE_PLUGIN_ROOT}/knowledge/dates.yaml`).
- **Qué puede pasar**: en concreto para este repo. Por ejemplo: diagnósticos en claro en Bronze al alcance de todo el equipo, un modelo que penaliza por código postal, una exportación que saca datos de salud del perímetro del cliente.
- **Opciones**: elige las dos o tres que encajen, de menos a más dato:
  1. Dejar la columna fuera en la ingesta si nadie la usa.
  2. Sustituirla por un agregado o un tramo que ya no revele la categoría de una persona.
  3. Aislarla: tabla aparte, seudonimizada, con permisos propios y registro de accesos (técnicas en `knowledge/masking-techniques.md`; para el detalle, skill `pii-masking`).
  4. En la rama de sesgos: cumplir las seis condiciones del art. 4 bis y decir cuáles faltan hoy en el repo, una por una.
  5. Mantenerla como está con la base del art. 9.2 que confirme el DPO.

## 4. Escala al DPO

Siempre, también cuando el ingeniero elige la opción más prudente: quien confirma que la categoría puede tratarse es el DPO (`escalation.dpo` del perfil; sin perfil, dilo y sugiere `/project-init`). Deja preparado lo que el DPO necesita para contestar: columnas y tablas, origen, capa, finalidad, quién accede y si sale del perímetro. Añade al PM (`escalation.pm`) si la decisión cambia el alcance o los plazos.

## 5. Registra la decisión

En `.ai-act/baseline.json`, sobre el id del hallazgo (`special-category-terms:…`); si el id falta en la línea base, `audit.py write` lo añade como `abierto`.

- `mitigado`, con `justification` que diga qué se hizo y dónde.
- `aceptado`, con `justification` que recoja la base del art. 9.2 y la respuesta del DPO (quién y qué día). Mientras llega esa respuesta, el estado sigue `abierto`.
- Falso positivo: añade el término a `exclusions` en `.ai-act/rules.json`. Vale para todo el repo, así que avisa al ingeniero de que ese término dejará de señalarse en cualquier fichero.

## Forma del aviso

Riesgo · Norma y artículo · Aplica ya o desde AAAA-MM-DD · Qué puede pasar · Opciones · A quién escalar (DPO) · Base normativa de AAAA-MM-DD (de `knowledge/VERSION`) · No es asesoramiento legal.

## Límites

- La detección es por nombre de columna (`special_category_terms` en `knowledge/signals.yaml`). Los proxies no tienen señal propia: salen de leer el esquema con la tabla de la referencia.
- La excepción del art. 9.2 que vale en cada caso la confirma el DPO; el aviso la propone como pregunta, sin darla por buena.
