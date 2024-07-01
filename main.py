from src.generators import filter_by_currency
from src.widget import get_data, mask_account_card
from src.masks import get_mask_account, get_mask_card_number



if __name__ == "__main__":
    print(get_mask_card_number(1234567890123456))
    print(get_mask_account(1111111111145673))

    s1 = "Счет 73654108430135874305"
    s2 = "Maestro 7000 7922 8960 6361"
    s3 = "Visa Platinum 7000 7922 8960 6361"
    s4 = "Счёт 7000 7922 8960 6361"

    print(mask_account_card(s1))
    print(mask_account_card(s2))
    print(mask_account_card(s3))
    print(mask_account_card(s4))

    print(get_data("2018-07-11T02:26:18.671407"))
    print(1+1)
