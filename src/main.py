from src.utils import *


def main():
    data = open_file()
    data = executed_operations(data)
    data = get_last_values(data, 5)
    data = format_date(data)
    data = hide_sender_number(data)
    data = hide_recipient_number(data)
    data = enter_transaction(data)

    print('\nОперации клиента:\n')
    for i in data:
        print(i)


if __name__ == "__main__":
    main()
