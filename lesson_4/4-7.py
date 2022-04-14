# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

def fact(num):      # Опеределяем функцию с одним аргументов
    result = 1      # переменная для накопления
    if num == 0:
        return result   #   Для нуля определяем руками значение = 1, так говорит математика 0!=1
    else:
        for i in range(num):    # Для не нуля, накапливаем значение
            yield f'{i}! = {result}'
            result *= i + 1

usr_num = int(input('Введите число для рассчета факториала :'))

for el in fact(usr_num + 1):    # Вызываем функцию, +1 надо что бы если человек введет 11, он увидел факториал 11, а не 10
    print(el)
