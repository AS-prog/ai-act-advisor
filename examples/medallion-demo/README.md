# medallion-demo

Proyecto **ficticio** para probar `ai-act-advisor`: una medallion (Bronze, Silver, Gold sobre Delta) de una distribuidora inventada que ingiere un CRM en PostgreSQL y un libro de SharePoint, y entrega un fichero a un socio de medios. No contiene código ni datos de ningún cliente.

Está hecho para que la auditoría encuentre lo que vimos en proyectos reales:

- una fuente con `pii_columns` y otra sin declarar;
- un libro de SharePoint, que no admite `pii_columns`;
- `pii_columns` validado pero nunca aplicado;
- Bronze con evolución de esquema y sin supresión ni retención;
- una exportación a un bucket de un tercero;
- y palabras que no deben dar falsos positivos («predicate», «planificadas», «model»).
