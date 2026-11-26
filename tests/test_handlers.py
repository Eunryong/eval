import pytest

from orders.api.handlers import quote


def test_quote_returns_total():
    payload = {"items": [{"name": "a", "unit_price": 60_000, "quantity": 1}]}
    assert quote(payload) == {"total": 60_000}


def test_quote_rejects_coupon_over_limit():
    payload = {"items": [{"name": "a", "unit_price": 60_000, "quantity": 1}], "coupon_percent": 51}
    with pytest.raises(ValueError):
        quote(payload)
