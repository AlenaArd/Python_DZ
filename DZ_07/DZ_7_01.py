from random import randint


class Matrix:
    def __init__(self, strings):
        self.strings = strings

    def __str__(self):
        aj = ""
        for i in range(len(self.strings)):
            for j in range(len(self.strings[i])):
                aj += f'{self.strings[i][j]:02} '
            aj += '\n'
        return aj

    def __add__(self, other):
        strings = [
            [self.strings[i][j] + other.strings[i][j] for j in range(len(self.strings[i]))]
            for i in range(len(self.strings))]
        return Matrix(strings)


m1 = Matrix([[randint(0, 10) for _ in range(5)] for _ in range(3)])
m2 = Matrix([[randint(0, 10) for _ in range(5)] for _ in range(3)])
print(m1)
print(m2)
print(m1 + m2)
