def div_ab(a, b):
    if b == 0:
        print('на 0 делить НЕЛЬЗЯ!')
    else:
        return a / b


a = float(input('Введите делимое - '))
b = float(input('Введите делитель - '))
print('часное = ', div_ab(a, b))
