# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

def int_func(var):          # Определяем функцию с одним аргументом
    if (var.islower() == True) and (ascii(var)[1:-1].isalpha() == True): # проверка на начало с маленькой буквы и потом на латинский алфавит
        result = var.capitalize()   # делаем первую букву заглавной, остальные маленькими, можно через title
    else:
        result = f'Вы где то ошиблись, проверьте язык ввода'
    return result

usr_var = input('Введите слово на латинском языке: ')

print(int_func(usr_var))