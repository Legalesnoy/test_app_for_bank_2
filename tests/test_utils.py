from src.utils import gen_fin_transactions, get_fin_transactions
import os


def test_gen_fin_transactions():
    relative_path = "data\\operations.json"
    absolute_path = os.path.abspath(relative_path)
    lst = next(gen_fin_transactions(absolute_path))
    assert lst["id"] == 441945886


def test_get_fin_transactions():
    relative_path = "data\\operations.json"
    absolute_path = os.path.abspath(relative_path)
    lst = get_fin_transactions(absolute_path)
    assert lst[0]["id"] == 441945886
