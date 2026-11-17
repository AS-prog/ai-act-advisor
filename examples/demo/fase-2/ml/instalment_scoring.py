"""Modelo de impago para la compra a plazos (ficticio).

El cliente quiere decidir en la tienda online quién puede pagar a plazos. El modelo
estima la probabilidad de impago de cada cliente con su historial de compras.
"""
import pandas as pd
from sklearn.linear_model import LogisticRegression

FEATURES = ["orders_12m", "avg_ticket", "returns_12m", "months_as_customer", "late_payments"]


def train(silver_customers: pd.DataFrame) -> LogisticRegression:
    model = LogisticRegression(max_iter=500)
    model.fit(silver_customers[FEATURES], silver_customers["impago"])
    return model


def score(model: LogisticRegression, customers: pd.DataFrame) -> pd.DataFrame:
    out = customers[["customer_id"]].copy()
    out["default_probability"] = model.predict_proba(customers[FEATURES])[:, 1]
    # Por debajo del umbral se ofrece el pago a plazos; por encima, se rechaza.
    out["instalments_allowed"] = out["default_probability"] < 0.15
    return out
