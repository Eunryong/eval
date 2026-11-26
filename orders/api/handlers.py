from orders.models.order import Item, Order
from orders.services.pricing import MAX_COUPON_PERCENT, total


def quote(payload: dict) -> dict:
    coupon_percent = payload.get("coupon_percent", 0)
    if coupon_percent > MAX_COUPON_PERCENT:
        raise ValueError("coupon_percent out of range")
    items = tuple(
        Item(name=i["name"], unit_price=i["unit_price"], quantity=i["quantity"])
        for i in payload.get("items", [])
    )
    order = Order(items=items, coupon_percent=coupon_percent)
    return {"total": total(order)}
