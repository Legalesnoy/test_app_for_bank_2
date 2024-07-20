"""функции для работы с транзакциями"""
import logging

import json

from typing import Iterable, List, Dict

if __name__ == '__main__':
    log_path = "../logs/app.log"
else:
    log_path = "logs/app.log"

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    filename=log_path,
                    filemode='w',
                    encoding='utf-8')
gen_trans_logger = logging.getLogger('app.utils.gen_fin_transactions')
get_trans_logger = logging.getLogger('app.utils.get_fin_transactions')


def gen_fin_transactions(file_path: str) -> Iterable:
    """генератор, который принимает на вход путь до JSON-файла
    и возвращает генератор словарей с данными о финансовых транзакциях."""
    with open(file_path, "r", encoding="utf-8") as f:

        for transaction in json.load(f):
            gen_trans_logger.info(f'фин. транзакция:{transaction}')
            yield transaction


def get_fin_transactions(file_path: str) -> List[Dict]:
    """функцию, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях."""
    trans_lst = list(gen_fin_transactions(file_path))

    get_trans_logger.info(f'всего транзакций:{len(trans_lst)}')
    return list(trans_lst)


# проверочка:
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
