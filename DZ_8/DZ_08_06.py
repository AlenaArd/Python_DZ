class OfficeEquipment:
    of_count = 0
    departments = {1: 0, 2: 0, 3: 0}


    def __init__(self, name, dep, number):
        print('У нас новый экземпляр')
        self.name = name
        self.dep = dep
        self.number = number
        OfficeEquipment.of_count += number

    def reception(self):
        self.statist = {'name': self.name, 'dep': self.dep, 'number_of': self.number}
        departments.get(self.dep) += self.number
        return (departments)

xerox1 = OfficeEquipment('Hp_0123', 1, 5)
scaner1 = OfficeEquipment('Epson_15', 1, 1)
printer1 = OfficeEquipment('Epson_23', 2, 2)
print(printer1.of_count)
print(printer1.reception())

"""
xerox1.reception()
scaner1.reception()
printer1.reception()
"""
