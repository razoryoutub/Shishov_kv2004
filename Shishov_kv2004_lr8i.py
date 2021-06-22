import tkinter as tk  # импортируем tkinter
import tkinter.ttk as ttk  # импортируем расширение для tkinter
ob = {}  # пустой основной словарь
while True:  # пока истина
    id = input('ID:\n')  # вводим ключ
    if id == '':  # если пустая строка
        break  # прерываем цикл
    u = input('Наименование дочерней компании:\n')  # вводим наименование компании
    o = input('Город:\n')  # вводим город
    vloz = [u, o]  # пустой список
    inc = []  # пустой список по зависимостям от зарубежних компаний
    for i in range(6):  # ввод 6 зависимостей в список
        c = int(input('зависимость:\n'))  # ввод зависимостей
        inc.append(c)  # добавлем зарубежнюю компанию в список
    for i in inc:  # элементы из списка зарубежних компаний
        vloz.append(i)  # добавляем в список компанию
    s = sum(inc)  # считаем сумму зависимостей
    vloz.append(s)  # добавляем в список сумму
    ob[id] = vloz  # словарь

sort_m = sorted(ob.items(), key=lambda x: x[1][-1], reverse=True)  # сортировка по значению (суммы зависимостей)
id_2 = []  # список для значений id
name = []  # список для наименований дочерних компаний
obj = []  # список для городов
ovo = []  # список для Microsoft
ncd = []  # список для amazon
ud = []  # список для google
md = []  # список для vivo
nfts = []  # список для mikrotik
niv = []  # список для siemens
summ = []  # список для суммы

for row in sort_m:  # элементы из отсортированного списка
    id_2.append(row[0])  # список для значений id
    name.append(row[1][0])  # список для наименований дочерних компаний
    obj.append(row[1][1])   # список для городов
    ovo.append(row[1][2])  # список для Microsoft
    ncd.append(row[1][3])  # список для amazon
    ud.append(row[1][4])  # список для google
    md.append(row[1][5])  # список для vivo
    nfts.append(row[1][6])  # список для mikrotik
    niv.append(row[1][7])  # список для siemens
    summ.append(row[1][8])  # список для суммы


class Table(tk.Frame):  # создаём класс
    def __init__(self, parent=None, headings=list(), rows=list()):  # инициализируем
        super().__init__(parent)  # множественное наследование

        table = ttk.Treeview(self, show="headings", selectmode="browse")  # виджет разделителя на колонки
        table["columns"] = headings
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


rows_danger = []
for i in range(len(id_2)):
    for j in range(10):
        exec(f'danger_{i} = (id_2[{i}], name[{i}], obj[{i}], ovo[{i}], ncd[{i}], ud[{i}],md[{i}], nfts[{i}],niv[{i}], summ[{i}])')
    exec(f'rows_danger.append(danger_{i})')


root = tk.Tk()
table = Table(root, headings=['ID', 'Наименование дочерней компании', 'Город расположения', 'microsoft', 'amazon', 'google', 'vivo', 'mikrotik', 'siemens', 'Сумма'], rows=rows_danger)
table.pack(expand=tk.YES, fill=tk.BOTH)
root.mainloop()
