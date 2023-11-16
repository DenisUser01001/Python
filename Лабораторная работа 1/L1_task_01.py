numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
missing_index = 4  # Определение индекса элемента, который требуется заменить.

new_list = numbers[:missing_index] + numbers[missing_index+1:]
print(len(new_list))
print(len(numbers))
average_of_new_list = sum(new_list)/(len(numbers))
numbers[missing_index] = average_of_new_list

print("Измененный список:", numbers)
