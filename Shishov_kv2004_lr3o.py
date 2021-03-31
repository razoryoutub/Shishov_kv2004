# import ctypes
from tkinter import messagebox  # импортирование messagebox из tkinter для работы с диалоговыми окнами
cost_Per_Minute = 1.9  # стоимость разговора в минуту
discount = 0.2  # размер скидки
duration = float(input('Длительность разговора: '))  # ввод длительности разговора в консоль
day_of_week = int(input('Номер дня недели: '))  # ввод номера дня недели в консоль
if (day_of_week == 6) | (day_of_week == 7):  # проверка является ли день недели субботой или воскресеньем
    summ = duration * cost_Per_Minute * (1 - discount)  # расчет стоимости, если сегодня выходной
else:
    summ = duration * cost_Per_Minute  # расчет стоимости, если сегодня не выходной
# ctypes.windll.user32.MessageBoxW(0, 'Стоимость разговора: ' + str(sum) + ' ₽', 'Стоимость телефонного разговора', 0)
messagebox.showinfo(title='Стоимость разговора', message='Стоимость разговора: ' + str(summ) + ' ₽')  # вывод стоимости в окно вывода
