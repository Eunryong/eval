from orders.models.order import Item, Order
from orders.services.vat import vat_breakdown


def order(price: int) -> Order:
    return Order(items=(Item("x", price, 1),))


def test_vat_breakdown_splits_total():
    assert vat_breakdown(order(8_000)) == {"supply": 10_000, "vat": 1_000}


def test_vat_breakdown_drops_below_one_won():
    assert vat_breakdown(order(60_000)) == {"supply": 54_546, "vat": 5_454}
