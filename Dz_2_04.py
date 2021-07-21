words_str = input('Введите несколько слов, разделяя их пробелами')
words_list = words_str.split()
for i in range(len(words_list)):
    s = words_list[i]
    print(i + 1, end = ') ')
    print(s[:9])
print(f'Вы ввели {len(words_list)} слов.')
