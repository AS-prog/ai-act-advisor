# Técnicas de protección de datos personales

Referencia para la skill `pii-masking`. Cada técnica: qué es, cuándo conviene, qué no protege y ejemplo por stack. Los ejemplos son orientativos: adáptalos a las convenciones del repo.

Recordatorio de base: un dato seudonimizado sigue siendo dato personal (RGPD considerando 26). Solo la anonimización real lo saca del RGPD, y es difícil de conseguir con datos de clientes.

## Dónde proteger en una arquitectura medallion

| Capa | Qué conviene | Por qué |
|---|---|---|
| Fuente / ingesta | No traer columnas que nadie usa | Lo que no se copia no hay que proteger ni borrar |
| Bronze | Copia fiel, acceso muy restringido, retención corta | Suele ser append-only y con cambio de esquema automático: es donde la PII entra sin que nadie la mire |
| Bronze → Silver | Seudonimizar o tokenizar identificadores directos; generalizar | Es la frontera natural: a partir de aquí trabajan AE y analistas |
| Gold | Solo agregados o seudónimos; nada en claro salvo necesidad documentada | Es lo que se comparte y exporta |
| Exportación | Lo mínimo para la finalidad; contrato de encargado (art. 28) y transferencia (art. 44-49) | Sale del perímetro del cliente |

## Supresión de columnas

- **Qué es**: no seleccionar, o eliminar, la columna.
- **Cuándo**: la columna no tiene uso analítico (teléfono, dirección completa en un modelo de propensión).
- **Qué no protege**: nada que falte; es la opción más fuerte. Riesgo: que alguien la necesite después y la vuelva a traer sin revisar.
- **Ejemplo**: en la configuración de fuentes, una lista de columnas permitidas en vez de `select *`; en dbt, seleccionar columnas explícitas en el modelo de staging.

## Seudonimización con hash con clave (HMAC)

- **Qué es**: sustituir el identificador por `HMAC-SHA256(clave, valor)`. Mismo valor → mismo seudónimo, así que se puede cruzar.
- **Cuándo**: se necesita unir tablas o contar personas distintas sin ver el dato.
- **Qué no protege**: un hash sin clave (o con sal conocida) de emails, DNI o teléfonos se revierte por diccionario en minutos. La clave debe vivir en un gestor de secretos, nunca en el repo. No impide inferencias por las demás columnas.
- **Ejemplos**:
  - Python: `hmac.new(key, email.strip().lower().encode(), hashlib.sha256).hexdigest()`
  - Spark / Fabric / Databricks: `sha2(concat(lower(trim(email)), secret), 256)` con `secret` desde el key vault; mejor una UDF con HMAC.
  - PostgreSQL (pgcrypto): `encode(hmac(lower(email), current_setting('app.pii_key'), 'sha256'), 'hex')`
  - BigQuery: `TO_HEX(SHA256(CONCAT(@pii_key, LOWER(email))))`, o cifrado determinista con `DETERMINISTIC_ENCRYPT` y claves de Cloud KMS.
  - Snowflake: `SHA2(CONCAT(LOWER(email), $pii_key), 256)` o una función externa de tokenización.
  - dbt: una macro `pseudonymize(column)` que lea la clave de una variable de entorno y se aplique en staging.

## Tokenización

- **Qué es**: sustituir el valor por un token aleatorio y guardar la correspondencia en una tabla o servicio separado (bóveda).
- **Cuándo**: hay que poder volver al dato original (atención al cliente, campañas) o atender el derecho de supresión borrando una sola fila.
- **Qué no protege**: si la bóveda está en el mismo almacenamiento y con los mismos permisos, no aporta nada. Añade una pieza que operar.
- **Ejemplo**: tabla `pii_vault(token, email, created_at)` en un esquema con acceso restringido; Silver y Gold solo llevan `token`.

## Generalización

- **Qué es**: reducir la precisión: fecha de nacimiento → año o tramo de edad; código postal → provincia; coordenadas → municipio; importe → rango.
- **Cuándo**: el análisis no necesita el detalle.
- **Qué no protege**: combinaciones raras siguen identificando (edad + municipio pequeño + producto). Revisa grupos con pocas personas (k-anonimato aproximado).
- **Ejemplos**: SQL `date_trunc('year', birth_date)` o `floor(datediff(current_date, birth_date)/365.25/10)*10 as age_band`; `left(postal_code, 2) as province_code`.

## Masking dinámico y políticas de columna

- **Qué es**: el dato está en claro en la tabla, pero según el rol quien consulta ve `****` o un valor parcial.
- **Cuándo**: hay perfiles que deben ver el dato (operaciones) y otros que no (analítica).
- **Qué no protege**: los administradores y los procesos con permisos altos lo ven en claro; exportaciones hechas con esos permisos salen en claro. No es minimización.
- **Ejemplos**:
  - Fabric / Synapse / SQL Server: `ALTER TABLE ... ALTER COLUMN email ADD MASKED WITH (FUNCTION = 'email()')`.
  - Databricks Unity Catalog: `ALTER TABLE ... ALTER COLUMN email SET MASK mask_email`.
  - Snowflake: `CREATE MASKING POLICY` y `ALTER TABLE ... MODIFY COLUMN email SET MASKING POLICY`.
  - BigQuery: policy tags con data masking en Dataplex.
  - PostgreSQL: vistas con columnas enmascaradas y permisos solo sobre las vistas, o la extensión `postgresql_anonymizer`.

## Cifrado

- **Qué es**: cifrar la columna (o el fichero) con una clave gestionada.
- **Cuándo**: hay que guardar el dato en claro recuperable y protegerlo en reposo y en copias.
- **Qué no protege**: el cifrado del disco o del bucket por defecto no protege frente a quien tiene acceso a la tabla. Útil para el "borrado criptográfico": destruir la clave de una persona equivale a borrarla.

## Supresión y retención en almacenamiento append-only

Delta Lake, Iceberg y Bronze en general guardan versiones antiguas: borrar una fila no la borra del historial.

- Delta (Spark o delta-rs): `DELETE` de la persona y después `VACUUM` con la retención acordada; documenta la retención en la configuración.
- Particionar o tokenizar facilita borrar a una persona sin reescribir todo.
- Con `schema_mode="merge"` o `mergeSchema`, una columna nueva de PII entra en Bronze sin revisión: valida el esquema contra la lista de columnas permitidas antes de escribir.

## Logs y ficheros compartidos

- No imprimas filas ni muestras de datos en logs (`print(df.head())`, `logger.info(row)`).
- Hojas de SharePoint o Drive con contactos: trátalas como una fuente más, con su lista de columnas permitidas.
