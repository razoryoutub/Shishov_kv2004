from math import exp, pi  # импортирование переменной pi и функции exp из модуля math
x = int(input('Введите значение x: '))  # Ввод пользователем значения x в переменную x
y = exp(x * pi) + 1  # Вычисление значения y и помещение его в переменную y
print('Значение y: ', y)  # Вывод текста и значения y в консоль