import random


with open('Text_5_05.txt', 'w') as file:
    for i in range(30):
        file.write(f'{random.randint(10, 20)} ')
with open('Text_5_05.txt') as file:
    num_str = file.read().split(' ')[:-1]
    s = 0
    for num in num_str:
        s += int(num)
print(num_str)
print(f'Сумма чисел = {s}')
