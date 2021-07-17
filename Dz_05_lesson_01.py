proceeds = int(input('Введите значение выручкики фирмы'))
cost = int(input('Введите значение издержек фирмы'))
if proceeds>cost:
    rentability = round((proceeds - cost) / proceeds * 100, 2)
    print (f'Ваша фирма работает в прибыль, выручка больше издержек. Рентабельность состовляет {rentability} %.')
    amount = int(input('Введите колличество сотрудников фирмы'))
    print(f'Прибыль на одного сотрудника состaвляет {round((proceeds - cost) / amount, 2)} руб.')
else:
    print('Ваша фирма работает в убыток, издержки не больше выручки.')


