import pytest

from src.generators import card_number_generator, filter_by_currency, sign


@pytest.mark.parametrize("n, expected", [(-10, -1), (0, 1), (2323, 1)])
def test_sign(n, expected):
    assert sign(n) == expected


def test_filter_by_currency(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    result = list(usd_transactions)
    expected_result = [transactions[1], transactions[3], transactions[0]]

    assert result == expected_result


def test_card_number_generator():
    expected_result = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert list(card_number_generator(1, 5)) == expected_result
