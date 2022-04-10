# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.

with open("file_5_3.txt", "r", encoding="UTF-8") as data:   # Открываем файл на чтение через менеджер контеста, т.к. ничего менять в нем нет необходимости
    lines = data.readlines()                                # Построково записываем в список

    staff = [elem.split()[0] for elem in lines]             # В список записываем фамилии
    salary = [float(elem.split()[1]) for elem in lines]     # Список зарплат, из зарплат делаем числа типа float т.к. это числа и могут быть дробные

    avg_income = sum(salary) / len(salary)                  # Считаем среднюю зп как сумма всех зп на количество сотрудников

    for i in range(len(salary)):                            # проходимся по циклу
        if salary[i] < 20000:                               # если ЗП < 20К Выводим
            print(f'Сотрудник {staff[i]} имеет зарплату менее 20000 и она составляет = ', salary[i])    # выводим фамилию и значение ЗП
        else:                                               # если более, то ничего не делаем, можно эту ветку вообще не писать
            pass

    print('Средняя зарплата сотрудников = ', avg_income)

# Можно было делать через словарь и в ключи писать фамилии, а в значения ЗП, но по сути фамилии нам нужны только для вывода на экран