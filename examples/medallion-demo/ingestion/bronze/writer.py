"""Escritura en Bronze con delta-rs (ficticio)."""
from deltalake import write_deltalake


def write_batch(df, path: str, batch_id: str) -> None:
    # Solo añade filas; el primer lote reemplaza por predicate sobre _batch_id.
    write_deltalake(
        path,
        df,
        mode="append",
        schema_mode="merge",
    )
