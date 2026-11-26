from orders.models.cart import Cart
from orders.models.order import Item
from orders.services.pricing import total

MAX_CART_TOTAL = 1_000_000


def cart_quote(payload: dict) -> dict:
    items = tuple(
        Item(name=i["name"], unit_price=i["unit_price"], quantity=i["quantity"])
        for i in payload.get("items", [])
    )
    cart = Cart(items=items, coupon_percent=payload.get("coupon_percent", 0))
    amount = total(cart.to_order())
    if amount > MAX_CART_TOTAL:
        raise ValueError("cart total too large")
    return {"total": amount}
