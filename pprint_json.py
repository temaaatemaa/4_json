import json


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
    return json.load(file_handler)


def pretty_print_json(data):
    pprint.pprint(file, width=70,indent=5)


if __name__ == '__main__':
    pass

filepath_from_keyboard=input("Введите путь до файла ")
file=load_data(filepath_from_keyboard)
pretty_print_json(file)
