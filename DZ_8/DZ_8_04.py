class OfficeEquipment:
    def __init__(self, name, dep, number_of):
        self.name = name
        self.dep = dep
        self.number_of = number_of


class Printer(OfficeEquipment):
    def __init__(self, name, dep, number_of, intended_use='for print'):
        super(Printer, self).__init__(name, dep, number_of)
        self.intended_use = intended_use


class Scanner(OfficeEquipment):
    def __init__(self, name, dep, number_of, intended_use='for scan'):
        super(Scanner, self).__init__(name, dep, number_of)
        self.intended_use = intended_use


class Xerox(OfficeEquipment):
    def __init__(self, name, dep, number_of, intended_use='for copy'):
        super(Xerox, self).__init__(name, dep, number_of)
        self.intended_use = intended_use
