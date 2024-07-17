from unittest.mock import patch
import os
from src.external_api import convert_fin_transactions
from dotenv import load_dotenv

load_dotenv()


def test_convert_fin_transactions():
    with patch("requests.get") as mock_get:
        dct = {"operationAmount": {"amount": 123, "currency": {"code": "USD"}}}
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {
            "to": "RUB",
            "from": "USD",
            "amount": 123,
        }
        API_KEY = os.getenv("API_KEY")
        headers = {"apikey": API_KEY}

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"result": 111.11}
        assert convert_fin_transactions(dct) == 111.11
        mock_get.assert_called_once_with(url, headers=headers, params=payload)
