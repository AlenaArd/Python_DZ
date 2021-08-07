class Worker:

    def __init__(self, name, surname, position, wage_rate, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage-rate': wage_rate, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return '{0} {1}'.format(self.name, self.surname)

    def get_total_income(self):
        return self._income['wage-rate'] + self._income['bonus']


co_worker_1 = Position('Alena', 'Ardyuk', 'Data Scientist', 100000, 10000)
co_worker_2 = Position('Max', 'Miller', 'Data Engineer', 105000, 10500)
print(co_worker_1.name, co_worker_2.name)
print(co_worker_1.surname, co_worker_2.surname)
print(co_worker_1.position, co_worker_2.position)
print(co_worker_1.get_full_name(), co_worker_2.get_full_name())
print(co_worker_1.get_total_income(), co_worker_2.get_total_income())
