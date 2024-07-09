import pytest

from src.masks import get_mask_account, get_mask_card_number


# @pytest.mark.parametrize('n, expected',[(num1, str_expected1), (num2, str_expected2)])
def test_get_mask_card_number(num1, str_expected1):
    assert get_mask_card_number(num1) == str_expected1


def test_get_msk_crd_num(num2, str_expected2):
    assert get_mask_card_number(num2) == str_expected2


def test_get_msk_c_num():
    assert get_mask_card_number(0) == "0000 00** **** 0000"


@pytest.mark.parametrize("n, expected", [(1234567890123456, "**3456"), (1111111111111111, "**1111"), (0, "**0000")])
def test_get_mask_account(n, expected):
    assert get_mask_account(n) == expected
