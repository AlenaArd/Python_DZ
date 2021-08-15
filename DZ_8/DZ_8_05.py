#departments = {1: 0, 2: 0, 3: 0}

class OfficeEquipment:

    of_count = 0
    departments = {1: 0, 2: 0, 3: 0}



    def __init__(self, name, dep, number_of, intended_use=None):
        self.name = name
        self.dep = dep
        self.number_of = number_of
        self.intended_use = intended_use
        OfficeEquipment.of_count += number_of


    def reception(self):
        self.statist = {'name': self.name, 'dep': self.dep, 'number_of': self.number_of}
        return (self.statist)

    def dep(self):
        v = departments[self.statist['dep']] + self.statist['number_of']
        departments[self.statist['dep']] = v
        return (departments)


class Printer(OfficeEquipment):
    printer_count = 0

    def __init__(self, name, dep, number_of, intended_use=None):
        super(Printer, self).__init__(name, dep, intended_use)
        self.intended_use = 'for print'
        self.number_of = number_of
        Printer.printer_count += number_of


class Scanner(OfficeEquipment):
    scanner_count = 0

    def __init__(self, name, dep, number_of, intended_use=None):
        super(Scanner, self).__init__(name, dep, intended_use)
        self.number_of = number_of
        self.intended_use = 'for scan'
        Scanner.scanner_count += number_of


class Xerox(OfficeEquipment):
    xerox_count = 0

    def __init__(self, name, dep, number_of, intended_use=None):
        super(Xerox, self).__init__(name, dep, intended_use)
        self.number_of = number_of
        self.intended_use = 'for copy'
        Xerox.xerox_count += number_of


xerox_1 = Xerox('Hp_0123', 1, 5)
scaner_1 = Scanner('Epson_15', 1, 1)
printer_1 = Printer('Epson_23', 2, 2)

print(printer1.of_count)

