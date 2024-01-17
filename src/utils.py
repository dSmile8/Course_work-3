import json
from datetime import datetime


def open_file():
    """Открывает json файл и записывает его в переменную 'data' """

    with open('../operations.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def executed_operations(data):
    """Оставляем EXECUTED(выполненные операции) и убираем операции без поля отправитель(from)"""

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

    global from_, to_
    operations_list = []
    for i in data:
        date = datetime.fromisoformat(i['date']).strftime('%d.%m.%Y')  # меняем формат даты
        description = i['description']  # описание типа перевода
        from_last_elem = i['from'].split(' ')[-1]  # последний элемент строки "от кого"
        to_last_elem = i['to'].split(' ')[-1]  # последний элемент строки "кому"
        if len(from_last_elem) == 16:  # задаем условия для разных длинн счет/номер карты отправителя
            from_ = ' '.join(i['from'].split(' ')[0:-1]) + ' ' + from_last_elem[0:4] + ' ' + from_last_elem[4:6] + '**' + ' **** ' + from_last_elem[-4:]
        elif len(from_last_elem) == 20:  # задаем условия для разных длинн счет/номер карты отправителя
            from_ = ' '.join(i['from'].split(' ')[0:-1]) + ' ' + '**' + from_last_elem[-4:]
        if len(to_last_elem) == 16:  # задаем условия для разных длинн счет/номер карты получателя
            to_ = ' '.join(i['to'].split(' ')[0:-1]) + ' ' + to_last_elem[0:4] + ' ' + to_last_elem[4:6] + '**' + ' **** ' + to_last_elem[-4:]
        elif len(to_last_elem) == 20:  # задаем условия для разных длинн счет/номер карты получателя
            to_ = ' '.join(i['to'].split(' ')[0:-1]) + ' ' + '**' + to_last_elem[-4:]
        amount = i['operationAmount']['amount']  # сумма перевода
        currency = i['operationAmount']['currency']['name']  # валюта
        operations_list.append(f'{date} {description}\n{from_} -> {to_}\n{amount} {currency} \n\n ')
    return operations_list