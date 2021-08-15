class Data:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def date_check(dd, mm, yy):
        count_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        result_date = None
        if 1900 <= yy <= 2300:
            if 0 < mm < 13:
                if dd <= count_day[mm - 1]:
                    result_date = True
                    pr = 'Дата корректна'
                else:
                    pr = 'Количество дней в месяце другое!'
            else:
                pr = 'Нет такого месяца!'
        else:
            pr = 'Год указан не верно!'
        return result_date, pr

    def number_type(self):
        if self.date_check(self.day, self.month, self.year)[0] is True:
            return f'{self.day:02}.{self.month:02}.{self.year}'
        else:
            return f'Дата {self.day:02}.{self.month:02}.{self.year} - НЕ корректна!!!'

    @classmethod
    def number_print(cls):
        return cls.number_type


date_1 = Data(1, 1, 2019)
date_2 = Data(31, 2, 2021)

print(date_1.date_check(1, 1, 2019))
print(date_2.date_check(31, 2, 2021))


print(date_1.number_type())
print(date_2.number_type())
print(date_2.number_print)
