# вариант 1
def myfunk_ab(a, b):
    if a <= 0 or b > 0:
        print('Должно выполняться условие: a>0 и b<0')
    else:
        return 1 / (a ** (-1 * b))

a = float(input('Введите a положительное число:'))
b = int(input('Введите b - целое, отрицательное'))
print('а в степени b = ', myfunk_ab(a, b))

# вариант 2
def myfunk_ab(a, b):
    if a <= 0 or b > 0:
        print('Должно выполняться условие: a>0 и b<0')
    else:
        c = 1
        for i in range(b * -1):
            c *= a
        return 1 / c


a = float(input('Введите a положительное число:'))
b = int(input('Введите b - целое, отрицательное'))
print('а в степени b = ', myfunk_ab(a, b))


