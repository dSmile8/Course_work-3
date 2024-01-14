import json
from datetime import datetime


def open_file():
    with open('operations.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data

operations = open_file()

def executed_operations():
    execut_operations = []
    for i in operations:
        for v in i.values():
            if v == 'EXECUTED':
                execut_operations.append(i)
    return execut_operations



# print(executed_operations())
# b = executed_operations()
# for c in b:
#     print(c)

