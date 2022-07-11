class Myecxept(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b


x = float(input('Введите делимое - '))
y = float(input('Введите делитель - '))

try:
    res = x / y
except ZeroDivisionError:
    print("Делить на ноль НЕЛЬЗЯ!!!")
else:
    print("Все нормально. x/y=", res)
