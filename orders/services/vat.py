from orders.models.order import Order
from orders.services.pricing import total


def vat_breakdown(order: Order) -> dict:
    """합계를 공급가액과 부가세(10%)로 나눈다. 부가세는 원 미만을 버린다."""
    amount = total(order)
    vat = amount // 11
    return {"supply": amount - vat, "vat": vat}
