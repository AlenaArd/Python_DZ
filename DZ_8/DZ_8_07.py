class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_com(self, other):
        return self.a + other.a, self.b + self.b

    def mul_com(self, other):
        return self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a
    
    def complex_n(self):
        print(f'{self.a} + {self.b}*i')

    
    @classmethod
    def complex_num(cls):
        return cls.complex_n


com_num_1 = ComplexNum(1, 2)
print(com_num_1.complex_num)
print(com_num_1.complex_n)
