# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

rating = [10, 9, 7, 5, 3, 3, 2, 1]  # Задали рейтинг - набор чисел по убыванию
new_element = int(input('введите число - новый элемент рейтинга: ')) # Делаем из него целое число сразу

i = 0                       # счетчик для ловли нужной позиции
for n in rating:            # В цикле смотрим по эементам с нулевого
    if new_element <= n:    # Если введенный элемент меньше или равен значеню из списка под номером n то прибавляем счетчик и смотрим следующий элемент списка
        i += 1
    else:
        break               # если больше то нужное i поймали, выходим
rating.insert(i, new_element)   # Вставляем новый элемент в наш рйетинг под накопленным i

print(f'Новое значение - {new_element} вставлено в {i+1}-ю позицию рейтинга: ', rating)

