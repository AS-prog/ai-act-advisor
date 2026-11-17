-- Silver de la encuesta de accesibilidad de las tiendas (ficticio).
-- Marketing quiere cruzarla con clientes para campañas de productos adaptados.
select
    r.customer_id,
    r.store_id,
    r.discapacidad,
    r.movilidad_reducida,
    r.necesita_ayuda_en_tienda,
    c.postal_code,
    r.answered_at
from bronze_accessibility_survey r
join silver_customers c using (customer_id)
