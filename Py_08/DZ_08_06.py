class OfficeEquipment:
    of_count = 0
    dep_di = {1: 0, 2: 0, 3: 0}

    def __init__(self, name, dep, number):
        print('У нас новый экземпляр')
        self.name = name
        self.dep = dep
        self.number = number
        OfficeEquipment.of_count += number

    def reception(self):
        try:
            self.number == int(self.number)
        except TypeError:
            print('Введите целое положительное число!!!')
        self.statist = {'name': self.name, 'dep': self.dep, 'number_of': self.number}
        return self.statist

    def dep_dict(self):
        dep_di[self.dep] += self.number
        return dep_di


xerox1 = OfficeEquipment('Hp_0123', 1, 5)
scaner1 = OfficeEquipment('Epson_15', 3, 1)
printer1 = OfficeEquipment('Epson_23', 2, 2)
print(printer1.of_count)
print(printer1.reception)
print(printer1.dep_dict)
