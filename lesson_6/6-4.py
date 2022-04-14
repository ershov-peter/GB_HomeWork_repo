# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

from random import choice                           # Для выбора направления

class Car():
    direction = ['Прямо', 'влево', 'вправо', 'назад']   # Словарь с направлениями

    def __init__(self, speed, color, name, is_police=False):    # Определяем атрибуты, по умолчанию машина не полицейская, цвет получился ненужный)
        self.speed = speed
        self.color = color
        self. name = name
        self.is_police = is_police

    def go(self):                       # метод, который сообщает, что машина поехала
        return f'Машина {self.name} в движении'

    def stop(self):                     # метод, который сообщает, что машина остановилась
        return f'Машина {self.name} остановилась'

    def turn(self):                     # метод, который сообщает, что машина повернула и куда
        return f'Машина {self.name} едет {choice(self.direction)}'

    def show_speed(self):               # родительский метод, который показывает скорост
        return f'Машина {self.name} двигается со скоростью {self.speed}'

class TownCar(Car):
    def show_speed(self):               # переопределяем метод,которйы показывает скорост
        if self.speed <= 60:
            result = super().show_speed()
        else:
            result = f'Машина {self.name} превысила допустимую скорость на {self.speed - 60}'
        return result

class SportCar(Car):
    """ SportCar"""

class WorkCar(Car):                     # переопределяем метод,которйы показывает скорост
    def show_speed(self):
        if self.speed <= 40:
            result = super().show_speed
        else:
            result = f'Машина {self.name} превысила допустимую скорость на {self.speed - 40}'
        return result

class PoliceCar(Car):                   # переопределяем исходный набор атрибутов для полицеской машины, на самом деле только один из атрибутов is_police

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)

# Создаем экземпляры разных классов
town_car_1 = TownCar(75, 'белый', 'Смарт')
sport_car_1 = SportCar(150, 'баклажан', 'Лада Калина')
work_car_1 = WorkCar(60, 'Оранжевый', 'Камаз')
police_car_1 = PoliceCar(100, 'Черно-белый', 'Форд фокус')

# Выводим все методы
print(town_car_1.show_speed())
print(work_car_1.show_speed())
print(sport_car_1.turn())
print(police_car_1.go())
print(town_car_1.stop())



