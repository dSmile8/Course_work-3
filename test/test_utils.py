from src.utils import *
from src import main

def test_main():
    main.main()
    assert True

def test_open_file():
    data = open_file()
    assert type(data) == list

def test_executed_operations(test_data1):

    assert executed_operations(test_data1) == [
         {"date": "2019-07-03T18:35:29.512364",
          "description": "Перевод организации",
          "id": 41428829,
          "operationAmount": {"amount": "8221.37",
              "currency": {"code": "USD", "name": "USD"}},
          "state": "EXECUTED",
          "to": "Счет 35383033474447895560"},
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
          "to": "Счет 74489636417521191160"}]


def test_format_date(test_data1):
        assert format_date(test_data1)[0] == {
         "date": "26.08.2019",
         "description": "Перевод организации",
         "from": "Maestro 1596837868705199",
         "id": 441945886,
         "operationAmount": {"amount": "31957.58",
                      "currency": {"code": "RUB", "name": "руб."}},
         "to": "Счет 64686473678894779589"}


def test_hide_recipient_number(test_data2):
    assert hide_recipient_number(test_data2)[0] == {
     "date": "2018-06-30T02:08:58.425572",
     "description": "Перевод организации",
     "id": 939719570,
     "operationAmount": {"amount": "9824.07",
                         "currency": {"code": "USD", "name": "USD"}},
     "state": "EXECUTED",
     "to": "**67021"}

    assert hide_recipient_number(test_data2)[1] == {
        "date": "2019-04-04T23:20:05.206878",
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "id": 142264268,
        "operationAmount": {"amount": "79114.93",
                            "currency": {"code": "USD", "name": "USD"}},
        "state": "EXECUTED",
        "to": "**41881"
    }

def test_hide_sender_number(test_data2):
    assert hide_sender_number(test_data2)[0] == {
     "date": "2018-06-30T02:08:58.425572",
     "description": "Перевод организации",
     "id": 939719570,
     "operationAmount": {"amount": "9824.07",
                         "currency": {"code": "USD", "name": "USD"}},
     "state": "EXECUTED",
     "to": "Счет 11776614605963066702"}

    assert hide_sender_number(test_data2)[1] == {
        "date": "2019-04-04T23:20:05.206878",
        "description": "Перевод со счета на счет",
        "from": "Счет **8542",
        "id": 142264268,
        "operationAmount": {"amount": "79114.93",
                            "currency": {"code": "USD", "name": "USD"}},
        "state": "EXECUTED",
        "to": "Счет 75651667383060284188"}


def test_hide_recipient_number(test_data2):
    assert hide_recipient_number(test_data2)[0] == {
        "date": "2018-06-30T02:08:58.425572",
        "description": "Перевод организации",
        "id": 939719570,
        "operationAmount": {"amount": "9824.07",
                            "currency": {"code": "USD", "name": "USD"}},
        "state": "EXECUTED",
        "to": "Счет **6702"}

    assert hide_recipient_number(test_data2)[3] == {
          "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-01-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет **5560"}


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
    assert enter_transaction(test_data2)[0] == '2018-06-30T02:08:58.425572 Перевод организации\nСчет 11776614605963066702\n9824.07 USD\n\n '




