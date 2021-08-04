with open('Text_5_01.txt', 'w') as file:
    in_str = input('Введите текстовую строку:\n')
    while in_str:
        file.write(f'{in_str}\n')
        in_str = input('Введите текстовую строку:\n')
