from src.utils import open_file, executed_operations, get_last_values, enter_transaction
from src import main
import json

def test_main():
    # main.main()
    # assert True

def test_open_file():
    with open('operations.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
    assert type(data) == list

def test_executed_operations(test_data1):

    assert executed_operations(test_data1) == [
        {"date": "2018-06-30T02:08:58.425572",
         "description": "Перевод организации",
         "from": "Счет 75106830613657916952",
         "id": 939719570,
         "operationAmount": {"amount": "9824.07",
             "currency": {"code": "USD", "name": "USD"}},
         "state": "EXECUTED",
         "to": "Счет 11776614605963066702"},
         {"date": "2019-04-04T23:20:05.206878",
          "description": "Перевод со счета на счет",
         "from": "Счет 19708645243227258542",
         "id": 142264268,
         "operationAmount": {"amount": "79114.93",
             "currency": {"code": "USD", "name": "USD"}},
         "state": "EXECUTED",
         "to": "Счет 75651667383060284188"},
         {"date": "2019-03-23T01:09:46.296404",
         "description": "Перевод со счета на счет",
         "from": "Счет 44812258784861134719",
         "id": 873106923,
         "operationAmount": {"amount": "43318.34",
                     "currency": {"code": "RUB", "name": "руб."}},
          "state": "EXECUTED",
          "to": "Счет 74489636417521191160"}
    ]

def test_get_last_values(test_data2):
    assert get_last_values(test_data2, 2) == [
        {"date": "2019-04-04T23:20:05.206878",
         "description": "Перевод со счета на счет",
         "from": "Счет 19708645243227258542",
         "id": 142264268,
         "operationAmount": {"amount": "79114.93",
                             "currency": {"code": "USD", "name": "USD"}},
         "state": "EXECUTED",
         "to": "Счет 75651667383060284188"},
        {"date": "2019-03-23T01:09:46.296404",
         "description": "Перевод со счета на счет",
         "from": "Счет 44812258784861134719",
         "id": 873106923,
         "operationAmount": {"amount": "43318.34",
                             "currency": {"code": "RUB", "name": "руб."}},
         "state": "EXECUTED",
         "to": "Счет 74489636417521191160"}
    ]

def test_enter_transaction(test_data2):
    assert enter_transaction(test_data2)[1] == '04.04.2019 Перевод со счета на счет\nСчет **8542 -> Счет **4188\n79114.93 USD \n\n '
    assert enter_transaction(test_data2)[-1] == '03.01.2018 Перевод организации\nMasterCard 7158 30** **** 6751 -> MasterCard 7158 30** **** 6758\n8221.37 USD \n\n '




