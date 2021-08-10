class Cells:
    def __init__(self, parts):
        self.parts = parts

    def __add__(self, other):
        return Cells(self.parts + other.parts)

    def _sub__(self, other):
        diff = self.parts - other.parts
        if diff >= 0:
            return Cells(diff)
        else:
            print('Ошибка вычитания')

    def __mul__(self, other):
        return Cells(self.parts * other.parts)

    def __truediv__(self, other):
        return Cells(self.parts // other.pa)

    def make_order(self, count):
        s = '*'
        for i in range(self.parts // count):
            s += '*' * count + '\n'
        s += '*' * (self.parts % count) + '\n'
        return s

    def __str__(self):
        return f'{self.parts}'


cell_1 = Cells(50)
print(cell_1.make_order(7))
cell_2 = Cells(35)
print(cell_2.make_order(4))

print(cell_1 - cell_2)
print(cell_1 + cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2 - cell_1)
