default = 0.5  # коэффициент по умолчанию
countries = {  # словарь с коэффициентами для разных стран
    'Россия': 0.4059,
    'Англия': 0.453592,
    'Австрия': 0.56001,
    'Германия': default,
    'Дания': default,
    'Исландия': default,
    'Италия': 0.31762,
    'Нидерланды': default
}


print('Выберите страну из списка: ')
for country in countries.keys():  # вывод списка всех стран
    print(country)


user_select = ''
while user_select not in countries:  # ожидание ввода пользователем страны из списка
    user_select = input('Введите страну из списка: ')


pounds = float(input('Введите вес в фунтах: '))  # ввод веса в функтах
kg = pounds * countries[user_select]  # конвертация фунтов в килограммы
print(f'В стране {user_select}: {pounds} (фунт) = {kg} (кг)')  # вывод
