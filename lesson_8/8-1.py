# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


# Определяем класс с одним атрибутом в виде строки, куда пишеться дата
class Date:
    def __init__(self, date_string):
        self.date_string = str(date_string)

    # метод класса, извлекающий дату и преобразующей ее в целые числа, возвращает список из дня, месяца, года
    @classmethod
    def date_extractor(cls, date_string):
        return list(map(int, date_string.split('-')))

    # статический метод, на входе получает список, проверяет числа на предмет принадлежности области допустимых значений
    # для года взял от балды нашу эру и до выборов президента )
    @staticmethod
    def date_validation(some_list):
        day, month, year = some_list[0], some_list[1], some_list[2]
        if 1 <= day <= 31:
            if 0 < month <= 12:
                if 0 <= year <= 2024:
                    return f'Дата прошла валидацию!'
                else:
                    return f'Дата не прошла валидацию, проверьте правильность ввода года: {year}'
            else:
                return f'Дата не прошла валидацию, проверьте правильность ввода месяца: {month}'
        else:
            return f'Дата не прошла валидацию, проверьте правильность ввода дня: {day}'

    # переопределяем метод str для просмотра даты и метода по извлечению дат
    def __str__(self):
        return f"Текущая дата объекта {Date.date_extractor(self.date_string)}"

# создаем две строки для передачи экземплярам класса, вторая дата с косяком
str_1 = '12-11-2012'
str_2 = '15-15-2022'
# создаем два объекта с этими строками
date_1 = Date(str_1)
date_2 = Date(str_2)
# Смотрим объекты
print(date_1)
print(date_2)
# Смотрим метод извелкающий даты на классе
print(Date.date_extractor(str_1))
print(Date.date_extractor(str_2))
# Смотрим метод извелкающий даты на объектах
print(date_1.date_extractor(date_1.date_string))
print(date_2.date_extractor(date_2.date_string))
# Смотрим метод валидации через класс и через объект
print(Date.date_validation(date_1.date_extractor(date_1.date_string)))
print(date_2.date_validation(date_2.date_extractor(date_2.date_string)))
