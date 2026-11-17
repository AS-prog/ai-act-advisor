---
name: ai-transparency
description: "Comprueba las obligaciones de transparencia del art. 50 del AI Act en chatbots, agentes y contenido generado: aviso de que se habla con una IA y marcado del contenido sintético. Úsala cuando aparezca un SDK de LLM, un widget de chat o generación de texto, imagen, audio o vídeo."
---

# ai-transparency

> Esqueleto del prototipo. El diseño está en `docs/diseno/propuesta-prototipo.md`.

Rol: DE, AE y PM. Carga automática.

## Qué hará

1. Comprobar el aviso de IA en la interfaz o en el primer turno (art. 50.1).
2. Comprobar el marcado legible por máquina (art. 50.2), aplicable desde 2026-08-02 y desde 2026-12-02 para sistemas anteriores.
3. Excluir salidas máquina a máquina (código, JSON, SQL).

## Forma del aviso

Riesgo · Norma y artículo · Aplica ya o desde AAAA-MM-DD · Qué puede pasar · Opciones · A quién escalar · Base normativa de AAAA-MM-DD · No es asesoramiento legal.

Nunca bloquea: informa y deja la decisión a quien trabaja.
