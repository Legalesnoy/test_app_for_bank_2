import logging

if __name__ == '__main__':
    log_path = "../logs/app.log"
else:
    log_path = "logs/app.log"

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


mask_card_logger = logging.getLogger('app.masks.mask_card')
mask_account_logger = logging.getLogger('app.masks.mask_account')


def get_mask_card_number(card_number: int) -> str:
    """Функция маскирует номер карты и возвращается в формате XXXX XX** **** XXXX"""
    mask_card_logger.info = (f'принимаем номер карты: {card_number}')

    mask_card_number = ""
    card_number_str = str(card_number)
    if len(card_number_str) <= 16:
        card_number_str = "0" * (16 - len(card_number_str)) + card_number_str

    for i, symb in enumerate(list(card_number_str)):
        if i % 4 == 0:
            mask_card_number += " "
        if 5 < i < 12:
            symb = "*"
        mask_card_number += symb

    mask_card_logger.info = (f'получили маску номера карты: {mask_card_number}')
    return mask_card_number.lstrip(" ")


def get_mask_account(account_number: int) -> str:
    """Функция маскирует номер счета XXXXXXXXXXXXXXXXX и возвращает в формате **XXXX"""
    mask_account_logger.info(f'принимаем номер счета: {account_number}')
    if account_number == 0:
        return "**0000"

    mask_account = f"**{str(account_number)[-4:]}"

    mask_card_logger.info = (f'получили маску номер счета: {mask_account}')
    return mask_account
