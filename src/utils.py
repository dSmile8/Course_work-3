import json
from datetime import datetime


def open_file():
    with open('operations.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data

data = open_file()

def executed_operations(data):
    execut_operations = []
    empty_from = []
    for i in data:
        for v in i.values():
            if v == 'EXECUTED':
                execut_operations.append(i)
    for i in execut_operations:
        if 'from' in i:
            empty_from.append(i)
    return empty_from

exec_operations = executed_operations(data)
# for u in exec_operations:
#     print(u)
print(exec_operations)

def enter_transaction():
    operations_list = []
    for i in exec_operations:
        for data in i:
            date = datetime.fromisoformat(i['date']).strftime('%d.%m.%Y')  # меняем формат даты
            description = i['description']  # описание типа перевода
            from_last_elem = i['from'].split(' ')[-1]  # последний элемент строки "от кого"
            to_last_elem = i['to'].split(' ')[-1]  # последний элемент строки "кому"
            # print(' '.join(i['to'].split(' ')[0:-1]))
            if len(from_last_elem) == 16:
                from_ = ' '.join(i['from'].split(' ')[0:-1]) + ' ' + from_last_elem[0:4] + ' ' + from_last_elem[5:7] + '**' + ' **** ' + from_last_elem[-4:]
            elif len(from_last_elem) == 20:
                from_ = ' '.join(i['from'].split(' ')[0:-1]) + ' ' + '**' + from_last_elem[-4:]
            else:
                print('Длинна счета (20 цифр) либо номера карты (16 цифр) не верна')
            if len(to_last_elem) == 16:
                to = ' '.join(i['to'].split(' ')[0:-1]) + ' ' + to_last_elem[0:4] + ' ' + to_last_elem[5:7] + '**' + ' **** ' + to_last_elem[-4:]
            elif len(to_last_elem) == 20:
                to = ' '.join(i['to'].split(' ')[0:-1]) + ' ' + '**' + to_last_elem[-4:]
            else:
                print('Длинна счета (20 цифр) либо номера карты (16 цифр) не верна')
            # to = i['to']
            amount = i['operationAmount']['amount']
            currency = i['operationAmount']['currency']['name']
            return f'{date} {description}\n{from_} -> {to}\n{amount} {currency}\n\n '
print(enter_transaction())
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#






# def date_sorting():
#     date_list = []
#     date_list1 = []
#     for operations in exec_operations:
#         for key, value in operations.items():
#             if key == 'date':
#                 print(type(value))
#                 value = datetime.fromisoformat(value)
#                 #date_list.append(value)
#                 # sorted(date_list1)
#                 print(type(value))
#                 # operations['date'] = value
#                 date_list.append(operations)
#
#     return date_list
# print(date_sorting())
# # print(type(date_sorting()[1]['date']))
# # date_sort = date_sorting()
# # print(date_sort[-5:])
# # for i in date_sort:
# #     print(i)
#
#
#
#
#
#
# # print(executed_operations())
# # b = executed_operations()
# # for c in b:
# #     print(c)
#
