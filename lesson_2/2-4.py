# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

user_string = input('Введите строку, разделяя слова пробелами: ')
user_list = user_string.split()   # Это уже список, для рездленеия используем сплит с пробелом, пробел явно можно не укзывать, а можно указывать

print(user_list) # Необязательная строка, просто смотрю что получилось

t=0     # Переменная для нумерации строк и обращения к нужному элементу списка
for i in user_list:
    print(f'{t+1}-я строка : ', str(user_list[t])[:10])     # Выводим номер строки + элемент списка с заданным номером, делая из него строку и применяя к строке обрезку до 10 знака
    t += 1
