# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num = input('Введите число :')              # запрашиваем на ввод число, но знаем, что это строка
num_2 = num + num                           # получаем второе слагаемое, тоже строка
num_3 = num + num + num                     # получаем третье слагаемое, тоже строка
result = int(num) + int(num_2) + int(num_3) # получаем итоговое значение, через смену типа переменной

print(f"{num} + {num_2} + {num_3} =", result)   # выводим результат в привычном виде
