from orders.models.order import Item, Order
from orders.services.pricing import total
from orders.services.ratio import average


def stats(payload: dict) -> dict:
    items = tuple(
        Item(name=i["name"], unit_price=i["unit_price"], quantity=i["quantity"])
        for i in payload.get("items", [])
    )
    order = Order(items=items, coupon_percent=payload.get("coupon_percent", 0))
    people = payload.get("people", 1)
    return {
        "per_person": total(order) // people,
        "average_quantity": average(tuple(item.quantity for item in items)),
    }
