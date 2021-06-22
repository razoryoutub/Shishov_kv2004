import math  # импорт библиотеки math
n = int(input('Введите значение n: '))  # ввод значения n
m = int(input('Введите значение m: '))  # ввод значения m
x = int(input('Введите значние x: '))  # ввод значения x
c = int(input('Введите значение C: '))  # ввод значения c

if (n + m == 0) or (n - m == 0):  # проверка введённых значений по ОДЗ
    print('Введённые значения не входят в область допустимых значений!')  # вывод в случае неверно введённых значений
else:  # иначе, если значения введены верно
    f = (math.sin(m-n) * x)/(2*(m-n)) - ((math.sin(m+n) * x)/(2*(m+n))) + c  # вычисление значения функции
    print('Значение функции равно: ', f)  # вывод в случае успешного расчета функции
