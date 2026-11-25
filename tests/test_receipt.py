from orders.services.receipt import format_won


def test_format_won_adds_commas_and_unit():
    assert format_won(12_000) == "12,000원"


def test_format_won_zero():
    assert format_won(0) == "0원"


def test_format_won_negative():
    assert format_won(-3_000) == "-3,000원"
