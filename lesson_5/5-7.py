# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).

import json             # Для импорта в json

profit = {}             # Словарь с прибылью
avg_profit = {}         # Словарь со средним значением
result_list = []        # Итоговый список

# Открываем файлы на запись для json и для чтения из файла
with open("Out_file_5_7.jsone", "w", encoding="UTF-8") as out_data, open("file_5_7.txt", "r", encoding="UTF-8") as in_data:
    lines = in_data.readlines()     # Список строк
    profit = {elem.split()[0]: int(elem.split()[2]) - int(elem.split()[3]) for elem in lines}   # формируем словарь с прибылями
    profit_result = 0
    for i in profit:                    # в цикле считаем среднюю прибыль,выкидывая отрицательные значения
        if profit[i] > 0:
            profit_result += profit[i]
        else:
            pass
    avg_profit["average_profit"] = profit_result / len(profit)  # Формируем словарь сосредней прибылью
    result_list = [profit, avg_profit]                          # Формируем итоговый список

    # Смотрим что получилось
    print(profit)
    print(avg_profit)
    print(result_list)

    json.dump(result_list, out_data, ensure_ascii=False)



