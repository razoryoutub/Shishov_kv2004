data = ['радар СБ', 'дозор СБ', 'курс СБ', 'BMSMIRA 42']  # список со средствами
data_type = ['радиолокационная станция', 'оптико-электронный модуль наблюения', 'система мобильного позиционирования', 'многофункциональный комплекс слежения']  # список с типами средств
for i in range(0, len(data)):  # цикл от 0 до длины списка со средствами
	print(f'{i + 1}: "{data[i]}"')  # вывод номера(+1 для удобства пользоватея) и списка со средствами
input_ok = False  # условие выхода из программы
while not input_ok:  # проверка условаия выхода из программы
	user_choose = input('Введите номер или название средства: ')  # ввод номера или названия средства
	try:
		user_choose = int(user_choose)  # попытка перевести ввод к типу int
	except:  # если не удалось перевести тип
		if user_choose in data:  # если введенное название существует в списке со средствами
			print(f'выбранное средство относится к следующему типу: {data_type[data.index(user_choose) - 1]}')  # вывод типа
			input_ok = True  # перевод условия выхода в состояние True
		else:  # если введенное название не существует в списке со средствами
			print('неверно указано название средства!')  # вывод сообщения об ошибке
	else:  # если тип ввода успешно приведен к типу int
		if user_choose > 0 and user_choose < len(data) + 1:  # проверка номера на существование
			print(f'выбранное средство относится к следующему типу: {data_type[user_choose - 1]}')  # вывод типа
			input_ok = True  # перевод условия выхода в состояние True
		else:  # если номер введен неверно
			print('неверно указан номер средства!')  # вывод сообщения об ошибке