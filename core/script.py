from terminaltables import AsciiTable

from core.setup_data import add_new_task
from core.setup_data import read_data


def show_table():
    data = read_data()
    table_data = [["name", "time", "messages", "path"]]
    table_data.extend(list(x.values()) for x in data)
    table = AsciiTable(table_data)
    print(table.table)


def menu():
    name = input("Name: ")
    time = input("Time: (HH:MM:SS): ")
    messages = input("Messages: ")
    path = input("Path: ")
    return name, time, messages, path


def main():
    name, time, messages, path = menu()
    add_new_task(name=name, time=time, messages=messages, path=path)
    show_table()


if __name__ == "__main__":
    main()
