nalog = int(input('Введите величину налога: '))  # ввод величины налога
for i in range(1, 16):  # цикл длинной в 15 дней
	nalog = nalog * (301 / 300)  # перерасчет задолжности
	print(f'день {i}: сумма {nalog}')  # вывод задолжности
