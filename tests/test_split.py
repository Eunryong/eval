import pytest

from orders.models.order import Item, Order
from orders.services.split import split_bill


def order(price: int) -> Order:
    return Order(items=(Item("x", price, 1),))


def test_split_bill_even():
    assert split_bill(order(9_000), 3) == [4_000, 4_000, 4_000]


def test_split_bill_remainder_goes_to_first():
    assert split_bill(order(10_000), 3) == [4_334, 4_333, 4_333]


def test_split_bill_rejects_zero_people():
    with pytest.raises(ValueError):
        split_bill(order(10_000), 0)
