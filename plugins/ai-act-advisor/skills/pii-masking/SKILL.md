---
name: pii-masking
description: "Explica el riesgo de trabajar con datos personales sin enmascarar y propone técnicas (seudonimización, hashing con sal, tokenización, generalización, masking dinámico del stack). Úsala cuando aparezcan columnas con PII en SQL, dbt o Python."
---

# pii-masking

> Esqueleto del prototipo. El diseño está en `docs/diseno/propuesta-prototipo.md`.

Rol: DE y AE. Carga automática.

## Qué hará

1. Identificar las columnas y su tipo de dato personal.
2. Explicar la norma (RGPD art. 5.1.c y art. 25) y que aplica ya.
3. Proponer opciones según el stack del perfil, con sus límites, y dejar la decisión al ingeniero.

## Forma del aviso

Riesgo · Norma y artículo · Aplica ya o desde AAAA-MM-DD · Qué puede pasar · Opciones · A quién escalar · Base normativa de AAAA-MM-DD · No es asesoramiento legal.

Nunca bloquea: informa y deja la decisión a quien trabaja.
