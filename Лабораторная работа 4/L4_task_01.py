import json


def task() -> float:
    """ функция читает JSON файл и находит сумму произведений
     двух значений по ключам "score" и "weight" в каждом словаре.

    Функция должна вернуть значение с плавающей запятой,
     округленное до 3 знаков после запятой."""

    with open("input.json") as file:
        data = json.load(file)

    list_of_multiplications = [(i["score"] * i["weight"]) for i in data]

    return round(sum(list_of_multiplications),3)


print(task())
