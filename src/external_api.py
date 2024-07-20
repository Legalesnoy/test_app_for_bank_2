"""функции для конвертации суммы транзакций в рубли через https://api.apilayer.com/exchangerates_data/convert"""
import logging
import os
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    log_path = "../logs/app.log"
else:
    log_path = "logs/app.log"

logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    filename=log_path,
                    filemode='w',
                    encoding='utf-8')
convert_logger = logging.getLogger('app.external_api.convert_fin_transactions')


def convert_fin_transactions(transaction: Dict) -> float:
    """функция, которая принимает на вход транзакцию
    и возвращает сумму транзакции (amount) в рублях"""
    API_KEY = os.getenv("API_KEY")
    # current_date_time = datetime.datetime.now()
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {
        "to": "RUB",
        "from": currency,
        "amount": amount,
        # "date":current_date_time.strftime("%d-%m-%Y %H:%M:%S")
    }
    headers = {"apikey": API_KEY}
    try:
        response = requests.get(url, headers=headers, params=payload)

        status_code = response.status_code
        convert_logger.info(f'response.status_code: {status_code}, {response.json()}')
        if status_code == 200:
            amount = round(response.json()["result"], 2)
        else:
            amount = -1
            # print('status_code = ',status_code)
    except requests.exceptions.RequestException as ex:
        convert_logger.error(f"Произошла ошибка {ex}")
        amount = -2
        # print("RequestException")

    return amount
