# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# сли ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.


class Cell:
    def __init__(self, alveola):
        self.alveola = int(alveola)

# перегружаем метод add
    def __add__(self, other):
        return f'Количество ячеек объединенной клетки = {self.alveola + other.alveola}'

# перегружаем метод sub
    def __sub__(self, other):
        result = self.alveola - other.alveola
        if result > 0:
            return f'Количество ячеек уменьшилось и теперь = {result}'
        else:
            return f'Похоже клетка умерла, но мы будем ее помнить ('


# перегружаем метод mul
    def __mul__(self, other):
        return f'Количество ячеек в итоговой клетке = {self.alveola * other.alveola}'

# перегружаем метод truediv
    def __truediv__(self, other):
        return f'Количество ячеек в итоговой клетке = {self.alveola // other.alveola}'

# реализуем метод make_order()
    def make_order(self, number):
        tmp = self.alveola // number    # Сколько целых рядов надо будет вывести
        for i in range(tmp):
            print(f'{i + 1}-ый ряд :', '*' * number)     # В цикле выводим целые ряды *
        print(f'{tmp + 1}-ый ряд :', '*' * (self.alveola - tmp * number))    # ряд с остатками *

# Создаем экземпляры класса
cell_1 = Cell(27)
cell_2 = Cell(11)

# Смотрим как отрабатывают перегруженные методы
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

# Смотрим как отрабатывает метод make_order
print(cell_1.make_order(8))
