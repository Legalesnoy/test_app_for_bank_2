"""функции для конвертации суммы транзакций в рубли через https://api.apilayer.com/exchangerates_data/convert"""

import os
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()


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
        if status_code == 200:
            amount = round(response.json()["result"], 2)
        else:
            amount = -1
            # print('status_code = ',status_code)
    except requests.exceptions.RequestException:
        amount = -2
        # print("RequestException")

    return amount
