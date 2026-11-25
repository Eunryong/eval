from orders.models.order import Item, Order
from orders.services.points import earn_points

if __name__ == "__main__":
    result = earn_points(Order(items=(Item("sample", 120_000, 1),)))
    print("earned", result.earned, "bonus", result.bonus)
