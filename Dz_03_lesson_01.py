number = int(input('Введите целое число от 1 до 9 ?'))
print(f'n={number}')
nn = number * 10 + number
nnn = number * 100 + nn
print(f'Считаем n+nn+nnn: {number}+{nn}+{nnn}={number + nn + nnn}.')
