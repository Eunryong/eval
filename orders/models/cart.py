from dataclasses import dataclass

from orders.models.order import Item, Order


@dataclass
class Cart:
    items: tuple[Item, ...] = ()
    coupon_percent: int = 0

    def to_order(self) -> Order:
        return Order(items=self.items, coupon_percent=self.coupon_percent)
