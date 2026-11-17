"""Silver de clientes (ficticio): limpia tipos, pero no trata la PII."""
import duckdb

QUERY = """
select customer_id, email, phone, birth_date, city, created_at
from bronze_customers
where not _is_deleted
"""


def build(con: duckdb.DuckDBPyConnection):
    return con.execute(QUERY).df()
