import pytest

from src.widget import get_data, get_data_int, mask_account_card


@pytest.mark.parametrize(
    "n, expected", [("2018-07-11T02:26:18.671407", 20180711), ("2019-06-01T02:26:18.671407", 20190601)]
)
def test_get_data_int(n, expected):
    assert get_data_int(n) == expected


def test_get_data():
    assert get_data("2019-06-01T02:26:18.671407") == "01.06.2019"


s1 = "Счет 73654108430135874305"
s2 = "Maestro 7000 7922 8960 6361"
s3 = "Visa Platinum 7000 7922 8960 6361"
s4 = "Счёт 7000 7922 8960 6361"

s1_e = "**4305"
s2_e = "7000 79** **** 6361"
s3_e = "**6361"


@pytest.mark.parametrize("n, expected", [(s1, s1_e), (s2, s2_e), (s3, s2_e), (s4, s3_e)])
def test_mask_account_card(n, expected):
    assert mask_account_card(n) == expected
