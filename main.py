from src.get_data import get_data
from src.processing import filter_by_state, sort_by_date
from src.selection import search_transactions
from src.utils import get_fin_transactions

incorrect_answer_str = "В меню такого нет :("

expected_responses = {"choice_file_type": ("JSON", "CSV", "XLSX"),
                      "filter1_choice": ("EXECUTED", "CANCELED", "PENDING"),
                      "sort_choice": ("Да", "Нет"),
                      "ascending_sort": ("по возрастанию", "по убыванию"),
                      "ru_transactions": ("Да", "Нет"),
                      "filter2_choice": ("Да", "Нет")
                      }

user_choice = dict.fromkeys(expected_responses, None)

dialog = {"salutation": "Привет! Добро пожаловать в программу работы с банковскими транзакциями.",
          "main_menu_salutation": "Выберите необходимый пункт меню:",
          "choice_file_type":  f"Получить информацию о транзакциях из {'/'.join(expected_responses['choice_file_type'])} файла?",
          "filter_menu_salutation": "Введите статус, по которому необходимо выполнить фильтрацию.",
          "filter_menu": "Доступные для фильтровки статусы:",
          "filter1_choice": f"{'/'.join(expected_responses['filter1_choice'])}",
          "sort_choice":  f"Отсортировать операции по дате? {'/'.join(expected_responses['sort_choice'])}?",
          "ascending_sort": f"Отсортировать {'/'.join(expected_responses['ascending_sort'])}?",
          "ru_transactions": f"Выводить только рублевые тразакции? {'/'.join(expected_responses['ru_transactions'])}",
          "filter2_choice": f"Отфильтровать список транзакций по определенной строке в описании? {'/'.join(expected_responses['filter2_choice'])}",
          "result_asw": "Распечатываю итоговый список транзакций..."
          }

json_file = "data\\operations.json"
csv_file = "data\\transactions.csv"
xl_file = "data\\transactions_excel.xlsx"

for key, replica in dialog.items():
    print(replica)

    if expected_responses.__contains__(key):
        exp_resp = [resp.lower() for resp in expected_responses[key]]

        while True:

            if ((answer := input().lower()) in exp_resp
                    or (answer.isdigit() and 0 < int(answer) <= len(exp_resp))):

                if answer.isdigit():
                    user_choice[key] = expected_responses[key][int(answer)-1]
                else:
                    user_choice[key] = expected_responses[key][exp_resp.index(answer)]
                break
            else:
                if answer == 'q':
                    break
                print(incorrect_answer_str)
                print(replica)

        if answer == 'q':
            break

        if user_choice['filter2_choice'] == "Да":
            user_choice['filter2_choice'] = input("введите строку:\n")
        print(f"выбран {user_choice[key]}")

if user_choice['choice_file_type'] == 'JSON':
    result = get_fin_transactions(json_file)
elif user_choice['choice_file_type'] == 'CSV':
    result = get_data(csv_file)
elif user_choice['choice_file_type'] == 'XLSX':
    result = get_data(xl_file)

result = filter_by_state(result, user_choice['filter1_choice'])

if user_choice['sort_choice'] == 'Да':
    result = sort_by_date(result, ascending = not (user_choice['ascending_sort'] == 'по возрастанию'))

if user_choice['ru_transactions'] == 'Да':
    result = search_transactions(result, 'RUB')

if user_choice['filter2_choice'] == 'Да':
    result = search_transactions(result, user_choice['filter2_choice'])

if not result:
    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
else:
    print(result)



# result =





# print(dialog['salutation'])
# print(dialog['main_menu_salutation'])
# for n,item in enumerate(dialog['choice_file_type'],1):
#     print(f"{n}. {dialog['main_menu'][0]} {item}{dialog['main_menu'][1]}")
#
# choice = input()
#
# if not choice.isdigit() or (int(choice) < 1 or int(choice) > len(dialog['choice_file_type'])):
#     print(dialog['incorrect_answer_str'])
# else:
#     choice = int(choice)-1
#     user_choice["file_type"] = dialog['choice_file_type'][choice]
#
#     print(f"{dialog['answer_str'][0]} {dialog['choice_file_type'][choice]}{dialog['answer_str'][1]}")
#     print(dialog['filter_menu_salutation'])
#
#     while True:
#         print(f"{dialog['filter_menu']}", end=' ')
#         for item in dialog['filter_choice1']:
#             print(f"{item}", end = ' ')
#         filter_str = input('\n').upper()
#         if filter_str not in dialog['filter_choice1']:
#             print(f"{filter_str} - {dialog['incorrect_answer_str'].lower()}")
#             continue
#         else:
#             user_choice["filter1"] = filter_str
#             break
#    if dialog["sort_choice"])

























# # from src.generators import filter_by_currency
# from src.masks import get_mask_account, get_mask_card_number
# from src.widget import get_data, mask_account_card
#
# if __name__ == "__main__":
#     print(get_mask_card_number(1234567890123456))
#     print(get_mask_account(1111111111145673))
#
#     s1 = "Счет 73654108430135874305"
#     s2 = "Maestro 7000 7922 8960 6361"
#     s3 = "Visa Platinum 7000 7922 8960 6361"
#     s4 = "Счёт 7000 7922 8960 6361"
#
#     print(mask_account_card(s1))
#     print(mask_account_card(s2))
#     print(mask_account_card(s3))
#     print(mask_account_card(s4))
#
#     print(get_data("2018-07-11T02:26:18.671407"))
#     print(1 + 1)
