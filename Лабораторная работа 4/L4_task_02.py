# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    """Читает CSV файл, разбирает его на отдельные столбцы.
    Создаёт для каждой записи словарь в формате JSON, где ключами будут названия столбцов,
     а значениями - соответствующие значения в этой строке."""

    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME) as input_csv:
        list_of_dics = []
        reader = csv.DictReader(input_csv, delimiter=",")
        for row in reader:
            # print(row)
            # print(type(row))
            list_of_dics.append(row)
        # print(list_of_dics)
        # print(type(list_of_dics))

    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w",) as output_json:
        json.dump(list_of_dics, output_json, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
