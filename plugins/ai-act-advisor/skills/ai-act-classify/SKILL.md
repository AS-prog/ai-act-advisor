---
name: ai-act-classify
description: "Clasifica un modelo de scoring, propensión o decisión sobre personas según el AI Act, cruzando su finalidad con el sector del cliente para ver si cae en el anexo III, y da las fechas que aplican. Úsala cuando aparezca un modelo que puntúa o decide sobre personas."
---

# ai-act-classify

> Esqueleto del prototipo. El diseño está en `docs/diseno/propuesta-prototipo.md`.

Rol: DE, AE y PM. Carga automática.

## Qué hará

1. Leer sector y finalidad del perfil y cruzarlos con `knowledge/sectors.yaml`.
2. Revisar la excepción del art. 6.3 y su anulación por perfilado.
3. Dar la fecha: alto riesgo del anexo III desde 2027-12-02.

## Forma del aviso

Riesgo · Norma y artículo · Aplica ya o desde AAAA-MM-DD · Qué puede pasar · Opciones · A quién escalar · Base normativa de AAAA-MM-DD · No es asesoramiento legal.

Nunca bloquea: informa y deja la decisión a quien trabaja.
