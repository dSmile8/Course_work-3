from src.utils import open_file, executed_operations, enter_transaction, get_last_values


def main():
    data = open_file()
    data = executed_operations(data)
    data = get_last_values(data, 5)
    data = enter_transaction(data)

    print('\nОперации клиента:\n')
    for i in data:
        print(i)


if __name__ == "__main__":
    main()
