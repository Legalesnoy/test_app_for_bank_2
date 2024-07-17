"""функции для работы с транзакциями"""

import json

from typing import Iterable, List, Dict


def gen_fin_transactions(file_path: str) -> Iterable:
    """генератор, который принимает на вход путь до JSON-файла
    и возвращает генератор словарей с данными о финансовых транзакциях."""
    with open(file_path, "r", encoding="utf-8") as f:

        for transaction in json.load(f):
            yield transaction


def get_fin_transactions(file_path: str) -> List[Dict]:
    """функцию, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях."""
    return list(gen_fin_transactions(file_path))


# # проверочка:
# if __name__ == '__main__':
#     # print(get_fin_transactions("..\\data\\operations.json"))
#     from src.external_api import convert_fin_transactions
#     tr = gen_fin_transactions("..\\data\\operations.json")
#     ch = input()
#     while ch != 'q':
#         v = next(tr,None)
#         if v is None:
#             break
#         print(v)
#         print(f"{convert_fin_transactions(v)} руб.")
#         ch=input()
