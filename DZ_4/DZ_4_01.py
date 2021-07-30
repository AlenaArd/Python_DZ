def work_pay(w_hour, w_cost, w_bonus):
    w_pay = w_hour * w_cost + w_bonus
    return w_pay

w_hour = float(input('Введите данные - кол-во часов: '))
w_cost = float(input('Введите данные - ставка: '))
w_bonus = float(input('Введите данные - премия: '))
print('Заработная плата равна: ', work_pay(w_hour, w_cost, w_bonus))

""" Попытка переделать с учетом разбора ДЗ на уроке, у меня этот код не запускается
import sys
if len(sys.argv) < 4:
    raise w_value(f'Введите данные - кол-во часов: ставка: премия: ')
else:
    w_hour = float(sys.argv[0])
    w_cost = float(sys.argv[1])
    w_bonus = float(sys.argv[2])
    w_pay = w_hour * w_cost + w_bonus
    print(f'Заработная плата равна: {w_pay}')
"""