text = "Буря мглою небо покроет"  # Вводим значение нашей строки
text_splited = text.split()  # разделяем строку на массив с отдельными словами
# (при нескольких пробелах между словами программа всё равно корректно разделяет предложение)
len_1 = len(text_splited[0])  # длинна слова номер 1
len_2 = len(text_splited[1])  # длинна слова номер 2
len_3 = len(text_splited[2])  # длинна слова номер 3
len_4 = len(text_splited[3])  # длинна слова номер 4
lens = [len_1, len_2, len_3, len_4]  # объединяем все длины в массив
number_of_word = list(max(enumerate(lens)))[0]  # поиск номера самого длинного слова
count_of_letters = list(max(enumerate(lens)))[1]  # определение максимальной длинны
print(str(text_splited[number_of_word]) + ' - самое длинное слово в предложении (' + str(count_of_letters) + ')')  # вывод на экран
