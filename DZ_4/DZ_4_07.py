def factorial_n(nu):
    f = 1
    for ind in range(1, nu+1):
        f *= ind
        yield f


nu = int(input('Введите n: '))
for i, el in enumerate(factorial_n(nu)):
    print(f'{i+1}! =  {el}')
    