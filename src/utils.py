import json


def open_file():
    with open('operations.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


