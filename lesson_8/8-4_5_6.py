# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. +
# А также класс «Оргтехника», который будет базовым для классов-наследников.+
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры,+
# общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.+
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# Определяем класс склад оргтехники, общего с другими классами у него нет, поэтому будет просто хранить, то что дадут, в словаре.
# что-то вроде реестра

class OfficeEquipmentWarehouse:
    def __init__(self):
        self._dict = {}         # Словарь для записи хранимого оборудования

# метод отвечающий за прием. Это реестр в виде словаря, еденицу оборудования по названию группы, в ключи пишем названия
# объектов, в значения пишем атрибуты.
    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

# метод отвечающий зв передачу в определённое подразделение компании. Хотя на самом деле просот удаляет со склада
    def take_out(self, name):
        self._dict.setdefault(name).pop(0)

    # перегружаем строку для просмотра
    def __str__(self):
        return f'на складе хранится столько оборудования: {self_dict}'

# определяем класс оборудование, с атрибутами: название, призводитель, год (производства)
class Equipment:
    def __init__(self, name, manufacturer, year):
        self.name = name
        self.manufacturer = manufacturer
        self.year = year
        self.group = self.__class__.__name__        # имя класса нужно для вывода

    # метод который возвращает имя класса
    def group_name(self):
        return f'{self.group}'

    # переопределяем вывод для просмотра
    def __str__(self):
        return f'объект {self.group} с параметрами: \n Имя: {self.name}, Производитель :{self.manufacturer}, Год :{self.year}'

    # Этот метод надо перееопределять, что бы нормально посмотреть что там записалось в реестр оборудования, в значения словаря
    def __repr__(self):
        return f'[{self.name}, {self.manufacturer}, {self.year}]'

    def action(self):
        return f'Это пока просто оборудование, оно многое может, но пока ничего не делает'

    # т.к. я не реализовывал отправку на склад пакетами, я буду проверять просто атрибуты, например год, должен быть c 2015 до 2022
    @staticmethod
    def validation(year):
        if 2015 <= year <= 2022:
            return print(f'год поизводства {year} прошел валидацию')
        else:
            return print(f'год поизводства {year} не прошел валидацию')

# Определяем класс "принтер" для которого "Оборудование" - родительский, отличается от родительского признаком лазерности
class Printer(Equipment):
    def __init__(self, name, manufacturer, year, is_laser=False):
        super().__init__(name, manufacturer, year)
        self.is_laser = is_laser

    def action(self):
        return f'Это принтер, он может печатать'

# Определяем класс "сканер" для которого "Оборудование" - родительский, отличается от родительского признаком работы с формтами выше а4
class Scaner(Equipment):
    def __init__(self, name, manufacturer, year, is_A4plus=False):
        super().__init__(name, manufacturer, year)
        self.is_A4plus = is_A4plus

    def action(self):
        return f'Это сканер, он может сканировать'


# Определяем класс "ксерокс" для которого "Оборудование" - родительский
class Xerox(Equipment):
    def __init__(self, name, manufacturer, year, is_mfu=False):
        super().__init__(name, manufacturer, year)
        self.is_mfu = is_mfu

    def action(self):
        return f'Это копировальный агрегат, он копирует'

# Создаем объект склад
sklad = OfficeEquipmentWarehouse()

# создаем объекты разных типов
printer_1= Printer('hp','japan', 2020)
scaner_1 = Scaner('hp','USA', 2021)
xerox_1 = Xerox('kyocera','China', 2022)
xerox_2 = Xerox('xerox','Thaiwan', 2022)
# смотрим, что получилось
print(printer_1)
print(scaner_1)
print(xerox_1)
print(xerox_2)

# добавляем на склад объекты
sklad.add_to(printer_1)
sklad.add_to(scaner_1)
sklad.add_to(xerox_1)
sklad.add_to(xerox_2)
# Смотрим склад
print(sklad._dict)
# Забираем со склада / отправляем куда-то, куда хз
sklad.take_out('Scaner')

# Смотрим склад снова
print(sklad._dict)

# Смотрим валидацию на заранее плохом объекте
printer_bad = Printer('canon', 'Canada', 1991)
Printer.validation(printer_bad.year)

