def filter_by_state(state_data : list, state: str) -> list:
    """Функция выдает лист state_data с необходимым значением state"""
    # out_lst=[]
    #
    # for el in state_data:
    #     if el['state']==state:
    #         out_lst.append(el)
    #
    # return out_lst
    return list(filter(lambda x: x['state'] == state, state_data))

def sort_by_date():
    ...




# Вход функции
l1=[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(filter_by_state(l1,'EXECUTED'))
# Выход функции со статусом по умолчанию EXECUTED
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]