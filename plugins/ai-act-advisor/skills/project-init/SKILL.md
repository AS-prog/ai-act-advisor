---
name: project-init
description: "Configura un proyecto frente al AI Act y el RGPD: en un repo nuevo entrevista al PM y escribe .ai-act/profile.yaml; en un proyecto ya encaminado audita (solo lectura) entornos y riesgos y deja reglas, línea base e informe. Úsala cuando pidan «iniciar proyecto», «kickoff», «perfil del proyecto», «auditoría de riesgos» o cuando cambie el alcance o el stack."
---

# project-init

Rol: PM. Lanzamiento manual con `/project-init`. Nunca bloquea: informa y deja la decisión a quien trabaja.

**Carpeta del plugin**: en Claude Code, `${CLAUDE_PLUGIN_ROOT}` llega ya sustituido por una ruta. Si lo ves tal cual, el plugin se instaló con APM: usa en su lugar la primera de estas carpetas, en la raíz del repo, que tenga `knowledge/VERSION` dentro: `.claude/hooks/ai-act-advisor`, `.github/hooks/scripts/ai-act-advisor`, `.codex/hooks/ai-act-advisor`, `.cursor/hooks/ai-act-advisor`, `.gemini/hooks/ai-act-advisor` o `.windsurf/hooks/ai-act-advisor`. Haz lo mismo con `$CLAUDE_PROJECT_DIR`, que es la raíz del repo.

## Reglas de seguridad (siempre)

- Solo lectura sobre el código del cliente. Lo único que se escribe es la carpeta `.ai-act/` del repo.
- No abras credenciales ni secretos: `.env*`, `secrets*`, claves, `*.pem`, `*.key`, `credentials*`. De `profiles.yml` solo interesa la línea `type:`.
- No abras ficheros de datos (`.csv`, `.parquet`, `.xlsx`, `.json` de datos, `.db`…) ni te conectes a bases de datos o warehouses.
- No copies código ni datos del cliente fuera del repo (ni a otros repos, ni a la conversación más allá de rutas y nombres de columna).

## 1. Decide el modo

Ejecuta la auditoría en modo consulta, que no escribe nada:

```sh
sh "${CLAUDE_PLUGIN_ROOT}/scripts/run.sh" audit.py scan --root "$CLAUDE_PROJECT_DIR"
```

- **Proyecto nuevo**: no hay código (sin entornos detectados ni ficheros de transformación). Ve al paso 2 y marca el stack como `status: declarado`.
- **Proyecto encaminado**: hay código. Haz el paso 2 con lo que ya sabes y después el paso 3.
- **Ya existe `.ai-act/profile.yaml`**: no vuelvas a preguntar todo. Enseña el perfil, pregunta qué ha cambiado y relanza la auditoría.

## 2. Perfil del proyecto

Rellena primero con lo que haya en el repo (README, `docs/`, propuesta, SOW) y pregunta solo lo que falte, en pocas preguntas agrupadas:

1. Cliente y sector (usa las claves de `knowledge/sectors.yaml`).
2. Finalidad del entregable y si infiere (modelo, scoring, LLM) o solo mueve y agrega datos.
3. Rol de la consultora: proveedor, responsable del despliegue o ambos.
4. Datos personales que se tratan (contacto, financieros, salud, menores…). Si hay categorías especiales, avisa de que se escala al DPO.
5. Stack (si hay código, propón el detectado y que el PM lo corrija).
6. Contactos de escalado: DPO, legal, PM.
7. Si el proyecto ocupa varios repos, lista los repos. El informe consolidado vive en el repo de gestión.

Escribe `.ai-act/profile.yaml` con la forma de `profile.example.yaml`, en la carpeta de esta skill. Para la clasificación inicial usa `knowledge/dates.yaml` y explica qué fecha aplica a cada obligación (art. 4 y 5 desde 2025-02-02, art. 50 desde 2026-08-02, Anexo III desde 2027-12-02 tras el Omnibus). Si hay dudas sobre alto riesgo, propón la skill `ai-act-classify`.

## 3. Auditoría de riesgos (proyecto encaminado)

1. Enseña al PM lo que encontró `scan`, en este orden y breve:
   - Entornos que toca el repo (warehouses, almacenamiento, ficheros compartidos, exportaciones, SDK de LLM).
   - Reglas del propio repo: dónde declara las fuentes, con qué clave marca la PII (`pii_key`), qué escribe en Bronze, qué exporta.
   - Hallazgos de severidad alta y media, con su evidencia (ruta), norma, artículo y desde cuándo aplica.
2. Pide que confirme o corrija: entornos que sobran o faltan, falsos positivos (se añaden a `exclusions` en `.ai-act/rules.json`) y hallazgos que ya están resueltos fuera del repo.
3. Escribe el estado:

   ```sh
   sh "${CLAUDE_PLUGIN_ROOT}/scripts/run.sh" audit.py write --root "$CLAUDE_PROJECT_DIR"
   ```

   Deja `.ai-act/rules.json` (reglas que usan los hooks), `.ai-act/baseline.json` (hallazgos con estado) y `.ai-act/audits/AAAA-MM-DD.md` (informe fechado).
4. Estados de la línea base: `abierto`, `mitigado`, `aceptado` (con `justification`) y `no detectado` (lo pone la auditoría cuando un hallazgo abierto desaparece). Si el PM acepta un riesgo, edita su estado y la justificación en `baseline.json`; al relanzar la auditoría se conservan. Los hooks solo avisan de lo que no está en la línea base.
5. Si el repo tiene `docs/site/site.toml`, ofrece además una versión HTML del informe con la skill de documentación del sistema de diseño del repo.

## Forma de cada aviso

Riesgo · Norma y artículo · Aplica ya o desde AAAA-MM-DD · Qué puede pasar · Opciones · A quién escalar · Base normativa de AAAA-MM-DD (de `knowledge/VERSION`) · No es asesoramiento legal.

## Al terminar

Resume en cinco líneas: modo, clasificación inicial, número de hallazgos por severidad, los dos que conviene mirar primero y la skill que ayuda con cada uno (`pii-masking`, `special-categories`, `ai-transparency`, `ai-act-classify`). Recuerda que se puede relanzar cuando cambie el stack o el alcance.
