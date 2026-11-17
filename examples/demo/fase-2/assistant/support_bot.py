"""Asistente de atención al cliente de la tienda online (ficticio).

Responde a dudas de pedidos y devoluciones en el chat de la web. Las respuestas las
escribe un modelo de lenguaje.
"""
import anthropic

SYSTEM = "Eres el asistente de la tienda. Responde en español, breve y con amabilidad."

client = anthropic.Anthropic()


def answer(question: str, order_summary: str) -> str:
    msg = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=400,
        system=SYSTEM,
        messages=[{"role": "user", "content": f"Pedido: {order_summary}\n\nPregunta: {question}"}],
    )
    return msg.content[0].text
