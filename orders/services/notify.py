from orders.models.order import Order


def notify_placed(order: Order) -> None:
    print("order placed", order)
