# TODO Напишите функцию для поиска индекса товара
def fnc_item_finder(products_list, item):
    for i, fruit in enumerate(products_list):
        if fruit == item:
            item_position = i
            break
        else:
            item_position = None
    return item_position


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = fnc_item_finder(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
