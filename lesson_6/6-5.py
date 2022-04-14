# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        return print('Запуск отрисовки ручкой')
class Pencil(Stationery):
    def draw(self):
        return print('Запуск отрисовки карандашем')
class Handle(Stationery):
    def draw(self):
        return print('Запуск отрисовки маркером')

stationery_1 = Stationery('Абстрактная концелярская принадлежность')
pen_1 = Pen('Шариковая ручкая')
pencil_1 = Pencil('Карандаш')
handle_1 = Handle('Маркер')

stationery_list = [stationery_1, pen_1, pencil_1, handle_1]

for elem in stationery_list:
    elem.draw()

