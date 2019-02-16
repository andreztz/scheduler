import os
import json

from utils import validate_time


APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))

DATA_DIR = os.path.join(APPLICATION_DIR, "data")


def read_data():
    with open(DATA_DIR + "/data.json") as f:
        try:
            data = json.load(f)
            return data
        except Exception as exc:
            print(exc)
            data = []
            return data


def add_new_task(**kwargs):
    data = read_data()
    data.append(
        {
            "name": kwargs.get("name"),
            "time": kwargs.get("time"),
            "messages": kwargs.get("messages"),
            "path": kwargs.get("path"),
        }
    )
    with open(DATA_DIR + "/data.json", "w") as f:
        json.dump(data, f)


def main():
    name = input("Name: ")
    time = validate_time(input("Time: (HH:MM:SS): ")).split(" ")[1]
    messages = input("Messages: ")
    path = input("Path: ")

    add_new_task(name=name, time=time, messages=messages, path=path)
    data = read_data()
    print(data)


if __name__ == "__main__":
    main()
