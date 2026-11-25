from orders.models.order import Item, Order
from orders.services.points import PointResult, earn_points


def order(price: int) -> Order:
    return Order(items=(Item("x", price, 1),))


def test_earn_points_one_percent():
    assert earn_points(order(10_000)) == PointResult(earned=100, bonus=False)


def test_earn_points_doubles_from_bonus_amount():
    assert earn_points(order(99_999)) == PointResult(earned=999, bonus=False)
    assert earn_points(order(100_000)) == PointResult(earned=2_000, bonus=True)


def test_earn_points_empty_order():
    assert earn_points(Order(items=())) == PointResult(earned=0, bonus=False)
