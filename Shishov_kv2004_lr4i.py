vulnerabilities = {  # словарь с уязвимостями и компаниями производителями ПО
    'VULN-20210317.9': 'Western Digital',
    'VULN-20210317.4': 'Google',
    'VULN-20210317.3': 'Google',
    'VULN-20210317.2': 'Google',
    'VULN-20210304.5': 'Cisco',
    'VULN-20210304.4': 'Cisco',
    'VULN-20210225.1': 'VMWare',
    'VULN-20210219.6': 'Microsoft'
}
print('Выберите необходимую уязвимость: ')
for vulnerability in vulnerabilities.keys():  # вывод списка уязвимостей на экран
    print(vulnerability)


user_choose = ''
while user_choose not in vulnerabilities:
    user_choose = input('Введите название уязвимости: ')  # ожидание ввода пользователем названия уязвимости

print(f'уязвимость {user_choose} обнаружена у производителя ПО: {vulnerabilities[user_choose]}')  # вывод производителя ПО для заданной уязвимости
