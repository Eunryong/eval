from orders.models.order import Item, Order


def summary(payload: dict) -> dict:
    items = tuple(
        Item(name=i["name"], unit_price=i["unit_price"], quantity=i["quantity"])
        for i in payload.get("items", [])
    )
    order = Order(items=items, coupon_percent=payload.get("coupon_percent", 0))
    return {"count": len(order.items), "subtotal": order.subtotal()}
