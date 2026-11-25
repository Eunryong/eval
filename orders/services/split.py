from orders.models.order import Order
from orders.services.pricing import total


def split_bill(order: Order, people: int) -> list[int]:
    if people < 1:
        raise ValueError("people must be at least 1")
    amount = total(order)
    share = amount // people
    shares = [share] * people
    shares[0] += amount - share * people
    return shares
