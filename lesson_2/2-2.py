# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

user_string = input('Введите ваш список, значения списка указывайте через запятую - ",": ')    # Это пока не список, это строка. Можно сделать сразу список через list()
user_list = user_string.split(",")   # Это уже строка, для рездленеия используем сплит с запятой

print(user_list) # Выводим исходную строку

for i in range(0, len(user_list)-1, 2):     # Прогоняем цикл от 0 элемента до последнего
    user_list[i], user_list[i+1] = user_list[i+1], user_list[i]     # меняем i и i+1 местами с i+1 и i, можно делать через временную переменную, но так красивей)

print(user_list) # Выводим итоговую строку
