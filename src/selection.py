import re
from collections import Counter, abc

from src.decorators import log

"""
модуль с функциями для поиска данных о банковских операций
и вывода статистики по категориям операций
"""

if __name__ == '__main__':
    log_path = "../logs/app.log"
else:
    log_path = "logs/app.log"


def search_transactions(transactions, search_data):
    """функция поиска данных о банковских операций"""
    result = []

    for transaction in transactions:

        t_str = str(transaction).lower()
        pattern = re.compile(search_data.lower())

        if re.search(pattern, t_str, flags=0) is not None:
            result.append(transaction)

    return result


def stat_transactions(transactions, description_list):
    """функция вывода статистики по категориям операций"""
    count_list=description_list.copy()
    descr_lst=[]

    for el in description_list:
        descr_lst.append(el.lower())

    for transaction in transactions:
        description = str(transaction.get('description', '')).lower()

        if description in descr_lst:
            operation = description_list[descr_lst.index(description)]
            count_list.append(operation)

    counted = Counter(count_list)
    counted.subtract(description_list)

    return dict(counted)


# def flat_dct(dct):
#     """функция расщепляет словарь с высокой вложенностью до символов"""
#     for k, v in dct.items():
#         yield str(k)
#         if isinstance(v, abc.Iterable) and not isinstance(v, (str, bytes)):
#             flat_lst(v)
#         else:
#             yield v
#
#
# def flat_lst(nested_list):
#     """функция расщепляет лист с высокой вложенностью до символов'"""
#     for el in nested_list:
#         if isinstance(el, abc.Iterable) and not isinstance(el, (str, bytes)):
#             if isinstance(el, dict):
#                 yield from flat_lst([[k, *flat_lst(v)] for k, v in el.items()])
#             else:
#                 yield from flat_lst(el)
#
#         else:
#             yield el



# if __name__ == '__main__':
#     from src.get_data import get_data
#     csv_data = get_data('..\\data\\transactions.csv')
#     print(stat_transactions(csv_data, ['ПерЕвод с карты на карту', 'ПеревоД оРГанизаЦии', 'ОткрыТиЕ вклада', 'Закрытие вклада' ]))
#     print(search_transactions(csv_data, 'EUR'))
