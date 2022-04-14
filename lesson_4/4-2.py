# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.



my_list = [17, 5, 12, 15, 6, 18, 4, 5, 6, 13]       # Исходный список
print(my_list)


result_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el-1]]
print(result_list)


