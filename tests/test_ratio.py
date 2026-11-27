from orders.services.ratio import average, per_unit


def test_per_unit_drops_remainder():
    assert [per_unit(10, 3), per_unit(9, 3)] == [3, 3]


def test_average():
    assert [average((1, 2)), average(())] == [1.5, 0.0]
