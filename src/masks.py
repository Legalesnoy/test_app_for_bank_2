def get_mask_card_number(card_number: int) -> str:
    """Функция маскирует номер карты и возвращается в формате XXXX XX** **** XXXX"""
    mask_card_number = ""
    if card_number == 0:
        return "0000 00** **** 0000"

    for i, symb in enumerate(list(str(card_number))):
        if i % 4 == 0:
            mask_card_number += " "
        if 5 < i < 12:
            symb = "*"
        mask_card_number += symb

    return mask_card_number.lstrip(" ")


def get_mask_account(account_number: int) -> str:
    """Функция маскирует номер счета XXXXXXXXXXXXXXXXX и возвращает в формате **XXXX"""

    if account_number == 0:
        return "**0000"

    mask_account = f"**{str(account_number)[-4:]}"

    return mask_account
