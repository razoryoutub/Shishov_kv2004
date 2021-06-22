import tkinter as tk  # импортируем tkinter
import tkinter.ttk as ttk  # импортируем расширение для tkinter
box = {}  # глобальный пустой словарь
victories = {}  # пустой словарь для количества побед
print('Введите названия стран-участниц\n(для окончания нажмите enter:)\n')  # вывод в консоль
while True:  # пока истина
	country = input()  # вводим название страны
	if country == '':  # если строка пустая
		break  # прерываем цикл
	box[country] = 0  # присваиваем ключу значение 0
for strana in box:  # для каждой страны в словаре
	a = int(input(f'{strana} - количество побед по внедрению вредоносного кода: '))  # вводим количество побед по внедрению вредоносного кода
	b = int(input(f'{strana} - количество побед по получению административного доступа: '))  # вводим количество побед по получение административного доступа
	c = int(input(f'{strana} - количество побед по организации отказа в обслуживании: '))  # вводим количество побед по организации отказа в обслуживании
	victories[strana] = a + b + c  # записываем в словарь сумму количества побед для страны
	box[strana] = a * 7 + b * 6 + c * 5  # записываем в глоабльный словарь сумму очков
sort_box = sorted(box.items(), key=lambda x: x[1], reverse=True)  # возвращаем отсортированный по значениям список
countrys = []  # пустой список для стран
count_ochkov = []  # пустой список для суммы очков
count_victories = []  # пустой список для количества побед
for strana in sort_box:  # для стран из отсортированного списка
	countrys.append(strana[0])  # добавляем название страны
	count_ochkov.append(strana[1])  # добавляем сумму очков
	count_victories.append(victories[strana[0]])  # добавляем количество побед


class Table(tk.Frame):  # создаём класс
	def __init__(self, parent=None, headings=list(), rows=list()):  # инициализируем класс с переменными заголовка и строки
		super().__init__(parent)  # множественное наследование

		table = ttk.Treeview(self, show="headings", selectmode="browse")  # виджет разделителя на колонки
		table["columns"] = headings
		table["displaycolumns"] = headings

		for head in headings:
			table.heading(head, text=head, anchor=tk.CENTER)  # расставляем названия
			table.column(head, anchor=tk.CENTER)  # расставляем колонки

		for row in rows:
			table.insert('', tk.END, values=tuple(row))

		scrolltable = tk.Scrollbar(self, command=table.yview)   # добавляем скролбар
		table.configure(yscrollcommand=scrolltable.set)   # конфигурируем его
		scrolltable.pack(side=tk.RIGHT, fill=tk.Y)   # ставим его на форму
		table.pack(expand=tk.YES, fill=tk.BOTH)   # ставим форму


rows_countrys = []  # пустой список для строк со странами
for i in range(len(countrys)):  # по длине списка стран
	for j in range(3):  # создаем три столбца
		exec(f'country_{i} = (countrys[{i}], count_ochkov[{i}], count_victories[{i}])')  # переводим строку в код
	exec(f'rows_countrys.append(country_{i})')  # переводм строку в код, добавляем название страны в список


root = tk.Tk()  # создаем окно вывода
table = Table(root, headings=['Страна', 'Количество очков', 'Количество побед'], rows=rows_countrys)  # заполнение таблицы
table.pack(expand=tk.YES, fill=tk.BOTH)
root.mainloop()  # запускаем работу главного цикла
