import logging
from dataclasses import dataclass

from orders.models.order import Order
from orders.services.pricing import subtotal

logger = logging.getLogger(__name__)

POINT_PERCENT = 1
BONUS_THRESHOLD = 100_000


@dataclass
class PointResult:
    earned: int
    bonus: bool


def earn_points(order: Order) -> PointResult:
    amount = subtotal(order)
    if amount <= 0:
        return PointResult(earned=0, bonus=False)
    logger.debug("earn_points amount %s", amount)
    bonus = amount >= BONUS_THRESHOLD
    rate = POINT_PERCENT * 2 if bonus else POINT_PERCENT
    return PointResult(earned=amount * rate // 100, bonus=bonus)
