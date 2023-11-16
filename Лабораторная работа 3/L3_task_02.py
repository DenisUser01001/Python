# TODO Напишите функцию find_common_participants
def find_common_participants(list01, list02, devidor=","):
    common_list = list(set(list01.split(devidor)).intersection(set(list02.split(devidor))))
    common_list.sort()
    return common_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
