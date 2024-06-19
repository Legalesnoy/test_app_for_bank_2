from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Функция общей маскировки карты и счета"""
    card_type = [
        "visa platinum",
        "maestro",
    ]
    account_type = [
        "счёт",
        "счет",
    ]

    number_str = ""
    card_account = ""
    card_num_lst = card_number.split()
    mask_account_card = ""

    for word in card_num_lst:
        if word.isdigit():
            number_str += word
        else:
            card_account += word + " "

    card_account = card_account.strip()
    number = int(number_str)

    if card_account.lower() in card_type:
        mask_account_card = get_mask_card_number(number)
    elif card_account.lower() in account_type:
        mask_account_card = get_mask_account(number)

    return mask_account_card


def get_data(str_with_data: str) -> str:
    """Функция преобразования даты"""

    data_dct = {
        "year": str_with_data[0:4],
        "month": str_with_data[5:7],
        "day": str_with_data[8:10],
    }

    data = ".".join(list(data_dct.values())[::-1])

    return data


# if __name__ == "__main__":
#      s1 = "Счет 73654108430135874305"
#      s2 = "Maestro 7000 7922 8960 6361"
#      s3 = "Visa Platinum 7000 7922 8960 6361"
#      s4 = "Счёт 7000 7922 8960 6361"
#
#
#     print(mask_account_card(s1))
#     print(mask_account_card(s2))
#     print(mask_account_card(s3))
#     print(mask_account_card(s4))
#
#     print(get_data('2018-07-11T02:26:18.671407'))
