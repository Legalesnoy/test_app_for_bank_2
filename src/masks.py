def get_mask_card_number(card_number: int) -> str:
    """Функция маскирует номер карты и возвращается в формате XXXX XX** **** XXXX"""
    mask_card_number = ""

    for i, symb in enumerate(list(str(card_number))):
        if i % 4 == 0:
            mask_card_number += " "
        if 5 < i < 12:
            symb = "*"
        mask_card_number += symb

    return mask_card_number.lstrip(" ")


def get_mask_account(account_number: int) -> str:
    """Функция маскирует номер счета XXXXXXXXXXXXXXXXX и возвращает в формате **XXXX"""
    mask_account = f"**{str(account_number)[-4:]}"

    return mask_account


def get_mask_card_number2(card_number: int) -> str:
    """Функция маскирует номер карты и возвращается в формате XXXX XX** **** XXXX"""
    mask_card_number = list('XXXX XX** **** XXXX')
    mask_card_number = list(str(card_number)[0:4])
    # [mask_card_number.insert((i+1)*4,' ') for i in range(3)]
    s1=list(str(card_number))
    [s1.insert(((i+1)*4)+i,' ') for i in range(4)]
    [s1.insert(((i + 1) * 4) + i, ' ') for i in range(4)]

    print(''.join(s1))
    # print(f'{str(card_number)[0:4]} {str(card_number)[5:7]}** **** {str(card_number)[12:]}')

    # for i, symb in enumerate(list(str(card_number))):
    #     if i % 4 == 0:
    #         mask_card_number += " "
    #     if 5 < i < 12:
    #         symb = "*"
    #     mask_card_number += symb
    #
    # return mask_card_number.lstrip(" ")
print (get_mask_card_number2(123456789012345678))