x = input('Введите первое число: ')  # ввод первого числа
y = input('Введите второе число: ')  # ввод второго числа
if ((4 > abs(x) > 0 or abs(x) == 5 or abs(x) == 7) or (x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0 and x != 0)) and ((4 > abs(y) > 0 or abs(y) == 5 or abs(y) == 7) or (y % 2 != 0 and y % 3 != 0 and y % 5 != 0 and y % 7 != 0 and y != 0)):  # проверка чисел на простоту
	list_for_Evklid = [max(x, y), min(x, y)]  # если оба числа простые используем алгоритмом Евклида чтобы найти наибольший общий делитель
	while 0 not in list_for_Evklid:  # пока в последовательности нет нуля
		list_for_Evklid.append(list_for_Evklid[-2] % list_for_Evklid[-1])  # добавляем элемент, который равен остатку от деленя двух последних элементов последовательности
	nod = list_for_Evklid[-2]  # наибольший общий делитель это предпоследний элемент последовательности
if 'nod' in globals():  # проверяем существует ли переменная nod (наибольший общий делитель)
	print(f'наименьшее общее кратное равно: {int(x * y / nod)}')  # выводим наименьшее общее кратное, согласно формуле поиска наименьшего общего кратного с использованием наибольшего общего делителя
else:  # если наибольший общий делитель не был найден
	start = 1  # начало цикла поиска
	end = 1000  # окончание цикла поиска
	while True:  # бесконечный цикл
		x_list = []  # список для переменной x
		y_list = []  # список для переменной y
		for i in range(start, end + 1):  # цикл от переменной начала до переменной конца
			x_list.append(x * i)  # добавление элемента в последовательность
			y_list.append(y * i)  # добавление элемента в последовательность
		for i in range(0, len(x_list)):  # цикл от 0 до длины списка для переменной x
			if x_list[i] in y_list:  # если элемент из списка для переменной x есть в  списке для переменной y
				print(f'наименьшее общее кратное равно: {x_list[i]}')  # вывод наименьшего общего кратного
				exit()  # выход
		start += 1000  # увеличение начальной переменной
		end += 1000  # увеличение конечной переменной
