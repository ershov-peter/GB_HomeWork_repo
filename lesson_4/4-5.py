# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce()

from functools import reduce

def my_func(var_1, var_2):  # Функция которая перемножает два числа
    result = var_1 * var_2
    return result

result_list = [el for el in range(100, 1000 + 1) if el % 2 == 0]    # Формируем список четных числе, +1 что бы 1000 вошла в правую границу, + условие на четност, но можно в рендж добавить третий аргумент (100, 1000+1,2)
print(f'Список четных чисел :', result_list)
print(f' произведение всех четных эелементов от 100 до 1000 = ', reduce(my_func, result_list)) # Проверять не стал, уж больно большое число получается


