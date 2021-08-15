class OfficeEquipment:
    of_count = 0
    departments = {1: 0, 2: 0, 3: 0}

    def __init__(self, name, dep, number_of):
        self.name = name
        self.dep = dep
        self.number_of = number_of
        OfficeEquipment.of_count += number_of

    def reception(self):
        statist = {'name': self.name, 'dep': self.dep, 'number_of': self.number_of}
        return statist

    def dep(self):
        v = departments[self.statist['dep']] + self.statist['number_of']
        departments[self.statist['dep']] = v
        return departments
        

class Printer(OfficeEquipment):
    printer_count = 0

    def __init__(self, name, dep, number_of, intended_use='for print'):
        super(Printer, self).__init__(name, dep, number_of)
        self.intended_use = intended_use
        Printer.printer_count += number_of


class Scanner(OfficeEquipment):
    scanner_count = 0

    def __init__(self, name, dep, number_of, intended_use='for scan'):
        super(Scanner, self).__init__(name, dep, number_of)
        self.intended_use = intended_use
        Scanner.scanner_count += number_of


class Xerox(OfficeEquipment):
    xerox_count = 0

    def __init__(self, name, dep, number_of, intended_use='for copy'):
        super(Xerox, self).__init__(name, dep, number_of)
        self.intended_use = intended_use
        Xerox.xerox_count += number_of
       

xerox_1 = Xerox('Hp_0123', 1, 5)
scanner_1 = Scanner('Epson_15', 1, 1)
printer_1 = Printer('Epson_23', 2, 2)

print(printer_1.printer_count)
print(scanner_1.of_count)
print(scanner_1.scanner_count)
print(printer_1.reception())
print(xerox_1 .reception())
