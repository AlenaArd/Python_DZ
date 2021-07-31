def factorial_n(n):
    f = 1
    for ind in range(1, n+1):
        f *= ind
        yield f


n = int(input('Введите n: '))
for i, el in enumerate(factorial_n(n)):
    print(f'{i+1}! =  {el}')
    