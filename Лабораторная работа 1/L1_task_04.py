users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dict_visitors = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

dict_visitors["Общее количество"] = len(users)
unique_visitors = set(users)
dict_visitors["Уникальные посещения"] = len(unique_visitors)

print(dict_visitors)
