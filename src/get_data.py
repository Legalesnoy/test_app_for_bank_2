import pandas as pd
from typing import List, Dict


def get_data(file_path: str) -> List[Dict]:
    '''функция получающая данные с транзакциями из Excel или CSV файла'''
    data_lst = list()

    df = pd.read_excel(file_path) if '.xlsx' in file_path else pd.read_csv(file_path, delimiter=';')
    columns, rows = df.shape

    for v in range(columns):
        data_lst.append({k: str(df.loc[v, k]) for k in df.keys()})

    return data_lst


# # проверочка:
# csv_data = get_data('..\\data\\transactions.csv')
# print(len(csv_data), csv_data[56])
# xl_data = get_data('..\\data\\transactions_excel.xlsx')
# print(len(xl_data), xl_data[56])
# # for i,el in enumerate(xl_data):
# #     print(i, el)
# #     print()
