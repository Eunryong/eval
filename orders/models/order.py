from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    name: str
    unit_price: int
    quantity: int

    def __post_init__(self) -> None:
        if self.quantity < 1:
            raise ValueError("quantity must be at least 1")


@dataclass(frozen=True)
class Order:
    items: tuple[Item, ...]
    coupon_percent: int = 0
