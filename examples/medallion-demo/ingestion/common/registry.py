"""Registro de objetos de ingesta (ficticio)."""

_OPTIONAL = {"pii_columns": list, "active": bool}


def validate(obj: dict) -> dict:
    """Comprueba la forma del objeto. pii_columns solo se valida: nadie lo aplica."""
    cols = obj.get("pii_columns", [])
    if not all(isinstance(c, str) for c in cols):
        raise ValueError("pii_columns debe ser una lista de nombres")
    return obj
