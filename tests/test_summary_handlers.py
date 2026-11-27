from orders.api.summary_handlers import summary


def test_summary_counts_items_and_sums_prices():
    payload = {
        "items": [
            {"name": "a", "unit_price": 1_000, "quantity": 2},
            {"name": "b", "unit_price": 500, "quantity": 3},
        ]
    }
    assert summary(payload) == {"count": 2, "subtotal": 3_500}


def test_summary_empty_order():
    assert summary({}) == {"count": 0, "subtotal": 0}
