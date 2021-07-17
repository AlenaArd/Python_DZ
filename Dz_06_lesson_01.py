a = 5
b = 4
day = 1
while a < 9:
    print(f'{day}-й день: {a}')
    day += 1
    a = round(a * 1.1, 2)
else:
    print(f'{day}-й день: {a}')
