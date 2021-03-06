# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

usr_file = open("out_file_5_1.txt", "w", encoding="UTF-8")  # Открываем файл на запись

while True:                                                 # запускаем бесконечный цикл
    data = input('Введите данные для записи в файл: ')      # запрашиваем у пользователя данные для записи
    if data != '':                                          # если данные не пусты, то
        usr_file.write(data + '\n')                         # Пишем их в файл, добавляя "\n" переходим на новую строку для построчного ввода
    else:                                                   # если данные пусты
        print('Ввод данных окончен, можно смотреть файл')   # пишем пользователю о том, что ввод данных закончен
        break                                               # выходим из цикла

usr_file.close()                                            # закрываем файл