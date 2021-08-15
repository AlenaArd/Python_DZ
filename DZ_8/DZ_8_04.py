class OfficeEquipment:
    def __init__(self, name, department, intended_use):
        self.name = name
        self.department = department
        self.intended_use = intended_use


class Printer(OfficeEquipment):
    def __init__(self, name, department, intended_use):
        super(Printer, self).__init__(name, department, intended_use)
        self.intended_use = 'for print'


class Scanner(OfficeEquipment):
    def __init__(self, name, department, intended_use):
        super(Scanner, self).__init__(name, department, intended_use)
        self.intended_use = 'for scan'


class Xerox(OfficeEquipment):
    def __init__(self, name, department, intended_use):
        super(Xerox, self).__init__(name, department, intended_use)
        self.intended_use = 'for copy'
