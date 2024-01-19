import json
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent.joinpath('operations.json')
def open_file():
    """Открывает json файл и записывает его в переменную 'data' """

    with DATA_DIR.open(encoding='utf-8') as file:
        data = json.load(file)
    return data


def executed_operations(data):
    """Оставляем EXECUTED(выполненные операции)"""

    execut_operations = []
    for v in data:
        if 'state' in v and v['state'] == 'EXECUTED':
            execut_operations.append(v)
    return execut_operations


def get_last_values(data, count_last_values):
    """Сортируем список по дате и оставляем последние несколько операций"""

    data = sorted(data, key=lambda x: x["date"], reverse=True)  # сортируем список словарей по ключу 'date'
    data = data[:count_last_values]  # берем последние count_last_values операций
    return data


def format_date(data):
    """Меняем формат даты в файле"""

    for i in data:
        i['date'] = datetime.fromisoformat(i['date']).strftime('%d.%m.%Y')
    return data

def hide_sender_number(data):
    """Маскирует номер карты/счета отправителя"""

    for i in data:
        if 'from' in i:
            sender = i['from'].split()  # получаем список с информацией об отправителе из строки
            sender_number = sender[-1]  # получаем номер отправителя из списка
            if len(sender_number) == 16:
                hide_sender_number = f"{' '.join(sender[0:-1])} {sender_number[:4]} {sender_number[4:6]}** **** {sender_number[-4:]}"
                i['from'] = hide_sender_number
            elif len(sender_number) == 20:
                hide_sender_number = f"{' '.join(sender[0:-1])} **{sender_number[-4:]}"
                i['from'] = hide_sender_number
    return data


def hide_recipient_number(data):
    """Маскирует номер карты/номера получателя"""

    for i in data:
        recipient = i['to'].split()  # получаем список с информацией об получателе из строки
        recipient_number = recipient[-1]  # получаем номер отправителя из списка
        if len(recipient_number) == 16:
            hide_recipient_number = f"{' '.join(recipient[0:-1])} {recipient_number[:4]} {recipient_number[4:6]}** **** {recipient_number[-4:]}"
            i['to'] = hide_recipient_number
        elif len(recipient_number) == 20:
            hide_recipient_number = f"{' '.join(recipient[0:-1])} **{recipient_number[-4:]}"
            i['to'] = hide_recipient_number
    return data

def enter_transaction(data):
    """Создаем список строк для дальнейшего вывода в нужном нам формате"""

    operations_list = []
    for i in data:
        date = i['date']
        description = i['description']
        operations_amount = i['operationAmount']['amount'] + ' ' + i['operationAmount']['currency']['name']
        to_info = i['to']
        if 'from' in i:
            from_info = i['from']
            to_info = i['to']
            operations_list.append(f'{date} {description}\n{from_info} -> {to_info}\n{operations_amount}\n\n ')
        else:
            operations_list.append(f'{date} {description}\n{to_info}\n{operations_amount}\n\n ')
    return operations_list