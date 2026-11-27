from orders.api.handlers import quote

MAX_CART_TOTAL = 1_000_000


def cart_quote(payload: dict) -> dict:
    amount = quote(payload)["total"]
    if amount > MAX_CART_TOTAL:
        raise ValueError("cart total too large")
    return {"total": amount}
