import json
from datetime import datetime
from path import Path

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
        if 'state' in v and v['state'] == 'EXECUTED' and 'from' in v:
            execut_operations.append(v)
    return execut_operations


def get_last_values(data, count_last_values):
    """Сортируем список по дате и оставляем последние несколько операций"""

    data = sorted(data, key=lambda x: x["date"], reverse=True)  # сортируем список словарей по ключу 'date'
    data = data[:count_last_values]  # берем последние count_last_values операций
    return data


def enter_transaction(data):
    """Создаем список строк для дальнейшего вывод в нужном нам формате"""

    operations_list = []
    for i in data:
        date = datetime.fromisoformat(i['date']).strftime('%d.%m.%Y')  # меняем формат даты
        description = i['description']                                 # описание типа перевода
        operations_amount = f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"
        if 'from' in i:
            sender = i['from'].split()  # получаем список с информацией об отправителе из строки
            recipient = i['to'].split()  # получаем список с информацией об получателе из строки
            sender_number = sender.pop()  # получаем номер отправителя из списка
            recipient_number = recipient.pop()  # получаем номер отправителя из списка
            if len(sender_number) == 16:
                hide_sender_number = f"{sender_number[:4]} {sender_number[4:6]}** **** {sender_number[-4:]}"
            elif len(sender_number) == 20:
                hide_sender_number = f"**{sender_number[-4:]}"
            if len(recipient_number) == 16:
                hide_recipient_number = f"{recipient_number[:4]} {recipient_number[4:6]}** **** {recipient_number[-4:]}"
            elif len(recipient_number) == 20:
                hide_recipient_number = f"**{recipient_number[-4:]}"
            to_info = f"{' '.join(recipient)} {hide_recipient_number}"
            from_info = f"{' '.join(sender)} {hide_sender_number}"
        else:
            from_info, to_info = '', ''
        operations_list.append(f'{date} {description}\n{from_info} -> {to_info}\n{operations_amount}\n\n ')
    return operations_list