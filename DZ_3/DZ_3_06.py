def int_func(in_word):
    word = in_word[0].upper() + in_word[1:].lover()
    return (word)

print(int_func('word'))

st_list = input('введите слова:')
for in_word in st_list.split(' '):
    print(f'{int_func(in_word)}', end='.')
