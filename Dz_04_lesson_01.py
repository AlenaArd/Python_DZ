number = input('Введите целое положительное число.')
maxim = 0
probe = 0
n = len(number)
remainder = int(number)
while n > 0:
    n -= 1
    d = 10 ** n
    probe = remainder // d
    remainder = remainder % d
    if probe == 9:
        maxim = 9
        break
    if probe >= maxim:
        maxim = probe
else:
    print(f'самая большая цифра в числе "{number}" = {maxim}')
