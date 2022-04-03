# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_funk(var_1, var_2, var_3):       # Определяем функцию с тремя аргументами
    if (var_1.isdigit() == True) and (var_2.isdigit() == True) and (var_3.isdigit() == True):   # проверяем все ли они числа
        tmp_list = [int(var_1), int(var_2), int(var_3)]     # Формируем  список из аргументов, делая их числами на этапе формирования
        tmp_list.remove(min(tmp_list))                      # убираем из списка минимальное значение
        result = sum(tmp_list)                              # записываем в результат сумму оставшихся в списке элементов
    else:
        result = f'Вы, ошиблись, необходимо вводить только цифры'     # если где-то есть не числовое значение, то в результат пишем строку с сообщением об ошибке
    return result                                                     # Возвращаем результат

user_var_1 = input('Введите первое число: ')
user_var_2 = input('Введите второе число: ')
user_var_3 = input('Введите третье число: ')

print(my_funk(user_var_1,user_var_2,user_var_3))