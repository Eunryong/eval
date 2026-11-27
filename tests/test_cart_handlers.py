import pytest

from orders.api.cart_handlers import cart_quote


def test_cart_quote_returns_total():
    payload = {
        "items": [{"name": "a", "unit_price": 60_000, "quantity": 1}],
        "coupon_percent": 10,
    }
    assert cart_quote(payload) == {"total": 54_000}


def test_cart_quote_rejects_large_total():
    payload = {"items": [{"name": "a", "unit_price": 1_000_001, "quantity": 1}]}
    with pytest.raises(ValueError):
        cart_quote(payload)
