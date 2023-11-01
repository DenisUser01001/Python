numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
new_list = numbers[:4] + numbers[5:]
average_of_new_list = sum(new_list)/(len(new_list)+1)
numbers[4] = average_of_new_list

print("Измененный список:", numbers)
