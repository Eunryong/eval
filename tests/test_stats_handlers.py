from orders.api.stats_handlers import stats


def test_stats_splits_total_and_averages_quantity():
    payload = {
        "items": [
            {"name": "a", "unit_price": 30_000, "quantity": 1},
            {"name": "b", "unit_price": 10_000, "quantity": 4},
        ],
        "people": 3,
    }
    assert stats(payload) == {"per_person": 23_333, "average_quantity": 2.5}


def test_stats_empty_order():
    assert stats({}) == {"per_person": 0, "average_quantity": 0.0}
