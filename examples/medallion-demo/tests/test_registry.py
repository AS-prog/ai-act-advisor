from ingestion.common.registry import validate


def test_validate_accepts_pii_list():
    assert validate({"name": "x", "pii_columns": ["email"]})
