class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_com(self, other):
        return f'{self.a + other.a} + {self.b + other.b}*i'

    def mul_com(self, other):
        return f'{self.a * other.a - self.b * other.b} + {self.a * other.b + self.b * other.a}*i'
    
    def complex_n(self):
        return f'{self.a} + {self.b}*i'
    
    @classmethod
    def complex_num(cls):
        return cls.complex_n


com_num_1 = ComplexNum(1, 2)
com_num_2 = ComplexNum(2, 3)
print(com_num_1.complex_num)
print(com_num_1.complex_n)
print(com_num_1.add_com(com_num_2))
print(com_num_1.mul_com(com_num_2))
