# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDivInsurance:
    def __init__(self, dividend, devider):
        self.dividend = float(dividend)
        self.devider = float(devider)

    @staticmethod
    def validation(dividend, devider):
        try:
            return f'Деление возможно, результат = {dividend / devider}'
        except:
            return f'Вы пытаетесь поделить на ноль, не надо так'

    def __str__(self):
        return f"Вы хотите поделить {self.dividend} на {self.devider}"

obj_1 = ZeroDivInsurance(input('Введите делимое'),input('Введите делитель'))
print(obj_1)

print(ZeroDivInsurance.validation(obj_1.dividend,obj_1.devider))
