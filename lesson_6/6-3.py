# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker():                                                     # Определяем класс дорога
    def __init__(self, name, surname, position, wage, bonus):       # Определяем атрибуты
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):                 # класс на основе класса Worker
    def get_full_name(self):            # Определяем метод полного имени
        result = self.name + ' ' + self.surname     # Полное имя
        return f'Полное имя сотрудника - {result}'  # Взвращаем строку с полным именем

    def get_total_income(self):         # Метод определения полного дохода
        result = self._income["wage"] + self._income["bonus"]       # Суммируем ЗП и бонусы
        return f'Доход {self.name} {self.surname} с учетом премии составил - {result}'  # Возвращаем строку с результатом

worker_1 = Position('Рулон', 'Обоев', 'odd-jobber', int(input('Введите зарплату сотрудника :')), int(input('Введите премию сотрудника :')))
worker_2 = Position('Равшан', 'Джабаров', 'mason', int(input('Введите зарплату сотрудника :')), int(input('Введите премию сотрудника :')))

print(worker_1.get_full_name())
print(worker_1.get_total_income())
print(worker_2.get_full_name())
print(worker_2.get_total_income())
