x = int(input('Введите число: '))  # получаем число на вход
sl = []  # создаем пустой список для ответов
for i in range(1, x + 1):  # цикл от 1 до введенного числа
	for j in range(1, x + 1):  # цикл от 1 до введенного числа
		if (i + j == x) and (f'{str(i)} + {str(j)}' not in sl) and (f'{str(j)} + {str(i)}' not in sl):  # если i + j = x и ответ ещё не был записан в список с ответами
			sl.append(f'{str(i)} + {str(j)}')  # записываем ответ
for i in sl:  # цикл вывода ответов
	print(f'{i} = {x}')  # вывод ответа
